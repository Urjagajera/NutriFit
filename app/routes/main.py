from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.models import User, Profile, WaterLog, WeightLog, DietPlan, WorkoutLink
from app.extensions import db
from functools import wraps

main_bp = Blueprint('main', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


@main_bp.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('main.user_home'))
    return render_template('index.html')

@main_bp.route('/home')
@login_required
def user_home():
    user = User.query.get(session['user_id'])
    
    # Redirect if basic choice not made
    if not user.focus:
        return redirect(url_for('main.select_focus'))
    
    # If no profile, we can still show the page but with a message
    return render_template('home.html', user=user, profile=user.profile)


@main_bp.route('/select-focus', methods=['GET', 'POST'])
@login_required
def select_focus():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        focus = request.form.get('focus')
        user.focus = focus
        db.session.commit()
        return redirect(url_for('main.quiz'))
        
    return render_template('select_focus.html')

@main_bp.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        try:
            age = int(request.form.get('age'))
            gender = request.form.get('gender')
            height = float(request.form.get('height'))
            weight = float(request.form.get('weight'))
            primary_goal = request.form.get('primary_goal')
            food_habit = request.form.get('food_habit')
            allergies = request.form.get('allergies')
            sleep_hours = float(request.form.get('sleep_hours'))
            medical_conditions = request.form.get('medical_conditions')
            commitment_level = request.form.get('commitment_level')
            
            profile = Profile.query.filter_by(user_id=user.id).first()
            if not profile:
                profile = Profile(user_id=user.id)
                db.session.add(profile)
                
            profile.age = age
            profile.gender = gender
            profile.height = height
            profile.weight = weight
            profile.primary_goal = primary_goal
            profile.food_habit = food_habit
            profile.allergies = allergies
            profile.sleep_hours = sleep_hours
            profile.medical_conditions = medical_conditions
            profile.commitment_level = commitment_level
            
            profile.calculate_metrics()
            db.session.commit()
            
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('main.dashboard'))
            
        except (ValueError, TypeError) as e:
            db.session.rollback()
            flash('Invalid data submitted. Please check your entries.', 'danger')
        except Exception as e:
            db.session.rollback()
            flash('An unexpected error occurred. Please try again.', 'danger')
            
    return render_template('quiz.html', user=user, profile=user.profile)
        
from datetime import date

@main_bp.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    # Redirect if profile not complete
    if not user.focus:
        return redirect(url_for('main.select_focus'))
    if not user.profile:
        return redirect(url_for('main.quiz'))
        
    # Handle Water Log (Daily Reset Logic)
    today = date.today()
    water_log = WaterLog.query.filter_by(user_id=user.id, date=today).first()
    
    if not water_log:
        # Calculate daily target based on weight (standard: 35ml per kg)
        # or use default 2000ml if profile is weird
        target = (user.profile.weight * 35) if user.profile.weight else 2000
        water_log = WaterLog(user_id=user.id, date=today, goal=round(target, 0))
        db.session.add(water_log)
        db.session.commit()
        
    # Fetch assigned plans (Versioned)
    diet_plans = user.diet_plans.order_by(DietPlan.upload_date.desc()).all()
    latest_diet = diet_plans[0] if diet_plans else None
    previous_diets = diet_plans[1:] if len(diet_plans) > 1 else []
    
    latest_workout = user.workout_links.order_by(WorkoutLink.upload_date.desc()).first()
    
    water_percent = (water_log.consumed / water_log.goal * 100) if water_log.goal > 0 else 0
    
    return render_template('dashboard.html', 
                           user=user, 
                           profile=user.profile, 
                           water=water_log,
                           water_percent=water_percent,
                           diet=latest_diet,
                           previous_diets=previous_diets,
                           workout=latest_workout)


from datetime import date, timedelta
import json

@main_bp.route('/reports')
@login_required
def reports():
    user = User.query.get(session['user_id'])
    
    # 1. Water Consumption Data (Last 7 Days)
    today = date.today()
    water_data = []
    water_labels = []
    
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        log = WaterLog.query.filter_by(user_id=user.id, date=day).first()
        water_labels.append(day.strftime('%b %d'))
        water_data.append(log.consumed if log else 0)
        
    # 2. Weight Progress Data
    weights = WeightLog.query.filter_by(user_id=user.id).order_by(WeightLog.date.asc()).all()
    weight_labels = [w.date.strftime('%b %d') for w in weights]
    weight_values = [w.weight for w in weights]
    
    # If no weighted logs, use the initial profile weight
    if not weights and user.profile:
        weight_labels = ['Initial']
        weight_values = [user.profile.weight]

    return render_template('reports.html', 
                           water_labels=water_labels,
                           water_values=water_data,
                           weight_labels=weight_labels,
                           weight_values=weight_values)


@main_bp.route('/log-weight', methods=['POST'])
@login_required
def log_weight():
    user = User.query.get(session['user_id'])
    new_weight = float(request.form.get('weight'))
    
    # Add to historical logs
    log = WeightLog(user_id=user.id, weight=new_weight)
    db.session.add(log)
    
    # Update current profile weight
    if user.profile:
        user.profile.weight = new_weight
        user.profile.calculate_metrics()
            
    db.session.commit()
    flash('Weight progress logged successfully!', 'success')
    return redirect(url_for('main.reports'))

@main_bp.route('/update-water', methods=['POST'])
@login_required
def update_water():
    user_id = session['user_id']
    amount = float(request.form.get('amount', 250))
    today = date.today()
    water_log = WaterLog.query.filter_by(user_id=user_id, date=today).first()
    
    if not water_log:
        # Fallback if session is old and crosses midnight
        user = User.query.get(user_id)
        target = (user.profile.weight * 35) if user.profile and user.profile.weight else 2000
        water_log = WaterLog(user_id=user_id, date=today, goal=round(target, 0))
        db.session.add(water_log)
        
    water_log.consumed += amount
    db.session.commit()
    flash(f'Added {amount}ml of water!', 'success')
    return redirect(url_for('main.dashboard'))



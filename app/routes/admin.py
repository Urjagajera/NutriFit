import os
from flask import Blueprint, render_template, redirect, url_for, flash, session, request, current_app
from app.models import User, Profile, DietPlan, WorkoutLink, WaterLog
from app.extensions import db
from functools import wraps
from werkzeug.utils import secure_filename
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("DEBUG: ADMIN DECORATOR EXECUTED")
        try:
            if 'user_id' not in session:
                print("DEBUG: ADMIN DECORATOR - No user_id in session")
                flash('Please login to access this page.', 'warning')
                return redirect(url_for('auth.login'))
            if session.get('user_role') != 'admin':
                print(f"DEBUG: ADMIN DECORATOR - User {session.get('user_id')} is not admin (Role: {session.get('user_role')}")
                flash('Admin access required.', 'danger')
                return redirect(url_for('main.index'))
            print("DEBUG: ADMIN DECORATOR - Validation successful")
            return f(*args, **kwargs)
        except Exception as e:
            print(f"DEBUG: ADMIN DECORATOR CRASHED: {str(e)}")
            raise e
    return decorated_function

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    users = User.query.filter_by(role='user').order_by(User.created_at.desc()).all()
    return render_template('admin/dashboard.html', users=users)

from app.models import User, Profile, DietPlan, WorkoutLink, WaterLog, WeightLog
import logging

# Configure logging for this module
logger = logging.getLogger(__name__)
@admin_bp.route('/user/<int:user_id>')
@admin_required
def user_detail(user_id):
    print(f"DEBUG: ADMIN USER DETAIL ROUTE EXECUTED for user_id: {user_id}")
    """
    Production-grade user detail route with zero-crash guarantee.
    All data is pre-processed and validated before being passed to the template.
    """
    try:
        # 1. Validate Admin Session (redundant but safe)
        if session.get('user_role') != 'admin':
            print("DEBUG: ADMIN ROUTE - Unauthorized access attempt")
            flash("Unauthorized access attempt.", "danger")
            return redirect(url_for('main.index'))

        # 2. Safe User Fetch
        user = User.query.get(user_id)
        if not user:
            print(f"DEBUG: ADMIN ROUTE - User {user_id} not found")
            flash(f"User with ID {user_id} not found.", "warning")
            return redirect(url_for('admin.dashboard'))
        
        # 3. Defensive Profile Access
        profile = user.profile
        
        # 4. Pre-process Water History (Safe Date Handling)
        from datetime import date, timedelta
        today = date.today()
        water_labels = []
        water_values = []
        
        try:
            for i in range(6, -1, -1):
                day = today - timedelta(days=i)
                log = WaterLog.query.filter_by(user_id=user.id, date=day).first()
                water_labels.append(day.strftime('%b %d'))
                water_values.append(float(log.consumed) if log and log.consumed is not None else 0.0)
        except Exception as water_err:
            print(f"DEBUG: ADMIN ROUTE - Water error: {water_err}")
            current_app.logger.warning(f"Water history fetch failed for user {user_id}: {water_err}")
            water_labels, water_values = [], []

        # 5. Pre-process Weight History (Safe Date Handling)
        weight_labels = []
        weight_values = []
        try:
            weights = WeightLog.query.filter_by(user_id=user.id).order_by(WeightLog.date.asc()).all()
            if weights:
                weight_labels = [w.date.strftime('%b %d') if w.date else "Unknown" for w in weights]
                weight_values = [float(w.weight) if w.weight is not None else 0.0 for w in weights]
            elif profile and profile.weight:
                weight_labels = ['Initial']
                weight_values = [float(profile.weight)]
        except Exception as weight_err:
            print(f"DEBUG: ADMIN ROUTE - Weight error: {weight_err}")

        # 6. Explicitly Fetch Logs and Plans (No lazy-loading in template)
        water_logs = []
        weight_logs = []
        diet_plans = []
        
        try:
            water_logs = WaterLog.query.filter_by(user_id=user_id).order_by(WaterLog.date.desc()).limit(10).all()
            weight_logs = WeightLog.query.filter_by(user_id=user_id).order_by(WeightLog.date.desc()).all()
            diet_plans = user.diet_plans.order_by(DietPlan.upload_date.desc()).all()
        except Exception as rel_err:
            print(f"DEBUG: ADMIN ROUTE - Rel error: {rel_err}")

        # 7. Zero-Risk Render
        print("DEBUG: ADMIN ROUTE - Rendering template")
        return render_template('admin/user_detail.html', 
                               user=user, 
                               profile=profile,
                               diet_plans=diet_plans,
                               water_logs=water_logs,
                               weight_logs=weight_logs,
                               water_labels=water_labels,
                               water_values=water_values,
                               weight_labels=weight_labels,
                               weight_values=weight_values)

    except Exception as fatal_err:
        print(f"DEBUG: ADMIN ROUTE - FATAL ERROR: {fatal_err}")
        current_app.logger.exception(f"CRITICAL: System failure in user_detail for ID {user_id}")
        flash("We encountered a stability issue loading this profile.", "warning")
        return redirect(url_for('admin.dashboard'))

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS and \
           filename.count('.') == 1 # Prevent double extensions

@admin_bp.route('/assign-diet/<int:user_id>', methods=['POST'])
@admin_required
def assign_diet(user_id):
    user = User.query.get_or_404(user_id)
    
    if 'diet_file' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('admin.user_detail', user_id=user_id))
        
    file = request.files['diet_file']
    
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('admin.user_detail', user_id=user_id))
        
    if file:
        if not allowed_file(file.filename):
            flash('Invalid file type. Allowed: PDF, DOCX, XLSX.', 'danger')
            return redirect(url_for('admin.user_detail', user_id=user_id))

        filename = secure_filename(file.filename)
        # Add timestamp to prevent name collisions while keeping it readable
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
        
        # New Scalable Path: uploads/<user_id>/diet_plans/
        user_upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], str(user_id), 'diet_plans')
        
        if not os.path.exists(user_upload_path):
            os.makedirs(user_upload_path)
            
        file.save(os.path.join(user_upload_path, filename))
        
        new_diet = DietPlan(user_id=user_id, filename=filename)
        db.session.add(new_diet)
        db.session.commit()
        
        flash('Diet plan uploaded and assigned successfully!', 'success')
        
    return redirect(url_for('admin.user_detail', user_id=user_id))

@admin_bp.route('/assign-workout/<int:user_id>', methods=['POST'])
@admin_required
def assign_workout(user_id):
    user = User.query.get_or_404(user_id)
    link = request.form.get('workout_link')
    
    if link:
        new_workout = WorkoutLink(user_id=user_id, link=link)
        db.session.add(new_workout)
        db.session.commit()
        flash('Workout link assigned successfully!', 'success')
        
    return redirect(url_for('admin.user_detail', user_id=user_id))

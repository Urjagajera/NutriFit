from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.models import User, Profile
from app.extensions import db
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('auth.register'))
            
        # Check if user already exists
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('Email address already registered.', 'danger')
            return redirect(url_for('auth.register'))
            
        # Create new user
        new_user = User(full_name=full_name, email=email)
        new_user.set_password(password)
        
        # Check if this is the first user, and if so, make them an admin
        if User.query.count() == 0:
            new_user.role = 'admin'
            
        try:
            db.session.add(new_user)
            db.session.flush() # Get user.id
            
            # Auto-create profile
            profile = Profile(user_id=new_user.id)
            db.session.add(profile)
            
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
        except IntegrityError:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'danger')
            
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['user_role'] = user.role
            flash(f'Welcome back, {user.full_name}!', 'success')
            
            if user.role == 'admin':
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('main.user_home'))
            
        flash('Invalid email or password.', 'danger')
        
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

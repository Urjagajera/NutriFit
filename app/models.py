from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # 'user' or 'admin'
    focus = db.Column(db.String(50))  # 'diet', 'workout', or 'both'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to profile
    profile = db.relationship('Profile', backref='user', uselist=False, cascade="all, delete-orphan")
    water_logs = db.relationship('WaterLog', backref='user', lazy='dynamic', cascade="all, delete-orphan")
    weight_logs = db.relationship('WeightLog', backref='user', lazy='dynamic', cascade="all, delete-orphan")
    diet_plans = db.relationship('DietPlan', backref='user', lazy='dynamic', cascade="all, delete-orphan")
    workout_links = db.relationship('WorkoutLink', backref='user', lazy='dynamic', cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    height = db.Column(db.Float)  # in cm
    weight = db.Column(db.Float)  # in kg
    primary_goal = db.Column(db.String(100))
    food_habit = db.Column(db.String(100))
    allergies = db.Column(db.Text)
    sleep_hours = db.Column(db.Float)
    medical_conditions = db.Column(db.Text)
    commitment_level = db.Column(db.String(50))
    bmi = db.Column(db.Float)
    bmr = db.Column(db.Float)

    @property
    def bmi_category(self):
        if not self.bmi:
            return "Unknown"
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def calculate_metrics(self):
        """Centralized calculation of BMI and BMR"""
        if not self.height or not self.weight or not self.age or not self.gender:
            return
            
        # BMI Calculation
        height_m = self.height / 100
        self.bmi = round(self.weight / (height_m ** 2), 2)
        
        # BMR Calculation (Mifflin-St Jeor)
        if self.gender == 'male':
            self.bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            self.bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161

class WaterLog(db.Model):
    __tablename__ = 'water_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    goal = db.Column(db.Float, default=2000)  # in ml
    consumed = db.Column(db.Float, default=0)

class DietPlan(db.Model):
    __tablename__ = 'diet_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

class WorkoutLink(db.Model):
    __tablename__ = 'workout_links'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

class WeightLog(db.Model):
    __tablename__ = 'weight_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    weight = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow().date, index=True)

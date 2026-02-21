from app import create_app
from app.extensions import db
import time

app = create_app()

# Explicitly import all models to ensure they are registered with SQLAlchemy metadata
from app.models import User, Profile, WaterLog, WeightLog, DietPlan, WorkoutLink

with app.app_context():
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI'].split('@')[-1]}") # Redacted URI for security
    print(f"Registered models: {db.metadata.tables.keys()}")
    print("Initializing database...")
    try:
        db.create_all()
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
        print("Note: Make sure your MySQL server is running and the database 'nutrifit_db' exists.")

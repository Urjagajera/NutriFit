import traceback
from app import create_app
from flask import render_template
from app.models import User, Profile, DietPlan

app = create_app()

with app.app_context():
    with app.test_request_context():
        # Create a dummy user and profile
        user = User(full_name="Audit Tester", email="audit@test.com")
        user.id = 1
        profile = Profile(age=30, gender="male", height=175, weight=80, 
                          primary_goal="muscle_gain", commitment_level="high")
        user.profile = profile
        
        # Test Case 1: Healthy context
        print("--- Testing admin/user_detail.html (Healthy Context) ---")
        diet_plans = [
            DietPlan(filename="plan1.pdf"),
            DietPlan(filename="plan2.pdf")
        ]
        try:
            html = render_template('admin/user_detail.html', 
                                   user=user, 
                                   profile=profile,
                                   diet_plans=diet_plans,
                                   water_labels=['Feb 20', 'Feb 21'], 
                                   water_values=[1500, 2000],
                                   weight_labels=['Initial'], 
                                   weight_values=[80.0])
            print("SUCCESS: Admin User Detail page rendered correctly.")
        except Exception:
            print("FAILURE: Admin User Detail page failed to render.")
            traceback.print_exc()

        # Test Case 2: No Profile context
        print("\n--- Testing admin/user_detail.html (No Profile Context) ---")
        try:
            html = render_template('admin/user_detail.html', 
                                   user=user, 
                                   profile=None,
                                   diet_plans=[],
                                   water_labels=[], 
                                   water_values=[],
                                   weight_labels=[], 
                                   weight_values=[])
            print("SUCCESS: Admin User Detail rendered safely without profile.")
        except Exception:
            print("FAILURE: Admin User Detail crashed on missing profile.")
            traceback.print_exc()

        # Test Case 3: Verify home.html safety
        print("\n--- Testing home.html ---")
        try:
            html = render_template('home.html', user=user, profile=profile)
            print("SUCCESS: Home page rendered correctly.")
        except Exception:
            print("FAILURE: Home page failed to render.")
            traceback.print_exc()

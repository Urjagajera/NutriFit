# NutriFit

## 1. PROJECT OVERVIEW
NutriFit is a personalized health and fitness web application. It allows users to register, log in, complete a health profile, and track their daily water intake and weight progression over time. The application also provides an administrative interface for staff to review user profiles and securely upload personalized diet plans and workout links.

## 2. TECH STACK
- **Core Framework**: Flask (3.0.0)
- **Database ORM**: Flask-SQLAlchemy (3.1.1)
- **Database Driver**: PyMySQL (1.1.0)
- **Forms & CSRF**: Flask-WTF (1.2.2)
- **Environment Management**: python-dotenv (1.0.0)
- **WSGI Server**: Werkzeug (3.0.1) & Gunicorn (21.2.0)
- **Cryptography**: cryptography (50.0.1)

## 3. SETUP INSTRUCTIONS
Follow these steps to run the application locally.

**1. Clone the repository and navigate into the directory:**
```bash
git clone https://github.com/Urjagajera/NutriFit
cd NutriFit
```

**2. Set up the virtual environment:**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Database Configuration:**
Ensure you have a local MySQL server running.
Create a database named `nutrifit_db`.
Create a `.env` file in the root directory (or use the existing one) with the following content (update the password and credentials as needed):
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/nutrifit_db
FLASK_ENV=development
```

**5. Initialize the Database:**
Run the database creation script to generate all necessary tables based on the SQLAlchemy models:
```bash
python create_db.py
```

**6. Start the Development Server:**
Start the application using the runner script:
```bash
python run.py
```
Access the application at `http://127.0.0.1:5000/`.

## 4. FEATURES
- **User Authentication**: Secure user registration, login, and logout.
- **Profile Generation**: Collection of user age, gender, height, and goals.
- **Metrics Calculation**: Automatic generation of Body Mass Index (BMI) and Basal Metabolic Rate (BMR) based on the Mifflin-St Jeor equation.
- **Water Tracking**: Daily water logging functionality.
- **Weight Logging**: Historical weight progress tracking.
- **Admin Dashboard**: Administrator views for managing users, assigning `.pdf`, `.docx`, or `.xlsx` diet plans, and assigning workout links.

## 5. PROJECT STRUCTURE
```
NutriFit/
├── app/
│   ├── models.py       # SQLAlchemy database models (User, Profile, WaterLog, DietPlan, etc.)
│   ├── routes/         # Application routing blueprints
│   │   ├── admin.py    # Admin-specific routes and file upload logic
│   │   ├── auth.py     # Login and registration routes
│   │   └── main.py     # Core user dashboard and logging routes
│   ├── templates/      # HTML templates (Jinja2) for the frontend views
│   └── static/         # CSS, images, and user file uploads
├── config.py           # Application configuration and environment loading
├── create_db.py        # Database initialization script
├── requirements.txt    # Python dependencies
└── run.py              # Application entry point
```

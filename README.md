# 🥗 NutriFit — Personalized Health & Fitness Management Platform

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Chart.js](https://img.shields.io/badge/Chart.js-Data%20Visualization-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](LICENSE)

---

## 📖 Table of Contents

1. [Project Overview](#-1-project-overview)
2. [Key Features](#-2-key-features)
   - [User Features](#user-features)
   - [Admin Features](#admin-features)
3. [Technology Stack](#-3-technology-stack)
4. [System Architecture](#-4-system-architecture)
5. [Prerequisites for PC](#-5-prerequisites-for-pc)
6. [Step-by-Step Installation & Setup on PC (Windows)](#-6-step-by-step-installation--setup-on-pc-windows)
   - [Step 1: Clone or Download the Repository](#step-1-clone-or-download-the-repository)
   - [Step 2: Open Terminal in Project Directory](#step-2-open-terminal-in-project-directory)
   - [Step 3: Create a Python Virtual Environment](#step-3-create-a-python-virtual-environment)
   - [Step 4: Activate the Virtual Environment](#step-4-activate-the-virtual-environment)
   - [Step 5: Upgrade pip and Install Dependencies](#step-5-upgrade-pip-and-install-dependencies)
   - [Step 6: Set Up MySQL Database on PC](#step-6-set-up-mysql-database-on-pc)
   - [Step 7: Configure Environment Variables (.env)](#step-7-configure-environment-variables-env)
   - [Step 8: Initialize Database Tables](#step-8-initialize-database-tables)
   - [Step 9: Launch the Application](#step-9-launch-the-application)
   - [Step 10: Access and Create the First Admin Account](#step-10-access-and-create-the-first-admin-account)
7. [Running on macOS / Linux](#-7-running-on-macos--linux)
8. [Project Structure](#-8-project-structure)
9. [Database Schema & Models](#-9-database-schema--models)
10. [Health Calculations & Algorithms](#-10-health-calculations--algorithms)
11. [Testing & Verification](#-11-testing--verification)
12. [Troubleshooting & Common PC Issues](#-12-troubleshooting--common-pc-issues)
13. [Security Notes & Production Readiness](#-13-security-notes--production-readiness)
14. [License & Acknowledgements](#-14-license--acknowledgements)

---

## 🌟 1. Project Overview

**NutriFit** is a full-featured, secure, and personalized health and wellness web application designed to bridge the gap between clients and fitness professionals. 

Clients can easily register, complete a comprehensive health questionnaire, monitor their daily hydration intake against personalized targets, log historical weight data, view interactive trend analytics, and download customized diet plans or access workout routines prescribed directly by administrators.

Administrators have access to a dedicated management dashboard allowing them to inspect user profiles, review individual fitness metrics, upload personalized meal plans (`.pdf`, `.docx`, `.xlsx`), and assign targeted workout resources.

---

## 🚀 2. Key Features

### User Features
* **Secure Authentication**: User registration, login, and session persistence protected by PBKDF2 SHA-256 password hashing.
* **Automatic First-User Admin Bootstrap**: The very first user to register on a fresh database is automatically designated as the system **Admin**. All subsequent registrations receive standard user roles.
* **Focus Selection**: Tailor the journey by selecting focus areas: *Diet*, *Workout*, or *Both*.
* **Comprehensive Health Onboarding Quiz**:
  - Collects age, gender, height (cm), weight (kg), primary fitness goals, food habits, allergies, daily sleep duration, medical conditions, and commitment level.
* **Automated Health Metrics Engine**:
  - **Body Mass Index (BMI)** calculation and classification (`Underweight`, `Normal`, `Overweight`, `Obese`).
  - **Basal Metabolic Rate (BMR)** calculation using the scientifically validated **Mifflin-St Jeor Equation**.
* **Smart Daily Hydration Tracker**:
  - Automatically computes daily water target based on body weight ($35\text{ ml per kg}$).
  - Daily log auto-initialization and date-tracking reset.
  - One-click hydration logger ($+250\text{ ml}$ increments).
  - Dynamic visual hydration progress percentage bar.
* **Weight Progress Logging**:
  - Record ongoing weigh-ins to track weight loss or muscle gain over time.
  - Dynamically recalculates current BMI and BMR upon weight change.
* **Visual Analytics & Reporting**:
  - Interactive **7-Day Water Consumption Chart** powered by **Chart.js**.
  - Historical **Weight Trend Line Chart** tracking progress against the initial profile weight.
* **Prescribed Diet Plan Downloads**:
  - Direct download access to customized nutrition plans uploaded by the coach (`.pdf`, `.docx`, `.xlsx`).
* **Assigned Workout Routines**:
  - Direct links to customized exercise playlists and workout guides assigned by the coach.

### Admin Features
* **Role-Based Admin Portal** (`/admin/dashboard`):
  - Accessible exclusively to users with `role='admin'` via `@admin_required` route decorators.
* **Client Overview**:
  - View all registered clients, their registration dates, and chosen focus.
* **In-Depth Client Profile Inspection** (`/admin/user/<id>`):
  - Review client health quiz answers, medical history, dietary restrictions, and allergies.
  - Review live BMI and BMR calculations.
  - Inspect 7-day hydration logs and complete weight history.
  - View assigned diet plans and workout links.
* **Secure Diet Plan Management**:
  - Upload user-specific meal plans (`.pdf`, `.docx`, `.xlsx`).
  - Secure filename sanitization, double-extension injection defense, and timestamp collision prevention.
  - User-isolated storage structure (`static/uploads/<user_id>/diet_plans/`).
* **Workout Link Assignment**:
  - Dispatch custom workout video URLs and routine links directly to any user.

---

## 🛠️ 3. Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend Framework** | [Flask 3.0.0](https://flask.palletsprojects.com/) (Python 3.10+) |
| **Database ORM** | [Flask-SQLAlchemy 3.1.1](https://flask-sqlalchemy.palletsprojects.com/) |
| **Database Driver** | [PyMySQL 1.1.0](https://pymysql.readthedocs.io/) with [cryptography 50.0.1](https://cryptography.io/) |
| **Database Engine** | [MySQL 8.0+](https://www.mysql.com/) |
| **Form Handling & Security** | [Flask-WTF 1.2.2](https://flask-wtf.readthedocs.io/) (CSRF Protection), [Werkzeug 3.0.1](https://werkzeug.palletsprojects.com/) |
| **Session Management** | Flask Session with HTTP-only cookies |
| **Environment Config** | [python-dotenv 1.0.0](https://github.com/theskumar/python-dotenv) |
| **WSGI Servers** | Werkzeug Built-in Server (Dev), [Gunicorn 21.2.0](https://gunicorn.org/) (Linux Prod) |
| **Frontend Technologies** | HTML5 (Semantic), Vanilla CSS3 (Custom Design System), JavaScript (ES6) |
| **Data Visualization** | [Chart.js](https://www.chartjs.org/) |
| **Typography** | Google Fonts (*Montserrat*, *Playfair Display*) |

---

## 🏗️ 4. System Architecture

NutriFit is architected using the **Application Factory Pattern** (`create_app`) and modular **Flask Blueprints**, ensuring clear separation of concerns, testability, and scalability:

```
                      +-----------------------------+
                      |         Browser / UI        |
                      +--------------+--------------+
                                     | HTTP Requests (with CSRF Tokens)
                                     v
+------------------------------------+------------------------------------+
|                         Flask Application Core                         |
|                                                                         |
|  +--------------------+  +--------------------+  +--------------------+ |
|  |     auth_bp        |  |      main_bp       |  |      admin_bp      | |
|  |  /auth/register    |  |  /home, /dashboard |  |  /admin/dashboard  | |
|  |  /auth/login       |  |  /quiz, /reports   |  |  /admin/user/<id>  | |
|  |  /auth/logout      |  |  /log-weight       |  |  /assign-diet      | |
|  |                    |  |  /update-water     |  |  /assign-workout   | |
|  +---------+----------+  +---------+----------+  +---------+----------+ |
|            |                       |                       |            |
|            +-----------------------+-----------------------+            |
|                                    |                                    |
|                                    v                                    |
|                       SQLAlchemy ORM (models.py)                        |
|             (User, Profile, WaterLog, WeightLog, DietPlan)              |
+------------------------------------+------------------------------------+
                                     | PyMySQL Connection
                                     v
                      +-----------------------------+
                      |   MySQL Relational Database |
                      |       (nutrifit_db)         |
                      +-----------------------------+
```

---

## 💻 5. Prerequisites for PC

Before running the application on your PC, make sure you have the following software installed:

1. **Operating System**: Windows 10 or Windows 11 (64-bit recommended), macOS, or Linux.
2. **Python 3.10 or Higher**:
   - Download from [python.org](https://www.python.org/downloads/).
   - ⚠️ **Important on Windows**: During installation, make sure to check the box **"Add python.exe to PATH"**.
3. **MySQL Server 8.0 or Higher**:
   - You can install **MySQL Community Server** from [MySQL Downloads](https://dev.mysql.com/downloads/mysql/), OR
   - Install **XAMPP** from [apachefriends.org](https://www.apachefriends.org/) (which includes MySQL/MariaDB), OR
   - Install **WampServer**.
4. **Git** (Optional, for cloning):
   - Download from [git-scm.com](https://git-scm.com/).
5. **A Modern Web Browser**: Google Chrome, Microsoft Edge, Mozilla Firefox, or Brave.

---

## 🖥️ 6. Step-by-Step Installation & Setup on PC (Windows)

Follow these detailed steps to set up and run NutriFit on your Windows PC.

---

### Step 1: Clone or Download the Repository

#### Option A: Using Git (Recommended)
Open **PowerShell** or **Command Prompt** and run:
```bash
git clone https://github.com/Urjagajera/NutriFit.git
cd NutriFit
```

#### Option B: Download as ZIP
1. Download the ZIP file from GitHub.
2. Extract the folder to your preferred location (for example, `C:\Users\<YourUsername>\Desktop\NutriFit`).
3. Open the extracted `NutriFit` folder.

---

### Step 2: Open Terminal in Project Directory

Open **Windows PowerShell** or **Command Prompt** and navigate to your project folder:
```powershell
cd "C:\Users\<YourUsername>\Desktop\NutriFit"
```
*(Verify you are in the directory containing `run.py`, `requirements.txt`, and `config.py` by typing `dir`)*.

---

### Step 3: Create a Python Virtual Environment

Creating an isolated virtual environment ensures project dependencies do not conflict with other Python packages installed on your system.

Run the following command:
```powershell
python -m venv venv
```
This creates a `venv` folder containing a dedicated Python executable and `pip`.

---

### Step 4: Activate the Virtual Environment

Activate the virtual environment using PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

Or, if you are using standard **Command Prompt (CMD)**:
```cmd
venv\Scripts\activate.bat
```

> [!TIP]
> **PowerShell Execution Policy Fix**:
> If PowerShell gives the error `running scripts is disabled on this system`, run this one-time command in your current PowerShell window:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> .\venv\Scripts\Activate.ps1
> ```
> When activated, your prompt will show `(venv)` at the beginning of the line:
> ```text
> (venv) PS C:\Users\...\NutriFit>
> ```

---

### Step 5: Upgrade pip and Install Dependencies

Ensure `pip` is up to date and install all required packages listed in `requirements.txt`:
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
* `Flask 3.0.0`
* `Flask-Login 0.6.3`
* `Flask-SQLAlchemy 3.1.1`
* `Flask-WTF 1.2.2`
* `python-dotenv 1.0.0`
* `PyMySQL 1.1.0`
* `cryptography 50.0.1`
* `Werkzeug 3.0.1`
* `gunicorn 21.2.0`

---

### Step 6: Set Up MySQL Database on PC

#### 1. Ensure MySQL Server is Running:
* **If using MySQL Community Server**: Check that the MySQL Windows service is running (Open **Task Manager** > **Services** > `MySQL80` should be **Running**).
* **If using XAMPP**: Open **XAMPP Control Panel** and click **Start** next to **MySQL** (the port indicator should turn green and show `3306`).

#### 2. Create the Database `nutrifit_db`:
Open your **MySQL Command Line Client** or use PowerShell/CMD:
```powershell
mysql -u root -p
```
Enter your MySQL root password when prompted. Then run:
```sql
CREATE DATABASE IF NOT EXISTS nutrifit_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW DATABASES;
EXIT;
```

---

### Step 7: Configure Environment Variables (`.env`)

In the root of the `NutriFit` folder, you will find a `.env.example` file. Create your local `.env` file from it:

#### In PowerShell:
```powershell
Copy-Item .env.example .env
```

#### Edit the `.env` file:
Open `.env` in Notepad or your favorite text editor (e.g. VS Code, Notepad++):
```powershell
notepad .env
```

Set your configuration values:
```env
# A strong random secret key for Flask session encryption
SECRET_KEY=replace_with_a_random_secure_hex_key

# MySQL Connection String:
# mysql+pymysql://<user>:<password>@<host>:<port>/<dbname>
DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/nutrifit_db

# Flask Environment Mode
FLASK_ENV=development
```

> [!IMPORTANT]
> **Password URL Encoding Note**:
> If your MySQL password contains special symbols (such as `@`, `:`, `/`, `#`, `%`, or `,`), you **must** URL-encode them in the `DATABASE_URL` connection string:
> * `@` $\rightarrow$ `%40`
> * `,` $\rightarrow$ `%2C`
> * `#` $\rightarrow$ `%23`
> * `:` $\rightarrow$ `%3A`
> * `/` $\rightarrow$ `%2F`
> 
> *Example*: If your password is `MyPass@123`, use:
> `DATABASE_URL=mysql+pymysql://root:MyPass%40123@localhost:3306/nutrifit_db`

To generate a secure random `SECRET_KEY`, you can run:
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

---

### Step 8: Initialize Database Tables

Run the database setup script to generate all required tables (`users`, `profiles`, `water_logs`, `weight_logs`, `diet_plans`, `workout_links`):

```powershell
python create_db.py
```

#### Expected Output:
```text
Database URI: localhost:3306/nutrifit_db
Registered models: dict_keys(['users', 'profiles', 'water_logs', 'weight_logs', 'diet_plans', 'workout_links'])
Initializing database...
Tables created successfully.
```

---

### Step 9: Launch the Application

Start the local Flask development server:
```powershell
python run.py
```

#### Expected Output:
```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

Open your web browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)** (or `http://localhost:5000`)

---

### Step 10: Access and Create the First Admin Account

1. Click on **Join Now** in the top navigation bar or go to `http://127.0.0.1:5000/auth/register`.
2. Fill in your name, email, and password.
3. 🌟 **Admin Privilege Bootstrap**:
   - Because this is the **first account created** in your database, NutriFit will automatically assign this user the role of **`admin`**!
   - When you log in with this account, you will be automatically directed to the **Admin Dashboard** (`/admin/dashboard`).
4. To test a regular client user:
   - Log out from the admin account.
   - Register a second account (`user2@example.com`).
   - This account will be created with the standard **`user`** role and will proceed to the Focus Selection and Health Quiz onboarding flow!

---

## 🍏 7. Running on macOS / Linux

For macOS or Linux users, the setup steps are nearly identical:

```bash
# 1. Clone repository
git clone https://github.com/Urjagajera/NutriFit.git
cd NutriFit

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Copy .env and configure
cp .env.example .env
nano .env

# 5. Initialize MySQL database
python3 create_db.py

# 6. Run the application
python3 run.py
```

For production deployment on Linux using Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

---

## 📂 8. Project Structure

```
NutriFit/
├── .env.example             # Configuration template for local environment variables
├── .gitignore               # Excluded files (virtual environments, cache, sensitive logs)
├── Procfile                 # Cloud deployment process file (Heroku/Render)
├── README.md                # Comprehensive project documentation & run instructions
├── requirements.txt         # Explicit Python dependencies list
├── runtime.txt              # Targeted Python runtime version (3.10+)
├── run.py                   # Application entry point script (starts dev server)
├── config.py                # Environment loading, configuration classes & DB settings
├── create_db.py             # Database table initialization script
├── test_render_audit.py     # Template rendering safety audit & unit test script
│
├── app/                     # Main Flask Application Package
│   ├── __init__.py          # App Factory (create_app), extensions, blueprints & error handlers
│   ├── extensions.py        # SQLAlchemy extension instance
│   ├── models.py            # Database entity models (User, Profile, WaterLog, etc.)
│   │
│   ├── routes/              # Modular Blueprints
│   │   ├── auth.py          # User authentication: register, login, logout, first-admin role logic
│   │   ├── main.py          # User routes: dashboard, quiz, hydration, weight log, reports
│   │   └── admin.py         # Admin routes: dashboard, client profile audit, file uploads, workout links
│   │
│   ├── static/              # Static Assets
│   │   ├── css/
│   │   │   └── style.css    # Unified custom design system (Flexbox/Grid, themes, cards, tables)
│   │   ├── images/          # UI illustration assets and branding
│   │   └── uploads/         # User uploaded documents (isolated by <user_id>/diet_plans/)
│   │
│   └── templates/           # Jinja2 HTML Templates
│       ├── base.html        # Main shared layout with responsive navbar and alert flashes
│       ├── base_user.html   # User portal master layout
│       ├── base_admin.html  # Admin portal master layout
│       ├── index.html       # Landing page (hero, features overview, call to action)
│       ├── select_focus.html# Onboarding focus selection (Diet, Workout, Both)
│       ├── quiz.html        # Comprehensive health questionnaire
│       ├── home.html        # Client welcome page
│       ├── dashboard.html   # Client daily dashboard (water tracker, assigned plans)
│       ├── reports.html     # Client visual analytics (Chart.js water & weight charts)
│       │
│       ├── admin/
│       │   ├── dashboard.html   # Admin user table and overview
│       │   └── user_detail.html # Deep-dive user inspection, diet upload & workout assignment
│       │
│       ├── auth/
│       │   ├── login.html       # Clean authentication login form
│       │   └── register.html    # Client registration form
│       │
│       └── errors/
│           ├── 404.html         # Custom branded 404 Not Found error page
│           └── 500.html         # Custom branded 500 Internal Server Error page
│
└── docs/                    # Technical & Requirement Documentation
    ├── Backend_Technical_Doc.md # Backend architecture and engineering rationale
    └── SRS.md                   # Software Requirements Specification
```

---

## 🗄️ 9. Database Schema & Models

The database models are implemented via **Flask-SQLAlchemy** in `app/models.py`.

```mermaid
erDiagram
    USERS ||--o| PROFILES : "has one (1:1)"
    USERS ||--o{ WATER_LOGS : "logs daily (1:N)"
    USERS ||--o{ WEIGHT_LOGS : "records progress (1:N)"
    USERS ||--o{ DIET_PLAN : "assigned (1:N)"
    USERS ||--o{ WORKOUT_LINK : "assigned (1:N)"

    USERS {
        int id PK
        string full_name
        string email UK
        string password_hash
        string role "user | admin"
        string focus "diet | workout | both"
        datetime created_at
    }

    PROFILES {
        int id PK
        int user_id FK
        int age
        string gender "male | female"
        float height "in cm"
        float weight "in kg"
        string primary_goal
        string food_habit
        text allergies
        float sleep_hours
        text medical_conditions
        string commitment_level
        float bmi
        float bmr
    }

    WATER_LOGS {
        int id PK
        int user_id FK
        date date
        float goal "in ml (default: weight * 35)"
        float consumed "in ml"
    }

    WEIGHT_LOGS {
        int id PK
        int user_id FK
        float weight "in kg"
        date date
    }

    DIET_PLAN {
        int id PK
        int user_id FK
        string filename
        datetime upload_date
    }

    WORKOUT_LINK {
        int id PK
        int user_id FK
        string link
        datetime upload_date
    }
```

---

## 🧮 10. Health Calculations & Algorithms

NutriFit performs automated health assessments when users complete their profile or record a new weight:

### 1. Body Mass Index (BMI)
$$\text{BMI} = \frac{\text{Weight (kg)}}{(\text{Height (m)})^2}$$

* **Classification Thresholds**:
  * $\text{BMI} < 18.5$: **Underweight**
  * $18.5 \le \text{BMI} < 25.0$: **Normal Weight**
  * $25.0 \le \text{BMI} < 30.0$: **Overweight**
  * $\text{BMI} \ge 30.0$: **Obese**

### 2. Basal Metabolic Rate (BMR)
Calculated using the **Mifflin-St Jeor Equation** (calories burned at complete rest):

* **For Men**:
  $$\text{BMR} = 10 \times \text{weight (kg)} + 6.25 \times \text{height (cm)} - 5 \times \text{age (years)} + 5$$
* **For Women**:
  $$\text{BMR} = 10 \times \text{weight (kg)} + 6.25 \times \text{height (cm)} - 5 \times \text{age (years)} - 161$$

### 3. Recommended Daily Hydration Target
$$\text{Daily Water Goal (ml)} = \text{Weight (kg)} \times 35\text{ ml}$$
*(Fallback: $2000\text{ ml}$ if profile weight is not yet recorded).*

---

## 🧪 11. Testing & Verification

NutriFit includes a defensive rendering test suite (`test_render_audit.py`) to verify template rendering under healthy, edge-case, and empty-profile scenarios:

To run the audit tests:
```powershell
python test_render_audit.py
```

#### Successful Output:
```text
--- Testing admin/user_detail.html (Healthy Context) ---
SUCCESS: Admin User Detail page rendered correctly.

--- Testing admin/user_detail.html (No Profile Context) ---
SUCCESS: Admin User Detail rendered safely without profile.

--- Testing home.html ---
SUCCESS: Home page rendered correctly.
```

---

## ❓ 12. Troubleshooting & Common PC Issues

### Issue 1: PowerShell Script Execution Disabled
* **Error**: `File ...\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`
* **Solution**: PowerShell restricts script execution by default on Windows. Run:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .\venv\Scripts\Activate.ps1
  ```
  *(This allows scripts only in your active terminal session without changing global system security).*

---

### Issue 2: Can't Connect to MySQL Server (Error 2003 / 10061)
* **Error**: `pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'localhost'")`
* **Solution**:
  1. If using **XAMPP**: Open XAMPP Control Panel and ensure the **MySQL** module has started.
  2. If using **MySQL Community Server**: Press `Win + R`, type `services.msc`, locate `MySQL80` (or `MySQL`), right-click and select **Start**.

---

### Issue 3: Access Denied for User 'root'@'localhost'
* **Error**: `pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")`
* **Solution**:
  1. Double check the password in your `.env` file matches your actual MySQL root password.
  2. **URL-Encoding**: If your password has special characters like `@`, `#`, or `,`, encode them (e.g. `My@Password` becomes `My%40Password`).
  3. Verify access via MySQL CLI: `mysql -u root -p`.

---

### Issue 4: Database `nutrifit_db` Does Not Exist (Error 1049)
* **Error**: `pymysql.err.OperationalError: (1049, "Unknown database 'nutrifit_db'")`
* **Solution**: Log into MySQL and create the database:
  ```sql
  CREATE DATABASE nutrifit_db;
  ```

---

### Issue 5: Port 5000 Already in Use
* **Error**: `OSError: [Errno 98/10048] Address already in use`
* **Solution**:
  Another application is using port 5000 (often AirPlay on macOS, or a lingering Python instance on Windows).
  * **Option A**: Find and terminate the process holding port 5000:
    ```powershell
    netstat -ano | findstr :5000
    taskkill /PID <PID_NUMBER> /F
    ```
  * **Option B**: Run on a different port (e.g., 5050):
    Edit `run.py` and specify `app.run(port=5050, debug=True)`.

---

### Issue 6: `ModuleNotFoundError`
* **Error**: `ModuleNotFoundError: No module named 'flask'`
* **Solution**: Your virtual environment is either not activated or dependencies weren't installed into it.
  1. Ensure your terminal prompt shows `(venv)`.
  2. Re-run: `pip install -r requirements.txt`.

---

## 🔒 13. Security Notes & Production Readiness

* **CSRF Protection**: All POST/PUT forms throughout the app implement Flask-WTF CSRF tokens.
* **SQL Injection Prevention**: All queries use SQLAlchemy ORM parameter binding.
* **Password Hashing**: Passwords are encrypted using salted PBKDF2 hashes via Werkzeug (`generate_password_hash`).
* **Upload Security**:
  - File extension validation (`.pdf`, `.docx`, `.xlsx` only).
  - Double extension stripping (e.g., `file.php.pdf` is rejected).
  - Filename sanitization with Werkzeug `secure_filename`.
  - Automatic timestamp appending to prevent file overwrites.
  - Per-user directory isolation (`static/uploads/<user_id>/diet_plans/`).
* **For Production Deployment**:
  - Set `FLASK_ENV=production` in your `.env`.
  - Ensure `DEBUG=False` in `config.py` to prevent sensitive traceback leakage.
  - Set a strong, randomly generated `SECRET_KEY`.
  - Configure a reverse proxy like Nginx or cloud hosting (Render, Railway, AWS, DigitalOcean) with HTTPS enabled.

---

## 📄 14. License & Acknowledgements

* **License**: This project is licensed under the [MIT License](LICENSE).
* **Author**: [Urja Gajera](https://github.com/Urjagajera)
* **Special Thanks**: Built with Flask, SQLAlchemy, Chart.js, and Google Fonts.

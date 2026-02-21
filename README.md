# NutriFit - Personal Health & Nutrition Management

NutriFit is a premium, data-driven web application designed to help users track their fitness journey, hydration, and nutritional progress through personalized plans and interactive visualizations.

## 🚀 Key Features

- **Personalized Biometric Assessment**: Interactive quiz to calculate BMI and BMR.
- **Dynamic User Dashboard**: Real-time hydration tracking with daily reset logic.
- **Interactive Analytics**: Progress charts for weight and water consumption powered by Chart.js.
- **Admin Control Center**: Secure user management, diet plan assignment (PDF/Images), and workout guide integration.
- **Role-Based Access Control**: Secure authentication system with protected administrative routes.
- **Premium UI/UX**: Modern glassmorphism design with smooth transitions and responsive layouts.

## 🛠 Technology Stack

- **Backend**: Python / Flask
- **Frontend**: Pure HTML5 / CSS3 (Vanilla JS for interactive components)
- **Database**: MySQL (Flask-SQLAlchemy ORM)
- **Authentication**: Flask Sessions / Werkzeug Password Hashing
- **Visuals**: Chart.js

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd NutriFit
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_secret_key
   DATABASE_URL=mysql+pymysql://user:password@localhost/nutrifit_db
   ```

5. **Initialize Database**:
   ```bash
   python create_db.py
   ```

6. **Run the application**:
   ```bash
   python run.py
   ```

## 🛡 Security

- Password hashing via PBKDF2.
- Session-based authentication.
- CSRF protection concepts (Flask-built-in).
- Secure file upload handling using `secure_filename`.
- `@admin_required` custom decorators for RBAC.

---
© 2026 NutriFit Application Team. Built for Excellence.

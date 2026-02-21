# Backend Technical Documentation - NutriFit

## 1. Technology Selection Rationale
- **Python Flask**: Chosen for its lightweight, micro-framework nature, allowing for rapid development and flexibility in architectural design.
- **SQLAlchemy ORM**: Utilized to provide a high-level abstraction for MySQL database interactions, ensuring maintainability and preventing SQL injection.
- **MySQL**: Selected for its robustness, reliability, and widespread industry adoption for relational data management.

## 2. Architectural Patterns
### Application Factory Pattern
The application is initialized using the `create_app()` factory function. This pattern facilitates easier testing, multiple instance configurations, and prevents circular dependencies.

### Blueprint Structure
The system is divided into modular Blueprints:
- `auth`: Manages user registration, login, and session handling.
- `main`: Controls core user features, dashboards, and profile management.
- `admin`: Exclusive routes for system administrators.

## 3. Core Logic and Flow
### Role-Based Routing
Access control is enforced via custom decorators and Flask-Login's `login_required`. Routes are segregated based on the `is_admin` attribute of the User model.

### Login and Redirect Logic
Upon authentication, the system evaluates the user's role:
- Administrators are redirected to the `/admin/dashboard`.
- Standard users are redirected to their personalized `/home`.

### User Flow Architecture
1. **Registration**: User provides credentials.
2. **Quiz/Onboarding**: User completes a health focus quiz (Weight Loss, Muscle Gain, etc.).
3. **Dashboard**: User views personalized metrics and water tracking.

## 4. Database Schema
- **User**: Stores credentials, profile information, and role flags.
- **WaterTracker**: Records daily hydration logs indexed by User ID.
- **QuizResults**: Stores historical quiz data for personalized recommendations.

## 5. Data Visualization (Chart.js)
The backend processes raw database metrics and transmits them to the frontend via Jinja2's `|tojson` filter. This ensures data is safely serialized for client-side rendering while maintaining security against XSS.

## 6. Security Implementation
- **CSRF Protection**: Flask-WTF provides CSRF tokens for all form submissions.
- **Password Hashing**: Implemented via Werkzeug security helpers (PBKDF2 with SHA256).
- **Role Decorators**: `@admin_required` custom decorators ensure unauthorized users cannot access sensitive administrative endpoints.

## 7. Frontend Integration
### Responsive Architecture
The frontend utilizes a mobile-first approach with CSS Media Queries. Flexbox and Grid layouts ensure components (cards, tables, navbars) adapt dynamically to various screen dimensions.

### Theme Implementation
Theming is achieved via CSS Variables defined in `:root`. A JavaScript listener toggles the `data-theme` attribute on the `body` tag, with state persistence managed through `localStorage`.

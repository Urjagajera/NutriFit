# Software Requirement Specification (SRS) - NutriFit

## 1. Introduction
This document provides a comprehensive overview of the requirements for the NutriFit web application. NutriFit is designed to assist users in achieving their health and fitness goals through personalized nutrition planning and data-driven insights.

## 2. Purpose
The purpose of this SRS is to define the functional and non-functional requirements of the NutriFit system to ensure transparency between stakeholders and the development team.

## 3. Scope
NutriFit encompasses a web-based portal for users to track nutrition, access personalized meal plans, and view health analytics. It also includes an administrative dashboard for system monitoring and user management.

## 4. Definitions
- **SaaS**: Software as a Service.
- **ORM**: Object-Relational Mapping (SQLAlchemy).
- **Blueprint**: A modular design pattern in Flask for organizing routes.

## 5. Overall Description
The system follows a modular architecture using the Flask framework. It integrates with a MySQL database for persistent storage and utilizes Chart.js for data visualization.

## 6. User Classes
- **User**: General users accessing personalized health plans, tracking data, and viewing reports.
- **Admin**: System administrators responsible for monitoring user activity and managing the platform.

## 7. Functional Requirements
| ID | Requirement Description |
|---|---|
| FR-1 | The system shall allow users to register and securely log in. |
| FR-2 | The system shall provide personalized nutrition and focus recommendations. |
| FR-3 | The system shall track daily water intake and visualize progress. |
| FR-4 | The system shall generate comprehensive health reports via Chart.js. |
| FR-5 | The system shall provide an admin dashboard for user oversight. |

## 8. Non-Functional Requirements
- **Performance**: Page load times shall be under 2 seconds for core dashboards.
- **Scalability**: The application factory pattern ensures the system can handle an increasing number of concurrent users.
- **Reliability**: The system should maintain 99.9% uptime.

## 9. Security Requirements
- **Encryption**: All passwords MUST be hashed using industry-standard algorithms (e.g., Bcrypt/Scrypt).
- **Authorization**: Role-based access control (RBAC) must be enforced for admin routes.
- **Protection**: Use of CSRF protection for all state-changing requests.

## 10. Database Overview
The system utilizes MySQL for relational data management, including tables for Users, Quiz results, and Activity logs, managed via SQLAlchemy ORM.

## 11. System Architecture Overview
A modular Flask application utilizing the Application Factory pattern and Blueprints for clean separation of concerns between Auth, Main, and Admin modules.

## 12. UI/UX Design Considerations
- **Aesthetics**: Premium, modern interface with high readability.
- **Navigation**: Intuitive navbar with role-specific links.

## 13. Responsive Design Requirement
The application must be fully responsive, providing an optimal viewing experience across Desktop, Tablet, and Mobile devices using CSS Media Queries and Flexbox/Grid.

## 14. Theme Support (Light Mode)
The system shall support a persistent Light Mode (default) and Dark Mode, togglable via the UI and saved in the user's browser local storage.

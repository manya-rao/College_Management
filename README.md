# College Management System

A full-stack College Management System developed using MySQL, Node.js, Express.js, HTML, CSS, and JavaScript. The project manages students, faculty, departments, courses, enrollments, attendance, and academic reports.

## Features

### Database Management
- Student Management
- Faculty Management
- Department Management
- Course Management
- Enrollment Management
- Attendance Tracking

### SQL Operations
- CRUD Operations
- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING Clause
- Subqueries
- Correlated Subqueries
- NOT EXISTS Queries
- Stored Procedures
- Triggers

### Frontend
- Responsive Dashboard
- Student Records Display
- Course Information
- Faculty Information
- Attendance Reports
- Performance Reports

---

## Database Schema

### Student
| Column | Type |
|----------|----------|
| student_id | INT (PK) |
| name | VARCHAR |
| department_id | INT (FK) |
| year | INT |
| email | VARCHAR |

### Faculty
| Column | Type |
|----------|----------|
| faculty_id | INT (PK) |
| name | VARCHAR |
| department_id | INT (FK) |
| designation | VARCHAR |

### Department
| Column | Type |
|----------|----------|
| department_id | INT (PK) |
| department_name | VARCHAR |

### Course
| Column | Type |
|----------|----------|
| course_id | INT (PK) |
| course_name | VARCHAR |
| credits | INT |
| department_id | INT (FK) |

### Enrollment
| Column | Type |
|----------|----------|
| enrollment_id | INT (PK) |
| student_id | INT (FK) |
| course_id | INT (FK) |
| semester | VARCHAR |
| grade | DECIMAL |

### Attendance
| Column | Type |
|----------|----------|
| attendance_id | INT (PK) |
| student_id | INT (FK) |
| course_id | INT (FK) |
| attendance_percentage | DECIMAL |

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Node.js
- Express.js

### Database
- MySQL

### Tools
- MySQL Workbench
- VS Code
- Git & GitHub
- Postman

---

## Project Structure

```text
CollegeManagementSystem/
│
├── backend/
│   ├── server.js
│   ├── routes/
│   ├── controllers/
│   └── database/
│
├── frontend/
│   ├── index.html
│   ├── students.html
│   ├── courses.html
│   ├── faculty.html
│   ├── attendance.html
│   ├── css/
│   └── js/
│
├── database/
│   ├── schema.sql
│   ├── inserts.sql
│   ├── procedures.sql
│   └── triggers.sql
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/CollegeManagementSystem.git
```

### Navigate to Project

```bash
cd CollegeManagementSystem
```

### Install Dependencies

```bash
npm install
```

### Configure Database

1. Create MySQL database:

```sql
CREATE DATABASE college_management;
```

2. Execute:
   - schema.sql
   - inserts.sql
   - procedures.sql
   - triggers.sql

### Run Server

```bash
node server.js
```

Server runs at:

```text
http://localhost:5000
```

---

## Implemented Queries

1. Retrieve all students.
2. Display courses offered by a department.
3. Student and enrollment details (INNER JOIN).
4. Student, course, and faculty details (3-table JOIN).
5. Count students per department.
6. Departments having more than 50 students.
7. Students scoring above average GPA.
8. Correlated subquery for enrollment comparison.
9. Students including those not enrolled (LEFT JOIN).
10. Courses with no enrollments (NOT EXISTS).

---

## Stored Procedures

### Calculate GPA

```sql
CALL CalculateGPA(student_id);
```

### Department Performance Report

```sql
CALL DepartmentPerformance();
```

---

## Triggers

### Prevent Duplicate Enrollment

Prevents a student from enrolling in the same course multiple times.

### Attendance Update Trigger

Automatically updates attendance records after insertion.

---

## Future Enhancements

- Authentication and Authorization
- Student Login Portal
- Faculty Login Portal
- GPA Analytics Dashboard
- Attendance Charts
- Export Reports to PDF
- Email Notifications

---

## Learning Outcomes

- Relational Database Design
- SQL Query Optimization
- Stored Procedures
- Triggers
- Backend API Development
- Frontend Development
- Database Connectivity

---

## Author

**Manya Rao**

College Management System Project for DBMS Laboratory.

Mini Job Portal

A simple console-based Python application integrated with MySQL, designed for two user roles: Recruiters and Job Seekers. The system supports job posting, job viewing, and application management through a clean modular structure.

🚀 Features
Recruiter

Register & Login

Post Jobs

View Applicants

Job Seeker

Register & Login

View Jobs

Apply for Jobs

🛠 Technologies Used

Python

MySQL

mysql-connector-python

📂 Project Structure
db.py          - Database connection
recruiter.py   - Recruiter features
jobseeker.py   - Job seeker features
main.py        - Main program & menu logic

🔄 How It Works

Users register as recruiter or job seeker.

Recruiters post jobs and view applicants.

Job seekers view all jobs and apply.

All interactions are stored and retrieved using MySQL.

🗄 Database Tables

users – stores recruiters & job seekers

jobs – job postings

applications – job applications linked to jobs & seekers

▶️ Running the Project

Install dependencies:

pip install mysql-connector-python


Update MySQL credentials in db.py

Run the app:

python main.py

✅ Summary

A simple and functional job portal demonstrating Python–MySQL integration, modular programming, and role-based interactions.

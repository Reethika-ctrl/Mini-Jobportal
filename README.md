# 📌 Mini Job Portal

A simple console-based Python application integrated with MySQL, designed for two user roles: **Recruiters** and **Job Seekers**.  
The system supports job posting, job viewing, and application management through a clean and modular architecture.

---

## 🚀 Features

### 👨‍💼 Recruiter
- Register & Login  
- Post Jobs  
- View Applicants  

### 👩‍💻 Job Seeker
- Register & Login  
- View Jobs  
- Apply for Jobs  

---

## 🛠️ Technologies Used
- **Python**
- **MySQL**
- **mysql-connector-python**

---

## 📂 Project Structure
db.py → Database connection
recruiter.py → Recruiter features
jobseeker.py → Job seeker features
main.py → Main program & menu logic


---

## 🔄 How the System Works
- Users register as **Recruiter** or **Job Seeker**  
- Recruiters can:
  - Post jobs  
  - View applicants  
- Job seekers can:
  - View all available jobs  
  - Apply for jobs  
- All data is stored and retrieved using **MySQL**  

---

## 🗄️ Database Design (ER Diagram)

> 📌 Upload your ER diagram → then replace the link below

![ER Diagram](link-to-your-er-diagram.png)

---

## 🎭 Use Case Diagram

> 📌 Upload your Use Case diagram → replace link

![Use Case Diagram](link-to-your-usecase-diagram.png)

---

## 📸 Screenshots

### 🔐 Recruiter Module
![Recruiter Register](link-recruiter-register.png)  
![Recruiter Login](link-recruiter-login.png)  
![Post Job](link-post-job.png)  
![View Applicants](link-view-applicants.png)  

---

### 👤 Job Seeker Module
![Job Seeker Login](link-jobseeker-login.png)  
![View Jobs](link-view-jobs.png)  
![Apply Job](link-apply-job.png)

---

## ▶️ Running the Project

### 1️⃣ Install dependencies
```bash
pip install mysql-connector-python

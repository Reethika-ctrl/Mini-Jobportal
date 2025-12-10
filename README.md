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

![ER Diagram](https://github.com/Reethika-ctrl/Mini-Jobportal/raw/main/Mini%20Job%20Portal.png)

---

## 🎭 Use Case Diagram

> 📌 Upload your Use Case diagram → replace link

![Use Case Diagram](https://github.com/Reethika-ctrl/Mini-Jobportal/raw/main/Screenshot%202025-11-23%20120257.png)
)

---

## 📸 Screenshots

### 🔐 Recruiter Module
![Screenshot](https://github.com/Reethika-ctrl/Mini-Jobportal/raw/main/Screenshot%202025-11-23%20123951.png)
  

---

### 👤 Job Seeker Module
![Screenshot](https://github.com/Reethika-ctrl/Mini-Jobportal/raw/main/Screenshot%202025-11-22%20165310.png)

---


## ▶️ Running the Project

### 1️⃣ Install dependencies
```bash
pip install mysql-connector-python
```
2️⃣ Configure database in db.py

3️⃣ Run the application
```bash
python main.py

```

📌 Summary
A clean and functional job portal demonstrating:

Python–MySQL integration

Modular programming

Role-based authentication

Real-time data operations


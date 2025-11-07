# 🧠 CBT Exam Web App

A **Computer-Based Test (CBT)** web application built with **Django (Python)** for conducting online scholarship examinations. It allows administrators to create courses, questions, and answers, while students can take exams and receive instant, auto-graded results. The app is hosted on **AWS Cloud** for performance, scalability, and reliability.

---

## 🚀 Key Features
- 👨‍🎓 **Students:** Register, log in, take exams, and view scores instantly.  
- 🧑‍💼 **Admins:** Manage courses, questions, and answers; view reports and performance analytics.  
- 🧮 **Auto Grading:** Automatic result computation and storage.  
- 📊 **Reports:** Generate performance summaries and exportable insights.  
- ☁️ **AWS Deployment:** Scalable and secure cloud infrastructure.

---

## 🏗️ Tech Stack
**Frontend:** HTML, CSS, JavaScript  
**Backend:** Python (Django Framework)  
**Database:** PostgreSQL / MySQL  
**Hosting:** AWS (EC2, RDS, S3)  
**Version Control:** Git + GitHub  

---

## ⚙️ Installation (Local Setup)
```bash
# 1️⃣ Clone the repository
git clone https://github.com/akinzsoft/CBTEXAM.git
cd CBTEXAM

# 2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure the database
# Update settings.py or .env with your DB credentials
python manage.py migrate

# 5️⃣ Create superuser for admin access
python manage.py createsuperuser

# 6️⃣ Run the development server
python manage.py runserver





🛠️ Future Enhancements

Timed exams with countdown

Advanced analytics dashboard

PDF/Excel report export

Email/SMS notifications for results

👨‍💻 Developer

Ayotunde Daniel Akinwumi
Founder – Akinzsoft Technologies
📧 Email: your-email@example.com

🌐 GitHub: https://github.com/akinzsoft

☁️ Hosted on Amazon Web Services (AWS)

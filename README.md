📖 README.md (SheCan Foundation Web App)

# 🌸 SheCan Foundation - Intern Dashboard & Login System

A simple Django-based web application built for **SheCan Foundation** to demonstrate:
- Dummy login/signup functionality  
- Intern dashboard with referral code & donations display  
- Static leaderboard for top fundraisers  
- Rewards/unlockables section (static)

---

## ⚙️ Features
✅ **Login/Signup Page** (Bootstrap UI with background image)  
✅ **Intern Dashboard**  
   - Intern name (from dummy DB/session)
   - Dummy referral code generation (e.g., `username2025`)
   - Total donations raised (static value)
   - Rewards/unlockables section (static badges)  
✅ **Leaderboard Page** (Top 5 dummy fundraisers)  
✅ **Bootstrap-based modern UI** with SheCan branding  
✅ Backend powered by **Django (Python)** with session handling  

---

## 🖥️ Tech Stack
- **Backend:** Django (Python 3.13+)
- **Frontend:** HTML, CSS (Bootstrap 5)
- **Database:** SQLite (default Django DB)
- **Other Tools:** Django template engine, static files

---

## 📂 Project Structure
she_foundation/
│
├── login/ # Login app (signup form)
│ ├── templates/
│ │ └── login_.html
│ └── views.py
│
├── dashboard/ # Dashboard app (intern dashboard & leaderboard)
│ ├── templates/
│ │ ├── dashboard.html
│ │ └── leaderboard.html
│ └── views.py
│
├── static/ # Static assets (CSS, images)
│ └── images/
│
├── she_foundation/ # Main project config
│
└── manage.py

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/shecan-foundation.git
cd shecan-foundation
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate         # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Database Migrations
python manage.py migrate

5️⃣ Start the Development Server
python manage.py runserver
Now open http://127.0.0.1:8000/ in your browser.

🚀 Usage
Visit the Login/Signup Page → Enter dummy details (username, email, password).

After signup, you'll be redirected to the Dashboard:

View your name, dummy referral code, total donations.

See static rewards/unlockables.

Click Leaderboard in navbar to view top 5 fundraisers.

📸 Screenshots
![Login Page](<img width="1366" height="768" alt="Screenshot (206)" src="https://github.com/user-attachments/assets/0678933a-a284-4713-a148-ec7e834254ee" />
)
![Dashboard](<img width="1366" height="768" alt="Screenshot (207)" src="https://github.com/user-attachments/assets/7325455e-d64e-4e20-b7a2-45d361f9c047" />
)
![Dashboard](<img width="1366" height="768" alt="Screenshot (208)" src="https://github.com/user-attachments/assets/217bbd75-abd8-4feb-90a6-874e22a63a89" />
)
![Leaderboard](<img width="1366" height="768" alt="Screenshot (209)" src="https://github.com/user-attachments/assets/8bdceefa-1655-4d68-8842-92aeb3d7c891" />
)
📌 Notes
This is a dummy prototype – authentication and donation data are mocked for demonstration purposes.

For real deployment, connect to Firebase/MySQL or API endpoints.

👩‍💻 Author
Yuvraj (Vruk)
Developed for SheCan Foundation Intern Assignment 2025
GitHub: @xVrukx

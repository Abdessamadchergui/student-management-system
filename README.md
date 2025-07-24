# Student Management System

This is a simple Student Management System desktop application developed in Python using **Tkinter** for the GUI and **MySQL** for the backend database.

The system supports user authentication through login and registration features, enabling basic interaction with a `user` table in the database.

---

## ✨ Features

- User Login & Registration
- Password confirmation and error handling
- MySQL database integration
- Clean and responsive GUI with a background image
- Input validation for login and registration forms

---

## 🛠️ Tech Stack

- **Frontend:** Tkinter (Python GUI library)
- **Backend:** MySQL (via `pymysql`)
- **Image Handling:** PIL (Pillow)
- **Language:** Python 3.x

---



## ⚙️ Setup Instructions

1. **Install Dependencies:**

```bash
pip install pymysql pillow
```

2. **Create Database and Tables in MySQL:**

```sql
CREATE DATABASE db_stu;

USE db_stu;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);
```

> Make sure your MySQL server is running and accessible.

3. **Configure the Database Connection:**

In `conn_myql.py`, make sure to update the credentials:

```python
import pymysql
conn = pymysql.Connection(
    host="localhost",
    port=3306,
    user="root",            # change if necessary
    password="your_password",
    autocommit=True
)
conn.select_db("db_stu")
```

4. **Run the Application:**

```bash
python main.py
```

---

## 🖼️ Screenshots

### 🔐 Login Screen
<img width="1366" height="768" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/69ab547a-6de5-417a-86d2-6debd9ed6830" />


### 📝 Registration Screen

<img width="1366" height="768" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/bac27185-894d-4e87-99ca-bf71336a065d" />

### 📝 mainpage
<img width="1366" height="768" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/78b45e36-7b31-43f6-8a38-81a754db535f" />


---

## 💡 Notes

- This project is meant for educational/demo purposes.
- Passwords are stored in plain text (not recommended for production).
- You can expand this system to include CRUD operations for student data.

---

## 📄 License

This project is open source and free to use.

---

## 👨‍💻 Author

Developed by [ABDESS]

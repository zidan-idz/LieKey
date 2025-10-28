<p align="center">
  <img src="img/logo.png" width="900" alt="LieKey Logo">
</p>

---

## • Information
[![Author](https://img.shields.io/badge/Author-Zidan%20IDz-0A66C2?style=for-the-badge&logo=github)](#)
[![Version](https://img.shields.io/badge/Version-0.0.4-0A66C2.svg)](#)
[![Language](https://img.shields.io/badge/Language-Python-0A66C2.svg?logo=python)](#)
[![Framework](https://img.shields.io/badge/Framework-Flask-0A66C2.svg?logo=flask)](#)
[![Database](https://img.shields.io/badge/Database-SQLite-0A66C2.svg?logo=sqlite)](#)

---

## • Description
**LieKey** is a lightweight Flask-based web application that provides text encryption and decryption using **two classical cryptographic algorithms**:  
**Caesar Cipher** and **Vigenère Cipher**.

It features a simple and responsive interface built with **Bootstrap 5**, along with a **local history tracking system** powered by **SQLite**, which stores recent operations performed by users.

> ⚠️ Currently, the history is shared among all users, meaning all visitors can view or clear the same data.

---

## • Features
- Encrypt and decrypt text using Caesar and Vigenère Ciphers  
- Automatically log each operation with a timestamp  
- Option to clear the entire encryption history  
- Responsive interface using Bootstrap 5  
- Lightweight and easy to host with SQLite  

---

## • Documentation

**Live Demo:**  
[https://liekey.pythonanywhere.com/](https://liekey.pythonanywhere.com/)

**Source Code:**  
- [GitLab Repository](https://gitlab.com/zidan-idz/liekey)  
- [GitHub Repository](https://github.com/zidan-idz/liekey)

---

## • Project Structure

```bash
LieKey/
│
├── app.py              # Main Flask application
├── history.db          # SQLite database storing encryption/decryption history
│
├── templates/          # HTML templates for Flask
│   └── index.html      # Main user interface
│
├── static/             # Static assets (CSS, JS, etc.)
│   └── style.css       # Custom styling
│
├── img/                # Images used in the project
│   └── logo.png        # Project logo
│
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python runtime version (for deployment)
└── README.md           # Project documentation

```

---

## • Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/zidan-idz/liekey.git
   cd liekey
   ```
2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate   # On Linux / macOS
    ```
3. **Install dependencies**
    ```bash
    pip install flask
    ```
4. **Run the application**
    ```bash
    python app.py
    ```
5. **Open in your browser**
    ```bash
    http://127.0.0.1:5000
    ```
---

## • License

This project is licensed under the **[MIT Lisence](https://gitlab.com/zidan-idz/liekey/-/blob/main/LICENSE?ref_type=heads)**.
Feel free to use, modify, and distribute with proper attribution.


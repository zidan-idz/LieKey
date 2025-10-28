<p align="center">
  <img src="img/logo.png" width="900" title="LieKey Logo" alt="LieKey">
</p>

---

### • Information
[![Author](https://img.shields.io/badge/Author-Akira%20Hitomi-0A66C2?style=for-the-badge&logo=github)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-0A66C2.svg)](#)
[![Language](https://img.shields.io/badge/Language-Python-0A66C2.svg?logo=python)](#)
[![Framework](https://img.shields.io/badge/Framework-Flask-0A66C2.svg?logo=flask)](#)
[![Database](https://img.shields.io/badge/Database-SQLite-0A66C2.svg?logo=sqlite)](#)

---

### • Description
**LieKey** is a lightweight Flask-based web application that provides text encryption and decryption using **two classical cryptographic algorithms**:  
**Caesar Cipher** and **Vigenère Cipher**.

It includes a simple, responsive interface built with **Bootstrap 5**, and a **local history tracking feature** powered by **SQLite** to store recent operations.

---

### • Features
- Text encryption and decryption using Caesar and Vigenère Ciphers  
- Automatic history logging with timestamps  
- Option to clear encryption history  
- Responsive Bootstrap interface  
- S

---
### • Documentation

##### Live Demo
[(https://liekey.pythonanywhere.com/)]

##### Source Code
[(https://gitlab.com/zidan-idz/liekey)]
[(https://github.com/zidan-idz/liekey)]

---

### • Project Structure

```bash
LieKey/
│
├── app.py # Main Flask application
├── history.db # SQLite database for history
├── templates/
│ └── index.html # Main HTML interface
├── static/
│ ├── style.css # Custom CSS
│ └── liekey-logo.png # Project logo
└── README.md
```

---

## • Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/zidan-idz/liekey.git
   cd LieKey
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

• License

This project is licensed under the **[MIT Lisence](https://gitlab.com/zidan-idz/liekey/license)**.
Feel free to use, modify, and distribute with proper attribution.


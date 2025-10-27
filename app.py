from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_input TEXT,
            result TEXT,
            algorithm TEXT,
            mode TEXT,
            shift INTEGER,
            key TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_history(text_input, result, algorithm, mode, shift, key):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO history (text_input, result, algorithm, mode, shift, key, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (text_input, result, algorithm, mode, shift, key, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY id DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return data

def clear_history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("DELETE FROM history")
    conn.commit()
    conn.close()

# ---------------- ALGORITMA ----------------
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_cipher(text, key, mode):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        if "delete_history" in request.form:
            clear_history()
            return redirect(url_for("index"))

        text = request.form["text"]
        algo = request.form["algo"]
        mode = request.form["mode"]
        shift = int(request.form.get("shift", 0))
        key = request.form.get("key", "")

        if algo == "caesar":
            result = caesar_cipher(text, shift, mode)
        elif algo == "vigenere":
            result = vigenere_cipher(text, key, mode)

        save_history(text, result, algo, mode, shift, key)

    history = get_history()
    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)

    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        # Check for duplicate email
        cursor.execute(
            "SELECT * FROM students WHERE email = ?",
            (email,)
        )

        result = cursor.fetchone()

        if result:
            message = "Duplicate Record Found!"
        else:
            cursor.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)",
                (name, email)
            )
            conn.commit()
            message = "Record Added Successfully!"

        conn.close()

    return render_template("index.html", message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE INIT ----------------
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        department TEXT,
        year TEXT,
        email TEXT,
        phone TEXT,
        gender TEXT,
        address TEXT
    )
    """)

    # INSERT SAMPLE DATA ONLY IF EMPTY
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("""
        INSERT INTO students
        (name, roll, department, year, email, phone, gender, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            ("Arun Kumar", "CS101", "CSE", "3rd", "arun@gmail.com", "9876543210", "Male", "Chennai"),
            ("Priya S", "CS102", "IT", "2nd", "priya@gmail.com", "9876543211", "Female", "Madurai"),
            ("Vikram R", "CS103", "CSE", "4th", "vikram@gmail.com", "9876543212", "Male", "Coimbatore"),
            ("Ananya", "CS104", "ECE", "1st", "ananya@gmail.com", "9876543213", "Female", "Trichy"),
            ("Rahul", "CS105", "MECH", "3rd", "rahul@gmail.com", "9876543214", "Male", "Salem"),
            ("Divya", "CS106", "CSE", "2nd", "divya@gmail.com", "9876543215", "Female", "Chennai"),
            ("Karthik", "CS107", "IT", "4th", "karthik@gmail.com", "9876543216", "Male", "Erode"),
            ("Sneha", "CS108", "ECE", "3rd", "sneha@gmail.com", "9876543217", "Female", "Madurai"),
            ("Manoj", "CS109", "CSE", "1st", "manoj@gmail.com", "9876543218", "Male", "Vellore"),
            ("Keerthi", "CS110", "IT", "2nd", "keerthi@gmail.com", "9876543219", "Female", "Chennai"),
        ])

    conn.commit()
    conn.close()

init_db()

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]
        department = request.form["department"]
        year = request.form["year"]
        email = request.form["email"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        address = request.form["address"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students
        (name, roll, department, year, email, phone, gender, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, roll, department, year, email, phone, gender, address))

        conn.commit()
        conn.close()

        return redirect("/students")

    return render_template("register.html")

@app.route("/students")
def students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return render_template("students.html", students=data)

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True) 
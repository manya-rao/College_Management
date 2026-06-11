from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# ==========================
# DATABASE CONNECTION
# ==========================

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rammi@1968",      # Change if needed
        database="college_management"
    )

# ==========================
# LOAD STUDENTS
# ==========================

def load_students():

    for row in tree.get_children():
        tree.delete(row)

    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        SELECT student_id,
               name,
               department_id,
               year,
               email
        FROM Student
    """)

    rows = cur.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    con.close()

# ==========================
# ADD STUDENT
# ==========================

def add_student():

    if name_var.get() == "":
        messagebox.showerror(
            "Error",
            "Name is required"
        )
        return

    con = connect_db()
    cur = con.cursor()

    sql = """
    INSERT INTO Student
    (name,department_id,year,email)
    VALUES(%s,%s,%s,%s)
    """

    cur.execute(
        sql,
        (
            name_var.get(),
            dept_var.get(),
            year_var.get(),
            email_var.get()
        )
    )

    con.commit()
    con.close()

    clear_fields()
    load_students()

    messagebox.showinfo(
        "Success",
        "Student Added Successfully"
    )

# ==========================
# DELETE STUDENT
# ==========================

def delete_student():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a student first"
        )
        return

    values = tree.item(selected, "values")

    sid = values[0]

    con = connect_db()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM Student WHERE student_id=%s",
        (sid,)
    )

    con.commit()
    con.close()

    load_students()

    messagebox.showinfo(
        "Deleted",
        "Student Deleted Successfully"
    )

# ==========================
# FILL FORM
# ==========================

def select_student(event):

    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected, "values")

    name_var.set(values[1])
    dept_var.set(values[2])
    year_var.set(values[3])
    email_var.set(values[4])

# ==========================
# UPDATE STUDENT
# ==========================

def update_student():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a student"
        )
        return

    values = tree.item(selected, "values")

    sid = values[0]

    con = connect_db()
    cur = con.cursor()

    sql = """
    UPDATE Student
    SET name=%s,
        department_id=%s,
        year=%s,
        email=%s
    WHERE student_id=%s
    """

    cur.execute(
        sql,
        (
            name_var.get(),
            dept_var.get(),
            year_var.get(),
            email_var.get(),
            sid
        )
    )

    con.commit()
    con.close()

    load_students()

    messagebox.showinfo(
        "Updated",
        "Student Updated Successfully"
    )

# ==========================
# CLEAR
# ==========================

def clear_fields():

    name_var.set("")
    dept_var.set("")
    year_var.set("")
    email_var.set("")

# ==========================
# DASHBOARD COUNTS
# ==========================

def update_dashboard():

    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM Student")
    students = cur.fetchone()[0]

    try:
        cur.execute("SELECT COUNT(*) FROM Faculty")
        faculty = cur.fetchone()[0]
    except:
        faculty = 0

    try:
        cur.execute("SELECT COUNT(*) FROM Course")
        courses = cur.fetchone()[0]
    except:
        courses = 0

    con.close()

    student_count.config(
        text=f"Students\n{students}"
    )

    faculty_count.config(
        text=f"Faculty\n{faculty}"
    )

    course_count.config(
        text=f"Courses\n{courses}"
    )

# ==========================
# GUI
# ==========================

root = Tk()

root.title("College Management System")
root.geometry("1200x700")
root.configure(bg="#f5f7fa")

# Title

title = Label(
    root,
    text="COLLEGE MANAGEMENT SYSTEM",
    bg="#1e3a8a",
    fg="white",
    font=("Segoe UI", 22, "bold"),
    pady=15
)

title.pack(fill=X)

# Dashboard

dash = Frame(root, bg="#f5f7fa")
dash.pack(fill=X, pady=15)

student_count = Label(
    dash,
    bg="#2563eb",
    fg="white",
    width=20,
    height=4,
    font=("Segoe UI", 12, "bold")
)

student_count.grid(row=0, column=0, padx=10)

faculty_count = Label(
    dash,
    bg="#16a34a",
    fg="white",
    width=20,
    height=4,
    font=("Segoe UI", 12, "bold")
)

faculty_count.grid(row=0, column=1, padx=10)

course_count = Label(
    dash,
    bg="#dc2626",
    fg="white",
    width=20,
    height=4,
    font=("Segoe UI", 12, "bold")
)

course_count.grid(row=0, column=2, padx=10)

# Form

form = LabelFrame(
    root,
    text="Student Information",
    font=("Segoe UI", 12, "bold")
)

form.pack(fill=X, padx=20)

name_var = StringVar()
dept_var = StringVar()
year_var = StringVar()
email_var = StringVar()

Label(form, text="Name").grid(row=0, column=0, padx=10, pady=10)

Entry(
    form,
    textvariable=name_var,
    width=30
).grid(row=0, column=1)

Label(form, text="Department ID").grid(row=0, column=2)

Entry(
    form,
    textvariable=dept_var,
    width=30
).grid(row=0, column=3)

Label(form, text="Year").grid(row=1, column=0)

Entry(
    form,
    textvariable=year_var,
    width=30
).grid(row=1, column=1)

Label(form, text="Email").grid(row=1, column=2)

Entry(
    form,
    textvariable=email_var,
    width=30
).grid(row=1, column=3)

Button(
    form,
    text="Add Student",
    bg="green",
    fg="white",
    command=add_student
).grid(row=2, column=0, pady=15)

Button(
    form,
    text="Update Student",
    bg="orange",
    fg="white",
    command=update_student
).grid(row=2, column=1)

Button(
    form,
    text="Delete Student",
    bg="red",
    fg="white",
    command=delete_student
).grid(row=2, column=2)

Button(
    form,
    text="Clear",
    command=clear_fields
).grid(row=2, column=3)

# Table

style = ttk.Style()
style.theme_use("clam")

tree = ttk.Treeview(
    root,
    columns=(
        "id",
        "name",
        "dept",
        "year",
        "email"
    ),
    show="headings"
)

tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("dept", text="Department")
tree.heading("year", text="Year")
tree.heading("email", text="Email")

tree.column("id", width=70)
tree.column("name", width=200)
tree.column("dept", width=100)
tree.column("year", width=100)
tree.column("email", width=250)

tree.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=20
)

tree.bind(
    "<<TreeviewSelect>>",
    select_student
)

load_students()
update_dashboard()

root.mainloop()
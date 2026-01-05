import tkinter as tk
from tkinter import messagebox
import input as inp
import output

students, courses = inp.load_data()

def add_student():
    sid = entry_sid.get()
    name = entry_name.get()
    dob = entry_dob.get()
    inp.add_student(students, sid, name, dob)
    messagebox.showinfo("Info", f"Added student {name}")

def add_course():
    cid = entry_cid.get()
    name = entry_cname.get()
    credits = int(entry_credits.get())
    inp.add_course(courses, cid, name, credits)
    messagebox.showinfo("Info", f"Added course {name}")

def show_students():
    text.delete("1.0", tk.END)
    for s in students:
        s.calculate_gpa(courses)
        text.insert(tk.END, f"ID: {s.get_id()}, Name: {s.get_name()}, GPA: {s.get_gpa()}\n")

def show_courses():
    text.delete("1.0", tk.END)
    for c in courses:
        text.insert(tk.END, f"ID: {c.get_id()}, Name: {c.get_name()}, Credits: {c.get_credits()}\n")

def save_all():
    inp.save_data(students, courses, background=False)
    messagebox.showinfo("Info", "Data saved successfully!")

root = tk.Tk()
root.title("PW9 Management System")

# Student form
tk.Label(root, text="Student ID").grid(row=0, column=0)
entry_sid = tk.Entry(root); entry_sid.grid(row=0, column=1)
tk.Label(root, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(root); entry_name.grid(row=1, column=1)
tk.Label(root, text="DoB").grid(row=2, column=0)
entry_dob = tk.Entry(root); entry_dob.grid(row=2, column=1)
tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, columnspan=2)

# Course form
tk.Label(root, text="Course ID").grid(row=4, column=0)
entry_cid = tk.Entry(root); entry_cid.grid(row=4, column=1)
tk.Label(root, text="Course Name").grid(row=5, column=0)
entry_cname = tk.Entry(root); entry_cname.grid(row=5, column=1)
tk.Label(root, text="Credits").grid(row=6, column=0)
entry_credits = tk.Entry(root); entry_credits.grid(row=6, column=1)
tk.Button(root, text="Add Course", command=add_course).grid(row=7, column=0, columnspan=2)

# Display area
text = tk.Text(root, width=50, height=15)
text.grid(row=8, column=0, columnspan=2)

tk.Button(root, text="Show Students", command=show_students).grid(row=9, column=0)
tk.Button(root, text="Show Courses", command=show_courses).grid(row=9, column=1)
tk.Button(root, text="Save Data", command=save_all).grid(row=10, column=0, columnspan=2)

root.mainloop()

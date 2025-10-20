import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def submit_form():
    data=f"""
    Student Name:
{entry_fullname.get()}
    Matric Number:
{entry_matricnumber.get()}
    Department:
{department_combo.get()}
    Semester:
{semester_combo.get()}
    level:
{level_combo.get()}
    Courses Selected
    """
    messagebox.showinfo("Form Submitted Successfully",data)


root=tk.Tk()
#HEADER
tk.Label(root,text="Faculty of Computing Course Enrollment Form", font=("Arial",16, "bold")).pack(pady=10)
root.title("Course enrollment form")
root.geometry("500x500")

frame=tk.Frame(root)
frame.pack()

#User Info Frame
user_info_frame=tk.LabelFrame(frame,text="Course Registration")
user_info_frame.grid(row=0,column=0, pady=10)
#STUDENT FULLNAME

lbl_fullname=tk.Label(user_info_frame,text="Fullname")
lbl_fullname.grid(row=0,column=0)
entry_fullname=tk.Entry(user_info_frame,width=18)
entry_fullname.grid(row=1,column=0)

#STUDENT MATRICNUMBER
lbl_matricnumber=tk.Label(user_info_frame,text="Matricnumber")
lbl_matricnumber.grid(row=0,column=1)
entry_matricnumber=tk.Entry(user_info_frame,width=18)
entry_matricnumber.grid(row=1,column=1)

#STUDENT DEPARTMENT
lbl_department=tk.Label(user_info_frame,text="Department")
lbl_department.grid(row=0,column=2)
department_combo=ttk.Combobox(user_info_frame,values=["","Computer Science.","Cyber Security","Information Technology","Software engineering","libary and Information Science"])
department_combo.grid(row=1,column=2)

#SEMESTER
lbl_semester=tk.Label(user_info_frame,text="Semester")
lbl_semester.grid(row=2,column=0)
semester_combo=ttk.Combobox(user_info_frame,values=["","first semester.","second semester"])
semester_combo.grid(row=2,column=1)

#LEVEL

lbl_level=tk.Label(user_info_frame,text="Level")
lbl_level.grid(row=3,column=0)
level_combo=ttk.Combobox(user_info_frame,values=["","100","200","300","400","500"])
level_combo.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=15,pady=5)

#COURSES
tk.Label(root,text="Select Courses").pack(pady=10)
courses={
    "csc131": tk.IntVar(),
    "MTH131": tk.IntVar(),
    "GST131": tk.IntVar(),
    "CSC231": tk.IntVar(),
    "CYB212": tk.IntVar(),
    "SWE212": tk.IntVar(),
    "CSC321": tk.IntVar(),
    "IFT321": tk.IntVar(),
    "SWE311": tk.IntVar(),
    "CYB313": tk.IntVar(),
    "CSC411": tk.IntVar(),
    "IFT414": tk.IntVar(),
    "CYB431": tk.IntVar(),
    "LIS131": tk.IntVar(),
    "LIS231": tk.IntVar(),
}
for courses, var in courses.items():
    tk.Checkbutton(root,text=courses,variable=var).pack(anchor='w')

#SUBMIT BUTTON
tk.Button(root,text="Submit",command=submit_form,bg="blue",fg="white").pack(pady=20)
root.mainloop()


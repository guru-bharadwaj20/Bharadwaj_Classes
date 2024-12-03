import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def on_click(entry1, entry2):
    name = entry1.get().strip()
    contact = entry2.get().strip()

    if name == "" or contact == "":
        messagebox.showinfo("Warning", "Please enter valid Username and Password")
    elif name.lower() == "admin" and contact == "password":
        call()
    elif name.lower() == "admin" and contact != "password":
        messagebox.showinfo("Login Failed", "Invalid Password")
    elif name.lower() != "admin" and contact == "password":
        messagebox.showinfo("Login Failed", "Invalid Username")
    else:
        messagebox.showinfo("Login Failed", "Invalid Username and Password")

def submit(entry5, entry6, entry7, entry8):
    a = entry5.get().strip()
    b = entry6.get().strip()
    c = entry7.get().strip()
    d = entry8.get().strip()

    if a == "" or b == "" or c == "" or d == "":
        messagebox.showinfo("Warning", "Please enter valid Credentials!")
    else:
        messagebox.showinfo("Success!", "Credentials stored!")
        print(a, b, c, d)
        call2()

def validate_age_input(char, entry):
    if char.isdigit() or char == "":
        return True
    return False

def show_course_info(selected_language):
    course_info = {
        "Java": {
            "Instructor": "John Doe",
            "Duration": "3 months",
            "Description": "Learn Java from basics to Advanced level.",
            "Price": "₹3000"
        },
        "C": {
            "Instructor": "Jane Smith",
            "Duration": "2 months",
            "Description": "Understand the fundamentals of C programming.",
            "Price": "₹2000"
        },
        "C++": {
            "Instructor": "Alice Johnson",
            "Duration": "4 months",
            "Description": "Master object-oriented programming with C++.",
            "Price": "₹4000"
        },
        "Python": {
            "Instructor": "Bob Lee",
            "Duration": "3 months",
            "Description": "Learn Python for Data science, AI, and Web-Dev.",
            "Price": "₹3000"
        }
    }

    details = course_info.get(selected_language, None)
    
    if details:
        course_details = f"Language: {selected_language}\n"
        course_details += f"Instructor: {details['Instructor']}\n"
        course_details += f"Duration: {details['Duration']}\n"
        course_details += f"Description: {details['Description']}\n"
        course_details += f"Price: {details['Price']}"

        info_label.config(text=course_details)
    else:
        info_label.config(text="")

def exitt():
    root.destroy()

def create_footer():
    label_footer = tk.Label(root, text="©Guru R Bharadwaj", bg="#000000", fg="#FFFFFF", font=("Calibri", 12))
    label_footer.pack(side="bottom", fill='x')

def create_input_frame(label_text, entry, frame, entry_width=20, entry_show=None):
    label = tk.Label(frame, text=label_text, bg="#f7f7f7", fg="#333333")
    label.pack(side="left", padx=5)

    entry_widget = tk.Entry(frame, bg="#FFFFFF", width=entry_width, show=entry_show)
    entry_widget.pack(side="left", padx=5)

    return entry_widget

def call():
    for widget in root.winfo_children():
        widget.destroy()

    label1 = tk.Label(root, text="Welcome to Bharadwaj Classes!", bg="#f7f7f7", font=("Calibri", 14), fg="#8B0000")
    label1.pack(side="top", fill='x')

    frame5 = tk.Frame(root)
    frame5.pack(pady=10, anchor="center")
    entry5 = create_input_frame("Enter your Name: ", None, frame5)

    frame6 = tk.Frame(root)
    frame6.pack(pady=10, anchor="center")

    label6 = tk.Label(frame6, text="Enter your Age: ", bg="#f7f7f7", fg="#333333")
    label6.pack(side="left", padx=5)

    validate_command = root.register(validate_age_input)
    entry6 = tk.Entry(frame6, bg="#FFFFFF", width=20, validate="key", validatecommand=(validate_command, "%P", "%W"))
    entry6.pack(side="left", padx=5)

    frame7 = tk.Frame(root)
    frame7.pack(pady=10, anchor="center")
    entry7 = create_input_frame("University's Name: ", None, frame7)

    frame4 = tk.Frame(root)
    frame4.pack(pady=10, anchor="center")

    genders = ["Male", "Female", "Prefer not to Say"]
    label4 = tk.Label(frame4, text="Gender: ", bg="#f7f7f7", fg="#333333")
    label4.pack(side="left", padx=5)

    combo_frame = ttk.Combobox(frame4, values=genders, width=20)
    combo_frame.pack(side="left", padx=5)

    frame8 = tk.Frame(root)
    frame8.pack(pady=10, anchor="center")
    entry8 = create_input_frame("Nationality: ", None, frame8)

    button_frame2 = tk.Frame(root)
    button_frame2.pack(pady=15, anchor="center")

    button2 = tk.Button(button_frame2, text="Submit", bg="#FF5733", fg="#FFFFFF", command=lambda: submit(entry5, entry6, entry7, entry8))
    button2.pack(side="left", padx=5)

    create_footer()

def call2():
    for widget in root.winfo_children():
        widget.destroy()

    label_welcome = tk.Label(root, text="Select a Course:", bg="#f7f7f7", font=("Calibri", 14), fg="#8B0000")
    label_welcome.pack(pady=10)

    frame3 = tk.Frame(root)
    frame3.pack(pady=10)

    label4 = tk.Label(frame3, text="Language: ", bg="#f7f7f7", fg="#333333")
    label4.pack(side="left", padx=5)

    languages = ["Java", "C", "C++", "Python"]
    combo_frame = ttk.Combobox(frame3, values=languages, width=28)
    combo_frame.pack(side="left", padx=5)

    global info_label
    info_label = tk.Label(root, text="", bg="#f7f7f7", font=("Calibri", 12), justify="left", anchor="w", fg="#333333")
    info_label.pack(pady=20)

    combo_frame.bind("<<ComboboxSelected>>", lambda event: show_course_info(combo_frame.get()))

    button_frame3 = tk.Frame(root)
    button_frame3.pack(pady=15, anchor="center")

    button3 = tk.Button(button_frame3, text="Submit", bg="#FF5733", fg="#FFFFFF", command=lambda: call3())
    button3.pack(side="left", padx=5)

    create_footer()

def call3():
    for widget in root.winfo_children():
        widget.destroy()

    label_welcome = tk.Label(root, text="Payment Window", bg="#f7f7f7", font=("Calibri", 14), fg="#8B0000")
    label_welcome.pack(pady=10)

    try:
        img = tk.PhotoImage(file="QR.png")
        image_label = tk.Label(root, image=img)
        image_label.image = img
        image_label.pack()
    except:
        messagebox.showinfo("Error", "QR image not found!")

    button_frame4 = tk.Frame(root)
    button_frame4.pack(pady=15, anchor="center")

    button1 = tk.Button(button_frame4, text="Done!", bg="#FF5733", fg="#FFFFFF", command=lambda: exitt())
    button1.pack(side="left", padx=5)

    create_footer()

def create_gui(root):
    label1 = tk.Label(root, text="Welcome to Bharadwaj Classes!", bg="#f7f7f7", font=("Calibri", 14), fg="#8B0000")
    label1.pack(side="top", fill='x')

    frame1 = tk.Frame(root)
    frame1.pack(pady=20, anchor="center")

    label2 = tk.Label(frame1, text="Username: ", bg="#f7f7f7", fg="#333333")
    label2.pack(side="left", padx=5)

    entry1 = tk.Entry(frame1, bg="#FFFFFF", width=20)
    entry1.pack(side="left", padx=5)

    frame2 = tk.Frame(root)
    frame2.pack(pady=5, anchor="center")

    label3 = tk.Label(frame2, text="Password: ", bg="#f7f7f7", fg="#333333")
    label3.pack(side="left", padx=5)

    entry2 = tk.Entry(frame2, bg="#FFFFFF", show="*", width=20)
    entry2.pack(side="left", padx=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=15, anchor="center")

    button1 = tk.Button(button_frame, text="Login", bg="#FF5733", fg="#FFFFFF", command=lambda: on_click(entry1, entry2))
    button1.pack(side="left", padx=5)

    create_footer()

root = tk.Tk()
root.title("Bharadwaj Classes")
root.geometry("440x400")
create_gui(root)
root.mainloop()
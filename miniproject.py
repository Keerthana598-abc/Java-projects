import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Sample Data (Database)
# -----------------------------
opportunities = {
    "Web Development": [
        {
            "company": "ABC Tech",
            "role": "Frontend Developer Intern",
            "location": "Hyderabad",
            "stipend": "₹10,000/month",
            "details": "Work on React.js projects, build UI components, and collaborate with backend team."
        },
        {
            "company": "Webify Solutions",
            "role": "Backend Developer",
            "location": "Bangalore",
            "stipend": "₹15,000/month",
            "details": "Develop APIs using Python and Django. Knowledge of databases required."
        }
    ],
    "Data Analytics": [
        {
            "company": "DataCorp",
            "role": "Data Analyst Intern",
            "location": "Chennai",
            "stipend": "₹12,000/month",
            "details": "Analyze datasets using Python, Excel, and Power BI."
        }
    ],
    "Artificial Intelligence": [
        {
            "company": "FutureAI",
            "role": "AI Intern",
            "location": "Pune",
            "stipend": "₹20,000/month",
            "details": "Work on AI models and deep learning algorithms."
        }
    ]
}

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Placement & Internship Tracker")
root.geometry("600x500")

# -----------------------------
# Clear Screen Function
# -----------------------------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# -----------------------------
# Login Screen
# -----------------------------
def login_screen():
    clear_screen()

    tk.Label(root, text="Login Page", font=("Arial", 18)).pack(pady=20)

    tk.Label(root, text="Email ID").pack()
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack(pady=5)

    def login():
        if email_entry.get() and password_entry.get():
            domain_screen()
        else:
            messagebox.showerror("Error", "Please enter Email and Password")

    tk.Button(root, text="Login", command=login).pack(pady=20)

# -----------------------------
# Domain Selection Screen
# -----------------------------
def domain_screen():
    clear_screen()

    tk.Label(root, text="Select Interested Domain", font=("Arial", 16)).pack(pady=20)

    domain_list = [
        "Web Development",
        "Data Analytics",
        "Full Stack",
        "Artificial Intelligence",
        "Machine Learning",
        "AI & ML",
        "IOT"
    ]

    selected_domain = tk.StringVar()

    dropdown = ttk.Combobox(root, textvariable=selected_domain, values=domain_list, state="readonly")
    dropdown.pack(pady=10)

    def enter_domain():
        domain = selected_domain.get()
        if domain:
            opportunity_screen(domain)
        else:
            messagebox.showerror("Error", "Please select a domain")

    tk.Button(root, text="Enter", command=enter_domain).pack(pady=20)

# -----------------------------
# Opportunities Screen
# -----------------------------
def opportunity_screen(domain):
    clear_screen()

    tk.Label(root, text=f"Opportunities in {domain}", font=("Arial", 16)).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox = tk.Listbox(frame, width=80, height=10)
    listbox.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    if domain in opportunities:
        for job in opportunities[domain]:
            listbox.insert(tk.END,
                f"{job['company']} | {job['role']} | {job['location']} | {job['stipend']}")
    else:
        listbox.insert(tk.END, "No opportunities available.")

    # -----------------------------
    # Show Details When Clicked
    # -----------------------------
    def show_details(event):
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            job = opportunities[domain][index]

            detail_window = tk.Toplevel(root)
            detail_window.title("Company Details")
            detail_window.geometry("400x300")

            tk.Label(detail_window, text=job["company"], font=("Arial", 14)).pack(pady=10)
            tk.Label(detail_window, text=f"Role: {job['role']}").pack()
            tk.Label(detail_window, text=f"Location: {job['location']}").pack()
            tk.Label(detail_window, text=f"Stipend: {job['stipend']}").pack(pady=5)
            tk.Label(detail_window, text="Job Description:", font=("Arial", 10, "bold")).pack(pady=5)

            tk.Label(detail_window, text=job["details"], wraplength=350).pack(pady=5)

            def apply_job():
                messagebox.showinfo("Success", "Applied Successfully!")
                detail_window.destroy()

            tk.Button(detail_window, text="Apply", command=apply_job).pack(pady=10)

    listbox.bind("<<ListboxSelect>>", show_details)

    tk.Button(root, text="Logout", command=login_screen).pack(pady=20)

# Start App
login_screen()
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Dữ liệu đăng nhập mẫu
USERNAME = "admin"
PASSWORD = "password"

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Đăng nhập thành công", "Chào mừng bạn đến với hệ thống!")
    else:
        messagebox.showerror("Đăng nhập thất bại", "Tên đăng nhập hoặc mật khẩu không đúng!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đăng Nhập")

# Tạo nhãn và ô nhập cho tên đăng nhập
label_username = tk.Label(root, text="Tên đăng nhập:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Tạo nhãn và ô nhập cho mật khẩu
label_password = tk.Label(root, text="Mật khẩu:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Tạo nút đăng nhập
button_login = tk.Button(root, text="Đăng Nhập", command=login)
button_login.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
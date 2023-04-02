import os
import subprocess
import tkinter as tk

# Hàm này được gọi khi người dùng ấn nút "Thực thi"
def run_program():
    num_images = int(num_images_entry.get())
    
    if num_images == 3:
        subprocess.run(["python", "program4.py"])
    elif num_images == 4:
        subprocess.run(["python", "program1.py"])
    elif num_images == 5:
        subprocess.run(["python", "program2.py"])
    else:
        # In ra thông báo nếu số lượng file không phù hợp
        status_label.config(text="Số lượng hình không hợp lệ")

# Tạo một cửa sổ Tkinter
root = tk.Tk()
root.title("Chương trình chọn và thực thi")

# Tạo một nhãn để yêu cầu người dùng nhập số lượng hình
num_images_label = tk.Label(root, text="Nhập số lượng hình (3, 4 hoặc 5):")
num_images_label.pack()

# Tạo một hộp văn bản để người dùng nhập số lượng hình
num_images_entry = tk.Entry(root)
num_images_entry.pack()

# Tạo một nút để thực thi chương trình
run_button = tk.Button(root, text="Thực thi", command=run_program)
run_button.pack()

# Tạo một nhãn để hiển thị trạng thái
status_label = tk.Label(root, text="")
status_label.pack()

# Chạy vòng lặp chính của cửa sổ Tkinter
root.mainloop()

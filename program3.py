from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import base64
from io import BytesIO

# Tạo cửa sổ để chọn file
root = Tk()
root.withdraw()
root.filename = askopenfilename(title="Chọn file ảnh")

# Cắt ảnh gốc thành hình vuông
image = Image.open(root.filename).convert("RGBA")
width, height = image.size
size = min(width, height)
left = (width - size) // 2
top = (height - size) // 2
right = left + size
bottom = top + size
image = image.crop((left, top, right, bottom))

# Resize ảnh về kích thước 900x900
image = image.resize((900, 900))

# Load ảnh và play icon
overlay = Image.open("playicon.png").convert("RGBA")
overlay = overlay.resize((180, 180))

# Chèn play icon vào ảnh
image.paste(overlay, ((image.width - overlay.width) // 2, (image.height - overlay.height) // 2), overlay)
image.save("result.png")

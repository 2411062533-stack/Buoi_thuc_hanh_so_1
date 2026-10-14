# Hoạt động 1: Cửa sổ Tkinter đầu tiên
# bài 1.1 cửa sổ cơ bản
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Cua so Tkinter dau tien")
cua_so.geometry("400x300") #rong x cao (don vi)pixel
cua_so.mainloop() # vong lap su kien, giu cua so hien tai
#bài 1.2 Tuy chinh khong cho resize va them noi dung
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Ung dung demo")
cua_so.geometry("400x300") 
cua_so.resizable(False, False) #khong cho resize
nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)
cua_so.mainloop()
#Hoat dong 2: Widget & frame - khai niem to chuc giao dien
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Vi du Frame")
cua_so.geometry("400x300")

khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)
tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue").pack(pady=10)
tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow").pack(pady=10)
cua_so.mainloop()

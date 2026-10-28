import tkinter as tk
from tkinter import messagebox
# Hàm xử lý khi bấm các nút số hoặc phép toán
def nhap(gia_tri):
    hien_tai = bien_bieu_thuc.get()
    bien_bieu_thuc.set(hien_tai + str(gia_tri))
# Hàm xóa toàn bộ màn hình tính toán
def xoa_tat_ca():
    bien_bieu_thuc.set("")
# Hàm tính toán kết quả khi bấm nút =
def tinh_toan():
    bieu_thuc = bien_bieu_thuc.get().strip()
    if not bieu_thuc:
        messagebox.showerror("Lỗi", "Vui lòng nhập biểu thức cần tính.")
        return
    try:
        # Sử dụng hàm eval để tính toán biểu thức an toàn ở mức cơ bản
        ket_qua = eval(bieu_thuc)
        bien_bieu_thuc.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho số 0.")
        bien_bieu_thuc.set("")
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ.")
        bien_bieu_thuc.set("")

# Khởi tạo cửa sổ ứng dụng
cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

# Biến lưu trữ biểu thức hiển thị trên Entry
bien_bieu_thuc = tk.StringVar()

# Tiêu đề ứng dụng
tk.Label(cua_so, text="MAY TINH BO TUI", font=("Arial", 16, "bold")).grid(
    row=0, column=0, columnspan=4, pady=15
)

# Ô Entry hiển thị biểu thức và kết quả
entry_hien_thi = tk.Entry(
    cua_so, textvariable=bien_bieu_thuc, font=("Arial", 16), justify="right", width=18
)
entry_hien_thi.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
# Định nghĩa danh sách các nút bấm của máy tính và vị trí (row, column)
cac_nut = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

# Tạo các nút bấm bằng vòng lặp và phương thức grid()
for (text, r, c) in cac_nut:
    if text == 'C':
        nut = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 12), command=xoa_tat_ca)
    elif text == '=':
        nut = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 12), command=tinh_toan)
    else:
        # Sử dụng lambda để truyền tham số vào hàm nhap
        nut = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 12), command=lambda t=text: nhap(t))
    
    nut.grid(row=r, column=c, padx=5, pady=5)

if __name__ == "__main__":
    cua_so.mainloop()
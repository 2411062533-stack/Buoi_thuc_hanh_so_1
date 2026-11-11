import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_qly_chi_tieu as db
DANH_MUC = ["An uong", "Luong", "Di lai", "Giai tri", "Tiec tung", "Bieu bo me", "Y te", "Tiet kiem"]
LOAI_GIAO_DICH = ["Thu", "Chi"]
class UngDungQuanLyChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly chi tieu ca nhan")
        self.geometry("520x480")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_muc_chi_tieu()
        

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady = 10, padx=10, fill = "x")

        tk.Label(khung_nhap, text= "So tien: ").grid(row = 0, column=0, sticky="w", pady=5)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_tien.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Loai giao dich:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_chon_loai_giao_dich = ttk.Combobox(khung_nhap, values=LOAI_GIAO_DICH, width = 28, state="readonly")
        self.o_chon_loai_giao_dich.current(1)
        self.o_chon_loai_giao_dich.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh muc: ").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_MUC, width=28, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text= "Ghi chu: ").grid(row = 3, column=0, sticky="w", pady=5)
        self.o_nhap_ghi_chu = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ghi_chu.grid(row=3, column=1, padx=10, pady=5)
        

        khung_danh_muc = tk.Frame(self)
        khung_danh_muc.pack(pady=5, padx=10, fill="both", expand = True)
        self.listbox_chitieu = tk.Listbox(khung_danh_muc, width=75, height = 14)
        self.listbox_chitieu.pack(side="left", fill="both", expand=True)
        thanh_cuon = tk.Scrollbar(khung_danh_muc, orient="vertical", command=self.listbox_chitieu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chitieu.config(yscrollcommand=thanh_cuon.set)

        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)
        
        tk.Button(khung_nut_thao_tac, text="Them tien", command=self.xu_ly_them_giao_dich).grid(row=0, column=0, pady=5)
        tk.Button(khung_nut_thao_tac, text="Xoa sach", command=self.xu_ly_xoa_sach).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut_thao_tac, text="Thong ke theo danh muc", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def xu_ly_them_giao_dich(self):
        so_tien = self.o_nhap_so_tien.get().strip()
        loai_giao_dich = self.o_chon_loai_giao_dich.get().strip()
        danh_muc = self.chon_danh_muc.get()
        ghi_chu = self.o_nhap_ghi_chu.get().strip()
        if so_tien == "" or loai_giao_dich == "":
            messagebox.showerror("Loi", "Vui long nhap so tien va loai giao dich.")
            return
        try:
            so_tien_float = float(so_tien)
        except ValueError:
            messagebox.showerror("Loi", " So tien phai la so.")
            return
        db.them_giao_dich(so_tien_float, loai_giao_dich, danh_muc, ghi_chu)
        self.o_nhap_so_tien.delete(0, tk.END)
        self.o_nhap_ghi_chu.delete(0, tk.END)
        self.o_chon_loai_giao_dich.current(0)
        self.tai_lai_danh_muc_chi_tieu()
        messagebox.showinfo("Thanh cong", f"Da them chi tieu:{so_tien} VND")
    def tai_lai_danh_muc_chi_tieu(self):
        self.listbox_chitieu.delete(0, tk.END)
        self.du_lieu_hien_tai = db.lay_toan_bo_giao_dich()
        for giao_dich in self.du_lieu_hien_tai:
            self.listbox_chitieu.insert(
                tk.END,
                f"ID: {giao_dich[0]} | "
                f"So tien: {giao_dich[1]} | "
                f"Loai: {giao_dich[2]} | "
                f"Danh muc: {giao_dich[3]} | "
                f"Ghi chu: {giao_dich[4]}"
            )
    def xu_ly_xoa_sach(self):
        lua_chon = self.listbox_chitieu.curselection()
        if not lua_chon :
            messagebox.showerror("Loi", "Vui long chon mot giao dich de xoa.")
            return
        id_giao_dich = self.du_lieu_hien_tai[lua_chon[0]][0]
        db.xoa_giao_dich(id_giao_dich)
        self.tai_lai_danh_muc_chi_tieu()
        messagebox.showinfo("Thanh cong", "Da xoa giao dich ")
    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_danh_muc()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thong bao", "Chua co du lieu ve giao dich de thong ke.")
            return
        
        cac_danh_muc = [dong[0] for dong in du_lieu_thong_ke]
        so_lan = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_danh_muc, so_lan, color="cornflowerblue")
        plt.title("So lan giao dich theo danh muc")
        plt.xlabel("Danh muc")
        plt.ylabel("So lan giao dich")
        plt.tight_layout()
        plt.show()
if __name__ == "__main__":
    ung_dung = UngDungQuanLyChiTieu()
    ung_dung.mainloop()



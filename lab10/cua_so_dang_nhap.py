# Hoạt động 5
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_dang_nhap.ui", self)  # Nạp giao diện từ file .ui
        
        # Kết nối signal - slot cho nút đăng nhập (tên widget lấy từ objectName đã đặt trong Designer)
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()
        
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du tai khoan va mat khau.")
            return
            
        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()          # Hiển thị cửa sổ giao diện lên màn hình
    sys.exit(app.exec_())  # Chạy vòng lặp sự kiện của ứng dụng
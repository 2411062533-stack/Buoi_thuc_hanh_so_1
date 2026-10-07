danh_sach_sinh_vien = [
    {"ma_sinh_vien": 1234, "ho_ten":"Bui Van Huy", "lop_hoc": "DH13C5", "ngay_thang_nam_sinh":"07/01/2005","khoa": "CNTT", "nganh_hoc":"CNTT", "noi_o":"Ha Noi", "diem_so":"9.0", "so_tin_tich_luy":"90", "so_dien_thoai":"032456", "so_can_cuoc":"012245566767", "trang_thai":"Dang hoc"},
        {"ma_sinh_vien": 1234, "ho_ten":"Bui Phuong Thao", "lop_hoc": "DH14C5", "ngay_thang_nam_sinh":"07/01/2006","khoa": "CNTT", "nganh_hoc":"CNTT", "noi_o":"Ha Noi", "diem_so":"10.0", "so_tin_tich_luy":"63", "so_dien_thoai":"032956", "so_can_cuoc":"012245566768", "trang_thai":"Dang hoc"},
            {"ma_sinh_vien": 1234, "ho_ten":"Ho Thu Hien", "lop_hoc": "DH14C5", "ngay_thang_nam_sinh":"07/06/2006","khoa": "CNTT", "nganh_hoc":"CNTT", "noi_o":"Ha Noi", "diem_so":"10.0", "so_tin_tich_luy":"63", "so_dien_thoai":"032476", "so_can_cuoc":"012245566769", "trang_thai":"Dang hoc"},
                {"ma_sinh_vien": 1234, "ho_ten":"Bui Quang Hieu", "lop_hoc": "DH14N3", "ngay_thang_nam_sinh":"07/01/2006","khoa": "Ngon ngu anh", "nganh_hoc":"Ngon ngu anh", "noi_o":"Ha Noi", "diem_so":"9.9", "so_tin_tich_luy":"70", "so_dien_thoai":"032156", "so_can_cuoc":"012245566765", "trang_thai":"Dang hoc"},
]
lich_su_nhap_hoc = []
def hien_thi_danh_sach_sinh_vien():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien hien dang trong.")
        return
    print("\n" + "=" * 175)
    print(
        f"{'Ma SV':<10}{'Ho ten':<20}{'Lop':<10}{'Ngay sinh':<15}{'Khoa':<15}"
        f"{'Nganh':<15}{'Noi o':<12}{'Diem':<8}{'Tin chi':<10}{'SDT':<15}"
        f"{'So CCCD':<18}{'Trang thai':<12}"
    )
    print("-" * 175)
    for sv in danh_sach_sinh_vien:
        print(
            f"{sv['ma_sinh_vien']:<10}{sv['ho_ten']:<20}{sv['lop_hoc']:<10}"
            f"{sv['ngay_thang_nam_sinh']:<15}{sv['khoa']:<15}{sv['nganh_hoc']:<15}"
            f"{sv['noi_o']:<12}{sv['diem_so']:<8}{sv['so_tin_tich_luy']:<10}"
            f"{sv['so_dien_thoai']:<15}{sv['so_can_cuoc']:<18}{sv['trang_thai']:<12}"
        )
    print("=" * 175)


def tim_sinh_vien_theo_ma(ma_sinh_vien):
    for sv in danh_sach_sinh_vien:
        if str(sv["ma_sinh_vien"]).strip().lower() == str(ma_sinh_vien).strip().lower():
            return sv
    return None


def xem_thong_tin_chi_tiet(ma_sinh_vien):
    sv = tim_sinh_vien_theo_ma(ma_sinh_vien)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sinh_vien}.")
        return
    print("\n" + "=" * 50)
    print("        THONG TIN HO SO SINH VIEN CHI TIET")
    print("=" * 50)
    print(f" Ma sinh vien        : {sv['ma_sinh_vien']}")
    print(f" Ho va ten           : {sv['ho_ten']}")
    print(f" Lop hoc             : {sv['lop_hoc']}")
    print(f" Ngay thang nam sinh : {sv['ngay_thang_nam_sinh']}")
    print(f" Khoa                : {sv['khoa']}")
    print(f" Nganh hoc           : {sv['nganh_hoc']}")
    print(f" Noi o hien tai      : {sv['noi_o']}")
    print(f" Diem so (GPA)       : {sv['diem_so']}")
    print(f" So tin chi tich luy : {sv['so_tin_tich_luy']}")
    print(f" So dien thoai       : {sv['so_dien_thoai']}")
    print(f" So can cuoc (CCCD)  : {sv['so_can_cuoc']}")
    print(f" Trang thai hoc tap  : {sv['trang_thai']}")
    print("=" * 50)


def tim_kiem_sinh_vien(tu_khoa):
    tu_khoa = tu_khoa.lower().strip()
    ket_qua = [
        sv for sv in danh_sach_sinh_vien
        if tu_khoa in str(sv['ma_sinh_vien']).lower() or tu_khoa in sv['ho_ten'].lower()
    ]
    if len(ket_qua) == 0:
        print(f"-> Khong tim thay sinh vien nao phu hop voi tu khoa '{tu_khoa}'.")
        return
    print(f"\n>>> KET QUA TIM KIEM ({len(ket_qua)} sinh vien):")
    for sv in ket_qua:
        print(f" - [{sv['ma_sinh_vien']}] {sv['ho_ten']} | Lop: {sv['lop_hoc']} | Khoa: {sv['khoa']} | GPA: {sv['diem_so']}")



def them_sinh_vien(ma_sinh_vien, ho_ten, lop_hoc, ngay_sinh, khoa, nganh, noi_o, diem, tin_chi, sdt, cccd):
    if tim_sinh_vien_theo_ma(ma_sinh_vien) is not None:
        print(f"-> Ma sinh vien {ma_sinh_vien} da ton tai, khong the them.")
        return
    danh_sach_sinh_vien.append({
        "ma_sinh_vien": ma_sinh_vien,
        "ho_ten": ho_ten,
        "lop_hoc": lop_hoc,
        "ngay_thang_nam_sinh": ngay_sinh,
        "khoa": khoa,
        "nganh_hoc": nganh,
        "noi_o": noi_o,
        "diem_so": diem,
        "so_tin_tich_luy": tin_chi,
        "so_dien_thoai": sdt,
        "so_can_cuoc": cccd,
        "trang_thai": "Dang hoc"
    })
    
    lich_su_nhap_hoc.append({
        "ma_sinh_vien": ma_sinh_vien,
        "ho_ten": ho_ten,
        "lop_hoc": lop_hoc,
        "ngay_nhap_hoc": "Moi ghi danh",
        "ly_do_nhap_hoc": "Nhap hoc moi"
    })
    print(f"-> Da them sinh vien {ho_ten} ({ma_sinh_vien}) thanh cong.")


def sua_thong_tin_sinh_vien(ma_sinh_vien):
    sv = tim_sinh_vien_theo_ma(ma_sinh_vien)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sinh_vien}.")
        return
    
    print(f"\n--- CAP NHAT THONG TIN SINH VIEN: {sv['ho_ten']} ({ma_sinh_vien}) ---")
    print("(Nhan Enter de giu nguyen gia tri cu)")
    
    ho_ten = input(f"Ho ten cu [{sv['ho_ten']}]: ").strip().title()
    lop_hoc = input(f"Lop cu [{sv['lop_hoc']}]: ").strip().upper()
    khoa = input(f"Khoa cu [{sv['khoa']}]: ").strip()
    nganh = input(f"Nganh cu [{sv['nganh_hoc']}]: ").strip()
    noi_o = input(f"Noi o cu [{sv['noi_o']}]: ").strip()
    
    diem_input = input(f"Diem GPA cu [{sv['diem_so']}]: ").strip()
    tin_chi_input = input(f"So tin chi cu [{sv['so_tin_tich_luy']}]: ").strip()
    sdt = input(f"SDT cu [{sv['so_dien_thoai']}]: ").strip()
    trang_thai = input(f"Trang thai cu [{sv['trang_thai']}]: ").strip()

    if ho_ten: sv["ho_ten"] = ho_ten
    if lop_hoc: sv["lop_hoc"] = lop_hoc
    if khoa: sv["khoa"] = khoa
    if nganh: sv["nganh_hoc"] = nganh
    if noi_o: sv["noi_o"] = noi_o
    if diem_input:
        try: sv["diem_so"] = float(diem_input)
        except ValueError: print("-> Diem khong hop le, giu nguyen gia tri cu.")
    if tin_chi_input:
        try: sv["so_tin_tich_luy"] = int(tin_chi_input)
        except ValueError: print("-> So tin chi khong hop le, giu nguyen gia tri cu.")
    if sdt: sv["so_dien_thoai"] = sdt
    if trang_thai: sv["trang_thai"] = trang_thai

    print(f"-> Da cap nhat thong tin cho sinh vien {ma_sinh_vien} thanh cong.")


def xoa_sinh_vien(ma_sinh_vien):
    sv = tim_sinh_vien_theo_ma(ma_sinh_vien)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sinh_vien}.")
        return
    danh_sach_sinh_vien.remove(sv)
    print(f"-> Da xoa sinh vien {sv['ho_ten']} ({ma_sinh_vien}) khoi he thong.")


def thong_ke_sinh_vien():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co du lieu sinh vien de thong ke.")
        return
    
    thong_ke_khoa = {}
    tong_diem = 0.0
    for sv in danh_sach_sinh_vien:
        k = sv["khoa"]
        thong_ke_khoa[k] = thong_ke_khoa.get(k, 0) + 1
        # Ép kiểu float(sv["diem_so"]) để tránh lỗi nếu điểm đang là kiểu string
        tong_diem += float(sv["diem_so"])

    print("\nTHONG KE SO LUONG SINH VIEN THEO KHOA:")
    print(f"{'Khoa':<25}{'So luong SV':<15}")
    print("-" * 40)
    for khoa, so_luong in thong_ke_khoa.items():
        print(f"{khoa:<25}{so_luong:<15}")
    print("-" * 40)
    print(f">>> TONG SO SINH VIEN: {len(danh_sach_sinh_vien)}")
    print(f">>> DIEM TRUNG BINH CHUNG: {tong_diem / len(danh_sach_sinh_vien):.2f}")

def xem_lich_su_nhap_hoc():
    if len(lich_su_nhap_hoc) == 0:
        print("-> Chua co ghi nhan lich su nhap hoc nao.")
        return
    print("\nLICH SU NHAP HOC / GHI DANH MOI:")
    print(f"{'Ma SV':<10}{'Ho ten':<20}{'Lop':<10}{'Ngay nhap hoc':<18}{'Ly do':<20}")
    print("-" * 80)
    for ls in lich_su_nhap_hoc:
        print(f"{ls['ma_sinh_vien']:<10}{ls['ho_ten']:<20}{ls['lop_hoc']:<10}{ls['ngay_nhap_hoc']:<18}{ls['ly_do_nhap_hoc']:<20}")


def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


def nhap_so_thuc(loi_nhac):
    while True:
        try:
            return float(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so thuc (VD: 8.5).")


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach tat ca sinh vien")
    print("2. Xem thong tin chi tiet sinh vien")
    print("3. Tim kiem sinh vien theo Ten / Ma SV")
    print("4. Them sinh vien moi")
    print("5. Sua thong tin sinh vien")
    print("6. Xoa sinh vien")
    print("7. Thong ke sinh vien theo khoa & diem TB")
    print("8. Xem lich su nhap hoc")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_sinh_vien()
        elif lua_chon == "2":
            ma_sv = input("Nhap ma sinh vien can xem: ").strip().upper()
            xem_thong_tin_chi_tiet(ma_sv)
        elif lua_chon == "3":
            tu_khoa = input("Nhap tu khoa tim kiem: ").strip()
            tim_kiem_sinh_vien(tu_khoa)
        elif lua_chon == "4":
            ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()
            ho_ten = input("Nhap ho va ten: ").strip().title()
            lop_hoc = input("Nhap lop hoc: ").strip().upper()
            ngay_sinh = input("Nhap ngay sinh (dd/mm/yyyy): ").strip()
            khoa = input("Nhap khoa: ").strip()
            nganh = input("Nhap nganh hoc: ").strip()
            noi_o = input("Nhap noi o hien tai: ").strip()
            diem = nhap_so_thuc("Nhap diem GPA: ")
            tin_chi = nhap_so_nguyen("Nhap so tin chi tich luy: ")
            sdt = input("Nhap so dien thoai: ").strip()
            cccd = input("Nhap so CCCD: ").strip()
            them_sinh_vien(ma_sv, ho_ten, lop_hoc, ngay_sinh, khoa, nganh, noi_o, diem, tin_chi, sdt, cccd)
        elif lua_chon == "5":
            ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
            sua_thong_tin_sinh_vien(ma_sv)
        elif lua_chon == "6":
            ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
            xoa_sinh_vien(ma_sv)
        elif lua_chon == "7":
            thong_ke_sinh_vien()
        elif lua_chon == "8":
            xem_lich_su_nhap_hoc()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()

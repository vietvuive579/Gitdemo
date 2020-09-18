class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xin_chao(self):
        return "Xin chao, ta chinh la " + self.ten 
        #print("suc manh cua ta la ", self.suc_manh)

sieu_nhan_A = SieuNhan("do", "Kiem", "Do")


print(SieuNhan.xin_chao(sieu_nhan_A)) # một cách gọi khác nhưng rất không phổ biến

print(sieu_nhan_A.suc_manh)

sieu_nhan_A.xin_chao()


from xulytaikhoan import *


def main():
    global dang_nhap_status, user
    dang_nhap_status = False
    if dang_nhap_status == False:
        dang_nhap()
    if user == 'admin':
      menu_admin()
      choice = int(input('Bạn Chọn: '))
      if choice == 1:
           admin_quan_ly_tai_khoan()
      elif choice == 2:
           admin_nap_tien()
      elif choice == 3:
           admin_statistics()
      elif choice ==4: 
           dang_nhap_status = False
           print('Bye!')
    else:
      menu_user()
      choice = int(input('Bạn Chọn: '))
      if choice == 1:
           choi_lan_1()
           choi_lo()
           main()
      elif choice == 2:
           user_nap_tien()
           main()
      elif choice ==33: 
           dang_nhap_status = False
           print('Bye!')       

tien_co = 0
tien_cuoc = 0
user = 'NONE'
dang_nhap_status = False
main()

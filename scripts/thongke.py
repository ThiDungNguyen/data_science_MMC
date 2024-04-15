from .xulyfile import *
from .mypath import *

def admin_statistics():
  global path
  if not os.path.exists(f'{path}/choilo.txt'):
    write_file(f'{path}/choilo.txt', '', 'w')
  else:
    stats_lines = read_file_txt(f'{path}/choilo.txt')
    users_list = []
    tong_so_luot_choi_lo = len(stats_lines)
    tong_luot_thang = 0
    tong_luot_thua = 0
    for i in stats_lines:
      if i[1] not in users_list:
        users_list.append(i[1])
      tong_luot_thang += len(i[5])
      tong_luot_thua +=(len(i[2] -leni[5]))
    trung_binh_ty_le_thang_thua = tong_luot_thang/ tong_luot_thua
    print('Tổng số tài khoản: {len(users_list)} /n Tổng số lượt chơi game: {len(stats_lines)} \n Trung Binh tỷ lệ thắng/ thua: {trung_binh_ty_le_thang_thua}')

def user_statistics(user):
  global path
  if not os.path.exists(f'{path}/choilo.txt'):
    write_file(f'{path}/choilo.txt', '', w)
  else:
    choilo_lines = read_file_txt(f'{path}/choilo.txt')
    user_lines =[]
    for line in choilo_lines:
      line[1] == user 
      user_lines.append(line)
    so_lan_thang = 0
    tong_so_tien_thua = 0
    so_lan_thua = 0
    for i in user_lines:
      so_lan_thang += len(i[5])
      tong_so_tien_thua += (len(i[2]) - len(i[5])) * i[3]
      so_lan_thua += (len(i[2]) - len(i[5]))
    ty_le_thang_thua = so_lan_thang/so_lan_thua
    print(f'So lan choi lo: {user_lines} /n Số lần thắng lô {so_lan_thang} \n Tổng số tiền thua {tong_so_tien_thua} \n Tỷ lệ thắng/thua: {ty_le_thang_thua}')



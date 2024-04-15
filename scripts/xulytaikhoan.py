from xulyfile import *
from mypath import *
from IPython.display import clear_output
import os

def dang_nhap():
    global dang_nhap_status, user
    global path
    print('-- Game Lô Đề ---')
    print('Vui lòng đăng nhập')
    if not os.path.exists(PATH_DATA_TAI_KHOAN):
      lines = 'admin,admin,0\njulie,julie,0\n'
      write_file(PATH_DATA_TAI_KHOAN,lines, 'w')
    lines =read_file_txt(PATH_DATA_TAI_KHOAN)
    print('lines---1',lines)
    while dang_nhap_status == False:
         user = str(input('username: '))
         password = str(input('Password: '))
         for line in lines:
           if str(line[0]) == user and str(line[1]) == password:
            dang_nhap_status = True
            break
         else:
            print('vui long dang nhap lại')

def change_pass():
    global path
    lines =read_file_txt(PATH_DATA_TAI_KHOAN)
    while change_pass == True:
      user_names = [i[0] for i in lines]
      user= input('Nhap username: ')
      if user in user_names:
        new_pass = input('Nhap new pass: ')
        change_pass == False
        break
      else:
        input('vui long dang nhap lại username: ')
    for i in lines:
      if i[0] == user:
        i = [f'{user}',f'{new_pass}']
    write_file(PATH_DATA_TAI_KHOAN,lines,'w') 

def admin_quan_ly_tai_khoan():
  if not os.path.exists(PATH_DATA_TAI_KHOAN):
    write_file(path, 'taikhoan.txt','', 'w')
  else:
    lines = read_file_txt(PATH_DATA_TAI_KHOAN)
    print('lines',lines)
    user_names = [i[0] for i in lines]
    while True:
      try:
          new_user = str(input('Nhap ten new user: (NONE for cancle)'))
          if new_user == 'NONE':
            break
          elif new_user in user_names:
            new_user = str(input('username exists!, Nhap lai: '))
          elif new_user not in user_names:
            new_user_pass = str(input('Nhap pass cho new user: '))
            lines.append([f'{new_user}',f'{new_user_pass}','0'])
            print('lines',lines)
            break
      except ValueError as e:
            print(e)
    while True:
      try:
        del_user = str(input('Nhap user name muốn xoa: (NONE for cancle)'))
        if del_user in user_names:
          for i in lines:
            if i[0] == del_user:
              i =''
              break
        elif del_user == 'NONE':
          break
        elif del_user not in user_names:
          del_user = str(input('username khong ton tai, Nhap lai username: '))
      except ValueError as e:
            print(e)
    print('lines--3',lines)
    lines_str =''
    for line in lines:
      lines_str += ','.join(line) + '\n'
    write_file(PATH_DATA_TAI_KHOAN,lines_str,'w')

def admin_nap_tien():
    global tien_co, user, path
    while True:
      try:
        nap_cho_user = str(input(f'Nap tien cho username ? (NONE to exits): '))
        lines = read_file_txt(PATH_DATA_TAI_KHOAN)
        user_names = [i[0] for i in lines]
        if nap_cho_user in user_names:
          so_tien_nap = float(input('So tien muon nap: '))
          for i in lines:
            if i[0] == nap_cho_user:
              i[2] = float(i[2]) + so_tien_nap
              break
          lines_str =''
          for line in lines:
            lines_str += ','.join(map(str, line)) + '\n'
          write_file(PATH_DATA_TAI_KHOAN,lines_str,'w')
        elif nap_cho_user == 'NONE':
          break
        else:
          print('username khong ton tai! Nhap lai username')
      except ValueError as e:
        print(e)

def user_nap_tien():
    global tien_co, user, path
    while tien_co <=0:
      try:
         tien_nap = float(input(f'số tiền hiện có của bạn là: {tien_co}. Nhap so tien Nap  (0 for exit)?'))
         if tien_nap > 0:
             tien_co += tien_nap
             break
         elif tien_nap == 0:
             print(f'Cám ơn bạn đã chơi gam nô đề. số tiền hiện tại của bạn là: {tien_co}. Chúc bạn may mắn lần sau')
             break
         else:
             print('Nhap so tien lon hon 0')
      except ValueError as e:
         print(e)
    lines = read_file_txt(PATH_DATA_TAI_KHOAN)
    for i in lines:
        if i[0] == user:
          i[2] = float(i[2]) + tien_nap

    lines_str =''
    for line in lines:
      lines_str += ','.join(map(str, line)) + '\n'
    write_file(PATH_DATA_TAI_KHOAN, lines_str, 'w')      


import random
from .xlytaikhoan import *
import numpy as np
import sys, os
import random
from datetime import datetime


def hàm_quay_số(n=7):
    random_numbers = []
    for _ in range(n):
        number = random.randint(0, 99999)
        number = str(number).zfill(5)
        random_numbers.append(number)
    print(f"danh sách các số trúng giải là:")
    for i in range(len(random_numbers)):
        print(f"Giải {i+1} là: {random_numbers[i]} \n")
    so_trung_giai = []
    for so in random_numbers:
        so_trung_giai.append(so[-2:])
    return so_trung_giai  

def nhap_so_lo_de():
    global user, tien_cuoc
    while True:
        try:
            cac_so_de = str(input('Nhập số đề: từ 0 đến 99, cách nhau bằng dấu phẩy: '))
            cac_so_de = cac_so_de.split(',')
            print('cac_so_de', cac_so_de)
            so_de_verified = []
            so_de_unsatisfied = []
            for so in cac_so_de:
                so = so.strip()
                if so.isdigit() and (0 <= int(so) <= 99):
                    so_de_verified.append(so)
                else:
                    so_de_unsatisfied.append(so)
            if so_de_unsatisfied:
                raise ValueError("Số đề không đạt yêu cầu. Vui lòng nhập lại.")
            elif len(so_de_verified)* tien_cuoc > tien_co:
              print(f'nhap lai {int(tien_co/tien_cuoc)} so lo!')
            else:
                print('số đề đã nhập:',so_de_verified)
                return so_de_verified
        except ValueError as e:
            print(e)

def nhap_tien_cuoc():
    global tien_co
    while True:
        try:
            tien_cuoc = int(input(" số tiền cược: (0 to exit)"))
            if tien_cuoc > tien_co:
                print("Số tiền cược phải nhỏ hơn số tiền đang có. Vui lòng nhập lại. ")
            else:
                return tien_cuoc
        except ValueError:
           print("Số tiền cược không phải là chữ số. Vui lòng nhập lại tiền cược.")

def hàm_quyết_định_trúng_thưởng(tien_cuoc, so_de_verified, so_trung_giai):
    global tien_co,user
    cac_so_trung = []
    cac_so_thua = []
    for so_de in so_de_verified:
        if so_de in so_trung_giai:
            tien_co = tien_co + tien_cuoc*70
            cac_so_trung.append(so_de)
        else:
            tien_co = tien_co - tien_cuoc
            cac_so_thua.append(so_de)
    if len(cac_so_trung) != 0:
        print(f'chúc mừng bạn! Bạn đã trúng {len(cac_so_trung)} nháy, số tiền bạn đang có: {tien_co}')
        print(f'các số trúng lô: {cac_so_trung}')
    else:
        print(f'Bạn đã thua lô, số tiền bạn đang có: {tien_co}')
        print(f'Các số thua lô: {cac_so_thua}')

    current_time = datetime.now()
    content=[f'{current_time}', f'{user}',f'{so_de_verified}', f'{tien_cuoc}', f'{so_trung_giai}', f'{cac_so_trung}']
    content_str = ','.join(content) + '\n'
    write_file(f'{path}/choilo.txt',content_str,'a')
    lines = read_file_txt(f'{path}/taikhoan.txt')
    for line in lines:
      if line[0] == user:
        line[2] = tien_co

    lines_str =''
    for line in lines:
      lines_str += ','.join(map(str, line)) + '\n'
    write_file(f'{path}/taikhoan.txt',lines_str,'w')
    
    return tien_co

def choi_lan_1():
    global tien_co, user
    lines = read_file_txt(f'{path}/taikhoan.txt')
    for line in lines:
      if line[0] == user:
        tien_co = float(line[2])
    while tien_co <= 0: 
      user_nap_tien()
      while tien_co >0:
        tien_cuoc = nhap_tien_cuoc()
        so_de = nhap_so_lo_de()
        random_numbers = hàm_quay_số()
        tien_co = hàm_quyết_định_trúng_thưởng(tien_cuoc, so_de, random_numbers)

def choi_lo():
    global tien_co, tien_cuoc
    while int(tien_co) >0:
         tien_cuoc = nhap_tien_cuoc()
         if tien_cuoc == 0:
          break
         else:
           so_de = nhap_so_lo_de()
           random_numbers = hàm_quay_số()
           tien_co = hàm_quyết_định_trúng_thưởng(tien_cuoc, so_de, random_numbers)
           if tien_co ==0:
             tien_co = user_nap_tien()

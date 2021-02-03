import os

# 1. 해당 폴더로 이동
os.chdir(r'C:\Users\jwp05\Desktop\원표\SSAFY\자율학습\C반\4기_C반_DB_3일차')

# 2. 해당 폴더(현재 폴더 -> .)에 있는 모든 파일 목록을 리스트로 받는다.
filenames = os.listdir('.') # filenames -> list
# print(type(filenames))
# 3. 반환 받을 파일 목록의 이름을 반복을 통해 변경

for filename in filenames:
    old_num = filename[2:5]
    new_num = format(int(old_num) - 43, '03')
    new_filename = filename.replace(old_num, new_num)
    os.rename(filename, new_filename)
    # print(filename)
    # os.rename(filename, f'SAMSUNG_{filename}')
    # new_filename = filename.replace('SAMSUNG_', 'SSAFY_')
    # print(new_filename)
    # os.rename(filename, new_filename)
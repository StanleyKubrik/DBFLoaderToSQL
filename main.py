import os

base_path = '//192.168.4.2//Z//1C_Bases//kolbaska//'  # 'C:\\Users\\SUPERMAN\\Documents\\2022_01_13\\'
tree = os.walk(base_path)
folder = []
for i in tree:
    folder.append(i)
files = folder[0][2]
for i in files:
    if i.endswith('.DBF'):
        file_size = os.path.getsize(folder[0][0] + i)
        print(i, file_size)

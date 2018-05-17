
import os

# 代码目录
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
print(BASE_DIR)

# 数据文件目录
data_path = os.path.join(BASE_DIR, 'data')
print(data_path)

# 数据文件名
school_file = os.path.join(data_path, 'school')
print(school_file)


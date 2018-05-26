
import os

# 代码目录
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
print(BASE_DIR)

# 数据文件目录
data_file = os.path.join(BASE_DIR, 'data')

# 数据文件
school_file = os.path.join(data_file, 'school')




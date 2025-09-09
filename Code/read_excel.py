import pandas as pd

# 指定Excel文件路径
excel_file_path = '/Users/yux/Documents/Github_File/learn_Python/Code/TEST.xlsx'

# 使用pandas的read_excel函数读取Excel文件
# 如果Excel文件的第一行包含列名，可以使用header=0参数，否则可以省略这个参数。
# 如果要读取特定工作表，可以使用sheet_name参数指定工作表的名称或索引。
df = pd.read_excel(excel_file_path, header=0)

# 打印读取的数据框（DataFrame）的前几行
print(df.head())

# 如果需要访问特定列的数据，可以使用列名：
# column_data = df['ColumnName']

# 如果需要访问特定行的数据，可以使用行号或标签：
# row_data = df.loc[row_index]
import os
import difflib

def file_diff(directory):
    try:
    
        n_files = 0

        # 使用 os.listdir 获取指定目录下的所有文件和文件夹
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        # 打印文件列表
        print(f"Files in {directory}:")
        for file in files:
            # 仅处理*.CSV文件
            if file[-4:].upper() == '.CSV':
                
                print(f"File name: {file}")

                new_file_path = ""
                
                file_path = directory+"/"+file

                with open(file_path,'r') as f1
                






    except FileNotFoundError:
        print(f"The specified directory '{directory}' does not exist.")
    except Exception as e:
        print(f"1-An error occurred: {e}")


# 指定目录路径
directory_path = '/Users/yux/Downloads/F'

# 调用函数，列出指定目录下的文件
file_diff(directory_path)
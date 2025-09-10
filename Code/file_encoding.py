import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        encoding = result.get('encoding')
        confidence = result.get('confidence')
        print(f"文件编码: {encoding}")
        print(f"置信度: {confidence}")

if __name__ == "__main__":
    file_path = input("请输入要检测的文件路径: ")
    detect_file_encoding(file_path)
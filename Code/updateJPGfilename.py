import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime

# 该脚本根据JPG文件Exif信息中的DateTimeOriginal（标记0x9003）来更新文件名。
# 新文件名格式为：%Y%m%d-%H%M%S.JPG
#
# JPG文件的Exif数据是一种元数据，它包含了图像的各种信息，如拍摄时间、相机型号等。
# DateTimeOriginal是Exif数据中的一个标准标签，用于记录图像数据生成的原始日期和时间。
# 对于数码相机来说，这个时间通常是指照片拍摄的时间。
# 标签ID: 0x9003 (十进制: 36867)
# 更多关于Exif标签的信息可以参考: https://exiv2.org/tags.html


def list_files_in_directory(directory):
    """
    列出指定目录下的所有*.JPG文件，并基于Exif信息中的拍摄时间重命名这些文件。
    
    参数:
        directory (str): 要处理的目录路径。

    说明:
        - 该函数会遍历指定目录下的所有文件。
        - 只处理扩展名为'.JPG'或'.jpg'的图片文件。
        - 从每个JPG文件的Exif数据中提取DateTimeOriginal标签（标记0x9003），该标签记录了图像数据生成的原始日期和时间。
        - 使用提取到的日期时间信息重新命名文件。
        - 如果文件没有Exif数据，则跳过重命名操作。
    """
    try:
        n_files = 0  # 记录已处理文件数

        # 使用os.listdir获取目录下所有文件和子目录列表
        # 过滤得到仅包含文件的列表
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        print(f"Files in {directory}:")

        # 遍历文件列表
        for file in files:
            # 只处理扩展名为'.JPG'或'.jpg'的图片文件
            if file[-4:].upper() == '.JPG':
                print(f"File name: {file}

                new_file_path = ""
                
                file_path = directory+"/"+file

                img = Image.open(file_path)

                # 获取图像的Exif数据
                exif_data = img._getexif()


                # 如果存在 Exif 数据
                # Standard Exif Tags https://exiv2.org/tags.html 
                # 0x9003	36867	Photo	Exif.Photo.DateTimeOriginal	Ascii	The date and time when the original image data was generated. For a digital still camera the date and time the picture was taken are recorded.
                
                if exif_data is not None:
                    # 获取 DateTimeOriginal 标签/数据, '2016:07:13 15:22:29'，暂不考虑标签无值场景
                    exif_tag = TAGS.get(0x9003)
                    exif_value = exif_data.get(0x9003)
                    print(f"  {exif_tag}: {exif_value}")

                    new_file_path = directory+"/"+exif_value[0:4]+exif_value[5:7]+exif_value[8:10]+"-"+exif_value[11:13]+exif_value[14:16]+exif_value[17:19]+'.JPG'
                    
                    img.close()

                    os.rename(file_path, new_file_path)
                    n_files = n_files + 1

                    print(f"  File name modifie to: {new_file_path}")


                else:

                    img.close()



        print(f"Total files: {n_files}")


    except FileNotFoundError:
        print(f"The specified directory '{directory}' does not exist.")
    except Exception as e:
        print(f"1-An error occurred: {e}")



# 指定目录路径,模式
directory_path = '/Users/yux/Downloads/F'

# 调用函数，列出指定目录下的文件
list_files_in_directory(directory_path)
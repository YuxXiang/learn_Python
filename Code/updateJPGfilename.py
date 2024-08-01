import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime

# 根据JPG文件Exif中的DateTimeOriginal（0x9003	36867）更新文件名，文件名格式：%Y%m%d-%H%M%S.JPG


def list_files_in_directory(directory):
    try:

        n_files = 0

        # 使用 os.listdir 获取指定目录下的所有文件和文件夹
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        # 打印文件列表
        print(f"Files in {directory}:")
        for file in files:
            # 仅处理*.JPG文件
            if file[-4:].upper() == '.JPG':
                
                print(f"File name: {file}")

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
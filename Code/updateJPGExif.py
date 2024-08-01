import os
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import datetime




# --- AI created ---
# def change_exif_date(file_path, new_date):
#     try:
#         # Open the image file
#         img = Image.open(file_path)
        
#         # Check if the image has Exif data
#         if 'exif' in img.info:
#             # Load the Exif data
#             exif_dict = piexif.load(img.info['exif'])
            
#             # Update the DateTimeOriginal tag with the new date
#             exif_dict['Exif'][36867] = new_date.encode('utf-8')
            
#             # Dump the modified Exif data
#             new_exif_data = piexif.dump(exif_dict)
            
#             # Save the image with the modified Exif data
#             img.save(file_path, exif=new_exif_data)
            
#             print(f"Exif data is modified for {file_path}")
#         else:
#             print(f"The image {file_path} does not have Exif data.")
#     except Exception as e:
#         print(f"An error occurred: {e}")



def modify_exif_date(file_path, process_type):
    try:
        print(file_path)

        # 打开图像文件
        img = Image.open(file_path)

        s_format = "%Y:%m:%d %H:%M:%S"

        # 查看文件模式，基于Pillow库
        if process_type == "only_show":

            # 获取图像的Exif数据
            exif_data = img._getexif()

            # 如果存在 Exif 数据
            # Standard Exif Tags https://exiv2.org/tags.html 
            # 0x9003	36867	Photo	Exif.Photo.DateTimeOriginal	Ascii	The date and time when the original image data was generated. For a digital still camera the date and time the picture was taken are recorded.
            # 0x9004	36868	Photo	Exif.Photo.DateTimeDigitized	Ascii	The date and time when the image was stored as digital data.

            if exif_data is not None:
                # 获取 DateTimeOriginal 标签/数据
                exif_tag = TAGS.get(0x9003)
                exif_value = exif_data.get(0x9003)
                print(f"  {exif_tag}: {exif_value}")

                # 原有拍摄时间后退1天，获取新拍摄时间
                # 由DateTimeOriginal标签值获取拍摄时间，后退1日，并转换为Bytes字符串
                # new_dto = bytes(datetime.datetime.strftime((datetime.datetime.strptime(exif_value, s_format) + datetime.timedelta(days=-1)),s_format), encoding='utf-8')
                
                # 原有拍摄时间增加10年，获取新拍摄时间
                # 直接修改标准时间字符串中，年数据
                new_exif_time = str(int(exif_value[:4]) + 10) + exif_value[4:]
                new_dto = bytes(new_exif_time, encoding='utf-8')





                # 获取 DateTime 标签/数据
                exif_tag = TAGS.get(0x9004)
                exif_value = exif_data.get(0x9004)
                print(f"  {exif_tag}: {exif_value}")

                # # 获取 DateTime 标签/数据
                # exif_tag = TAGS.get(0x0132)
                # exif_value = exif_data.get(0x0132)
                # print(f"  {exif_tag}: {exif_value}")

                print(f'  New dto: {new_dto}')

            else:
                print("  该图像没有 Exif 数据。")


        # 修改文件模式：使用piexif库, 基于Pillow库没成功 :-(
        if process_type != "only_show":
            exif_dict = piexif.load(img.info['exif'])  # get info dict

            # if there are not exif data you could set a structure like this
            if exif_dict is not None: 
                # 获取原始拍摄时间
                s_dto = str((exif_dict['Exif'][36867]), 'utf-8')
                print(f"  DateTimeOriginal: {s_dto}")

                # 由DateTimeOriginal标签值获取拍摄时间，后退1日，并转换为Bytes字符串
                # sn_new_dto = bytes(datetime.datetime.strftime((datetime.datetime.strptime(s_dto, s_format) + datetime.timedelta(days=-1)),s_format), encoding='utf-8')
                
                # 原有拍摄时间增加10年，获取新拍摄时间
                # 直接修改标准时间字符串中，年数据
                new_exif_time = str(int(s_dto[:4]) + 10) + s_dto[4:]
                sn_new_dto = bytes(new_exif_time, encoding='utf-8')


                print(f"  New DateTimeOriginal: {sn_new_dto}")

                exif_dict['Exif'][36867] = sn_new_dto  # this ->(['Exif'][36867])<- could be 
                exif_dict['Exif'][36868] = sn_new_dto  # this ->(['Exif'][36867])<- could be 

                # different, check in your info dict structure
                # print(exif_dict)  # check new info dict structure
                new_exif_data = piexif.dump(exif_dict)  # set new exif data
                img.save(file_path, exif=new_exif_data)  # save a new image equal 
                print("  Exif data is modified.")
            # to original with new exif data

        
    except Exception as e:
        print(f"2-发生错误: {e}")




def list_files_in_directory(directory, process_type):
    try:

        n_files = 0

        # 使用 os.listdir 获取指定目录下的所有文件和文件夹
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        # 打印文件列表
        print(f"Files in {directory}:")
        for file in files:
            # 仅处理*.JPG文件
            if file[-4:].upper() == '.JPG':
                file_name = directory+"/"+file
                modify_exif_date(file_name, process_type)
                n_files = n_files + 1

        print(f"Total files: {n_files}")


    except FileNotFoundError:
        print(f"The specified directory '{directory}' does not exist.")
    except Exception as e:
        print(f"1-An error occurred: {e}")



# 指定目录路径,模式
directory_path = '/Users/yux/Downloads/F'
process_type = "only_show"

# 调用函数，列出指定目录下的文件
list_files_in_directory(directory_path, process_type)
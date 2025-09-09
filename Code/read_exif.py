from PIL import Image
import piexif


# 指定 JPEG 文件路径
file_path = '/Users/yux/Downloads/F/20160709-193410.JPG'


# change date in a image exif data
image = Image.open(file_path)  # open image
exif_dict = piexif.load(image.info['exif'])  # get info dict

# print(exif_dict)  # check info dict structure

# if there are not exif data you could set a structure like this
if exif_dict is not None: 
    
    new_date = exif_dict['Exif'][36867]
    
    print(str(new_date, 'utf-8'))

    # exif_dict['Exif'][36867] = new_date  # this ->(['Exif'][36867])<- could be 
    # exif_dict['Exif'][36868] = new_date  # this ->(['Exif'][36867])<- could be 

    # different, check in your info dict structure
    # new_exif_data = piexif.dump(exif_dict)  # set new exif data
    # image.save(file_path, exif=new_exif_data)  # save a new image equal 
# to original with new exif data


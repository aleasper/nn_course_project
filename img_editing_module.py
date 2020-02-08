import numpy as np
from PIL import Image
import os

def get_Y_img(path_to_jpg):
    image = Image.open(path_to_jpg)
    ycbcr = image.convert('YCbCr')
    y, cb, cr = ycbcr.split()
    y.save(r'.\temp_y.jpg')
    with open(r'.\temp_y.jpg', 'rb') as imgfile:
        file_raw_cd = imgfile.read()
    return file_raw_cd

def get_imgcode_arr(path):
    img = get_Y_img(path)
    img_code = get_imgcode(img)
    arr = (get_array_from_imgcode((200, 200), img_code))
    return arr

def get_imgcode(img_str):
    i = 0
    i_last =0
    for i in range(len(img_str)):
        if img_str[i_last] == 255 and img_str[i] == 218:
            break
        i_last = i
    img_code = [img_str[item] for item in range(i, len(img_str))]
    return img_code

def get_array_from_imgcode(size, img_code):
    i = 0
    arr = np.empty(size)
    for k in range(size[0]):
        for j in range(size[1]):
            if i < len(img_code):
                arr[k, j] = img_code[i]
                i += 1
            else:
                i = 0
                k -= 1
                j -= 1
    return arr

def clear_temp():
    os.remove(r'.\temp_y.jpg')

class BadPath(Exception):
    def __init__(self):
        self.error_text = "Incorrect path"

def get_array_of_images(dir_path):
    parts_array = []
    for i in range(25):
        img = Image.open(os.path.join(dir_path, "IMG_PART-%s.jpeg" % i))
        parts_array.append(img)
    return parts_array

def crop_generator(file_path, crop_h, crop_w):
    img_crop = Image.open(file_path)
    img_w, img_h = img_crop.size
    for i in range(img_w//crop_h):
        for j in range(img_w//crop_w):
            box = (j*crop_w, i*crop_h, (j+1)*crop_w, (i+1)*crop_h)
            yield img_crop.crop(box)

def compress_image(original_img_path, new_img_path, quality_lvl):
    new_img = Image.new('RGB', (500, 500))
    new_img.paste(Image.open(original_img_path))
    print("paste success")
    new_img.save(new_img_path, "JPEG", quality=quality_lvl)
    # os.path.join(path1, "Collected90.jpeg")

def crop_image(image_path, save_path, w_crop, h_crop, start_number):
    file_to_crop = image_path
    # collect_image(path2)
    for number, piece in enumerate(crop_generator(file_to_crop, h_crop, w_crop), start_number):
        img = Image.new('RGB', (h_crop, w_crop), 255)
        img.paste(piece)
        path = os.path.join(save_path, "IMG_PART-%s.jpeg" % number)
        img.save(path)

def verify_open_path(path):
    try:
        if not os.path.exists(path):
            raise BadPath
        return True
    except BadPath as error:
        print(error.error_text)
        return False





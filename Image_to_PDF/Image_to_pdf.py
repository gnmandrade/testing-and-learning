# -*- coding: utf-8 -*-
"""
Script to detect all jpg, jpeg and png files in a directory,
put them in the same orientation and store in a pdf.
"""

import os
import pathlib
from PIL import Image

import Config

wdir = Config.wdir
files_folder = Config.output_path
output_pdf_path = Config.outpdf_path

list_dir = os.scandir(files_folder)


list_files = [path for path in pathlib.Path(files_folder).rglob('*.*')]
list_files_filtered = list()
list_files_images = list()

for item in list_files:
    item_path = str(item)
    
    if item_path.endswith('.jpg') or item_path.endswith('.jpeg') or item_path.endswith('.png'):
        list_files_filtered = list_files_filtered + [item_path]
        with Image.open(item_path) as image:
            temp_img = image.convert('RGB')
            temp_img_size = temp_img.size
            
            if temp_img_size[0] > temp_img_size[1]:
                temp_img = temp_img.rotate(90, expand = True)
            
            temp_img = temp_img.resize((2880, 3868))
            
            list_files_images = list_files_images + [temp_img]
    
    print(item_path)


first_img = list_files_images[0]
rest_of_img = list_files_images[1:]

first_img.save(output_pdf_path, save_all = True, append_images = rest_of_img)
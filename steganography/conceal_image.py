#!/usr/bin/env python

import sys
from numpy import array
from PIL import Image
import steganography_utils as st

if __name__ == "__main__":

    ori_img_path = "./originals/duck.jpg"
    sec_img_path = "./originals/penguin.png"
    enc_img_path = "./encoded/duck_with_secret.png"

    if len(sys.argv) > 1:

        ori_img_path = sys.argv[1]
        sec_img_path = sys.argv[2] 
        enc_img_path = sys.argv[3] 

    ori_img = Image.open(ori_img_path)
    sec_img = Image.open(sec_img_path)
    
    ori_array = array(ori_img)
    sec_array = array(sec_img)
    
    enc_img = st.encode(ori_array, sec_array)

    ori_img.show('Original image.')
    sec_img.show('Image to be hidden.')
    enc_img.show('Encoded image.')

    enc_img.save(enc_img_path, "PNG")

#!/usr/bin/env python

import sys
from numpy import array
from PIL import Image
import steganography_utils as st

if __name__ == "__main__":

    enc_img_path = "./encoded/duck_with_secret.png"
    dec_img_path = "./decoded/decoded_img.png"

    if len(sys.argv) > 1:

        enc_img_path = sys.argv[2] 
        dec_img_path = sys.argv[3] 

    enc_img = Image.open(enc_img_path)

    dec_img = st.decode(enc_img)

    enc_img.show('Encoded image.')
    dec_img.show('Decoded image.')
    dec_img.save(dec_img_path)

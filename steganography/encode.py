from PIL import Image
from numpy import array

code = 1

def encode(array1, array2):

    if len(array1) != len(array2):
        print "Images not same length"
        return false

    for j in range(0, len(array1)):
        for i in range(0, len(array1[0])):
            newVal = (array1[j, i, 2] >> 1 << 1) | array2[j, i]
            array1[j, i, 2] = newVal

    out = Image.fromarray(array1, 'RGB')
    return out


def decode(codedim):
    imdata = array(codedim)
    length = len(imdata)

    for ipix in range(0, 500):
        for jpix in range(0, 500):
            format_bin = format(imdata[ipix, jpix, 2], '08b')
            bit = (int(format_bin) % 2)

            imdata[ipix, jpix, 0] = 255 * (1-bit)
            imdata[ipix, jpix, 1] = 255 * (1-bit)
            imdata[ipix, jpix, 2] = 255 * (1-bit)

    out = Image.fromarray(imdata, 'RGB')
    return out

im1 = Image.open("img/duck.jpg")
im2 = Image.open("img/p1bw.png")

array1 = array(im1)
array2 = array(im2)

encoded = encode(array1, array2)
encoded.show()

decoded = decode(encoded)
decoded.show()

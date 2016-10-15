from PIL import Image
from numpy import array


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
    out.show()
    return out


# Steganography challange

Steganography is the practice of concealing a file, message, image, or video within another file,
message, image, or video. (See: [Wikipedia][wiki-steganography])


**Image containing a secret message:**

![Encoded image][img-encoded]

**The concealed image:**

![Decoded image][img-decoded]

**Encoding method used:**

Overwriting the least significant bit of each pixel of the original image to contain the black and
white image.

[img-original]: originals/duck.jpg
[img-concealed]: originals/penguin.png
[img-encoded]: encoded/duck_with_secret.png
[img-decoded]: decoded/decoded_img.png
[wiki-steganography]: https://en.wikipedia.org/wiki/Steganography

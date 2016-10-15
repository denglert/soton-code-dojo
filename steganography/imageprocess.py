from PIL import Image
from numpy import array

code=1

def process_image( codedim ):
	imdata = array( codedim )

	length = len( imdata )
	print 'Length of the input image: ', length

	#for pix in range(0, length):
	for ipix in range(0, 500):
		for jpix in range(0, 500):
#	for ipix in range(0, 2):
#		for jpix in range(0, 2):
#			binary = bin( imdata[ipix][jpix][code] ) 
	#		print ( imdata[pix] )
	#		print ( binary )
			format_bin = format( imdata[ipix, jpix, 2], '08b')
#			print ( format_bin )
			bit = (int(format_bin) % 2)

#			print 'bit: ', bit
#
#			print '0', imdata[ipix,jpix,0]
#			print '1', imdata[ipix,jpix,1]
#			print '2', imdata[ipix,jpix,2]
#
			imdata[ipix,jpix,0] = 255 * bit
			imdata[ipix,jpix,1] = 255 * bit
			imdata[ipix,jpix,2] = 255 * bit
#			print '0', imdata[ipix,jpix]
#			print '1', imdata[ipix,jpix]
#			print '2', imdata[ipix,jpix]


		#	decoded = Image.new(1, (500, 500), 0 )

	out = Image.fromarray(imdata, 'RGB' )
	out.show()
##########

	return 0


image_filename="duck.jpg"
im = Image.open( image_filename	)

process_image(im)

# im.show()

#print( array )





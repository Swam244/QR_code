from pyqrcode import create
from sys import argv
query = ""
qr = create('{}'.format(query))
qr.png('qrcode_1{}.png'.format(query).replace('www.',''), scale=5)

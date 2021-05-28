import pyqrcode
import png
from pyqrcode import QRCode

s="Name :- V. Phani Raj\nPhone :- 8919165613"

url = pyqrcode.create(s)
  
url.svg("myqr.svg", scale = 8)
  
url.png('myqr.png', scale = 6)




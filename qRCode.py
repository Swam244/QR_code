from pyqrcode import create
from sys import argv
query = "Nirav"
qr = create('{}'.format(query))
qr.png('qrcode_1{}.png'.format(query).replace('www.',''), scale=5)



# from weather import Weather, Unit
# key = "xF3ItVGYToPBaEn674GSGEPJ824CLAdgJ4mhthX5"
# weather = Weather(unit=Unit.CELSIUS)
# lookup = weather.lookup_by_latlng(lat=20.904221,lng=74.774895)
# condition = lookup.condition
# print(condition.text)
from datetime import datetime 
import pytz

#locale.setlocale(locale.LC_ALL, '')

dt = datetime.now(pytz.timezone('Asia/Tokyo'))

timeStamp = dt.strftime("%m-%d-%Y_%H:%M:%S")

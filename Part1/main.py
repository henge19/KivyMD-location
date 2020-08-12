from kivymd.app import MDApp
from locationmapview import LocationMapView
from gpshelper import GpsHelper
#main.py import etmediğim için başta çalışmadı

class MainApp(MDApp):
    def on_start(self):
        #gps başlat
        GpsHelper().run()


MainApp().run()
from kivy.app import App
#for worked on mobile
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class GpsHelper():
    has_centered_map=False
    def run(self):

        #get a reference to GpsBlinker,then call blink()
        gps_blinker=App.get_running_app().root.ids.mapview.ids.blinker
        #start blinking the GpsBlinker
        gps_blinker.blink()
        pass

        #Request permission on Android
        if platform == "android":
            from android.permission import Permission,requests_permissions

            def callback(permission,results):
                if all([res for res in results]):
                    print("Got all permissions")
                    from plyer import gps
                    gps.configure(on_location=self.update_blinker_position,
                                  on_status=self.on_auth_status)
                    gps.start(minTime=1000,minDistance=0)

                else:
                    print("Did not get all permissions")

            #we put these two parameter inside of buildozer.spec file
            requests_permissions([Permission.ACCESS_COARSE_LOCATION,
                                  Permission.ACCESS_FINE_LOCATION],callback)


        #configure GPS
        if platform == "ios":
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000,minDistance=0)


    #on_location pass to function  update_blinker_position.it is took lat,lon and values and pass to kwargs.
    def update_blinker_position(self,*args,**kwargs):
        my_lat=kwargs['lat']
        my_lon=kwargs["lon"]

        print("GPS POSITION",my_lat,my_lon)
        #update GpsBlinker position
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.lat=my_lat
        gps_blinker.lon=my_lon

        #Center Map on GPS.First we reference to the app
        if not self.has_centered_map:
            map=App.get_running_app().root.ids.mapview
            map.center_on(my_lat,my_lon)
            self.has_centered_map=True


    #when on_status function in line 18 recive a  new status  it passes 2 variables.
    def on_auth_status(self,general_status,status_message):

        if general_status=="provider-enabled": #that means we got gps position
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog=MDDialog(title="GPS Error",text="You need to enable to GPS access for the app to function properly")
        dialog.size_hint=[.8,.8]
        dialog.pos_hint={'center_x':.5,'center_y':.5}
        dialog.open()

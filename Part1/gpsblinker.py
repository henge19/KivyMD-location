from kivy_garden.mapview import MapMarker
from kivy.animation import Animation

class GpsBlinker(MapMarker):
    def blink(self):
        #it will change the blink size and opacity
        anim=Animation(outer_opacity=0 ,blink_size=50)
        #when animation done , it resets the animation and repeat.we bind to animation to that
        anim.bind(on_complete=self.reset)
        #it will start the animation on GpsBlinker
        anim.start(self)

    #reset function
    def reset(self,*args):
        self.outer_opacity=1
        self.blink_size=self.default_blink_size
        #for repeat to process
        self.blink()
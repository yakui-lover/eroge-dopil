

init python:
    
    
    
    
    import random
    
    
    random.seed()
    
    
    
    
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
            This creates the snow effect. You should use this function instead of instancing
            the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
            using the default values =D)
    
            @parm {image} image:
                The image used as the snowflakes. This should always be a image file or an im object,
                since we'll apply im transformations in it.
    
            @parm {int} max_particles:
                The maximum number of particles at once in the screen.
    
            @parm {float} speed:
                The base vertical speed of the particles. The higher the value, the faster particles will fall.
                Values below 1 will be changed to 1
    
            @parm {float} wind:
                The max wind force that'll be applyed to the particles.
    
            @parm {Tuple ({int} min, {int} max)} xborder:
                The horizontal border range. A random value between those two will be applyed when creating particles.
    
            @parm {Tuple ({int} min, {int} max)} yborder:
                The vertical border range. A random value between those two will be applyed when creating particles.
                The higher the values, the fartest from the screen they will be created.
            """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    
    class SnowFactory(object):
        """
            The factory that creates the particles we use in the snow effect.
            """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
                Initialize the factory. Parameters are the same as the Snow function.
                """
            
            self.max_particles = max_particles
            
            
            self.speed = speed
            
            
            self.wind = wind
            
            
            self.xborder = xborder
            self.yborder = yborder
            
            
            
            
            self.depth = kwargs.get("depth", 10)
            
            
            self.image = self.image_init(image)
        
        
        def create(self, particles, st):
            """
                This is internally called every frame by the Particles object to create new particles.
                We'll just create new particles if the number of particles on the screen is
                lower than the max number of particles we can have.
                """
            
            if particles is None or len(particles) < self.max_particles:
                
                
                depth = random.randint(1, self.depth)
                
                
                
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      
                                          random.uniform(-self.wind, self.wind)*depth_speed,  
                                          self.speed*depth_speed,  
                                          random.randint(self.xborder[0], self.xborder[1]), 
                                          random.randint(self.yborder[0], self.yborder[1]), 
                                          ) ]
        
        
        def image_init(self, image):
            """
                This is called internally to initialize the images.
                will create a list of images with different sizes, so we
                can predict them all and use the cached versions to make it more memory efficient.
                """
            rv = [ ]
            
            
            for depth in range(self.depth):
                
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )
            
            return rv
        
        
        def predict(self):
            """
                This is called internally by the Particles object to predict the images the particles
                are using. It's expected to return a list of images to predict.
                """
            return self.image
    
    
    class SnowParticle(object):
        """
            Represents every particle in the screen.
            """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
                Initializes the snow particle. This is called automatically when the object is created.
                """
            
            
            self.image = image
            
            
            
            
            if speed <= 0:
                speed = 1
            
            
            self.wind = wind
            
            
            self.speed = speed
            
            
            
            self.oldst = None
            
            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
        
        
        def update(self, st):
            """
                Called internally in every frame to update the particle.
                """
            
            
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
            
            
            if self.ypos > renpy.config.screen_height or\
                   (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                
                return None
            
            
            
            
            return int(self.xpos), int(self.ypos), st, self.image

init:
    image snow = Snow("images/1080/anim/snow.png")
    image heavy_snow = Snow("images/1080/anim/snow.png", max_particles=500)

    $ flash = Fade(1, 0, 1, color="#fff")
    $ flash2 = Fade(2, 2, 2, color="#fff")
    $ flash_red = Fade(1, 0, 1, color="#e11")
    $ fade3 = Fade(1.5, 0, 1.5)
    $ fade2 = Fade(1, 0, 1)
    $ dissolve2 = Dissolve(2)
    $ dspr = Dissolve(.2)

    $ backdrop = "prologue"

init python:
    
    import itertools
    locations = ["bg ext_aidpost", "bg ext_beach", "bg ext_boathouse", "bg ext_clubs", "bg ext_dining_hall_away", "bg ext_library", "bg ext_house_of_mt", "bg ext_playground", "bg ext_road", "bg ext_square", "bg int_dining_hall"]
    variations = ["night", "sunset", "day"]
    all_loc = ["%s_%s" % (location, variation) for (location, variation) in itertools.product(locations, variations)]
    
    
    
    
    
    if persistent.endings == None:
        persistent.endings = {
                    "main_good":False,
                    "main_bad":False,
                    "dv_good":False,
                    "dv_bad":False,
                    "sl_good":False,
                    "sl_bad":False,
                    "un_good":False,
                    "un_bad":False,
                    "us_good":False,
                    "us_bad":False,
                    "mi":False,
                    "uv_city":False,
                    "uv_unknown_fucken_shit":False
                    }
    
    
    
    if persistent.CardsDemo == None:
        persistent.CardsDemo = False
    
    if persistent.CardsFail == None:
        persistent.CardsFail = False
    
    if persistent.CardsWon1 == None:
        persistent.CardsWon1 = False
    
    if persistent.CardsWon2 == None:
        persistent.CardsWon2 = False
    
    if persistent.CardsWon3 == None:
        persistent.CardsWon3 = False
    
    if persistent.hentai == None:
        persistent.hentai = False
    
    if persistent.foobar == None:
        persistent.foobar = False



init:

    python:
        
        import math
        
        class Shaker(object):
            
            anchors = {
                        'top' : 0.0,
                        'center' : 0.5,
                        'bottom' : 1.0,
                        'left' : 0.0,
                        'right' : 1.0,
                        }
            
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):
            
            move = Shaker(start, child, dist=dist)
            
            return renpy.display.layout.Motion(move,
                                  time,
                                  child,
                                  add_sizes=True,
                                  **properties)
        
        Shake = renpy.curry(_Shake)



init:

    $ lp_dv = 0
    $ lp_sl = 0
    $ lp_un = 0
    $ lp_us = 0
    $ lp_uv = 0

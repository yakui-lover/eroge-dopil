














init -50 python:
    import pygame
    import os
    import os.path
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite
    
    def any_time(time):
        global time_of_day
        time_of_day = time
        reload_names()
    
    
    store.map_enabled = False
    store.map_enabled_tmp = False
    def disable_stuff():
        store.map_enabled_tmp = store.map_enabled_tmp or store.map_enabled
        store.map_enabled = False
    def enable_stuff():
        store.map_enabled = store.map_enabled_tmp
        store.map_enabled_tmp = False
    
    
    class Sandwich(Composite):
        def __init__(self, base_directory, *images, **properties):
            args = []
            for image in images:
                args.extend([(0, 0), base_directory + '/' + image])
            super(Sandwich, self).__init__(None, *args, **properties)
    
    class VerticalCrop(ImageBase):
        def __init__(self, im, y, h, **properties):
            im = image(im)
            super(VerticalCrop, self).__init__(im, y, h, **properties)
            self.image = im
            self.y = y
            self.h = h
        
        def load(self):
            surf = cache.get(self.image)
            width, _ = surf.get_size()
            return surf.subsurface((0, self.y, width, self.h))
    
    
    
    def get_name():
        pattern = "screenshot%04d.png"
        i = 1
        while True:
            fn = pattern % i
            if not os.path.exists(fn):
                break
            i += 1
        return fn
    
    
    
    
    if persistent.falling_bar_speed==None:
        persistent.falling_bar_speed=128
    def get_falling_bar_speed():
        if persistent.falling_bar_speed==0:
            return 1.0
        else:
            return persistent.falling_bar_speed / 256.0
    
    def screen_recount(x,y):
        return (x/float(config.screen_width), y/float(config.screen_height))
    
    class WidgetContainer(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.buttons=[]
            self.enabled=True
            config.overlay_functions.append(self.widgets_overlay)
        def disable(self):
            self.enabled=False
        def enable(self):
            self.enabled=True
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        def hide_elem(self, name):
            for i in self.buttons:
                if  i["name"]==name:
                    i["visible"]=0
        def show_elem(self, name):
            for i in self.buttons:
                if  i["name"]==name:
                    i["visible"]=1
        def is_visible(self, name):
            for i in self.buttons:
                if  i["name"]==name:
                    if i["visible"]:
                        return True
            return False
        def widgets_overlay(self):
            if self.enabled:
                self.widgets_specific()
    
    class WidgetSet(WidgetContainer):
        def __init__(self):
            WidgetContainer.__init__(self)
        def add(self,name,im1,im2,cl,x,y,v=1):
            self.buttons.append({"name":name,"elem":(im1,im2,cl,x,y),"visible":v})
        def widgets_specific(self):
            for i in self.buttons:
                if i["visible"]:
                    b = i["elem"]
                    ui.imagebutton(b[0],b[1],clicked=b[2],xpos=b[3],ypos=b[4])
    
    class WidgetBar(WidgetContainer):
        SHOWN   = 1.0
        SHOWING = 0.75
        HIDING  = 0.25
        HIDDEN  = 0.0
        
        def is_shown(self):
            return self.state == self.SHOWN
        def is_showing(self):
            return self.state == self.SHOWING
        def is_hiding(self):
            return self.state == self.HIDING
        def is_hidden(self):
            return self.state == self.HIDDEN
        
        def set_shown(self):
            self.state = self.SHOWN
        def set_showing(self):
            self.state = self.SHOWING
        def set_hiding(self):
            self.state = self.HIDING
        def set_hidden(self):
            self.state = self.HIDDEN
        
        def recount_x(self):
            x = config.screen_width
            for i in self.buttons:
                if i["visible"]:
                    x -= self.arr_dx
            if x!= config.screen_width:
                x += self.arr_dx - self.button_h
            self.arr_x=x/2
        
        def __init__(self,arr_y,arr_dx,arr_dy,button_h):
            WidgetContainer.__init__(self)
            self.arr_y=arr_y
            self.arr_dx=arr_dx
            self.arr_dy=arr_dy
            self.button_h=button_h
            self.recount_x()
            self.set_hidden()
        def event(self, ev, x, y, st):
            if st>=get_falling_bar_speed():
                x,y = pygame.mouse.get_pos()
                if y < self.button_h+self.arr_y*2 and self.is_hidden():
                    self.set_showing()
                    renpy.restart_interaction()
                if y > self.button_h+self.arr_y*2 and self.is_shown():
                    self.set_hiding()
                    renpy.restart_interaction()
            else:
                renpy.timeout(0.1)
        def safe_exec(self,click):
            disable_stuff()
            click()
            enable_stuff()
        def add(self,name,im1,im2,click,v=1):
            cl = renpy.curry(self.safe_exec)(click)
            self.buttons.append({"name":name,"elem":(im1,im2,cl),"visible":v})
        def show_button(self,img1,img2,cl,x,y):
            ui.layer('widgetoverlay')
            if self.is_showing():
                ui.at(Move(
                        screen_recount(x,-self.button_h),
                        screen_recount(x,y),
                        get_falling_bar_speed()
                    ))
            if self.is_hiding():
                ui.at(Move(
                        screen_recount(x,y),
                        screen_recount(x,-self.button_h),
                        get_falling_bar_speed()
                    ))
            ui.imagebutton(img1,img2,clicked=cl,xpos=x,ypos=y)
            ui.close() 
        def widgets_specific(self):
            if not self.is_hidden():
                self.recount_x()
                x = self.arr_x
                y = self.arr_y
                for i in self.buttons:
                    if i["visible"]:
                        b = i["elem"]
                        self.show_button(b[0],b[1],b[2],x,y)
                        x = x + self.arr_dx
                        y = y + self.arr_dy
                if self.is_showing():
                    self.set_shown()
                if self.is_hiding():
                    self.set_hidden()
    
    class WidgetBarWithPlashka(WidgetBar):
        def __init__(self,arr_y,arr_dx,arr_dy,button_h,plashka,plashka_dy,plashka_xstep):
            WidgetBar.__init__(self,arr_y,arr_dx,arr_dy,button_h)
            self.plashka = plashka
            self.plashka_dy = plashka_dy
            self.plashka_xstep = plashka_xstep
        def update_plashka(self,plashka):
            self.plashka = plashka
        def widgets_specific(self):
            renpy.scene('widgetoverlay')
            if not self.is_hidden():
                self.recount_x()
                y = self.arr_y+self.plashka_dy
                lx = int(self.arr_x-self.plashka_xstep)
                rx = int(self.arr_x+self.plashka_xstep - self.arr_dx)
                for i in self.buttons:
                    if i["visible"]:
                        rx += int(self.arr_dx)
                self.show_button(self.plashka["left"],self.plashka["left"],None,lx,y)
                lx += self.plashka_xstep
                while lx<rx:
                    self.show_button(self.plashka["center"],self.plashka["center"],None,lx,y)
                    lx += int(self.plashka_xstep)
                self.show_button(self.plashka["right"],self.plashka["right"],None,lx,y)
            WidgetBar.widgets_specific(self)
        def disable(self):
            WidgetContainer.disable(self)
            renpy.scene('widgetoverlay')
    
    
    
    class KeychainListener(renpy.Displayable):
        def __init__(self, code, target):
            renpy.Displayable.__init__(self)
            self.target = target
            self.state = 0
            self.code = code
        def event(self, ev, x, y, st):
            if ev.type != pygame.KEYDOWN:
                return
            if ev.key != self.code[self.state]:
                self.state = 0
                return
            self.state += 1
            if self.state == len(self.code):
                self.state = 0
                self.target()
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
    
    class MultiKeychainListener(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.array={}
            config.overlay_functions.append(self.keychains_overlay)
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        
        def add(self,name,code,target,v=1):
            self.array[name] = {"elem":KeychainListener(code,target),"visible":v}
        
        def keychains_overlay(self):
            for name,i in self.array.iteritems():
                if i["visible"]:
                    ui.add(i["elem"])
    
    
    
    class WatchDogs(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.arr=[]
        def add(self,assertion,errortext):
            self.arr.append((assertion,errortext))
        def event(self, ev, x, y, st):
            for a,e in self.arr:
                if(eval(a)!=True):
                    renpy.error(e)
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
    
    
    
    class SoundDogs(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.max_volume = {}
            for i in range(0,7):
                self.max_volume[i] = 1             
            self.real_volume = self.max_volume
            self.target_volume = self.max_volume
            self.delta = 0.001
            self.delay = 3
        def chan_down(self,i):
            self.target_volume[i] = 0              
        def chan_up(self,i):
            self.target_volume[i] = 1              
        def event(self, ev, x, y, st):
            b = False
            for i in range(0, 7):
                if self.real_volume[i]<self.target_volume[i]:
                    self.real_volume[i]+=self.delta
                    b = True
                if self.real_volume[i]>self.target_volume[i]:
                    self.real_volume[i]-=self.delta
                    b = True
                renpy.sound.set_volume(self.real_volume[i], channel=i) 
                renpy.music.set_volume(self.real_volume[i], channel=i)
            if b:
                renpy.game.interface.timeout(1.0)
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)



init -50 python:
    
    global_map_result="error"
    
    def init_map_zones_realization(zones,default):
        global global_zones
        global_zones=zones
        for i,data in global_zones.iteritems():
            data["chibi"] = None
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0
    
    class Map(renpy.Displayable):
        def __init__(self,pics,chibi,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default = default
            config.overlay_functions.append(self.overlay)
        
        def disable_all_zones(self):
            global global_zones
            for name,data in global_zones.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
        def enable_all_zones(self):
            global global_zones
            for name,data in global_zones.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0
        def set_zone(self,name,label):
            global global_zones
            global_zones[name]["label"] = label
            global_zones[name]["avaliable"] = True
        def reset_zone(self,name):
            global global_zones
            global_zones[name]["label"] = self.default
            global_zones[name]["avaliable"] = False
            global_zones[name]["been_here"] = 0
        def enable_empty_zone(self,name):
            global global_zones
            self.set_zone(name,self.default)
            global_zones[name]["avaliable"] = True
        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result)
        def disable_current_zone(self):
            global global_zones
            global_zones[global_map_result]["avaliable"] = False
        def been_there(self):
            global global_zones
            return global_zones[global_map_result]["been_here"]
        def set_chibi(self,name,ch):
            global global_zones
            if  ch in self.chibi:
                global_zones[name]["chibi"] = self.chibi[ch]
            else:
                global_zones[name]["chibi"] = None
        def reset_chibi(self,name):
            self.set_chibi(name,"")
        
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        
        def zoneclick(self,name):
            global global_zones
            global global_map_result
            store.map_enabled=False
            renpy.scene('mapoverlay')
            global_zones[name]["been_here"] += 1
            global_map_result = name
            renpy.scene()
            
            if not not_in_rollback_or_fast_forward():
                
                renpy.log("renpy.roll_forward_info()")
                
                renpy.config.skipping = False
                renpy.game.after_rollback = False
            ui.jumps(global_zones[name]["label"])()
        
        def overlay(self):
            if  store.map_enabled:
                global global_zones
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in global_zones.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                                im.Crop(self.pics["avaliable"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                                im.Crop(self.pics["selected"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                                clicked = renpy.curry(self.zoneclick)(name),
                                xpos = pos[0],
                                ypos = pos[1]
                            )
                        if  data["chibi"] != None:
                            ui.imagebutton(
                                    anim.Blink(data["chibi"]),
                                    anim.Blink(data["chibi"]),
                                    clicked = renpy.curry(self.zoneclick)(name),
                                    xpos = pos[0],
                                    ypos = pos[1]
                                )
                ui.close() 
    
    store.map = Map(store.map_pics, store.map_chibi, default)


label _show_map:
    scene widget map 
    $ store.map_enabled = True
    $ ui.interact()
    jump _show_map

label nothing_here:
    python:
        random = renpy.random.choice([
                             u"Тут ничего нет",
                             u"Мне нечего тут делать",
                             u"Пойду-ка я лучше еще куда-нибудь"
                         ])
    "%(random)s"
    jump _show_map

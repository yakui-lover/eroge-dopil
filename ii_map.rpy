init -41 python:
    store.map_zones = {
                "un_mi_house":   {"position":[804,146,853,203,0,0],"default_bg":bg_tmp_image(u"Уныл и Мику")},
                "me_mt_house":   {"position":[957,173,1007,231,0,0],"default_bg":bg_tmp_image(u"Мой домик")},
                "sl_mz_house":   {"position":[1020,243,1079,309,0,0],"default_bg":bg_tmp_image(u"Славя и Мицу-тян")},
                "estrade":       {"position":[1061, 49,1157,145,0,0],"default_bg":bg_tmp_image(u"Эстрада")},
                "sy_sh_house":   {"position":[843,283,891,340,0,0],"default_bg":bg_tmp_image(u"Сыроега и Шурик")},
                "music_club":    {"position":[622,250,701,342,0,0],"default_bg":bg_tmp_image(u"Музклуб")},
                "admin_house":   {"position":[772,352,880,448,0,0],"default_bg":bg_tmp_image(u"Админкорпус")},
                "wash_house":    {"position":[694,438,791,527,0,0],"default_bg":bg_tmp_image(u"Банно-прачечная")},
                "square":        {"position":[885,352,1003,545,0,0],"default_bg":bg_tmp_image(u"Площадь")},
                "dining_hall":   {"position":[1010,449,1145,585,0,0],"default_bg":bg_tmp_image(u"Столовая")},
                "dv_us_house":   {"position":[711,615,768,674,0,0],"default_bg":bg_tmp_image(u"Дваче и СССР")},
                "store_house":   {"position":[1148,489,1215,583,0,0],"default_bg":bg_tmp_image(u"Склад")},
                "valleyball":    {"position":[1222,488,1320,602,0,0],"default_bg":bg_tmp_image(u"Воллейбол")},
                "sport_area":    {"position":[1321,478,1579,658,0,0],"default_bg":bg_tmp_image(u"Спорткомплекс")},
                "beach":         {"position":[1185,666,1492,831,170,40],"default_bg":bg_tmp_image(u"Пляж")},
                "boat_station":  {"position":[831,771,962,856,0,0],"default_bg":bg_tmp_image(u"Лодочный причал")},
                "old_house":     {"position":[228,993,347,1080,0,0],"default_bg":bg_tmp_image(u"Старый корпус")},
                "clubs":         {"position":[430,440,651,603,50,0],"default_bg":bg_tmp_image(u"Клубы")},
                "library":       {"position":[1160,273,1286,363,0,0],"default_bg":bg_tmp_image(u"Библиотека")},
                "badminton":     {"position":[1343,378,1448,475,0,0],"default_bg":bg_tmp_image(u"Бадминтон")},
                "medic_house":   {"position":[1037,357,1137,450,0,0],"default_bg":bg_tmp_image(u"Медпункт")},
                "camp_entrance": {"position":[271,432,424,567,0,0],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
                "forest":        {"position":[550,60,697,199,0,0],"default_bg":bg_tmp_image(u"о. Лес")},
        }

    def init_map_zones_realization(zones,default):
        global global_zones
        global_zones=zones
        for i,data in global_zones.iteritems():
            data["chibi"] = []
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0

    class IIMap(Map):
        def __init__(self, pics, chibi, default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default = default
            config.overlay_functions.remove(store.map.overlay)
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones
            for name,data in global_zones.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
                data["chibi"] = []

        def set_chibi(self,name,chib):
            global global_zones
            if type(chib) == str:
                chib = [chib]
            for ch in chib:
                if  ch in self.chibi:
                    global_zones[name]["chibi"].append(self.chibi[ch])
                else:
                    global_zones[name]["chibi"] = []
                    break

        def reset_chibi(self,name):
            self.set_chibi(name,"")

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
                        if len(data["chibi"]) == 1:
                            ui.imagebutton(
                                    anim.Blink(data["chibi"][0]),
                                    anim.Blink(data["chibi"][0]),
                                    clicked = renpy.curry(self.zoneclick)(name),
                                    xpos = pos[0]+pos[4],
                                    ypos = pos[1]+pos[5]
                                )
                        elif len(data["chibi"]) == 2:
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][0]),
                                   anim.Blink(data["chibi"][0]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]-25,
                                   ypos = pos[1]+pos[5]
                               )
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][1]),
                                   anim.Blink(data["chibi"][1]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]+25,
                                   ypos = pos[1]+pos[5]
                               )
                        elif len(data["chibi"]) == 3:
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][0]),
                                   anim.Blink(data["chibi"][0]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4],
                                   ypos = pos[1]+pos[5]-25
                               )
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][1]),
                                   anim.Blink(data["chibi"][1]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]-25,
                                   ypos = pos[1]+pos[5]+25
                               )
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][2]),
                                   anim.Blink(data["chibi"][2]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]+25,
                                   ypos = pos[1]+pos[5]+25
                               )
                        elif len(data["chibi"]) == 4:
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][0]),
                                   anim.Blink(data["chibi"][0]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]-25,
                                   ypos = pos[1]+pos[5]-25
                               )
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][1]),
                                   anim.Blink(data["chibi"][1]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]+25,
                                   ypos = pos[1]+pos[5]-25
                               )
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][2]),
                                   anim.Blink(data["chibi"][2]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]-25,
                                   ypos = pos[1]+pos[5]+25
                               )
                           ui.imagebutton(
                                   anim.Blink(data["chibi"][3]),
                                   anim.Blink(data["chibi"][3]),
                                   clicked = renpy.curry(self.zoneclick)(name),
                                   xpos = pos[0]+pos[4]+25,
                                   ypos = pos[1]+pos[5]+25
                               )
                ui.close() 
    
    store.map = IIMap(store.map_pics, store.map_chibi, default)



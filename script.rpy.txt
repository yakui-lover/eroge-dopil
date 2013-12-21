
init -999:
    transform backdrop_trans:
        xalign -0.2
        linear 2.0 xalign 0.0
        pause 3.0

    transform achievement_trans:
        align (1.1, 0.97)
        ease 1.0 align (0.85, 0.97)
        ease 0.5 align (0.95, 0.97)

    image backdrop_back = "images/1080/anim/backdrop/back.jpg"

    image backdrop_new:
        pause 0.1
        "images/1080/anim/backdrop/1.png" 
        pause 0.1
        "images/1080/anim/backdrop/2.png" 
        pause 0.1
        "images/1080/anim/backdrop/3.png" 
        pause 0.1
        "images/1080/anim/backdrop/2.png" 
        repeat

    $ style.backdrop_text = Style(style.default)
    $ style.backdrop_text.color = "#fff"
    $ style.backdrop_text.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.backdrop_text.drop_shadow_color = "#000"
    $ style.backdrop_text.italic = False
    $ style.backdrop_text.bold = False
    $ style.backdrop_text.size = 80

init 5 python:
    
    import renpy.store as store
    
    if  not config_session:
        
        def show_achievement(img):
            renpy.play(sfx_achievement)
            renpy.show(img, [achievement_trans])
            renpy.pause(3.5)
            renpy.hide(img)
        
        class FunctionCallback(Action):
            def __init__(self,function,*arguments):
                self.function=function
                self.arguments=arguments
            def __call__(self):
                return self.function(self.arguments)
        
        def on_load_callback(slot):
            try:
                if persistent.on_save_timeofday[slot]:
                    persistent.timeofday = persistent.on_save_timeofday[slot][0]
                    persistent.sprite_time = persistent.on_save_timeofday[slot][1]
                    persistent.font_size = persistent.on_save_timeofday[slot][2]
                    persistent.hentai = persistent.on_save_timeofday[slot][3]
                    _preferences.volumes['music'] = persistent.on_save_timeofday[slot][4]
                    _preferences.volumes['sfx'] = persistent.on_save_timeofday[slot][5]
                    _preferences.volumes['voice'] = persistent.on_save_timeofday[slot][6]
            
            except:
                pass
        
        def on_save_callback(slot):
            if not persistent.on_save_timeofday:
                persistent.on_save_timeofday={}
            persistent.on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, persistent.hentai, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])
        
        def do_rollback(cnt):
            if not d2_cardgame_block_rollback:
                k=cnt[0]
                renpy.rollback(True, k)
        
        
        def new_chapter(day_number,chapter_name="",mode="adv",music_stop=False):
            global save_name
            global _window_subtitle
            
            
            
            
            renpy.scene()
            renpy.show("bg black")
            renpy.pause(0.5)
            
            if backdrop == "prologue":
                
                
                
                pass
            elif backdrop == "epilogue":
                
                renpy.show("backdrop_back")
                renpy.show("day_num",what=Text("День ...",style=style.backdrop_text,ypos=0.35,xpos=0.38))
                renpy.show("backdrop_new")
                renpy.transition(dissolve)
                renpy.pause(1.0)
            else:
                dn = u'День %d'%(day_number)
                
                renpy.show("backdrop_back")
                renpy.show("day_num",what=Text(dn,style=style.backdrop_text,ypos=0.35,xpos=0.38))
                renpy.show("backdrop_new")
                renpy.transition(dissolve)
                renpy.pause(1.0)
                if backdrop == "dv":
                    renpy.show("dv normal pioneer", [backdrop_trans])
                    renpy.transition(dissolve)
                    renpy.pause(2.0)
                if backdrop == "us":
                    renpy.show("us normal pioneer", [backdrop_trans])
                    renpy.transition(dissolve)
                    renpy.pause(2.0)
                if backdrop == "sl":
                    renpy.show("sl normal pioneer", [backdrop_trans])
                    renpy.transition(dissolve)
                    renpy.pause(2.0)
                if backdrop == "un":
                    renpy.show("un normal pioneer", [backdrop_trans])
                    renpy.transition(dissolve)
                    renpy.pause(2.0)
            
            
            
            
            if music_stop:
                for i in range(0,8):
                    renpy.music.stop(channel=i)
            if day_number != -1 and day_number != 0:
                dn = u'День %d'%(day_number)
                save_name = chapter_name
            
            
            else:
                pass
                
                save_name = chapter_name
            
            
            
            
            if  backdrop != "prologue":
                renpy.pause(3.0)
                renpy.scene()
                renpy.show("bg black")
                renpy.transition(dissolve)
                renpy.pause(2.0)
            
            if (mode=="adv") :
                set_mode_adv()
            else:
                set_mode_nvl()
        
        def disable_all_zones():
            store.map.disable_all_zones()
        def enable_all_zones():
            store.map.enable_all_zones()
        def set_zone(name,label):
            store.map.set_zone(name,label)
        def reset_zone(name):
            store.map.reset_zone(name)
        def enable_empty_zone(name):
            store.map.enable_empty_zone(name)
        def reset_current_zone():
            store.map.reset_current_zone()
        def disable_current_zone():
            store.map.disable_current_zone()
        def been_there():
            return store.map.been_there()
        def set_chibi(name,ch):
            store.map.set_chibi(name,ch)
        def reset_chibi(name):
            store.map.reset_chibi(name)
        def show_map():
            ui.jumps("_show_map")()
        
        def day_time():
            any_time('day')
            persistent.timeofday='day'
        def sunset_time():
            any_time('sunset')
            persistent.timeofday='sunset'
        def night_time():
            any_time('night')
            persistent.timeofday='night'
        def prolog_time():
            any_time('prolog')
            persistent.timeofday='prologue'
        
        
        def init_map_zones():
            init_map_zones_realization(store.map_zones,"nothing_here")
        
        def possible_skip(text, lbl):
            if  skip_text_blocks:
                say("",text)
                ui.jumps(lbl)()
        
        real_map_event = renpy.display.behavior.map_event
        my_map_event = lambda ev, name: False
        real_renpy_run = renpy.display.behavior.run
        my_renpy_run = lambda name: True
        
        def nonsafe_noskip_mode():
            
            
            
            
            renpy.display.behavior.map_event = my_map_event
            renpy.display.behavior.run = my_renpy_run
        
        def nonsafe_skip_mode():
            renpy.display.behavior.map_event = real_map_event
            renpy.display.behavior.run = real_renpy_run
        
        def not_in_rollback_or_fast_forward():
            return not renpy.config.skipping and not renpy.game.after_rollback
        real_sound_play = renpy.sound.play
        renpy.sound.play = lambda file,channel="sound",fadeout=0,fadein=0,tight=False,loop=False: real_sound_play(file,channel=channel,fadeout=fadeout,fadein=fadein,tight=tight,loop=loop) if not_in_rollback_or_fast_forward() else True



label start:
    $ renpy.music.stop()
    $ skip_text_blocks = True
    $ renpy.block_rollback()
    $ prolog_time()
    $ persistent.sprite_time = "day"
    $ init_map_zones()

    python:
        if persistent.jump_to:
            j = persistent.jump_to
            persistent.jump_to = False
            
            renpy.jump(j)

    jump prologue

label splashscreen:
    $ prolog_time()
    if not persistent.licensed:
        $ lic_tab = "        "
        $ lic_tabQ = "                                              "
        $ lic_tabY = "                                                                                          "
        $ lic_tabN = "                                                                                      "
        menu:
            "%(lic_tabQ)s{color=#aaa}Вы принимаете условия {a=http://creativecommons.org/licenses/by-nc-sa/4.0/deed.ru}CC-BY-NC-SA-4.0{/a} в отношении данной игры?\n\n{size=-10}Вы можете свободно:\n\n%(lic_tab)s {b}Делиться{/b} – копировать и распространять материал на любом носителе и в любом формате.\n%(lic_tab)s {b}Адаптировать{/b} – делать ремиксы, видоизменять и создавать новое, опираясь на этот материал.\n\nПри обязательном соблюдении следующих условий:\n\n%(lic_tab)s {b}Attribution{/b} – вы должны указать авторство, предоставить ссылку на лицензию и обозначить изменения, если они были сделаны.\n%(lic_tab)s {b}NonCommercial{/b} – вы не вправе использовать этот материал в коммерческих целях.\n%(lic_tab)s {b}ShareAlike{/b} – если вы перерабатываете материал игры, вы должны распространять переделанные вами части на условиях той же лицензии.{/size}{/color}\n"
            "%(lic_tabY)s{u}Да, я принимаю условия.{/u}\n":
                $ persistent.licensed = True    
            "%(lic_tabN)s{u}Нет, я не принимаю условия.{/u}":
                $ renpy.quit()

    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            persistent.achievement = True
            
            persistent.font_size = "small"
            persistent.hentai = False
            
            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .75

    python:
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")

    $ renpy.pause(1)
    scene soviet_games  with dissolve
    if persistent.achievement:
        play sound sfx_achievement
        show achievement :
            align (1.1, 0.97)
            ease 1.0 align (0.85, 0.97)
            ease 0.5 align (0.95, 0.97)
        $ persistent.achievement = False
    $ renpy.pause(3.5)
    scene disclaimer  with dissolve
    $ renpy.pause(20)

    $ hour = int(hour)



    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene splashscreen_night  with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_night  with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
        return
    if hour in [20,21] or hour in [7,8]:
        scene splashscreen_sunset  with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_sunset  with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
        return
    else:
        scene splashscreen_day  with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_day  with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
        return

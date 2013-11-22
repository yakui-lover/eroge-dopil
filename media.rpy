init -1000 python:
    config_session = False
    def get_image(file):
        return "images/%d/%s" % (1080,file)

init -100 python:
    persistent.has_768=False
    persistent.has_1080=True
    
    store.selected_slot = "_"
    persistent._file_page = 1


init:

    transform center:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0

    transform left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0

    transform right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0

    transform fleft:
        xalign 0.16
        xanchor 0.5
        yanchor 0.0

    transform fright:
        xalign 0.84
        xanchor 0.5
        yanchor 0.0

    transform cleft:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0

    transform cright:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0





init:

    if not config_session:


        define dis = Dissolve(0.5, alpha=True)

        $ none                     = "images/misc/none.png"
        image black = "#000"
        image white = "#fff"
        image bg black = "#000"
        image bg white = "#fff"

        image bg map = get_image("maps/map_avaliable.jpg")
        image bg hall = im.Sepia(get_image("bg/int_dining_hall_day.jpg"))

        image un night = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/un/un_1_body.png",(0,0), "images/1080/sprites/normal/un/un_1_pioneer.png",(0,0), "images/1080/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) )

        image ctc_animation = Animation("images/misc/ctc01.png", 0.15, "images/misc/ctc02.png", 0.15, "images/misc/ctc03.png", 0.15, "images/misc/ctc04.png", 0.15, "images/misc/ctc05.png", 0.15, "images/misc/ctc06.png", 0.15, "images/misc/ctc07.png", 0.15, "images/misc/ctc08.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)

        image ctc_animation_nvl = Animation("images/misc/ctc01.png", 0.15, "images/misc/ctc02.png", 0.15, "images/misc/ctc03.png", 0.15, "images/misc/ctc04.png", 0.15, "images/misc/ctc05.png", 0.15, "images/misc/ctc06.png", 0.15, "images/misc/ctc07.png", 0.15, "images/misc/ctc08.png", 0.15, xpos=0.95, ypos=0.94, xanchor=1.0, yanchor=1.0)

        image op_uv:
            "images/misc/op/uv1.png" 
            pause 0.5
            "images/misc/op/uv2.png" 
            pause 0.5
            "images/misc/op/uv3.png" 
            pause 0.5
            "images/misc/op/uv2.png" 
            pause 0.5
            "images/misc/op/uv1.png" 
            pause 0.5

        image stars:
            "images/1080/anim/stars_1.jpg"  with Dissolve(1.5) 
            pause 1.5
            "images/1080/anim/stars_3.jpg"  with Dissolve(1.5) 
            pause 1.5
            repeat

        image candle:
            "images/1080/anim/candle_1.png"  with Dissolve(2.0) 
            pause 2.0
            "images/1080/anim/candle_2.png"  with Dissolve(2.0) 
            pause 2.0
            repeat

        image prologue_dream:
            "images/1080/anim/prologue_1.png" 
            pause 0.1
            "images/1080/anim/prologue_2.png" 
            pause 0.1
            "images/1080/anim/prologue_3.png" 
            pause 0.1
            "images/1080/anim/prologue_2.png" 
            repeat

        image unblink:
            contains:
                "anim blink_up" 
                xalign 0 yalign 0
                ease 1.5 pos (0,-1080)
            contains:
                "anim blink_down" 
                xalign 0 yalign 0
                ease 1.5 pos (0,1080)

        image blink:
            contains:
                "anim blink_up" 
                pos (0,-1080)
                ease 1.5 xalign 0 yalign 0
            contains:
                "anim blink_down" 
                pos (0,1080)
                ease 1.5 xalign 0 yalign 0


        image blinking:
            contains:
                "anim blink_up" 
                pos (0,-1080)
                ease 1.5 xalign 0 yalign 0
            contains:
                "anim blink_down" 
                pos (0,1080)
                ease 1.5 xalign 0 yalign 0
            pause 2.0
            contains:
                "anim blink_up" 
                xalign 0 yalign 0
                ease 1.5 pos (0,-1080)
            contains:
                "anim blink_down" 
                xalign 0 yalign 0
                ease 1.5 pos (0,1080)

        image anim 1 _prologue:
            "anim prologue_keyboard_1" 
            pause 6
            "anim prologue_keyboard_2" 
            pause 0.1
            "anim prologue_keyboard_3" 
            pause 0.1
            "anim prologue_keyboard_4" 
            pause 3
            "anim prologue_keyboard_3" 
            pause 0.1
            "anim prologue_keyboard_2" 
            pause 0.1
            "anim prologue_keyboard_1" 

        image anim 2 _prologue:
            "anim prologue_keyboard_monitor_1" 
            pause 6
            "anim prologue_keyboard_monitor_2" 
            pause 0.1
            "anim prologue_keyboard_monitor_3" 
            pause 0.1
            "anim prologue_keyboard_monitor_4" 
            pause 3
            "anim prologue_keyboard_monitor_3" 
            pause 0.1
            "anim prologue_keyboard_monitor_2" 
            pause 0.1
            "anim prologue_keyboard_monitor_1" 

        image anim 3 _prologue:
            "anim prologue_monitor_1" 
            pause 6
            "anim prologue_monitor_2" 
            pause 0.1
            "anim prologue_monitor_3" 
            pause 0.1
            "anim prologue_monitor_4" 

        image anim 4 _prologue:
            "anim prolog_15" 
            pause 6
            "anim prolog_3"  with fade3 
            pause 3
            "anim prolog_4"  with fade3 

        image owl:
            "anim owl_1" 
            pause 5
            "anim owl_2" 
            pause 0.5
            repeat

        image bg ext_square_night_flash:
            "bg ext_square_night"  with Fade(1, 1, 1, color="#fff") 
            pause 1
            "bg ext_square_night"  with Fade(1, 1, 1, color="#fff") 
            pause 1
            repeat

        $ style.credits = Style(style.default)
        $ style.credits.color = "#fff"
        $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.credits.drop_shadow_color = "#000"
        $ style.credits.italic = False
        $ style.credits.bold = False

        image credits = ParameterizedText(style = "credits", size = 50)


        $ style.urhere1 = Style(style.default)
        $ style.urhere1.color = "#eee"
        $ style.urhere1.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
        $ style.urhere1.drop_shadow_color = "#000"
        $ style.urhere1.italic = True
        $ style.urhere1.bold = False

        image urhere1 = ParameterizedText(style = "urhere1", size = 40)

        $ style.urhere2 = Style(style.default)
        $ style.urhere2.color = "#111"
        $ style.urhere2.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere2.drop_shadow_color = "#000"
        $ style.urhere2.italic = False
        $ style.urhere2.bold = False

        image urhere2 = ParameterizedText(style = "urhere2", size = 80)

        $ style.urhere3 = Style(style.default)
        $ style.urhere3.color = "#a3d"
        $ style.urhere3.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere3.drop_shadow_color = "#000"
        $ style.urhere3.italic = False
        $ style.urhere3.bold = False

        image urhere3 = ParameterizedText(style = "urhere3", size = 60)

        $ style.urhere4 = Style(style.default)
        $ style.urhere4.color = "#e34"
        $ style.urhere4.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere4.drop_shadow_color = "#000"
        $ style.urhere4.italic = False
        $ style.urhere4.bold = False

        image urhere4 = ParameterizedText(style = "urhere4", size = 100)

        $ style.urhere5 = Style(style.default)
        $ style.urhere5.color = "#d00"
        $ style.urhere5.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere5.drop_shadow_color = "#000"
        $ style.urhere5.italic = False
        $ style.urhere5.bold = False

        image urhere5 = ParameterizedText(style = "urhere5", size = 50)



        $ style.urhere6 = Style(style.default)
        $ style.urhere6.color = "#e01"
        $ style.urhere6.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
        $ style.urhere6.drop_shadow_color = "#000"
        $ style.urhere6.italic = True
        $ style.urhere6.bold = False

        image urhere6 = ParameterizedText(style = "urhere6", size = 60)

        $ style.urhere7 = Style(style.default)
        $ style.urhere7.color = "#ad5"
        $ style.urhere7.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere7.drop_shadow_color = "#000"
        $ style.urhere7.italic = False
        $ style.urhere7.bold = False

        image urhere7 = ParameterizedText(style = "urhere7", size = 30)

        $ style.urhere8 = Style(style.default)
        $ style.urhere8.color = "#a30"
        $ style.urhere8.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere8.drop_shadow_color = "#000"
        $ style.urhere8.italic = False
        $ style.urhere8.bold = True

        image urhere8 = ParameterizedText(style = "urhere8", size = 70)

        $ style.urhere8 = Style(style.default)
        $ style.urhere8.color = "#f54"
        $ style.urhere8.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere8.drop_shadow_color = "#000"
        $ style.urhere8.italic = True
        $ style.urhere8.bold = False

        image urhere8 = ParameterizedText(style = "urhere8", size = 90)

        $ style.urhere9 = Style(style.default)
        $ style.urhere9.color = "#d10"
        $ style.urhere9.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        $ style.urhere9.drop_shadow_color = "#000"
        $ style.urhere9.italic = False
        $ style.urhere9.bold = False

        image urhere9 = ParameterizedText(style = "urhere9", size = 65)

        $ style.urhere10 = Style(style.default)
        $ style.urhere10.color = "#ee1"
        $ style.urhere10.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
        $ style.urhere10.drop_shadow_color = "#000"
        $ style.urhere10.italic = True
        $ style.urhere10.bold = False

        image urhere10 = ParameterizedText(style = "urhere10", size = 30)









init:
    if not config_session:


        image cg uvao_demo_sorry = get_image("cg/uvao_demo_sorry.png")





        image cg lvl_1 = get_image("cg/cards_contest/lvl_1.jpg")
        image cg lvl_2_lena_win = get_image("cg/cards_contest/lvl_2_lena_win.jpg")
        image cg lvl_2_semen_win = get_image("cg/cards_contest/lvl_2_semen_win.jpg")
        image cg lvl_4_semen_win = get_image("cg/cards_contest/lvl_4_semen_win.jpg")







init:
    if not config_session:
        $ std_set_for_preview = {}
        $ std_set = {}
        $ store.colors= {}
        $ store.names_list=[]
        $ time_of_day = 'night'


        $ _show_two_window = True


        $ colors['voice'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
        $ store.names_list.append('voice')


        $ colors['me'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
        $ store.names_list.append('me')



        $ store.names_list.append('narrator')



        $ store.names_list.append('th')
        $ th_prefix = "«"
        $ th_suffix = "»"



        $ colors['el'] = {'night': (205, 205, 0, 255), 'sunset': (255, 255, 0, 255), 'day': (255, 255, 0, 255), 'prolog': (255, 255, 0, 255)}
        $ store.names_list.append('el')



        $ colors['un'] = {'night': (170, 100, 217, 255), 'sunset': (185, 86, 255, 255), 'day': (185, 86, 255, 255), 'prolog': (185, 86, 255, 255)}
        $ store.names_list.append('un')



        $ colors['dv'] = {'night': (210, 139, 16, 255), 'sunset': (255, 170, 0, 255), 'day': (255, 170, 0, 255), 'prolog': (255, 170, 0, 255)}
        $ store.names_list.append('dv')



        $ colors['sl'] = {'night': (214, 176, 0, 255), 'sunset': (255, 210, 0, 255), 'day': (255, 210, 0, 255), 'prolog': (255, 210, 0, 255)}
        $ store.names_list.append('sl')



        $ colors['us'] = {'night': (234, 55, 0, 255), 'sunset': (255, 50, 0, 255), 'day': (255, 50, 0, 255), 'prolog': (255, 50, 0, 255)}
        $ store.names_list.append('us')



        $ colors['mt'] = {'night': (0, 182, 39, 255), 'sunset': (0, 234, 50, 255), 'day': (0, 234, 50, 255), 'prolog': (0, 234, 50, 255)}
        $ store.names_list.append('mt')



        $ colors['cs'] = {'night': (134, 134, 230, 255), 'sunset': (165, 165, 255, 255), 'day': (165, 165, 255, 255), 'prolog': (165, 165, 255, 255)}
        $ store.names_list.append('cs')



        $ colors['mz'] = {'night': (84, 129, 219, 255), 'sunset': (114, 160, 255, 255), 'day': (74, 134, 255, 255), 'prolog': (74, 134, 255, 255)}
        $ store.names_list.append('mz')



        $ colors['mi'] = {'night': (0, 180, 207, 255), 'sunset': (0, 252, 255, 255), 'day': (0, 222, 255, 255), 'prolog': (0, 222, 255, 255)}
        $ store.names_list.append('mi')



        $ colors['dy'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('dy')



        $ colors['uv'] = {'night': (64, 208, 0, 255), 'sunset': (78, 255, 0, 255), 'day': (78, 255, 0, 255), 'prolog': (78, 255, 0, 255)}
        $ store.names_list.append('uv')



        $ colors['lk'] = {'night': (255, 128, 128, 255), 'sunset': (255, 128, 128, 255), 'day': (255, 128, 128, 255), 'prolog': (255, 128, 128, 255)}
        $ store.names_list.append('lk')
        $ help = Character("", kind=nvl)



        $ colors[ 'sh'] = {'night': (205, 194, 18, 255), 'sunset': (255, 242, 38, 255), 'day': (255, 242, 38, 255), 'prolog': (255, 242, 38, 255)}
        $ store.names_list.append('sh')


        $ colors['pi'] = {'night': (230, 0, 0, 255), 'sunset': (230, 0, 0, 255), 'day': (230, 1, 1, 255), 'prolog': (230, 0, 0, 255)}
        $ store.names_list.append('pi')


        $ colors['all'] = {'night': (227, 58, 58, 255), 'sunset': (227, 58, 58, 255), 'day': (237, 68, 68, 255), 'prolog': (227, 58, 58, 255)}
        $ store.names_list.append('all')


        $ colors['kids'] = {'night': (235, 120, 131, 255), 'sunset': (235, 120, 131, 255), 'day': (235, 120, 131, 255), 'prolog': (235, 120, 131, 255)}
        $ store.names_list.append('kids')


        $ colors['dreamgirl'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('dreamgirl')


        $ colors['bush'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('bush')


        $ colors['voices'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('voices')


        $ colors['FIXME_voice'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('FIXME_voice')


        $ colors['odn'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('odn')



        $ colors['dreamgirl'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('dreamgirl')



        $ colors['message'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('message')



        $ colors['mt_voice'] = {'night': (0, 182, 39, 255), 'sunset': (0, 234, 50, 255), 'day': (0, 234, 50, 255), 'prolog': (0, 234, 50, 255)}
        $ store.names_list.append('mt_voice')






init python:
    if not config_session:
        def set_name(who,name):
            gl = globals()
            gl[who+"_name"] = name
        
        def make_names_unknown():
            global store
            set_name('mt_voice',u"Голос")
            set_name('FIXME_voice',u"Голос")
            set_name('odn',u"Одногруппник")
            set_name('message',u"Сообщение")
            set_name('dreamgirl',u"...")
            set_name('voice',u"Голос")
            set_name('me',u"Семен")
            set_name('dy',u"Голос из динамика")
            set_name('lk',u"Луркмор-кун")
            set_name('pi',u"Пионер")
            set_name('all',u"Пионеры")
            set_name('kids',u"Малышня")
            set_name('dreamgirl',u"...")
            set_name('bush',u"Голос")
            set_name('voices',u"Голоса")
            set_name('el',u"Пионер")
            set_name('un',u"Пионерка")
            set_name('dv',u"Пионерка")
            set_name('sl',u"Пионерка")
            set_name('us',u"Пионерка")
            set_name('mt',u"Вожатая")
            set_name('cs',u"Медсестра")
            set_name('mz',u"Пионерка")
            set_name('mi',u"Пионерка")
            set_name('uv',u"Странная девочка")
            set_name('sh',u"Пионер")
        
        def make_names_known():
            global store
            set_name('mt_voice',u"Голос")
            set_name('FIXME_voice',u"Голос")
            set_name('odn',u"Одногруппник")
            set_name('message',u"Сообщение")
            set_name('dreamgirl',u"...")
            set_name('voice',u"Голос")
            set_name('me',u"Семен")
            set_name('dy',u"Голос из динамика")
            set_name('lk',u"Луркмор-кун")
            set_name('pi',u"Пионер")
            set_name('all',u"Пионеры")
            set_name('kids',u"Малышня")
            set_name('dreamgirl',u"...")
            set_name('bush',u"Голос")
            set_name('voices',u"Голоса")
            set_name('el',u"Электроник")
            set_name('un',u"Лена")
            set_name('dv',u"Алиса")
            set_name('sl',u"Славя")
            set_name('us',u"Ульяна")
            set_name('mt',u"Ольга Дмитриевна")
            set_name('cs',u"Виола")
            set_name('mz',u"Женя")
            set_name('mi',u"Мику")
            set_name('uv',u"Юля")
            set_name('sh',u"Шурик")
        
        def meet(who, name):
            set_name(who,name)
        
        def char_define(x,is_nvl=False):
            global DynamicCharacter
            global _show_two_window
            global nvl
            global store
            global time_of_day
            gl = globals()
            v = "_voice"
            if  x == 'narrator':
                if  is_nvl:
                    gl['narrator'] = Character(None, kind=nvl, what_style="narrator_%s"%time_of_day, ctc="ctc_animation_nvl", ctc_position="fixed")
                else:
                    gl['narrator'] = Character(None, what_style="narrator_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
                return
            if  x == 'th':
                if  is_nvl:
                    gl['th'] = Character(None, kind=nvl, what_style="thoughts_%s"%time_of_day,what_prefix = th_prefix,what_suffix=th_suffix, ctc="ctc_animation_nvl", ctc_position="fixed")
                else:
                    gl['th'] = Character(None, what_style="thoughts_%s"%time_of_day,what_prefix = th_prefix,what_suffix=th_suffix, ctc="ctc_animation", ctc_position="fixed")
                return
            if  is_nvl:
                gl[x] = DynamicCharacter("%s_name"%x, color=store.colors[x][time_of_day], kind=nvl, what_style="normal_%s"%time_of_day,who_suffix=":", ctc="ctc_animation_nvl", ctc_position="fixed")
                gl[x+v] = DynamicCharacter("voice_name", color=store.colors[x][time_of_day], kind=nvl,  what_style="normal_%s"%time_of_day,who_suffix=":", ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl[x] = DynamicCharacter("%s_name"%x, color=store.colors[x][time_of_day], show_two_window=_show_two_window,  what_style="normal_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
                gl[x+v] = DynamicCharacter("voice_name", color=store.colors[x][time_of_day], show_two_window=_show_two_window, what_style="normal_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
        
        def set_mode_adv():
            nvl_clear()
            
            global menu
            menu = renpy.display_menu
            
            global store
            for x in store.names_list:
                char_define(x)
        
        def set_mode_nvl():
            nvl_clear()
            
            global menu
            menu = nvl_menu
            
            global narrator
            global th
            narrator_nvl = narrator
            th_nvl = th
            
            global store
            for x in store.names_list:
                char_define(x,True)
        
        def reload_names():
            global store
            for x in store.names_list:
                char_define(x)
        
        make_names_unknown()
        set_mode_adv()
        reload_names()






init:
    if not config_session:
        image widget map = get_image("maps/map.jpg")

init -997 python:
    def bg_tmp_image(bgname):
        renpy.image("text "+bgname,LiveComposite((config.screen_width, config.screen_height),(0, 0),"#ffff7f",(50, 150),Text(u"А здесь будет фон про "+bgname, size=40, color="6A7183")))
        return "text "+bgname
    
    store.map_pics = {
            "bgpic": get_image("maps/map.jpg"),
            "avaliable": get_image("maps/map_avaliable.jpg"),
            "selected": get_image("maps/map_selected.jpg")
        }
    
    
    store.map_zones = {
                "un_mi_house":   {"position":[804,146,858,203],"default_bg":bg_tmp_image(u"Уныл и Мику")},
                "me_mt_house":   {"position":[953,173,1007,231],"default_bg":bg_tmp_image(u"Мой домик")},
                "sl_mz_house":   {"position":[1015,243,1079,309],"default_bg":bg_tmp_image(u"Славя и Мицу-тян")},
                "estrade":       {"position":[1061, 49,1157,145],"default_bg":bg_tmp_image(u"Эстрада")},
                "sy_sh_house":   {"position":[839,283,895,340],"default_bg":bg_tmp_image(u"Сыроега и Шурик")},
                "music_club":    {"position":[622,250,701,342],"default_bg":bg_tmp_image(u"Музклуб")},
                "monument":      {"position":[921,390,977,444],"default_bg":bg_tmp_image(u"Памятник вождю")},
                "admin_house":   {"position":[772,352,880,438],"default_bg":bg_tmp_image(u"Админкорпус")},
                "wash_house":    {"position":[694,440,791,527],"default_bg":bg_tmp_image(u"Банно-прачечная")},
                "square":        {"position":[890,450,986,545],"default_bg":bg_tmp_image(u"Площадь")},
                "dining_hall":   {"position":[1014,449,1145,583],"default_bg":bg_tmp_image(u"Столовая")},
                "dv_us_house":   {"position":[708,615,768,674],"default_bg":bg_tmp_image(u"Дваче и СССР")},
                "store_house":   {"position":[1148,489,1215,583],"default_bg":bg_tmp_image(u"Склад")},
                "valleyball":    {"position":[1222,488,1320,602],"default_bg":bg_tmp_image(u"Воллейбол")},
                "sport_area":    {"position":[1321,478,1579,658],"default_bg":bg_tmp_image(u"Спорткомплекс")},
                "beach":         {"position":[1185,666,1492,831],"default_bg":bg_tmp_image(u"Пляж")},
                "boat_station":  {"position":[831,771,962,856],"default_bg":bg_tmp_image(u"Лодочный причал")},
                "old_road":      {"position":[355,829,504,1080],"default_bg":bg_tmp_image(u"Дорога на старый лагерь")},
                "old_house":     {"position":[228,993,347,1080],"default_bg":bg_tmp_image(u"Старый корпус")},
                "clubs":         {"position":[430,443,654,603],"default_bg":bg_tmp_image(u"Клубы")},
                "library":       {"position":[1165,275,1286,363],"default_bg":bg_tmp_image(u"Библиотека")},
                "badminton":     {"position":[1344,379,1448,475],"default_bg":bg_tmp_image(u"Бадминтон")},
                "medic_house":   {"position":[1037,362,1132,450],"default_bg":bg_tmp_image(u"Медпункт")},
                "camp_entrance": {"position":[271,432,424,567],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
                "island_nearest":{"position":[560,937,866,1077],"default_bg":bg_tmp_image(u"о. Ближний")},
                "forest":{"position":[550,60,697,199],"default_bg":bg_tmp_image(u"о. Лес")}
            
            
        }
    
    store.map_chibi = {
            "?" : get_image("maps/map_icon_n00.png"),
            "me": get_image("maps/map_icon_n01.png"),
            "mi": get_image("maps/map_icon_n02.png"),
            "sh": get_image("maps/map_icon_n03.png"),
            "el": get_image("maps/map_icon_n04.png"),
            "mz": get_image("maps/map_icon_n05.png"),
            "mt": get_image("maps/map_icon_n06.png"),
            "uv": get_image("maps/map_icon_n07.png"),
            "un": get_image("maps/map_icon_n08.png"),
            "us": get_image("maps/map_icon_n09.png"),
            "dv": get_image("maps/map_icon_n10.png"),
            "sl": get_image("maps/map_icon_n11.png"),
            "cs": get_image("maps/map_icon_n12.png"),
        }






init:

    $ flash = Fade(.25, 0, .75, color="#fff")




init -10 python:
    if not config_session:
        avatar_frame = Frame("images/misc/avaframe.png", 5, 5)
        card_down = "images/misc/down.png"
        card_up = "images/misc/up.png"
        p = "images/avatars/dv/dv-"
        dv_avatar_set = {
                     'body':p+"body.png",
                     -2    :p+"emo9.png",
                     -1    :p+"emo8.png",
                     0     :p+"emo6.png",
                     1     :p+"emo12.png",
                     2     :p+"smile.png",
                }
        p = "images/avatars/sl/sl-"
        sl_avatar_set = {
                     'body':p+"body.png",
                     -2    :p+"emo04.png",
                     -1    :p+"emo01.png",
                     0     :p+"emo05.png",
                     1     :p+"emo02.png",
                     2     :p+"emo03.png",
                }
        p = "images/avatars/un/un-"
        un_avatar_set = {
                     'body':p+"body.png",
                     -2    :p+"emo07.png",
                     -1    :p+"emo08.png",
                     0     :p+"emo02.png",
                     1     :p+"emo01.png",
                     2     :p+"emo10.png",
                }
        p = "images/avatars/us/us-"
        us_avatar_set = {
                     'body':p+"body.png",
                     -2    :p+"emo01.png",
                     -1    :p+"emo11.png",
                     0     :p+"emo02.png",
                     1     :p+"emo03.png",
                     2     :p+"emo09.png",
                }






init python:
    
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    
    def volume(vol, chnl):
        renpy.music.set_volume(vol, channel=chnl)

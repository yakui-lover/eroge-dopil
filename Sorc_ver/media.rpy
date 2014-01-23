# Служебный скрипт.
# Описание всех ресурсов.

# ВНИМАНИЕ!
# __ВСЕ__ ДО ЕДИНОГО ВНЕШНИЕ РЕСУРСЫ ДОЛЖНЫ БЫТЬ ОБЪЯВЛЕНЫ ИСКЛЮЧИТЕЛЬНО В ЭТОМ ФАЙЛЕ!
# ПОВТОРЯЮ, ____________НИКАКИХ____________ ИМЕН ФАЙЛОВ В ТЕКСТАХ СЦЕНАРИЕВ!!!!!

# bg ---------------------------------------------------------------
init:

    #часто используемые цвета фона
    image bg black                 = "#000"
    image bg white                 = "#fff"

    image bg int_bus               = "images/bg/int_bus.jpg"
    image bg ext_bus               = "images/bg/ext_bus.jpg"
        
    image bg ext_clubs_day         = "images/bg/ext_clubs_day.jpg"
    image bg ext_camp_entrance_day = "images/bg/ext_camp_entrance_day.jpg"  
    image bg ext_houses_day = "images/bg/ext_houses_day.jpg"
    image bg ext_dining_hall_near_day = "images/bg/ext_dining_hall_near_day.jpg"
    image bg ext_dining_hall_away_day = "images/bg/ext_dining_hall_away_day.jpg"


    image bg ext_square_day        = "images/bg/ext_square_day.jpg"
    image bg ext_cabin_day         = "images/bg/ext_cabin_day.jpg"
    image bg ext_boathouse_day  = "images/bg/ext_boathouse_day.jpg"
    image bg ext_path_day          = "images/bg/ext_path_day.jpg"
    image bg ext_house_of_mt_day   = "images/bg/ext_house_of_mt_day.jpg"
    image bg ext_house_of_mt_evening   = "images/bg/houses_evening.jpg" # временно!!!
    image bg int_house_of_mt2_morning  = "images/bg/int_house_of_mt2_morning.jpg" # временно!!!
    image bg int_house_of_mt_day   = "images/bg/int_house_of_mt_day.jpg"
    image bg int_house_of_mt_evening   = "images/bg/int_house_of_mt_evening.jpg"
    image bg ext_house_of_el_day   = "images/bg/ext_house_of_el_day.jpg"
    image bg int_house_of_el_day   = "images/bg/int_house_of_el_day.jpg"
    image bg ext_square_day        = "images/bg/ext_square_day.jpg"
    image bg int_dining_hall_day         = "images/bg/int_dining_hall_day.jpg"
    image bg ext_corner_day        = "images/bg/ext_corner_day.jpg"

#  New
#TODO: удалить строчку и сам файл из репозитория! image bg ext_square2_day       = "images/bg/ext_square2_day.jpg"
    image bg ext_washstand_day     = "images/bg/ext_washstand_day.jpg"
    image bg ext_washstand2_day     = "images/bg/ext_washstand2_day.jpg"
    image bg int_aidpost_day       = "images/bg/int_aidpost_day.jpg"
    image bg ext_aidpost_day       = "images/bg/ext_aidpost_day.jpg"
    image bg ext_Stage_day         = "images/bg/ext_Stage_day.jpg"
    image bg ext_house_of_un_day   = "images/bg/ext_house_of_un_day.jpg"
    image bg ext_house_of_dv_day   = "images/bg/ext_house_of_dv_day.jpg"
    image bg ext_library_day       = "images/bg/ext_library_day.jpg"
    image bg ext_beach_day         = "images/bg/ext_beach_day.jpg"
    image bg int_library_day       = "images/bg/int_library_day.jpg"
    image bg ext_musclub_day       = "images/bg/ext_musclub_day.jpg"
    image bg int_musclub_day       = "images/bg/int_musclub_day.jpg"
    image bg ext_StageBig_day      = "images/bg/ext_StageBig_day.jpg"
    image bg map                   = "images/maps/map_avaliable.jpg"
    image bg ext_playground_day = "images/bg/ext_playground_day.jpg"
    image bg int_clubs_male_day = "images/bg/int_clubs_male_day.jpg"

# bg конец ---------------------------------------------------------



# cg ---------------------------------------------------------------
init:

#added on first day            
    image cg ext_hell_bus          = "images/cg/ext_hell_bus.jpg"
    image cg calc                  = "images/cg/calc.jpg"
    image cg grasshopper           = "images/cg/grasshopper.jpg"
    image cg rena_sunset           = "images/cg/rena_sunset.jpg"
    image cg day1_mao              = "images/cg/day1_mao.jpg"
    image cg food_normal           = "images/cg/food_normal.jpg"
    image cg food_skolop           = "images/cg/food_skolop.jpg"
    image cg nu_pogodi             = "images/cg/nu_pogodi.jpg"
    image cg ussr_catched          = "images/cg/ussr-tan_catched_cg.jpg"

#added on second day  
    image cg d2_mt_morning         = "images/cg/d2_mt_morning.jpg"
    image cg d2_Miku_piano         = "images/cg/d2_miku_piano.jpg"
    image cg d2_Miku_piano2       = "images/cg/d2_miku_piano2.jpg"
    image cg d2_cake                      = "images/cg/d2_cake.jpg"

# cg конец ---------------------------------------------------------



# персонажи --------------------------------------------------------
init:

#Данная переменная определяет, показывать ли имя персонажа в отдельном мини-окошке
    $ _show_two_window = True

#Игрок
    # me - именование в диалогах
    $ me_name = u"Я"
    $ me_color = (255, 255, 255, 255)
    $ me_adv = DynamicCharacter("me_name", color=me_color, show_two_window=_show_two_window)
    $ me_nvl = DynamicCharacter("me_name", color=me_color, kind=nvl)
  
#Описание происходящего
    # <пустая строка> - именование в диалогах
    $ narrator_adv = Character(None, what_style="narrator")
    $ narrator_nvl = Character(None, kind=nvl, what_style="narrator")

#Внутренний голос игрока
    # th - именование в диалогах
    $ th_prefix = "~ "
    $ th_suffix = " ~"
    $ th_adv = Character(None, what_style="thoughts",what_prefix = th_prefix,what_suffix=th_suffix)
    $ th_nvl = Character(None, kind=nvl, what_style="thoughts",what_prefix = th_prefix,what_suffix=th_suffix)

#Вод-тян
    # dr - именование в диалогах
    $ dr_name = u"Водитель"
    $ dr_color = (64, 128, 172, 255)
    $ dr_adv = DynamicCharacter("dr_name", color=dr_color, show_two_window=_show_two_window)
    $ dr_nvl = DynamicCharacter("dr_name", color=dr_color, kind=nvl)

#Электроник-кун
    # elektronik - именование в диалогах
    $ el_name = u"Незнакомец"
    $ el_color = (255, 128, 0, 255)
    $ el_adv = DynamicCharacter("el_name", color=el_color, show_two_window=_show_two_window)
    $ el_nvl = DynamicCharacter("el_name", color=el_color, kind=nvl)
    image el normal   = VerticalCrop(
        Sandwich("images/sprites/el", "body2.png", "cheeks.png", "emotion1.png"),
        0, 800)
    image el thinking = VerticalCrop(
        Sandwich("images/sprites/el", "body1.png", "cheeks.png", "emotion2.png"),
        0, 800)

#Уныл-тян
    # un - именование в диалогах
    $ un_name = u"Незнакомка"
    $ un_color = (255, 0, 255, 255)
    $ un_adv = DynamicCharacter("un_name", color=un_color, show_two_window=_show_two_window)
    $ un_nvl = DynamicCharacter("un_name", color=un_color, kind=nvl)
    image un normal = VerticalCrop(
        Sandwich("images/sprites/un", "body5.png", "nose.png", "eyes.png", "emotion12.png"),
        0, 900)
    image un calmdown = VerticalCrop(
        Sandwich("images/sprites/un", "body1.png", "nose.png", "eyes.png", "emotion12.png"),
        0, 900)
    image un down   = VerticalCrop(
        Sandwich("images/sprites/un", "body1.png", "nose.png", "eyes.png", "emotion5.png"),
        0, 900)

#Двач-тян
    # dv - именование в диалогах
    $ dv_name = u"Незнакомка"
    $ dv_color = (255, 128, 0, 255)
    $ dv_adv = DynamicCharacter("dv_name", color=dv_color, show_two_window=_show_two_window)
    $ dv_nvl = DynamicCharacter("dv_name", color=dv_color, kind=nvl)
    image dv first_contact = VerticalCrop("images/sprites/dvach_tan_uniform_pose1.png", 0, 600)
    image dv normal = VerticalCrop(
        Sandwich("images/sprites/dv", "body3.png", "cheeks.png", "oldemo.png"),
        0, 900)
    image dv tricky = VerticalCrop(
        Sandwich("images/sprites/dv", "body2.png", "cheeks.png", "nose.png", "eyes.png", "emotion6.png"),
        0, 900)
    image dv smile = VerticalCrop(
        Sandwich("images/sprites/dv", "body1.png", "cheeks.png", "nose.png", "eyes.png", "emotion8.png"),
        0, 900)
    image dv bored = VerticalCrop(
        Sandwich("images/sprites/dv", "body2.png", "cheeks.png", "oldemo.png"),
        0, 900)

#Славя-тян
    # sl - именование в диалогах
    $ sl_name = u"Незнакомка"
    $ sl_color = (255, 255, 0, 255)
    $ sl_adv = DynamicCharacter("sl_name", color=sl_color, show_two_window=_show_two_window)
    $ sl_nvl = DynamicCharacter("sl_name", color=sl_color, kind=nvl)
    image sl first_contact = "images/sprites/slavya_tan_tmp.png"
    image sl first_contact_frowning = "images/sprites/slavya_tan_tmp.png"
    image sl normal  = VerticalCrop(
        Sandwich("images/sprites/sl", "body1.png", "cheeks.png", "nose.png", "eyes.png", "emotion4.png"),
        0, 900)
    image sl smile  = VerticalCrop(
        Sandwich("images/sprites/sl", "body1.png", "cheeks.png", "nose.png", "emotion2.png"),
        0, 900)

#СССР-тян
    # us - именование в диалогах
    $ us_name = u"Незнакомка"
    $ us_color = (255, 0, 0, 255)
    $ us_adv = DynamicCharacter("us_name", color=us_color, show_two_window=_show_two_window)
    $ us_nvl = DynamicCharacter("us_name", color=us_color, kind=nvl)
    image us normal = VerticalCrop(
        Sandwich("images/sprites/us", "body1.png", "nose.png", "eyes.png", "emotion4.png"),
        0, 900)
    image us tricky   = VerticalCrop("images/sprites/us/us_tricky.png", 0, 900)
    image us thinking = VerticalCrop(
        Sandwich("images/sprites/us", "body5.png", "nose.png", "emotion14.png"),
        0, 900)

#Мод-тян
    # mt - именование в диалогах
    $ mt_name = u"Незнакомка"
    $ mt_color = (128, 255, 0, 255)
    $ mt_adv = DynamicCharacter("mt_name", color=mt_color, show_two_window=_show_two_window)
    $ mt_nvl = DynamicCharacter("mt_name", color=mt_color, kind=nvl)
    # если надо сдвинуть картинку вверх-вниз, последнюю чиселку можно менять
    image mt normal  = VerticalCrop(
        Sandwich("images/sprites/mt", "body1.png", "cheeks.png", "emotion2.png"),
        0, 900)
    image mt smile  = VerticalCrop(
        Sandwich("images/sprites/mt", "body1.png", "cheeks.png", "emotion1.png"),
        0, 900)
    image mt hand_up  = VerticalCrop(
        Sandwich("images/sprites/mt", "body2.png", "cheeks.png", "emotion1.png"),
        0, 900)

#Коллайдер-сама
    # cs - именование в диалогах
    $ cs_name = u"Незнакомка"
    $ cs_color = (0, 0, 255, 255)
    $ cs_adv = DynamicCharacter("cs_name", color=cs_color, show_two_window=_show_two_window)
    $ cs_nvl = DynamicCharacter("cs_name", color=cs_color, kind=nvl)
    # image cs first_contact = "images/sprites/collider_sama_tmp.png"
    image cs normal = "images/sprites/cs/koll-chan.png"

#Мицу-тян
    # mz - именование в диалогах
    $ mz_name = u"Незнакомка"
    $ mz_color = (0, 0, 255, 255)
    $ mz_adv = DynamicCharacter("mz_name", color=mz_color, show_two_window=_show_two_window)
    $ mz_nvl = DynamicCharacter("mz_name", color=mz_color, kind=nvl)

#Мику-тян
    # mi - именование в диалогах
    $ mi_name = u"Незнакомка"
    $ mi_color = (45, 151, 151, 255)
    $ mi_adv = DynamicCharacter("mi_name", color=mi_color, show_two_window=_show_two_window)
    $ mi_nvl = DynamicCharacter("mi_name", color=mi_color, kind=nvl)
    image mi normal = "images/sprites/mi/miku.png"
    image mi smile = "images/sprites/mi/miku2.png"

#Голос из динамика
    # dy - именование в диалогах
    $ dy_name = u"Голос из динамика"
    $ dy_color = (192, 192, 192, 255)
    $ dy_adv = DynamicCharacter("dy_name", color=dy_color, show_two_window=_show_two_window)
    $ dy_nvl = DynamicCharacter("dy_name", color=dy_color, kind=nvl)

#Луркмор-кун
    # lk - именование в диалогах
    $ lk_name = u"Луркмор-кун"
    $ lk_color = (255, 128, 128, 255)
    $ lk = DynamicCharacter("lk_name", color=lk_color, show_two_window=_show_two_window)
    $ help = Character("", kind=nvl)
    image lurkmore = 'images/sprites/lk/lurkmoar.png'

#Шурик
    # sh - Шурик
    $ sh_name = u"Незнакомец"
    $ sh_color = (255, 128, 128, 255)
    $ sh = DynamicCharacter("sh_name", color=sh_color, show_two_window=_show_two_window)
    image sh normal = "images/sprites/sh/shurik.png"
    image sh big = "images/sprites/sh/shurik2.png"

# персонажи конец --------------------------------------------------



# карты ------------------------------------------------------------
init:
    image widget map = "images/maps/map.jpg"
init -999 python:
    def bg_tmp_image(bgname):
        renpy.image("text "+bgname,LiveComposite((1024, 768),(0, 0),"#ffff7f",(50, 150),Text(u"А здесь будет фон про "+bgname, size=40, color="6A7183")))
        return "text "+bgname

    store.map_pics = {
        "bgpic": "images/maps/map.jpg",
        "avaliable": "images/maps/map_avaliable.jpg",
        "selected": "images/maps/map_selected.jpg"
    }
    store.map_zones = {
        "un_mi_house":   {"position":[402,117,431,153],"default_bg":bg_tmp_image(u"Уныл и Мику")},
        "me_mt_house":   {"position":[507,133,542,169],"default_bg":bg_tmp_image(u"Мой домик")},
        "sl_mz_house":   {"position":[555,180,592,221],"default_bg":bg_tmp_image(u"Славя и Мицу-тян")},
        "estrade":       {"position":[587, 70,673,152],"default_bg":bg_tmp_image(u"Эстрада")},
        "sy_sh_house":   {"position":[431,204,462,246],"default_bg":bg_tmp_image(u"Сыроега и Шурик")},
        "music_club":    {"position":[207,146,299,213],"default_bg":bg_tmp_image(u"Музклуб")},
        "monument":      {"position":[480,254,553,330],"default_bg":bg_tmp_image(u"Памятник вождю")},
        "admin_house":   {"position":[385,240,461,318],"default_bg":bg_tmp_image(u"Админкорпус")},
        "wash_house":    {"position":[313,319,395,390],"default_bg":bg_tmp_image(u"Банно-прачечная")},
        "square":        {"position":[409,382,528,453],"default_bg":bg_tmp_image(u"Площадь")},
        "dining_hall":   {"position":[529,333,644,431],"default_bg":bg_tmp_image(u"Столовая")},
        "dv_us_house":   {"position":[331,436,373,478],"default_bg":bg_tmp_image(u"Дваче и СССР")},
        "store_house":   {"position":[645,343,698,427],"default_bg":bg_tmp_image(u"Склад")},
        "valleyball":    {"position":[699,340,767,430],"default_bg":bg_tmp_image(u"Воллейбол")},
        "sport_area":    {"position":[769,350,946,476],"default_bg":bg_tmp_image(u"Спорткомплекс")},
        "beach":         {"position":[671,478,886,600],"default_bg":bg_tmp_image(u"Пляж")},
        "boat_station":  {"position":[414,456,525,583],"default_bg":bg_tmp_image(u"Лодочный причал")},
        "old_road":      {"position":[148,570,202,629],"default_bg":bg_tmp_image(u"Дорога на старый лагерь")},
        "old_house":     {"position":[  2,691, 82,766],"default_bg":bg_tmp_image(u"Старый корпус")},
        "village_road":  {"position":[966,448,1013,552],"default_bg":bg_tmp_image(u"Дорога в деревню")},
        "clubs":         {"position":[122,298,295,406],"default_bg":bg_tmp_image(u"Клубы")},
        "library":       {"position":[693,175,764,244],"default_bg":bg_tmp_image(u"Библиотека")},
        "badminton":     {"position":[777,269,862,343],"default_bg":bg_tmp_image(u"Бадминтон")},
        "medic_house":   {"position":[555,255,618,319],"default_bg":bg_tmp_image(u"Медпункт")},
        "camp_entrance": {"position":[ 14,311,109,407],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
        "island_nearest":{"position":[220,660,444,768],"default_bg":bg_tmp_image(u"о. Ближний")}
    }

# карты конец ------------------------------------------------------



# анимация ---------------------------------------------------------
init:

#FIXME intro 
    image intro = Animation(
        "images/intro/intro1.jpg", 3.0,
        "images/intro/intro2.jpg", 3.0)

# анимация конец ---------------------------------------------------




# музыка -----------------------------------------------------------
init:
   
    $ music_nu_pogodi_gameboy = "sound/sfx/nu_pogodi_gameboy.ogg"
    $ music_eat_some_trouble = "sound/music/eat_some_trouble.ogg"
    $ music_my_daily_life = "sound/music/my_daily_life.ogg"
    $ music_everyday_theme = "sound/music/everyday_theme.ogg"
    $ music_pioneer_loudspeaker_tape = "sound/music/pioneer2_loudspeaker_tape.ogg"
    $ music_memories_piano_outdoors = "sound/music/memories_piano_outdoors.ogg"
    $ music_no_tresspassing = "sound/music/no_tresspassing.ogg"
    $ music_take_me_beautifully = "sound/music/take_me_beautifully.ogg"
    $ music_smooth_machine = "sound/music/smooth_machine.ogg"
    $ music_just_think = "sound/music/just_think.ogg"

# музыка конец -----------------------------------------------------


    
# эмбиенсы ---------------------------------------------------------
init:
    
    $ ambience_water_stream = "sound/ambiences/water_stream_closer.ogg"
    $ ambience_dining_room_full = "sound/ambiences/dining_room_people.ogg"
    $ ambience_dining_room_empty = "sound/ambiences/dining_room_empty.ogg"
    $ ambience_crickets = "sound/ambiences/oyez_crickets.ogg"
    $ ambience_forest_birds = "sound/ambiences/forestbirds.ogg"
    
# эмбиенсы конец --------------------------------------------------
    
    
    
# звуки -----------------------------------------------------------
init:
    
#автобус
    $ sfx_bus_loop = "sound/sfx/bus_loop.ogg"
    $ sfx_bus_stop = "sound/sfx/bus_stop.ogg"
    $ sfx_bus_out = "sound/sfx/bus_out.ogg"
    
#умывальник, кран    
    $ sfx_open_water_open = "sound/sfx/water_faucet/open_water_open.ogg"
    $ sfx_open_water_close = "sound/sfx/water_faucet/open_water_close.ogg"
    $ sfx_open_water_flow = "sound/sfx/water_faucet/open_water_flow.ogg"

#шкафчики и ящики столов
    $ sfx_drawer_open = "sound/sfx/drawer/drawer_open.ogg"
    $ sfx_drawer_close = "sound/sfx/drawer/drawer_close.ogg"
    $ sfx_drawer_struggle = "sound/sfx/drawer/closed_drawer_struggle.ogg"    
    $ sfx_drawer_hack = "sound/sfx/drawer/lock_open_close_1.ogg"    

#двери
    $ sfx_knock_door_polite = "sound/sfx/knock_door/knock_door7_polite.ogg"
    $ sfx_knock_door_closed = "sound/sfx/knock_door/knock_door6_closed.ogg"
    
#удары, захваты, тело
    $ sfx_punch_medium = "sound/sfx/punch/punch_medium.ogg"
    $ sfx_punch_comic = "sound/sfx/punch/punch_comic.ogg"
    $ sfx_clench = "sound/sfx/punch/clench2.ogg"
    
#мебель, предметы и окружающая остановка   
    $ sfx_out_of_bushes = "sound/sfx/out_of_bushes.ogg"
    $ sfx_kill_skolopendra = "sound/sfx/kill_skolopendra.ogg"
    $ sfx_chair_drop = "sound/sfx/chair_drop.ogg"
    $ sfx_bed_squeak_2 = "sound/sfx/bed_squeak/bed_squeak2.ogg"
    
#прочее
    $ sfx_china_anthem = "sound/sfx/china_anthem.ogg"
    $ sfx_suspence_bang = "sound/sfx/suspence_bang.ogg"
    $ sfx_inhale = "sound/sfx/inhale.ogg"
    $ sfx_stomach_growl = "sound/sfx/stomach_growl.ogg"
    $ sfx_nu_pogodi_loud = "sound/sfx/nu_pogodi_loud.ogg"
    $ sfx_heavy_click = "sound/sfx/power_tumblers/heavy_click.ogg"
    $ sfx_ghm_1 = "sound/sfx/ghm_1.ogg"
    
#FIXME: Этих звуковых файлов не хватает
    $ sfx_bus_away = "sound/sfx/bus_away.wav"
    
# звуки конец -----------------------------------------------------

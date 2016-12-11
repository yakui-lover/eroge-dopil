init:
    python:
        def silhouette_matrix (r,g,b,a=1.0):
             return im.matrix((0, 0, 0, 0, r, 
                               0, 0, 0, 0, g,
                               0, 0, 0, 0, b,
                               0, 0, 0, a, 0,))
        def silhouetted (filename, r,g,b, a = 1.0):
            return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))

    if not config_session:
        image widget map = get_image("maps/oldmap.jpg")
        image bg map = get_image("maps/oldmap_avaliable.png")
    
init 2:
    #Флаги, которые можно получить за второй день.
    $ d2_necessary_done = 0
    $ d2_met_dv = False
    $ d2_dv_fight = False
    $ d2_visited_modellers = 0
    $ d2_visited_unnats = 0
    $ d2_visited_playing_club = 0
    $ d2_times_been_to_dv_us_house = 0
    $ d2_met_mt = False
    $ d2_no_shame = False
    $ more_fiz = False
    $ d2_times_been_to_green_theatre = 0
    $ d2_dv_interrogation = False
    $ mus_club = False
    $ tech_club = False
    $ modeller_club = False
    $ unnat_club = False
    $ chess_club = False
    $ sport_club = False
    $ gazette_club = False
    $ med_exam = False
    $ d2_qt_places = 0
    $ d2_qt_sleep = False
    $ d2_qt_library = False
    $ d2_met_ug = False
    $ d2_chess_decision = False
    $ d2_chess_agreement = False
    $ d2_day_places = 0
    $ d2_mz_help = False
    $ d2_dv_quits = False
    $ d2_girls_event = 0
    $ d2_us_dv_day = False
    $ d2_mz_helped = False
    $ d2_books_chosen = False
    $ d2_un_day = False
    $ d2_times_been_to_unnat_club = 0
    $ d2_times_been_to_modeller_club = 0
    $ d2_times_been_to_chess_club = 0
    $ d2_sl_day = False
    $ d2_modellers_day = False
    $ d2_mi_day = False
    $ d2_guitar_illegal = False
    $ d2_dv_help = False
    $ d2_ug_game = False
    $ d2_met_ld = False
    $ d2_mt_promise = False
    $ d2_in_game = False
    $ d2_seen_bathhouse = False
    $ d2_walk = 0
    $ d2_fail = 0
    $ d2_cards_win = False
    $ d2_us_try_fail = False
    $ d2_mk_deal = False
    $ d2_evening_places = 0
    $ d2_us_evening = False
    $ d2_mi_dv_evening = False
    $ d2_sl_evening = False
    $ d2_un_evening = False
    $ d2_dv_evening = False
    $ d2_mt_banned = False
        
    #Лавпоинты и френдшип-поинты.
    $ lp_cs = 0
    $ lp_mi = 0
    
    #Ивент-поинты за события коммон-рута, которые можно пропустить.
    $ common_event = 0
    
    #Назначение имён новых персонажей и их цвета.
    $ colors['bt'] = {'night': (0, 182, 39, 255), 'sunset': (0, 234, 50, 255), 'day': (0, 234, 50, 255), 'prolog': (0, 234, 50, 255)}
    $ store.names_list.append('bt')
    $ colors['lk'] = {'night': (145, 145, 0, 255), 'sunset': (170, 170, 0, 255), 'day': (170, 170, 0, 255), 'prolog': (170, 170, 0, 255)}
    $ store.names_list.append('lk')
    $ colors['km'] = {'night': (92, 149, 255, 255), 'sunset': (92, 201, 255, 255), 'day': (92, 201, 255, 255), 'prolog': (92, 201, 255, 255)}
    $ store.names_list.append('km')
    $ colors['st_chess'] = {'night': (150, 150, 150, 255), 'sunset': (150, 150, 150, 255), 'day': (150, 150, 150, 255), 'prolog': (150, 150, 150, 255)}
    $ store.names_list.append('st_chess')
    $ colors['boy'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('boy')
    $ colors['boy_A'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('boy_A')
    $ colors['boy_B'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('boy_B')
    $ colors['boy_C'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('boy_C')
    $ colors['boy_D'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('boy_D')
    $ colors['efg'] = {'night': (50, 125, 50, 255), 'sunset': (95, 210, 55, 255), 'day': (95, 210, 55, 255), 'prolog': (95, 210, 55, 255)}
    $ store.names_list.append('efg')
    $ colors['nc'] = {'night': (60, 155, 77, 255), 'sunset': (77, 199, 99, 255), 'day': (77, 199, 99, 255), 'prolog': (77, 199, 99, 255)}
    $ store.names_list.append('nc')
    $ colors['girl_A'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('girl_A')
    $ colors['lir'] = {'night': (255, 255, 255, 255), 'sunset': (255, 255, 255, 255), 'day': (255, 255, 255, 255), 'prolog': (255, 255, 255, 255)}
    $ store.names_list.append('lir')
    $ colors['ci'] = {'night': (16, 136, 255, 255), 'sunset': (51, 153, 255, 255), 'day': (51, 153, 255, 255), 'prolog': (51, 153, 255, 255)}
    $ store.names_list.append('ci')
    $ colors['girl_B'] = {'night': (225, 30, 30, 255), 'sunset': (255, 30, 30, 255), 'day': (255, 30, 30, 255), 'prolog': (255, 30, 30, 255)}
    $ store.names_list.append('girl_B')
    $ colors['nf'] = {'night': (228, 191, 144, 255), 'sunset': (255, 215, 162, 255), 'day': (255, 215, 162, 255), 'prolog': (255, 215, 162, 255)}
    $ store.names_list.append('nf')
    $ colors['tok'] = {'night': (255, 255, 255, 255), 'sunset': (255, 255, 255, 255), 'day': (255, 255, 255, 255), 'prolog': (255, 255, 255, 255)}
    $ store.names_list.append('tok')
    $ colors['ld'] = {'night': (45, 120, 245, 255), 'sunset': (100, 155, 245, 255), 'day': (100, 155, 245, 255), 'prolog': (100, 155, 245, 255)}
    $ store.names_list.append('ld')
    
    #Объявление новых спрайтов.
    image cs normal stethoscope glasses = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/cs/cs_1_body.png",(0,0), "images/1080/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/1080/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/1080/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/cs/cs_1_body.png",(0,0), "images/1080/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/1080/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/1080/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "images/1080/sprites/normal/cs/cs_1_body.png",(0,0), "images/1080/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/1080/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/1080/sprites/normal/cs/cs_1_normal.png") )
    image cs smile stethoscope glasses = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/cs/cs_1_body.png",(0,0), "images/1080/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/1080/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/1080/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/cs/cs_1_body.png",(0,0), "images/1080/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/1080/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/1080/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "images/1080/sprites/normal/cs/cs_1_body.png",(0,0), "images/1080/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/1080/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/1080/sprites/normal/cs/cs_1_smile.png") )
    image sl smile2 pioneer close bw = im.Grayscale(im.Composite((1050,1080), (0,0), "images/1080/sprites/close/sl/sl_2_body.png",(0,0), "images/1080/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/1080/sprites/close/sl/sl_2_smile2.png") )
    image sl surprise pioneer close bw = im.Grayscale(im.Composite((1050,1080), (0,0), "images/1080/sprites/close/sl/sl_3_body.png",(0,0), "images/1080/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/1080/sprites/close/sl/sl_3_surprise.png") )
    image mt normal pioneer close bw = im.Grayscale(im.Composite((1050,1080), (0,0), "images/1080/sprites/close/mt/mt_1_body.png",(0,0), "images/1080/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/1080/sprites/close/mt/mt_1_normal.png") )
    image mt surprise pioneer close bw = im.Grayscale(im.Composite((1050,1080), (0,0), "images/1080/sprites/close/mt/mt_1_body.png",(0,0), "images/1080/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/1080/sprites/close/mt/mt_1_surprise.png") )
    image dv grin pioneer2 close bw = im.Grayscale(im.Composite((1050,1080), (0,0), "images/1080/sprites/close/dv/dv_2_body.png",(0,0), "images/1080/sprites/close/dv/dv_2_pioneer2.png",(0,0), "images/1080/sprites/close/dv/dv_2_grin.png") )
    image el grin pioneer bw = im.Grayscale(im.Composite((900,1080), (0,0), "images/1080/sprites/normal/el/el_1_body.png",(0,0), "images/1080/sprites/normal/el/el_1_pioneer.png",(0,0), "images/1080/sprites/normal/el/el_1_grin.png") )
    image sh upset pioneer bw = im.Grayscale(im.Composite((900,1080), (0,0), "images/1080/sprites/normal/sh/sh_1_body.png",(0,0), "images/1080/sprites/normal/sh/sh_1_upset.png") )
    image mz normal glasses pioneer far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/mz/mz_1_body.png",(0,0), "images/1080/sprites/far/mz/mz_1_glasses.png",(0,0), "images/1080/sprites/far/mz/mz_1_normal.png",(0,0), "images/1080/sprites/far/mz/mz_1_pioneer.png"),0,0,0)
    image mi normal pioneer far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/mi/mi_3_body.png",(0,0), "images/1080/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/1080/sprites/far/mi/mi_3_normal.png"),0,0,0)
    image un normal pioneer far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/un/un_1_body.png",(0,0), "images/1080/sprites/far/un/un_1_pioneer.png",(0,0), "images/1080/sprites/far/un/un_1_normal.png"),0,0,0)
    image dv grin pioneer2 far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/dv/dv_2_body.png",(0,0), "images/1080/sprites/far/dv/dv_2_pioneer2.png",(0,0), "images/1080/sprites/far/dv/dv_2_grin.png"),0,0,0)
    image sl normal pioneer far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/sl/sl_1_body.png",(0,0), "images/1080/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/1080/sprites/far/sl/sl_1_normal.png"),0,0,0)
    image mt smile panama pioneer far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/mt/mt_1_body.png",(0,0), "images/1080/sprites/far/mt/mt_1_panama.png",(0,0), "images/1080/sprites/far/mt/mt_1_smile.png",(0,0), "images/1080/sprites/far/mt/mt_1_pioneer.png"),0,0,0)
    image us normal sport far hidden = silhouetted (im.Composite((630,1080), (0,0), "images/1080/sprites/far/us/us_1_body.png",(0,0), "images/1080/sprites/far/us/us_1_sport.png",(0,0), "images/1080/sprites/far/us/us_1_normal.png"),0,0,0)
    image el smile pioneer bw = im.Grayscale(im.Composite((900,1080), (0,0), "images/1080/sprites/normal/el/el_1_body.png",(0,0), "images/1080/sprites/normal/el/el_1_pioneer.png",(0,0), "images/1080/sprites/normal/el/el_1_smile.png") )
    
    #Объявление новых BG.
    image bg ext_bathhouse_day = im.Scale("images/720/bg/ext_bathhouse_day.jpg",1920,1080)
    image bg ext_musclub_night_fog = im.Scale("images/720/bg/ext_musclub_night_fog.jpg",1920,1080)
    image bg ext_square_day_bw = im.Grayscale("images/1080/bg/ext_square_day.jpg")
    image bg bus_stop_bw = im.Grayscale("images/1080/bg/bus_stop.jpg")
    image bg ext_dining_hall_near_day_bw = im.Grayscale("images/1080/bg/ext_dining_hall_near_day.jpg")
    image bg ext_musclub_day_bw = im.Grayscale("images/1080/bg/ext_musclub_day.jpg")
    image bg int_clubs_male_day_bw = im.Grayscale("images/1080/bg/int_clubs_male_day.jpg")
    
    #Объявление новых CG.
    image cg d2_mt_morning_change = "images/768/cg/d2_mt_morning_change.jpg"
    image cg d2_cake = "images/1080/cg/d2_cake.jpg"
    image cg d2_soccer = "images/1080/cg/d2_soccer.jpg"
    image anim stars_3o_bw = im.Grayscale("images/1080/anim/stars_3o.jpg")
    image anim stars_1_north = im.Flip("images/1080/anim/stars_1.jpg", horizontal=True, vertical=True)
    image anim stars_3_south_east = im.Flip("images/1080/anim/stars_3.jpg", horizontal=True)
    image anim stars_2o_bw = im.Grayscale("images/1080/anim/stars_2o.jpg")
    image cg d2_2ch_beach_night_horizontal = "images/1080/cg/d2_2ch_beach_night_horizontal.jpg"
    
    #Объявление новой музыки.
    
    $ music_list["80s_youre_my_heart"] = "sound/ii_side_music/80s_youre_my_heart.mp3"
    $ music_list["wonderful_future"] = "sound/ii_side_music/wonderful_future.mp3"
    $ music_list["song_about_bears"] = "sound/ii_side_music/song_about_bears.mp3"

    #Объявление новых эмбиентов.
    $ ambience_water_stream_closer = "sound/ambiences/water_stream_closer.ogg"

    #Объявление новых звуков.
    $ sfx_table_move_outside = "sound/sfx/table_move_outside.ogg"
    $ sfx_heavy_click = "sound/sfx/heavy_click.ogg"
    $ sfx_ghm_1 = "sound/sfx/ghm_1.ogg"
    
#Общие TODO по дню:
#

init -997 python:
    store.map_pics = {
            "bgpic": get_image("maps/oldmap.jpg"),
            "avaliable": get_image("maps/oldmap_avaliable.jpg"),
            "selected": get_image("maps/oldmap_selected.jpg")
        }

label ii_eroge_d2:

    $ set_name('bt',u"Инга Максимовна")
    $ set_name('lk',u"Дмитрий Евгеньевич")
    $ set_name('km',u"Староста моделистов")
    $ set_name('st_chess',u"Староста кружка игр")
    $ set_name('boy',u"Пионер")
    $ set_name('boy_A',u"Пионер A")
    $ set_name('boy_B',u"Пионер B")
    $ set_name('boy_C',u"Пионер C")
    $ set_name('boy_D',u"Пионер D")
    $ set_name('efg',u"Михаил Ефграфович")
    $ set_name('girl_A',u"Пионерка A")    
    $ set_name('lir',u"Пионер")
    $ set_name('ci',u"Пионерка")
    $ set_name('girl_B',u"Пионерка B")
    $ set_name('tok',u"Пионер")
    $ set_name('ld',u"Лодочник")
    
    $ day_time()
    $ persistent.sprite_time = "day"
    
    scene black
    with dissolve
    show screen central_text("День 2 — Утро пионера")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    
    play music music_list["my_daily_life"]
    play ambience ambience_int_cabin_day fadein 1

    scene bg int_house_of_mt_sunset
    with fade
    window show
    "Я проснулся."
    "В этом не было бы ничего удивительного, если бы я оказался у себя дома."
    "С трудом разлепив веки, я разглядел, что всё ещё нахожусь в домике вожатой из пионерлагеря, куда меня привёз автобус."
    "Я лежал на правом боку, лицом к стене. Постель была мягкой, и от этого не хотелось шевелиться, вставать, словно наступил необыкновенный выходной, когда можно проваляться до полудня."
    th "Что же мне снилось несколько минут назад?"
    "Вспомнить не удалось, сон быстро выветрился из памяти."
    "Наутро в голове посвежело — я чувствовал себя отдохнувшим. Организм ощущал незнакомую обстановку и готовился к возможным нагрузкам."
    "Мысли немного прояснились, я отвлёкся от тщетных попыток припомнить сон..."
    th "Я спал в одной комнате с малознакомой женщиной. В первый раз."
    th "Что?" 
    "Какая-то часть меня отказывалась верить в это."
    "Я медленно лёг на спину, готовясь заставить себя отлепиться от кровати и встать, как вдруг замер."
    #К этапу работ по графике. Возможно, в будущем cg будет подлежать доработке, поскольку в нём незавершённый фон из раннего билда.
    show cg d2_mt_morning_change at truecenter
    with dissolve
    th "Оп-па..."
    th "Блин, какого чёрта я не проснулся хотя бы на десять минут раньше?"
    th "Кажется, она меня не заметила."
    th "Или заметила?"
    th "Или она это вообще специально делает?"
    "Я замер, целиком поглощённый моментом. Такую картину я видел впервые, и она стоила того, чтобы запомнить её во всех деталях."
    "В мягких лучах зыбкого утреннего солнца Ольга Дмитриевна надевала светло-розовый лифчик. Мне удалось заметить полоску её трусиков того же цвета, потому что шорты на отчётливо выступающих бёдрах девушки не были до конца застёгнуты." 
    "Изящным движением вожатая завела руки за спину, чтобы сцепить вместе застёжки бюстгальтера."
    "Мой взгляд нетерпеливо блуждал от локтя к груди, по изгибу спины к бёдрам и ниже — по стройным ногам Ольги Дмитриевны. Не меньше волновала мысли её мягко схватившаяся загаром кожа."
    "Справившись с застёжкой и молнией шорт, девушка убрала за плечи длинные волосы, ещё не расчёсанные после сна."
    "До меня дошло, что Ольга Дмитриевна сейчас повернётся и..."
    hide cg d2_mt_morning_change
    show blink
    "Я попытался аккуратно перевалиться обратно на бок, зажмурив глаза, будто всё ещё спал и совсем-совсем ничего не видел."
    "Кровать предательски скрипнула."
    mt "Ага! Проснулся, я вижу. Доброе утро."
    th "Ни тени смущения в её голосе!"
    hide blink
    show unblink
    with dissolve
    "Опять оказавшись на правом боку, носом к стенке, я не стал оборачиваться и вставать."
    hide unblink
    me "Ну, вроде как.{w} Я подожду, когда вы... оденетесь."
    "..."
    mt "Всё. Можешь тоже одеваться."
    show mt smile pioneer at center with dissolve
    "Я снова развернулся к Ольге Дмитриевне, сел на кровати и скомкал простыню, прикрывая натянувшиеся бугром трусы из-за особенностей физиологии парней.{w} Или от увиденной сцены?"
    "Улыбавшаяся Ольга Дмитриевна уже застегнула верхнюю пуговицу рубашки, оправила форму."
    hide mt  with dissolve
    show mt smile pioneer far at right with dissolve
    "Вожатая достала из сумочки расчёску и прошла мимо меня причёсываться к зеркалу, не глядя, как я маскирую простынёй своё хозяйство."
    th "Как же быть с этой оказией в следующие дни?"
    "Голос вожатой нарушил мои размышления."
    show mt surprise pioneer far at right with dspr
    mt "А ты встал раньше положенного, общий подъём по лагерю только через тридцать с чем-то минут..."
    me "Правда? Я не знаю расписания."
    show mt normal pioneer far at right with dspr
    mt "Оно висит на стенде у медпункта."
    if d1_dv_evening: 
     me "Нет, я не видел стенда."
    else: 
     me "Я был там, расписания не видел."
    mt "Ох, Семён. Хотя, у меня где-то тут лежала копия с распорядком дня для себя..."
    "Ольга Дмитриевна прекратила расчёсывать волосы, мельком оценив причёску в отражении, и вернулась к столику."
    hide mt with dissolve
    show mt normal pioneer at center with dissolve
    mt "Секунду."
    "Она взяла одну из книжек, что лежали на полке, вынула свёрнутую закладку и отдала её мне. Это оказался лист бумаги в клеточку, где в четыре столбца было составлено расписание для разных отрядов на чётные и нечётные дни."
    me "Спасибо. Можно переписать?"
    show mt smile pioneer at center with dspr
    mt "Конечно."
    "Я взял у неё листок."
    "Вожатая коснулась моей руки."
    show mt normal pioneer at center with dissolve
    mt "Значит так: будет без четверти восемь на часах — двигай умываться и чистить зубы, а потом марш на зарядку с построением. Буду из тебя образцового пионера делать."
    me "Что? Построение?"
    mt "Обязательная часть расписания, Семён." 
    "Затея, надо сказать, совершенно не привела меня в восторг."
    "Я хотел было возразить, но Ольга Дмитриевна продолжила."
    mt "Ты здесь на особом счету."
    me "Это ещё почему?"
    show mt grin pioneer at center with dspr
    mt "Во-первых, выглядишь повзрослее. Во-вторых, приехал отдельно. Будешь облегчать тяжёлую ношу пионервожатой."
    if d1_genda_flag:
        "Я бы облегчил её ношу, если вы понимаете, о чём я..."
    else:
        th "Подождите-подождите. Что? Я не вызывался мальчиком на побегушках!"
        "Но она вряд ли потерпит возражения. Тем более, вожатая помогла мне с одеждой, и я в долгу перед Ольгой Дмитриевной..."
        me "Ольга Дмитриевна, а где мои вещи со вчерашнего дня, которые промокли?"
        show mt normal pioneer at center with dissolve
        mt "Они в прачечной. Можешь забрать сам, когда позавтракаешь."
    hide mt with dissolve
    "С этими словами Ольга Дмитриевна вышла из комнаты, а я так и остался сидеть на кровати с открытым ртом."
    if d1_genda_flag:
        "Это она {i}во мне{/i} хорошего мальчика разглядела?"
    "Ну, без неё откинуть простынь и одеться будет несколько проще."
    "Мой взгляд упал на часы, стоявшие на подоконнике. Было полвосьмого утра."
    "Я покосился на окно." 
    th "Надеюсь, она не будет подглядывать, эта странная-странная пионервожатая?"
    "Подождав немного, точно собираясь с мыслями, я вытянул сумку из-под кровати, чтобы достать блокнот и одежду, которая могла бы сгодиться для зарядки."
    "Моей физкультурной формой стали короткие тёмно-синие шорты с лампасами и лёгкая белая футболка."
    "Несмотря на чистоту, одежда всё же казалась чуточку старомодной, напоминая о советской эпохе." 
    "Расписание обещало проведение обязательной для всех разминки, поэтому я сразу надел спортивную форму и обулся в кеды."
    "Вооружившись карандашом, я сел за стол и принялся переносить распорядок дня записную книжку."
    th "Ну да, в таком месте надо было ожидать общие зарядки, приём пищи и отбой в строго назначенное время. Но лучше уж пионерский лагерь, чем военная часть."
    th "Может быть, моё попадание в лагерь — это кармическое наказание за уклонение от службы?" 
    th "Впрочем, слишком всё радужно выглядит для наказания. Тут тепло, светло и мухи не кусают. Но вот без Интернета не так весело..."
    "Убрав блокнот, я отыскал в сумке пакет с умывальными принадлежностями." 
    th "Так... Мыльницу вижу, щётку вижу, пасту вижу, а это что?"
    "Из складок свёрнутого полотенца я вытряхнул округлую баночку. В ней обнаружился порошок для чистки зубов, если верить этикетке на крышечке."
    if d1_genda_flag:
        "Электроник говорил, что пасту надо беречь для проделок. "
        th "Стратегически важный ресурс в пионерлагере, однако!"
        "Я бросил тюбик в сумку."
        "И к тому же я давно забыл, как это — чистить зубы порошком."
    else:
        th "Порошок сойдёт, кто знает, паста ещё может пригодиться."
        th "Когда-то давно я чистил зубы только им, и ничего. Пришло время вспомнить детство."
        "Пасту я оставил в сумке под кроватью."
    "Я проверил мобильник. Оператор связи так и не был найден, да я уже и не надеялся на это. Батарея оказалась разряженной чуть более, чем наполовину, поэтому я выключил его и тоже спрятал в кармане сумки."
    "Вернув коробок порошка в пакет, я вышел из домика."
    window hide
    stop ambience fadeout 1
    stop music fadeout 2
    scene black 
    with dissolve
    window show
    "..."
    window hide
    jump d2_washing

label d2_washing:

    scene bg ext_washstand_day
    with dissolve
    play music music_list["everyday_theme"] fadein 2
    window show
    "Найти умывальники оказалось несложно — они находились на поляне в окружении сосен неподалёку от здания администрации."
    "Дул прохладный утренний ветерок. Здесь не было ни живой души, кроме одного меня. Я остановился у ближайшего умывальника, облицованного мелкой плиткой, того, что не скрывался в тени навеса, и выложил из пакета мыльницу на бортик возле крана."
    scene bg ext_washstand2_day 
    with dissolve
    "Я много раз пытался начать жить правильно. Чистить зубы, делать зарядку по утрам."
    "Было приятно вставать рано утром, пока солнце низкое, когда оно едва поднялось из-за горизонта, открывать форточку и делать разминку, чувствуя, что всё делаешь как надо."
    "Приятно... первые две недели. Дольше мне не удавалось заставлять себя соблюдать дисциплину, и спустя какое-то время я снова начал подниматься по будильнику позднее, когда уже было не до зарядки, а в последние годы и вовсе сразу садился за компьютер."
    "Похоже, напутствие отца «Никогда не сдаваться!» осталось неуслышанным. Может, он был прав."
    "Раз мне выпал второй шанс, почему бы не попробовать снова? Начать с чистого листа, как говорится."
    "Не обнаружив рукояток у несколько ржавого изогнутого крана, я просто надавил сверху на него."
    play sound sfx_open_water_sink
    $ renpy.pause(0,5)
    play sound_loop sfx_water_sink_stream fadein 1
    "...И тут же с брызгами хлынул поток воды, искрящейся от солнечного света, наполняя раковину..."
    "Я подставил сложенные руки под воду и вздрогнул, отдёрнув их, до того ледяной она была!"
    "Набрав воды в ладони, пока пальцы не занемели от холода, я плеснул ею в лицо."
    "Второй раз оказалось не так страшно. Я намылил руки, затем лицо. Главное — сжечь мосты."
    stop sound_loop fadeout 1
    me "А-а-а-а!"
    th "Нет, недостаточно. Ещё не всё мыло смыл." 
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "Я снова нажатием открыл кран и набрал ледяной воды в руки."
    me "А-а-а-а!"
    "Захер Мазох бы оценил. Маркиз де Сад, наверно, тоже."
    "Третий, последний..."
    me "А-а-а-а!"
    "Я с трудом отдышался."
    stop sound_loop fadeout 1
    th "Люди, вон, с парашютом прыгают, экстремальщиной всякой занимаются, а я просто умыться попробовал, и вышел такой шок-рок, что мама не горюй. Я слишком привык к благам цивилизации."
    th "Теперь дело за зубами." 
    "Я открыл баночку и осторожно, будто опасаясь, что с неопознанного вещества может унести далеко-далеко-о, понюхал белый порошок внутри."
    "Запах зубного порошка. Ни с чем не спутаешь. Особенно когда он смешивается с другими запахами утра — сосновой смолой, запахом покрытых росой листьев, свежим утренним воздухом..."
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "Снова надавив на кран, я смочил щётку и черпнул порошка из баночки. В зубном порошке была какая-то своя прелесть."
    stop music fadeout 4
    "Приятный островатый мятный привкус во рту, да и само ощущение порошка на языке и зубах совсем другое — не как от пасты..."
    stop sound_loop fadeout 1
    play sound sfx_dinner_jingle_speaker_tape
    "За деревьями ожили динамики, заиграла музыка." 
    th "Гимн лагеря наверное, или ещё что-то в этом духе."
    "Но это была не песня, просто красивая мелодия без слов."
    $ renpy.pause(1)
    play sound sfx_open_water_sink
    play sound sfx_water_sink_stream fadein 1
    "Когда мне показалось, что я достаточно поездил щеткой по зубам, я сполоснул её и убрал. Наклонился, чтобы хлебнуть воды и..."
    me "Ой-и-и-и!"
    "От ледяной воды все зубы мгновенно заныли."
    "Я поплевался и подумал, что второй раз такого мазохизма просто не вынесу. Мысль, что мне, возможно, придётся провести здесь несколько дней, ужасала."
    "Хлебнул воды ещё раз, кое-как прополоскал рот. Плюхнул водой на лицо напоследок и утёрся небольшим полотенцем из пакета."
    scene bg ext_washstand_day
    with dissolve
    me "Фух. Вроде закончил."
    "..."
    "К умывальникам начали стекаться пионеры, сразу занявшие свои места под навесом и снаружи для утренней гигиены. Некоторые спешили, как на пожар, а другие с трудом отходили ото сна."
    stop sound fadeout 2
    "Музыка доиграла. Из динамика прозвучал голос, и я прислушался к нему, вытирая руки."
    dy "Доброе утро, пионеры!"
    dy "Сегодня ваш восьмой день в лагере."
    dy "Температура воздуха — двадцать восемь градусов."
    dy "Температура воды — двадцать пять."
    dy "Партия сказала, что в ближайшие дни погода солнечная и жаркая, значит, купаться будем!"
    dy "Сегодня понедельник, свободный от мероприятий день, для занятий открыты кружки и клубы."
    dy "Однако эта неделя будет такой же насыщенной, как и прошлая. Не забывайте о подготовке ко Дню самодеятельности!"
    dy "Зарядка и построение через десять минут. Не опаздывать."
    play music music_list["everyday_theme"] fadein 2
    "Голос подозрительно напоминал Ольгу Дмитриевну... Да, я узнал её. Это определённо была она."
    "Только я собрался уходить, кинув мыльницу в пакет, как со стороны дороги от здания клубов показалась Славя." 
    show sl normal sport far at center with dissolve
    "Она бежала прямиком к умывальникам, ко мне, пока не перешла на шаг и не остановилась рядом. Я же застыл, глядя на неё."
    hide sl with dissolve
    show sl smile sport close at center with dissolve
    sl "Доброе утро!"
    me "Доброе."
    "Она была в спортивной форме, шорты и майка легко очерчивали её стройную фигуру, а щёки раскраснелись. И этот румянец ей очень шёл."
    "Кеды на её голых ногах были мокрыми от росы."
    sl "Вижу, Ольга Дмитриевна уже рассказала тебе про зарядку."
    me "Ага."
    me "Где ты была?"
    sl "На пробежке! Каждый день встаю на полтора часа раньше для этого."
    me "И далеко бегаешь?"
    sl "Когда как: иногда только на территории лагеря, иногда ухожу за ворота и делаю кросс по дороге. "
    if d1_road_decision:
        th "Блин, я едва не забыл про то, что хотел дождаться автомобиля на шоссе и уехать в город..."
        me "Славя, скажи, по дороге машины часто ездят?"
        show sl surprise sport close at center with dspr
        sl "Тут недалеко есть дачный сектор и гаражный кооператив, иногда в эти места приезжают. А почему ты спрашиваешь?"
        me "Зарядку делать неохота, планировал удрать."
        show sl smile sport close at center with dspr
        th "Надеюсь, отшутился..."
        "Намного занимательней то, что Славя так просто ушла с территории лагеря."
    "И всё равно голос её был чист, а она совсем не запыхалась."
    me "Вообще круто вот так рано вставать и бегать, ничего не скажешь. Я-то себя еле отодрал от постели. Если б не расписание, я бы валялся до полудня."
    show sl happy sport close at center with dspr
    "Девочка, смеясь, положила руку мне на плечо, и я немного напрягся. Всё ещё усугублялось тем, что мы были не одни. Вокруг галдели пионеры, и мне казалось, что на нас кто-то искоса смотрит, слушает и ждёт, когда я ляпну какую-нибудь глупость."
    sl "Не удивляйся так, Семён! Привычка делать пробежку у меня уже давно."
    me "Давно — это насколько?"
    show sl smile sport close at center with dspr
    sl "Ещё с начальной школы."
    me "Ого."
    th "Спортсменка, пионерка, пока ещё не комсомолка, и просто красавица — это явно про неё."
    me "Могу только позавидовать. Мне вот никогда не хватало выдержки, чтобы каждое утро делать зарядку."
    show sl normal sport close at center with dspr
    "Она понимающе кивнула, безо всякой насмешки. Славя убрала руку с моего плеча, и я позволил себе расслабиться."
    sl "Зарядка у нас обязательная, от неё никуда не убежишь, к сожалению."
    me "Да, я б сейчас убежал куда подальше, лишь бы не махать руками-ногами по указке вожатых, честно."
    sl "Может быть, по утрам..."
    "Славя неожиданно запнулась на полуслове."
    show sl shy sport close at center with dspr
    me "Что — по утрам?"
    sl "Ты бы тоже мог делать пробежку, чтобы тренировать выдержку и силу воли... Стоит только начать...{w} Если хочешь, конечно. Я не вожатая, я не буду заставлять!"
    "Снова эта добрая улыбка. Я не знал куда деваться. Что-то не давало мне прямо отказаться, но в то же время я не хотел обременять себя обещаниями."
    me "Ох... Спасибо за предложение, правда..." 
    me "Но к вашему распорядку я ещё не привык, а сплю я обычно долго, так что... Не знаю. Подумаю."
    "Неловкость в словах чувствовалась настолько явно, что я поспешил закончить разговор и поскорей удалиться с глаз Слави долой."
    me "Ладно, пойду к себе, отнесу вещи."
    "Я покачал целлофановым пакетом с зубной щёткой и полотенцем."
    show sl smile sport close at center with dspr
    sl "Хорошо!" 
    "Славя нажала на кран умывальника и, совсем не боясь холодной воды, сполоснула лицо."
    hide sl with dissolve
    "Я же двинулся назад к своему домику."
    window hide
    scene bg ext_houses_day
    with dissolve
    window show
    th "Подумать только: девочка! сама! первая предложила мне!.. Это что-то из области фантастики..."
    th "Обычно про силу воли и полезные дела мне многократно говорили родители и некоторые знакомые, но Славе простительно, она не знает, как часто я бросал всевозможные начинания."
    "Но сама мысль присоединиться к девочке для пробежки по утрам была волнительной и чем-то соблазнительной. Впервые за долгое время я не отозвался на подобный намёк категорическим отказом."
    th "Что со мной делается-то? Атмосфера лагеря повлияла, не иначе!"
    stop music fadeout 2
    window hide
    jump d2_gymnastics

label d2_gymnastics:

    scene black
    with dissolve
    show screen central_text("День 2 — Девять кругов ада")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_house_of_mt_day
    with dissolve
    window show
    "Оставив пакет с умывальными принадлежностями на кровати в домике, я направился к памятнику Генде."
    window hide
    scene bg ext_square_day
    with fade
    play ambience ambience_camp_center_day fadein 1
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    window show
    "На площади уже собрались пионеры в спортивных формах, ожидающие начала зарядки. Опаздывавшие и только-только проснувшиеся ребята спешно подходили к умывальнику на газоне и, пихаясь, брызгая друг на друга водой, умывались, после чего присоединялись к остальным."
    th "Куда же мне приткнуться?"
    "Я определённо чувствовал себя чужим на этом празднике жизни, остановившись где-то в стороне от всех. Казалось, что я один такой, а все остальные уже сбились в группы и уж точно не были одиноки."
    "К моему большому удивлению, я приметил странного пионера, вроде бы общавшегося с приятелями. Но, как выяснилось, в разговоре он не принимал участия, он играл на портативной консоли, подозрительно напоминающей PSP."
    "На пионере была обычная физкультурная одежда — синие спортивные штаны и мятая белая футболка. За спиной зачем-то он нёс небольшой рюкзак. Однако не это привлекло моё внимание, а голова пионера."
    "Вернее отсутствие головы. Голову заменял белый ЭЛТ монитор для настольного компьютера."
    th "Что это? Самодельная маска шутки ради? Иначе я бы заметил его ещё в столовой на ужине."
    "Он, точно ощутив, что за ним наблюдали, повернулся ко мне. Белый экран монитора светился, показывая крупное изображение английской литеры L."
    "Я даже испугался на миг, но пионер снова склонил голову-монитор к приставке."
    "Меня спас чей-то окрик из гущи пионеров."
    play music music_list["so_good_to_be_careless"] fadein 1
    el_voice "Эй, Семён! Иди-ка сюда к нам!"
    show el smile pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    #TODO (к этапу работ по графике): заменить пионерскую форму на физкультурную обоим персонажам. 
    if d1_genda_flag:
        "Среди детей я увидел Электроника, звавшего меня. Рядом с ним стоял Шурик."
    else:
        "Среди детей я увидел Электроника, звавшего меня. Рядом с ним стоял неизвестный мне парень в очках, видимо, его приятель."        
    "Мне ничего не оставалось, кроме как подойти к ним."
    hide el
    hide sh
    with dissolve
    show el smile pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    el "Здор{i}о{/i}во."
    "Мы обменялись рукопожатиями."
    if (d1_dv_evening == True) or (d1_un_evening == True):
        show el laugh pioneer at cleft with dspr
        el "Семён, знакомься: это Шурик, мой товарищ и напарник по проекту. Шурик, это Семён, о котором я тебе вчера говорил."
        $ meet('sh', u"Шурик")
        "Шурик, подобно Сыроежкину, внешне тоже был почти неотличим от своего воплощения из советских фильмов. Пионерлагерь в очередной раз удивил меня."
        show el smile pioneer at cleft
        show sh normal_smile pioneer at cright
        with dspr
        sh "А, ясно. Рад знакомству!" 
        "Он пожал мне руку."
        show sh normal pioneer at cright with dspr
    sh "Как тебе у нас?"
    me "Э-э... В общем, ничего так, пока что мне нравится."
    sh "В технике шаришь?"
    me "Смотря в какой. В компьютерной — более-менее разбираюсь."
    show sh surprise pioneer at cright with dspr
    sh "Приходи в наш клуб после завтрака."
    me "Может быть загляну."
    show sh normal pioneer at cright with dspr
    "Сыроежкин прервал нас."
    show el serious pioneer at cleft with dspr
    el "Довольно об этом. Сейчас есть куда более важные вещи."
    "Он вновь нравоучительно поднял руку."
    el "Очень-очень важные, Семён."
    me "Ну, не тяни."
    show el laugh pioneer at cleft with dspr
    el "Утреннее построение с зарядкой. Только во время него можно по достоинству, с уверенностью и в полной мере оценить девчонок из лагеря: их физические данные, внешность, объёмы, гибкость, привлекательность... Вот!"
    th "Блин, кто о чём, а этот всё про пионерок."
    show el serious pioneer at cleft with dspr
    el "Тема такая, Семён. Сначала все пионеры становятся в одну шеренгу, рассчитываются на первый-второй. Чётные потом образуют вторую шеренгу. Мы же должны оставаться в первой, для этого надо становиться через одного на нечётных местах."
    me "И зачем?"
    show el grin pioneer at cleft with dspr
    el "Чтобы лучше видеть нашу Ольхен, конечно же! Когда она показывает всякие упражнения, подпрыгивает... Ну, ты понимаешь, о чём я говорю, Семён? Зарядка — это не наказание, а услада для глаз."
    "Он заговорщически подмигнул."
    show sh upset pioneer at cright with dspr
    "У Шурика было другое мнение на этот счёт."
    sh "Я не согласен. Не лучше ли нам быть во второй шеренге? Во-первых, можно рассмотреть девчонок не только впереди, но и рядом, не придётся оглядываться, чтобы оценить их, и нам никто замечания не сделает. Во-вторых, будут упражнения с наклонами... По-моему, эти формы сзади не менее впечатляющи, чем груди."
    show el serious pioneer at cleft with dspr
    el "А я думаю, что надо вставать в первую шеренгу!" 
    show el smile pioneer at cleft with dspr
    el "Потом, Ольга Дмитриевна не девочка, а женщина, она сто очков форы даст нашим пионеркам..."
    show sh normal_smile pioneer at cright with dspr
    sh "Но ведь она в спортивной ветровке, а девочки — в тонких маечках, если уж говорить о груди. И в шортиках.{w} Ты забываешь про ноги, Серёг. В женской фигуре всё должно быть прекрасно."
    show el serious pioneer at cleft with dspr
    with vpunch
    el "Абсолютного идеала нет! Но есть те, у кого абсолютно идеальные сиськи!"
    show sh scared pioneer at cright with dspr
    "Я испугался, что Сыроежкин вот-вот потеряет контроль над собой. Как бы эти двое не подрались из-за своих неделикатных предпочтений. К тому же, на нас уже начали коситься некоторые пионеры."
    me "Тихо, тихо..."
    show el upset pioneer at cleft with dspr
    show sh normal_smile pioneer at cright with dspr
    "Шурик деловито коснулся очков на переносице."   
    sh "Серёг, вечно ты идёшь по лёгкому пути. Да, идеала может и нет, но его надо искать. Нужно получать удовольствие от процесса, высматривать, отсеивать. Тебе же известны научные методы познания и исследования? Наблюдение в физике, например. Поэтому я предлагаю во второй ряд."
    th "Серьёзный аргумент."
    show el serious pioneer at cleft with dspr
    el "Семён! А ну-ка рассуди нас."
    me "Кто, я?"
    show el smile pioneer at cleft with dspr
    el "Ну а кто ещё же, ты новенький, со свежей головой и незамутнённым взглядом. Лучше первый или второй ряд?"
    show el grin pioneer at cleft with dspr
    el "Я знаю, что ты в одном домике с вожатой спишь, поэтому выбрать должен правильно — первую шеренгу..."
    show sh serious pioneer at cright with dspr
    sh "Но-но, Сыроега, пусть он сам сделает выбор."
    "Я думал недолго, сразу решив уступить им обоим."
    show el normal pioneer at cleft
    show sh normal pioneer at cright
    with dspr
    me "Каждый из вас по-своему прав. Сколько ещё у нас дней впереди? Давайте по очереди, сегодня в одной шеренге, завтра в другой."
    show sh serious pioneer at cright with dspr
    sh "Да, так будет справедливо. В какой шеренге мы стояли вчера?"
    show el laugh pioneer at cleft with dspr
    el "Во второй! Поэтому сегодня в будем первой!"
    show sh upset pioneer at cright with dspr
    "Шурик выглядел побеждённым."
    sh "Значит, завтра как я предлагал. Хорошо?"
    show el smile pioneer at cleft with dspr
    el "Хорошо-хорошо... О, пришли."
    stop sound_loop fadeout 4
    hide sh
    hide el
    with dissolve
    show mt normal pioneer at center with dissolve
    #show bt; show lk; TODO (к этапу работ по графике): Мод-тян и Бан-тян в физкультурной форме, см. спрайт Мод в демоверсии abcb.
    "На площадь явились все трое вожатых: Ольга Дмитриевна в спортивном костюме, ещё одна девушка чуть ниже её ростом и темноволосый парень в очках, явно студент старших курсов, возможно, уже отучившийся."
    "Их имена я сразу вспомнил — Инга Максимовна и Дмитрий."
    stop sound_loop fadeout 1
    if (d1_genda_flag == False):
        "О них Сыроежкин успел немного рассказать до того, как мы разошлись вечером."
    "Ольга Дмитриевна резко дунула в свисток."
    #TODO: sfx whistle — свисток.
    mt "Старший отряд! В одну шеренгу ста-ановись!"
    hide mt with dissolve
    #hide bt; hide lk
    "Все пионеры засуетились, выстраиваясь по команде."
    show el normal pioneer close at right with dissolve
    el "Становимся через одного, не забыл?"
    me "Нет, конечно."
    hide el with dissolve
    "Мы заняли места точно по указанию Сыроежкина."
    "Я встал сбоку от незнакомой мне девочки и тоже представил себя пионером..."
    "Чувствуя себя в окружении стольких людей не совсем привычно, я просто постарался расслабиться. Глянул на Сыроежкина, а он, заметив меня, показал большой палец."
    show el smile pioneer close at right with dissolve
    el "Всё путём."
    hide el with dissolve
    "А зарядка уже началась. К тому же выяснилось, что старший и младший отряд расположили друг напротив друга — по обе стороны площади, и за каждым из двух отрядов следило по вожатому." 
    show mt normal pioneer at center with dissolve
    "С нами, естественно, осталась Ольга Дмитриевна, а её коллега ушла к младшим. Без своего отряда был только парень с шарфиком, как мне показалось, в виде дохлого удава. Этот парень облокотился о памятник Генде и просто наблюдал за нами."
    "Пока я размышлял, зачем шарф летом, раздался громкий голос."
    show mt smile pioneer at center with dspr
    mt "Здравствуйте, пионеры."
    all "Здрась!"
    "Все так дружно гаркнули, что я даже вздрогнул и запоздало присоединился к выкрику, поприветствовав Ольгу Дмитриевну последним, особо не стараясь."
    "А у них это здорово получилось!"
    show mt surprise pioneer at center with dspr
    mt "Вы хорошо сегодня спали? Все здоровые и выспавшиеся перед новой неделей?"
    all "Да!"
    "На этот раз я не отстал и крикнул вместе со всеми, правда, без энтузиазма."
    show mt grin pioneer at center with dspr
    mt "Очень хорошо! К свершениям подвигов и зарядке готовы?"
    all "Да!"
    stop music fadeout 2
    play music music_list["always_ready"] fadein 2
    "Вожатая дунула в свисток."
    show mt smile pioneer at center with dissolve
    mt "Смирно! Руки по швам!"
    "Все выпрямились."
    th "Ну вот, началась муштра."
    if d1_dv_evening:
        th "А говорили, что она пионеров не гоняет. Соврали?"
    "И если возвещавший из динамиков о начале нового дня голос Ольги Дмитриевны был добрым, то сейчас он звучал строго и громко — командовать она умела, да ещё как, и мне хватило секунды, чтобы понять это."
    mt "Направо равняйсь!"
    "Мы повернули головы, и я уставился вдаль, мимо лиц в шеренге."
    mt "Отставить."
    mt "Налево равняйсь!"
    "Я попытался высмотреть кого-то из знакомых, но команда «Отставить» прозвучала сразу, и я не успел никого заметить."
    mt "Напра-во!"
    "Пионеры в шеренге развернулись."
    mt "По кругу — бегом марш!"
    "Вожатая опять свистнула."
    hide mt with dissolve
    show mt grin pioneer far at center with dissolve
    "Все, в том числе и я, рванули следом за первым человеком из ряда. Так же было и в младшем отряде. Они бежали вокруг памятника, а для нас центром стала Ольга Дмитриевна."
    "Мы бежали быстро, и уже на пятом кругу я взмолился, чтобы поскорей прозвучал свисток. Но даже когда мы замедлились, для меня, отвыкшего от подобной активности, пытка не окончилась: нам скомандовали пройти по кругу на носках, на пятках и гуськом."
    th "Когда я вышел из автобуса, я думал, что попал в рай. Я серьёзно ошибся..."
    "Утешало лишь то, что нас не заставили бежать по периметру площади или всего лагеря. Стоически выдерживая экзекуцию, я ни разу не остановился, чтобы перевязать шнурки или отдохнуть каким-либо образом. В горле сильно пересохло."
    "На девятом кругу мы тянули руки вверх, в такт вдоху и выдоху, пока не остановились в ряд по команде."
    hide mt with dissolve
    show mt smile pioneer at center with dissolve
    mt "Нале-во! На первый-второй рассчитайсь!"
    "Зазвучали выкрики «Первый!», «Второй!», «Первый!», пока одна из девочек в конце шеренги не сказала: «Расчёт окончен!»."
    "Вожатая обвела взглядом наш отряд."
    mt "Вторые номера, в две шеренги стройся!"
    "Я остался на месте, тогда как мои соседи по ряду сделали по два шага — назад и вбок, за спину человека по правую руку, тем самым построив ещё одну шеренгу."
    mt "Первые номера, шаг вперёд!"
    "Теперь я повторил то, что сделали Электроник и все остальные из нашего ряда — сделали большой шаг, разорвав дистанцию между двумя шеренгами."
    mt "На расстояние вытянутых рук — ста-ановись!"
    "Ольга Дмитриевна развела руки в стороны, показывая, как надо, и пионеры повторили за ней, чтобы было достаточно пространства для спортивных упражнений."
    stop music fadeout 2
    play music music_list["lightness"] fadein 4
    mt "Сначала — разминаем спину и плечи. Ноги на уровне плеч... И-и раз, и-и два..."
    "Вожатая плавно взмахнула руками: правая взметнулась вверх, левая — вниз. На слове «раз» все меняли положение рук со сжатыми кулаками."
    hide mt with dissolve
    "Пока мы выполняли упражнения, я изредка успевал понаблюдать за другими пионерами. Сбоку было видно не всех, поэтому я несколько раз оглядывался на второй ряд."
    "И действительно, девушки приковывали к себе всё внимание, особенно те, с кем мне вчера удалось поговорить — знакомые лица нетрудно было отыскать." 
    #TODO (к этапу работ по графике): заменить на физкультурную форму, здесь и далее по ивенту для пионерок, кроме Слави, Уныл и СССР-тян. 
    #Опционально и не так важно: СССР-тян можно сделать шортики пофизкультурней и покороче. Как в советских фильмах.
    show dv normal pioneer far at left with dissolve
    "Алиса стояла почти в конце первого ряда, далеко от меня, но заметить её было легко из-за яркой причёски и спортивного костюма, в котором девочка заметно выделялась: её топ с нарисованной жёлтой молнией, пересекавшей грудь, открывал взору плоский живот девочки, — у иных пионерок наряды такой откровенностью не отличались."
    show dv smile pioneer far at left with dissolve
    "То и дело Алиса посматривала куда-то вперёд, улыбаясь, и я увидел, что как раз напротив неё среди пионеров младшего отряда была Ульяна."
    show us smile sport far at right with dissolve
    "Она, как ни странно, добросовестно исполняла упражнения... Ещё бы — без сил и здорового тела от вожатых не побегаешь!"
    #TODO (к этапу работ по графике): чертовски не хватает эмоции с высунутым языком. Войдёт в ТЗ по спрайтам.
    show us grin sport far at right with dissolve
    "Но Ульяна ещё успевала корчить рожи Алисе, будто пытаясь рассмешить её..."
    hide dv
    hide us
    with dissolve
    "Я оглянулся на второй ряд позади меня."
    show sl smile sport at cleft with dissolve
    "Славю тоже легко было найти — она была единственной из пионерок в форме чёрного цвета. Каждое движение гибкого тела девочки было плавным, изящно отточенным... Сразу видно: спорт — её конёк. Даже после утренней пробежки она спокойно осилила те злополучные девять кругов бегом по площади, а сейчас без устали повторяла упражнения за вожатой."
    show un normal sport at cright with dissolve
    "Неподалёку от Слави находилась Лена, будто специально державшаяся поближе к ней на случай неприятностей."
    "Под стать своему замкнутому характеру, Лена была в мешковатых невзрачных шортах и свободной белой футболке, чтобы не открывать чужим взглядам плечи и выдающуюся грудь. Последнее, при всём желании девочки, не удавалось."
    "Лена будто через силу выполняла упражнения."
    "Пожалуй, ей, как и мне, тоже совсем не хочется быть на зарядке, но по другим причинам..."
    "Девочка чуть не заметила меня."
    hide sl
    hide un
    with dissolve
    "Я едва заставил себя отвернуться и посмотреть, какое упражнение на этот раз показывает Ольга Дмитриевна, и вот с ней-то я и встретился взглядом."
    show mt smile pioneer at center with dissolve
    "Вожатая, глядя мне в глаза, многозначительно усмехнулась, и я почувствовал, как горю от стыда, смутно догадываясь, что она имела в виду."
    "Наверно, она подумала: «Я знаю, куда ты смотришь, Семён. Ты совсем не порядочный пионер...»"
    "И такое знакомое выражение лица, как утром после моего пробуждения..."
    th "Всё-таки не надо было палиться перед ней — меньше поводов для выговоров и замечаний."
    #show lk
    "Ольга Дмитриевна неожиданно уступила место подошедшему парню-вожатому."
    mt "Пожалуйста, Дима! Упражнения на живот и ноги."
    hide mt with dissolve
    "А сама отошла к вожатой младшего отряда. Они шепнули друг другу о чём-то и посмеялись."
    show el shocked pioneer close at right with dissolve
    "Я глянул на Электроника. На его физиономии читалось непонимание."
    el "Что за дела? А как же прыжки?"
    hide el with dissolve
    "Вожатый, названный Дмитрием, дунул в потёртый свисток, вытащенный из кармана."
    lk "Делаем наклоны, тянемся до мысков руками. Ноги не сгибаем! И-и раз! И-и..."
    "Пока мы нагибались, касаясь кончиками пальцев своих кед или асфальта — у кого как получалось — я думал над словами Шурика о наблюдении."
    "Лучше бы я, конечно, был не среди пионеров, а прохлаждался в другом месте. Однако эти взгляды украдкой вызвали странные мысли. Их я бы мог назвать... симпатией?"
    "Возникло желание не казаться перед этими девочками не совсем уж безнадёжным затворником, которым я являюсь."
    th "Проклятые Сыроежкин и Шурик слишком легко влияют на меня дурными разговорами."
    #hide lk
    show mt normal pioneer at center with dissolve
    "После разминки на ноги вожатого Диму опять сменила Ольга Дмитриевна, когда я уж было решил, что эта зарядка не закончится вовек."
    "Прозвучал отрывистый свист."
    mt "Вторые номера, в одну шеренгу стройся!"
    "И слева, и справа от меня в ряд вернулись пионеры, снова разделив меня с Элом и Шуриком."
    show mt smile pioneer at center with dspr
    mt "Зарядка окончена! Марш по палатам заправлять свои постели и переодеваться к построению!"
    hide mt with dissolve
    "Послышался обречённый стон некоторых особо ленивых или просто голодных пионеров, но шеренга рассыпалась, и все послушно отправились к своим домикам."
    "Невзирая на болящие после зарядки мышцы ног, я побежал, чтобы поскорей разделаться с оставшимися обязанностями и наконец пойти в столовую."
    stop ambience fadeout 1
    stop music fadeout 2
    window hide
    jump d2_lineup

label d2_lineup:

    scene black
    with dissolve
    show screen central_text("День 2 — Построение")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    play music music_list["so_good_to_be_careless"] fadein 0
    scene bg int_house_of_mt_day
    with dissolve
    play ambience ambience_int_cabin_day fadein 0
    window show
    "В домике было прохладней, чем на улице."
    "Постель я заправил быстро, даже не заморачиваясь, чтобы подушка стояла треугольником."
    "Тяжело дыша, я скинул физкультурные шорты с футболкой и переоделся в обычную пионерскую форму."
    "Я взял красный галстук и с сомнениями повертел его в руках."
    th "Разве это не парадная форма? Белая рубашка и шорты на ремне — всё это обычно надевают для всяких приёмов и торжественных мероприятий, вроде начала и конца смены, концертов и тому подобного..."
    "Но вчера, как я убедился, большинство пионеров ходило именно в такой одежде и с галстуками, разве что без пилоток."
    "В домик постучались. Это была вожатая."
    play sound sfx_knock_door7_polite
    mt "Переоделся, Семён? Входить уже можно?"
    me "Да."
    show mt surprise pioneer at center with dissolve
    mt "Чего же тогда ждёшь? Пора на построение."
    th "Наверно, всё дело в нём, вот и официальный повод для парадной формы. Пионерам, видимо, лень переодеваться ещё раз после построения и завтрака."
    me "Думал, надевать форму или нет..."
    show mt laugh pioneer at center  with dspr
    mt "Индюк тоже думал, да в суп попал. Быстрее надо, Семён, без тебя построение не начнётся."
    me "Что, правда?"
    show mt angry pioneer at center  with dspr
    mt "Не испытывай моё терпение, пожалуйста."
    th "Что-то она слишком сурова."
    "Я принялся торопливо повязывать галстук как-нибудь."
    show mt smile pioneer close at center  with dissolve
    "Вожатая неожиданно улыбнулась, взяла у меня галстук из рук."
    mt "Ты пионер, так?"
    me "Да..."
    mt "А пионеры должны уметь повязывать галстук."
    "Я лишь нахмурился."
    mt "Иди сюда, я покажу, как надо, и не делай такое недовольное лицо!"
    "И она ловко затянула на мне красный узел, так что я ничего не успел ни понять, ни возразить..."
    show mt grin pioneer close at center  with dspr
    mt "Отлично!"
    "Я чувствовал себя так, словно мне на шею накинули петлю..."
    th "Чего здесь такого отличного?!"
    show mt normal pioneer close at center  with dspr
    mt "В следующий раз сам будешь завязывать."
    th "Сомневаюсь, что у меня выйдет, я даже не понял, как..."
    mt "Ну, иди!"
    "Я, подгоняемый вожатой и долгом, выскочил из домика."
    hide mt with dissolve
    window hide
    scene bg ext_square_day with fade
    window show
    "На площади нас всех снова собрали, и я не стал делать предположений, для чего, просто наблюдая за происходящим. " 
    "Нарядные пионеры (разве что без пилоток), стояли в две шеренги по обе стороны памятника, с которого Генда молчаливо взирал на них."
    "Пару минут мы ждали, пока не появилась Ольга Дмитриевна, быстро переодевшаяся в свою форму после меня."
    show mt normal panama pioneer at center with dissolve
    if (d1_genda_flag == True) or (d1_dv_evening == True):
     "А ещё на ней та самая шляпа-панама, за которую получила прозвище от пионеров."
    stop music fadeout 2
    show mt smile panama pioneer at center with dspr
    mt "Старший отряд сдаёт пост. Дежурство по лагерю передаётся младшему отряду."
    "Их вожатая Банникова вызвала какого-то парня в очках из строя."
    #show bt
    bt "К поднятию флагов — приступить!"
    "И тот с важным видом отправился к флагштокам."
    #hide bt
    #TODO: на самом деле тут полагается другой звук — совмещение горна и барабана, применяется при поднятиях флага и спуске в заключительный день смены. Текущий звук — заглушка.
    play sound_loop sfx_dinner_jingle_normal fadein 3
    "Другой пионер, тоже в очках, по имени Нафанаил из младшего отряда по команде вожатой Банниковой поднял горн с прицепленным снизу красным знаменем и загудел в инструмент, а нестриженый пацан, названный Мишей Вересаевым, с жаром застучал по барабану палочками."
    $ meet('nf', u"Нафаня")
    $ meet('vz', u"Вересаев")
    mt "Равнение на флаги!"
    hide mt with dissolve
    "Все как один, кроме горниста с барабанщиком, в полуобороте вскинули руки ко лбу, отдавая пионерский салют — и я, замешкавшись на мгновение."
    "Торжественная музыка звучала всё время, пока флаги не были задраны на самый верх, где их один за другим расправил ветер."
    "Что-то тяжёлое во мне будто надломилось, а в горле собрался ком, которого я совсем не ждал, будучи малознакомым с временами, когда такие ритуалы были обычным явлением."
    stop sound_loop
    play music music_list["get_to_know_me_better"] fadein 3
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    "Горн и барабан утихли, когда пионеры вернулись в шеренгу своего отряда."
    "После этого нам велели сойтись в один ряд у памятника, и тут пионеры, уже не стесняясь, забыли о порядке и становились рядом со своими знакомыми и друзьями, с кем особенно хотелось."
    "Теперь я был рука об руку с Шуриком и Сыроежкиным, которые довольно быстро взяли меня в оборот ещё до зарядки."
    "Не то что бы я был враждбно настроен к ним, просто их вимание ко мне было чуть излишним."
    show mt smile panama pioneer at cleft with dissolve
    "Началась общая линейка. Вожатые собрались вместе. Ольга Дмитриевна с улыбкой обвела всех взглядом."
    show mt grin panama pioneer at cleft with dspr
    mt "Кто помнит, какой сегодня день?"
    show us laugh pioneer at right with dissolve
    "Ульяна вытянула руку, как школьник за партой, едва не выскакивая из шеренги."
    us "Понедельник, понедельник!!!"
    "Инга Максимовна зашикала на неё, чтобы девчонка не кричала и не высовывалась."
    hide us with dissolve
    show mt smile panama pioneer at cleft with dspr
    mt "А ещё?"
    boy_A "Семнадцатое..."
    mt "Уже теплее! Хорошо, а ещё?"
    "Все как-то немного напряглись, и я тоже задумался: в самом деле, что может означать сегодняшний день? Какой он? Солнечный? Тёплый? Или что-то другое?"
    girl_A "У кого-то день рождения?"
    show mt laugh panama pioneer at cleft with dspr
    mt "Горячо! Да, день рождения. А у кого?"
    "Все пожали плечами — никто из пионеров не оказался именинником." 
    show mt smile panama pioneer at cleft with dspr
    mt "Подсказываю: я говорю об известном человеке, нашем соотечественнике."
    show el normal pioneer close at cright  with dissolve
    "К моему уху склонился Электроник."
    el "А, это у нас и в прошлый понедельник было..." 
    hide el with dissolve
    "Но первой догадалась Славя."
    show sl smile2 pioneer at cright with dissolve
    sl "Сегодня родился русский путешественник и этнограф Николай Миклухо-Маклай. Вы его имели в виду, Ольга Дмитриевна?"
    show mt grin panama pioneer at cleft with dspr
    mt "Правильно! Молодец, Славя!"
    hide sl with dissolve
    show dv normal pioneer at right with dissolve
    "Двачевская сложила рупором ладони."
    dv "У-у-у! А родившийся сегодня бас-гитарист из Black Sabbath незаслуженно забыт!"
    show mt smile panama pioneer at cleft with dspr
    "Несколько пионеров в унисон задали Алисе одинаковые вопросы." 
    all "А кто это? А как его зовут?" 
    "На площади поднялся смех."
    show dv angry pioneer at right with dspr
    "Двачевская побагровела и надулась, скрестив руки."
    dv "Как можно такое не знать? Не понимаю!.."
    hide dv with dissolve
    "Ольга Дмитриевна успокоила детей."
    show mt normal panama pioneer at center with dissolve
    mt "Мы все немного путешественники в душе, и поэтому для вас наверняка будет нерадостной новостью, что запланированный поход откладывается."
    "Снова раздалось протяжное «У-у!», и к Алисе в этот раз присоединились все остальные."
    mt "Сегодня у вас свободный день для занятий в кружках. Напоминаю ещё раз, что в конце смены пройдёт День творческой, или, как правильней сказать, художественной самодеятельности, поэтому всем добровольцам, желающим поучаствовать, советую не терять время понапрасну и готовиться к выступлению заранее." 
    all "А пляж? А купаться?"
    show mt smile panama pioneer at center with dspr
    mt "Вот про купание — хорошая новость. На этой неделе — обязательно! Более того: без какого водного праздника не обходится ни одна смена в пионерском лагере?"
    "Дети ответили воплем."
    all "День Нептуна-а!"
    mt "Верно! И организация праздника — не самое лёгкое дело. Прежде всего, к завтрашнему дню надо будет выполнить несколько поручений..."
    hide mt with dissolve
    "Ольга Дмитриевна принялась рассказывать, к чему и как нужно готовиться, а я от нечего делать стал разглядывать пионеров, уже не отвлекаясь на построение."
    "Детей в нашем отряде было довольно много, двадцать восемь человек, почти как в обычном школьном классе. Младших, с которыми сейчас говорила вожатая Инга, оказалось больше на три пионера."
    show dv normal pioneer at right with dissolve
    "Алиса на противоположном от меня краю шеренги откровенно скучала."
    "Она только изредка стреляла глазами по пионерам... {w=.3}как будто выбирая жертву."
    "И встречаться с ней взглядом никто не рисковал."
    show dv smile pioneer at right with dspr
    th "Чёрт!"
    "А вот я поздно сообразил, что пялиться на неё было не самой лучшей затеей!"
    "Внезапно я понял, что мы уже какое-то время смотрим друг на друга, неотрывно..."
    hide dv with dissolve
    show mt smile panama pioneer at center with dissolve
    "Я быстро отвёл глаза, делая вид, что слушаю вожатую."
    th "Надо же было так неаккуратно попасться!.."
    mt "...наш отряд меньше, но это значит, что мы приложим вдвое больше сил, чтобы стать первыми! А как старшие, вы должны помогать младшим."
    hide mt with dissolve
    th "Надеюсь, они не каждый день так собираются. Невероятная скучища."
    "Но здесь я был не единственным, кто слушал свою вожатую вполуха."
    show us pioneer at left with dissolve
    "Ульянка крутилась в шеренге, не в силах устоять на одном месте даже рядом с Алисой, ёрзала и, судя по виду, была готова сбежать в любой момент."
    "Останавливало её только то, что Инга Максимовна посматривала на неё, явно зная о намерениях своей подопечной..."
    th "А Ульяна с Двачевской не сильно любят работать, а?"
    hide us with dissolve
    "Я отыскал Славю."
    show sl normal pioneer at left with dissolve
    "Она, тоже переодевшаяся, стояла опрятная в середине строя, внимательно и безмятежно слушая Ольгу Дмитриевну и ни на что не отвлекаясь."
    "Кажется, ей даже нравилось, что та раздает всем поручения на следующую неделю."
    th "Как бы мне не пришлось в этом участвовать..."
    hide sl with dissolve
    "Рядом со Славей я заметил Лену."
    show un normal pioneer at left with dissolve   
    "Она стояла там же, в центре, в окружении пионеров, и было видно, что вынужденно, из-за Слави поблизости."
    "Лена была чем-то смущена и потому только изредка поднимала голову, видимо, дожидаясь конца построения, чтобы опять где-нибудь затеряться."
    "В этот раз я не успел вовремя глянуть в сторону."
    show un shy pioneer at left with dissolve
    "Словно почувствовав на себе мой взгляд, она посмотрела на меня..."
    "И тут же отвернулась, только еще гуще покраснев."
    hide un with dissolve
    show mt smile panama pioneer at center with dissolve
    mt "...Это будет вам хорошей возможностью проявить самостоятельность и поучиться ответственности."
    mt "А я посмотрю, как вы с этим справитесь."
    th "О чём она только что говорила?"
    "Наконец Ольга Дмитриевна перевела дух и только тогда улыбнулась, оглядывая всех нас."
    show mt normal panama pioneer at center with dspr
    mt "Что ж... По расписанию сегодня дежурит отряд младших. Кто-нибудь желает помочь им произвести уборку территории лагеря?{w} Кроме Славяны, конечно."
    "Голубоглазая девочка вернулась в строй."
    show mt surprise panama pioneer at center with dspr
    mt "Нет? Тогда назначим пионеров..."
    th "О нет, только не это."
    show mt smile panama pioneer at center with dspr
    "На моё счастье, Ольга Дмитриевна назвала имена неизвестных мне детей. Они были обречены на помощь с мытьём полов в столовой и приборку клубных помещений до их закрытия вечером."
    if (d1_dv_evening == True) or (d1_un_evening == True):
        show mt normal panama pioneer at center with dspr
        mt "Кстати. Вчера к нам в лагерь приехал ещё один пионер..."
        th "Что же она собралась сказать всем про меня?"
        show mt smile panama pioneer at center with dspr
        "Вожатая подозвала меня к себе."
        "Я словно прирос к асфальту, а во мне до предела натянулись нервы. Но всё равно, преодолев секундное волнение, я шагнул к Ольге Дмитриевне."
        "Она положила мне руки на плечи, повернув к детям."
        mt "Его зовут Семён Персунов. Будьте обходительными и дружными вместе!"
        th "Точно, я же просил её вчера представить меня пионерам в другой раз."
        "Несмотря на это, я всё равно вернулся в шеренгу с беспокойством, отвыкший от внимания посторонних людей."
    stop music fadeout 2
    show mt normal panama pioneer at center with dspr
    "Вожатая достала из кармана небольшие наручные часики со сложенным ремешком."
    mt "Построение окончено. Напра-во!"
    mt "Отряды, шагом марш на завтрак!"
    hide mt with dissolve
    stop sound_loop
    play sound sfx_dinner_jingle_speaker_tape
    "Заиграла музыка из динамиков, и мы, позабыв о том, что нам велели держать строй, врассыпную с младшими дружно помчались к столовой (а некоторые — к умывальнику, чтобы сполоснуть руки перед едой). Несмотря на это, вожатые не стали останавливать нас и требовать идти не спеша, чеканя шаг и под песню."
    window hide
    scene black 
    with dissolve
    window show
    "..."
    "......"
    stop sound fadeout 1
    "........."
    window hide
    jump d2_clubs_common_event

label d2_clubs_common_event:

    scene black
    with dissolve
    show screen central_text("День 2 — Знакомство с лагерем")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    play music music_list["smooth_machine"] fadein 1
    play ambience ambience_int_cabin_day fadein 0
    scene bg int_house_of_mt_day
    with dissolve
    window show
    "Уф-ф-ф, наконец-то. Здесь, в домике — тихо и спокойно..."
    "Раннее пробуждение, зарядка, вся эта беготня, размахивание руками и ногами так утомили меня, что завтрака я почти не заметил. Еда будто сгорела, не успев попасть в желудок. Я до сих пор чувствовал себя голодным, хотя раньше бывало и так, что мне хватало бэпэшки в день." 
    "Не то чтобы хватало, на самом деле, но выбирать не приходилось. И ведь жил как-то."
    "А теперь местного завтрака мало."
    "Я плюхнулся на заправленную кровать, не беспокоясь, что сомну её и снова приведу в непрезентабельный вид, за что меня наверняка пожурит вожатая."
    th "Что же теперь делать?"
    "Вспомнилось приглашение Шурика посетить их кружок. Однако после того спора между ним и Элом идти туда не очень хотелось."
    "Может быть, я ещё не знал Сыроежкина достаточно хорошо, но мне хватило его беспрестанных мыслей о девочках, словно кроме этого ничего не существовало."
    "В домик зашла Ольга Дмитриевна, даже не постучавшись."
    show mt normal panama pioneer at center with dissolve
    mt "Семён? Поднимайся, есть дело для тебя."
    show mt grin panama pioneer at center with dspr
    mt "Ты сегодня не пионер, а Миклухо-Маклай, и поэтому тебе придётся совершить большое путешествие по лагерю."
    th "Ошибаетесь, я Марти Макфлай, а единственное путешествие, которое меня сейчас интересует — это от ворот лагеря до своего компьютера."
    me "Зачем?"
    "Она дала мне пару листов, напоминавших пустую анкету."
    show mt smile panama pioneer at center with dspr
    mt "Это обходной листок."
    mt "Там всё указано. До обеда тебе надо обойти всех и получить подписи."
    show mt grin panama pioneer at center with dspr
    mt "Заодно и с лагерем познакомишься!"
    show mt smile panama pioneer at center with dspr
    mt "А это..."
    "Мне уже не нужно было объяснять — кроме листов я получил медицинскую справку, причём частично заполненную."
    mt "...отнеси медсестре Виолетте. Ты же не был на медосмотре со всеми, когда мы заезжали в лагерь, поэтому тебе следует пройти его."
    me "А... Спасибо."
    show mt normal panama pioneer at center with dspr
    mt "Не забудь пройти тест о себе."
    "Вожатая обратила моё внимание на листок с перечнем вопросов."
    mt "Как обойдёшь всех в любом порядке, отдашь мне обе бумаги, понял? Если меня в домике не будет, иди в административный центр."
    me "Понял."
    show mt smile panama pioneer at center with dspr
    mt "Хорошо. Не теряй время! У тебя всего день на всё про всё. Чем раньше вступишь в кружок, тем лучше."
    me "То есть, участие в кружке — это обязательно?"
    show mt grin panama pioneer at center with dspr
    mt "Конечно! Если будешь сидеть в домике всё время, считай, поездка в лагерь пошла насмарку. Вперёд!"
    hide mt with dissolve
    "И она ушла, весьма довольная собой."
    "А я задумчиво смотрел, что же мне предстоит..."
    "Первое, что привлекло моё внимание больше всего — это справка, оказавшаяся кладезью информации."
    "«Министерство здравоохранения СССР»... «Форма №079/у»... «Медицинская справка на школьника, отъезжающего в пионерский лагерь»."
    th "Надо же! Справка из поликлиники, будто я туда ходил перед поездкой в лагерь! Но ничего такого не было."
    th "Или я просто не помню об этом. Откуда же она взялась?"
    if d1_dv_evening:
        "Не меньший шок у меня вызвала новость, что я нахожусь в СССР, существующем в двухтысячных годах."
        th "Ох ты ж!.."
        "Это что же получается?"
        "Пришибленный новостью, я медленно сел на кровать."
    "Что немаловажно, здесь была вся контактная информация обо мне."
    "Справка подписана моими фамилией, именем и отчеством, тут же были домашний адрес с телефоном, номер школы и класса." 
    "Единственное «но» — они не соответствовали реальным, кроме ФИО. И я не знал, как воспринимать сфабрикованный документ: принесёт ли это мне в будущем проблемы или нет?"
    "Кроме того, я заметил, что дата рождения тоже присутствует."
    th "Май девяносто первого года."
    "Хоть дата была написана ошибочно — ведь я родился осенью, по ней выходило, что в этом мире мне семнадцать лет."
    if d1_un_evening:
        th "Значит, я не соврал Лене о возрасте."
    "На оборотной стороне справки были пустые поля, которые должен заполнять врач пионерского лагеря."
    th "Так, с этим всё понятно."
    th "А вот все свои контактные данные надо зафиксировать. Может быть, по этому номеру телефона я смогу дозвониться, а главное, тут есть адрес квартиры на случай, если я не смогу вернуться." 
    "Я торопливо переписал в блокнот информацию со справки."
    "..."
    "Анкета, которую мне дали, была рассчитана на выявление интересов и характера пионера в общих чертах. Все эти психологические штучки мне были известны ещё со школы, где неоднократно проводились такие опросы."
    th "Но почему бы не заполнить анкету?"
    "Я сел и начал по-быстрому отвечать на коротенькие вопросы об интересах, досуге и взаимоотношениях с другими детьми."
    "Покончив с опросом, я отложил бумажку в сторону."
    "...Бегунок, он же обходной лист."
    "Список всех действующих кружков оказался небольшим, но мне было лень волочиться по всему лагерю за подписями. Да и вообще, идея ставить закорючки за посещение показалась мне вершиной формализма."
    th "А может, ну его?"
    th "Останусь здесь, поваляюсь в кровати, почитаю, сыграю ещё раз в «Электронику»?"
    "У меня не было какого-то особого желания оправдывать чьи-то ожидания."
    "Ну и ладно. День впереди длинный. Успею как-нибудь... Может ещё смогу тайком поплавать в речке."
    "Но сначала помешает узнать об этом лагере поподробнее, раз уж я здесь оказался."
    window hide
    stop music fadeout 1
    jump d2_morning_map_prep

label d2_morning_map_prep:
    
    $ disable_all_zones()

    $ set_zone('music_club', 'd2_event_mus_club')
    $ set_chibi("music_club",  "?")
    $ set_zone('clubs', 'd2_event_clubs')
    $ set_chibi("clubs",  "?") #TODO (код): пофиксить месторасположение иконки ? — между зданиями кружков.
    $ set_zone('camp_entrance', 'd2_event_camp_entrance')
    $ set_zone('dv_us_house', 'd2_event_dv_us_house')
    $ set_zone('dining_hall', 'd2_event_dining_hall')
    $ set_zone('sport_area', 'd2_event_sport_club')
    $ set_chibi("sport_area",  "?") #TODO (код): пофиксить месторасположение иконки ? — или между футбольным полем и спортзалом, или на правом нижнем углу футбольного поля.
    $ set_zone('beach', 'd2_event_beach')
    $ set_zone('me_mt_house', 'd2_event_me_mt_house')
    $ set_zone('library', 'd2_event_library')
    $ set_chibi("library",  "?")
    $ set_zone('medic_house', 'd2_event_aidpost')
    $ set_chibi("medic_house",  "?")
    $ set_zone('estrade', 'd2_event_green_theatre')
    $ set_zone('square', 'd2_event_square')
    $ set_zone('boat_station', 'd2_event_boat_station')

    $ d2_necessary_done = 0
    jump d2_morning_map
    
label d2_morning_map:
    if d2_necessary_done != 5:
        $ show_map() 
    else:
        jump d2_decisions

label d2_event_mus_club:

    $ reset_chibi("music_club")
    play music music_list["so_good_to_be_careless"] fadein 2
    scene bg ext_musclub_day 
    with dissolve
    window show
    "Музыкальный клуб располагался на краю основной территории лагеря, отдельно от зданий кружков и чуть вдалеке — там, где начинался лес."
    "Деревья старательно укрывали дом от палящего солнца в тени, а покатая крыша и вовсе создавала приятный полумрак на открытой веранде."
    "Единственное освещённое окно было зашторено, и я не смог сразу увидеть, что меня там ожидает."
    "Изнутри не доносилось ни единого звука."
    "Но я здесь был не один. Алиса околачивалась на веранде, заглядывая в ближайшее к двери окно."
    show dv normal pioneer2 far at center with dissolve
    $ d2_met_dv = True
    th "Смотрит так, будто в первый раз видит."
    "Я поднялся к ней неслышным шагом."
    show dv normal pioneer2 close at center with dissolve
    me "Что делаешь?"
    show dv scared pioneer2 close at center with dspr
    dv "А-а!"
    "Она даже подпрыгнула на месте."
    show dv angry pioneer2 close at center with dspr
    dv "Тьфу, Семён! Больше не подкрадывайся ко мне так."
    "Она облегчённо выдохнула, положив руку на грудь."
    show dv angry pioneer2 at center with dissolve
    "На мой вопрос она не ответила и сразу убежала к лесу, перемахнув через периллу."
    hide dv with dissolve
    "Девочка скрылась среди зарослей кустов и деревьев, а прямо под окном клуба лежала помятая пачка сигарет знакомой мне марки."
    th "Это же «Родопи»!"
    "Я аккуратно подобрал их и сложил в карман — пригодятся. Цой, который, наверное, в этом мире может быть ещё жив, был прав про пачку сигарет — всё не так уж плохо на сегодняшний день!"
    "Интересно, не ищет ли она сейчас пропавшие сигареты?"
    menu:
        "Меня ждёт обходной лист":
            th "Выяснять некогда, я пришёл сюда по делу. Чем быстрей соберу эти подписи, тем лучше."
            pass
        "Пойти за Алисой" if (sp_crg >= 1):
            stop music fadeout 1
            scene bg ext_path_day
            with dissolve
            play music music_list["went_fishing_caught_a_girl"] fadein 1
            if d1_tricked: 
                "Кроме того, эта девчонка сейчас ответит за вчерашний холодный (и мокрый!) приём."
            if d1_runaway:
                "Жаль, сейчас под рукой нет спичек, но может мне удастся договориться с Алисой?"
            "Я двинулся в том направлении, куда убежала девчонка."
            scene bg ext_path2_day with dissolve
            "Нашёл я её почти сразу."
            show dv angry pioneer2 at center with dissolve
            "Алиса, опустив голову, рассматривала лесную траву у себя под ногами, шаря взглядом по земле. Пару раз обойдя поляну, Двачевская задумалась."
            show dv sad pioneer2 at center with dspr
            "Со стороны это дьявольски романтично: одинокая печальная пионерка с поникшей головой на фоне грустной плакучей ивы, будто бы ждет своего пионера. Правда, ирония в том, что романтичная пионерка ищет потерянные сигареты, которые уже лежат в рубашке у не-совсем-настоящего-пионера."
            "И Алиса явно догадывалась, что сигареты пропали не когда она убегала, а раньше."
            "Эх, и как же к ней обратиться? Давненько я не заговаривал с девчонками первым! Ну, была не была!"
            me "Хэллоу, Дваче... вская!"
            show dv angry pioneer2 at center with dspr
            "Алиса с неодобрением посмотрела в мою сторону."
            dv "Здор{i}о{/i}во. Ты чё за мной ходишь? Дел больше нет?"
            me "Дело есть. Правда не уверен, к тебе ли..."
            th "Смотрю на её лицо, но со своими никудышными знаниями мимики не понимаю, чего от неё можно ожидать дальше."
            dv "Не уверен — проваливай!"
            me "Но это же общие кусты! Общая территория для всех пионеров."
            dv "Сейчас эта поляна и кусты мои. Я, может, тут по делу, а ты здесь трёшься."
            me "А, у тебя делишки в кустиках? Тогда прошу прощения, пардон..."
            show dv grin pioneer2 at center with dspr
            "Алиса слабо улыбнулась, в глазах её читался упрёк." 
            dv "Ой дурак ты, Сеня!"
            th "Когда это я стал просто Сеней для неё?"
            me "Ну, сама посмотри: ты одна, в лесу, с дороги не видно..."
            show dv rage pioneer2 at center with dspr
            dv "Ща фингал поставлю, чтоб дорогу было виднее."
            me "Ладно-ладно, Двачевская, успокойся, покури..."
            show dv angry pioneer2 at center with dissolve
            $ renpy.pause(0.5)
            show dv surprise pioneer2 at center with dissolve
            $ renpy.pause(0.5)
            show dv normal pioneer2 at center with dspr
            "На лице Алисы последовательно проявилось сразу несколько противоречивых эмоций."
            if d1_dv_evening:
                dv "А у тебя есть сигареты?"
            else:
                dv "Так-так... Семён, а ты куришь что ли? Есть сигареты?"
            me "Ога, импортные. С фильтром. Да, кстати, они мне тут с неба упали, правда здорово?"
            if d1_un_evening:
                "Мне вдруг стало интересно, была ли эта пачка единственной у неё? И вообще, курит ли она сама? Разумеется, если её так сильно волнует пропажа сигарет."
            dv "Сеня, ты ведь знаешь, что не твоё, отдай по-хорошему!"
            me "Но ведь всяко же и не твоё?"
            th "Что упало, то пропало."
            show dv angry pioneer2 at center with dspr
            dv "Знаешь, это уже не твои заботы!"
            if d1_un_evening:
                "Алиса выглядела рассерженной. А внутри меня боролись подросток, срочно требующий запретного плода, и порядочный гражданин, ругающий детей за пристрастие к куреву. Надо же было как-то проучить её за розыгрыш?"
            if d1_dv_evening:
                "Алиса выглядела рассерженной. Надо же было как-то проучить её за розыгрыш?"
            if d1_runaway:
                th "Что выгодного для себя можно выторговать за сигареты?"
                "В голову не приходило ничего дельного, кроме того как подколоть Алису. К тому же, её встреча новичка в лагере мне совсем не понравилась."
            me "Элис, половину мне, половину — тебе. Согласна?"
            show dv guilty pioneer2 at center with dspr
            dv "Семён, я их еле достала! У директора! Ты понимаешь, как это было сложно?"
            if d1_dv_evening:
                dv "Причём они из моей заначки, чтобы не просить ни у кого." 
            "Двачевская совсем погрустнела."
            me "Ну пофиг, давай так: пятнадцать — тебе, пять — мне. И я буду звать тебя Дваче до конца смены."
            show dv rage pioneer2 at center with dspr
            dv "Ах ты засранец!"
            stop music fadeout 0
            play music music_list["pile"] fadein 0
            with vpunch
            show dv rage pioneer2 close at center with dspr
            "Алиса тигрицей прыгнула на меня, и мы покатились по траве. Ее цель — помятая пачка — лежала в нагрудном кармане моей рубашки, и перед этой девчонкой я так просто сдаваться не хотел, ощутив внезапный и совершенно ранее незнакомый мне азарт."
            with vpunch
            "Двачевская лупила меня руками и ногами, во мне же неожиданно проснулся боец: парируя весьма неженские удары Алисы, я умудрился опрокинуть девчонку и прижал её к земле всем телом, руками и ногами, пока она не обессилела."
            show dv angry pioneer2 close at center with dspr
            "Секунд десять я держался, глядя в её глаза и пытаясь понять, притворяется ли она, или в самом деле сдалась. Её лицо покраснело, а глаза горели то ли злостью, то ли таким же азартом, и губы тоже... Блин, что за чёрт, у неё такие невероятно красивые гу.."
            show dv rage pioneer2 close at center with dspr
            with vpunch
            "И тут я получил коленом в пах."
            hide dv with dissolve
            stop music fadeout 4
            "..."
            $ renpy.pause(2)
            play music music_list["you_won_t_let_me_down"] fadein 3
            "Едва ко мне вернулась способность дышать, как я постарался высказаться по поводу Алисиного поступка, совершенно не стесняясь в выражениях. Мне даже показалось, что во время моего пламенного спича с ивы упали несколько листьев, а Алиса покраснела уже второй раз."
            show dv guilty pioneer2 at center with dissolve
            dv "Семён! Ну я же не специально, просто ты задумался, я не удержалась, чтобы не... Сильно болит?"
            "После Алисиного фаталити низ живота адски ныл. Я попытался подняться на ноги, но получилось не ахти, и я поковылял, скрюченный, аки Баба-Яга с последней стадией ревматизма."
            show dv normal pioneer2 close at cleft with dspr
            "Алиса, тем не менее, попыталась взять меня под руку. Я уже боялся её, честно! — и, ожидая от девочки ещё каких-нибудь сюрпризов, руку отдернул."
            me "Знаешь, я и сам дойду."
            dv "И куда ты такой пойдёшь? К Шляпе в домик? Ох она обрадуется."
            me "Ну тогда пока полежу на скамеечке, если там никого нет."
            show dv smile pioneer2 close at center with dspr
            dv "Ну тогда держи руку, инвалид!"
            scene bg ext_path_day with dissolve
            show dv normal pioneer2 close at cleft with dissolve
            "Мы поковыляли по направлению к аллее."
            me "А у тебя отличный удар. Я еле уворачивался!"
            show dv grin pioneer2 close at cleft with dspr
            dv "Ха, в школе накачала!"
            if d1_dv_evening:
                dv "А ты отлично ругаешься, кстати, ещё вчера хотела сказать."
            else:
                dv "А ты отлично ругаешься, кстати."
            me "Прости, это было не для твоих ушей."
            show dv laugh pioneer2 close at cleft with dspr
            dv "Да ничего, у нас иногда на трудах и не такое услышишь..."
            me "Я думал, на трудах девчонки шьют, готовят..."
            show dv smile pioneer2 close at cleft with dspr
            me "Они при этом покрывают друг друга матюками?"
            dv "Ха, дурной! Это когда мы таскаем парты, столы и прочую дрянь."
            if d1_us_chase:
                me "А что, парней нет?"
                show dv normal pioneer2 close at cleft with dspr
                dv "Нет, просто..." 
                me "Это что за школа такая? Школа злословия для девочек?"
            else:
                me "Ты ведь из интерната? Что там с парнями, если девочки мебель таскают?"
            show dv angry pioneer2 close at cleft with dspr
            "Алиса внезапно перестала улыбаться, и её лицо стало обычно-строгим."
            if d1_us_chase:
                dv "Ты что-то расшутился, инвалид."
            else:
                dv "Слишком много вопросов задаёшь, инвалид."
            me "Да я уже выздоровел почти."
            scene bg ext_musclub_day
            with dissolve
            "Мы подошли к музыкальному клубу."
            show dv normal pioneer2 close at center with dissolve
            dv "Ну вот и отлично. Дальше — без меня."
            "Она по-хозяйски забрала пачку сигарет из кармана моих шорт."
            me "Э-э! Ты чего?"
            dv "Обойдёшься без них."
            "И Алиса оставила меня на скамейке в одиночестве и недоумении..."
            hide dv with dissolve
            stop music fadeout 3
            $ d2_dv_fight = True
            "..."
            play music music_list["so_good_to_be_careless"] fadein 1
            th "И что я опять не так сказал? Вечно с девчонками так происходит! Блин, почему же она обиделась?" 
            th "Хм... И почему меня это волнует? Я вижу её едва ли не третий раз в жизни, она мне пнула в яйца, сама же обиделась и ушла. Но тем не менее, мне почему-то не всё равно, как могло бы быть раньше. Что со мной происходит?"
            "Лучше бы мне и дальше не приходилось задумываться о чём-то напрягяющем."
            "Я растянулся лавочке, дожидаясь, когда боль пройдёт."
            if med_exam:
                "Обходной лист, скрученный трубкой в кармане шорт, оказался серьёзно помятым."
            else:
                "Обходной лист и медицинская справка, скрученные трубкой в кармане шорт, оказались серьёзно помятыми."
            "Выглядело соответствующе моему отношению к поручению вожатой."
            th "Блин. Ничего, как-нибудь попытаюсь разгладить."
            "Кряхтя, я поднялся со скамейки. Наконец, я смог идти без поддержки и вернулся на веранду музыкального клуба."
    stop music fadeout 1
    th "Надо постучаться."
    play sound sfx_knock_door2
    $ renpy.pause(1)
    "Никто не отозвался."
    play sound sfx_knock_door2
    "На всякий случай я ещё раз легонько постучал и толкнул дверь. Она оказалась не заперта и легко отворилась."
    play sound sfx_open_door_2
    $ renpy.pause(1)
    scene bg int_musclub_day
    with dissolve
    play music music_list["get_to_know_me_better"] fadein 3
    play ambience ambience_music_club_day fadein 1
    "Сначала мне показалось, что никого нет."
    "Внутри клуб оказался довольно маленьким, но уютным."
    "Он весь был заставлен разными инструментами."
    "Здесь даже стоял рояль!"
    th "Ух ты!"
    th "Жаль, что я не умею на нём играть."
    "Я уже хотел уходить, как наткнулся глазами на..."
    scene cg d2_miku_piano2 with dspr
    "Клуб вовсе не был пустым. Здесь была девочка!"
    "Она полностью скрылась под роялем, а снаружи оставались только её ноги в чёрных туфлях и чулках."
    th "Хм!"
    "Я не сразу заметил её из-за барабана, стоявшего у рояля."
    "Пройдя в помещение, я с интересом поглядел, что же она делала на полу."
    if d1_un_evening:
        th "Да это ведь Мику! Должно быть, она подскажет, у кого надо взять подпись о посещении кружка."
    "Выгнувшись всем телом, девочка тянулась рукой к губной гармошке, только вот никак не могла её достать. Было ясно, что девочка поленилась обойти этот громоздкий музыкальный инструмент."
    "Гармошка упорно не хотела идти к ней в руки, и пионерка, стараясь дотянуться до неё, всё дальше лезла под рояль, пока не опустилась целиком."
    "Её ноги, длинные и стройные, слегка покачивались, а короткая юбка задралась так, что я мог видеть..."
    play sound sfx_brass_drop
    "Я задел рукой пюпитр, и он с грохотом упал."
    scene cg d2_miku_piano with dspr
    mi "Ой!"
    th "В полосочку!"
    "Теперь она смотрела на меня, а я смутился того, что стоял и пялился на неё, пока она была на коленках под роялем."
    me "Извини, я не хотел..."
    scene bg int_musclub_day
    with dissolve
    "Она начала выбираться, а я поднял железную конструкцию, забыв о нотной тетради, которая слетела с неё и осталась на полу."
    me "Вроде бы не сломал эту штуковину."
    show mi laugh pioneer at center with dissolve
    mi "Да ничего, его постоянно роняют."
    show mi smile pioneer at center with dspr
    "Я чуть было не спросил, не постоянно ли она сидит под роялем."
    me "А меня вот с бегунком послали... знакомиться с лагерем."
    "Я был смущён и не знал, что сказать."
    if (d1_un_evening == False):
        "Но незнакомая девочка словно ничего не заметила."
    show mi happy pioneer at center with dspr
    "Она поставила пюпитр в сторону и нагнулась за нотной тетрадкой."
    "И я ещё раз увидел..."
    th "Ух!"
    "Она положила тетрадь на подставку и переставила железный пюпитр на то же место.{w=0.3} Ох, его же наверняка опять уроня{font=fonts/DejaVuSansMono.ttf}~{/font}т!"
    if d1_un_evening:
        "Я всё ещё считал себя виноватым за нечаянное подглядывание и за устроенный шум."
        show mi normal pioneer at center with dspr
        "Мику повернулась ко мне."
        mi "Привет, Семён!"
        show mi smile pioneer at center with dspr
        me "Привет."
    else:
        show mi normal pioneer at center with dspr
        "Девочка повернулась ко мне."
        mi "Привет. Меня Мику зовут."
        $ mi_name = u"Мику"
        me "Мику?"
        mi "Угу."
        show mi upset pioneer at center with dspr
        "Она слегка насупилась, впрочем, ненадолго."
        mi "Никто почему-то не верит, а это моё настоящее имя!"
        mi "У меня мама из Японии. А папа — русский инженер!"
        show mi serious pioneer at center with dspr
        "Она произнесла это с таким чувством, что я невольно улыбнулся..."
        "Я всё ещё считал себя виноватым за нечаянное подглядывание и за то, что переспросил имя."
        "Но Мику это, казалось, больше не заботило."
        mi "А это мой музыкальный клуб."
        show mi smile pioneer at center with dspr
        "Она с гордостью обвела маленькую каморку глазами и улыбнулась. Трудно было сказать, что в лагере много желающих заниматься музыкой. Пока что передо мной из всех была только вот эта девочка."
        "Я наконец собрался с мыслями."
        me "А меня Семён зовут."
    "Она кивнула, так, что её красивые струящиеся хвосты взметнулись во все стороны, и только тогда заметила у меня в руках листок."
    show mi smile pioneer at center with dspr
    mi "Так что ты говоришь? С бегунком послали?"
    me "А кто должен подпись поставить?"
    show mi serious pioneer at center with dspr
    "Она взяла у меня лист и сразу же засуетилась."
    mi "Я, потому что отвечаю за кружок. Сейчас подпишу."
    "Она что-то искала по комнате."
    show mi smile pioneer at center with dspr
    mi "Ты проходи, садись! Вот тут."
    "Я присел на стул у открытого окна."
    mi "Подожди немного, я сейчас."
    show mi happy pioneer at center with dspr
    "Мику повертела головой, снова что-то выискивая, а потом нагнулась... видимо, за ручкой..."
    th "Снова эти гипнотизирующие полосы девичьих трусиков!"
    show mi normal pioneer at center with dspr
    "Не замечая моего смущения, Мику продолжала весело болтать. Девочка встала у окна, чтобы расписаться в обходном листке на подоконнике."
    mi "Я почти всё время здесь. Можешь заходить... Даже если не запишешься в кружок. А если запишешься..."
    show mi smile pioneer at center with dspr
    "Она посмотрела на меня."
    mi "В любом случае, мы всегда будем рады!" 
    show mi serious pioneer at center with dspr
    mi "Другие участники кружка сюда нечасто заходят, им больше на улицу хочется. Конечно, есть два мальчика, хорошо играющих на инструментах, но и они гуляют. Им интересней проводить время на пляже или где-нибудь ещё..."
    show mi upset pioneer at center with dspr
    mi "Представляешь, одна девчонка мне даже сказала, что ноты скучные! А ведь вожатые потом будут спрашивать у ребят, выполнены ли нормативы кружка за смену? Будут и меня винить, как недостойного руководителя клуба. Зачем было записываться?"
    mi "Жаль, что с ребятами ничего не поделать, а выгораживать — это нехорошо! Даже не знаю, как с ними быть."
    "Она снова надула губки бантиком, но тут же улыбнулась и протянула мне подписанную бумажку."
    show mi smile pioneer at center with dspr
    "Я поднялся."
    th "Как-то у неё всё сложно. Если запишусь, придётся тоже отдуваться за всех, но тогда Мику хотя бы не будет одна."
    th "И клуб не кажется особенно пустым — Мику чересчур общительная, заменит нескольких человек, это точно."
    th "Остаётся решить, надо оно мне или нет."
    me "Спасибо."
    "Уходить не хотелось, я всё ещё размышлял о записи, но нужно было отвязаться от этого глупого обходного листа."
    th "О чём же я ещё хотел сказать напоследок?{w} А!{w} Сработает или нет?"
    me "Мику, а что ты искала под роялем?"
    show mi surprise pioneer at center with dspr
    mi "Гармошку! Спасибо, я совсем забыла о ней!"
    scene cg d2_miku_piano2
    with dissolve
    "И девочка снова опустилась на пол под рояль, в который раз пытаясь дотянуться до упавшего музыкального инструмента. Юбка задралась, и сейчас мне уже больше ничего не нужно было."
    th "О, наивное создание!"
    "Белая полоска, зелёная полоска, белая полоска, зелёная, складки и натянутая ткань, манящий просвет белой кожи между подолом юбки и чулочками..."
    me "Обязательно ещё зайду!"
    scene cg d2_miku_piano with dspr
    mi "Ага, хорошо! Достала-таки гармошку!"
    me "Поздравляю!"
    "Я был рад и за неё, и за всё увиденное. Полностью избавившись от чувства, что виновен в подглядывании, я выскочил из клуба."
    stop ambience fadeout 2
    play sound sfx_close_door_1
    $ d2_necessary_done += 1
    window hide
    scene bg ext_musclub_day
    with dissolve
    $ renpy.pause(1)
    window show
    "Лагерь определенно начинал мне нравиться. Здесь было весело и хорошо, не так, как..."
    "В голове прозвучал неприятный голос."
    th "Как где?"
    "Но я отогнал его прочь."
    th "Как раньше! И такого больше уже не будет!"
    "И тот же голос переспросил."
    th "Не будет? Жаль, если..."
    "Но на этот раз я его просто проигнорировал."
    "На самом деле, в том и загвоздка. В жизни у меня никогда не было таких перемен, и поэтому сейчас мне стало намного лучше.{w} \nА всё хорошее имеет свойство заканчиваться."
    "Я шёл по дорожке, раздумывая, записаться ли мне в музыкальный кружок..."
    th "Интересно, почему Алиса заглядывала в окно клуба?"
    "Впрочем, неважно. Я очень сильно надеялся, что Алиса не окажется там, куда я запишусь."
    if (d2_dv_fight == False):
        th "А вот сигареты надо бы припрятать, нехорошо шататься везде с ними в кармане."
        "По прямой от музыкального клуба я вышел к берегу реки, выбрал один куст с запоминающимся для меня местоположением и укрыл пачку в траве под листьями."
        "Теперь, когда душа спокойна, можно и продолжить обход лагеря с бегунком."
    stop music fadeout 1
    $ disable_current_zone()
    window hide
    jump d2_morning_map
    
label d2_event_clubs:
    
    $ reset_chibi("clubs")
    if been_there()>1:
        scene bg ext_clubs_day
        "Нет, хватит! Я и так уже задержался тут надолго!"
        $ disable_current_zone()
        jump d2_morning_map
    
    scene bg ext_clubs_day
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 2
    window show
    "Здания клубов, к которым я вышел..."
    th "Это же первое, что я увидел вчера за воротами лагеря!"
    th "Сначала я остановился тут, а потом появились Лена с Ульяной."
    "Так что рассмотреть корпуса удалось только сейчас."
    "Оба одноэтажных дома были длинными, но не очень широкими. Старенькие и обшарпанные, краска на стенах местами облупилась."
    if d1_genda_flag:
        th "Казалось бы, лагерь построен буквально несколько лет назад!"
    "Ближе к торцам домов висели приколоченные жестяные указатели с номерами: «Корпус 1» и «Корпус 2» соответственно."
    "Ещё издали можно было разглядеть сбоку от дверей небольшую табличку с надписью «Клубы» у первого корпуса."
    "Двери выглядели надежно, а рядом висел снятый замок, которым запросто можно было закрывать амбар — таким он был большим."
    "Хотя, судя по количеству труб, проводов и электрических кабелей, которые к нему тянулись, можно было предположить, что внутри находилась атомная электростанция."
    "Не меньше."
    "Я шагнул вперёд."
    th "Сначала обойдём первый корпус."
    "На той же табличке было расписание занятий в кружках:"
    window hide
    $ set_mode_nvl()
    window show
    "- Шашки, шахматы (клуб настольных игр)"
    "- Клуб юного техника"
    "- Клуб юного моделиста"
    "- Клуб юного натуралиста"
    window hide
    $ set_mode_adv()
    window show
    "Каждая строчка завершалась временными промежутками, в которые эти кружки работали, но я не стал вчитываться, потому что поверх всех надписей мелом большими буквами было выведено: {b}«ЗАНЯТО!»{/b}"
    "Это меня слегка заинтересовало."
    th "Может, и заходить туда нельзя?"
    "В обходном листе «Клуб юного техника и моделиста» значился первым."
    th "Ну что же, вперёд, раз надо знакомиться с лагерем."
    "Я зашёл внутрь и оказался в пустом коридорчике, куда свет проникал только через окна, обнажая немереное количество пыли, витавшей здесь."
    "Стены здесь тоже были не в самом лучшем состоянии, как и снаружи, отчего я почувствовал себя немного неуютно."
    stop music fadeout 2
    "Первая же дверь, попавшаяся мне на глаза, вела именно в «Клуб юного техника» — так было написано на табличке под притолокой, как у врачебного кабинета."
    play music music_list["i_want_to_play"] fadein 1
    "..."
    "Внутри кто-то разговаривал. Я остановился и прислушался."
    "Кажется, разговаривали двое, и оба голоса были очень знакомыми..."
    th "Точно! Это же Шурик и Сыроежкин. И они как раз приглашали меня к себе после завтрака."
    "Я уже хотел открыть дверь, как внутри закричали."
    el "А-а!!! Больно."
    play sound sfx_knock_door_closed_hard1
    "Я толкнул дверь, но та даже не сдвинулась с места."
    "В это время послышался другой голос, очевидно, принадлежащий Шурику."
    sh "А ты терпи! Потом легче будет..."
    "Я вздрогнул и повременил открывать дверь."
    "Голос спокойный и уверенный, даже серьезный... и слегка запыхавшийся."
    "Электроник пытался оправдаться."
    el "Больно же..."
    "Но Шурик его не слушал."
    sh "В первый раз всегда так."
    "Это меня насторожило. И они будто заперли помещение."
    "Здесь явно было что-то...{w} что-то странное."
    "Я прислонил ухо к двери, чтобы лучше слышать."
    "В это время Электроник снова заговорил."
    el "Давай по-другому."
    el "Лучше я сверху!"
    "Шурику это не слишком понравилось."
    sh "Как хочешь. Только давай быстрее."
    play sound sfx_table_move_outside
    "Внутри раздался звук, словно кто-то подвинул стол."
    sh "Ну!"
    "Голос его стал нетерпеливее."
    el "А-а-ай!"
    sh "Да не держи ты его так, как будто это что-то плохое!"
    "Снова возникла какая-то возня."
    sh "Не туда! Ниже!"
    "Теперь шум из клуба только возрастал."
    sh "Крепче держи! Чего ты боишься? Не отвалится."
    "Как будто внутри что-то билось..."
    sh "Вот так!"
    "Голос Шурика стал довольным."
    sh "А теперь встань на колени... только держи его, не отпускай."
    "Кажется, волосы у меня на голове зашевелились. Я не знал, что мне делать."
    "Это было..."
    sh "Вот. Хорошо!"
    "Я начал медленно отодвигаться от двери."
    sh "Ещё немного! Ну!{w} ВОШЁЛ!"
    "Я был в ужасе. А внутри явно ликовали."
    sh "Получилось!"
    sh "Видишь — ничего страшного. Всё легко."
    sh "И больно бы не было, если бы ты только не поторопился."
    "Я БЫЛ В УЖАСЕ!"
    "Фактически, я уже поворачивался, чтобы бежать отсюда."
    "Куда угодно, но лишь бы подальше от этого оплота содо..."
    "Как мне на плечо опустилась рука."
    th "Б-же, за что мне это?"
    "Я повернулся, ожидая увидеть всё что угодно..."
    "Физрука-извращенца, который утянет меня за собой. Пришельца-гомопедофила..."
    show sl normal pioneer at center with dissolve
    "Но это была Славя."
    sl "Привет."
    show sl smile pioneer at center  with dspr
    "Я только и смог кивнуть в ответ."
    "А Славя улыбалась."
    show sl smile2 pioneer at center  with dspr
    sl "Ты их не слушай, клубы общие, сюда каждый может приходить."
    th "А, видимо это Сыроежкин написал мелом ту надпись."
    show sl surprise pioneer at center  with dspr
    "Только сейчас Славя заметила, что я какой-то нервный."
    sl "А они тебя не пустили, да?"
    show sl serious pioneer at center  with dspr
    sl "Пойдем, я сейчас там наведу порядок."
    "И взяв мою руку, она решительно потянула дверь."
    th "Сейчас она войдёт и увидит..."
    "Мне нужно было во что бы то ни стало не допустить этого, не дать Славе осквернить свои красивые и добрые глаза цвета лазури!"
    "Но испуг сделал своё дело, и я не мог ничего произнести."
    play sound sfx_open_door_clubs
    "Славя легко открыла дверь."
    th "Она же открывается в другую сторону!"
    stop music fadeout 3
    scene black with fade
    "Я закрыл глаза."
    th "Поздно спохватился."
    play music music_list["eat_some_trouble"] fadein 2
    play ambience ambience_clubs_inside_day fadein 1
    sl "Опять вы за своё?"
    th "Хм..."
    "Голос Слави не был встревоженным, в нём не было ненависти и даже намёка на удивление. "
    th "Странно..."
    sl "Сколько раз повторять, что кружки — не ваша собственность."
    sl "Занимайтесь, но не мешайте другим."
    "Немного успокоившись от такого начала, но морально подготовив себя к самому страшному, я приоткрыл глаза."
    scene bg int_clubs_male_day
    with dissolve
    show sl serious pioneer at left with dissolve
    show el sad pioneer at cright with dissolve
    show sh rage pioneer at fright with dissolve
    "Электроник и Шурик стояли, поникнув головой...{w} Они были одеты."
    "Я облегченно вздохнул."
    "А ещё Сыроежкин держал паяльник."
    "Шурик, яростно жестикулируя, пытался что-то доказать Славе."
    sh "У нас тут важное дело!"
    "Я заметил на столе что-то объёмное под большим покрывалом." 
    sh "Нам совсем немного осталось, а вы только как всегда мешаете!"
    sh "Уходите немедленно!{w} Хотя погодите, Семён, ты-то останься."
    "Но на Славю это, казалось, не произвело никакого впечатления."
    show sl angry pioneer at left with dspr
    sl "Не будете уважать других людей, закрою все инструменты от вас."
    "В ответ на эту угрозу Шурик попытался высказать всё, что думает по этому поводу."
    "На лице было написано презрение к обывателям, прервавшим важнейший научный эксперимент."
    "Он уже поднял руку, чтобы взмахнуть ей в ознаменование начала своей пламенной речи в защиту науки, но Славя не дала ему вставить ни слова."
    sl "Запрещу совсем ваш кружок — тогда будете знать! Пионеры так себя не ведут."
    show sh upset pioneer at fright with dspr
    "После этого пионер махнул рукой и уже не пытался перебить Славю."
    th "А она здесь пользуется авторитетом..."
    sl "Придумали — выгонять людей из клуба!"
    sl "Клубы общие!"
    sl "И каждый может вступить!"
    show sl normal pioneer at left with dspr
    "И тут же она смягчилась, вспомнив обо мне."
    sl "Семён, знаком уже с Сашей, как я погляжу? Он здесь ведёт кружок юного техника."
    show sh normal pioneer at fright with dspr
    sl "Не смотри, что такой важный, он совершенно безобидный."
    me "Ничего, общий язык найдём."
    show sl smile pioneer at left with dspr
    sl "Кстати, Семён, приходи отметиться в кружок юннатов, как выйдешь в коридор, поворачивай за угол и прямо — наш кабинет там."
    show el serious pioneer at cright with dspr
    el "Вот не надо так нагло переманивать к себе новенького!"
    show sl angry pioneer at left with dspr
    show el sad pioneer at cright with dspr
    "Но она так на него посмотрела, что Электроник только виновато вжал плечи. Славя всё ещё немного сердилась, но потом сразу же засобиралась."
    show sl smile2 pioneer at left with dspr
    sl "Ну, раз всё в порядке, то я пойду."
    "Она уже снова стала той улыбающейся Славей, какой я увидел её впервые."
    "Но она всё же погрозила на прощанье Шурику пальцем."
    show sh surprise pioneer at fright with dspr
    sl "И больше не забывайте, что клубы общие!"
    "А я хотел её остановить, сказать что-то благодарное — ведь она опять выручила меня. Из-за своей разбушевавшейся фантазии я мог натворить каких угодно глупостей."
    show sh normal pioneer at fright with dspr
    hide sl with dissolve
    show el normal pioneer at cleft with dspr
    show sh normal pioneer at cright with dspr
    "Электроник, стоявший до этого удивительно тихо, кивнул мне и сказал, словно извиняясь за что-то."
    el "Мы тут проект доделываем, поэтому лучше, если  сюда никто не будет заходить, пока мы не закончим."
    "Шурик закрыл за девочкой дверь, и, видимо, решив сменить тему, обратился ко мне."
    sh "Хочешь в наш кружок? Ты ведь записываться пришёл?"
    "Но только я собрался отвечать, как меня опередил Электроник, только что сдёрнувший покрывало со стола, явив на свет нечто похожее на робота без рук и ступней."
    show el laugh pioneer at cleft with dspr
    el "Да какие вопросы! Конечно, записывай его, он нам пригодится."
    me "Я не записываться, а только сделать отметку в обходном листе. Так-то я ещё подумаю, вступать в кружок или нет."
    show el normal pioneer at cleft with dspr
    show sh upset pioneer at cright with dspr
    th "А то уже успели потрепать нервы этим эпизодом."
    hide el with dissolve
    show sh normal pioneer at center with dissolve
    sh "Ладно... Давай сюда бумажку, подпишу." 
    "В его голосе послышалось недовольство. Он явно ожидал другого ответа."
    show sh normal_smile pioneer at center with dspr
    sh "И, кстати, мы не «Клуб юного техника», а «Кружок кибернетиков»."
    hide sh with dissolve
    th "Будто название что-то меняет."
    "Мы находились в светлой комнате, явно предназначавшемся для моделистов и любителей радиоэлектроники. Под самым потолком были подвешены законченные модели самолётов, на противоположной стене висели инструменты и недостроенный фюзеляж. Под ними же были два стола: верстальный с тисками и компьютерный."
    th "Компьютер! Неужели..."
    show el smile pioneer at cleft with dissolve
    "Но не успел я что либо спросить о компьютере, как Электроник схватил меня за руку и потащил показывать своего робота. Хотя тащить было всего два шага — мы сразу остановились."
    el "Во!"
    "Железная человекоподобная махина лежала распластанной на столе в центре комнаты, вокруг робота валялась уйма мелких деталей из металла, всяческих батареек, инструментов и проводков. На самый край столешницы был смещён весь посторонний мусор, коробки и старый магнитофон."
    "Творческий беспорядок, одним словом."
    "Сам робот походил очертаниями на женскую фигуру с кошачьими ушками на голове. Корпус этого андроида был частично разобран, и я смог разглядеть большую часть технической начинки в нём."
    me "И это тот самый проект, о котором вы молчали?"
    el "Именно."
    "Сыроежкин сложил паяльник с проводом на стол."
    me "С чего бы мне оказана честь узнать о том, что вы делаете?"
    show sh normal pioneer at cright with dissolve
    sh "Ты сам сказал, что разбираешься в компьютерной технике. Держи."
    "Он вернул мне лист-бегунок."
    me "Но я имел в виду обычные персональные компьютеры, как этот."
    "Я кивнул в сторону большого монитора с клавиатурой на столе у окна."
    "Присмотревшись к компьютеру получше, я с сожалением понял, что на нём в современные игры скорее всего не поиграть, и, если верить Ольге Дмитриевне, доступа к Интернету у пионеров не было."
    "Впрочем, старые игры тоже здорово увлекают, и я мог бы зависнуть тут надолго."
    show el laugh pioneer at cleft with dspr
    el "Ничего, мы тебя быстро подтянем, будешь и с этой техникой на «ты». Потом, две головы хорошо — а три лучше.{w} Понимаешь, мы вдвоём можем и не успеть сделать робота ко Дню творческой самодеятельности."
    show sh smile pioneer at cright with dspr
    sh "Да, поэтому всю прошлую неделю мы едва ли не сутками работали над ним."
    show el smile pioneer at cleft with dspr
    me "А что такого в роботе, чем он пригодится?"
    show sh serious pioneer at cright with dspr
    sh "Сделаем что-то более выдающееся, чем просто модели самолётов."
    show el serious pioneer at cleft with dspr
    el "Ну, кроме того, что выступим... Так, давай не будем сейчас об этом, хорошо?"
    th "Темнит. Но если я вступлю в клуб, то рано или поздно узнаю, что задумал Сыролежкин."
    show el normal pioneer at cleft with dspr
    me "Хотите сказать, робот будет выполнять какие-то трюки на публику? Типа открывать банку колы и наливать в стакан?"
    show sh normal_smile pioneer at cright with dspr
    "Шурик усмехнулся, поправляя очки, ещё больше напоминая мне сумрачного гения."
    sh "И не только...{w} Она будет ходить, танцевать, отвечать на вопросы пионеров..."
    me "...Печь тосты, варить пиво, показывать ТВ, качать торренты, летать и стрелять лазером из глаз?"
    show el grin pioneer at cleft with dspr
    el "Лазер ей не нужен, она сможет постоять за себя, а реактивный ранец я не привёз в лагерь, извини. Всё остальное реально сделать."
    me "Оу."
    th "Не многовато ли планов на две недели? Это же звучит невероятно, фантастически! В моём мире на подобное у людей уходят месяцы, если не годы, а главное — уйма денег!"
    show el laugh pioneer at cleft with dspr
    el "А главное, она будет выглядеть как настоящая девушка, от живой не отличишь, я гарантирую!"
    "Глаза кибернетиков светились азартом. Парни явно были одержимы своей задумкой."
    th "Да вы уже заочно влюбились в своё творение, Пигмалионы!"
    me "Что-то верится с трудом."
    sh "А ты к нам присоединяйся, поверишь. У нас есть всё для этого."
    "Сыроежкин как бы случайно пихнул друга локтем, не дав ему сказать что-то."
    el "Я хотел построить собственного робота на каникулах, поэтому привёз в лагерь уже готовый каркас и основную технику для него. Я думал, что закончу робота к концу лета, но познакомился с Шуриком, и мы решили, что сможем достроить её раньше."
    th "Её?"
    "Я снова окинул взглядом полуразобранного андроида. Там, где должна быть человеческая грудь, действительно виднелись округлости корпуса."
    "Планы казалась настолько же впечатляющими, насколько нереализуемыми. Я не мог взять в голову, как кибернетики собирались «научить» робота сложным вещам вроде танцев и голосовой реакции на вопросы пионеров. А человеческая внешность?.."
    "Вдруг я снова обратил внимание на кошачьи уши на макушке андроида."
    me "Что это такое? Почему уши как у животного?"
    show el smile pioneer at cleft with dspr
    el "Вот тут мы подошли к самому главному."
    sh "Это была моя идея."
    show el grin pioneer at cleft with dspr
    el "Но мы расскажем тебе, только если ты запишешься к нам."
    me "Так, всё, хватит, шантажисты! Я пошёл. Кстати, где находится кружок юного моделиста?"
    show el normal pioneer at cleft with dspr
    show sh upset pioneer at cright with dspr
    "Их положительный настрой стремительно обнулился."
    sh "Они тут, в смежной комнате."
    "Он махнул рукой, указывая на пустую стенку справа от шкафа с чертежами моделей самолётов. Шкаф и стенку разделяла узкая дверь."
    me "Мне туда?"
    show el serious pioneer at cleft with dspr
    el "Нет-нет, там кладовка! Помнишь, Славя сказала, куда идти? Там три двери, все от кружков из этого корпуса."
    me "Спасибо."
    hide el
    hide sh
    with dissolve
    "Но кибернетики не стали мне препятствовать, и я вышел в коридор."
    stop ambience fadeout 1
    stop music fadeout 1
    scene bg ext_clubs_day
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 2
    th "Фух! Кое-как освободился!"
    th "Конечно, я не смогу с закрытыми глазами собрать какого угодно робота..."
    th "Но бегунок они мне подписали!"
    "Я свернул за угол в коридоре и увидел те самые три двери. Слева — кружок юных моделистов, справа — клуб настольных игр, а прямо — кружок юннатов."
    th "С чего начать?"
    menu:
        "Клуб юного моделиста":
            jump d2_event_modelists
        "Клуб юного натуралиста":
            jump d2_event_unnats
        "Клуб настольных игр":
            jump d2_event_chess

label d2_event_modelists:

    "Я зашёл к моделистам и очутился в тесном помещении без окон. Ситуацию спасала только пара люминесцентных ламп, и то, не очень ярких, из-за чего пионеры держали включенными ещё настольные светильники, под которыми собирать что-то из мелких деталей было намного проще."
    "На двух широких столах, которые и создавали тесноту, громоздились собранные модели: на одном самолёты с кораблями, на другом — незаконченная диорама — макет старинного города."
    "Здесь занимались шесть пионеров, и, как мне показалось, без особой радости."
    th "Аскетично и мрачно..."
    if d1_dv_evening:
        show mk at center with dissolve
        "Но тут я увидел Антона, с которым провёл прошлый вечер."
        me "Привет."
        mk "Привет, Семён. Что-то нужно?"
        me "Ольга Дмитриевна заставила пройти все кружки по списку и отметиться, потому что я как бы только вчера приехал в лагерь."
        mk "А, ясно. За подписью тебе к нему."
        "Он позвал какого-то пионера в матроске, и тот взял у меня бумажку."
        mk "На самом деле этот бегунок имел смысл в начале заезда, когда по кружкам водили всех пионеров, выбирали ответственных за клубы, да и вообще, это было похоже на игру с вожатыми."
        me "Ну, кому игра, а кому пытка."
        mk "Вот-вот.{w} Ненавижу волокиту."
        km "Ой, брось, Антон! Ты вообще всё ненавидишь."
        "Тот резко поднял руку, указывая пальцем в сторону старосты, подписывавшего лист."
        mk "Заткнись."
        "Но белокурый мальчишка не испугался. Наверно, он даже еле удержался, чтобы не засмеяться."
        "Мне вернули бегунок."
        mk "Записывайся к нам, если тебе интересно моделирование."
        me "Да я этим никогда не занимался, сомневаюсь что..."
        show mk smile at center with dspr
        mk "По инструкциям всё легко, это особо талантливые товарищи у нас могут и без схем блоху подковать, вон как тот парень."
        "Названный им пионер с гордостью продемонстрировал мне миниатюрную модель винтовки длиной не больше восьми сантиметров."
        me "Здорово, но я ещё подумаю, ладно?"
        show mk at center with dspr
        "Антон пожал плечами."
        mk "Как знаешь."
        me "А Угрюмый тоже здесь? Он говорил, что ты его знакомый."
        mk "Да, знакомый. Он записан в кружок настольных игр, но иногда заходит к нам. Видишь макет старой Англии? Это почти целиком его работа."
        me "Понял. Спасибо."
        "Антон повернулся к столу, за которым он собирал небольшой биплан, а я ушёл, закрыв за собой дверь."
        hide mk with dissolve
    else:
        "К тому же, тут не было ни одного из моих знакомых пионеров."
        "Пришлось спрашивать сразу у всех."
        me "Э-э... Привет. У кого можно получить подпись за обход?"
        "Какой-то мальчик поднялся с места и весело попросил у меня бумажку."
        th "Ну хотя бы без лишних вопросов и по-быстрому."
        "Получив на руки бегунок, я ушёл."
    $ d2_visited_modellers += 1
    th "Так, что ещё?"    
    if (d2_visited_unnats == 1) and (d2_visited_modellers == 1) and (d2_visited_playing_club == 1):
        pass
    else:
        menu:
            "Клуб юного натуралиста" if (d2_visited_unnats == 0):
                jump d2_event_unnats
            "Клуб настольных игр" if (d2_visited_playing_club == 0):
                jump d2_event_chess

label d2_event_unnats:

    "Постучавшись, я зашёл к юннатам."
    "Это была небольшая, но очень светлая комната, почти всё пространство которой занимал круглый стол. За ним сидели только девочки. Заметив меня, некоторые начали перешёптываться и хихикать, словно я пришёл учиться балету, а не ставить подпись." 
    "Один единственный парень из младшего отряда кормил черепаху в аквариуме, примостившемся на комоде у окна. Слева от него тянулся стол, больше похожий на парту, тут была пара микроскопов и чьи-то раскрытые тетради с гербарием." 
    "Около двери громоздился шкаф с книжками. Повсюду на стенах, заполняя пустоту, в застеклённых рамках красовалась бабочки. В углу помещения с тихим гудением работал холодильник."
    show sl normal pioneer at center with dissolve
    "Меня сразу же встретила Славя."
    show sl surprise pioneer at center with dspr
    sl "Давай подпишу обходной, Семён. Пойдёшь к нам, или ты уже к техникам записался?"
    me "Они себя кибернетиками называют, между прочим."
    show sl smile2 pioneer at center with dspr
    "Славя улыбнулась на это."
    sl "Значит, к ним?"
    me "...Нет, я пока ещё никуда не вступил, как обойду всех, решу."
    show sl smile pioneer at center with dspr
    sl "Разумно! Смотри, к чему лежит душа, и выбирай."
    "Красивым почерком она вывела подпись в соответствующей графе бегунка и вернула его мне."
    me "Сразу в два кружка можно?"
    show sl normal pioneer at center with dspr
    sl "Ольга Дмитриевна просила нас выбрать что-то одно. Понимаешь, вожатых на всех не хватает." 
    sl "Поэтому одни пионеры были назначены старостами, а другие решали, где и с кем им будет интересней."
    me "А чем вы занимаетесь?"
    show sl happy pioneer at center with dspr
    sl "Отдыхаем и в то же время приобретаем знания. У нас познавательно-развлекательный кружок!"
    me "И всё?"
    show sl smile pioneer at center with dspr
    sl "Ты только не думай, что мы просто сидим на месте! Мы изучаем флору и фауну нашего края, проводим викторины и выходим на природу. Каждый юннат ведёт дневник с наблюдениями за природой и изучаемыми им объектами."
    "Она произнесла это так, словно была учительницей."
    "И, если честно, я бы с удовольствием поучился бы под её чутким руководством... Ну, или в своё время не отказался бы от помощи по школьным предметам, будь Славя моей одноклассницей."
    sl "Занятия в кружке будут полезны тем, кому в школе дали задание по биологии на лето."
    "Я кивнул в сторону аквариума."
    me "Живой уголок?"
    show sl surprise pioneer at center with dspr
    sl "Вроде того, но не как в школе. Мы юннаты, а не зооуголок. Других животных кроме черепахи нам держать не разрешают, потому что воспитывать их и кормить пионерам накладно. Ухаживать за питомцами постоянно не выйдет."
    me "Жалко. Мне нравятся животные."
    show sl smile2 pioneer at center with dspr
    sl "Правда? Это хорошо."
    "Особенно экзотические, я бы содержал бы дома кого-нибудь необычного. Но желания остались всего лишь желаниями, и вслух об этом я никому не говорил."
    show sl smile pioneer at center with dspr
    sl "В таком случае, тебе понравится наш кружок, присоединяйся!"
    me "Спасибо, буду иметь в виду."
    hide sl with dissolve
    "Сжимая бегунок, я вернулся в коридор."
    $ d2_visited_unnats += 1
    th "Может быть, если проводить время с приятными людьми, как Славя, тут не будет скучно."
    if (d2_visited_unnats == 1) and (d2_visited_modellers == 1) and (d2_visited_playing_club == 1):
        pass
    else:
        menu:
            "Клуб юного моделиста" if (d2_visited_modellers == 0):
                jump d2_event_modelists
            "Клуб настольных игр" if (d2_visited_playing_club == 0):
                jump d2_event_chess

label d2_event_chess:

    "От клуба настольных игр меня отделяли двойные двери, напомнившие мне о столовой, и через окошки в створах было видно такое же просторное и светлое помещение."
    "Я толкнул двери вперёд и зашёл. Некоторые пионеры отвлеклись на меня, но снова вернулись к своим делам. За столами одни играли в шахматы, другие — в шашки. У кого-то я увидел по две доски необычной формы с пластиковыми корабликами — эти ребята играли в морской бой."
    "В комнате изредка был слышен стук фигур и шашек, игроки, если и говорили, то негромко, и мне было неловко нарушать идиллическую атмосферу."
    "Поэтому я подошёл с бегунком к невысокому пионеру, искавшему что-то в шкафу, где хранили настольные игры."
    "Кучерявый паренёк, явно из младшего отряда, признался, что это он сейчас отвечает за кружок и согласился подписать обходной лист."
    me "Сейчас? Значит, раньше был кто-то другой?"
    "Мальчуган поправил на переносице очки с толстыми линзами." 
    st_chess "Да, до меня был Угрюмый, а теперь он больше не посещает кружок со всеми. Он заходит сюда, когда никого нет."
    if d1_dv_evening:
        th "Отвечал за кружок и перестал приходить? Это похоже на него."
    "Я только собирался поинтересоваться, почему так вышло, как малой, шумно потянув носом, точно простуженный, неожиданно атаковал меня вопросом."
    st_chess "Сыграем в шахматы?"
    "Я подумал, что разок можно, всё равно записываться для этого было необязательно. Заодно вспомню, как. В последний раз я играл очень давно, и не совсем плохо." 
    th "Есть шансы на победу."
    me "Ха. Давай."
    "Пацан даже не улыбнулся."
    "...................."
    "Через пятнадцать минут я, обхватив голову руками и не понимая, что произошло, склонился над доской с прореженными рядами своих фигур, часть которых уже скопилась в кучу рядом с противником."
    "Это был полный разгром."
    th "ПОЗОР!"
    th "Я, двадцатипятилетний лоб, продул восьмикласснику!"
    th "Как, блджад?"
    th "И этот гик от мира шахмат ещё успевал суетливо записывать каждый ход в блокнотик!"
    "На поставленный мне мат в ответ рвался только мат, но я молчал, словно обухом ударили по спине."
    "Пионер великодушно поблагодарил меня за игру, и я вынужденно пожал ему потную руку."
    "Из кружка я уходил на ватных ногах и с чувством глубокой подавленности."
    th "Может быть, я проиграл, потому что мне фосфора не хватает?"
    "..."
    $ d2_visited_playing_club += 1
    "За дверями, убедив себя, что надо достойно принимать поражения (а их у меня в жизни было немало), я пробежал глазами по обходному листу, проверяя оставшиеся места для посещения."
    if (d2_visited_unnats == 1) and (d2_visited_modellers == 1) and (d2_visited_playing_club == 1):
        pass
    else:
        menu:
            "Клуб юного моделиста" if (d2_visited_modellers == 0):
                jump d2_event_modelists
            "Клуб юного натуралиста" if (d2_visited_unnats == 0):
                jump d2_event_unnats

    th "В этом корпусе со всеми кружками покончено."
    "Мне предстояло обойти ещё одно здание — то, что напротив."
    "И здесь была табличка с перечнем кружков и расписанием."
    window hide
    $ set_mode_nvl()
    window show
    "- Студия ИЗО и лепки"
    "- Кружок столярного дела (закрыт)"
    "- Кружок шитья и кройки (закрыт)"
    "- Фотолаборатория"
    window hide
    $ set_mode_adv()
    window show
    "В обходном листе действительно не было ни кружка столярного дела, ни по шитью и кройке, только секция ИЗО, а фотолаборатория была частью кружка пионерской стенгазеты, который в порядке очерёдности шёл за библиотекой."
    th "Значит, я задержусь тут ненадолго."
    "............"
    $ d2_necessary_done += 1
    "И правда, в этом корпусе я пробыл от силы две минуты."
    "В кружке рисования мне не встретился ни один пионер, с кем я мог быть знакомым."
    "Да и рисовал я не ахти как, поэтому желания записываться туда не было."
    stop music fadeout 1
    "Я поплёлся мимо второго корпуса, размышляя, куда идти дальше."
    if (d2_met_dv == True) and (d2_dv_fight == False) and (d2_dv_interrogation == False):
        jump d2_dv_talk
    th "Сверимся с бегунком. Что ещё осталось?"
    window hide
    jump d2_morning_map

label d2_event_camp_entrance:
    
    if been_there()==1:
        scene bg ext_camp_entrance_day
        with dissolve
        play ambience ambience_camp_entrance_day
        window show
        "Пусто."
        "Ворота никто и не думал запирать, а автобус давно укатил."
        "Раньше я бы запаниковал, но мне уже начал нравиться этот лагерь, пусть я и не вполне понимал, как здесь очутился."
        "Пожалуй, сейчас я даже хотел в нём остаться..."
        "Всё было так запутанно, что я никак не мог разобраться в своих желаниях!"
        window hide
        stop ambience fadeout 1
        jump d2_morning_map
    if been_there()==2:
        scene bg ext_camp_entrance_day
        with dissolve
        play ambience ambience_camp_entrance_day
        window show
        "Я уже был здесь..."
        "И с тех пор ничего не изменилось."
        window hide
        stop ambience fadeout 1
        $ disable_current_zone()
        jump d2_morning_map

label d2_event_dv_us_house:
    
    if (d2_times_been_to_dv_us_house >= 1) or (d1_un_evening == False):
        scene bg oldmap
        window show
        "Идти туда, зная, что там живут Алиса и Ульянка? Да ни за что на свете!"
        window hide
        $ disable_current_zone()
        jump d2_morning_map
    scene bg ext_houses_day 
    with dissolve
    stop music fadeout 1
    play music music_list["just_think"] fadein 2
    window show
    "Аккуратные ряды домиков, причудливо насаженные вдоль хорошо утоптанных тропинок, настраивали на удивительно созерцательный лад..."
    th "Красиво! Давно же я не был за городом!"
    "А когда-то мне нравились такие пейзажи, я даже хотел жить на природе."
    th "Может это всё же мой шанс?"
    "Какой-то заросший пионер вышел из соседнего домика и теперь равнодушно разглядывал меня."
    "Я даже смутился собственных мыслей."
    th "А в лагере полно народу — это я ещё в столовой и на построении понял." 
    th "Хотя в лагерях обычно гораздо больше отрядов и вожатых. А здесь мне этого и так хватает с лихвой."
    "Один из домиков привлек моё внимание."
    "Он выделялся среди остальных."
    th "Ну, как ядерный гриб на фоне подберёзовиков."
    scene bg ext_house_of_dv_day
    with dissolve
    "Вот это бункер! Выглядит устрашающе."
    boy_voice "Лучше не входи!"
    th "Входить туда? Я не сумасшедший."
    me "Я и не собирался..."
    "Позади стоял всё тот же самый пионер."
    "Он был невысокий, ещё ребенок, но с длинными всклокоченными волосами."
    boy "Там Алиска с Ульянкой живут."
    me "О! Спасибо за предостережение."
    "Но он уже уходил."
    th "Неудивительно, что домик выглядит так... мрачно."
    scene bg ext_houses_day
    with dissolve
    "Хм. А глаза у паренька были красные. Где я ещё мог видеть такие? Точно, у Двачевской."
    "Почему-то всё это напоминало мне о вампирах...{w} или программистах."
    "Хотя после встречи с Алисой и десятками пионеров с необычными причёсками и глазами я уже должен был перестать удивляться."
    "Оглядевшись, я больше никого не заметил."
    "Интересно, кого ещё я здесь встречу?"
    window hide
    $ d2_times_been_to_dv_us_house = 1
    stop music fadeout 1
    jump d2_morning_map

label d2_event_dining_hall:
    
    scene bg oldmap
    window show
    "Ещё вчера я понял, что еда в лагере выдается только в строго определенное время."
    "Так что до обеда тут делать абсолютно нечего, да и в бегунке столовая не указана. А жаль!"
    window hide
    $ disable_current_zone()
    jump d2_morning_map

label d2_event_sport_club:

    $ reset_chibi("sport_area")
    scene bg ext_playground_day
    with dissolve
    play music music_list["get_to_know_me_better"] fadein 1
    window show
    "В спортивном кружке явно было много детей. Девочки играли в бадминтон и волейбол, а мальчики заняли поле."
    "На залитой солнечным светом площадке пионеры гоняли в футбол."
    "Азартно подзадоривая друг друга выкриками, они носились туда-сюда по полю."
    if d1_genda_flag:
        "Я сразу увидел Ульяну среди них, как всегда одетую в ярко-красную футболку."
        th "Вот уж с кем я не хочу оказаться в одном кружке, не считая Алисы!"
    else:
        "Я застыл, наблюдая за стремительной игрой, напомнившей мне о том, как когда-то я тоже принимал участие в школьных матчах по футболу."
        th "Погонять с ними, что ли..."
        th "К черту! Это же не плэйстейшн!"
        "Утренней зарядки мне хватило."
    th "У кого же проставить подпись и слинять отсюда?"
    lk_voice "Семён! Ты ко мне?"
    #show lk
    "Я повернулся на голос и увидел шедшего ко мне парня-вожатого, что был с нами на зарядке и построении."
    me "Здравствуйте?.."
    lk "Тебе, наверно, не сказали, кто я. Меня зовут Дмитрий Евгеньевич, но к чёрту формальности, можешь звать просто Димой."
    "Поправив свои необычные очки, в которых одна линза была темнее другой, он добродушно протянул мне открытую ладонь, и я пожал её."
    "Форма на нём выглядела не совсем по регламенту. Рукава были закатаны, а воротник расстёгнут, из-за чего слегка повышенная волосатость рук и груди вожатого явно бросалась в глаза. Красный галстук Дима держал повязанным у плеча, словно пионер-шалопай, чихавший на правила."
    "«Удав», служивший ему шарфиком, оказался вовсе не дохлым, просто до этого был повернут головой от меня. Напротив, розовощёкий удав хитровато щурился, будто увидел нечто пошло-эротичное."
    th "Забавно."
    me "Я пришёл с обходным листом, чтобы отметиться."
    lk "Знаю, твоя вожатая сказала мне об этом ещё утром. Давай бегунок."
    lk "Кстати, я же отвечаю за спортивный кружок. У нас несколько секций: футбольная, волейбольная, бадминтон... Можешь заниматься где хочешь. Сегодня в одной, завтра в другой!"
    "Он говорил весело и вообще был настроен дружелюбно."
    me "А записываться для этого обязательно?"
    lk "Ха, нет, но тогда если потеряешь инвентарь, покалечишься или примешь ислам, — я не виноват. Договорились?"
    "Дима отдал мне обходной лист."
    me "Ну и шутки у вас."
    lk "Не у «вас», а у «тебя», со мной можно не выкать."
    "Он улыбнулся."
    "Что-то было в нём такое. Дима напоминал мне студента-балагура, вечно небритого, легкомысленного, но в то же время достаточно везучего и пользующегося вниманием. Такие как он являются душой компании."
    "Трудно было понять: пытается ли вожатый казаться пионеру своим в доску, или он действительно не утруждает себя ролью воспитателя?"
    "Он взял меня за плечо и развернул лицом к полю."
    lk "Можешь хоть прямо сейчас присоединиться к футболистам. За какую команду пойдёшь играть?"   
    me "Но я не в спортивной форме..."
    lk "Главное — кеды на ногах. Клади галстук в карман и вперёд!"
    me "Нет, спасибо. Я того... перетрудился на зарядке, если хотите знать."
    "Дима засмеялся."
    lk "Я тебя прекрасно понимаю. Не буду настаивать."
    "Он похлопал меня по плечу и направился к пионерам, которые наблюдали за игрой с лавочек."
    #hide lk
    $ d2_necessary_done += 1
    "Я двинулся по аллее мимо душевых, просматривая список кружков."
    th "Куда мне теперь?"
    $ disable_current_zone()
    stop music fadeout 1
    if (d2_met_dv == True) and (d2_dv_fight == False) and (d2_dv_interrogation == False):
        jump d2_dv_talk
    window hide
    jump d2_morning_map

label d2_event_beach:

    scene bg ext_beach_day 
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    play ambience ambience_lake_shore_day fadein 1
    $ renpy.pause(1)
    window show
    "Пляж был гораздо шире, больше и красивее, чем мне раньше представлялось при взгляде на карту."
    "Золотисто-белый песок отблескивал на солнце, а на гладь залива нельзя было смотреть не щурясь — вода сверкала так, что глазам было больно."
    "День был жаркий. Завидев пляж и реку, я сразу же захотел окунуться в воду с головой."
    "...И плевать, что я ещё не проставил все подписи, дело подождёт."
    "Я начал торопливо расстёгивать рубашку, положив галстук в карман..."
    show mt normal panama swim at center with dissolve
    mt "Привет."
    "Я аж оторопел, встретив Ольгу Дмитриевну."
    "Вожатая, как оказалось, отдыхала на шезлонге в тени деревца, мимо которого я прошёл, спускаясь на пляж, и не заметил её."
    th "Так вот куда она отправилась...{w} работать! С книжкой!"
    "В руках у Ольги Дмитриевны покоился том какого-то автора."
    show mt smile panama swim at center with dspr
    mt "Я смотрю, ты уже обошёл весь лагерь и со всеми перезнакомился?"
    "Она язвительно улыбалась, но я уже был готов простить ей строгость."
    th "А купальник ей очень даже идёт."
    "В уме я немедленно восстановил картинку после утреннего пробуждения, когда застал вожатую за переодеванием. Как назло, этот интригующий купальник скрывал всё то, что мне не случилось узреть."
    "Думая об этом, я немного помедлил с ответом."
    me "Да вот — знакомлюсь."
    show mt angry panama swim at center with dspr
    "Ольга Дмитриевна недоверчиво покачала головой."
    mt "Ну-ну! И уже готов мне показать бегунок?"
    "И продолжила, не давая мне вставить ни слова."
    mt "Пока со всеми не познакомишься и дело не выполнишь, о пляже можешь и не мечтать!"
    "По тону было ясно, что её решение обсуждению не подлежит."
    show mt normal panama swim at center with dspr
    "Чёрт! Вода так изумительно переливалась на солнце. Мягкие волны манили к себе."
    "Я был на море всего раз, но это было так давно..."
    me "Я ведь только искупнусь и сразу же дальше с бегунком пойду!"
    me "Обещаю!"
    show mt smile panama swim at center with dspr
    mt "И {w=0.2}не {w=0.2}меч{w=0.2}тай!"
    hide mt with dissolve
    "И, улыбнувшись, пошла в воду!"
    th "Да что за лагерь здесь такой? Исправительный, что ли?!"
    th "Вожатые делают, что хотят, а пионерам остаётся только завидовать?"
    window hide
    stop music fadeout 1
    stop ambience fadeout 1
    $ d2_met_mt = True
    $ disable_current_zone()
    jump d2_morning_map

label d2_event_me_mt_house:

    if been_there()>1:
        scene bg ext_houses_day
        with dissolve
        window show
        "И что я здесь забыл?"
        window hide
        $ disable_current_zone()
        jump d2_morning_map
    play music music_list["lightness"] fadein 1
    scene bg ext_house_of_mt_day
    with dissolve
    window show
    "Я вышел к домику, которому предстояло стать моим на эти две недели, и остановился..."
    "Спать совершенно не хотелось."
    th "Какого чёрта? Солнце, чистый воздух — нужно пользоваться!"
    th "Пусть меня и отправили с бегунком, но я же могу просто гулять!"
    th "Что ж, похожу ещё по лагерю!"
    stop music fadeout 1
    if (d2_met_dv == True) and (d2_dv_fight == False) and (d2_dv_interrogation == False):
        jump d2_dv_talk
    window hide
    jump d2_morning_map

label d2_event_library:
    
    $ reset_chibi("library")
    play music music_list["lightness"] fadein 2
    scene bg ext_library_day
    with dissolve
    window show
    "Широкая дорожка из каменных плиток привела меня к библиотеке, где мне должны были проставить подпись за кружок пионерской стенгазеты."
    "Небольшое здание стояло немного на отшибе, куда не долетали шум и голоса лагеря, а внутри, наверно, царила та самая библиотечная тишина, знакомая с детства."
    "Храм знаний — тоже храм..."
    "Я слегка постучал и толкнул дверь, которая легко отворилась."
    window hide
    play sound sfx_open_door_1
    stop music fadeout 1
    $ renpy.pause(1)
    scene bg int_library_day
    with dissolve
    play music music_list["get_to_know_me_better"] fadein 2
    play ambience ambience_library_day fadein 1
    window show
    "Из тесной проходной я двинулся свободной парте мимо столиков, занятых пионерами. Остановился и осмотрелся."
    "Внутри было прохладно, пахло книгами."
    "Но больше всего меня поразило обилие советской символики."
    "Тут висели лозунги, транспаранты, вымпелы, красные флаги и даже стоял гипсовый бюст..."
    th "Похоже, и в этом мире Ленин имел непосредственное отношение к советской власти."
    "Но здесь всё было расставлено в идеальном порядке, а на бюсте — ни следа пыли."
    "Несколько пионеров, мальчиков и девочек, тихо читали, что-то писали и рисовали, изредка шушукаясь между собой."
    show un normal pioneer far at left with dissolve
    "Я заметил уже знакомую мне голову с двумя фиолетовыми хвостиками — Лена тоже читала за столиком, но в затенённой половине библиотеки, словно решив отделиться ото всех на время."
    hide un with dissolve
    "Очевидно, что с бегунком подходить надо было не к ней."
    if d1_tricked:
        th "...А к Жене."
    "Я отыскал пионерку, которая должна была отвечать за это место."
    scene cg d2_micu_lib with dissolve
    "Она сидела за столом с компьютером и телефоном у входа."
    if d1_runaway:
        th "Библиотекарша?"
    "Сидела, склонив голову на сложенные руки и..."
    th "Да она же дрыхнет как суслик!"
    "Девочка даже тихо посапывала во сне!"
    "Осмелев, я подошёл чуть ближе."
    th "Хм... спит на рабочем месте?"
    th "Пожалуй, с ней можно иметь дело. По крайней мере, видно, что пионерка не очень-то прилежно относится к своим обязанностям."
    if d1_un_evening:
        "У неё был забавный вихор на макушке..."
    else:
        "У неё были очки с толстыми линзами и забавный вихор на макушке..."
    "За который почему-то сразу очень захотелось дёрнуть. Или уложить на место."
    "Не успев осознать, что именно происходит, я потянул руку к голове спящей ботанички..."
    scene bg int_library_day
    with dissolve
    show mz normal glasses pioneer at center with dissolve
    mz "Стоять!"
    "Я мигом застыл, с уже протянутой рукой."
    show mz bukal glasses pioneer at center  with dspr
    "Вихрастая библиотекарша подняла голову, посмотрела на меня внимательно и шлёпнула по ладони."
    mz "Другую руку."
    "Голос её прозвучал довольно резко, не самым приятным тоном."
    th "Вредина." 
    "Я почему-то сразу подумал так, а она повторила."
    mz "Давай руку."
    me "Что?"
    show mz angry glasses pioneer at center with dspr
    mz "Другую!"
    th "Ох, лучше её не злить!"
    "Я протянул ей скрученный в трубочку листок от Ольги Дмитриевны."
    show mz normal glasses pioneer at center with dspr
    th "Так вот что ей было нужно!"
    "Она взяла у меня листок и аккуратно развернула у себя на столе."
    show mz bukal glasses pioneer at center with dspr
    mz "Ага... ясно. Какие имя-фамилия, дата рождения?"
    me "Семён Персунов."
    "Дату я назвал ту, что видел на справке для медосмотра."
    show mz normal glasses pioneer at center with dspr
    "И если раньше девочку интересовал только листок, то теперь она снова смотрела на меня... Как-то оценивающе."
    "Мне это совсем не понравилось."
    mz "Так. Подпись я тебе не дам."
    th "Я подозревал это."
    mz "Её нужно заслужить."
    show mz bukal glasses pioneer at center with dspr
    mz "Книги видишь?"
    "Я посмотрел в ту сторону, куда она указала пальцем, и кивнул."
    "У стены действительно были сложены книги."
    me "Вижу."
    "Стопка была внушительная."
    show mz normal glasses pioneer at center with dspr
    mz "Возьмёшь эти книги и расставишь их по полкам."
    th "Что?"
    "Я уже собрался протестовать, почему это не поручили кому-то из посетителей библиотеки, но она с ещё более недовольным лицом проворчала."
    show mz angry glasses pioneer at center with dspr
    mz "Тогда подпишу. Ясно?"
    "И не давая мне ничего вставить, сказала, показывая, что разговор окончен."
    show mz normal glasses pioneer at center with dspr
    mz "Приступай."
    hide mz with dissolve
    "И отвернулась, делая вид, что что-то ищет в столе."
    "От такой наглости я просто онемел."
    th "Но меня ведь послали с бегунком..."
    "Да и грубить как-то не хотелось, а по-другому вряд ли что-нибудь удалось бы сделать."
    "И я двинулся к книгам, стараясь не думать о библиотекарше и прикидывая, как бы отделаться от этого задания побыстрее..."
    th "Может, просто бросить их в другом месте, за полками?"
    "Но вслед мне донеслось предупреждение." 
    mz "Я потом проверю, так что даже не думай свалить их куда-нибудь в угол!"
    th "Вот чёрт..." 
    th "Кажется, я не отделаюсь малой кровью. Интересно, они с Ольгой Дмитриевной в сговоре? Не хотел бы я однажды предстать пред их очами одновременно."
    "Несмотря на то, что стопка книг была довольно приличной, много хлопот она мне не доставила, так как большая часть из них оказалась томами сочинений разных авторов, и мне надо было всего-то найти полки с соответствующими инициалам буквами."
    "Пока я расставлял их, за мной краем глаза посматривала библиотекарша..."
    if d1_genda_flag:
        th "Даже имени своего не назвала — точно вредина!{w} Секунду, не её ли Сыроежкин называл Женей?"
        $ meet('mz', u"Женя")
        th "Да, всё правильно, это она."
    "Последнюю книжку я поместил на полку шкафа рядом с бюстом."
    show un normal pioneer at cright with dissolve
    "Вдруг в просвете между книжками и полочкой над ними я увидел читающую Лену, вновь задержав своё внимание на ней."
    th "Что же. Наша скромница предпочитает храм знаний спортивным мероприятиям или блаженному ничегонеделанию."
    th "Интересно, что она читает? Один вид этого кирпича заставляет ужасаться."
    "Рядом с девочкой лежали ещё две книжки, и я заметил обложку той, что была сверху, с красивым орнаментом и тиснёными позолоченными буквами названия."
    th "Легенды и сказания Древней Греции и Древнего Рима."
    "В голове всплыли образы древнегреческих богов и героев, римских полководцев..."
    th "Так вот что она читает — сказки с историческим флёром! Мило."
    "Почему-то стало очень приятно, хотя я в своём возрасте не стал бы перечитывать мифы, наверняка ещё изложенные в сокращении для юного читателя."
    th "Видимо, Лена очень романтичная особа и..."
    show un normal pioneer close at cright with dspr
    "Я тихо пробрался мимо шкафа и пустующего столика так, чтобы не дать себя заметить, и, затаив дыхание и слегка наклонившись через плечо Лены, заглянул в её книгу."
    "{i}- Погоди, припоминаю! Это вроде как отличие? \n- В любви. И дарит его тот, кто достиг этого с нею, но только тогда, когда заставил и её достигнуть наравне. Успех зависит от обоих...{/i}"
    "И она читает вот это..."
    th "В очень тихом омуте водятся очень толстые черти. Неужели я ошибся в ней?"
    "Я одёрнул себя за глупые и ханжеские мысли, ведь если подумать, то прочитанное тоже по-своему романтично: когда два любящих друг друга человека вместе..."
    "Внезапно, я почувствовал резкий прилив крови к своей промежности. Я наклонился ещё немножко, желая заглянуть под небрежно завязанный узел пионерского галстука на её воротнике..."
    show un shy pioneer close at cright with dspr
    "Кажется, Лена заметила меня!"
    show un scared pioneer close at cright with dspr
    "Девочка быстро захлопнула книгу и оглянулась на меня с болезненной синевой испуга на лице."
    me "Извини, если напугал."
    show un surprise pioneer at cright with dspr
    un "Нет, всё в порядке..."
    th "Как бы сказать, что я не сделал ничего плохого?"
    me "Я тут, э-э... Помогаю Жене с книгами... За подпись в обходном листе. Увидел тебя, решил посмотреть, что ты читаешь."
    show un grin pioneer at cright with dspr
    "Похоже, у Лены отлегло от сердца, она успокоилась и улыбнулась."
    show un smile pioneer at cright with dspr
    un "А, это? «Таис»."
    "Она показала мне угольно-чёрную обложку книги с фамилией автора. Похоже, это был один из томов его собрания сочинений."
    th "«Таис Афинская»? Слышал о таком произведении, но не читал, оно как-то прошло мимо меня. Я не могу ничего сказать Лене о нём."
    "Я изобразил спешку."
    me "Понял! Ладно, меня тут запрягли с книгами, не буду мешать."
    hide un with dissolve
    "И повернулся к девочке спиной, уткнувшись носом в книжный ряд на полке шкафа."
    "Подождав чуть-чуть, я бросил мимолётный взгляд на девочку. Она снова вернулась к чтению."
    th "По-моему, я смутился и перепугался куда сильней, чем сама Лена. Блин."
    th "А ещё она сидит в неудобном положении..."
    "Я был готов поклясться, что видел розоватую ткань её трусиков из-за согнувшегося края юбки!"
    "На меня нашло что-то нехорошее."
    th "Я хочу заглянуть ей под юбку."
    if sp_crg >= 2:
        stop music fadeout 1
        play music music_list["i_want_to_play"] fadein 1
        "Почему бы и нет? Момент самый подходящий."
        th "Да и опасаться, в целом, нечего. Может даже, всё окружающее меня вообще не существует, а я лежу в коме, пускаю слюни и вижу сны? Ведь мир не мог в один момент так сильно измениться."
        th "Во сне можно делать что угодно."
        th "И я не верю в чудеса."
        th "Возможно даже придётся чуть-чуть приподнять юбку..."
        "..."
        "Дерзкий план!"
        "Я взял с ближайшей полки первую попавшуюся книгу и сел с ней за стол позади Лены. Достал карандаш из стаканчика, взял подвернувшийся лист и стал делать вид, что выписываю что-то нужное для себя."
        "На случай, чтобы отмазаться, переписал одно предложение из книжки."
        "Я начертил на бумажке ещё пару бессмысленных фраз, перевернул её и положил карандаш на стол, слегка подтолкнув его. Благодаря силе инерции, он скатился на пол."
        "Лена ничего не услышала, а если и услышала, то не стала оборачиваться и предлагать помощь, так сильно она была увлечена своей книжкой или же постеснялась."
        th "То что надо!"
        "А теперь самое интересное..."
        "Я наклонился, будто бы за карандашом, но не это было моей целью."
        th "Блджад! Так и знал, что придётся приподнять юбку!"
        "Для этого я вооружился подобранным карандашом."
        "Я потянулся рукой вперёд и..."
        with vpunch
        play sound sfx_chair_fall
        #"БАХ!"
        "Не удержавшись на краю, я грохнулся на пол и повалил ногами стул за собой."
        "Аж искры из глаз посыпались!"
        show un shocked pioneer at center with dissolve
        "Испугавшаяся во второй раз Лена вскочила с места."
        th "Ну что, видно что-нибудь?"
        #Спрайты до закомментированной смены cg на bg здесь используются временно.
        #scene cg d2_un_pantsushot with dissolve
        show un sad pioneer at center with dspr
        "Превозмогая боль от ушибов, я поглядел вверх, когда девочка подошла ко мне."
        th "!"
        "Безукоризненно чистые (наверно, она ещё не дочитала до момента, попавшегося мне на глаза!) бледно-розовые трусики, чуть натянувшиеся оттого, что девочка свела коленки вместе."
        th "Да! Богиня удачи улыбнулась мне! Труды вознаграждены!"
        stop music fadeout 1
        play music music_list["she_is_kind"] fadein 2
        show un shy pioneer close at cleft with dspr
        "И тут же Лена едва склонилась ко мне, прижав руки к юбке, и прекрасное мгновение кончилось."
        un "Бедный! Помочь?"
        "Не дожидаясь моего ответа, она присела и помогла встать."
        #scene bg int_library_day with dissolve
        show un sad pioneer at center with dspr
        un "Что случилось? Не сильно ушибся?"
        "Она спрашивала меня робко, в голосе её слышалось сопереживание." 
        "А вот я начал чувствовать себя неуютно — ко мне со всей душой, а я пялился под юбку и целый спектакль ради этого разыграл."
        th "Не стыдно ли мне?"
        menu:
            "Я поступил неправильно":
                "Она, конечно же, ничего не заметила, но я вынес урок."
                me "Лена, я должен извиниться перед тобой..."
                "Я почувствовал, как закипаю от конфуза и неспособности выразить, в чём же я виноват."
                show un smile3 pioneer at center with dspr
                un "Ничего страшного! Ты сядь, подожди, когда нога пройдёт!"
                show un normal pioneer at center with dspr
                "Лена подняла стул и передала мне тот листик с ничего не значащами записями."
                "Действительно, я слегка прихрамывал из-за ушибленного колена. Плечу было не легче."
                show un sad pioneer close at center with dspr
                "Пришлось сесть с Леной за столик — напротив неё."
                "Девочка всё ещё была обеспокоена, но я убедил её, что нет смысла волноваться."
                me "Ерунда, через пару минут уже буду в порядке."
                "Лена кивнула."
                un "Я надеюсь на это!"
                show un normal pioneer close at center with dspr
                "Она снова вернулась к чтению."
                if d1_un_evening:
                    me "Кстати, ты вчера вроде другую книгу читала, верно?"
                    show un shy pioneer close at center with dspr
                    un "А?"
                    show un smile pioneer close at center with dspr
                    un "Да, я обычно читаю по нескольку разных книг сразу. Если что-то не удастся дочитать в лагере, то в городе схожу в библиотеку и возьму книжку там, чтобы прочесть до конца."
                    me "Вот как...{w} Можно?" 
                else:
                    me "Можно посмотреть?"
                    show un smile pioneer close at center with dspr
                "Я тронул объёмный том с мифами и сказаниями, намереваясь почитать его."
                un "Конечно! Только если захочешь взять с собой, надо подойти к Жене с книжкой."
                me "Угу. Спасибо!"
                show un normal pioneer close at center with dspr
                "И я принялся деловито листать книгу, выискивая хоть что-нибудь интересное, однако всё моё внимание ускользало прочь от напечатанных строчек вверх: я то и дело посматривал на Лену."
                "Остановившись на мифе об Аполлоне и Дафне, я потерял всякий интерес к книге..."
                "Бледный свет из окон делал кожу девочки белее, а лицо красивее."
                "Извечную печаль в зелёных глазах сменила сосредоточенность."
                th "Наверно, когда Лена поглощена чтением, она забывает о грустном. Конечно, книга — спасительное средство... Близкий друг."
                show un surprise pioneer close at center with dspr
                "Мы встретились взглядами, и Лена ойкнула от неожиданности, а потом пришла в смущение." 
                show un shy pioneer close at center with dspr
                un "Что-то хочешь спросить?" 
                "Я помотал головой."
                me "Просто хотел ещё раз сказать спасибо за помощь, я цел и могу идти с обходным листом дальше..."
                show un smile pioneer close at center with dspr
                un "Не за что! Это хорошо, что ты в порядке..."
                hide un with dissolve
                stop music fadeout 1
                play music music_list["get_to_know_me_better"] fadein 2
                "..."
                "Ноге с плечом стало лучше, и я спокойно вернулся к библиотечному ресепшену, где меня ждала недовольная Женя."
            "Если я хотел этого, не надо сожалеть":
                $ d2_no_shame = True
                th "Не стоит мозолить ей глаза своим присутствием, а то ещё догадается, что это не было случайностью."
                me "Всё нормально, бывало и больней."
                "Я махнул рукой."
                me "Пройдёт."
                stop music fadeout 1
                play music music_list["get_to_know_me_better"] fadein 2
                "..."
                hide un with dissolve
                "Я поднял упавший стул, забрал лист со столика и, невзирая на саднящее колено, стоически поковылял к Жене, которая встретила меня гневным взглядом."
        show mz rage glasses pioneer at center with dissolve
        mz "Первый раз не воспретительно, но на будущее: никакого шума в библиотеке! Пошумишь или сломаешь что вдругорядь, исключу из посетителей!"
        me "Извиняюсь..."
        mz "Нет, Семён! Надо говорить «извините», а «извиняюсь» — это по-разговорному и попросту невежливо!"
        "Я немного опешил, но понял, что хотела сказать пионерка."
        me "Извини меня, пожалуйста. Не хотел шуметь, правда. И книги расставил."
        show mz normal glasses pioneer at center with dspr
        "Женя смягчилась."
        mz "Извинения приняты."
    else:
        "Насколько быстро вспыхнула в мозгу эта идея, настолько же быстро она была отвергнута."
        th "Бессмысленный риск."
        "Я с трудом попытался представить свои манёвры при осуществлении затеи, и не решился. Пусть в очередной раз случайная мысль останется лишь фантазией."
        th "Книги-то я расставил, как надо, значит, Женя отпустит меня, и я смогу скорей пойти дальше по обходному листу."
        "К библиотекарше я подошёл с чувством выполненного долга. Хоть бы она не придумала ещё что-то кроме этого поручения!"
        show mz normal glasses pioneer at center with dissolve
        me "Всё, разобрал книги."
        mz "Молодец."

    show mz bukal glasses pioneer at center with dspr
    mz "Вот, держи, я внесла тебя в читательскую базу и сделала тебе билет..."
    "Передо мной легла карточка из плотной бумаги с заполненной формой."
    th "Может, зря я думал о ней, как о вредине? Всё-таки не без дела сидела, пока я таскал книжки."
    show mz normal glasses pioneer at center with dspr
    mz "Подпись за обход готова. Если запишешься в пионерскую редколлегию, то сможешь приходить сюда в тихий час для чтения и работы над стенгазетой." 
    mz "На руки выдаётся только три книги и три журнала за раз сроком на неделю. Если они ещё понадобятся, то я продлю их тебе. Если книга или журнал будут востребованы кем-то, и у них нет копии, то продления не жди, придётся оставить их другому читателю." 
    show mz angry glasses pioneer at center with dspr
    mz "И да! Страницы не рвать, не вырывать! Переплёт не портить! Если что не так, самодеятельность с ножницами, клеем и скотчем не разводить! Оставь это мне."
    me "Всё понял. Спасибо."
    hide mz with dissolve
    "Читательский билет перекочевал со стола ко мне в карман, а я получил обратно бегунок и вышел из библиотеки, поскольку больше ничего меня тут не держало."
    $ d2_necessary_done += 1
    scene bg ext_library_day
    with dissolve
    th "Пойдём дальше..."
    stop music fadeout 1
    stop ambience fadeout 1
    $ disable_current_zone()
    if (d2_met_dv == True) and (d2_dv_fight == False) and (d2_dv_interrogation == False):
        jump d2_dv_talk
    window hide
    jump d2_morning_map

label d2_event_aidpost:    
    
    $ reset_chibi("medic_house")
    if been_there()>1:
        scene bg ext_aidpost_day
        with dissolve
        window show
        "Вот разберусь с обходным листом — буду каждый день в медпункт заглядывать!"
        window hide
        $ disable_current_zone()
        jump d2_morning_map

    play music music_list["so_good_to_be_careless"] fadein 1
    scene bg ext_aidpost_day
    with dissolve
    window show
    "Медпункт мне был совершенно ни к чему: чувствовал я себя отлично."
    "Зато вожатая требовала, чтобы я прошёл медосмотр, как и все пионеры, поэтому я был здесь."
    "Издалека небольшой домик можно было принять за жилой, но он был куда более ухоженным."
    th "Похоже, здесь даже болеть приятно."
    "Я подошёл к двери и постучал."
    play sound sfx_knock_door7_polite
    $ renpy.pause(2)
    "Изнутри отозвался явно женский голос."
    cs_voice "Войдите."
    play sound sfx_open_door_2
    scene bg int_aidpost_day
    with dissolve
    play ambience ambience_medstation_inside_day fadein 2
    "И я вошёл."
    me "При..."
    stop music fadeout 2
    "Я остановился на полуслове."
    me "Здравствуйте."
    play music music_list["get_to_know_me_better"] fadein 1
    #Разрываюсь между этим треком и eternal_longing, поскольку в ивенте сочетаются и первое/интригующее знакомство, и флирт.
    #Вообще eternal_longing под активный хентай с Дваче. Звуковое сопровождение для текущей сцены пока под вопросом.
    show cs normal at center with dissolve
    #TODO: Сделать для первой встречи проезд по спрайту снизу вверх, с ног до груди и лица.
    #Снизу строчка из демо. Требуется адаптировать для нынешней версии.
    #show cs std at Pan((0, int(2250*config.screen_height/1080.0)-config.screen_height), (0, 0), 10.0)
    th "Ох..."
    "На меня, чуть прищурившись от яркого света, смотрела очаровательная женщина."
    th "А глаза у неё непростые — с хитрецой. И необычные: один красный, другой синий."
    cs "Пионер? Ну, заходи."
    show cs smile at center with dspr
    "Она улыбнулась, и я последовал за ней из тесного холла с диванчиками в процедурный кабинет, но остановился буквально на полпути, заглядевшись, как она шла, покачивая бёдрами."
    show cs normal at center with dspr
    cs "Я тебя здесь ещё не видела. Новенький?"
    me "Д-да, только вчера приехал."
    me "Вот, сказали знакомиться с лагерем..."
    "Я всё ещё стоял у порога кабинета, немного смущённый под взглядом её странных, пронизывающих насквозь глаз."
    me "Меня вообще-то послали с бегунком. И потребовали пройти медосмотр."
    show cs smile at center with dspr
    cs "Да-а?"
    "Медсестра это даже не сказала, а протянула томным голосом."
    th "Как будто играет со мной!"
    "Она двинулась ко мне навстречу. Я стоял, боясь шелохнуться и не зная, что делать."
    show cs smile close at center with dspr
    "А она подошла вплотную. Так, что наши лица почти соприкасались..."
    "И взяла из моих рук справку."
    cs "Ну, давай знакомиться...{w=.2} пионер."
    show cs normal at center with dspr
    "Она прочла моё имя на документе и пошла назад к своему столу."
    cs "Присаживайся на кушетку."
    "До этого момента я словно не дышал. Стараясь как можно тише выдохнуть, я послушно сел на койку."
    show cs normal glasses at center with dissolve
    "Докторша расположилась на стуле рядом, будто нарочно заложив ногу на ногу и оправив медицинский халат так, чтобы мне во всей красе были видны её элегантные и не менее эротичные чулки."
    cs "Зовут меня Коллайдер Виолетта Церновна. На Церновне обычно ломаются языки у всех мужчин, особенно когда они хотят сказать мне что-то приятное... И в итоге я остаюсь без добрых слов. Так что заранее устраним это препятствие... Да, Семён?"
    "Я попытался хоть что-то сказать, но с дыханием будто снова приключилась беда."
    show cs smile glasses at center with dspr
    "Она чуточку, краешком губ усмехнулась, продолжая что-то записывать себе в отдельный лист, а затем повернулась ко мне."
    cs "Ты..."
    "Тут она сделала ударение."
    cs "Можешь звать меня просто Виолой."
    $ cs_name = u"Виола"
    "Я судорожно сглотнул."
    cs "Или доктором. Как тебе больше нравится."
    "В тот момент я не нашёлся, что ответить."
    th "Как же мне её звать?"
    menu:
        "Виола":
            $ cs_name = u"Виола" 
            $ lp_cs = lp_cs + 1
        "Доктор":
            $ cs_name = u"Доктор"
    "Одно я знал точно." 
    th "{i}Этот{/i} доктор мне нравится!"
    show cs normal glasses at center with dspr
    cs "Есть жалобы, Семён?"
    th "Жалобы? Какие могут быть жалобы, когда рядом такая женщина?"
    me "...Нет, никаких."
    "Она что-то записала в справку с отдельным листом, покачала ручкой и положила её на стол."
    show cs normal at center with dspr
    cs "Тогда раздевайся.{w} До трусов."
    th "Что?"
    "Но я, даже не пытаясь вникнуть, для чего, расстегнул рубашку и начал стягивать шорты с носками. Тем временем Виола прошла к медицинскому ростометру и убрала сиденье над стойкой."
    cs "Прошу, пионер."
    show cs smile close at center with dspr
    "Я прислонился спиной к измерительному столбу и выпрямился."
    "Сверху заскрипела планка, пока не остановилась на делении с моим ростом. Я косился в сторону, глядя на доктора, точнее, на её декольте, плохо скрываемое рубашкой под белым халатом..."
    th "Ничего себе!"
    "Эти объёмы впечатляли и не на шутку взбудоражили моё воображение."
    cs "Хм, похоже, ты один из самых высоких парней в лагере, Семён!"
    th "Она что, помнит рост каждого пионера или только... наиболее выделяющихся?"
    "Вдруг женщина снова оказалась передо мной почти вплотную, и я вздрогнул."
    "Виола медленно провела изящным пальцем от шеи до живота и пощупала мой пресс."
    cs "Что-то ты худоват малость. И бледен."
    show cs shy close at center with dspr
    "Она, глядя вниз, улыбнулась и убрала руку, но я всё ещё чувствовал тот обжигающий холод и прикосновение острых ногтей."
    show cs smile close at center with dspr
    cs "Надо чаще бывать на свежем воздухе. Надо есть больше овощей!{w} Не помешает заниматься дополнительными физическими упражнениями и бегом. Физкультурная группа у тебя общая, так что это не проблема."
    show cs normal close at center with dspr
    cs "Я могу выписать разрешение, отдашь своей вожатой."
    me "В смысле, чтобы я мог бегать по утрам? Как Славя?"
    show cs smile close at center with dspr
    "Виола с любопытством глянула на меня, когда я произнёс имя девочки."
    cs "Да. Как Славя."
    menu:
            "Выписывайте разрешение":
                me "Давайте, я не против."
                $ more_fiz = True
            "Нет, спасибо, зарядки хватит":
                me "Нет, обойдусь зарядкой."
    "Я покинул стойку ростометра."
    show cs normal at center with dspr
    cs "А теперь измерим вес..."
    th "Что, медосмотр ещё не кончился? Но с таким доктором я не прочь проводить медосмотр хоть целый день!"
    show cs normal close at center with dspr
    "На платформу весов я ступил уже посмелей, как только доктор привела их в готовность."
    "Виола ловко переместила гирьки, пока указатель весов не замер у отметки."
    show cs smile close at center with dspr
    cs "Так... Всё, пионер, можешь слезать."
    show cs normal at center with dspr
    "Я отошёл к койке и взял шорты, чтобы надеть их, но Коллайдер с многозначительной улыбкой остановила меня."
    show cs smile at center with dspr
    cs "Разве я сказала одеваться, Семён?"
    me "Извините."
    cs "Ты куда-то спешишь?"
    me "Нет, что вы. Я думал, что уже всё."
    cs "Никогда не спеши, этим можно оскорбить..."
    show cs normal glasses at center with dissolve
    "Наверно, я покраснел в этот момент, а Виола села за стол, чтобы написать результаты измерений в справке."
    "Но мгновение спустя она поднялась."
    show cs normal at center with dspr
    cs "Вставай."
    show cs smile stethoscope close at center with dspr
    "Она взяла стетоскоп, надела его и, когда я выпрямился, приложила к моей груди холодную головку инструмента."
    "Я снова уставился на глубокий вырез её халата..."
    "Прослушав грудь, Виола попросила меня повернуться спиной к ней."
    hide cs with dissolve
    cs "Дыши ртом."
    "Она несколько раз приложила стетоскоп."
    cs "Теперь можешь одеваться."
    show cs normal stethoscope glasses at center with dissolve
    "А сама опять села дополнять записи в справке."
    cs "Куришь?"
    me "Да."
    "Она молча кивнула головой, вероятно, имея в виду, что так и поняла."
    show cs normal stethoscope at center with dspr
    "Я неторопливо оделся, а Виола достала из ящичка в столе какой-то инструмент, и я вспомнил, что последний раз видел такой на медкомиссии в военкомате."
    th "Ага, кистевая динамометрия."
    cs "Жми, сначала правой, потом левой."
    "Это было просто."
    "Я назвал получившиеся числа, на что Виолетта едва заметно покачала головой."
    show cs normal stethoscope glasses at center with dspr
    cs "Гм, показатели ниже среднего, чем требуется для парня твоего возраста..."
    show cs smile stethoscope glasses at center with dspr
    cs "К сожалению, ты пока можешь носить на руках только некоторых девочек из младшего отряда. Набирайся сил, потянешь и тех, кто постарше!"
    "Она подмигнула мне."
    th "На что это она намекает? Я не собирался никого носи...{w} А вдруг придётся?"
    "В некоторой степени эта мысль была приятной."
    "Виола улыбалась, видя моё замешательство."
    "Наконец, она закончила писать в справке и на отдельном листе."
    show cs normal stethoscope glasses at center with dspr
    if more_fiz:
        cs "Сейчас ещё разрешение для вожатой тебе сделаю, и будешь свободен."
        "Она достала новый бланк из другого ящичка в столе и быстро заполнила его."
        cs "Держи. А справка останется у меня до конца смены."
    else:
        cs "Семён, эта справка останется у меня до конца смены, получишь её перед отъездом."
    me "Понял."
    "Я, уже полностью одетый с кое-как повязанным галстуком, поднялся с койки."
    show cs smile at center with dspr
    "Медсестра отложила очки и стетоскоп на стол."
    cs "Ну вот и познакомились. А теперь иди...{w} Семён."
    "Мне оставалось только кивнуть..."
    me "Спасибо."
    hide cs with dissolve
    stop ambience fadeout 1
    "...И выйти из кабинета в холл и наружу."
    $ med_exam = True
    $ d2_necessary_done += 1
    scene bg ext_aidpost_day
    with dissolve
    "На улице я ещё недолго приходил в себя."
    th "Какая красивая женщина!"
    if d1_genda_flag:
        th "Правду говорил Сыроежкин!"
    stop music fadeout 2
    "И познакомился (даром, что говорить почти ничего не пришлось!), и ещё один пункт плана выполнил. Такие дела."
    if (d2_met_dv == True) and (d2_dv_fight == False) and (d2_dv_interrogation == False):
        jump d2_dv_talk
    window hide
    jump d2_morning_map

label d2_event_green_theatre:
    
    scene bg ext_stage_big_day
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    window show
    "Дорогу к сцене я нашёл у библиотеки. Идти отсюда было недалеко."
    "Эстрада производила впечатление! Она была большая и, видимо, только недавно построена."
    "Свежеструганные доски ещё приятно пахли смолой, а тенёк под крышей приятно манил с солнцепёка."
    "Осмотревшись — никого вокруг не было видно — я поднялся на сцену."
    scene bg ext_stage_normal_day
    with dissolve
    th "Усилитель, колонки... Неплохая аппаратура! Хотел бы я забрать такую себе домой!.."
    "Микрофон!"
    "Я подошёл и щёлкнул тумблером."
    play sound sfx_heavy_click
    th "М-м-м... Никогда раньше не стоял на сцене."
    "Я представил, что передо мной зал, полный людей. Джентльмены в смокингах и белоснежных накрахмаленных сорочках, черные бабочки, усы... У многих пенсне и монокли."
    "Дамы в вечерних туалетах лениво обмахиваются веерами и смотрят в лорнеты..."
    "Внезапно как будто ледяной ветер ударил мне в спину."
    "Что-то было не так." 
    th "Но что?!"
    if sp_crg >= 2:
        "Смотрят...{w} Они все смотрят на меня!!!"
    elif sp_crg <= 1:
        "Вот же чёрт! Я определенно чувствовал себя не в своей тарелке."
    play sound sfx_ghm_1
    me "Гм..."
    "Микрофон работал! Да ещё как!!!"
    "Колонки издали моё протяжное «Гм» и, казалось, разнесли по всему лагерю с омерзительным писком."
    "Я уже на ходу выключил микрофон и бросился бежать."
    window hide
    stop music fadeout 1
    $ d2_times_been_to_green_theatre = 1
    $ disable_current_zone()
    jump d2_morning_map

label d2_event_square:
    
    if been_there()>1:
        scene bg ext_square_day
        with dissolve
        window show
        me "Похоже, это одно из немногих мест, где всё по-прежнему."
        window hide
        $ disable_current_zone()
        jump d2_morning_map
    
    play music music_list["everyday_theme"] fadein 2
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_square_day
    with dissolve
    window show
    "Ни вчера, ни утром на линейке мне так и не удалось нормально рассмотреть внушительный памятник, тень от которого, казалось, с легкостью могла накрыть весь лагерь."
    "Теперь же я мог внимательно изучить его, ни от кого не спасаясь и никуда не торопясь."
    "Был он из бронзы, кое-где позеленевшей от времени, а верх покрывался толстым слоем гуано..."
    th "{b}Фу!{/b}"
    "Издали казалось, что памятник закрывает лицо рукой, будто стал свидетелем чьего-то фейла, но сейчас, стоя под самим памятником, я разглядел, что Генда всего лишь...{w} поправлял очки."
    th "Странный памятник."
    if d1_un_evening:
        th  "И кто такой Генда?{w} Ничего больше не написано под этим, так сказать, именем."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    jump d2_morning_map

label d2_event_boat_station:
    
    if been_there()>1:
        scene bg ext_boathouse_day
        with dissolve
        window show
        th "Здесь я уже был. Красиво, конечно, но нужно отвязаться от этого бегунка. Тогда я смогу пойти куда угодно."
        window hide
        $ disable_current_zone()
        jump d2_morning_map
    
    play music music_list["two_glasses_of_melancholy"] fadein 1
    play music ambience_water_stream_closer fadein 2
    scene bg ext_boathouse_day
    with dissolve
    window show
    "Приятно посидеть здесь, когда за тобой никто не гонится."
    "А место действительно было очень красивое."
    "Пристань лениво покачивалась на мелких волнах."
    "Над рекой медленно кружились чайки, изредка переговариваясь о чём-то своём — птичьем. Лёгкий ветерок приятно холодил кожу."
    #TODO: Сделать зум.
    "Я спустился к лодкам."
    "Все они были надежно привязаны цепями.{w} Так просто не покататься. А жаль."
    "Вдалеке маячили несколько островов."
    "Вернусь-ка я сюда позднее. А сейчас закончу с этим обходным листом."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    jump d2_morning_map

label d2_dv_talk:

    play music music_list["glimmering_coals"] fadein 0
    "Из-за угла вылетела чья-то рука, схватила меня за галстук и утянула за собой."
    with hpunch
    show dv smile pioneer2 close at center with dissolve
    "Спустя секунду я очутился рядом с Алисой, которая с многообещающей улыбкой притянула меня к себе и приобняла другой рукой за плечи. Не отпуская, впрочем, галстук. Её лицо оказалось в опасной близости от моего, своим телом я почувствовал её упругие, но в то же время необычайно мягкие груди."
    if d1_runaway:
        dv "Семё-ё-ё-н...{w} Ловко ты вырвался от меня прошлым утром. Не всякому это удаётся."
    "Где-то внутри открылся шлюз, и в кровеносные сосуды вырвалась стая маленьких, весёло-жгучих адреналинчиков, спешащих доложить мозгу о происходящем и привести моё главное орудие в боевое положение."
    "Причём это был отнюдь не интеллект."
    show dv grin pioneer2 close at center with dspr
    dv "Побудь со мной чуть-чуть? Я хочу кое о чём тебя спросить..."
    th "Что за кошачий голос... Ещё немножко, и я услышу в нём мурлыканье!"
    "Она отпустила галстук, и её указательный пальчик стал вырисовывать круги на моей шее."
    show dv smile pioneer2 close at center with dspr
    dv "Скрываешь от меня что-нибудь? Только не ври, Сеня."
    th "Сеня? Когда это я стал Сеней для неё?"
    "Рукой, что Алиса обнимала меня, она скользнула вниз ощупать мои карманы, хотя на долю секунды я рискнул подумать, что она коснётся совсем не карманов."
    th "И, кажется, она хватилась своих сигарет. Надо сохранить этот козырь в рукаве."
    me "Не понимаю, о чём ты... Мне скрывать нечего."
    show dv grin pioneer2 close at center with dspr
    "Она поднялась ладонью чуть выше и стала легонько поглаживать мою щёку. Какой сладкий допрос."
    dv "Темнишь, Сеня. У тебя есть то, что тебе не принадлежит. Не твоё, чужое. Ничего на ум не приходит?"
    me "Нет, в самом деле."
    dv "Да ну?"
    show dv angry pioneer2 close at center with dspr
    "Алиса усилила нажим, и я почувствовал, как в щёку впились её острые ноготки."
    dv "Тебе лучше не знать, что с тобой будет, если соврал."
    me "Я всё ещё не понимаю, о чём ты..."
    "Двачевская, сжав губы, посмотрела на меня с таким скептицизмом, что если бы его можно было измерять, все датчики бы поломались. Но вдруг её что-то заинтересовало."
    show dv smile pioneer2 close at center with dspr
    dv "А что это за листочек, с которым ты всё носишься? Дай-ка посмотреть!"
    show dv normal pioneer2 at center with dspr
    "Она выхватила у меня бланк со списком от вожатой, быстро пробежалась взглядом по нему и с погасшим интересом в глазах вернула."
    dv "Cобираешь подписи?{w} Ясно... Ну, удачи."
    me "Постой. Где у вас тут баня? Её, конечно, в списке нет, но и на карте я тоже не увидел..."
    dv "А с какой стати я буду тебе помогать? Твой листок, ты и ищи."
    show dv angry pioneer2 at center with dspr
    th "Вот же... "
    "Я разозлился."
    me "Может, в качестве извинения?! Ты меня оторвала от дела и расцарапала щёку!"
    show dv grin pioneer2 at center with dspr
    dv "Можно подумать, тебе не понравилось остальное!"
    me "{b}Я похож на мазохиста?!{/b}"
    show dv rage pioneer2 at center with dspr
    dv "{b}ДА!!!{/b}"
    with vpunch
    show dv angry pioneer2 at center with dspr
    "Я был ошарашен её атакой и не смог найти подходящих слов в пику ей. Мы молча стояли и с раздражением смотрели друг на друга."
    "Но вдруг выражение лица Алисы сменилось сначала на задумчивое, а затем на радостное."
    show dv laugh pioneer2 at center with dspr
    dv "Впрочем, извини. Пожалуйста."
    th "Что... с ней случилось? Она даже сказала «извини» и «пожалуйста»!"
    show dv smile pioneer2 at center with dspr
    dv "Я была неправа."
    "Теперь она просто светилась радостью. От этого мне стало не по себе."
    dv "Видишь ту дорогу? Баня по ней прямо и немного направо."
    "И Двачевская с гордостью удалилась."
    hide dv with dissolve
    stop music fadeout 4
    th "Ха... Можно делать засечки каждый раз после разговора с Алисой, что я уцелел. И едва устоял перед таким... напором."
    "Я мельком глянул на шорты, слегка натянутые, благодаря причинному месту."
    th "Может, Алиса заметила..."
    "С усилием я постарался не думать об этом — надо было возвращаться к делам."
    window hide
    $ d2_dv_interrogation = True
    jump d2_morning_map

label d2_decisions:

    scene black
    with dissolve
    show screen central_text("День 2 — Принимая решение")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_square_day
    with dissolve
    play music music_list["smooth_machine"] fadein 1
    window show
    "Теперь, когда я получил все подписи и обошёл кружки, можно и подумать, в какой из них записаться."
    "Все клубы по-своему интересны, но вступить я должен только в один."
    "Не исключено, что в течение смены я смогу прогулять какие-то занятия или погостить в чужом кружке."
    "И, разумеется, с одними пионерами (или пионерками!) я буду видеться чаще, чем с другими."
    "В любом случае, надо выбирать с умом."
    menu:
        "В музыкальный кружок":
            $ mus_club = True
        "В клуб юного техника":
            $ tech_club = True
        "В клуб юного моделиста":
            $ modeller_club = True
        "В клуб юного натуралиста":
            $ unnat_club = True
        "В клуб настольных игр":
            $ chess_club = True
        "В спортивный кружок":
            $ sport_club = True
        "В редколлегию стенгазеты":
            $ gazette_club = True
    th "Пока есть время до обеда, надо вернуться в кружок и записаться."
    if d1_tricked:
        "...И забрать из прачечной высохшую одежду."
    window hide
    scene black 
    with dissolve
    window show
    "..."
    "......"
    "........."
    window hide
    scene bg ext_square_day
    with dissolve
    window show
    th "Фух! Всё сделал."
    "Ольга Дмитриевна говорила, что будет или у себя в домике, или в администрации."
    if d2_met_mt:
        "А может она до сих пор отдыхает на пляже?"
    th "Что же, я просто оставлю все бумаги на столе и поскорей побегу к столовой — есть охота после такого марафона по лагерю!"
    window hide
    jump d2_dinner

label d2_dinner:

    scene bg ext_house_of_mt_day
    with dissolve
    window show
    ".................."
    window hide
    scene bg int_house_of_mt_day
    with dissolve
    window show
    show mt smile pioneer at center with dissolve
    "В домик вожатая меня пустила не сразу."
    if d2_met_mt:
        "Опять переодевалась, наверно."
        "Я тут же пожалел, что не обошёл домик, чтобы подглядеть в окно, а глупо стоял под дверью..."
    else:
        "Выглядела она подозрительно отдохнувшей."
        th "Она вообще работает или только посылает пионеров по заданиям бегать?"
    mt "Ну как, познакомился с лагерем?"
    me "Угу."
    me "Ещё как познакомился!"
    "Довольный, я протянул Ольге Дмитриевне заполненный бегунок..."
    show mt grin pioneer at center with dspr
    "А она не глядя сунула его в карман вместе с анкетой, которую я оставил на столике перед уходом."
    mt "Отлично! Скоро обед, не опаздывай."
    hide mt with dissolve
    "Вожатая ушла из домика."
    th "И ради этого я таскался целое утро с нелепой бумажкой?! Да я мог все что угодно там написать!"
    if d1_tricked:
        th "Ох..."
        play sound sfx_open_cabinet_1
        "Я раскрыл дверцу шкафа со своей половины комнаты и достал пару вешалок для джинсов и пальто, принесённых из прачечной."
        th "Интересно, доведётся ли мне вернуться домой сразу после лагеря — назад, в зимнюю Москву, в ту квартиру, которую я покинул?"
        "Ответа, к сожалению, я сейчас не знал."
        #close cabinet
        "Повесив одежду, я прилёг на кровать отдохнуть."
    else:
        "Делать было нечего, и я повалился на кровать отдохнуть."
    window hide
    stop music fadeout 3
    scene black 
    with dissolve
    window show
    ".................."
    window hide
    scene bg int_house_of_mt_day
    with dissolve
    window show
    play sound sfx_dinner_jingle_speaker
    "Cигнал на обед!"
    $ renpy.pause(1)
    th "Чёрт, я же совсем забыл о времени!"
    play music music_list["eat_some_trouble"] fadein 1
    if d1_us_chase:
        "А ведь опаздывать на обед в этом лагере чревато!"
        "То котлеты не досчитаешься, то вместо еды ядовитую гадость подсунут..."
    "Надо было спешить."
    window hide

    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 2
    window show
    if d1_us_chase:
        "На сей раз, кажется, меня никто не собирался разыгрывать. На всякий случай я сел с краю стола и придвинул к себе тарелку, внимательно изучая её содержимое. Рис. Котлета. Насекомых не видно, еда настоящая. Кажется, даже никто не сыпанул соли или перца."
        "Я вздохнул и начал есть."
        show un smile pioneer far at left with dissolve
        show dv normal pioneer far at cright
        show sl normal pioneer far at right
        with dissolve
        "Лена, как и вчера, немного опоздала и теперь мечтательно ковырялась вилкой в салате. Алиса о чём-то тихо допрашивала Славю, которая с недоумённой улыбкой отнекивалась."
        hide un with dissolve
        hide dv
        hide sl
        with dissolve
        "Внезапно моего локтя что-то коснулось и я заметил, что это Ульяна подсела ко мне со своей тарелкой и странно глядела на меня на меня."
        show us smile sport close at cright with dissolve
        us "Ну что, новенький? Где вчера после ужина пропадал? Обиделся?"
        "Почти в каждом классе обязательно есть такая мелкая, заводная, с шилом в попе девчонка, которая выбирает себе жертву на короткий срок и теребит её без конца."
        show us upset sport close at cright with dspr
        us "Я скучала..."
        th "Потеряла новую игрушку? Ну-ну."
        show us smile sport close at cright with dspr
        "Ульяна ехидно продолжила."
        us "Всю ночь плакал в подушку, небось?"
        th "Самое время возмутиться."
        show us laugh sport close at cright with dspr
        "Я приоткрыл рот для пламенной речи, но вдруг заметил кое-что интересное."
        "Она так много болтает, что даже ещё не притронулась к еде."
        th "А если наказать её за такое поведение?.."
        menu:
            "Стащить котлету" if (d2_no_shame == True):
                "Я молниеносно выхватил вилкой котлету из её тарелки и отправил в рот."
                me "М-мф!"
                th "Горячая, блин!"
                show us calml sport close at cright with dspr #TODO: исправить ошибку в наименованиях ресурсов (calm вместо calml) и переобъявить.
                us "А?!"
                th "Хе-хе. Ну вот теперь она действительно удивлена. И у меня взять уже нечего."
                "Злорадная улыбка расплылась по моему лицу."
                th "Надо сказать что-то, прежде чем она побежит жаловаться."
                me "Зачем такой маленькой девочке такая большая котлета?.."
                show us fear sport close at cright with dspr
                th "И довершающий удар."
                me "У фебя от неё софершенно ни-че-го не прибавится."
                show us angry sport close at cright with dspr
                th "Моя месть за вчерашнее свершилась. Вид Ульяны несказанно радует."
                "Но странно... Почему мне понравилось её дразнить? Утёр нос надоедливой пигалице и горд этим?"
                th "Как в детском саду, честное слово."
                hide us with dissolve
                "Ульяна же схватила тарелку и ушла к поварам, но ко мне не вернулась, а села с Двачевской, которая с улыбкой начала ей о чём-то шептать, поглядывая на меня."
                $ lp_us = lp_us + 1
            "Игнорировать":
                "Нет, пожалуй. Много чести пигалице. И проблем не оберёшься, с её-то характером."
                hide us with dissolve
                show un shy pioneer close at cright with dissolve
                "Я демонстративно взял тарелку, обошёл ряд столов и сел с другой стороны, рядом с Леной."
                show us surp1 sport at left with dissolve
                us "Ага!"
                us "Сбежал от меня к Ленке? Она тебе же нравится, да? Потому что у неё большие..."
                show us surp2 sport at left with dspr
                us "Признавайся, признавайся, признавайся!!!"
                show us fear sport at left with dspr
                show un shocked pioneer close at cright with dspr
                un "Ульяна!"
                "Голос Лены чуть-чуть дрожал. Наверное, от возмущения. Или от стеснительности, потому что Ульяна напомнила ей о внешних достоинствах?"
                "А мелкую надо поставить на место."
                me "Не твоё дело. С ней хотя бы можно спокойно поесть."
                $ lp_un = lp_un + 1
                show un surprise pioneer close at cright with dspr
                show us angry sport at left with dspr
                "Ульяна больше ничего не сказала." 
                hide us with dissolve
                "Она взяла тарелку и ушла к Двачевской за стол, которая с улыбкой начала ей о чём-то шептать, поглядывая на меня."
                show un shy pioneer close at cright with dspr
                "А Лена, густо залившись краской, отвернулась от меня и склонилась над тарелкой, не решаясь попросить у меня объяснения произошедшему."
                hide un with dissolve 
                "Ну, с Ульяной мне явно придётся столкнуться ещё не раз. Теперь она точно обижена и наверняка готовит против меня полномасштабную войну."
                "Но и я теперь знаю её больные места — возраст и ещё не развитая фигура. Бить по ним, конечно, против правил."
                "Но если она и сама рискнёт ударить меня ниже пояса, то и я смогу достойно ответить."
                th "Эх, если бы все мои проблемы исчерпывались только вознёй с «лоли»... тьфу, с девочками-подростками."
                "Здесь слово «лоли» вряд ли поймут и оценят. Особенно если читали «Лолиту»."
        stop music fadeout 1
    else:
        stop music fadeout 1
        "..."
        "......"
        "........."
    stop ambience fadeout 1
    play music music_list["lightness"] fadein 1
    show mt smile pioneer at center with dissolve
    "Когда пионеры уже почти закончили есть, а некоторые унесли пустые тарелки поварам, Ольга Дмитриевна обратилась ко всем."
    mt "Напоминаю, что после обеда положен тихий час, не разбегаемся, возвращаемся в корпуса!"
    #show bt
    "Вожатая младшего отряда вторила ей."
    bt "Я обязательно проверю всех!"
    hide mt with dissolve
    #hide bt
    th "Зато никакой беготни с обходным листом, отдыхать тоже надо. Но я распоряжусь временем так, как мне заблагорассудится."
    ".............."
    window hide
    scene black
    with dissolve
    show screen central_text("День 2 — Тихий час")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_dining_hall_away_day
    with dissolve
    window show
    "Я покинул столовую в самом хорошем расположении духа." 
    "Когда желудок полон, ты сыт, и никто не заставляет выполнять поручения, если не считать требования соблюдать тихий час, намного спокойней."
    th "Конечно, спать днём не сильно хочется, но можно остаться в домике изображать тишину. Или заняться чем-нибудь полезным."
    if chess_club:
        "Ещё староста из кружка настольных игр сказал, что Угрюмый бывает в здании клубов, когда там никого нет. Может быть, он имел в виду как раз тихий час?"
    window hide
    stop music fadeout 1
    jump d2_quiet_time_map_prep

label d2_quiet_time_map_prep:
    
    $ disable_all_zones()

    $ set_zone('clubs', 'd2_quiet_time_clubs')
    $ set_chibi("clubs",  "?")
    $ set_zone('me_mt_house', 'd2_quiet_time_me_mt_house')
    $ set_chibi("me_mt_house",  "me")
    $ set_zone('library', 'd2_quiet_time_library')
    $ set_chibi("library",  "?")
    $ set_zone('square', 'd2_quiet_time_square')
    $ set_chibi("square",  "?")
    
label d2_quiet_time_map:
    if d2_qt_places != 3:
        $ show_map() 
    else:
        jump d2_lunch

label d2_quiet_time_me_mt_house:

    $ reset_chibi("me_mt_house")
    $ disable_all_zones()
    scene bg int_house_of_mt_day
    with dissolve
    play music music_list["everyday_theme"] fadein 1
    window show
    "В домике никого не было, Ольга Дмитриевна ещё не вернулась из столовой. Или, может быть, она ушла по делам в админцентр."
    "При любом раскладе я был предоставлен самому себе."
    menu:
        "Лечь спать":
            th "Впрочем, нет ничего плохого в дневном сне. Вожатым виднее, каким должен быть режим дня у школьника в пионерском лагере."
            "Я расправил постель, снял рубашку с шортами и залез под лёгкую простыню."
            window hide
            scene black
            with dissolve
            window show
            "..."
            "......"
            "............"
            $ lp_mt = lp_mt + 1
            mt_voice "Подъём..."
            "Кто-то мягко тронул моё плечо."
            mt_voice "Подъём, Семён!..{w} Полдник через десять минут!"
            scene bg int_house_of_mt_day
            with fade
            me "А?.. Что?"
            show mt smile pioneer close at center with dissolve
            "Я заставил себя проснуться и увидел почему-то сидевшую рядом и склонившуюся надо мной вожатую со светлой улыбкой."
            th "Она что, наблюдала, как я сплю?"
            "Почему-то я резко вскочил от этой мысли."
            "Во рту даже пересохло."
            me "С-спасибо, что разбудили..."
            show mt smile pioneer at center with dspr
            mt "Одевайся и приходи в столовую."
            "Вожатая поднялась и ушла из домика."
            hide mt with dissolve
            $ d2_qt_sleep = True
            th "А сончас вещь неплохая... Усталость после обхода кружков и зарядки как рукой сняло."
            "Кое-как продрав глаза, я снова надел пионерскую форму, хоть и повязал галстук неправильно."
            th "И так сойдёт. Пора идти на полдник!"
            window hide
            stop music fadeout 1
            jump d2_lunch
        "Найти себе другое занятие" if (books_taken >0):
            call what_to_read
            play sound sfx_dinner_horn_processed
            th "Шо? Опять?"
            "С другой стороны, когда в нормальном пионерлагере кормят за просто так, зачем отказываться?"
            window hide
            stop music fadeout 1
            jump d2_lunch
            
label d2_quiet_time_square:

    $ reset_chibi("square")
    scene bg ext_square_day
    with dissolve
    play music music_list["my_daily_life"] fadein 0
    window show
    "На улице чувствовалось, как сильно греет солнце. Хотелось сразу же скрыться в тень или уйти в домик, где точно будет прохладней."
    "На площади не было пионеров, словно все уехали, и в лагере никого не осталось. Нечто похожее было вчера, когда я только прибыл сюда."
    th "Может быть, поэтому тихий час не такая уж плохая идея, ведь где-то надо пережидать эту жару."
    "Недолго я пробыл в одиночестве, просиживая штаны на лавочке в тени деревьев: на дороге от ворот к пляжу показалась вожатая младшего отряда."
    th "Лучше уйти от греха подальше, пока меня не заметили."
    window hide
    stop music fadeout 2
    $ d2_qt_places += 1
    $ disable_current_zone()
    jump d2_quiet_time_map

label d2_quiet_time_library:

    $ reset_chibi("library")
    scene bg ext_library_day
    with dissolve
    play music music_list["my_daily_life"] fadein 0
    window show
    "Вчерашние посиделки с книгой вновь доказали мне, что убивать время за чтением не менее приятно, чем перед компьютером."
    "Именно это мне сейчас и нужно было. Кто знает, когда я уеду отсюда? А дни тянутся чертовски медленно."
    scene bg int_library_day
    with dissolve
    play ambience ambience_library_day fadein 1
    "На этот раз в библиотеке стало поменьше посетителей — младших явно заставляли соблюдать тихий час.{w} Но Лены и той светловолосой девочки из нашего отряда тоже не было."
    "Женя опять спала на своём привычном месте. Видимо, у неё сончас длился с открытия библиотеки до вечера с перерывами на еду."
    th "Главное — читательский билет с собой. Не забыть бы его положить в сумку, а то потеряю ещё и буду должен выслушивать нотации от Жени."
    "Я решил не будить пионерку-библиотекаря в лишний раз и самостоятельно поискать книги."
    "Сначала я высматривал из нехудожественной литературы всё то, что как-то могло ракрыть подробности об этом мире. К сожалению, я не нашёл ни школьных, ни вузовских учебников по истории."
    "Архивных газет и журналов новостного типа тоже не было, только по интересам и увлечениям и для детей."
    "Но всё-таки мой поиск увенчался относительным успехом — я наткнулся на серию биографических книг «Жизнь замечательных людей», а биографии, как известно, неразрывно переплетены с историческими событиями и эпохами."
    th "Может, взять ещё что-то по теме занятий в кружке и лично для себя?"
    "Я двинулся мимо стеллажей с книгами."
    call take_books
    if books_taken >0:
        "Пришлось будить Женю, чтобы она выписала себе, какие книги у меня на руках."
        "Она всё сделала быстро, назначила дату возврата и снова уложила голову на руки, засыпая." 
    else:
        "По крайней мере узнал, что тут есть."
    window hide
    stop ambience fadeout 1
    stop music fadeout 2
    $ d2_qt_library = True
    $ d2_qt_places += 1
    $ disable_current_zone()
    jump d2_quiet_time_map

label d2_quiet_time_clubs:

    $ reset_chibi("clubs")
    scene bg ext_clubs_day
    with dissolve
    play music music_list["my_daily_life"] fadein 0
    window show
    th "Не могут же все пионеры без исключения послушно спать по указанию вожатых? Кто-то да сидит в кружках."
    "Я зашёл в первый корпус и попытался войти к Шурику и Сыроежкину, но помещение кружка кибернетиков было закрыто на ключ."
    "За дверью никто не говорил, звуков, даже двусмысленных, не было. Кибернетики явно отсутствовали."
    th "Хм... Наверно, заперли комнату, чтобы никто посторонний не мог прикоснуться к их трудам."
    "В коридоре, не заходя к юннатам и моделистам, я глянул в окошки двойных дверей."
    show ug normal at center with dissolve
    "Мои ожидания подтвердились: в клубе настольных игр находился всего один пионер — Угрюмый."
    "Окружённый тишиной и пылью, он читал какую-то книжечку, закинув ноги на соседний стул."
    "Пионер глянул в мою сторону, как услышал скрип входной двери, и снова вернулся к книжке."
    ug "Я ждал тебя."
    me "Зачем?"
    if chess_club:
        ug "Сказать, что ты зря записался в этот клуб."
    else:
        ug "Сказать — ты правильно сделал, что не записался в этот клуб."
    "Я прошёл к столам, между которыми устроился Угрюмый, прислонившийся спиной к стене."
    me "Почему?{w} Я слышал, ты больше не посещаешь кружок. По той же причие?"
    ug "Да. И тебе не советую.{w} В первые три дня смены я обыграл в шахматы всех участников кружка.{w} Скучно."
    ug "А отписаться нельзя, только перевестись."
    me "Всех по себе не судят. Может, кому-то интересно поучиться у своих товарищей."
    ug "Я был тут несколько дней. Не поверишь, никто не помогает друг другу."
    ug "Говорят: «Возьми книжку в библиотеке и учись!» Каждый сам за себя. Этим «товарищам» приятней играть и побеждать, а не делиться советами."
    me "А ты помогал кому-нибудь?"
    ug "Я предлагал одному пионеру, но он отказался."
    ug "Он блестяще ответил мне: «Спасение утопающего — дело рук самого утопающего». С этим я не мог не согласиться."
    ug "Но я потерял интерес ко всем остальным."
    "Угрюмый закрыл книжку — по всей видимости, шахматный учебник за авторством Симагина — и отложил её на стол."
    "..."
    "Пионер молча смотрел на меня несколько секунд, словно раздумывал, о чём поговорить." 
    "Потом он достал из нагрудного кармана сложенный пополам блокнотный лист."
    ug "Можешь найти свои ошибки?"
    "Я взял этот листочек и узнал в нём записи моей игры с тем мелким пионером."
    "Но сокращения, кроме первого хода белой пешкой с е2 на е4, не поддавались расшифровке — для меня это была сущая абракадабра, не говоря уже о том, чтобы понять, где я допустил ошибки."
    ug "Прочитать хотя бы можешь?"
    me "Нет. Я играл в шахматы очень давно, так что я на уровне начинающего и эту...{w=0.8} грамоту..."
    ug "...Шахматную нотацию."
    me "Нотацию? Да, я её совсем не знаю."
    "Угрюмый, закрыв глаза, с пониманием кивнул."
    ug "Некоторые ходы мне понравились, но они были случайными, инстинктивными. Ты не воспользовался ими для хорошей комбинации, а можно было."
    "Он встал, повёл затёкшими плечами и направился к шкафу, забитому коробками с настольными играми."
    "Угрюмый отыскал шахматную доску и принёс её ко мне на стол. Он осторожно вынул все фигуры и начал расставлять их на чёрно-белом поле."
    me "Будем играть?"
    ug "Нет, восстановим твою партию, разберём ошибки."
    "Жестом Угрюмый попросил у меня вырванные из блокнота листы и, подглядывая в них, начал с невероятной скоростью воспроизводить игру на доске."
    "Я едва поспевал разглядеть движения его руки."
    "Пешка за пешкой, фигура за фигурой, одни на доске, другие — побитые — на стол. В несколько секунд он разыграл начало моей партии, пока не остановился."
    ug "Ошибка первая: здесь ты прозевал слона."
    "Он показательно сменил названную фигуру чёрным конём."
    me "Я это помню, я тогда сразу понял, что неправильно сходил, но было поздно."
    "Пионер вернул слона и коня на исходные клетки."
    ug "А как надо было пойти?"
    "Я уставился на доску, пытаясь заново уяснить, что мне угрожает и какой ход в сложившейся ситуации будет верным." 
    th "Рокировка не сделана, белые фигуры в центре уступают чёрным. Как найти выход?"
    "Чем дольше я думал, тем ясней становилось, что мне не под силу предугадать, как поведёт себя в ответ воображаемый оппонент."
    th "Блин!"
    th "Допустим, этого слона стоило защитить."
    "Я переставил пешку."
    ug "Мотив, мотив, мотив?!{w=0.7} Объясняй."
    th "Я снова неправильно сходил, что ли?" 
    me "Э-э..."
    ug "Если не знаешь, зачем был сделан ход — это игра наугад."
    me "Защитил слона."
    ug "Хорошо."
    "Он всё равно съел конём эту фигуру, невзирая на пешку, защищавшую поле."
    ug "Это размен, его не стоит бояться, если вдруг тебе придётся быть на моём месте, только смотри, чтобы поля не остались ослабленными."
    ug "Мотив должен был быть другим: не дать сопернику развить фигуры в центре, но вывести вперёд свои, подготовить защиту.{w} Сейчас через два хода тебе нужно сделать рокировку или один из пяти альтернативных ходов, смотря как пойдёт игрок за чёрных."
    th "Мне намекают, что я должен был просчитывать игру на пять шагов вперёд?"
    "Он вернул фигуры и продолжил разыгрывать наши с мелким пионером ходы, всё реже заглядывая в листы, словно выучил наизусть, как заканчивается партия."
    ug "Ещё ошибка. Я бы сказал, самая главная. Видишь?"
    me "Последний ход — ладья на f5. Почему это неправильно? Я же отступил, чтобы её не побил ферзь или пешка."
    ug "Да, я говорил про ладью. Правильно было сходить именно ею, но по-другому."
    me "Но куда? Тут её тоже побьют, а тут я потеряю возможность обойти защиту короля и шаховать его."
    ug "Подумай."
    "..."
    me "Не понимаю. Сдаюсь, потому что не вижу, куда ставить ладью. Может, надо вообще другой фигурой пойти?"
    ug "Нет."
    "Он взял ладью и переместил на две клетки влево, подставив её под удар другой пешки."
    ug "Жертва."
    ug "Твоей ошибкой была мысль, что тяжёлую фигуру надо беречь всегда. Бывают ситуации, когда жертва значительно улучшает позицию."
    ug "Рушим защиту короля, отвлекаем вражеские фигуры, открываем направления для ударов фигур слева или позади — и всё это с помощью жертвы.{w} Интереснее всего — выманить короля противника на поле, но... В твоей игре не сложилось ничего для впечатляющей комбинации, потому что ты не захотел."
    ug "Ты топтался на месте, а можно было рискнуть и усложнить игру."
    "Угрюмый сделал несколько ходов, не объясняя их, пока не продемонстрировал мне мат чёрному королю, если бы я отдал ладью."
    "Теперь он замолчал, и я подумал, что выигрышное решение принесло ему куда больше удовольствия, чем мне. Угрюмый просто был слишком увлечён этой игрой, настолько, что разобрал партию, в которой не принимал участия."
    "Удивительно, как мало времени ему понадобилось, чтобы рассмотреть все ходы и мои ошибки!"
    "Пионер аккуратно снёс фигуры, перевернул доску и начал складывать их обратно."
    ug "Забирай на память."
    "Он отдал мне запись игры."
    me "Возможно, шахматы — просто не моё."
    ug "Это поспешный вывод. Ты ведь, считай, даже не начинал в них играть, так, попробовал несколько раз."
    me "А я и не собирался становиться профессиональным шахматистом."
    ug "..."
    "Угрюмый отнёс закрытую доску к шкафу и положил её на полку."
    ug "Кстати, староста кружка пытался разыграть с тобой что-то похожее на недавнюю партию двух известных гроссмейстеров, подсмотренную им в майском номере журнала «Шахматы в СССР», я сразу понял это по дебюту и манёврам в середине игры."
    ug "Ха." 
    ug "Глупая затея, ведь ты играл по-своему, не копируя чьих-то приёмов." 
    ug "Но не провоцировал соперника разумным образом и сам не рисковал. Не делал сильных ходов, не создал интересной ситуации."
    me "Конечно, я же не чемпион мира по шахматам! Чего ещё от меня можно было ожидать?"
    "Угрюмый отвернулся к окну и застыл, глядя на безлюдную аллею и дорожку к музыкальному клубу."
    ug "Чемпионы мира тоже ошибаются..."
    "Я ничего не ответил ему."
    ug "Хочешь, научу играть?"
    menu: 
        "Моя душа не лежит к шахматам":
            me "Боюсь, мне это неинтересно."
            me "Нет смысла заниматься чем-то из-под палки или через силу."
            "Он повернулся ко мне." 
            if chess_club:
                ug "Тебя никто не заставляет, кроме того, что если состоишь в кружке, ты должен принять участие в турнире с пионерами в День Шахмат. Это двадцатого числа, то есть, через пару дней."
                th "Вот это я попал!"
                me "Что?! И отписаться нельзя?"
                ug "Нельзя.{w} Нет, конечно, ты можешь пойти в админцентр к вожатым и побить чел{i}о{/i}м, чтобы перевели в другой кружок.{w} Наверно.{w} Я не делал этого."
                me "Ты собираешься играть на турнире?"
                ug "Да, чтобы не дать уму расслабиться, хоть это и будет невыносимо скучно для меня..."
                me "Сомневаюсь, что за два дня я смогу сравниться хоть с кем-то из кружка."
                ug "Я потому и предлагаю натаскать тебя по основам игры, а там смотри сам, интересно тебе это или нет."
                me "Ну, тебе я точно проиграю, без вопросов."
                ug "Не попробуешь, не узнаешь. Бывало, наши городские пионеры обыгрывали гроссмейстеров на показательных встречах."
                me "Тем более! Если шахматистов обыгрывают, то и меня подавно."
                "Его губы чуть дёрнулись, но он заставил себя подавить улыбку."
                ug "Посмотри на себя. Ты пионер?{w=0.5} Да.{w=0.5} У вас равные шансы."
                ug "Короче, будет желание, подходи. Сегодня я свободен после полдника."
                me "..."
                me "Хорошо."
                "Но на самом деле я точно не определился с решением. В клубе помимо шахмат есть ещё куча игр, так что я либо буду играть со всеми, либо без зазрения совести прогуливать."
                $ d2_chess_decision = True
            else:
                ug "Нет проблем. Я знаю, что ты не стал записываться, поэтому в твоём отказе нет ничего удивительного."
        "Спасение утопающего — дело рук самого утопающего":
            me "Ну, если я сам не попрошу помочь — никто не поможет?{w} Я не против скоротать время за игрой." 
            if chess_club:
                ug "И ещё тебя ждёт турнир двадцатого числа в честь международного Дня Шахмат. Если состоишь в кружке, то надо принять участие."
                me "И я должен подготовиться за двое суток? Impossibru!"
                ug "Конечно, ты можешь пойти в админцентр к вожатым и побить чел{i}о{/i}м, чтобы перевели в другой кружок.{w} Наверно.{w} Я не делал этого."
                ug "Не беспокойся, я научу тебя основам, и в турнире нет ничего страшного, не на деньги же играем."
                me "Да, это очень утешает."
            me "Когда к тебе можно будет подойти?"
            ug "Здесь в тихий час или на занятиях клуба моделистов. Но чаще я бываю на свежем воздухе, где-нибудь подальше от суеты."
            if chess_club:
                ug "И раз уж ты согласился на помощь, я поставлю одно условие."
                th "Условие?"
                "Он поднял указательный палец."
                ug "Никогда больше не посещай этот кружок. День турнира не считается."
                me "Это нетрудно, хорошо."
                ug "Договорились."
            ug "Сегодня я буду свободен после полдника."
            $ d2_chess_agreement = True 
            me "..."
            me "Хорошо."
    "Угрюмый взял недочитанную им книгу и снова устроился на стульях между партами."
    "Не подыскивая слов для прощания, я ушёл из клуба настольных игр."
    window hide
    stop music fadeout 2
    $ d2_met_ug = True
    $ d2_qt_places += 1
    $ disable_current_zone()
    jump d2_quiet_time_map
 
label d2_lunch:

    if (d2_qt_places == 3):
        play sound sfx_dinner_horn_processed
        "Прозвучал сигнал на полдник."
        th "Странно, однако я всё ещё чувствую себя сытым после обеда. Хорошо тут кормят!"
        "И тем не менее, хотелось быстро прохватить чего-нибудь, вроде чая."
        "Пребывая в хорошем настроении, я отложил все свои дела и отправился к столовой."
        window hide
    else:
        pass
    scene black
    with dissolve
    show screen central_text("День 2 — Полдник")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_dining_hall_near_day
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    window show
    "К столовой я пришёл не первым, но и не последним."
    show mt normal pioneer at center with dissolve
    "Ольга Дмитриевна уже была тут — как всегда следила за порядком в очереди из пионеров и ждала опаздывающих."
    if (d2_qt_places == 3):
        show mt angry pioneer at center with dspr
        mt "Где ты пропадал, Семён? Почему не был в палате, когда у всех тихий час?"
        "Вожатая была сердита, но не зла на меня."
        "Кажется, я легко отделаюсь..."
        me "Не переживайте, Ольга Дмитриевна, я был в здании кружков, никого не трогал, вёл себя тише воды и ниже травы. Это ведь не преступление?"
        show mt surprise pioneer at center with dspr
        mt "Нет, но порядок надо соблюдать! Если хочешь уйти куда-то в режимное время, сначала спроси разрешения."
        me "А сопровождение будет? Шаг влево или вправо по пути в туалет считаются за попытку побега?"
        show mt grin pioneer at center with dspr
        mt "Так, шутник, сопроводи уже себя на полдник, и не отвлекай вожатую."
        "Она легонько подтолкнула меня к порогу столовой, и я влился в очередь пионеров."
        hide mt with dissolve
        "С этой болтовнёй я и забыл, что хотел взять еду и снова прогуляться по лагерю."
        "Но я не имел ничего против мысли, чтобы меня сопровождала или даже охраняла симпатичная девушка."
    elif d2_qt_sleep:
        show mt smile pioneer at center with dspr
        "Вожатая наверняка была довольна тем, что я остался в домике, как ожидалось от порядочного пионера, хотя ещё вчера я размышлял, будто мне плевать на все лагерные правила."
        mt "Всегда приходи вовремя, как сегодня!"
        me "Это всё потому, что вы меня разбудили, Ольга Дмитриевна. Сам я бы обязательно проспал."
        show mt surprise pioneer at center with dspr
        mt "Тогда ставь будильник, не могу же я вечно заставлять тебя просыпаться? Вот именно."
        th "Ох, если бы!.."
        show mt grin pioneer at center with dspr
        mt "Приятного аппетита, Семён!"
        "Голос вожатой привёл меня в чувство, и я прошёл в столовую следом за пионерами."
        hide mt with dissolve
    else:
        "Я прошёл мимо неё, спеша на полдник."
    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 5
    mz_voice "Подожди, Семён!"
    show mz normal glasses pioneer at center with dissolve
    "Меня остановила не вожатая, а Женя."
    me "Да?"
    "Я взял с подноса кружку компота и яблоко из алюминиевого таза."
    show mz bukal glasses pioneer at center with dspr
    mz "Как пополдничаешь, приходи в библиотеку — поможешь книги разобрать."
    me "Опять?"
    me "Слушай, у вас что, кто-то специально ходит и разбрасывает книги? Вот этого пионера и накажите, заставьте наводить порядок."
    "Мой словесный выпад не произвёл на Женю никакого впечатления."
    show mz normal glasses pioneer at center with dspr
    mz "Те книги, убранные тобой, мне вернули после недельного срока, а сейчас я прошу помочь с теми, что привезли в коробках на автобусе, на котором ты приехал."
    "Я весь обратился в слух."
    me "На автобусе? Как это связано?"
    show mz bukal glasses pioneer at center with dspr
    mz "Так, что автобус ездит от института, за которым числится наш лагерь."
    th "Сомневаюсь... Я всё ещё хорошо помню вечер, когда решил пойти в «Макдональдс»."
    mz "...Ольга Дмитриевна звонила в деканат и просила отправить пару комплектов новых книг для библиотеки."
    show mz normal glasses pioneer at center with dspr
    mz "Я не хочу отрывать от дел ребят из редколлегии."
    if gazette_club:
        mz "А ты пока не занят."
        th "Вдруг это прольёт хоть какой-то свет на моё путешествие из будущего?"
        me "Ладно, так и быть, помогу."
        th "Всё равно мне надо идти в библиотеку на занятие кружка."
        $ d2_mz_help = True
        mz "Буду ждать, Семён."
        "Она ушла с полдником на свободное место за столом рядом со Славей."
        hide mz with dissolve
    else:
        th "Может, помочь ей?"
        menu:
            "Занятия в кружках подождут":
                me "Хорошо, я приду. Только, чур, ненадолго, мне ещё хотелось бы посетить свой кружок, раз туда записался."
                "Жене такого ответа было достаточно, и она сдержанно кивнула."
                mz "Буду ждать, Семён."
                "Она ушла с полдником на свободное место за столом рядом со Славей."
                hide mz with dissolve
                th "Вдруг это прольёт хоть какой-то свет на моё путешествие из будущего?"
                "Надежда была откровенно слабой, но всё же я не мог оставаться равнодушным к этой загадке."
                $ d2_mz_help = True
            "Пусть она попросит кого-нибудь другого":
                me "Извини, но я не смогу, попроси кого-то другого помочь тебе."
                "Пионерка восприняла мой отказ спокойно."
                mz "Поняла."
                "Закончив на этом, она взяла свой полдник и присоединилась к Славе за столом."
                hide mz with dissolve
    "С кружкой компота и яблоком в руках я оглядел столовую и выбрал себе место."
    show el smile pioneer close at left with dissolve
    show sh normal pioneer close at right with dissolve
    "Насладиться едой в одиночестве не удалось — через пару минут ко мне подсели Шурик с Электроником."
    if tech_club:
        el "Ну что, Семён, готов к погружению в кибернетику с головой?"
        me "Знаете, после сегодняшнего утра я уже как-то опасаюсь говорить «Всегда готов»."
        show el surprise pioneer close at left with dspr
        show sh surprise pioneer close at right with dspr
        el "А что утром-то было?"
        th "Он ещё спрашивает! Ладно, Сыроежкин не понимает, что мне довелось испытать."
        "Я отмахнулся."
        me "Всё, проехали."
        show el normal pioneer close at left with dspr
        show sh normal pioneer close at right with dspr
        sh "Семён, мы, конечно, записали тебя, но давай определим, кто с чем будет работать. Занимался когда-нибудь роботостроением?"
        me "Нет..."
        th "Вряд ли можно сказать, что у меня вообще было хобби или достойное увлечение, помимо банального чтения и компьютерных игр."
        show sh serious pioneer close at right with dspr
        sh "Тогда тебе придётся взять пару книжек из библиотеки, плюс почитать те, что уже есть у нас. Охвати всё, что касается элементарных комплектующих для робота и конструирования зубчатых передач. И про бионику не забудь."
        show el laugh pioneer close at left with dspr
        el "Одним чтением не обойдёшься! Практика тоже понадобится. Я расскажу и покажу тебе, как паять..."
        show el smile pioneer close at left with dspr
        "Он прервался, чтобы отгрызть кусок от яблока и запить компотом — разговор явно мешал ему подкрепиться, ради чего Сыроежкин пришёл в столовую."
        show sh normal pioneer close at right with dspr
        sh "Семён, начни с основ, поможешь нам ускорить работу, потому что Серёга вплотную займётся моторной частью и тепловыделением."
        me "А ты что делаешь?"
        show sh normal_smile pioneer close at right with dspr
        sh "Я тоже прикладываю руку к сборке робота, но в основном я программирую."
        show sh normal pioneer at cright with dspr
        "Шурик поднялся из-за стола, оставив пустой стакан, а недоеденное яблоко прихватил с собой."
        sh "Пора, идём в кружок, будет проще, если мы объясним тебе всё на месте..."
        if d2_mz_help:
            me "Я забыл сказать, что я обещал Жене помочь с книгами в библиотеке, так что я подойду немного позже, ладно?"
            show el shocked pioneer close at left with dspr
            "Вдруг Сыроежкин нервно дёрнулся."
            el "Шурик, знаешь, сегодня можно сделать небольшой перерыв, ничего важного по роботу я не планировал, так что..."
            show sh scared pioneer at cright with dspr
            sh "Куда ты собрался?"
            show el upset pioneer close at left with dspr
            el "В библиотеку, составлю компанию Семёну..."
            show sh surprise pioneer at cright with dspr
            sh "Нет, у нас каждый час на счету. Никаких библиотек!"
            show el sad pioneer at cleft with dspr
            show sh normal pioneer at cright with dspr
            sh "Семён, ты не задерживайся, приходи скорей."
            show el serious pioneer at cleft with dspr
            el "Смотри, не забудь!"
            show el laugh pioneer at cleft with dspr
            "Электроник козырнул мне напоследок, и кибернетики ушли."
            hide el 
            hide sh
            with dissolve
            "......"
            "Скоро вслед за ними я опустошил стакан компота и вышел на улицу."
            jump d2_gazette_club_day
        else:
            me "Да, конечно."
            show el smile pioneer at cleft with dspr
            "Свой компот я не стал допивать, но яблоко забрал — оно оказалось невероятно вкусным. Сыроежкин, уходя с нами, свистнул из общего таза с фруктами себе ещё одно яблоко."
            window hide
            stop ambience fadeout 1
            scene black
            with dissolve
            window show
            "Из-за того, что Шурик торопился, к зданию клубов мы пошли ускоренным шагом."
            "........."
            window hide
            stop music fadeout 2
            jump d2_tech_club_day
    else:
        show el sad pioneer close at left with dspr
        el "Очень жаль, что ты не записался к нам."
        me "Ты не думал, что кибернетика просто может быть неинтересна мне?"
        show el serious pioneer close at left with dspr
        el "Так и знай: если мы не успеем закончить робота ко Дню творческой самодеятельности — это останется на твоей совести."
        el "Шурик, значит, Семёна мы больше не пускаем в лабораторию?"
        th "Лабораторию? Они мнят себя безумными учёными?"
        show sh serious pioneer close at right with dspr
        sh "Нет, Серёг, Славя права, кружки общие."
        show sh surprise pioneer close at right with dspr
        sh "Семён, если хочешь, заходи, только стучись, ладно?"
        th "О да, после сегодняшнего я обязательно буду стучаться."
        "Я пожал плечами."
        me "Нет проблем."
        show el normal pioneer close at left with dspr
        show sh normal pioneer close at right with dspr
        el "Ну, тогда чтобы мы могли отличить тебя от других пионеров, стучись на морзянке, кодовое\nслово — «ЭШ»: точка, точка, тире, точка, точка, тире, тире, тире, тире. Запомнил?"
        me "Считай, что запомнил."
        show sh normal_smile pioneer close at right with dspr
        sh "Нет, Серёга, морзянка — это прошлый век... Даже позапрошлый. Почему бы нам не собрать домофон?"
        show el smile pioneer close at left with dspr
        el "Во, тоже вариант."
        th "Похоже, эти парни будут делать всё, что угодно, только не робота..."
        hide el
        hide sh
        with dissolve
        "Я тихонько встал из-за, чтобы не мешать разговорившимся кибернетикам о перспективах «изобретения» домофона и даже электронного замка для двери кружка юного техника."
        window hide
        stop ambience fadeout 1
        scene bg ext_dining_hall_near_day
        with dissolve
        window show
        "Ближайшие пару часов я точно проведу не с ними."
        window hide
        stop music fadeout 1
    jump d2_day_map_prep

label d2_day_map_prep:
    
    $ disable_all_zones()
           
    $ set_zone('sport_area', 'd2_sport_club_day')
    $ set_chibi("sport_area",  "us")
    $ set_zone('library', 'd2_gazette_club_day')
    #$ set_chibi("library",  "mz") TODO: сделать возможность выводить до 4х чибиков на одну локацию одновременно. (%локация_нейм%, "%чиби1%", "%чиби2%") на данный момент выдаёт ошибку, что приводятся лишние arguments.
    $ set_chibi("library",  "un")
    $ set_zone('clubs', 'd2_clubs_day')
    #$ set_chibi("clubs",  "el")
    #$ set_chibi("clubs",  "sh")
    $ set_chibi("clubs",  "sl")
    $ set_zone('music_club', 'd2_musclub_day')
    $ set_chibi("music_club",  "mi")
    
    $ set_zone('estrade', 'd2_green_theatre_day')
    $ set_chibi("estrade",  "?")
    $ set_zone('beach', 'd2_beach_day')
    $ set_chibi("beach",  "?")
    $ set_zone('boat_station', 'd2_boat_station_day')
    $ set_chibi("boat_station",  "?")
    $ set_zone('square', 'd2_square_day')
    $ set_zone('medic_house', 'd2_aidpost_day')
    $ set_zone('forest', 'd2_forest_day')
    $ set_zone('me_mt_house', 'd2_me_mt_house_day')
    #$ set_chibi("me_mt_house",  "me")
    $ set_chibi("me_mt_house",  "mt")
    #TODO: необходима позиция admin_center, создать новую точку на карте в globals.rpy
    
    jump d2_day_map
    
label d2_day_map:
    
    if d2_day_places == 1:
        #$ disable_all_zones()
        $ reset_zone('sport_area')
        $ reset_zone('library')
        $ reset_zone('clubs')
        $ reset_zone('music_club')
        
        if been_there == 0:
            $ set_zone('estrade', 'd2_green_theatre_day') 
        if been_there == 0:
            $ set_zone('beach', 'd2_beach_day')
        if been_there == 0:
            $ set_zone('boat_station', 'd2_boat_station_day')
        if been_there == 0:
            $ set_zone('square', 'd2_square_day')
        if been_there == 0:
            $ set_zone('medic_house', 'd2_aidpost_day')
        if been_there == 0:
            $ set_zone('forest', 'd2_forest_day')
        if been_there == 0:
            $ set_zone('me_mt_house', 'd2_me_mt_house_day')
    
    if d2_day_places != 3:
        $ show_map() 
    else:
        window show
        "..."
        "......"
        "Но мне больше помаяться по лагерю не удалось — вскоре прозвучал сигнал на ужин."
        window hide
        jump d2_pre_event

label d2_tech_club_day:

    scene black
    with dissolve
    show screen central_text("День 2 — Горькая правда")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg int_clubs_male_day
    with fade
    $ disable_current_zone()
    play music music_list["two_glasses_of_melancholy"] fadein 2
    play ambience ambience_clubs_inside_day fadein 1
    window show
    "В третий раз за день я очутился в помещении кружка кибернетиков."
    "Беспорядок с рабочего стола юных техников никуда не делся, а вот робота я не обнаружил."
    scene bg int_clubs_male2_night
    with dissolve
    show el normal pioneer far at cright with dissolve
    "Вопрос разрешился сам собой. Электроник первым делом зашёл в подсобку и включил там свет, так что я смог разглядеть всяческий хлам, пару столов и телевизор с видеомагнитофоном."
    "Сыроежкин отодвинул клеёнчатую занавесь, скрывавшую нишу в шкафу у дальней стены, и извлёк на божий свет девушку-робота."
    show el shocked pioneer far at cright with dspr
    el "Шурик, помоги!"
    sh "Иду!"
    show el scared pioneer far at cright with dspr
    show sh upset pioneer far at center with dissolve
    "Пионер в очках немедленно подбежал к Сыроежкину и подхватил металлическую конструкцию за ноги."
    scene bg int_clubs_male_day
    with dissolve
    show el normal pioneer at cleft with dissolve
    show sh normal pioneer at cright with dissolve
    "Вместе они с такой осторожностью вынесли её в комнату и уложили на стол, словно это был не робот, а раненый человек, которому срочно требовалась операция."
    me "Вы обещали рассказать, почему у неё кошачьи уши."
    show sh surprise pioneer at cright with dspr
    sh "Дело в том, что по лагерю гуляет байка, будто в окрестных лесах живёт девочка с ушами и хвостом, как у кошки. В прошлом году её видел кто-то из пионеров. Он клялся, что не врёт, но ему мало кто поверил, и доказательств не было."
    me "А вы сами верите?"
    show sh serious pioneer at cright with dspr
    sh "Я допускаю, что это может быть правдой. Мы уже давно сосуществуем с гибридами людей и животных. Тот пионер вполне мог обнаружить новый вид..."
    with vpunch
    me "!.."
    "Увлёкшийся рассказом Шурик не заметил, как сильно я удивился."
    show sh normal_smile pioneer at cright with dspr
    sh "Но даже если тот пионер всё выдумал, мы можем сделать легенду реальной — построим этого робота."
    show el smile pioneer at cleft with dspr
    el "Мы придумывали возможные предыстории для нашей девочки, чтобы представить её на Дне творческой самодеятельности. Выбирали имя, роль, сочиняли реплики, которые она сможет произнести о себе."
    show el laugh pioneer at cleft with dspr
    el "Я хотел, чтобы она была роботом-служанкой в очках, нашей подругой детства и одноклассницей, гением-вундеркиндом и путешественницей во времени, но скоропостижно скончавшейся от неизлечимой болезни, и чтобы её дух был заключён в эти металлические доспехи..."
    show sh upset pioneer at cright with dspr
    sh "...А я сказал, что его идеи глубоко вторичны."
    show el shocked pioneer at cleft with dspr
    el "Но людям нравятся штампы! Мозг цепляется за легко узнаваемые образы и ситуации, которые заставляют улыбаться или сопереживать в нужный момент!"
    show el serious pioneer at cleft with dspr
    el "Это психология, Шурик! Не будешь же ты спорить с психологией?"
    show sh scared pioneer at cright with dspr
    sh "Сколько людей, столько и мнений!"
    el "Понятие массовой культуры вообще говорит тебе о чём-нибудь?!"
    show sh rage pioneer at cright with dspr
    sh "А миллионы мух не могут ошибаться?"
    th "О нет, лучше бы они спорили о внешности пионерок, всё лучше, чем это."
    me "Ну, так на чём вы сошлись?"
    show el sad pioneer at cleft with dspr
    show sh upset pioneer at cright with dspr
    "Кибернетики разом перестали ругаться."
    sh "Ох...{w} Я предложил Серёге остановиться на роботе-служанке, а потом сам ещё вспомнил ту легенду о девочке-кошке."
    show el smile pioneer at cleft with dspr
    el "И я одобрил его решение."
    show sh normal pioneer at cright with dspr
    me "Не понимаю, как вы собираетесь заставить робота танцевать."
    show el grin pioneer at cleft with dspr
    el "Всё благодаря синтетическим мышцам. Подожди, сейчас принесу."
    hide el with dissolve
    "Он снова ушёл в подсобку и вернулся с целым пучком кабелей-шлейфов цвета сырого мяса."
    show el smile pioneer at cleft with dissolve
    "Они были переплетены вместе и повторяли анатомическое строение мышц человеческой конечности."
    "Сыроежкин подтвердил мои догадки."
    show el laugh pioneer at cleft with dspr
    el "Это её будущая правая рука. Электроток воздействует на отдельные участки полимерной цепи, и мышцы сокращаются."
    me "Круто."
    th "Откуда они достали такое?"
    me "Как вы сделаете робота похожим на человека?"
    show el sad pioneer at cleft with dspr
    show sh upset pioneer at cright with dspr
    "Шурик и Сыроежкин переглянулись."
    sh "Скажешь ему?"
    show el upset pioneer at cleft with dspr
    el "Придётся, раз он с нами."
    show el shocked pioneer at cleft with dspr
    el "Я немножко приврал, когда сказал, что у нас есть всё для полноценной сборки. Короче, нужна искусственная кожа и оболочка с микроэлектроникой под неё. Понимаешь, я не думал, что закончу робота до осени, и оставил их в городе, всё привезти сюда мне было бы тяжело."
    show el normal pioneer at cleft with dspr
    show sh normal pioneer at cright with dspr
    sh "Пока мы будем делать робота из имеющихся в нашем распоряжении деталей."
    me "Секундочку, а программный код? На чём он пишется? Си, ассемблер?"
    "Шурик ответил, и я понял, что никогда не слышал о названном языке и уж тем более никогда не видел его."
    "Раз в этом мире уже много различий по сравнению с моим, то почему бы здесь не существовать абсолютно уникальным разработкам в области техники и программирования?"
    th "Вот тут я точно могу сказать, что не боюсь чего-то нового."
    me "Интересно. Покажете?"
    show sh normal_smile pioneer at cright with dspr
    sh "Конечно."
    show sh serious pioneer at fright with dspr
    show el smile pioneer at center with dspr
    "Он включил настольный компьютер, подождал появления экрана мультизагрузки и выбрал одну из двух предустановленных операционных систем."
    th "Дуалбу{font=fonts/DejaVuSansMono.ttf}~{/font}т!.."
    "Как только появился рабочий стол, Шурик сразу запустил нужную программу и открыл в ней последний изменённый документ."
    "Я наклонился к монитору, вглядываясь в бледно-серое окошко, разбитое на несколько фреймов-полей для работы с кодом."
    "Через несколько секунд машинных раздумий на белом фоне отобразился текст, и Шурик стал неспешно проматывать его."
    show sh surprise pioneer at fright with dspr
    sh "Вот, собственно, оно."
    show sh normal pioneer at fright with dspr
    sh "В основе лежит синтаксис пары других языков, зная которые, сможешь понять и остальное в коде, не считая машинного."
    show el laugh pioneer at center with dspr
    el "Если тебя интересует, почему именно этот язык, то отвечу: он не является общим для разных платформ, его нельзя применить для нового робота с другой технической начинкой."
    me "Вы что, сами всё это написали?" 
    show el sad pioneer at center with dspr
    show sh upset pioneer at fright with dspr
    "Сыроежкин вздохнул, собираясь в чём-то признаться."
    show el upset pioneer at center with dspr
    el "Хорошо, Семён. Давай будем честными, мы никогда не смогли бы собрать робота с нуля и написать для него такой сложный код за короткое время. За нас это много лет делали те люди, которые создали моего двойника, а потом и производную от него женскую модель."
    el "Я одолжил у них разобранный тестовый образец Электронички и несколько внешних жёстких дисков с исходным кодом и необходимыми программами."
    show el normal pioneer at center with dspr
    el "Нам остаётся только достроить собственную модель андроида и внести некоторые изменения в код."
    "Моё разочарование сложно было передать словами."
    me "То есть, вы пришли на готовенькое? А я-то думал..."
    show sh surprise pioneer at fright with dspr
    sh "Ну, не скажи. Чтобы собрать робота по инструкции из тематического журнала, тебе всё равно пришлось бы идти в магазин и покупать готовые комплектующие. Серёга уже объяснил про титанический труд, затраченный на код."
    show el smile pioneer at center with dspr
    el "Да, правда часто бывает неприятной. А иначе не будет ничего: ни танцев, ни фокусов, ни удивительной девочки-кошки. Мы знаем секрет, а остальные ребята — нет. Устроим для них праздник, сказку."
    "В его словах был смысл. Подобные развлечения создаются кем-то для кого-то. Вроде кино: то, что для зрителя «магия» — для съёмочной команды обычная рутина. С другой стороны, творческий процесс крайне интересен для всех участвующих, если они по-настоящему любят своё дело."
    show sh normal_smile pioneer at fright with dspr
    sh "Мне нравится думать об этом как о сложном конструкторе. Нам втроём придётся собрать то, что в своё время сделали двенадцать человек."
    show el laugh pioneer at center with dspr
    el "Тем более, я всегда хотел смонтировать робота сам, даже если он спроектирован кем-то другим."
    stop music fadeout 2
    "Я кивнул."
    play music music_list["i_want_to_play"] fadein 2
    me "Хорошо, вы убедили меня.{w} Расскажите, что мы будем делать, начиная с сегодняшнего дня?"
    show el smile pioneer at center with dspr
    el "Мы собираемся задать роботу определённую поведенческую роль и подчинить ручному управлению на расстоянии. Изначально код рассчитывался на полную самостоятельность робота и обретение им личности. Это самообучающийся искусственный интеллект."
    show sh normal pioneer at fright with dspr
    sh "А мы должны поставить робота в зависимость от роли, чтобы она обращалась только к тем знаниям, которые нужны для выступления."
    show el serious pioneer at center with dspr
    el "Если мы не ограничим её, то она сама будет расставлять приоритеты, и вместо танцев и разливания напитков ей больше будет интересно проверить все возникающие в электронном разуме суждения, разрешить экзистенциальные вопросы и так далее."
    el "У нас, к сожалению, нет времени на социальную адаптацию девочки-робота среди пионеров, чтобы с ней можно было договориться, как с человеком. Придётся объяснять, для чего мы в пионерском лагере, что такое День творческой самодеятельности."
    el "При этом часть кода, отвечающего за нейросети, работает как часы. Мы её своими грязными ручками не трогаем."
    show el smile pioneer at center with dspr
    el "Общую проблему понял?"
    me "Да."
    el "Это всё регулируется в коде, им занимается Шурик. Я припаиваю микросхемы к платам и монтирую различные детали. Шурик часто помогает мне с этим."
    if d2_mz_help:
        el "Сегодня утром мы прикручивали амортизацию к внутренней конструкции ног робота, а пока ты был в библиотеке, я припаял модуль гироскопа к плате."
    else:
        el "Сегодня утром мы прикручивали амортизацию к внутренней конструкции ног робота, а сейчас я буду припаивать гироскоп к плате." 
    show el normal pioneer at center with dspr
    el "Двигательный анализатор с микроэлектроникой и гироскоп вместе для робота как нервная система и вестибулярный аппарат человека. Вот такое грубое анатомическое сравнение."
    show sh serious pioneer at fright with dspr
    sh "Да покажи ты ему, зачем рассказываешь."
    show el smile pioneer at left
    show sh serious pioneer at right
    with dissolve
    "Сыроежкин, обойдя стол, предложил мне поглядеть, как разбирать робота."
    "Сначала пионер отсоединил грудную пластину, и я увидел несколько плат и пару блоков, зажатых в салазках, как жёсткие диски. Располагались эти блоки симметрично, там же, где у человека находятся лёгкие."
    show el laugh pioneer at left with dspr
    el "Справа аккумулятор. У предыдущей модели было напряжение в сто десять вольт, у этой — двести двадцать." 
    "И в самом деле, в основании блока под ручкой, за которую он вытягивался из паза, торчал шнур с вилкой, скрученный несколько раз и стянутый резинкой."
    el "Слева самая главная часть робота — её мозг."
    show sh normal pioneer at right with dspr
    sh "Там основное хранилище памяти, процессор и двигательный анализатор. Это микрокомпьютер, в него мы загрузим исправленный код."
    show sh serious pioneer at right with dspr
    sh "Мы в принципе не имеем права на ошибку в коде. Для комплексной отладки такого объёма данных нужна большая специализированная ЭВМ. У нас есть средство отладки только для отдельных частей кода на предмет синтаксиса."
    me "Как же вы тогда пишете? Неужели настолько хорошо знаете язык?"
    show sh surprise pioneer at right with dspr
    sh "У нас есть учебная книжка, возьми её, почитай на досуге, если тоже хочешь внести свой вклад в программирование робота."
    show sh normal pioneer at right with dspr
    "Он выдвинул самый нижний ящик стола и достал увесистый том учебника с мягкой белой обложкой. Вместо издательства была указана типография Института кибернетики."
    $ books['От Эла и Шурика'] = {'language_manual' : Book('Учебник из Института кибернетики', 12, {1 : '..." "......" "Интересно... Язык немного напоминает Python." ".........', 2 : '..." "......" "Level up: знание языка программирования." ".........', 3 : '..." "......" ".........', 4 : '..." "......" ".........', 5 : '..." "......" ".........', 6 : '..." "......" "Level up: знание языка программирования." ".........', 7 : '..." "......" ".........', 8 : '..." "......" ".........', 9 : '..." "......" "Level up: знание языка программирования." ".........', 10 : '..." "......" ".........', 11 : '..." "......" ".........', 12 : '..." "......" "Level up: знание языка программирования." ".........'}, 'kn_cybernetics', 'Почитать учебник по языку программирования', 2)}
    me "Спасибо."
    show el serious pioneer at left with dspr
    el "Только не испорти и не потеряй, это единственный экземпляр!"
    me "Понял."
    "Я отложил книгу на край стола, потому что Сыроежкин ещё не закончил показывать мне строение робота."
    show el laugh pioneer at left with dspr
    if d2_mz_help:
        el "Тут пусто, но когда плата высохнет после мытья и пайки, я вмонтирую её обратно."
    else:
        el "Тут пусто, но я сейчас припаяю гироскоп и вмонтирую плату обратно после мытья и сушки."
    "Затем он провёл рукой по жёсткой оси с ветвящимися металлическими планками."
    el "Позвоночник и рёбра робота, упругие и прочные, нужны, чтобы поддерживать каркас и защищать основные устройства в теле."
    "Я показал на гофрированный шланг от шеи робота до живота, соединявшийся с металлическим коробом."
    me "А это для чего?"
    show el smile pioneer at left with dspr
    el "Пищевод, но не для еды, а чтобы фокусы показывать. Он ведёт в брюшную камеру хранения. Камера открывается со стороны спины, оттуда же вытягивается вилка для заряда аккумулятора от розетки."
    el "Ты не смотри, что корпус выглядит таким закрытым, в нём есть клапаны, которые сдвигаются, это нужно для прокладывания всех кабелей и синтетических мышц. А лицевая маска временная."
    "Он нащупал соединительные детали маски и снял её. Внутри я увидел железную конструкцию, имитирующую строение черепа."
    show sh surprise pioneer at right with dspr
    sh "Глаза и слух мы пока ещё не сделали, как и подвижные суставы челюсти, так что над этим надо работать."
    show sh normal pioneer at right with dspr
    "Там, где у робота должны быть щёки и скулы, уже было встроено небольшое скопление валиков."
    me "Что это?"
    show el laugh pioneer at left with dspr
    el "Механика губ и челюсти, вместе с синтетическими мышцами робот будет воспроизводить звуки и менять форму рта.{w} Никогда не видел, как тестовые роботы двигают челюстью только вверх-вниз? Это и отличает их от человека. Тут будет по-другому."
    el "А самое главное, этот робот сможет улыбаться."
    show el smile pioneer at left with dspr
    "Он вернул маску на место."
    el "В голове содержатся зрительные и слуховые органы, дополнительная память и система коммуникации: радио и телефон. Зная личный номер робота, можешь позвонить ей прямо в голову, и она ответит."
    me "А Интернет?"
    show sh surprise pioneer at right with dspr
    sh "Нет модуля. Мы же сказали, код рассчитан на социальную адаптацию робота среди людей. Если робот будет черпать все знания из сети, то может сократить общение с человеком до минимума."
    th "И станет затворником, прямо как я. Эй, вот кто мне нужен в качестве спутника жизни!"
    show sh normal_smile pioneer at right with dspr
    sh "Кошачьи уши не только для красоты и образа, задействуем их как антенны для дистанционного управления."
    show el normal pioneer at left with dspr
    el "В роботе должно быть шестьдесят восемь сенсорных элементов по всему телу, их я тоже пока не монтировал в корпус. Это понадобится, когда мы будем прикреплять оболочку с микроэлектроникой."
    me "Робот будет копировать внешность живой девушки во всём?"
    show el smile pioneer at left with dspr
    el "Конечно."
    me "Даже половые органы?"
    show el surprise pioneer at left
    show sh upset pioneer at right
    with dspr
    "Я задал первый вопрос, пришедший в голову, и Электроник немного смутился, не ожидавший, что разговор зайдёт в подобное русло. Шурик, сидевший в сторонке, не то кашлянул, не то хмыкнул."
    show el shocked pioneer at left with dspr
    el "Э-э, только снаружи...{w} Не, чтобы ещё и внутри, надо заказывать японскую силиконовую штуковину... Имитатор. Ну, ты понял."
    me "Ага."
    show el shocked pioneer at fleft with dspr
    show sh rage pioneer close at center with dspr
    with vpunch
    "Шурик вскочил с места и схватил меня за ворот рубашки."
    sh "Не вздумай, Семён! Кошка-горничная неприкосновенна!"
    me "Да я ничего такого не собирался делать..."
    "Он стал трясти меня, как грушу."
    sh "Не смей даже представлять себе {i}это{/i} при нас! И не при нас! Вообще, где бы то ни было. Понял?"
    th "Ну, хоть что-то святое у них есть."
    me "Да понял я, просто спросил из любопытства!"
    show sh upset pioneer close at center with dspr
    show el normal pioneer at fleft with dspr
    "Шурик отпустил меня и вздохнул, успокаиваясь."
    show el normal pioneer at left with dspr
    show sh upset pioneer at cright with dspr
    sh "Извини за резкость."
    me "Ничего, всё в порядке."
    sh "Давайте вернёмся к работе."
    if d2_mz_help:
        me "Да я уже наработался в библиотеке, не пора ли отдохнуть и развлечься? Или мы в лагерь приехали вкалывать? В таком случае, мы ошиблись лагерем."
        "Сыроежкин расплылся в улыбке."
        show el grin pioneer at left with dspr
        el "Слыхал, Шурик? Наш человек!"
        show el surprise pioneer at cleft with dspr
        show sh scared pioneer at cright with dspr
        el "Блин, я же чуть не забыл! Вчера перед сном поймал момент и пересёкся с дядей Мишей насчёт карточного турнира..."
        show sh normal pioneer at cright with dspr
        me "Дядя Миша?"
        show el normal pioneer at cleft with dspr
        el "Михаил Ефграфович, один из администраторов нашего лагеря."
        me "А кто ещё админ?"
        show el grin pioneer at cleft with dspr
        el "Оль-Дмитриевна, конечно же!"
        show el smile pioneer at cleft with dspr
        el "Надо сходить в админцентр и узнать, что он решил. Шурик, ты с нами?"
        show sh serious pioneer at cright with dspr
        sh "Ой, нет, код важней. Я останусь."
        show el surprise pioneer at cleft with dspr
        el "Разве ты не закончил тот фрагмент?.."
        sh "Закончил, но ещё не проверил на ошибки. А потом возьмусь за следующий."
        show el normal pioneer at cleft with dspr
        el "Я думал, ты тоже наш человек, как Семён."
        show sh surprise pioneer at cright with dspr
        sh "Да ваш, ваш. Делу время, потехе час." 
        show sh normal pioneer at cright with dspr
        sh "Я вас подожду. Если что, встретимся в столовой на ужине."
        show el smile pioneer at cleft with dspr
        el "Ладно, удачи тебе!"
        hide sh with dissolve
        el "Пойдём, Семён."
        window hide
        stop music fadeout 1
        stop ambience fadeout 1
        jump d2_admin_center
    else:
        "Он с виноватым выражением лица сел за компьютер."
        hide sh with dissolve
        stop music fadeout 3
        play music music_list["everyday_theme"] fadein 2
        show el smile pioneer at center with dissolve
        "Сыроежкин кивнул, соглашаясь, и взял плату и чёрный модуль гироскопа, который он собирался припаивать."
        el "Семён, самое время показать тебе, как паять!"
        me "Ну, давай."
        "Мы остановились у верстального стола. Сыроежкин подтащил табурет и уселся."
        show el normal pioneer at center with dspr
        "Он разложил перед собой на столе паяльник, плату, кисточку, жестяную банку канифоли, катушку с проволокой и пинцет."
        el "Ты вообще когда-нибудь в жизни паял?"
        me "Неа..."
        show el serious pioneer at center with dspr
        el "Значит, всей науки сразу я тебе не расскажу, только самое основное." 
        el "Тебе потом надо будет самому выполнить что-то похожее..."
        show el normal pioneer at center with dspr
        "Сыроежкин с озабоченным видом стал выдёргивать и тут же задвигать ящики в поисках чего-то недостающего, попутно выложив на стол ещё и клей."
        "А потом он наконец достал связочку зубочисток, флакон с надписью «Флюс для пайки» и несколько ушных палочек с тампонами."
        "Он раскрутил рычаг тисков, чтобы между железными губами поместилась плата, и аккуратно зажал её."
        show el smile pioneer at center with dspr
        el "Очевидно, если плата грязная, её стоит почистить. Эта вроде ничего, в порядке."
        el "Главное — привести инструмент в рабочий вид. Жало паяльника надо почистить в любом случае и подточить."
        "Пионер демонстративно обтесал напильником медное жало с двух сторон."
        show el normal pioneer at center with dspr
        el "А теперь пусть разогреется. Когда канифоль оплавится, можно начинать паять."
        "Паяльник временно лёг на деревянную подставку. Электроник пинцетом оставил на жале кристалл канифоли и воткнул в розетку вилку."
        hide el with dissolve
        show sh serious pioneer at center with dissolve
        "Пока Электроник ждал, я ещё раз подошёл к Шурику поглядеть, что же он делает на компьютере."
        "Пионер в очках старательно набирал нужные команды и вызовы функций по условиям. Иногда Шурик заглядывал в тощую тетрадку, где им были выписаны подсказки и рекомендации, видимо, из того учебника, который мне дали."
        "Но пока я не мог понять точно, за что именно отвечает пишущийся фрагмент кода — языка я не знал и глядел на экран просто из интереса."
        "..."
        hide sh with dissolve
        show el smile pioneer at center with dissolve
        el "Готово! Иди сюда, Семён, покажу."
        "Я с воодушевлением присоединился к нему."
        show el laugh pioneer close at center with dspr
        el "...В общем так! Ничего сложного здесь нет, просто берёшь и без задней мысли паяешь."
        me "Да ну?"
        show el normal pioneer close at center with dspr
        "Сыроежкин вынужденно пожал плечами."
        el "Хотя, комплектующие у нас не из простых, здесь нужно деликатное обращение."
        el "Для такой техники здешние условия чуть ли не кустарные."
        "Он надел слесарные очки и дал мне такие же."
        show el serious pioneer close at center with dspr
        el "Короче, смотри, как я делаю, и запоминай. Сначала надо точно приладить микросхему к своим контактам, чтобы элемент работал."
        show el normal pioneer close at center with dspr
        el "Для этого залудим два крайних контакта, на которых зафиксируем гироскоп до основной пайки."
        "Пионер размотал немного проволоки с катушки, слегка коснулся паяльником самого кончика металлического прута. От жала пошла струйка дыма, и Сыроежкин покрыл один контакт серебряным блеском."
        "С противоположным по диагонали контактом он поступил так же." 
        "Затем Сыроежкин взял пинцет, больше смахивающий на щипцы, и как можно более аккуратно совместил микросхему ножками со всеми контактными площадками."
        "Всё ещё придерживая элемент пинцетом, Сыроежкин спаял ножки с залуженными контактами."
        el "Теперь дело пойдёт быстрей."
        "Он обработал контактные площадки и ножки кисточкой, заранее смочив её флюсом. Беря совсем чуть-чуть припоя жалом с проволоки, Сыроежкин припаял микросхему сначала с одного края, потом с другого."
        show el laugh pioneer close at center with dspr
        el "Хочешь попробовать?"
        me "Да, конечно."
        "Я вооружился паяльником и проволокой."
        show el normal pioneer close at center with dspr
        el "Много припоя не надо брать — одного касания, в крайнем случае двух, достаточно для целой стороны."
        el "Хватишь лишнего, испачкаешь плату — будешь работать отсосом."
        me "Не собираюсь я быть никаким отсосом!.."
        "Я сказал это почти на автомате. По спине пробежали мурашки: не услышал ли нас кто за дверью, как я сам утром при обходе кружков?"
        "Сыроежкин глянул на меня с прищуром."
        show el grin pioneer close at center with dspr
        el "У-у, как всё запущено! Но ты нуб, и это простительно.{w} Был у стоматолога когда-нибудь? На операциях суют в рот трубку для отвода слюны. Здесь примерно то же самое."
        show el smile pioneer close at center with dspr
        el "Отсос — это такая полезная штуковина, которой мы убираем излишки припоя. Где же он завалялся?"
        "Он ещё раз прошёлся по всем ящикам в столе."
        el "А, вот!"
        "Сыроежкин показал мне инструмент, похожий на шприц."
        show el serious pioneer close at center with dspr
        el "Короче, прогревай жалом ножки, но не передерживай больше двух-трёх секунд. Сильно паяльником не дави."
        show el normal pioneer close at center with dspr
        "Я тронул жалом проволоку припоя, с лёгким шипением закурился дымок, и я осторожно — как будто делал штрихи кистью на бумаге, пропаял несколько ножек микросхемы."
        "На полпути мне снова пришлось взять немного припоя и повторить движения паяльником."
        show el smile pioneer close at center with dspr
        el "Молодец, хорошо получается."
        "Я обрадовался. В самом деле — просто берёшь и паяешь!"
        "Гироскоп мы приделали быстро."
        show el laugh pioneer close at center with dspr
        el "Вот так вот! Семён, почитай пока учебник по языку программирования, а я займусь промыванием платы, окей?"
        me "Кодинг мне ближе, так что я не против."
        hide el with dissolve
        stop music fadeout 1
        "..."
        "Через несколько минут воцарилась рабочая атмосфера — мы молчали, и каждый из нас был занят делом. Стало довольно тихо, если не считать стука клавиш и редкого металлического лязга, когда Электроник менял что-то в конструкции робота."
        "А я читал при дневном свете, устроившись на стуле."
        "Было приятно, что учебник написан легко и в то же время подробно, с подсказками и советами, однако сразу вникнуть в особенности синтаксиса нового языка не получилось, и я старательно перечитывал важные моменты."
        $ proficiencies ['kn_cybernetics']+=1
        "........."
        "Время шло, и чтобы отвлечься от работы, Сыроежкин рассказывал мне о том, как собирали его робота-двойника, и как он познакомился с ним, хотя эта история с большими отличиями уже была известна мне благодаря советскому фильму."
        "Только пионер закончил с пайкой других элементов и промыванием плат, мы открыли настежь все форточки в комнате и ушли на улицу, оставив помещение проветриваться от запаха канифоли..."
        window hide
        stop ambience fadeout 1
        scene bg ext_clubs_day
        with dissolve
        play music music_list["lightness"] fadein 2
        window show
        show el smile pioneer at cleft with dissolve
        show sh normal pioneer at cright with dissolve
        sh "Серёга, я дописал тот кусок кода, осталось проверить его на ошибки."
        el "Отлично."
        show sh serious pioneer at cright with dspr
        sh "Через пять минут, когда комната проветрится, снова за работу. Возьмусь ещё за один блок в коде."
        show el laugh pioneer at cleft with dspr
        el "А ты, Семён?"
        me "Книга безусловно интересная, но не пора ли уже прерваться? Когда мы будем развлекаться? А то у меня ощущение, будто я в школе, а не на отдыхе."
        show el grin pioneer at cleft with dspr
        "Сыроежкин расплылся в улыбке."
        el "Слыхал, Шурик? Наш человек!"
        show el surprise pioneer at cleft with dspr
        show sh scared pioneer at cright with dspr
        el "Блин, чуть не забыл! Вчера перед сном поймал момент и пересёкся с дядей Мишей насчёт карточного турнира..."
        show sh normal pioneer at cright with dspr
        me "Дядя Миша?"
        show el normal pioneer at cleft with dspr
        el "Михаил Ефграфович, один из администраторов нашего лагеря."
        me "А кто ещё админ?"
        show el grin pioneer at cleft with dspr
        el "Оль-Дмитриевна, конечно же!"
        show el smile pioneer at cleft with dspr
        el "Надо сходить в админцентр и узнать, что он решил. Шурик, ты с нами?"
        show sh serious pioneer at cright with dspr
        sh "Ой, нет, код важней. Я останусь."
        show el normal pioneer at cleft with dspr
        el "Я думал, ты тоже наш человек, как Семён."
        show sh surprise pioneer at cright with dspr
        sh "Да ваш, ваш. Делу время, потехе час. Как люди соберутся на ужин, я подойду."
        show el smile pioneer at cleft with dspr
        el "Ладно, удачи тебе!"
        hide sh with dissolve
        el "Пойдём, Семён."
        window hide
        stop music fadeout 1
        jump d2_admin_center

label d2_admin_center: 

    scene black
    with dissolve
    show screen central_text("День 2 — Главный корпус")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_square_day
    with dissolve
    #TODO (к этапу работ по графике): позднее здесь будут нужны новые bg. ТЗ по ним есть.
    play music music_list["memories"] fadein 1
    $ set_mode_nvl()
    window show
    "Мы с Электроником не дошли до площади совсем немного и сразу повернули на дорожку к зданию администрации."
    "Уже отсюда можно было заметить ухоженные, симметрично разбитые по сторонам от входа клумбы."
    "Вид крыльца с козырьком-навесом, подпираемым фигурными решётками, живо напомнил мне о школе и тех временах, когда я посещал её."
    "Это было довольно давно, и я уже подзабыл о тех беспокойных минутах, когда нужно выходить к доске, отвечать и демонстрировать выполненные домашние задания, а затем решать контрольные."
    "В пионерлагере, к счастью, такое не грозило мне, и даже было интересно увидеть того человека, который является директором."
    "Но если принять слова Сыроежкина во внимание, получается, что Ольга Дмитриевна тоже директор?"
    nvl clear
    show el smile pioneer at center with dissolve
    "Уточнить это я не успел. Вихрастый пионер, не стучась, распахнул передо мной дверь главного корпуса."
    "Мы оказались в небольшом холле."
    "Напрасно я ожидал увидеть роскошный и современный вестибюль!"
    "Помещение выглядело скромно и несколько пустынно, зато ничего лишнего: вахтёрский пост с подвесным шкафчиком для ключей на стене, общий гардероб-раздевалка, тройка мягких диванов для посетителей и несколько информационных досок. Кое-где стояли горшки с растениями. А самое любопытное и красивое, что бросалось в глаза — рисунки на стенах без окон. В холле был изображён пляж лагеря, словно наблюдающий картинку находился в тени — за деревом — и смотрел на песок и бегущие речные волны. Как же мне захотелось снова туда сходить и уж точно искупаться!"
    show el normal pioneer at center with dspr
    el "Эй, ты чего остановился?"
    me "Да так. Посмотреть уже нельзя? Я здесь в первый раз."
    show el smile pioneer at center with dspr
    el "А-а, понимаю! На той неделе в начале смены мы всё тут оббегали, пока нас не сплавили на очередное мероприятие. Здесь полно интересных мест! Жаль, что наши отряды не поселили сюда... Или ещё два новых отряда пионеров не организовали."
    me "А почему не организовали?"
    show el surprise pioneer at center with dspr
    el "Я-то почём знаю? Может, просто не хватает вожатых на всех?{w} В любом случае, в палаты этого корпуса заселяются в зимние смены, нам так Ольга Дмитриевна сказала."
    me "Странно, конечно..."
    nvl clear
    show el normal pioneer at center with dspr
    "Кроме нас в холле не было ни души. Я приблизился к стойке у входа."
    me "И пусто. У вас на вахте кто-нибудь сидит?"
    show el smile pioneer at center with dspr
    el "Не, и заведующей гардеробом тоже нет, лето ведь! Зато уборщицу можно встретить."
    "Поравнявшись со мной, Сыроежкин показал на подвесной шкафчик."
    show el laugh pioneer at center with dspr
    el "Видишь? Каждый вечер старосты кружков закрывают помещения клубов и приносят ключи сюда. Для порядка."
    me "А если не принести?"
    show el grin pioneer at center with dspr
    el "После ужина обязательно напомнят, не отвертишься."
    nvl clear
    show el normal pioneer at center with dspr
    "Я постоял на месте ещё немного, разглядывая информационные стенды, и пошёл следом за Сыроежкиным, который снова нетерпеливо позвал меня." 
    "По неширокой лестнице мы поднялись на второй этаж — в коридор, откуда можно было попасть в актовый зал, палаты пионеров, изолятор, офис вожатых и кабинет Михаила Ефграфовича."
    me "Я вот всё хотел спросить, у вас, выходит, сразу два директора?"
    show el smile pioneer at center with dspr
    el "Можно сказать так. Ольга Дмитриевна — директор-воспитатель, руководит вожатыми, занимается нами, а дядя Миша — финдиректор, он скорее по части работы лагеря и деньгам."
    "Говоря о деньгах, Сыроежкин сложил пальцы щепоткой."
    show el serious pioneer at center with dspr
    el "Зелень к зелени. Ну, ты сам всё поймёшь."
    nvl clear
    stop music fadeout 1
    show el normal pioneer at center with dspr
    "Мы прошли весь длинный коридор и постучались в обшитую бурым дермантином дверь с табличкой, называвшей должность Михаила Ефграфовича."
    "Ответили нам не сразу, и Сыроежкину пришлось постучать второй раз, посильней."
    play sound sfx_knock_door2
    efg_voice "Открыто!.."
    hide el with dissolve
    play music music_list["get_to_know_me_better"] fadein 1
    "Из-за двери потянуло чем-то странным, но спустя мгновение я сообразил, что пахло мятой. Войдя, я остановился."
    "Глаза не сразу привыкли к обстановке. Кабинет финдиректора был в почти глубоком полумраке из-за плотных чёрных штор, которыми небрежно задёрнули окна."
    "У стены слева находился громоздкий дубовый стол, обитый зелёным сукном, на нём располагались компьютер и позолоченная лампа с таким же зелёным абажуром. Этот успокаивающий цвет, казалось, целиком овладел директорским кабинетом. Даже содержимое аквариума на комоде казалось зелёным от подсветки и декоративной растительности. У противоположной окнам стены тянулся книжный шкаф, под ним я приметил невысокий столик, не то для журналов, не то для чайной церемонии, — на нём покоились чёрный нетбук, изгаженная пепельница, пара сложенных вместе грязных мисок из-под лапши и палочки для блюд восточной кухни. Позади Михаила Ефграфовича, сидевшего на кожаном кресле, висел портрет какого-то бородатого исторического деятеля в шляпе с высокой тульей."
    #show efg
    #show nc
    "Михаил был не один — на подлокотнике рядом с ним устроился большой кот с необыкновенно крупной головой и повязкой на одном глазу, как у пирата, только символ был каким-то непонятным, явно не череп с костями..."
    "...А ноль с косой чертой."
    th "Ох ты ж ё!.."
    "Кот тоже был зелёным, но с чёрными полосками. Изумрудно-зелёным, словно его облили зелёнкой."
    nvl clear
    "Я протёр глаза, решив, что всё мне основательно приглючилось от жары."
    "Но нет, кот как был зелёным, таким и остался. Увидев меня с Электроником, он слез на пол, чем добил мои представления о мире окончательно. Кот, ростом по плечи Ульяне, преспокойно стоял на задних лапах, как человек, и пропорции у него выглядели человеческими. Разница в том, что он всё таки был животным, а не представителем Homo Sapiens."
    "На физиономии кота застыла эмоция безразличия, какая обычно бывает после множества испытанных тягот и огорчений, когда терять больше нечего. Смерив меня равнодушным взглядом, он поплёлся к выходу из кабинета и ушёл по неведомым делам."
    #hide nc
    show el smile pioneer at left with dissolve
    "Нет, цвет его шерсти мне определённо не померещился в потёмках. Я был так поражён, что ничего не произнёс, только вопросительно взглянул на Сыроежкина. Но тот ничего не объяснил, попросту не заметив, что я впал в прострацию. Даже вид кота вообще не смутил его."
    el "Здрасте!"
    efg "Здравствуйте, пионеры. Надо признаться, вы немного отвлекли меня."
    el "От чего, если не секрет?"
    efg "Техподдержка веб-форума..."
    el "Ясно. Думаю, Шурику было бы интересно поговорить с вами об этом!"
    efg "Пусть заходит, я не возражаю."
    el "Обязательно передам!{w} А мы вот пришли узнать, разрешите ли вы нам провести карточный турнир в лагере..."
    nvl clear
    efg "Разрешил."
    el "А вы договорились с вожатыми?"
    efg "Договорился."
    efg "И с поварами тоже, насчёт ужина. Правда, они были не совсем рады, сказали: «Ерунду сделал.»"
    efg "Творческую инициативу я одобряю. Вы главное карты возьмите где-нибудь, и всё будет готово."
    "Голос финдиректора не был похож на властный голос большого начальника, а был, скорее, внушающе-доверительным. Поэтому я осмелел и тронулся с места."
    "Пока Михаил беседовал с Элом, я продолжил осматривать кабинет. Под ногами лежал однотонный ковёр цвета бордо, чем выделялся из общей картины, но в полутьме трудно было сразу заметить его, как и затейливый орнамент на зелёных обоях. Остановившись рядом с аквариумом и стараясь не шуметь, я отогнул штору, впуская дневной свет в кабинет. Окна выходили на площадь с памятником Генде, едва видную из-за крон деревьев."
    th "Не самое удачное место для наблюдения за жизнью в лагере."
    "Но, похоже, Михаилу Ефграфовичу это было не так важно. То, как он держал окна задёрнутыми, напомнило мне о своих днях затворничества."
    nvl clear
    th "Неужели я всё ещё жалею, что оказался тут?"
    "Я переключил своё внимание на аквариум, который правильней стоило называть террариумом: в нём не плавали рыбки, был один лишь грунт, нечто вроде пещеры из камней со мхом и кустиками, а у стекла — здоровый лоток с водой."
    me "Извините, а кто живёт в аквариуме?"
    "После того зелёного кота я ожидал увидеть что-то необычное, вроде волосатого краба-Йети или карликового электрического угря, но так как воды в аквариуме почти не было, я терялся в догадках."
    efg "Морская улитка.{w} Я её Мариной зову."
    me "А где она? Не вижу."
    efg "Прячется. Она обычно появляется рано утром, и я кормлю её."
    efg "Или кот."
    me "А-а, понятно..."
    "Я всё ещё пребывал в тихом шоке."
    nvl clear
    me "Скажите, а почему кот у вас так выглядит? Зелёнкой облили что ли?"
    efg "Да он просто съел чего-то не того."
    "Директор усмехнулся, и я не понял, шутит он или говорит всерьёз."
    "Вспомнив о чём-то, Михаил Ефграфович подошёл к шкафу с книгами и достал полупустую бутыль крепкого алкоголя."
    "Теперь уже удивился Сыроежкин."
    show el surprise pioneer at left with dspr
    el "Вы пьёте на рабочем месте?"
    efg "Без повода не выпиваю. Это для него."
    #show nc
    "Михаил показал на кота, только что вернувшегося в кабинет, и не с пустыми лапами — он принёс миску с заваренной лапшой, куда щедро были насыпаны веточки мяты, и банку шпрот."
    "Кот снова молча прошёл мимо нас и уселся за тем невысоким столиком для чайных церемоний, только вместо пиалы с этим благородным напитком директор поставил ему стакан с американским виски."
    show el smile pioneer at left with dspr
    el "Значит, киса молока не пьёт, киса пьёт бурбон?"
    efg "Какая он тебе киса? Это {i}он{/i}, и у него имя есть, между прочим. Зовите его Нулькот."
    $ meet('nc', u"Нулькот")
    nvl clear
    "В голосе директора появились нотки недовольства, однако он быстро сменил и тон, и тему."
    efg "Насчет карт — играйте, только без денег и... хм, юношеских забав с девчонками. Это я вам как взрослый взрослым говорю..."
    th "Педагогический прием? Или он всё знает про мой возраст?{w} А Сыроежкин? Он тоже?"
    "После увиденного я был вправе ждать чего угодно."
    efg "Турнир состоится, но сначала ужин, который мы перенесли на половину восьмого. Вообще, ребята, можно было не заходить ко мне, вы бы услышали горн и объявление вожатых."
    stop music fadeout 1
    th "Но что взять с нетерпеливого Сыроежкина?"
    $ renpy.music.set_volume (0.1, delay=0, channel=7)
    play sound sfx_dinner_jingle_speaker channel 7
    "За окнами и тяжёлыми шторами раздался сигнал, приглашающий всех пионеров в столовую — далёкий и тихий, как из другой вселенной."
    efg "О, а вот и он. Поспешите, а то вас недосчитаются. Приятного аппетита!"
    el "Спасибо!"
    "Он выскочил из кабинета, и я рванул следом за ним."
    nvl clear
    window hide
    play music music_list["get_to_know_me_better"] fadein 1
    $ set_mode_adv()
    scene bg ext_square_day
    with fade
    window show
    th "Ещё бы — пришло время поесть! Нет, ПОЖРАТЬ. Именно так, большими буквами."
    show el grin pioneer at cright with dspr
    "Электроник умудрялся ещё что-то болтать мне на бегу."
    el "Всё даже лучше получилось!"
    window hide
    scene bg ext_dining_hall_away_day
    with fade 
    $ renpy.pause(1)
    scene bg ext_dining_hall_near_day
    with fade
    window show
    "У столовой мы притормозили и устроились в образовавшуюся очередь так же быстро налетевшими пионерами."
    show el smile pioneer at center with dissolve
    "Отдышавшись, Сыроежкин указал на запылённый автомобиль «Волга» рядом с крыльцом."
    el "Это машина дяди Миши, кстати. Водить умеешь?"
    me "Нет, с чего бы?"
    show el sad pioneer at center with dspr
    "Авантюрный блеск в глазах пионера угас."
    show el smile pioneer at center with dspr
    el "А-а, ну а я умею, один знакомый помог. У меня в городе ещё мопед есть..."
    "Сыроежкин принялся рассказывать мне, как и когда научился вождению, и, если принимать его слова всерьёз, сначала это было трудновато, а затем сверхлегко."
    "Но я невнимательно слушал его: все мысли заняла необычная встреча с директором и котом, после которой этот лагерь в моих глазах уже не будет прежним."
    show el smile pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    "Мы дождалсь Шурика, и он встал к нам без очереди."
    show sh surprise pioneer at cright with dspr
    sh "Ну, разрешили вам провести игру?"
    show el grin pioneer at cleft with dspr
    el "Ага, я после ужина подойду к Ольге Дмитриевне..."
    "Я оставил на потом размышления, хочется ли мне участвовать в общем мероприятии, первым делом всё же надо было поесть."
    window hide
    stop music fadeout 1
    jump d2_pre_event

label d2_sport_club_day:

    if sport_club:
        $ reset_chibi("sport_area")
        scene black
        with dissolve
        show screen central_text("День 2 — Игры на траве")
        $ renpy.pause(99, hard=False)
        hide screen central_text
    
    if been_there()>1:
        $ reset_chibi("sport_area")
        scene bg ext_playground_day
        with dissolve
        "Пионеров стало больше, но мне здесь нечего делать."
        $ disable_current_zone()
        jump d2_day_map

    scene bg ext_playground_day
    with dissolve
    play music music_list["lightness"] fadein 1
    if (sport_club == False):
        window show
        "Я не вступил в спортивный кружок, но пока что не жалел о сделанном выборе."
        "После полдника лишь немногие пионеры явились на спортплощадки, и только единицы — в физкультурной одежде."
        "У меня не было времени стоять и ждать у моря погоды вместе с ними."
        th "Надо идти в свой кружок."
        window hide
        stop music fadeout 1
        jump d2_day_map
    window show
    "Несмотря на то, что усиленно заниматься физической деятельностью не хотелось, я всё равно пришёл на спортплощадки."
    "Околачиваться на свежем воздухе было лучше, чем сидеть в душной палате или помещении кружка."
    th "Если только меня не загоняют до смерти, как сегодня утром."
    "Сюда понемногу стекались пионеры в физкультурной форме. Они кучковались вместе и явно кого-то ждали.{w} Наверно, вожатого Дмитрия."
    "Я вдруг подумал, что мне тоже стоит пойти и переодеться в физкультурную форму, а то в рубашке и шортах на ремне станет жарковато."
    stop music fadeout 1
    scene black
    with dissolve
    "......"
    scene bg ext_playground_day
    with dissolve
    play music music_list["always_ready"] fadein 1
    "Ну, вот теперь я в полной готовности."
    "Даже появилось какое-никакое настроение играть."
    #show lk
    "Когда я вернулся на поле, здесь уже был Дмитрий Евгеньевич, окружённый небольшой толпой пионеров."
    "Я присоединился к ним."
    lk "...Ладно, значит, проведём занятие как обычно."
    "Он предложил девочкам и нескольким мальчикам проследовать на волейбольную и бадминтонную площадки, как эти пионеры хотели, а те, кто собрался играть в футбол, остались на месте, и я тоже."
    lk "Сейчас я принесу вам мячи, воланчики и ракетки."
    #hide lk
    "Позвав одного из пионеров помочь, он ушёл в крытый спортзал, а мы начали выбирать капитанов команды игрой в камень-ножницы-бумагу."
    "В результате, я оказался в числе обычных игроков, капитанами стали два неизвестных мне пионера."
    us_voice "Подождите! Я тоже с вами!"
    show us surp2 sport at center with dissolve
    "К нам прибежала Ульяна, вся перепачканная в земле и копоти. Видимо, лазила в неведомых дебрях и потому опоздала. Внешний вид её нисколько не волновал, она явилась как будто ничего не произошло."
    boy_A "А мы уже выбрали капитанов..."
    show us dontlike sport at center with dspr
    "Ульяна с обидой пожала плечами."
    us "Ну и ладно."
    "Рыжая девчонка была не слишком довольна, однако, заметив меня, расслабилась и хитро улыбнулась."
    show us smile sport at center with dspr
    boy_B "Я выбираю первый."
    "Капитаны по очереди называли имена ребят, которых брали к себе в команду. Вышло так, что мы с Ульяной оказались вместе."
    "Пионеры разошлись на свои стороны поля."
    show us upset sport at center with dspr
    us "А вот будь я капитаном, я бы ни за что тебя не выбрала."
    me "Я был бы только рад этому."
    show us grin sport at center with dspr
    us "Что, так хорошо играешь?"
    me "Ну, тебе с твоим ростом будет очень тяжело продуть."
    show us dontlike sport at center with dspr
    "Ульяна не успела ответить, как на поле появился Дмитрий. Он кинул на песчаную дорожку футбольный мяч."
    "Пионер-капитан попросил нас занять свои позиции, и мы отошли друг от друга."
    hide us with dissolve
    "..."
    show us smile sport far at cright with dissolve
    "Вожатый дунул в свисток, когда мяч положили в центре площадки."
    play ambience ambience_soccer_play_background fadein 1
    "Начинали мы. Ульяну поставили в нападающие, а мне была поручена роль защитника."
    "Команда противников играла слаженно, и нас неустанно прессовали."
    "Со своей задачей я справлялся на пару с ещё одним пионером, отбивая мяч у бегущих к воротам пацанов и возвращая его полузащитникам или Ульяне."
    #TODO: можно зациклить перемещения спрайта влево-вправо.
    "Она неплохо играла, ничем не уступая мальчишкам-ровесникам.{w} И бегала быстро, что с мячом, что без него. Маленький красный метеор — её иначе было не назвать."
    "И Ульяну мне было трудно спутать с кем-либо из игроков, выбирая, кому отдать пас — красноволосая девчонка была самой заметной на всём поле."
    "Ко всему прочему, ещё и самой чумазой от грязи."
    hide us with dissolve
    "Вратарь старался не меньше: из того числа раз, сколько бомбардировали наши ворота, он пропустил всего один гол, после которого мы перехватили инициативу." 
    "Форварды кричали мне и полузащитникам через всё поле и махали руками, чтобы мы пасовали им."
    "А особо внимательные пионеры, увлекавшиеся футболом, требовали право разыграть мяч, если противники допускали грубые нарушения и оффсайды.{w} Ничто из этого не вызывало препирательств, и за случайные касания мяча рукой и подножки обязательно штрафовали."
    "Мы сравняли счёт, а потом вырвались вперёд."
    "Но игра шла не так гладко, как нам хотелось."
    "Ребята из другой команды стали пасовать аккуратней, избегая меня в защите."
    show us dontlike sport far at center with dissolve
    "Как только наш вратарь прозевал два гола подряд, отчаявшись, Ульяна без всяких стеснений начала толкать противников и ставить им подножки, чтобы задавить атаку на наши ворота, пока один из пионеров, споткнувшись, не расквасил себе нос об землю."
    hide us with dissolve
    boy_C "Пенальти им!" 
    boy_D "Удалить Ульяну с поля!"
    boy_B "Протестую!"
    boy_A "Но у нас выбыл игрок! Отправьте свою нарушительницу на скамью запасных, так будет справедливо!"
    "Игра прервалась на ожесточённый спор капитанов. Упавшего мальчика подняли сотоварищи и повели в медпункт."
    "Пара игроков, заложив пальцы в рот, неодобрительно свистнула в нашу сторону."
    show us smile sport at cright with dspr
    me "Фух, это было жёстко. И вообще они по делу говорят, ты нарушила правила, и очень грубо."
    show us dontlike sport at center with dspr
    us "Пфе, Семён, как можно быть таким мягкотелым? Неужели ты не знаешь, что на войне все средства хороши?"
    me "Война войной, а это дружеский матч между своими... Впрочем, ты даже не извинилась."
    show us upset sport at center with dspr
    "Ульяна вздрогнула, но не подала виду."
    show us laugh2 sport at center with dspr
    us "Он знал, на что идёт и с кем играет. Мне было бы странно извиняться после такого, ведь я не случайно подставила ногу."
    me "А если тебе ногу подставят?"
    show us grin sport at center with dspr
    us "Будто мне так никогда не делали! Не раз падала, и ничё, всё заживало. Пусть только попробуют."
    th "Вот это самоуверенность! В сочетании с полным безразличием к чувствам других людей, конечно."
    show us laugh sport at center with dspr
    us "Спорт без травм — не спорт, а так, ерунда! Скукота."
    me "После десятка швов, поломанных конечностей и железных пластин в теле тебе будет уже не так весело."
    show us surp1 sport at center with dspr
    us "Железные пластины? Да это будет офигеть как круто! Если туда ткнут или ударят, боли не почувствуешь! Как Терминатор!"
    me "Э-э..."
    me "От боли это не спасёт, если тебе напомнят про нулевой размер."
    show us fear sport at center with dspr
    "Зря я издал смешок в конце фразы."
    show us cry2 sport close at center with dspr
    "В глазах Ульяны блеснули слёзы, и она принялась молотить по мне кулачками."
    show us angry sport close at center with dspr
    us "Дурак! Дурак! Дебил! Как о таком вообще можно шутить?"
    me "Я слишком много сидел в Интернете, так что моё ЧЮ безнадёжно испортилось, извини."
    me "Было бы из-за чего расстраиваться..."
    "Кажется, это взбесило её ещё больше. Ульяна в сердцах топнула по моей ноге."
    with vpunch
    me "А-а!!!"
    me "Блин, как я теперь буду играть?"
    show us dontlike sport at center with dspr
    us "Ничего, потерпишь."
    hide us with dissolve
    "Она отвернулась."
    "В итоге капитаны пришли к соглашению, и во многом благодаря вожатому Диме, который вмешался чуть позднее, чем я ожидал."
    "Где же он пропадал? Наверно, смотреть на играющих в волейбол девочек ему куда интересней..."
    "Из нашей команды на скамейку запасных вместо Ульяны ушёл другой нападающий пионер, а пенальти всё равно назначили."
    "Бил их форвард, и этот гол мы пропустили."
    "Было решено сделать перестановку в команде. Вратаря сменили, он занял место в защите, а я, как сказал капитан, должен был попробовать себя в качестве нападающего по левому флангу. Ульяна же осталась в центре."
    show us normal sport far at cright with dissolve
    "Раз я стал нападающим, наравне с Ульяной, то играть в пас мне приходилось в основном с ней и пионером на правой половине спортплощадки."
    show us surp2 sport far at cright with dspr
    us "Давай, пасуй!"
    "И я бил как следует, невзирая на ушибленную ногу."
    show us normal sport far at cright with dspr
    "Хоть мы втроём и метили в ворота противника, но бывало, что промахивались, а их вратарь уверенно отбивал мяч или хватал его, прижимая к телу."
    "Игра была в самом разгаре, когда пионер-голкипер, разбежавшись, выбил мяч вверх. Я, то и дело оглядываясь, стоял перед каким-то парнем и не давал ему выскочить вперёд и принять мяч для атаки на нашу половину поля."
    "Мяч достался мне, и я увёл его от незадачливого пионера, вырвавшись к защите противника."
    show us surp2 sport far at cright with dspr
    "На этот раз крик Ульяны я прослушал, не успел отдать ей пас."
    show us upset sport far at cright with dspr
    "Столкновение с защитником их команды привело к тому, что мяч ушёл в аут по моей вине."
    "Один мальчик сбегал за улетевшим на аллею мячом и вернулся, высоко подняв его над головой. Он медлил, выбирая, кому из своих бросить." 
    show us normal sport far at cright with dspr
    "Я не стал мешать какому-то пионеру заполучить мяч, но ждал его на пути для перехвата."
    th "Есть!"
    "Отобрав мяч, я ринулся к воротам и в рискованный момент отдал пас."
    show us smile sport far at cright with dspr
    "Ульяна изо всей силы ударила, вратарь коснулся мяча и отбил его за пределы поля."
    us "Угловой!"
    "Вратарь помахал своим товарищам, чтобы они в ответственный момент помогали защищать ворота от нас."
    show us normal sport far at right with dspr
    "Ульянка поместила мяч на угол, обозначенный придавленной камнями травой."
    th "И кому же она даст пас?.."
    "Девчонка разбежалась и..."
    "Мяч свистнул в сторону, как раз рядом, чтобы я остановил его и, не медля, повёл к воротам."
    hide us with dissolve
    "По наитию я обошёл защитника и ударил, целясь в ворота, потому что другого шанса уже могло не быть."
    all "Гол! ГО-О-ОЛ!!!"
    me "{b}Да!{/b}"
    "Я побежал назад, взмахивая руками с поднятыми указательными пальцами."
    "Сравняли счёт!"
    "Вся наша команда бегом вернулась на свою половину поля и сбилась в кучу, поздравить меня."
    boy_B "Отлично!"
    show us grin sport close at center with dissolve
    "Ульяна выставила обе пятерни навстречу мне."
    us "Дай десять, зануда!"
    me "Держи, грязнуля."
    show us laugh sport close at center with dspr
    "Мы хлопнули руками, и я подумал — это мы так хорошо сыгрались, или я просто пал жертвой стокгольмского синдрома?"
    stop music fadeout 1
    $ renpy.pause(1)
    play music music_list["eat_some_trouble"] fadein 0
    bt_voice "Сидорова-а-а!"
    mt_voice "Вот ты где!"
    show us fear sport close at right with dspr
    "Радость Ульяны как ветром сдуло."
    #show bt
    show mt angry pioneer far at center behind us
    show dv guilty pioneer far at cleft behind mt
    with dissolve
    "К спортплощадкам пришли вожатые Инга Максимовна и Ольга Дмитриевна. Последняя ещё вела за руку недовольную Двачевскую."
    show us dontlike sport close at right with dspr
    us "Вот блин!"
    me "В чём дело?"
    "Но Ульяна не слушала меня. Завидев наших вожатых, она мгновенно дала дёру куда-то по направлению к библиотеке, аж пятки засверкали."
    hide us with dspr
    mt "Персунов! Подойди, пожалуйста!"
    "Я быстро сказал капитану команды, что отлучусь на время, но чутьё подсказывало мне, что мне уже не доиграть матч."
    #show bt
    show mt angry pioneer at cright with dissolve
    show dv angry pioneer at center with dissolve
    me "Что случилось?"
    bt "Ничего особенного, просто Сидорова Ульяна в очередной раз провинилась и убежала от меня в лес."
    mt "А ещё она теперь грязная, как чертёнок."
    show mt rage pioneer at cright with dspr
    mt "Дима!"
    #show lk
    lk "Да, Оля?"
    show mt angry pioneer at cright with dspr
    mt "Почему Двачевская записана в спортивный кружок, а когда идут занятия, болтается по лагерю без дела?"
    th "Алиса из спорткружка? Вот это новость!"
    lk "Если пионерка не уделяет время кружку, то в День Спорта будет не в форме, выступит хуже и может подвести команду своего отряда. Алиса, ты что, хочешь подвести свой отряд?"
    th "Какой хитрый вожатый, знает, на кого перевести стрелки."
    show dv grin pioneer at center with dspr
    dv "Не хочу."
    lk "Тогда в следующий раз не бездельничай, а сразу приходи к нам."
    show dv normal pioneer at center with dspr
    lk "Это всё, Оля?"
    show mt normal pioneer at cright with dspr
    "Наша вожатая не слишком обрадовалась тому, как быстро Дмитрий Евгеньевич и Алиса замяли тему."
    mt "Семён, я поручаю тебе с Алисой отыскать Ульянку. Пусть она отмоется, чисто-чисто, как медный самовар, и тогда никто не будет наказан."
    dv "Всё, поняли."
    th "Как это Двачевская согласилась без всяких возражений?"
    show dv angry pioneer at center with dspr
    "Она пихнула меня локтем."
    dv "Погнали."
    "Алиса побежала, а я за ней."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ disable_current_zone()
    scene bg ext_square_day
    with fade
    play music music_list["my_daily_life"] fadein 1
    play ambience ambience_camp_center_day fadein 1
    window show
    show dv normal pioneer at center with dissolve
    "На площади, когда мы скрылись из поля зрения вожатых, я остановился."
    me "Ну и где будем искать Ульяну? Она могла убежать куда угодно."
    show dv smile pioneer at center with dspr
    dv "Она прячется недалеко, делает крюк и возвращается. Она же на спортплощадку обратно пришла?"
    me "Ага.{w} Так зачем её ловить, сама придёт через некоторое время."
    show dv angry pioneer at center with dspr
    dv "Ты вообще слышал вожатую? Шляпа, когда поймала меня у «Зелёного театра», сказала, что если я не помогу Инге Максимовне с Ульяной, то нас завтра не пустят на реку."
    dv "Типа «не любите мыться, не будете и купаться». И это в День Нептуна! Сечёшь?"
    th "А я каким боком тут? Потому что говорил с Ульяной последним?"
    "Но я ужасно хотел сходить на реку, и мысль, что мне не позволят окунуться в прохладную воду ещё сутки, заставила меня передумать. Теперь я прекрасно понимал Алису."
    if d1_river_flag:
        show dv normal pioneer at center with dspr
        dv "Хотя сегодня так жарко, что я пойду купаться, если вожатые будут заняты."
        "Она заметила мой удивлённый вид."
        show dv angry pioneer at center with dspr
        dv "Только ш-ш, никому не трепись, ясно? Мне не улыбается делить пляж с толпой пионеров."
    show dv normal pioneer at center with dspr
    dv "А Ульяну надо спасать, ей светит баня."
    me "Окей, я въехал. Где Ульяна?"
    "Не говоря ничего, Алиса помчалась к тем домикам, в которых жила большая часть младшего отряда."
    window hide
    scene bg ext_houses_day
    with fade
    $ renpy.pause(1)
    scene bg ext_house_of_dv_day
    with fade
    window show
    "Сначала девочка решила проверить свою комнату, что она делила с Ульяной."
    show dv normal pioneer at center with dissolve
    dv "Неа, её нет."
    me "С чего бы ей прятаться тут? Она убежала совсем в другую сторону."
    "Я показал туда, где за деревьями виднелся медпункт."
    show dv laugh pioneer at center with dspr
    dv "Ха, наивный!"
    show dv smile pioneer at center with dspr
    dv "Такое уже было: Ульяна спряталась у себя, а её искали весь день, Инга Максимовна чуть с ума не сошла, даже не наказала после всего. Это как с пультом от телика — ищешь-ищешь, а он на своём месте."
    dv "Есть ещё одно место — в лесу."
    me "А мы можем разминуться с Ульяной, если отправимся туда прямо сейчас?"
    show dv sad pioneer at center with dspr
    dv "Блин, я не думала об этом. Давай разделимся. Иди по левой стороне лагеря, ближе к забору, а я мимо библиотеки. Встретимся у сцены."
    me "А если я найду и поймаю Ульяну?"
    show dv smile pioneer at center with dspr
    dv "Тогда кричи погромче, и я вернусь."
    me "Я серьёзно! Кто мне поможет отмыть её? Она будет сопротивляться!"
    "В красках я представил, как эта мелкая рыжая девчонка без угрызений совести калечит меня, как того пионера-футболиста."
    th "Возможно я переоцениваю силу Ульяны..."
    show dv laugh pioneer at center with dspr
    dv "Семён, ты чё, испугался что ли?"
    me "Ни в коем случае. Но один я не смогу помыть её. Тут понадобится другая пара рук."
    show dv normal pioneer at center with dspr
    dv "Приведёшь к сцене, никаких проблем."
    dv "Хорош лясы точить, увидимся там. Мне кажется, Ульяна всё-таки не в лагере."
    hide dv with dissolve
    window hide
    stop ambience fadeout 1
    scene bg ext_houses_day
    with fade
    window show
    "Мы разделились, и я поспешил по улице к последнему по нумерации домику, начав поиски оттуда."
    "Как внимательно я ни смотрел по сторонам и за домиками, Ульяны не было видно."
    scene bg ext_bathhouse_day
    with fade
    "Возле самой реки на берегу, где находилась баня, тоже было пусто."
    "Я даже потрудился зайти внутрь и заглянуть во все комнаты, однако безуспешно."
    $ d2_seen_bathhouse = True
    scene bg ext_clubs_day
    with fade
    "Я вернулся к зданиям кружков."
    "Мне пришлось бегом прошарить оба корпуса и заглянуть в каждое незапертое помещение, где были пионеры."
    "Но красноволосая девочка нигде не отыскалась."
    scene bg ext_musclub_day
    with fade
    "Только после этого я двинулся к музыкальному клубу."
    "Внутри, кроме участников кружка, больше никого не было."
    scene bg ext_washstand_day
    with fade
    "Умывальники, должно быть, последнее место, где можно найти Ульяну."
    th "Почему бы ей просто не умыться и не мучить вожатых?"
    "Я задался глупым вопросом. Ульяна всё ещё была шебутным ребёнком, и поэтому меня с Двачевской заставили расхлёбывать кашу."
    scene bg ext_houses_day
    with fade
    "Оббежав все улицы между домами старшего отряда, я, порядком измученный, отправился к сцене."
    window hide
    scene bg ext_stage_big_day
    with dissolve
    window show
    "У скамеек перед эстрадой меня уже ждала запыхавшаяся Алиса."
    show dv sad pioneer2 at center with dissolve
    "За то время, пока я бегал, она к тому же снова завязала рубаху узлом, видимо, назло вожатой."
    show dv normal pioneer2 at center with dspr
    dv "Что, не нашёл её? И я тоже. Надо двигать в лес."
    "Глянув на зелёную массу деревьев, я развёл руками."
    me "Ну да, лес совсем маленький, меньше лагеря, просто тьфу. Мы сможем найти в нём Ульяну до того как состаримся?"
    show dv sad pioneer2 at center with dspr
    dv "Ей самой меньше всего хочется прятаться там, откуда хрен выберешься."
    me "Да кто её знает?"
    show dv angry pioneer2 at center with dspr
    "Алиса нахмурилась."
    dv "Я хорошо знаю её."
    show dv normal pioneer2 at center with dspr
    dv "Говорю же, есть одно место, где Ульяна точно может быть."
    th "Сезон охоты на лолей объявляется открытым!"
    me "Ладно, веди меня, Сусанин..."
    th "...в юбке."
    "Мой взгляд бесстыдно скользнул от плеч девочки к её попе."
    th "Подтянутая!"
    th "А может, не зря Ольга Дмитриевна требует, чтобы Алиса ходила в спортивный кружок..." 
    "Если бы Двачевская умела читать мысли, она бы сейчас убила меня. Я с облегчением вздохнул."
    "Мы перебрались за заборчик и побрели куда-то, немного взяв направо, но не сворачивая с пути."
    stop music fadeout 1
    play music music_list["so_good_to_be_careless"] fadein 1
    scene bg ext_path2_day
    with dissolve
    show dv normal pioneer2 at center with dissolve
    me "А куда мы вообще идём? Что за место такое?"
    dv "К танку."
    me "Какому танку?"
    dv "Это памятник героям Второй мировой."
    if (books['Художественная литература']['oseeva_v'].level >= 1) or (books['Серия "ЖЗЛ"']['jukov_general'].level >= 1):
        pass
    else:
        "Мозг машинально отметил факт — в этом мире тоже случались те же войны. Как минимум, эта."
    me "Понял."
    scene bg ext_path_day
    with dissolve
    "Молча мы преодолели ещё километр пути мимо оврага с валежником, пока я на расстоянии не увидел, что за окончившимся лесом начинается открытое поле. Там же у сходящихся троп на пьедестале красовался тёмно-зелёный танк с красной звездой на башне."
    show dv normal pioneer2 close at cleft with dissolve
    "Алиса сбавила шаг и остановила меня, схватив мой пионерский галстук так, словно это была узда."
    me "Угх!"
    dv "Тс-с!{w} Смотри, вот она!"
    show us laugh sport far at cright with dissolve
    "И правда, по броневой обшивке танка расхаживала Ульяна. Она играла: изображала, как отстреливается от врагов из автомата."
    show us sad sport far at cright with dspr
    "Наконец, она откровенно заскучала."
    show us smile sport far at cright with dspr
    "Вдруг, что-то нашло на неё, и девочка села на пушку и поползла по ней вперёд."
    hide us with dissolve
    "Двачевская перешла на шёпот."
    dv "Пойдём. Сначала я поговорю с Ульяной. Будет упираться — подам тебе знак. Хватай её за руки, а я за ноги."
    me "А если побежит?"
    show dv angry pioneer2 close at cleft with dspr
    dv "Догоним. Я-то смогу, а ты не будь лопухом, тоже беги изо всех сил."
    me "Так я не понял, какой сигнал будет?"
    show dv laugh pioneer2 close at cleft with dspr
    dv "М-м... Как подам, ты сразу поймёшь, что это сигнал."
    th "Зря она полагается на меня так легко, я бываю медленным."
    show dv normal pioneer2 close at cleft with dspr
    "Я хотел предупредить её, но не стал. Я кивнул, и Алиса отправилась к памятнику."
    hide dv with dissolve
    show us grin sport far at cright with dissolve
    "Непоседливая Ульяна уже добралась до конца пушки и заглядывала внутрь, словно намеревалась пролезть в неё."
    "Я отогнал прочь неприличные мысли."
    "Может быть, она хотела побывать в кабине танка, но не смогла из-за люка, закрытого сваркой?"
    show dv smile pioneer2 at cleft with dissolve
    dv "Привет, Уля."
    show us fear sport at cright with dspr
    us "Ой!"
    "Она едва не свалилась на траву, но успела схватиться обеими руками за пушку, повисла на ней, а потом спрыгнула."
    show us smile sport at cright with dspr
    "Девчонка всё ещё была грязной, и вдобавок она собрала вековой налёт пыли с танка."
    show us surp1 sport at cright with dspr
    us "Вожатые ищут меня?"
    dv "Нет. Но вожатые поручили нам отыскать тебя."
    show us surp2 sport at cright with dspr
    us "Но вы не сдадите меня им?"
    show dv normal pioneer2 at cleft with dspr
    dv "Нет. Но..."
    show us dontlike sport at cright with dspr
    us "А он что тут делает?"
    "Ульяна потыкала в меня пальцем, проигнорировав объяснения Двачевской."
    us "Он не должен знать об этом месте!"
    "Я примирительно раскрыл ладони."
    me "Не беспокойся, я просто за компанию пришёл."
    dv "В общем, от тебя требуется только помыться, и ты свободна."
    show us angry sport at cright with dspr
    us "Ни за что!"
    "Девчонка надулась."
    me "Не любишь мыться?"
    show us surp2 sport at cright with dspr
    us "Конечно не люблю, отстойней занятия не придумать!"
    show dv sad pioneer2 at cleft with dspr
    dv "Просто если вожатые снова застанут тебя в таком виде, то завтра нам троим не видать пляжа и купания как своих ушей."
    show us sad sport at cright with dspr
    us "Правда?"
    "Ульяна ещё немного сомневалась, поддаться нашим уговорам или нет."
    show us laugh sport at cright with dspr
    us "Пусть выкусят. Не буду мыться! А купаться завтра...{w} А купаться я прибегу, в домике меня никто не удержит!"
    show dv normal pioneer2 at cleft with dspr
    dv "Э-э..."
    "У Алисы иссякло терпение, и в дипломатике она явно не была сильна."
    show dv laugh pioneer2 at cleft with dspr
    dv "{b}ФАС!{/b}"
    show us calml sport at cright with dspr
    "Я мгновенно среагировал: поймал Ульяну за левую руку. Двачевская тоже не теряла времени и сразу схватила немытую подругу за лодыжки."
    show dv smile pioneer2 at center behind us with dspr
    show us fear sport at center with dspr
    "Мы подхватили её и понесли, когда я изловчился и вцепился в правую руку Ульяны."
    window hide
    stop music fadeout 1
    play music music_list["eat_some_trouble"] fadein 1
    scene bg ext_path2_day
    with dissolve
    show dv smile pioneer2 at center behind us
    show us fear sport at center
    with dissolve
    window show
    me "А-а-а-а-а!!!"
    "Я завопил, когда Ульяна оцарапала ногтями мои запястья."
    me "Вот зараза!"
    show us angry sport at center with dspr
    us "Лиска!"
    us "Предательница!"
    show dv guilty pioneer2 at center with dspr
    dv "Ты не понимаешь, дурочка, я тебя от бани спасаю, тебя же запрут на время праздника там, а не в домике."
    "Но Ульяна не унималась."
    us "Белка!"
    show dv normal pioneer2 at center with dspr
    th "Белка? Это что-то новенькое..."
    "Я не успел осмыслить, откуда взялось это прозвище, как раздался очередной выкрик Ульяны."
    us "Сучка!"
    show dv surprise pioneer2 at center with dspr
    th "Она серьёзно сказала это!"
    show dv laugh pioneer2 at center with dspr
    "Алиса только засмеялась."
    dv "Гляди, Семён, каких слов она понахваталась."
    me "Я умею складывать два и два. Вы живёте в одном домике..."
    show dv grin pioneer2 at center with dspr
    dv "Ага, моя школа!"
    "Я почувствовал гордость в её голосе."
    me "Ты не возражаешь, если я намылю ей язык за такое?"
    show dv smile pioneer2 at center with dspr
    dv "Да я сама... С удовольствием!"
    me "В ответе за тех, кого приручила?"
    us "Дваче!"
    show dv angry pioneer2 at center with dspr
    "Алиса не выдержала."
    dv "Тормозни, Семён. Я ей крапивку сделаю."
    show us fear sport at center with dspr
    us "Ненада!!1"
    "Двачевская взялась обеими руками за левую лодыжку Ульяны, а её освободившуюся ногу кедом придавила к земле, чтобы девочка не лягалась."
    us "Уй-уй-уй-уй-уй!"
    "Ульяна заголосила, претерпевая боль."
    show us angry sport at center with dspr
    "Наконец, пионерка притихла."
    me "Теперь мы квиты."
    dv "Нет, только я. Квитаться с Ульяной будешь сам."
    scene bg ext_stage_big_day
    with dissolve
    show dv normal pioneer2 at center
    show us upset sport at center
    with dissolve
    "Мы несли Ульяну всё дальше к лагерю. Кое-как смогли перебраться через забор и при этом не упустили девчонку — в один момент она едва не вырвалась от нас, но всё обошлось."
    show dv smile pioneer2 at center with dspr
    dv "Двигаем к умывальникам!"
    window hide
    scene bg ext_washstand_day
    with dissolve
    show dv smile pioneer2 at center
    show us angry sport at center
    with dissolve
    window show
    "Как только мы пришли на место, Алиса взяла вырывающуюся Ульяну под руки."
    show dv normal pioneer2 at center with dspr
    dv "Я буду держать, а ты умывай её."
    me "Нет, давай ты, я придумал, как поквитаться с ней..."
    show dv surprise pioneer2 at center with dspr
    dv "Ты куда?"
    me "Сейчас, подожди!"
    hide dv
    hide us
    with dissolve
    "Я отошёл подобрать замеченный мною шланг в траве, прикрутил его одним концом к поливальному крану для газона, повернул вентиль и вернулся."
    show dv normal pioneer2 close at center
    show us angry sport close at center
    with dissolve
    play ambience ambience_water_stream_closer
    me "Пионерка Сидорова Ульяна торжественно приговаривается к расстрелу за совершённые проступки на футбольном поле и в лесу..."
    show us fear sport close at center with dspr
    us "Эй! Эй! Семён!!!"
    "Кажется, Ульяна догадалась, что сейчас будет."
    "Я направил шланг ей в лицо, почти целиком сжав прорезиненный конец для усиления напора."
    play sound sfx_water_splash
    show us upset sport close at center
    show us dontlike sport close at center
    with dspr
    "Девчонка взвизгнула и замотала головой. Брызг было много, я намочил всю её футболку и шорты."
    show dv angry pioneer2 close at center with dspr
    "Двачевская прикрикнула на меня, чтобы я не задел и её."
    me "Тебе напомнить про вчерашнее утро с вёдрами?"
    show dv rage pioneer2 close at center with dspr
    dv "Не вздумай, идиот! Дай помыть Ульяну!"
    me "Ладно-ладно, мой."
    show dv normal pioneer2 close at center with dspr
    "..."
    show us upset sport close at center
    show dv smile pioneer2 close at center
    with dspr
    "Я стоял рядом, отведя шланг, а Алиса со смехом бережно стирала разводы грязи с сердитого личика Ульяны, лишь изредка прося меня плеснуть воды в девочку."
    "И чем чище становилась Ульяна, тем больше я заглядывался на неё, признавая, что она в самом деле очень даже милая."
    "А надувшаяся от негодования она казалась ещё и смешной, отчего невозможно было не улыбнуться всей этой сцене."
    show us laugh2 sport close at center with dspr
    "Ульяна жмурилась, словно кот, угодивший в душ. Такое сравнение показалось мне логичным — в ней много чего было от представителя семейства кошачьих — и царапается, и суётся во все щели, и мыться не хочет, не говоря уже о склонности подстраивать нехорошие сюрпризы в тапках."
    "Алиса перестала отмывать подруге лицо, когда та уже порядком успокоилась, перестав сопротивляться."
    show dv normal pioneer2 close at cright with dissolve
    dv "Всё, теперь ты больше не похожа на чумазика. Руки-ноги сама вымоешь?"
    show us dontlike sport close at center with dspr
    "Ульяна моргнула, смахивая капельки воды с ресниц и прищурилась, с ненавистью глядя на меня."
    th "И чего она молчит?"
    "Ульяна всё ещё держала щёки надутыми, будто набрала воды..."
    play sound sfx_water_splash
    "Я не успел увернуться, как девочка брызнула в меня сильной струёй, не хуже брандспойта, попав мне в глаза."
    me "Ау!"
    show dv laugh pioneer2 at cright
    show us laugh sport at center
    with dspr
    "Я даже отступил назад."
    me "Чёрт..."
    "Ульяна расхохоталась вместе с Алисой."
    me "Ну я тебе!"
    play sound sfx_water_splash
    show us laugh2 sport at center with dspr
    "Снова направив шланг и сжав его с краёв, я обдал и без того мокрую пионерку водой. Захлёбываясь от брызг и смеха, Ульяна пыталась защититься от гуляющей вверх-вниз струи."
    "Нетронутая Алиса веселилась, глядя на нас."
    me "Чё такая довольная? Может и тебя облить, а?"
    show us smile sport at cleft behind dv
    show dv angry pioneer2 at cright
    with dspr
    dv "В глаз получишь. Не водой, а кулаком."
    if sp_crg >= 2:
        me "Да ну?"
        "Осмелев, я облил и её."
        show us grin sport at cleft with dspr
        "Белая рубашка пионерки теперь была насквозь промочена, и я смог увидеть очертания лифчика."
        show dv rage pioneer2 at cright with dspr
        dv "А-ах ты..."
        if d1_tricked:
            "Вот теперь и мы квиты."
            $ d2_dv_quits = True
        show dv rage pioneer2 close at center with dspr
        "Алиса ринулась ко мне, и струя из шланга не остановила её. Я испугался и замешкался, но девочка не ударила меня кулаком, как грозилась, а схватила за руку и шланг, направив его мне на лицо."
        play sound sfx_water_splash
        me "Кха, тьфу!"
        show dv smile pioneer2 close at center with dspr
        "Воспользовавшись моментом, Двачевская и вовсе отняла у меня шланг."
        "В следующий миг облитым оказался я. Запинаясь, я попятился от неё и Ульяны."
        show us surp1 sport at cleft
        show dv smile pioneer2 at cright
        with dspr
        us "Дай мне! Дай мне, я тоже отомщу ему!"
        "Ульяна заскакала возле Алисы в нетерпении, и та с радостью поделилась шлангом."
        dv "Замочить этого гада? Всегда пожалуйста!"
    else:
        "Я не рискнул исполнить угрозу, решив, что вероятность схватить неиллюзорный тумак от Двачевской высока."
        show us smile sport close at center with dspr
        "И, зазевавшись, пропустил момент, когда Ульяна подбежала ко мне и схватилась за шланг. К счастью, я не выпустил его из рук."
        show dv smile pioneer2 at cright
        show us laugh sport close at center
        with dspr
        us "А ну отдай! Я хочу облить тебя! Имею право!"
        "Я потянул шланг в сторону, пытаясь рывком стряхнуть с него цепкую пионерку. Ульяна сжала конец прорезиненного шланга, и струя воды достала Двачевскую, крепко промочив её рубашку с плеч до груди."
        dv "А-ах..."
        show dv rage pioneer2 at cright with dspr
        "Сквозь ткань формы расплывчато виднелся лифчик Алисы." 
        th "Ох щи{font=DejaVuSansMono.ttf}~{/font}! Я увидел чуть больше, чем могла позволить Алиса!"
        "Она немедленно двинулась к нам."
        dv "Ты покойник, Семён!"
        me "Я не виноват, это всё Ульяна!"
        dv "Праотцам будешь сказки рассказывать!"
        show dv smile pioneer2 at cright with dspr
        "Стоило мне запаниковать, как Ульянка тут же присвоила себе шланг. А я кинулся прочь, немедленно получив удар струёй по спине и шее."
        show dv angry pioneer2 at cright with dspr
        dv "Ну-ка дай мне..." 
    hide dv
    hide us
    with dissolve
    "Я бы мог убежать к соснам вдалеке, где меня точно не достанут, но желание отыграться было сильнее, поэтому я спрятался за рядом умывальников, как за барьером."
    show dv laugh pioneer2 at cright
    show us smile sport at cleft
    with dspr
    "Алиса и Ульяна обошли умывальники сбоку, насколько им позволяла длина шланга, и снова окатили меня водой."
    me "Твою ж!.."
    hide dv
    hide us
    with dissolve
    "Я, как ужаленный, унёсся за дальний умывальник из тех, что стояли отдельно."
    "Смех девчонок быстро прекратился."
    dv "Блин, дальше шланг не тянется, размотали..."
    "Воцарилось молчание."
    "Тяжело дыша, я глянул на газон перед собой."
    th "И как же я буду отыгрываться?"
    "Другого шланга поблизости не обнаружилось."
    th "Да, такой расклад чересчур удачен, чтобы оказаться правдой."
    "Кафельная плитка холодила спину через мокрую рубашку.{w} Я раздумывал, что делать дальше.{w} Очевидно — надо было обойти девчонок и закрутить вентиль садового крана."
    "Только я наклонился влево, чтобы определить местоположение девчонок, как вдруг..."
    show us surp2 sport close at cright with dspr
    us "Бу!!!{w=0.2} Беги!"
    with vpunch
    "Она крикнула это прямо над ухом справа, да так внезапно, что я вздрогнул и стукнулся затылком об умывальник."
    me "Ай!.."
    "И вместо того, чтобы сорваться с места и убежать, я схватил пионерку за руку и дёрнул на себя."
    with hpunch
    show us fear sport close at center with dspr
    "А этого Ульяна совсем не ожидала..." 
    "Тут-то я и провёл захват лёжа, зажав Ульяне рот. Бедная мокрая девочка оказалась в плену моих объятий. Она беспомощно задёргалась на мне."
    us "М-м-ф!"
    dv "Ульяна?{w} Семён, ты что сделал?!"
    "Я был уверен, что для Алисы картина выглядела так: Ульянка наклонилась за умывальником, чтобы прикрикнуть на меня, а затем исчезла, смешно взмахнув ногами в воздухе."
    me "Поймал я твою бандитку!"
    "Их план был предельно ясен: Ульяна выгоняет меня с места, а Двачевская прицельно окатывает из шланга. Вот только всё провалилось ещё на первом пункте."
    show us angry sport close at center with dspr
    us "М-м-м!!!"
    "Я всё ещё мог обойти Алису и перекрыть напор воды. Теперь, как в компьютерных играх, я должен был свернуть шею пойманному неприятелю и перекатиться к соседним умывальникам."
    show us calml sport close at center with dspr
    th "Да разве у меня поднимется рука сделать этой девочке что-то плохое?.."
    show us dontlike sport close at center with dspr
    "Ульяна исхитрилась цапнуть зубами мой палец."
    "Я вскрикнул, но не отдёрнул ладони, жалея о последней мысли."
    show us angry sport close at center with dspr
    us "Офпуфти мня!"
    me "Фиг тебе."
    dv "Ну, хорош там прятаться! Вылезайте!"
    me "Не вылезем! Ты же обольёшь меня!"
    dv "Выйдешь по-хорошему, тогда я подумаю! Может, не оболью."
    dv "...А может и оболью."
    hide us with dissolve
    show dv normal pioneer2 far at left with dissolve
    "Я с осторожностью посмотрел за угол. Двачевская всё ещё стояла у края навеса, закусив губы в сомнениях."
    "У меня созрела идея."
    hide dv with dissolve
    me "Мы не выйдем, потому что мы кое-чем заняты. Кхм!"
    show us surp2 sport close at center with dissolve
    "Я с удовлетворением заметил, как глаза Ульяны расширились, когда она услышала это."
    show us angry sport close at center with dspr
    us "М-м-м!!!"
    th "Какой протестующий тон..."
    dv "Что ты несёшь?"
    me "Я мог бы сказать, чем заняты, но это слишком неприлично! Не для детских ушей!"
    me "Отгадай загадку: «Мальчик и девочка в траве что делали на «Е»?»"
    show us fear sport close at center with dspr
    us "{b}М-М!!!{/b}"
    "Это «м-м» Двачевская смогла услышать."
    dv "Какого чёрта, Семён?! Не смей трогать Ульяну!"
    hide us with dissolve
    show dv angry pioneer2 far at left with dissolve
    "Она уже была готова оставить шланг и прийти к Ульянке на помощь, чего я и добивался."
    "Нужна была капля, которая переполнит чашу терпения Алисы."
    hide dv with dissolve
    show us fear sport close at center with dissolve
    "И я решился..."
    "Отняв ладонь ото рта пленённой пионерки (на что она уже не надеялась), я рассчитанным движением шлёпнул Ульяну не то по ляжке, не то по заднице."
    show us surp2 sport close at center with dspr
    us "А-а!{font=fonts/DejaVuSansMono.ttf}~~{/font}"
    show us angry sport close at center with dspr
    us "СЕМЁН!!!"
    "Алиса бросила шланг и помчалась к нам, а я свалил опешившую девочку на траву и побежал по задуманному пути вокруг умывальников к тому оружию, что осталось лежать в пыли на поле брани."
    hide dv
    hide us
    with dissolve
    us "Алиса, шланг!"
    show us surp2 sport far at fright
    show dv surprise pioneer2 far at cright
    with dspr
    dv "Ульянка..."
    "Им обеим всё стало понятно, когда я завладел шлангом, но было поздно. Я ливанул водой в сторону Двачевской."
    hide dv
    hide us
    with dissolve
    "Алиса спряталась там же, где я секунду назад поймал её подругу."
    "Теперь я мог посмеяться над ними."
    me "Хар-хар! Вылезайте, моя очередь гонять вас."
    show us angry sport far at fright
    show dv angry pioneer2 far at cright
    with dissolve2
    $ renpy.pause(1)
    "Из-за умывальника медленно показались кулаки и две макушки: рыжая и красная. Чуть прищуренные глаза девчонок выражали предельную ненависть ко мне."
    dv "Извращенец."
    show us dontlike sport far at fright with dspr
    us "Просто идиот."
    "Я попробовал влепить струёй воды по девочкам, но их не достало."
    hide dv
    hide us
    with dspr
    th "Блджад."
    "Подумав немного, я попятился назад к вентилю, стараясь не упускать из виду место, где притаились две пионерки."
    "Железный кран темнел среди травы в шести метрах от площадки, их я уже пересёк бегом, чтобы скорей увеличить напор и показать зарвавшимся пионеркам, кто тут главный."
    "Полностью уверенный в своём превосходстве, я побрёл назад со шлангом наготове."
    show dv smile pioneer2 at cleft
    show us smile sport at cright
    with dspr
    "Не успел я дойти, как от умывальников под навесом ко мне наперерез побежали обе девчонки." 
    "Я инстинктивно окатил водой то одну, то другую, но их это не остановило — им уже было по барабану, ведь наша одежда и без того вымокла." 
    stop music fadeout 3
    th "Меня решили взять числом!"
    show dv smile pioneer2 close at cleft
    show us smile sport close at cright
    with dspr
    "Мой тактический гений оказался бессилен в эту секунду, и Алиса с Ульяной одновременно схватили шланг..."
    play music music_list["memories"] fadein 2
    show us grin sport close at cright with dspr
    "Втроём мы перетягивали его, и струя беспощадно била нас по рукам и лицу, взмывала вверх и накрывала фонтаном сверкающих на солнце брызг."
    "Двачевская пыталась крапивкой заставить меня разжать пальцы, но я был чуть посильней Ульяны и направлял шланг на Алису, и она снова отводила его, отпуская мою руку."
    "Ульяна старалась топнуть по моей ушибленной ещё на футболе ступне, но я вовремя отдёргивал промокший кед от её сандальки. Мы глядели вниз, и оттого струя воды ещё хаотичней металась по сторонам."
    "Но я не обижался на пионерок, в конце концов, все мы были в равном положении — мокрые и смеющиеся."
    "К тому же, прохладная волжская вода была настоящим спасением в жаркий день."
    "Сами того не ведая, вожатые дали нам повод устроить себе маленький оазис. Никто из нас уже не думал, последует ли за такое веселье соответствующее наказание."
    "И все несогласия между нами растаяли, как дым."
    "Время шло, и мы здорово устали. Наигрались так, что губы Ульяны уже казались синими."
    stop music fadeout 4
    show dv smile pioneer2 at cleft
    show us laugh2 sport at cright
    with dissolve2
    stop ambience fadeout 2
    "Я закрутил вентиль крана и бросил шланг рядом, опускаясь на траву, где уже расселись вразнобой Ульяна и Алиса."
    play music music_list["lightness"] fadein 2
    dv "Семён, тебе объявляется благодарность: молодец, хороший пёс. Жаль, что награду в виде рафинированного сахара я не принесла."
    me "Ты о чём?"
    show dv laugh pioneer2 at cleft with dspr
    dv "Команду «Фас» помнишь? Ты сразу правильно понял сигнал. Бросился на бедную Ульяну, как гончая."
    me "Ой, да ну тебя."
    show dv smile pioneer2 at cleft with dspr
    th "Спасибо, что с педомишкой не сравнила."
    "Ульяне показалось, что Двачевская похвалила меня."
    show us upset sport at cright with dspr
    us "Это Семён-то гончая? Обыкновенный бродяжка со двора."
    "Меня такой вариант устраивал, а Ульяна не ожидала, что я соглашусь. Хотя на самом деле я больше подходил эпитет «комнатно-декоративный»."
    show us normal sport at cright with dspr
    me "В точку, мне нравится. А ты, Алиса, почему Белка, а не Лиса Алиса? Нелогично."
    show dv angry pioneer2 at cleft with dspr
    "Девочка заметно напряглась."
    dv "Меньше знаешь, крепче спишь, Семён. Ульяна, кто тебя за язык тянул?"
    show us grin sport at cright with dspr
    "Девчонка продемонстрировала нам этот самый язык."
    us "Не надо было Семёна к танку приводить!"
    show us normal sport at cright with dspr
    us "Но мы бы тогда не поиграли..."
    $ lp_us = lp_us + 1
    "Я поднялся."
    me "Ладно, вы как хотите, я в домик, поскорей переодеться..."
    show us smile sport at cright with dspr
    "Ульяна скрутила край футболки и выжала его."
    us "Как будто нам переодеваться не нужно."
    mt_voice "Боже, что вы натворили?"
    show mt surprise pioneer at right behind us with dissolve
    "К нам подошла... нет, скорее, примчалась Ольга Дмитриевна."
    show dv surprise pioneer2 at left
    show us fear sport at cleft
    with dspr
    "Девочки подскочили и замерли вместе со мной."
    show mt rage pioneer at right with dspr
    mt "Я что вам сказала? Помыть Ульяну. А вы что?"
    show dv grin pioneer2 at left
    show us laugh2 sport at cleft
    with dspr
    me "Помыли её..."
    "Мы стояли в ряд перед вожатой, промокшие до ниточки, но почему-то всех нас распирало от удовольствия."
    show mt angry pioneer at right with dspr
    "Ольга Дмитриевна приложила к лицу ладонь."
    mt "Для мытья есть душевые, всегда открытые для пионеров, почему ты, Алиса, сразу не отвела Ульяну туда?"
    show dv guilty pioneer2 at left
    show us normal sport at cleft
    with dspr
    dv "Ну извините, мы не подумали."
    mt "Ох, что с вами делать?.. Марш по домикам переодеваться."
    show dv normal pioneer2 at left with dspr
    us "Так меня не накажут? Только не говорите, что я мылась зря!"
    show mt grin pioneer at right with dspr
    "Вожатая вдруг улыбнулась."
    mt "Нет, не зря, я побеседую с Ингой Максимовной. И через пятнадцать минут ужин."
    show us surp1 sport at cleft with dspr
    us "Так рано?"
    show mt smile pioneer at right with dspr
    mt "Сегодня перенесли на полвосьмого из-за вечернего, хм, мероприятия."
    mt "Почему вы ещё стоите здесь?{w} Вперёд!"
    hide dv
    hide us
    hide mt
    with dissolve
    "И мы разошлись — с радостью, потому что баловство не обернулось ничем плохим, и с печалью — из-за расставания, пусть даже всего на четверть часа."
    stop music fadeout 3
    "..."
    "......"
    "........."
    window hide
    $ d2_girls_event = (d2_girls_event) + (1)
    $ d2_us_dv_day = True
    jump d2_pre_event

label d2_gazette_club_day:

    $ reset_chibi("library")
    if gazette_club:
        scene black
        with dissolve
        show screen central_text("День 2 — Пионерская поддержка")
        $ renpy.pause(99, hard=False)
        hide screen central_text
    scene bg ext_library_day
    with dissolve
    play music music_list["my_daily_life"] fadein 2
    window show
    "Около библиотеки никого не было, кроме одной пионерки, сидевшей на лавочке с книгой в руках."
    if books_taken == 0:
        "Я сжал в кармане читательский билет, за которым зашёл к себе в домик по пути."
    if d2_mz_help:
        th "Ну, ставить книги на полки совсем не сложное занятие, если не лень ходить туда-сюда." 
        if books_taken == 0:
            "Заодно можно присмотреть для себя что почитать."
        "Я ещё подумал о водителе автобуса и тех коробках, упомянутых Женей."
        "Может быть, ради этого стоило заглянуть в блиблиотеку."
    elif (d2_mz_help == False) and (gazette_club == False):
        "Что-то подсказывало мне: как и утром, пионеры из кружка стенгазеты занимались всё тем же."
        "Достаточно было заглянуть в окна библиотеки, чтобы убедиться в этом. Две компании детей за столиками воодушевлённо писали и рисовали, переговариваясь друг с другом."
        "Я бы, конечно, предпочёл читать где-нибудь в сторонке от них в одиночестве."
        if books_taken == 0:
            th "Разумно сейчас зайти и выбрать себе книги, пока есть возможность — раньше возьму, больше прочитаю за смену."
            pass
        else:
            "Но раз я не записался к стенгазетчикам, то..."
            "Я двинулся обратно к площади, раздумывая, где ещё можно провести время до ужина."
            window hide
            stop music fadeout 1
            $ disable_current_zone()
            jump d2_day_map
    window hide
    scene bg int_library_day
    with dissolve
    play ambience ambience_library_day fadein 1
    window show
    if d2_mz_help:
        "Внутри меня сразу встретила Женя."
        show mz normal glasses pioneer at center with dissolve
        mz "Очень хорошо, что ты сдержал слово и явился. Давай приступим к делу."
        show mz bukal glasses pioneer at center with dspr
        mz "Вот таблица с наименованиями, в третьем столбце проставляй отметки напротив тех книг, что привезли, а во второй переписывай шифр книги." 
        "Она раскрыла случайно взятую книгу на странице после форзаца и показала, что именно надо переносить на бумагу — полочный индекс и авторский знак."
        show mz normal glasses pioneer at center with dspr
        mz "Я это всё потом внесу в библиотечный каталог, а ты расставишь их на полки."
        "Она дала мне планшет для бумаги и карандаш."
        "Никаких разговоров с отлагательствами — мы принялись за работу. Я раскрыл картонный короб, на который мне указала пионерка, а сама она занялась другим комплектом книг."
        "Первые шесть маленьких томиков — сборники стихов малоизвестных мне поэтов. За ними книга шведской писательницы, пара сказок и детская повесть о пионерах."
        "Всё, что я брал в руки, я проверял и отмечал в таблице, не забывая о библиотечном описании, а потом откладывал в стопку на стул."
        "И, что самое обидное, ничего связанного с автобусом. Никаких косвенных подсказок или записок."
        "Просто книги."
        "Зато они вызывали приятные воспоминания о тех детских годах, когда я с упоением читал подобные вещи."
        show mz bukal glasses pioneer close at center with dissolve
        "Послышался зевок, и я обратил внимание на Женю, на мгновение прикрывшую рот ладонью, прежде чем снова вернуться к списку книг." 
        show mz normal glasses pioneer close at center with dspr
        "Девочка выглядела усталой, сонливой, как будто сегодняшней дрёмы во время моего обхода по кружкам ей не хватило."
        "Можно было подумать, что этой ночью она не спала. Или, может быть, она просто сова — из тех, кому лучше просыпаться позже, а не так рано, когда у нас подъём на зарядку."
        "Размышляя об этом, я несколько отвлёкся от бумажно-книжной работы и засмотрелся на Женю. Слегка округлые черты лица, маленький аккуратный нос, на котором как-то держались крупные очки." 
        "Девочка была самим воплощением серьёзности: она усердно переписывала информацию, чуть поджав губы и не обращая внимания на происходящее вокруг. И всё-таки было что-то милое в этой строгости."
        "Наконец, Женя почувствовала на себе мой взгляд."
        show mz bukal glasses pioneer close at center with dspr
        mz "Ты чего замер, Семён? Не медли, работа сама себя не сделает."
        me "А... Да, извини. Просто задумался."
        show mz normal glasses pioneer close at center with dspr
        "Женя продолжила, как ни в чём не бывало, не поняв, из-за чего, вернее, из-за кого я отвлёкся."
        "Получив моральный пинок, я опять взялся за книги, но мои мысли всё ещё занимала та странность, окружавшая личность Жени."
        hide mz with dissolve
        "......"
        $ d2_mz_helped = True
        $ disable_current_zone()
        $ lp_mz = lp_mz + 1
        $ d2_girls_event = (d2_girls_event) + (1)
        "........."
        "Мы закончили с перечнем книг, и я отдал пионерке лист со всеми индексами и отметками. Женя ушла с ним к компьютеру, поручив мне расставить привезённые книги на полки."
        hide mz with dissolve
        if books_taken >0:
            "Всё, что хотелось прочесть, я уже взял в тихий час. Поэтому я не задерживался у стеллажей в поисках книг, которые могли бы заинтересовать меня."
        else:
            "Дело было непыльным (хотя в прямом смысле оно являлось именно таковым), и я заодно высматривал, какие книги можно взять."
            "Даже при скромных размерах библиотеки, я нашёл здесь всё, что могло бы мне пригодиться."
            call take_books
            if books_taken >0:
                $ d2_books_chosen = True
                "Я отнёс выбранное на стол к Жене, на что она первым делом поинтересовалась, расставил ли я все книги."
                show mz normal glasses pioneer close at center with dissolve
                me "Да, я всё сделал, можно не проверять."
                show mz bukal glasses pioneer close at center with dspr
                mz "Мало ли. Я обязательно посмотрю..."
                "Она снова зевнула перед тем как написать дату возврата в моём читательском билете."
                show mz normal glasses pioneer close at center with dissolve
                mz "...Потом."
                hide mz with dissolve
        if tech_club:
            th "Наверно, Электроник и Шурик уже заждались меня."
            "Не сказать, что я горел желанием находиться в их обществе, но они пообещали рассказать мне про своего робота."
            window hide
            stop music fadeout 1
            jump d2_tech_club_day
        elif (tech_club == False) and (gazette_club == False):
            "В том, что я помог Жене, безусловно не было ничего плохого, однако возня с книгами уже заметно поднадоела мне. Надо обладать усидчивостью, чтобы терпеть подобную работу."
            "Или, как это умеет Женя, спать между делом."
            "Но я не записался в редколлегию стенгазеты и уж тем более не стал помощником библиотекаря, поэтому здесь я только понапрасну терял время."
            "Меня ждал свой кружок, а в идеале я вообще мог прогулять занятие и поплутать в окрестностях лагеря."
            th "Отличная погода же!"
            window hide
            stop music fadeout 1
            jump d2_day_map
    else:
        "Не обращая внимания на пионеров, я прошёл к шкафам с книгами."
        th "Так, где мои Пинчон, Сорокин и «Сказки тёмного леса»?"
        "Я одёрнул себя: это ж детская библиотека!"
        call take_books
        if books_taken >0:
            "Женя отметила у себя, что я взял, и сделала напутствие, как обращаться с книгами вне библиотеки."
        elif books_taken == 0:
            "Я ушёл из библиотеки, так ничего и не выбрав."
        window hide
        stop music fadeout 1
        $ disable_current_zone()
        jump d2_day_map
    if gazette_club:
        stop music fadeout 1
        play music music_list["so_good_to_be_careless"] fadein 2
        th "Раз в клуб чтения и пионерской стенгазеты я вступил не просто так, надо бы подойти к ребятам и узнать, что и как они делают."
        "Все пионеры, собравшиеся в библиотеке, разделились на две группы — каждая за своим столиком. Дети читали журналы или писали свои заметки." 
        "Я подошёл к редколлегии своего отряда."
        show un normal pioneer at cright with dissolve
        "Лену я увидел сразу — она рисовала кому-то вокруг готовой заметки орнамент, не то в виде плюща, не то в виде лозы винограда."
        hide un with dissolve
        "Пионеры говорили почти шёпотом, дабы не нарушать главное правило библиотеки и не вызывать гнева ответственной Жени."
        "С края столика был один свободный стул, и я занял его. Мой взгляд упал на бумажный лист с неоконченной заметкой."
        th "Прочитать что ли?"
        "Не успел я что либо сделать, как ко мне обратилась пионерка, занимавшая место рядом."
        girl_A "Извини, Семён, вообще-то тут сидит Света."
        me "А где она?"
        girl_A "Отошла."
        me "Когда придёт, я освобожу место. Можно глянуть?"
        "Я показал на лист с заметкой."
        girl_A "Да, пожалуйста."
        "Я начал читать, и уже с самого начала был поражён количеством глуповатых ошибок, встречавшихся там и сям."
        "И для меня это было особенно неприятно после нескольких лет пребывания на форумах, где у некоторых посетителей проверка грамотности со временем становилась таким пунктиком, что над пишущими с опечатками насмехались, а если сами допускали ляпы, то старательно поправляли себя в следующем посте и извинялись за неровный почерк."
        th "А ведь в старшем отряде всем уже по пятнадцать-шестнадцать лет..." 
        me "Как можно писать настолько неграмотно?"
        "Последняя фраза вырвалась у меня из уст, да так, что все с недоумением обернулись на меня."
        #show lir
        lir "Э! Это вообще-то моё!"
        "Я встретился глазами с каким-то пионером, сидевшим в редколлегии младшего отряда. Его я узнал сразу — это он вчера вместе с братом-близнецом помогал Алисе в розыгрыше с вёдрами."
        "Казалось бы, после неловкого момента я должен был тихим голосом извиниться и заткнуться, но я вдруг решил высказать пионеру всё, что думаю."
        me "Ты в каком классе учишься? Седьмом-восьмом? Пора бы уже знать, что воин во множественном числе пишется через «и», а не через «и» краткое..."
        me "А за неверное написание «тся» и «ться» мне хочется ударить тебя ломом по пальцам.{w} Тут ещё есть перл, достойный смешных выдержек из школьных сочинений..."
        "Кто-то из детей зашикал на меня, некоторые стали перешёптываться между собой."
        girl_A "Ну-ну, зачем на Лирического нападаешь? Ему про свои проблемы известно, а Света как раз проверяет его заметки и поправляет ошибки."
        $ meet('lir', u"Лирический")
        me "Да?.. Я не знал..."
        show un shy pioneer at cright with dissolve
        "Я немного растерялся под взглядами пионерской братии, в том числе и Лены, чьё внимание я привлёк своим вызывающим поведением. Она была смущена, и я не совсем понимал, из-за чего."
        "И мне показалось, что Лена не осуждала меня..."
        hide un with dissolve
        "Паренёк совсем сник, расстроившись, хотя я не слишком сильно отчитал его. Но, ощутив поддержку детей, Лирический выплеснул на меня обиду."
        lir "Критиковать всегда просто! Попробуй сам написать что-нибудь!"
        me "Не нужно быть поваром, чтобы оценить блюдо."
        lir "Так ты же вступил в наш кружок!" 
        lir "Не хочешь, а придётся! Вот мы и посмотрим, как у тебя получится."
        "Возразить я не смог и тем самым принял вызов от младшего пионера, сам того не желая."
        me "Хорошо. Так и быть, напишу. Это несложно. А о чём надо?"
        lir "Сам придумай, умник!"
        th "Ох, кажется, я взял на себя обязательство, из-за которого надо в лишний раз потрудиться. Чёрт."
        #show dt
        "Пришла та самая Света — одетая в лёгкий голубой сарафан девочка с прямыми золотистыми волосами, одна прядь которых выбивалась на макушке, подобно антенне. Выглядела Света немного рассеянной, но её зелёные глаза были добрыми, как и её кроткая улыбка."
        "Оказалось, что она ходила за новой баночкой замазки-корректора, чтобы вычистить все ошибки Лирического."
        "Я уступил ей место."
        th "Да, Свете досталось совсем неблагодарное дело."
        "Но она, похоже, сама взялась за него по доброте душевной."
        #hide dt
        th "А вот я буду работать по принуждению. О чём бы написать?"
        th "И кто вообще придумал эти занятия для летнего лагеря, где пионеры, по идее, должны отдыхать, а не пахать с утра до вечера?"
        "Я принёс от дальнего столика незанятый стул и присоединился к своему отряду, сев на углу рядом с Леной."
        me "Извините, у вас в редколлегии есть главный редактор?"
        "Совсем близко послышался тихий девичий голос."
        show un normal pioneer close at cright with dissolve
        un "Это я..."
        th "Не ожидал, что так удачно сяду — рука об руку с главредом."
        me "Мне бы тему для заметки выбрать. Подскажешь что-нибудь?"
        show un shy pioneer close at cright with dspr
        "Она помедлила с ответом, словно что-то мешало ей начать говорить со мной."
        th "Уж не из-за других пионеров ли это?"
        un "Ну... Можно писать буквально обо всём, если есть мнение и его хочется выразить."
        me "Авторская колонка?"
        un "Вроде того."
        th "А что, можно регулярно вести колонку, переполненную ненависти ко всему сущему. Тема первого выпуска — неграмотность..."
        un "Но мы обычно пишем о прошедших мероприятиях и о календарных праздниках, международных или отечественных. Рецензии, советы...{w} Иногда что-то образовательное или творческое. Реже — про злободневные проблемы в отношениях среди пионеров."
        show un sad pioneer close at cright with dspr
        un "...Без сплетен и клеветы, конечно."
        "В порядке бреда и разыгравшегося воображения я представил себе полные желтизны материалы о том, кто чьи признания отверг, кто кого в лагере за что полапал, абсурдные и кричащие заголовки, прогнозы конца света, личные встречи с инопланетянами, — и всё это в пионерской стенгазете."
        "Будет весело, пока цензурный комитет в лице вожатых, маниакально смеясь, не выжжет эту ересь огнём."
        me "Да, я понимаю. Надо просвещать, а не развращать."
        show un surprise pioneer close at cright with dspr
        "Лена залилась краской на миг, замолчав, и я помог ей вернуть самообладание."
        me "Так за что мне можно взяться?"
        show un shy pioneer close at cright with dspr
        un "М-м..."
        show un smile pioneer close at cright with dspr
        un "Завтра у нас День Нептуна — это большое мероприятие! Хочешь, напиши о нём."
        "Лена поинтересовалась у пионеров, собирался ли кто сделать заметку на ту же тему, и оказалось, что других кандидатов не нашлось."
        th "Как будто все сговорились!"
        show un shy pioneer close at cright with dspr
        un "На самом деле, у тебя непростая задача."
        me "Почему?"
        show un sad pioneer close at cright with dspr
        un "Подобные мероприятия происходят в каждой смене, и пишут о них почти каждый раз." 
        un "Например, пионеры разных смен начинали заметки об одном и том же мероприятии с истории возникновения праздника, едва ли не слово в слово, потому что пользовались одной книгой-первоисточником из нашей библиотеки."
        un "Некоторым трудно быть оригинальным и не повторяться." 
        me "Но можно быть искренним."
        show un smile pioneer close at cright with dspr
        un "Верно!{w} Однако для чего-то серьёзного всё равно потребуется терпение, чтобы набить руку и хорошо выполнять свою работу..."
        "Я глянул на выведенный девочкой орнамент вокруг заметки."
        me "Это как с рисованием?"
        show un shy pioneer close at cright with dspr
        un "Да."
        me "Хорошо бы почитать все заметки про День Нептуна в предыдущие смены..."
        un "!.."
        show un smile pioneer close at cright with dspr
        un "Только что хотела сказать тебе об этом! Давай я принесу нужные выпуски из архива. Ещё возле Зелёного Театра висят стенгазеты прошлой смены, можешь почитать заметки других пионеров." 
        me "Отлично, спасибо!"
        me "Только необязательно мне приносить, я тоже пройдусь."
        show un normal pioneer at cright with dissolve
        show mz normal glasses pioneer at cleft with dissolve
        "Мы подошли к Жене, пополнявшей базу книг на компьютере."
        un "Можно в архив? Покажу несколько прошлых стенгазет Семёну."
        "Пионерка дала ей связку из трёх ключей."
        mz "Пожалуйста. Не забудь вернуть ключи мне до ужина."
        "..."
        window hide
        stop ambience fadeout 1
        stop music fadeout 1
        scene bg ext_library_day
        with dissolve
        play music music_list["timid_girl"] fadein 2
        window show
        "Далеко идти не пришлось — архивом оказалась небольшая пристройка возле библиотеки."
        show un normal pioneer at center with dissolve
        "Лена открыла дверь и включила свет в этой тесной каморке с двумя стеллажами запылённых книг и коробками на полу."
        un "Подожди немного..."
        me "Хорошо, я никуда не тороплюсь."
        "Девочка сняла кипу листов крупного формата и файловых папок с полки и начала перебирать их."
        "Да, пионерского творчества тут скопилось много, хоть прямо сейчас устраивай избу-читальню. Только не хватает удобного кресла и яркой лампы рядом."
        "Я по старой привычке коснулся переносицы, поздно сообразив, что уже не ношу очки, к тому же, они сломались в автобусе."
        me "Тут довольно темно, может, пойдём на улицу?"
        un "Давай."
        show un normal pioneer at cleft with dissolve
        "Мы вынесли стенгазеты из каморки и сели на лавочке у дорожки так, что кипа бумаг разделила нас — девочка в тени, а я на солнечной стороне. Может, Лена просто неосознанно отгородилась от меня."
        "Она просматривала старые заметки, а я наблюдал за ней."
        me "Мне один вопрос не даёт покоя."
        show un sad pioneer at cleft with dspr
        un "...Какой?"
        me "Утром я делал обход по бегунку, и узнал, что тут есть студия ИЗО для пионеров. Если тебе нравится рисовать, почему ты не там, а в кружке стенгазеты?"
        show un smile pioneer at cleft with dspr
        un "А...{w} Я уже несколько лет после уроков посещаю художественную школу, когда есть возможность..."
        show un surprise pioneer at cleft with dspr
        un "Т-т-только не подумай, будто я хотела сказать, что рисую лучше всех пионеров из кружка по ИЗО и поэтому не с ними!.. Они талантливые и ни в чём не уступают мне..."
        show un shy pioneer at cleft with dspr
        un "Просто решила попробовать что-нибудь другое. Когда наш отряд обходил клубы и секции, Ольга Дмитриевна предложила мне побыть во главе редколлегии, а я согласилась."
        show un smile pioneer at cleft with dspr
        un "Сначала сомневалась, правильно ли я сделала, но потом привыкла. У нас хорошие ребята!"
        me "Верю."
        show un normal pioneer at cleft with dspr
        "Я замолчал, опёрся о лавочку и распрямил плечи, подставив лицо солнцу."
        "В библиотеку мимо нас прошли несколько пионерок, которых я видел в кружке юннатов."
        "Пару минут спустя Лена отобрала несколько листов из файловых папок, в которых лежали заметки прошлых смен."
        show un smile pioneer at cleft with dspr
        un "Этого будет достаточно."
        "Мы поднялись."
        show un normal pioneer close at center with dspr
        me "Спасибо за помощь. А когда дедлайн?"
        show un smile pioneer close at center with dspr
        un "Напиши к среде или четвергу, не позже."
        me "Ладно.{w} Если с Днём Нептуна не выйдет, я сделаю колонку. Про неграмотность."
        show un shy pioneer close at center with dspr
        "Вдруг Лена, еле удерживая папки и стенгазеты одной рукой, тронула меня за рубашку — у локтя."
        un "Знаешь, Семён, мне кажется, у тебя всё получится!"
        show un smile pioneer close at center with dspr
        me "Ух, спасибо... Ещё раз."
        "От слов поддержки я точно воспарил духом."
        show un shy pioneer close at center with dspr
        "В смятении от невозможности подыскать слова для разговора, мы притихли, стоя рядом."
        "От неловкого положения нас спасла Ольга Дмитриевна."
        show un shy pioneer at cright
        show mt grin pioneer at cleft
        with dissolve
        mt "Чем заняты, пионеры?"
        me "Да вот, думаю, как написать для стенгазеты про День Нептуна, искали примеры в архиве."
        show mt smile pioneer at cleft with dspr
        mt "Рада слышать, что вы не сидели без дела."
        mt "Я пришла сказать, что у нас ужин сегодня будет в половине восьмого, так что окончить занятия в кружке и закрыть библиотеку вам надо раньше обычного."
        show un smile pioneer at cright with dspr
        un "Я поняла, Ольга Дмитриевна. Я передам остальным."
        "Она проверила на всякий случай, не забыла ли ключи, которые дала ей Женя."
        hide mt with dissolve
        show un smile pioneer at center with dspr
        "Убедившись, что у нас всё в порядке, вожатая всё с той же загадочной улыбкой ушла."
        "..."
        "Лене пришлось снова зайти в архив, чтобы положить стенгазеты на место."
        if d2_books_chosen:
            window hide
            scene bg int_library_day
            with dissolve
            play ambience ambience_library_day fadein 1
            show un normal pioneer at center with dissolve
            window show
            "Мы вернулись в библиотеку. Лена, как обещала, сообщила пионерам об ужине, а я забрал книги."
            th "По крайней мере, есть что почитать в тихий час или свободное время до ужина, и Ольга Дмитриевна не скажет, что я бездельничаю."
            me "Лена, я сейчас пойду к себе, а завтра после мероприятия попробую написать что-то."
            show un smile pioneer at center with dspr
            un "Хорошо! А я обязательно прочитаю."
            "И я ушёл из библиотеки."
            window hide
            stop ambience fadeout 1
            stop music fadeout 1
        else:
            me "Э-э... Тогда завтра после мероприятия я попробую набросать черновик..."
            un "Хорошо! А я обязательно прочитаю."
            "На том мы разошлись."
            window hide
            stop music fadeout 1
            hide un with dissolve
        scene bg ext_houses_day
        with dissolve
        play music music_list["two_glasses_of_melancholy"] fadein 2
        window show
        "По пути в домик мне вспомнились попытки Лены спокойно и непринуждённо говорить при остальных и та заминка, на которой прервалась наша беседа."
        th "Она явно не склонна быть общительной, и в кругу людей ей приходится перебарывать этот маленький недостаток."
        th "Может, Ольга Дмитриевна предложила Лене руководить кружком, чтобы клин клином вышибить?"
        "Пока я провёл в лагере слишком мало времени и ещё не очень хорошо знал всех, чтобы делать выводы о таких вещах." 
        "А наедине, как сейчас со мной, Лена вряд ли сможет подолгу поддерживать разговор, надо самому подталкивать её вопросами и быть готовым стать рассказчиком, а не только слушателем – в этом я уже убедился."
        "Иначе мы оба будем стоять и молчать, не зная, что сказать, пока не пройдёт день."
        "Смешно."
        "Она напомнила мне меня на первом курсе – тихого и замкнутого. Я не был активным и избегал контактов с другими из-за своего характера – одна из причин, почему я предпочёл стать затворником."
        "Сейчас, если от меня потребуется что-то произнести, я буду выдавать всякие нелепости."
        "Разница в том, что Лена ещё могла измениться, а мне, наверно, поздно меняться."
        "А вот это уже было грустно."
        window hide
        scene black
        with dissolve
        window show
        "..."
        "......"
        "........."
        window hide
        stop music fadeout 2
        $ d2_un_day = True
        $ lp_un = lp_un + 1
        jump d2_pre_event

label d2_clubs_day:

    scene bg ext_clubs_day
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    window show
    "Немного странно, что на улице отличная погода, а пионеры сидят в четырёх стенах и занимаются, как в школе, будто летние каникулы даже не начинались."
    "С другой стороны, не каждый же раз они пропадают в здании клубов на шесть часов с обеденным перерывом?"
    "Просто сегодня объявили день кружковых занятий."
    "Я не был против такого объяснения. Мне и самому стало любопытно, как пионеры вместе проводят время и чем занимаюся в клубах."
    if (unnat_club == True) or (modeller_club == True) or (chess_club == True):
        "Тем более, я записался в один из местных кружков."
    "Войдя в коридор, подстёгиваемый всё тем же любопытством, я попробовал открыть дверь, за которой трудились кибернетики — их голоса я хорошо расслышал."
    "Она была заперта. Шурик и Сыроежкин, как видно, серьёзно решили пускать только по стуку на азбуке Морзе. Из всех пионеров пароль должен был знать я."
    "Вот только я уже не помнил, как надо стучать."
    th "Окуклились. Ну и ладно. Я и так в свой кружок опаздываю."
    window hide
    menu:
        "Зайти к юннатам" if (d2_times_been_to_unnat_club != 2):
            if d2_times_been_to_unnat_club == 1:
                scene bg ext_clubs_day
                with dissolve
                window show
                "Приоткрыв дверь и не заходя внутрь, я снова заглянул к юннатам."
                "Обсуждавшие что-то пионеры замолчали, когда я показался на пороге."
                show sl smile pioneer at cright with dissolve
                sl "Может, всё-таки останешься с нами?"
                th "Напрасно я вернулся."
                me "Нет... Хотел спросить, но раздумал... Извините за беспокойство."
                hide sl with dissolve
                "Сгорая от чувства неловкости, я ушёл."
                window hide
                $ d2_times_been_to_unnat_club = 2
                jump d2_day_map
            stop music fadeout 1
            jump d2_unnat_club_day
        "Зайти к моделистам" if (d2_times_been_to_modeller_club == 0):
            stop music fadeout 1
            jump d2_modeller_club_day
        "Зайти в кружок настольных игр" if (d2_times_been_to_chess_club == 0):
            jump d2_chess_club_day

label d2_unnat_club_day:

    if (unnat_club == False):
        play music music_list["my_daily_life"] fadein 1
        window show
        "Я решил проведать юных натуралистов: может, у них происходит что-то интересное."
        "Пионерки за круглым столом негромко беседовали, а мальчик младшеотрядник сверял записи в тетради с книгой."
        #show iie
        #show hai
        "Из разговора девочек я уловил, что участники кружка собираются провести какие-то наблюдения на природе."
        hai "Ой, Славя, по-моему, к нам кто-то хочет зайти!"
        th "Вот и конец шпионству."
        show sl smile pioneer at cright with dissolve
        "Славя с добродушной улыбкой раскрыла дверь."
        sl "В чём дело, Семён?"
        me "Да так, интересно стало, чем вы занимаетесь..."
        show sl smile2 pioneer at center with dspr
        sl "Хочешь с нами побыть? Присоединяйся!"
        me "Нет, пожалуй, я просто мимо проходил, немного подслушал разговор. Прошу прощения."
        show sl normal pioneer at center with dspr
        sl "А всё-таки..."
        me "В другой раз, может быть."
        "Я бросил нечто вроде прощального взгляда на пионеров и вышел в коридор с непонятным чувством смятения."
        #hide iie
        #hide hai
        hide sl with dissolve
        "Дверь закрылась, но я услышал чей-то весёлый голос."
        ci_voice "Да понравилась ему какая-то девочка, вот и заглядывает!"
        "Последовал смех пионеров, однако быстро умолкший."
        sl "Саша! Не очень вежливо говорить такие вещи!"
        th "В самом деле!"
        "Очень хотелось снова зайти и возразить той девчонке с предубеждением насчёт меня... Но я возвратился на улицу, повременив с резкими действиями."
        window hide
        stop music fadeout 1
        $ d2_times_been_to_unnat_club = 1
        jump d2_day_map

    $ reset_chibi("clubs")
    scene black
    with dissolve
    show screen central_text("День 2 — Наблюдай всё")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_clubs_day
    with dissolve
    play music music_list["everyday_theme"] fadein 1
    window show
    "Сложно было сказать, зачем я записался к юным натуралистам — я никогда не проявлял особого интереса к тому, чем они занимаются."
    "Я надеялся, что юннаты помогут мне хоть как-то занять время."
    "..."
    "Все юннаты уже были на своих местах за круглым столом, подобно героям из легенд о короле Артуре. Слава рыцаря мне явно не светила, скорее, роль волшебника Мерлина, когда стукнет тридцать."
    "Один я стал опоздавшим."
    th "В который раз, если припомнить вчерашний день."
    me "Я вас не отвлёк?"
    show sl smile2 pioneer at center with dissolve
    sl "Ничего, мы бы без тебя всё равно не начали."
    me "Правда?"
    show sl smile pioneer at center with dspr
    sl "Конечно, садись сюда." 
    "Она пригласила меня сесть рядом, и я не отказался."
    show sl normal pioneer at center with dspr
    sl "Тебя надо познакомить со всеми."
    "Славя вежливо представила меня юннатам, а потом рассказала мне о них."
    show sl smile pioneer at center with dspr
    sl "Это сёстры Инна и Аня Данетко из нашего отряда..."
    #show iie
    #show hai
    if d1_un_evening:
        me "А мы уже знакомы, они вчера Электроника увели играть."
        "Фраза была абсолютно невинной, но я опять вызвал смех у всех юннатов, кроме одного мальчика, сидевшего рядом с аквариумом."
        th "Да что я сказал такого?"
        "Славя, улыбаясь, призвала пионеров к спокойствию."
        th "Надо привыкать к обществу девчонок и к их, хм, едва поддающихся толкованию реакциям."
    else:
        $ meet('hai', u"Аня")
        $ meet('iie', u"Инна")
        "Одна из девочек, которую назвали Аней, беззастенчиво разглядывала меня, а её соседка, своим видом походившая на типичную правильную отличницу, наклонилась к ней и что-то шепнула на ухо, чем заставила Аню снова искоса посмотреть в мою сторону с загадочной усмешкой."
        th "Надеюсь, они не меня обсуждают..."
    sl "А это Саша Снежина из младшего отряда."
    $ meet('ci', u"Саша")
    #show ci
    "Я глянул на весёлую девочку с голубыми волосами, подвязанными бантом. Она, улыбаясь во весь рот, показала мне знак мира."
    show sl happy pioneer at center with dspr
    sl "За ней нужен глаз да глаз! Так что, Семён, если я буду отсутствовать, а ты увидишь её с банкой, в которой сидит пойманная лягушка, не пускай Сашу к холодильнику."
    ci "Разве мы собрались тут не для учёбы и экспериментов? Это же эксперимент! Славя, почему ты мне не разрешаешь?"
    show sl smile2 pioneer at center with dspr
    sl "Потому что ничего хорошего с лягушкой не будет, поверь."
    "Под смех юннатов девочка надулась и постучала сжатыми от негодования кулаками по столу."
    ci "Нет, ну почему?! Пока не попробуешь — не узнаешь!"
    th "Хм, в самом деле, а что может случиться?"
    show sl normal pioneer at center with dspr
    "От глупой мысли меня отвлекла Славя, знакомя с оставшимися тремя пионерами. Все они были из младшего отряда, и ни с кем из них я ещё не пересекался."
    "Если не считать смеха девочек и непонятных взглядов, меня приняли спокойно."
    show sl smile pioneer at center with dspr
    sl "Сегодня мы проведём занятие в свободном порядке. Есть предложения?"
    girl_A "Как насчёт викторины?"
    iie "Нет, не стоит, к викторине нужно готовиться заранее, ведь за правильные ответы отряд получает баллы, а сейчас, когда Семён в первый раз с нами и не готов, это будет немножко нечестно по отношению к нему, верно?"
    me "Вообще-то да. Я закончил...{w} учебный год..."
    "Я чуть не сказал, что уже давным-давно получил среднее образование и больше не задумывался о школьной программе."
    me "...И совершенно всё позабыл."
    "Все покивали, соглашаясь с Инной."
    show sl happy pioneer at center with dspr
    sl "Это не страшно, у нас тематические викторины, мы всё подробно расскажем и напомним тебе!"
    girl_B "Может быть, поговорим о рыбах и других обитателях морей и рек? У нас же завтра День Нептуна."
    "Славя улыбнулась."
    show sl smile2 pioneer at center with dspr
    sl "Вы раскрыли мои планы. Я собиралась задать вам это на дом." 
    th "Ну точно всё как в школе.{w} Зато сбывается та пришедшая мне в голову мысль о Славе-учительнице. Не хватает только указки, очков и... личной провинности, чтобы остаться после занятия на внеурочный час."
    show sl smile pioneer at center with dspr
    sl "Ольга Дмитриевна говорила, что для юннатского кружка организуют небольшой конкурс, поэтому... Да, вам стоит посвятить немного времени подготовке." 
    sl "Ничего сложного и мудрёного быть не должно, однако я отпущу вас пораньше, вдруг, захочется взять нужные книги или журналы в библиотеке."
    hai "Так и сделаем!"
    show sl surprise pioneer at center with dspr
    sl "Ещё предложения?"
    iie "Можно сходить всем вместе на поле."
    show sl smile pioneer at center with dspr
    hai "Я за! К тому же, если бы у нас была инициация в юннаты, то мы бы заставили Семёна поймать там свою первую бабочку..."
    show sl surprise pioneer at center with dspr
    th "И откуда такие фантазии берутся?"
    me "Что, прости?"
    show sl laugh pioneer at center with dspr
    "Славе стало смешно."
    sl "Интересная идея, только если Семён в школе ещё не был членом юннатского кружка." 
    show sl surprise pioneer at center with dspr
    sl "Ты ведь не был, так?"
    me "Нет, я ни в каких кружках не состоял. Только в футбол играл."
    show sl smile pioneer at center with dspr
    sl "Посвящение в юннаты есть, и оно проводится, по крайней мере, так было у нас."
    show sl sad pioneer at center with dspr
    "Она вдруг задумалась, будто о чём-то серьёзном, потому что улыбка пропала с лица девочки. Славя приложила пальцы к губам."
    boy_A "Давайте в лес, а то я в прошлый раз я не успел закончить наблюдения за клестами. По-хорошему надо всё об этом месте написать, а уж потом на поле." 
    show sl normal pioneer at center with dspr
    ci "Давайте-давайте! Пойдём в лес!"
    th "Легко догадаться, зачем ей надо туда."
    "Мнения разделились."
    show sl happy pioneer at center with dspr
    sl "Проголосуем?{w=0.3} Кто за поле?"
    show sl smile2 pioneer at center with dspr
    "Подняли руки Инна и её сестра. Обе были удивлены, что к ним не присоединилось большинство. Пионеры младшего отряда оказались единодушны в решении пойти в лес."
    show sl surprise pioneer at center with dspr
    sl "Семён, а ты почему не голосовал?"
    me "Так и ты тоже не стала. Чтобы выбор состоялся, хоть кто-то должен поднять руку в пользу одних и против других. Это и произошло сейчас: из шести больше половины за лес."
    me "Для меня разницы нет, и я сам не очень понимаю, куда имеет смысл пойти."
    show sl smile pioneer at center with dspr
    "Славя согласилась."
    sl "Тогда на поле идём завтра, а сейчас в поход. Возьмите полевые сумки со всем необходимым, собираемся около музыкального клуба."
    "Пионеры закивали головами, поднялись и ушли."
    stop music fadeout 2
    #hide iie
    #hide hai
    #hide ci
    "..."
    show sl normal pioneer far at center with dspr
    play music music_list["smooth_machine"] fadein 1
    "Остались только мы со Славей. Она подошла к парте с микроскопами и подняла с пола брезентовую сумку с нашивкой в виде красного креста."
    "Как выяснилось, девочка задержалась, чтобы взять из шкафа книгу о природе края и связку бинтов."
    show sl normal pioneer at center with dspr
    me "Это и есть полевая сумка?"
    show sl smile pioneer at center with dspr
    "Славя показала на крест."
    sl "Да, но я ещё и староста кружка, поэтому ношу аптечку, ведь медсестра Виола не может каждый раз ходить с нами, а отвечать за здоровье пионеров кто-то должен, особенно если понадобится немедленная помощь."
    show sl happy pioneer at center with dspr
    sl "Все юннаты имеют при себе тетради с альбомами, книжки, линейки, ручки с карандашами и бинокли. А для ботанических исследований ещё берут садовые ножницы."
    me "Обстоятельно, ничего не скажешь."
    show sl smile2 pioneer at center with dspr
    sl "А ты думал! Записи о природе — необходимая часть деятельности юнната. Это не взялось откуда-то с потолка, есть заповеди, которые должен соблюдать каждый юный натуралист."
    show sl smile pioneer at center with dspr
    sl "Во-первых, наблюдай всё, что есть вокруг тебя в природе. Все наблюдения записывай. Некоторые юннаты делают зарисовки к наблюдениям — это по желанию и способностям."
    sl "Нужно быть точным, указывай все условия наблюдения, время и место.{w} Если чего-то не знаешь точно, не домысливай и не пиши об этом.{w} Выводы проверяй: ставь опыт или многократно наблюдай за объектом."
    show sl surprise pioneer at center with dspr
    sl "Если вдруг заметишь что-то важное, проблему, из-за которой надо бить тревогу, или сделаешь интересное открытие, сообщай нам, подготовим текст для пионеров из кружка стенгазеты."
    show sl smile pioneer at center with dspr
    sl "Последняя заповедь требует в конце месяца отметить все произошедшие в окружающей тебя природе перемены. К сожалению, мы проведём в лагере меньше времени, но это не значит, что в конце смены не надо писать заключительные выводы."
    show sl normal pioneer at center with dspr
    sl "Такие правила придумали ещё в первые годы возникновения юннатского движения. Не исполняя их, пионер считать себя натуралистом не может."
    show sl smile2 pioneer at center with dspr
    sl "На самом деле правил и целей у юннатов на порядок больше — я ещё не рассказала тебе об охране окружающей среды, защите природы и некоторых запретах."
    me "Н-нда. Мне кажется, что тратить на это пару недель бессмысленно, что ли. Надо быть в теме и заниматься подобным долго, чтобы появилась хоть какая-то отдача." 
    me "Я сейчас впервые узнал обо всём, и теперь не уверен, что мои попытки начать реально повлияют на мои нынешние увлечения."
    show sl happy pioneer at center with dspr
    sl "Ты прав. Но попробуй остаться с нами, вдруг втянешься и продолжишь после лагеря? Могу обещать, что несколько полезных дел мы вместе обязательно выполним, и тебе будет о чём вспомнить, даже если ты не посвятишь себя юннатскому движению."
    sl "И отдыхать, и приятно проводить время мы тоже будем вместе!"
    show sl smile2 pioneer at center with dspr
    "Я представил себе совместные высадку цветов, кустов и деревьев, всяческие субботники, походы на природу со сплавом на байдарках, волонтёрскую помощь экологическим организациям.{w} Да, наверно, Славя имела в виду именно такие полезные дела и отдых, где необязательно быть причастным к юннатам."
    "В голову ударил тупой страх от осознания, что я уже слышал раньше о чём-то подобном, но вскоре позабыл, поскольку это выпадало за грань моих интересов."
    th "Ну конечно... Поход со сплавом на байдарках..."
    "Именно так познакомились мои родители. Он — волонтёр, она — студентка медицинского университета."
    "В таких не совсем обычных обстоятельствах, когда два человека встречаются, и между ними возникают отношения, кроется необъяснимая романтика."
    "Страх возник, потому что мне меньше всего хотелось идти по стопам отца."
    show sl surprise pioneer at center with dspr
    sl "Что-то не так, Семён? Ты...{w} странно смотришь на меня."
    "Я спохватился, когда мы встретились взглядами."
    me "Нет, всё нормально."
    show sl smile pioneer at center with dspr
    "Славя улыбнулась."
    me "На чём мы остановились? У меня нет полевой сумки. И тетради для наблюдений."
    "О том блокноте-дневнике, куда я вчера записывал о лагере и его обитателях, я не стал говорить. Пионеры, очевидно, не редкие животные, а моё путешествие во времени — не трип-репорт, но Славя могла неправильно понять."
    show sl happy pioneer at center with dspr
    sl "Не вопрос!"
    show sl smile pioneer at center with dspr
    "Девочка выдвинула по очереди пару верхних ящиков комода, прежде чем нашла для меня тетрадь формата А4."
    sl "Вот, держи. Как раз в тему!"
    "На обложке тетради был изображён таёжный лес на берегу реки."
    me "В самом деле. Спасибо!{w} Осталось решить где носить все вещи. У меня с собой только баул с одеждой. Такой по лесу не потаскаешь."
    show sl surprise pioneer at center with dspr
    sl "Может, попросишь у кого-нибудь? Например, у кибернетиков. Пошли к ним!"
    show sl smile pioneer at center with dspr
    "Славя перекинула лямку сумки через плечо, и мы покинули комнату."
    #scene bg
    show sl normal pioneer at cleft with dspr
    "Стук в двери от кружка юных техников ничего не дал — нам не открыли, но явно было слышно, как переговариваются между собой Сыроежкин и Шурик."
    me "Откройте, пожалуйста! Это Семён!"
    el "Не верю! Вдруг ты не Семён? Назови пароль!"
    show sl surprise pioneer at cleft with dspr
    sl "Пароль?"
    "Я хлопнул себя по лбу."
    me "Они на полднике сказали мне, что будут пускать к себе только если правильно отстучать код морзянкой."
    sl "А ты запомнил его?"
    me "«ЭШ». Наверно, инициалы Эла и Шурика."
    show sl serious pioneer at cleft with dspr
    "Не слушая мои рассуждения, Славя уверенно постучала в дверь на азбуке Морзе."
    th "Ух ты, удивила!"
    me "А юннатам надо знать азбуку Морзе?"
    show sl normal pioneer at cleft with dspr
    "Я неудачно попытался придать словам шутливый тон, однако Славя ответила без капли иронии."
    sl "Думаю, это полезно. Вдруг, потеряешься в походе..."
    "Сыроежкину пришлось открыть — своим игровым правилам он изменить не мог."
    scene bg int_clubs_male_day
    with dissolve
    show sl normal pioneer at cleft with dissolve
    show el surprise pioneer at cright with dissolve
    "Робот на столе кибернетиков был спрятан под широким покрывалом, чтобы никто из непосвящённых не мог увидеть результаты их трудов."
    show el angry pioneer at cright with dspr
    el "Привет. Что-то хотели?"
    me "Есть ли у вас сумка вроде той, что у Слави? Мне нужно для занятий кружка юннатов."
    el "Нет. Очень жаль, что ты не вступил к нам. Пока."
    show sl angry pioneer at cleft with dspr
    show sh smile pioneer at fright with dissolve
    "Он хотел было закрыть дверь, но Шурик остановил его."
    show el scared pioneer at cright with dspr
    sh "Погоди, у меня есть, могу одолжить."
    show sh surprise pioneer at fright with dspr
    sh "Мы с Элом живём в третьем домике, он открыт, так что можешь зайти туда в любое время. Найдёшь на прикроватной тумбочке."
    show el sad pioneer at cright with dspr
    "Я поблагодарил его, обещав вернуть сумку в целости и сохранности."
    me "Я забегу к Шурику и к себе, возьму бинокль и ручку, подождёшь?"
    sl "Подожду со всеми, мы будем около музыкального клуба."
    me "Хорошо."
    sl "А к Сыроежкину у меня разговор. Сергей, я ведь говорила, что кружки общие!.."
    hide sl
    hide el
    hide sh
    with dissolve
    scene bg ext_clubs_day
    with dissolve
    "Выговор Слави незадачливому кибернетику я уже не застал."
    window hide
    stop music fadeout 1
    scene black 
    with dissolve
    window show
    "......"
    "........."
    window hide
    scene bg ext_musclub_day 
    with dissolve
    play music music_list["everyday_theme"] fadein 2
    window show
    "Мне пришлось задержаться из-за Ольги Дмитриевны, поэтому я снова оказался опоздавшим."
    show sl normal pioneer far at center with dissolve
    #show hai
    #show iie
    #show ci
    "Пионеры стояли кружком в конце аллеи, где за выложенной плиткой дорогой начиналась земляная тропа к лесу. Все они были в полной готовности — с небольшими рюкзаками и сумками-планшетками."
    "А у одной из девочек неприлично низкого роста, что в кремово-белом чепчике, с собой была даже позолоченная лейка." 
    "Юннатка Саша обеими руками держала пустую литровую банку и выслушивала наставления от Слави."
    "С кожаной борсеткой Шурика на боку я присоединился к ним."
    scene bg ext_path_day
    with dissolve
    "Не соблюдая строя и не разбиваясь на пары, мы пошли по тропе к лесу."
    show sl smile pioneer far at center with dissolve
    "Славя была впереди и вела юннатов за собой. Я обогнал пионеров и поравнялся с ней."
    show sl smile pioneer at center with dissolve
    me "Ольга Дмитриевна просила передать, что у нас сегодня ужин раньше — полвосьмого. Потом состоится какое-то мероприятие."
    sl "Значит, не будем уходить далеко."
    "..."
    scene bg ext_path2_day
    with dissolve
    play ambience ambience_forest_day fadein 1
    "Тропа сузилась. Пионерский лагерь остался позади, а мы оказались в царстве природы."
    "Под ногами шуршала землистая пыль, усыпанная хвоей и листьями в просвете между травянистыми коврами. Здесь всё было другим — и воздух, и запах."
    "Чуть прохладный ветерок и кроны деревьев спасали нас от жарких лучей солнца."
    "Где-то вверху зашумели потревоженные ветром лапы сосен. Стоило мне глянуть вверх на синее небо за кольцом ветвей, как закружилась голова."
    "По змеящейся тропинке мы осторожно проложили друг за другом путь мимо оврага, и только потом снова пошли вразнобой."
    "Были слышны трели и пересвист лесных птиц, но как я ни смотрел во все глаза, никакой живности найти не смог. Вдруг одна из юннаток негромким шёпотом позвала всех."
    girl_A "Смотрите, смотрите!"
    "Она указывала на небольшую поляну, утонувшую в солнечном свете."
    "Там, где около сухого дерева заканчивалась трава и темнела земляная плешь, не двигаясь, изредка поворачивая голову, сидела пёстрая серая птица со множеством бурых, почти рыжих пятнышек на перьях."
    show sl happy pioneer at center with dissolve
    sl "Это козодой... Эти птицы гнездятся прямо на земле..."
    show sl normal pioneer at center with dspr
    sl "Хорошая находка, ведь они показываются вечером, а днём прячутся — отдыхают, спят." 
    sl "Окрас перьев позволяет им маскироваться на земле и ветках деревьев..."
    "Все юннаты как один раскрыли сумки с рюкзаками и вынули свои тетради. Вооружившись ручками, пионеры стали записывать. Кто под диктовку Слави, а кто с опережением, точно уже сам знал, что надо занести в полевой дневник." 
    show sl smile2 pioneer at center with dspr
    "Тот паренёк из младшего отряда, который не закончил свои наблюдения за клестом, открыл чистую страницу в тетради, поднял к глазам бинокль и принялся рассматривать птицу, чтобы точно передать её внешний вид на бумаге."
    "Юные натуралисты действовали, а я довольствовался тем, что наблюдал за ними со стороны, не потрудившись достать подаренную Славей тетрадь."
    iie "А я помню, я читала про козодоев. Они звучат по-совиному, и начинают охотиться после сумерек, тоже как большинство сов."
    show sl smile pioneer at center with dspr
    sl "Они уничтожают насекомых-вредителей на речных берегах, тропах и около пасущегося вечером домашнего скота, и за то их по праву можно называть санитарами полей и деревень."
    sl "А здесь рядом и река, и деревня."
    th "Ну и пусть пионеры так внимательно разглядывают диковинную птицу. Важно было не это, а их наивная, в хорошем смысле этого слова, удивительная и неподдельная тяга к знаниям."
    th "В моём мире большинство их ровесников уже не так охотно стремится узнать что-то новое."
    th "Может быть, я сужу только по себе?"
    "Я прогнал из головы неприятные мысли. Не хватало ещё ворчать как старик и охать!"
    show sl normal pioneer at center with dspr
    sl "Пойдёмте."
    iie "Но я ещё не закончила."
    show sl smile pioneer at center with dspr
    sl "Видите деревья на краю опушки? Там хорошая поляна, где можно разместиться и продолжить наблюдения. Это рядом."
    "Юннаты повставали с травы, и мы осторожно, чтобы не потревожить птицу, отправились к той поляне."
    scene bg ext_polyana_day
    with dissolve
    "Славя оказалась права — тут было куда больше свободного места, чтобы юннаты могли разойтись и спокойно изучать природу, не теснясь на тропинке."
    show sl normal pioneer at center with dissolve
    sl "Если кому-то надо пройти дальше для поиска нового объекта наблюдений, то не забудьте: через полтора часа собираемся здесь, пользуйтесь компасами, если потеряетесь. Если что-то случится, зовите на помощь. За забор не уходите."
    me "Лес огорожен?"
    show sl smile pioneer at center with dspr
    sl "Да, мы всё ещё на территории лагеря, но расстояния тут приличные, можно заплутать."
    "Предоставленные самим себе юннаты разбрелись по сторонам, кому куда хотелось."
    hide sl with dissolve
    #hide hai
    #hide iie
    #hide ci
    "Что ж, мне предстояло заняться тем же — найти себе место и вести наблюдения." 
    th "И ничего не поделать, сам выбрал такой кружок. Назвался груздём... Вот такой ботанический каламбур."
    "Я сел в подножии раскидистого дерева, где, как мне показалось, побольше травы и сидеть мягче."
    "Прислонившись к дереву, я раскрыл кожаную борсетку Шурика."
    th "Хм, а он знает толк в стильных вещах..."
    "Я вытянул бинокль и грубо скрученную тетрадку, разворачивая её на первой странице."
    "Позаимствованной со стола Ольги Дмитриевны ручкой я попробовал написать что-нибудь относящееся к тому, чем занимаются юные натуралисты."
    "«П/л Совёнок, Подмосковье. Место наблюдения — смешанный лес.»"
    "«Время ≈пять вечера.»"
    "..."
    "Я не знал, что делать дальше. В отличие от других пионеров, я не выбрал себе никакого объекта для наблюдений."
    th "Может, мне надо присоединиться к кому-то?"
    "Об этом я подумал не сразу, по привычке обособившись ото всех."
    "Мне определённо нужен был тот блокнот, где я начал вести записи о пионерском лагере."
    "Я с разочарованием закрыл тетрадь." 
    th "Лучше уж посмотреть, что делают остальные юннаты."
    #show hai
    #show iie
    "Инна и Анна с пионером из младшего отряда взобрались на холм с поросшими мхом корнями деревьев, чтобы издалека понаблюдать за той серой птицей на соседней поляне."
    "Двух других пионерок больше интересовали растения.{w} Или насекомые.{w} В любом случае, девочки достали из сумок по увеличительному стеклу, высматривая что-то на траве возле густого кустарника."
    #show ci
    "Неутомимая Саша гуляла поблизости, не выпуская из рук прозрачной банки, и искала взглядом, не мелькнёт ли где на земле лягушка."
    #hide hai
    #hide iie
    #hide ci
    show sl smile pioneer far at center with dissolve
    "Воодушевлённая (наверняка лесной природой!) Славя тоже что-то пыталась найти. Она медленно обходила поляну, глядя куда-то по сторонам и вверх."
    th "Птиц ищет что ли?"
    show sl smile pioneer close at center with dissolve2
    "Когда Славя остановилась в полуобороте, и я поднёс к глазам бинокль, чтобы рассмотреть её получше, на что в разговоре между нами мне вряд ли хватило бы смелости." 
    "И как бы я ни сдерживался, отвести взгляда от милых очертаний лица девочки я не мог."
    show sl shy pioneer close at center with dissolve2
    "Загорелой рукой Славя отвела косу за плечо так, что мне стали видны беглая тень длинных ресниц и нежный румянец её щёк, едва заметный, как и улыбка."
    th "Почему она всё время улыбается?{w=0.3} О чём она думает?"
    "Это меня не смущало, напротив, казалось притягательным.{w} Я с уверенностью мог сказать, что Славя точно принадлежала к числу тех людей, чья улыбка мне понравилась."
    "Если светлая улыбка становилась неотъемлемой частью образа, то такого человека мне хотелось видеть чаще... И никогда не огорчать."
    hide sl with dissolve
    "Вдруг Славя пропала из вида. Я опустил бинокль на миг, чтобы понять, куда она ушла." 
    show sl smile2 pioneer far at cleft with dissolve
    "Староста юннатов направилась к девочкам, усевшимся на траве с лупами."
    sl "Как вы?"
    girl_A "Вот, смотри — земляника! А когда мы будем собирать её?"
    sl "Я только за! Надо сначала узнаю об этом у вожатых, а то нас нет ни стаканчиков, ни корзинок для ягод..."
    "Она отошла к сёстрам Данетко."
    show sl smile pioneer far at cright with dissolve
    #show hai
    #show iie
    sl "Приглядите за Сашей, пока меня нет, хорошо?"
    hai "Ага!"
    #hide hai
    #hide iie
    show sl normal pioneer far at left with dissolve
    th "Куда это она?"
    "Я подумал, что Славе зачем-то понадобилось вернуться в лагерь, но она твёрдым шагом направилась в противоположную от него сторону  — в глубь леса."
    hide sl with dissolve
    th "Иди за ней!"
    "Вопреки нежеланию двигаться с места, я резко поднялся и пошёл следом за девочкой, потому что ещё были вопросы, которые я хотел задать ей."
    window hide
    stop music fadeout 2
    scene bg ext_path2_day
    with dissolve
    play music music_list["get_to_know_me_better"] fadein 2
    show sl normal pioneer at center with dissolve
    window show
    "Я догнал Славю. В спешке я даже не удосужился убрать тетрадь, и теперь просто держал её за спиной."
    me "Ты куда?"
    show sl surprise pioneer at center with dspr
    sl "Я хотела пройтись, присматриваю места, где можно развесить кормушки. А ты почему не остался со всеми?"
    "Я мельком оглянулся, заметив, что поляну с юннатами уже не видно за деревьями, хоть Славя и сбавила шаг из-за меня."
    me "Не знаю, с чего начать. У меня нет отправной точки.{w} Раскрываю тетрадь, или книгу, как говорится, а вижу фигу."
    show sl smile pioneer at center with dspr
    "Славя с пониманием улыбнулась."
    sl "Ты, наверно, выпускник, если у тебя нет задания по биологии на лето?"
    me "Верно. И я никогда не планировал сдавать экзамен по этому предмету."
    show sl smile2 pioneer at center with dspr
    sl "А какие оценки за год по биологии?"
    me "Всегда были четвёрки. Но поверь, это к знаниям не относится. Ставили просто за то, что я тихо вёл себя на уроках, по сравнению с буйными одноклассниками.{w} А у тебя?"
    show sl happy pioneer at center with dspr
    sl "Ха, знакомая ситуация.{w} Всё так же, кроме того, что я стараюсь учиться на отлично по всем предметам."
    me "Неудивительно."
    show sl surprise pioneer at center with dspr
    sl "Что?"
    me "В смысле, я почему-то другого от тебя и не ожидал."
    show sl shy pioneer at center with dspr
    "Славя смутилась на мгновение."
    show sl smile2 pioneer at center with dspr
    sl "Ну, я просто была усидчивой, если дело касалось уроков. Наверно, из-за воспитания."
    sl "Если к чему-то в детстве приучаешься, то с большой вероятностью это останется на всю жизнь."
    th "Она права. Даже слишком. Всё как обо мне."
    "..."
    "Девочка немного потеснила меня, предлагая свернуть налево к очередной опушке среди деревьев."
    scene bg ext_polyana_day
    with dissolve
    show sl surprise pioneer at center with dissolve
    sl "Что значит — нет отправной точки? Почему ты не сел к Анне с Инной? Взял бы и переписал у них о козодое, а потом сам нашёл бы другую птицу или зверька."
    me "В том-то и дело, что я мог бы написать про другую? Выдумать из головы? Я же, считай, кроме воробьёв и голубей ничего не видел.{w} Ну хорошо, кроме ворон, синиц, чаек, попугаев... Страусов, аистов, сов, и орлов из зоопарка я не считаю."
    show sl laugh pioneer at center with dspr
    "Славя засмеялась."
    sl "Вот, а говоришь, что ничего не видел и не знаешь! Ещё пару вспомнишь, и можешь называть себя орнитологом."
    me "Да ты издеваешься!"
    show sl smile2 pioneer at center with dspr
    sl "Есть немного!"
    show sl surprise pioneer at center with dspr
    "Она заметила, как я нахмурился."
    show sl smile pioneer at center with dspr
    sl "Не принимай всерьёз, я шучу."
    "Её мягкая улыбка обезоруживала, и я легко согласился."
    show sl surprise pioneer at center with dspr
    sl "Так Инна и Аня могли отыскать другую птицу и рассказать о ней тебе, стоило только объяснить им...{w} Я правильно понимаю, что ты не захотел попросить сестёр о помощи?" 
    show sl smile2 pioneer at center with dspr
    sl"Постеснялся?"
    me "Не постеснялся, просто я даже не задумывался об этом. Я привык сам как-нибудь разбираться."
    show sl sad pioneer at center with dspr
    sl "Звучит нехорошо.{w} Опасно."
    me "Почему?"
    show sl serious pioneer close at center with dspr
    "Мы остановились. Славя заглянула мне в глаза, словно готовилась проверить меня на честность."
    sl "Если возникнет проблема, серьёзная или не очень, но вызывающая у тебя вопрос, задашь ли ты его кому-то, чтобы разобраться, или нет?"
    "Я стиснул зубы, догадываясь, к чему она клонит."
    me "Нет."
    sl "А если самому «как-нибудь разобраться» с проблемой не получится?"
    me "Тогда ну её к чёрту."
    "Не выдержав чистого взгляда Слави, я склонил голову и бесцельно уставился куда-то под ноги."
    show sl sad pioneer close at center with dspr
    sl "Я так и думала. Поэтому я сказала, что опасно, Семён."
    "Я снова взглянул на неё. Славя заметно погрустнела. Пропала та самая улыбка."
    me "Может быть... Но не фатально. Такое со мной уже случалось много раз. Вот, пожалуй, пример моей давней привычки, оставшейся на всю жизнь."
    show sl happy pioneer close at center with dspr
    "Вдруг к девочке вернулось её былое веселье."
    sl "Нет, не на всю!"
    sl "Мы оба с тобой ошибаемся!"
    me "Да?"
    show sl smile pioneer close at center with dspr
    sl "Ты же ушёл от юннатов, чтобы догнать меня и задать вопрос..."
    stop music fadeout 3
    me "Да нет же, не о том!{w} Просто хотел узнать, куда ты, лагерь-то в другом направлении отсюда...{w} Н-не подумай неправильно!"
    show sl shy pioneer close at center with dspr
    "Я не знал, как Славя истолковала мои слова, но на её щеках заалел тот самый нежный румянец."
    "Повисла тишина, и остался слышимым только далёкий пересвист лесных птиц."
    me "...Дело даже не в том, что я не знаю с чего начать. Просто у меня нет желания что ли. Нет мотивации. Смотрю на юннатов, и не могу понять — откуда такая увлечённость?"
    play music music_list["everyday_theme"] fadein 2
    show sl smile2 pioneer close at center with dspr
    sl "Как минимум, ради своего отряда, успехов на викторинах, которые будут проводить вожатые. За это награждают грамотами, значками."
    show sl smile pioneer close at center with dspr
    sl "Но ты верно заметил, что подобным надо заниматься долго, если нужна отдача. Многие из пионеров уже думают о будущем."
    show sl normal pioneer close at center with dspr
    sl "Кто-то собирается быть врачом, как Инна, кто-то мечтает быть зоологом или ветеринаром."
    me "А ты — думаешь о будущем?"
    sl "Невозможно не думать о нём."
    show sl smile pioneer close at center with dspr
    "Она улыбнулась."
    sl "Мне больше всего интересно краеведение." 
    sl "Из-за этого я помогла учительнице по географии сделать при школе краеведческий музей и кружок."
    me "Но ты говорила что-то про школьное посвящение в юннаты и зооуголок, разве ты не из их кружка?"
    show sl smile2 pioneer close at center with dspr
    sl "Всё правильно: в одном я участник, в другом помощник руководителя."
    show sl surprise pioneer close at center with dspr
    sl "Кстати, из какого ты города?"
    me "Из Москвы."
    "Я сказал это по наитию и спохватился, ведь {i}та{/i} Москва и здешняя — совершенно разные места."
    show sl smile2 pioneer close at center with dspr
    sl "Здорово! Можно встретиться после лагеря, когда учебный год начнётся. Покажу наш музей и зооуголок."
    show sl smile pioneer close at center with dspr
    sl "Я из сто семнадцатой школы. Ты приходи к нам, приходи!"
    th "О, как легко строить планы, когда есть крыша над головой, когда уверен в завтрашнем дне!"
    th "Неизвестно, что ещё случится в конце смены, куда мне потом деваться? Для этого мира в худшем случае я буду известен как человек Без Определённого Места Жительства, спящий в картонной коробке, если повезёт..."
    me "Не обещаю."
    show sl surprise pioneer close at center with dspr
    sl "Почему?"
    me "Чтобы не солгать. Поживём — увидим."
    show sl serious pioneer close at center with dspr
    "Славя вдруг осеклась и приняла серьёзный вид."
    sl "Знаешь, а ты прав. Поживём — увидим. Мало ли что может случиться?"
    show sl sad pioneer close at center with dspr
    sl "Прости, это было глупо — вот так, ни с того ни с сего приглашать, не подумав."
    "Я словно онемел, не зная, что ответить на неожиданное заявление."
    th "Как это вообще понимать?"
    stop music fadeout 3
    "Однако Славя молчала, не собираясь мне ничего объяснять."
    play music music_list["she_is_kind"] fadein 2
    show sl smile2 pioneer close at center with dspr
    sl "Пойдём, Семён."
    me "Э?"
    show sl happy pioneer close at center with dspr
    sl "Грех не протянуть руку помощи своему товарищу!"
    sl "Раз уж ты не подошёл к Анне с Инной, то я помогу тебе..."
    show sl smile pioneer close at center with dspr
    "Она, не дожидаясь моего согласия, взяла меня за ладонь и повела."
    if d1_us_chase:
        "Совсем как вчера..."
    me "Но я не хотел..."
    sl "Иногда, если не нравятся кошки, это значит, что ты не умеешь их готовить!"
    sl "Давай отыщем кого-нибудь, а я подскажу, что надо делать."
    sl "И потом, я решила, что если есть возможность, нельзя упускать её."
    scene bg ext_path_day
    with dissolve
    show sl smile pioneer close at center with dissolve
    "Мы вновь двинулись в чащу леса. Я сначала подумал, что Славя собирается вернуться назад и пристроить меня к кому-то из юннатов, но мы шли совсем в другом направлении." 
    "Впрочем, я скоро забыл, откуда мы начинали путь, потому что Славя по дороге рассказывала мне, кого из зверей их кружок уже находил, и я внимательно слушал её."
    scene bg ext_polyana_day
    with dissolve
    show sl smile pioneer close at center with dissolve
    "Наконец, Славя остановила меня на холмике, когда нашла красивую пичужку, восседавшую на ветви кустарника неподалёку."
    show sl surprise pioneer close at center with dspr
    sl "О, гляди. Видел когда-нибудь такую птицу, Семён?"
    me "Нет, и даже не имею понятия, как она называется."
    show sl smile2 pioneer close at center with dspr
    sl "Вот и отлично, доставай бинокль и ручку."
    show sl normal pioneer close at cleft with dspr
    "Разгладив юбку, Славя аккуратно села на травянистый полог холма. Я замешкался, доставая из сумки всё необходимое, и только тогда подсел к Славе справа."
    show sl smile pioneer close at cleft with dspr
    "Я раскрыл тетрадь."
    sl "Если ты не знаешь, что за это птица, то пиши всё, что наблюдаешь. Как она выглядит, как ведёт себя..."
    "Я затаил дыхание, боясь пропустить хоть что-то из её слов."
    show sl smile2 pioneer close at cleft with dspr
    "Она говорила, чуть наклонившись ко мне (так, что ей пришлось снова поправить одну из кос), а я записывал, иногда посматривая в бинокль и передавая его Славе."
    "С каждой секундой этого уединённого пребывания вместе возрастала благодарность, что кому-то не всё равно, а возможность — свершилась, и о ней не придётся вспоминать, как об упущенной."
    show sl happy pioneer close at cleft with dspr
    "Мы сидели плечом к плечу. Отвлёкшись от птицы, Славя стала рассказывать о видах, занесённых в Красную книгу."
    "Мысль о том, понадобятся ли мне в жизни эти записи в тетради, отступила на десятый план. На первом было другое — я хоть ненамного стал уверенней в завтрашнем дне."
    window hide
    scene black
    with dissolve
    window show
    "..."
    "......"
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ d2_girls_event = (d2_girls_event) + (1)
    $ d2_sl_day = True
    $ lp_sl = lp_sl + 1
    $ disable_current_zone()
    jump d2_pre_event

label d2_modeller_club_day:
    
    if (modeller_club == False):
        play music music_list["my_daily_life"] fadein 1
        window show
        "К моделистам я не записывался, и делать у них мне было абсолютно нечего."
        if d1_dv_evening:
            "Разве что поболтать с Антоном, но я даже не представлял, о чём."
        if d2_chess_agreement:
            "Ещё у них иногда бывает Угрюмый..."
            "Я открыл дверь и заглянул к моделистам."
            me "Извините, что отвлекаю, но Угрюмый здесь?"
            show mk at center with dissolve
            mk "Неа, хз, где он, вообще не видел его после завтрака."
            me "Ну, если появится тут, скажите, что я искал его."
            mk "Ладно, передам."
            hide mk with dissolve
            th "Не повезло."
        "Может, зайду к ним в другой раз, если очень понадобится."
        window hide
        stop music fadeout 1
        $ d2_times_been_to_modeller_club = 1
        jump d2_day_map
    $ reset_chibi("clubs")
    scene black
    with dissolve
    show screen central_text("День 2 — Вспоминая детство")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_clubs_day
    with dissolve
    play music music_list["farewell_to_the_past_full"] fadein 2
    window show
    "Я взялся за круглую ручку входной двери."
    th "Гм, интересно: если компьютер помогал мне компенсировать отсутствие личной жизни, то сможет ли поклейка танчиков компенсировать отсутствие того и другого?"
    th "Вот сейчас и узнаем."
    "С уверенностью я зашёл в комнату."
    "Пионеры встретили меня благодушно, и я подумал, что здесь не так мрачно, как мне показалось вначале."
    if d1_dv_evening:
        "Староста тут же познакомил меня со всеми, за исключением Антона, которого я уже знал, а сам представился как Владя."
    else:
        "Староста тут же познакомил меня со всеми, а сам представился как Владя."
    $ meet('km', u"Владя")
    km "...Ну, вот такая ситуация. Чем будешь заниматься? Здесь вся комната в распоряжении участников кружка."
    "Я пожал плечами, оглядывая комнату."
    me "Не знаю. Посоветуешь что-нибудь?.."
    km "Хм...{w} У тебя есть хобби?"
    me "Чтение, но это явно не про ваш кружок."
    km "Почему не про наш? Книги могут помочь при моделировании реального объекта.{w} Любишь конструкторы?"
    me "Как сказать... Давно не увлекался чем-то подобным."
    "Я услышал характерный шум пересыпаемых туда-сюда кирпичиков и обратил внимание на пионера, согнувшегося в три погибели над большой коробкой, почти доверху заполненной детальками LEGO."
    th "Ох, вау, LEGO в СССР?"
    "Староста заметил мою реакцию."
    km "А, значит, у тебя были Тёмные Времена?"
    me "В смысле, тёмные времена?"
    km "Видимо, ты не в теме... Это если ты когда-то сильно увлекался LEGO, а потом забросил, став старше. Пока ты не возвращался к нему — это и есть Тёмные Времена."
    me "Не то что бы увлекался, у меня было довольно мало наборов. А из игрушек мне даже больше запомнился конструктор «Полёт»: такой, с кучей квадратных секций."
    km "Но он же совсем старый!"
    "Владя посмотрел на меня с грустью и сочувствием в глазах."
    th "Он решил, что у меня было трудное детство? Типа, деревянные игрушки, прибитые к полу?"
    "Я не мог объяснить ему, что родился ещё до распада Советского Союза, а когда LEGO стало весьма популярным, я понемногу выходил из нежного возраста."
    "К тому моменту меня уже интересовали другие вещи: футбол, фишки-кэпсы, приставка SEGA и наклейки-вкладыши с голыми тётками под обёртками жвачки."
    km "Хорошо, а что тебе нравится больше всего?"
    me "Компьютерные игры."
    th "После многочасовых залипаний у телевизора с приставкой это неудивительно."
    km "О, я понял!{w=0.5} Сделай модель по одной из любимых игр!"
    "Стоило мне об этом подумать, сразу появилась куча идей, что можно сделать из имеющегося в распоряжении моделистов. Бластер червяка Джима? Минисценку из Sunset Riders?"
    "Надо было остановиться на чём-то общеизвестном и понятном для всех, например, на военной тематике, как в Call of Duty."
    th "Чую, я действительно буду в прямом смысле клеить танчики."
    me "М-м, я хочу самстерить танк... или самолёт, может быть даже это станет началом для маленькой диорамы... Вот."
    km "Садись тогда к Антону! Он сейчас тоже авимодели делает.{w} А я больше по судомоделированию. Захочешь собрать бригантину или каравеллу, обращайся ко мне!"
    if (d1_dv_evening == False):
        $ meet('mk', u"Антон")
    me "Cпасибо за помощь!"
    "..."
    show mk at cleft with dissolve
    "Я сел рядом с Антоном, корпевшим над моделью биплана под ярким светом настольной лампы."
    "Пионер отвлёкся и подвинулся, пуская меня к столу."
    me "Я собрался делать модели по боевой технике, подскажешь, где что для этого взять?"
    mk "Без проблем."
    "Он показал мне содержимое всех шкафчиков с ящиками и объяснил, как сконструировать диораму. Кое-что пришлось позаимствовать у сидевших рядом пионеров, а работы по раскрашиванию модели мне, как новичку, посоветовали отложить, чтобы поучиться тому у других моделистов или по тематическим журналам."
    "Теперь, с инструментами наготове и новыми знаниями, я уверенно приступил к сборке модели немецкого танка из только что распечатанной коробки."
    window hide
    stop music fadeout 1
    scene black
    with dissolve
    window show
    "..."
    "......"
    "........."
    $ proficiencies ['kn_modelling']+=1
    window hide
    scene bg ext_square_day
    with dissolve
    play ambience ambience_camp_center_day fadein 1
    window show
    "Когда прозвучала до конца мелодия сигнала на ужин, я уже направлялся к столовой. Остальные моделисты, конечно, побежали сломя голову занимать очередь, кроме Антона — он тоже шёл в одиночестве неподалёку."
    "Модель я почти собрал, осталось только доработать левый гусеничный движитель и приладить башню сверху. Я начинал без энтузиазма, но сам не заметил, как увлёкся." 
    th "Ошибочно было считать, что такое занятие подходит исключительно для подростков, вроде местных пионеров. Разумеется, есть взрослые, которые имеют вкус к подобным хобби и зарабатывают на свои интересы."
    "Ностальгические воспоминания об игрушках и развлечениях живо напомнили мне, что я стал старше, однако не нашёл работу и не обзавёлся семьёй, как многие дяденьки, возящиеся с моделями."
    th "Двадцать пять лет — жизнь кончена, всё пропало?"
    "Я думал, что потерял детство. Но, придя сюда, я осознал, что оно, в общем-то, никуда и не уходило."
    window hide
    stop ambience fadeout 1
    $ d2_modellers_day = True
    $ disable_current_zone()
    jump d2_pre_event
    

label d2_chess_club_day:
    
    if d2_chess_agreement:
        window show
        "Я помнил об условии, что я не должен посещать этот кружок."
        th "Если вдуматься, то кроме Угрюмого я никого тут не знаю, и просто так играть здесь будет не слишком интересно."
        th "Тем более, скоро турнир, а он готов помочь мне."
        th "И он сказал, что свободен после полдника.{w} Надо поискать Угрюмого."
        window hide
        stop music fadeout 1
        $ disable_current_zone()
        jump d2_day_map
    elif d2_chess_decision:
        window show
        th "Не сегодня."
        if books_taken == 0:
            th "Лучше самому подготовиться к турниру, раз уж на то пошло. В библиотеке же можно взять книги?"
        window hide
        stop music fadeout 1
        $ d2_times_been_to_chess_club = 1
        jump d2_day_map
    elif (chess_club == False) and (d2_met_ug == True):
        th "Мне не сюда."
        "К тому же, отказавшись от помощи Угрюмого, я окончательно расстался с идеей проводить время в лагере за настольными играми и шахматами, в частности."
        window hide
        stop music fadeout 1
        $ d2_times_been_to_chess_club = 1
        jump d2_day_map
    elif (chess_club == False) and (d2_met_ug == False):
        window show
        "Я не записался в этот кружок, и играть с кем-то нет желания."
        window hide
        stop music fadeout 1
        $ d2_times_been_to_chess_club = 1
        jump d2_day_map

label d2_musclub_day:

    if (mus_club == False):
        $ reset_chibi("music_club")
        scene bg ext_musclub_day
        with dissolve
        play music music_list["my_daily_life"] fadein 1
        window show
        "В музыкальный кружок я не стал заходить — повода не было."
        "Из раскрытого окна доносилась музыка."
        "По дороге назад к площади я не без интереса посмотрел, что же происходит внутри клуба."
        "Мику самозабвенно играла на флейте, а стоявшие рядом с ней пионеры и пионерки аккомпанировали на других музыкальных инструментах."
        th "Утром Мику жаловалась, что участники кружка гуляют, а сейчас они все дружно музицируют. Видимо, преувеличила."
        th "Значит, всё в порядке."
        "Я вообразил, что сам нахожусь в их компании, насилуя пальцы струнами гитары, но эта мысль не понравилась мне."
        th "Ну и правильно, что не записался сюда."
        window hide
        stop music fadeout 1
        $ disable_current_zone()
        jump d2_day_map

    $ reset_chibi("music_club")
    scene black
    with dissolve
    show screen central_text("День 2 — Не совсем одно и то же")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_musclub_day
    with dissolve
    play music music_list["everyday_theme"] fadein 1
    window show
    "По дороге к зданию клуба я размышлял, что же мне в нём делать до конца смены."
    th "Неужели учиться игре на музыкальном инструменте или пению?"
    th "Ох."
    "Вряд ли я бы снова стал тратить на это время."
    "Когда-то я ходил на занятия по гитаре, потому что услышал, будто так можно снискать успех у девчонок, но впоследствии я бросил попытки как научиться играть, так и привлечь чьё-то внимание."
    "То же было и с зарядкой по утрам, и со всем, что требовало методичной работы над собой." 
    "Музыкальный кружок имел смысл для тех, кто уже хоть что-то мог."
    "Меня же туда занесло то ли сочувствие к Мику, то ли естественное любопытство, если так можно назвать фривольные мысли, витавшие в районе пионерской юбки."
    "Я тяжело вздохнул, остановившись неподалёку от музклуба."
    "Из раскрытого в торце дома окна была слышна переливистая, как журчание воды, красивая мелодия."
    th "Что же, зайду тихо, чтобы не отвлечь Мику..."
    scene bg int_musclub_day
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    play ambience ambience_music_club_day fadein 1
    show mi normal pioneer far at center with dissolve
    "Мои ожидания не оправдались — пионерка была не одна."
    "Кроме неё в комнате находились две девочки и горнист Нафаня из младшего отряда, которого я видел на построении. Мику, прикрыв глаза, играла на флейте под аккомпанемент гитары, скрипки, и губной гармоники."
    "Никто из них не заметил, как я вошёл. Они ещё недолго играли, прежде чем Мику увидела меня."
    show mi grin pioneer at center with dspr
    mi "О, наконец-то ты пришёл, Семён!"
    me "Привет снова."
    if d1_us_chase:
        girl_A "Кто это?"
        girl_B "Семён, тот парень, который вчера приехал в лагерь."
    show mi laugh pioneer at center with dspr
    mi "Забыла вам сказать, что у нас новый участник кружка, вот!"
    show mi smile pioneer at center with dspr
    "Она представила нас друг другу."
    "Те две девчонки, похоже, были не слишком рады моему появлению. Наверно, это про них Мику говорила, что они нечасто приходят в кружок и отлынивают. Почему же они собрались?"
    me "А что вы тут делаете?"
    girl_A "Ты с луны свалился, Семён? На построении вожатая нам всё сказала."
    show mi scared pioneer at center with dspr
    me "Я не слушал её..."
    show mi smile pioneer at center with dspr
    "Мику поспешила сгладить назревающие углы в разговоре."
    mi "Мы разучиваем морские темы ко Дню Нептуна! Семён, будешь с нами?"
    me "Разве что на правах благодарного зрителя. Играть-то я всё равно не умею."
    show mi shocked pioneer at center with dspr
    "Глаза Мику округлились."
    mi "То есть, как не умеешь?!"
    me "От слова совсем."
    mi "Зачем же ты тогда вступил в наш кружо..."
    me "Ну хорошо, я несколько лет назад брал уроки гитары, но погоды это не меняет, потому что я забросил."
    show mi happy pioneer at center with dspr
    "Я не стал уточнять, что «несколько» — это десять лет, и сейчас же пожалел о сказанном: оптимизм Мику был непоколебим."
    mi "Значит, дело поправимо! Я могу принести для тебя акустическую гитару из складской комнаты, и самоучители по игре на разных инструментах у нас есть! Хочешь?"
    "Я не знал, что ей ответить, но всё же меня не отпускала мысль, что я бы не отказался снова попробовать от скуки, раз в лагере нечего делать."
    me "Скорее нет, чем да."
    show mi scared pioneer at center with dspr
    mi "А-а!" 
    "Она схватилась за голову."
    mi "Семён, я так не могу! Или да, или нет — что-то одно!"
    th "Ладно, не буду ломаться попусту и делать вид, будто никогда не слышал слова «музыка»."
    me "Если честно, то я не имею ничего против."
    show mi grin pioneer at center with dspr
    mi "Прекрасно!"
    show mi serious pioneer at center with dspr
    mi "А на какой гитаре ты играл?"
    me "На классической. Я сначала хотел сразу на электронной, но родители отговорили..."
    girl_A "Кхм-кхм."
    "Мы совсем забыли, что не одни в музклубе. Пионерки, стоявшие рядом, вовсе не разделяли восторга Мику."
    girl_B "Похоже, ты решила нянчиться с новичком, значит, мы тут лишние."
    show mi scared pioneer at center with dspr
    mi "Разве мы не должны вместе готовиться к празднику?.."
    girl_A "Нет-нет, вам без нас будет лучше."
    "Девочки ушли, но не на улицу, а в коридор за дверью слева от классной доски."
    me "А куда они..."
    show mi sad pioneer at center with dspr
    mi "В малый музыкальный класс. Там звуковая изоляция, так что мы друг другу не помешаем, если начнём играть."
    "Мику горько вздохнула."
    mi "Но мне кажется, что они будут просто болтать, а не разучивать мелодии."
    "В беседу вклинился пионер, за всё это время не тронувшийся с места."
    nf "Что же получается, наше занятие окончено?"
    show mi smile pioneer at center with dspr
    mi "Да, Нафаня. Но если захочешь остаться, мы продолжим втроём!"
    nf "Не, я пойду отыщу Мишку. Не могу взять в толк, чего он не пришёл..."
    "Он вернул гитару на место рядом с барабаном и кассетным магнитофоном и вышел из клуба."
    show mi sad pioneer at center with dspr
    me "Их легко понять, мы же приехали сюда отдыхать."
    mi "А я всегда думала, что музыка способна пробуждать жизнь, энергию и желание творить! И почему они не остались с нами?"
    me "Потому что иногда бывает лень, а творческое созидание тоже труд. Я сам бросил гитару по той же причине. Как по мне, труд может сделать из обезьяны только уставшую обезьяну, а не человека."
    show mi upset pioneer at center with dspr
    mi "Хорошо, Семён! А почему я не устаю от музыки?"
    me "Разве это не очевидно? Ты, наверно, очень любишь её."
    show mi surprise pioneer at center with dspr
    mi "Глупости! Я уверена, что Нафаня и Вересаев любят её не меньше чем я!"
    me "Может быть. Но самый лучший вид отдыха — смена деятельности, тем более, когда на дворе лето."
    show mi happy pioneer at center with dspr
    "Мику задумалась о чём-то."
    "Я умолчал, что в моём мире сменой деятельности для меня было переключение вкладок браузера с перерывами на еду и курсирование от монитора до кровати, чтобы почитать и поспать, а сейчас я начал рассуждать точь в точь, как мои родственники."
    th "А вдруг у Мику всё так же, только вместо компьютера — одна игра на инструментах?"
    #show tok
    show mi scared pioneer at cright with dspr
    "Не успел я задать ей вопрос об этом, как тут в помещение кружка влетел паренёк из младшего отряда."
    "Я узнал его — это он помогал Двачевской в розыгрыше."
    tok "Мику!!!"
    mi "Что тебе, Токарев?"
    $ meet('tok', u"Токарев")
    tok "Срочно научи меня играть на гитаре!!!"
    th "Интересно, что же скажет Мику?"
    show mi grin pioneer at cright with dspr
    mi "Срочно ничего не выйдет! Надо заниматься, разучивать аккорды и нотную грамоту... Но я согласна!"
    tok "Давай начнём прямо сейчас!"
    play sound sfx_brass_drop
    "Он добрался до гитары, едва не раскидав на своём пути все музыкальные инструменты в клубе. А вот пюпитр грохнулся на пол."
    show mi smile pioneer at cright with dspr
    "Мику, смеясь, подняла его и нотную книгу в мягкой обложке."
    show mi happy pioneer at cright with dspr
    mi "Видишь, Семён? Я была права! Музыка пробуждает желание творить!"
    me "Вижу, не слепой."
    th "А я был прав, что эту железную штуковину опять уронят, ха."
    show mi normal pioneer at cright with dspr
    "Токарев отмахнулся, неся гитару."
    tok "Да не надо меня учить всему, я не собираюсь быть звездой эстрады."
    tok "А вот королём дворов и подъездов — собираюсь! Мику, покажи мне, как играть блатные аккорды! Пацаны будут уважать!"
    show mi scared pioneer at cright with dspr
    mi "Какие-какие аккорды?{w} Блатные? Что это?"
    tok "А, то есть, ты не умеешь играть?"
    show mi shocked pioneer at cright with dspr
    "Мальчишка с разочарованием поглядел на Мику."
    th "Мда, просить японскую гостью научить исполнять «русский шансон» — это сильно..."
    "Надо было действовать, прежде чем Токарев спросит, слышала ли Мику полные трагизма песни об урках и подлых мусорах, и может ли она воспроизвести их на слух."
    me "Ну, я помню аккорды. Если мне не изменяет память, это Ре минор, Ми мажор и... Последний забыл."
    tok "Да-да, эти самые. Ещё Ля минор. Только я не знаю, где они на гитаре, тут же ничего не написано..."
    show mi grin pioneer at cright with dspr
    "Он печально оглядел весь гитарный гриф в поисках подробной шпаргалки для новичков. Точки-метки ладов ему ровным счётом ничего не говорили. Наверно, он думал, что это исключительно для дизайна."
    mi "О! Так бы сразу и сказали! Это легко. Садись, Марк."
    show mi happy pioneer at cright with dspr
    "Девочка поставила боком стул для Токарева, а сама примостилась рядом на табурете, вежливо позаимствовав у пионера гитару."
    mi "Первое, что мы делаем — проверяем, настроена ли гитара..."
    tok "Э, а когда я играть буду?"
    show mi smile pioneer at cright with dspr
    mi "Один момент!"
    "Хоть Мику и подкрутила колки с расторопностью, сравнивая звучание струн, за несколько секунд Токарев успел изъёрзаться на стуле, словно вшивый."
    tok "Ну?!"
    show mi grin pioneer at cright with dspr
    mi "Готово! Бери гитару."
    "Токарев закинул ногу за ногу, чтобы держать инструмент было удобней."
    show mi normal pioneer at cright with dspr
    "Мику стала объяснять Токареву что такое лады и каким нотам какие струны соответствуют, а он мучительно кивал, стараясь запомнить." 
    "Она, прислонившись к его спине, помогала найти пальцами нужные точки, где зажимаются струны для пресловутых блатных аккордов."
    th "Эге! А ведь на его месте должен быть я!"
    "Какое-то странное чувство неприятно кольнуло в сердце."
    th "И с чего бы во мне могла проснуться ревность?"
    "Казалось, Мику будет втолковывать плохо соображающему пионеру самые азы игры на гитаре целую вечность, но у Токарева неожиданно быстро кончилось терпение."
    tok "Ай, всё! Я больше так не могу. Не получается!"
    show mi scared pioneer at cright with dspr
    "Пионерка была расстроена едва ли не сильней Токарева."
    mi "Подожди! Но ты занимался всего ничего, каких-то пять минут! Нельзя вот так бросать, толком не поучившись!"
    th "Что верно, то верно. Даже меня хватило на несколько часовых занятий с преподавателем, когда я действительно хотел выучиться. А потом забил..."
    th "Но всё равно я знаю, что при желании способен на большее."
    tok "Да ладно, подумаешь! И вообще, меня футбол ждёт."
    show mi sad pioneer at cright with dspr
    "За хвастливым тоном в голосе Токарева слышалась досада. Пионер, не зная, куда деть гитару, всучил её Мику и убежал сломя голову."
    #hide tok
    th "Эх, надо было научить его песенке «Тихо в лесу» в исполнении «Красной Плесени» — осчастливил бы пионера на всё детство!"
    show mi sad pioneer at center with dspr
    "От весёлой мысли меня отвлекла крайне опечаленная Мику."
    mi "Семён, наверно из меня плохой учитель..."
    "Я не мог не отметить, с какой лёгкостью это малозначительное происшествие повлияло на её настроение и на отношение к самой себе."
    th "Как наивно. Даже слишком."
    me "Неправда, ты всё здорово рассказала, лучше моего бывшего препода, зуб даю. Это просто кто-то слишком нетерпеливый, чтобы уметь выслушать до конца."
    show mi surprise pioneer at center with dspr
    "Мику прямо расцвела у меня на глазах."
    mi "Значит, ты согласишься, чтобы я была твоим сэмпаем, а ты — моим кохаем?"
    "Я аж вздрогнул, с трудом попытавшись вникнуть в значение неведомых заморских слов, услышанных впервые. Мало ли что могло скрываться за ними?"
    me "Ты хотела сказать — сенсеем? И..."
    "Это единственное, что я мог припомнить из всего известного на японском, а слова для обозначения ученика я не знал."
    show mi smile pioneer at center with dspr
    mi "Нет, я имела в виду именно сэмпая и кохая. Это означает двух людей, как правило, близких по возрасту и статусу, занимающихся одним делом или имеющих общий интерес, в нашем случае — музыку."
    th "Общий интерес у парня и девушки? Как в пословице..."
    show mi happy pioneer at center with dspr
    mi "Сэмпай более опытен, поэтому он друг-наставник, а кохаем может называть себя только человек, соглашающийся на положение младшего." 
    "Тут я понял, что аналогия с той пословицей немного поспешна."
    show mi normal pioneer at center with dspr
    mi "Старший, напротив, старается не называть себя сэмпаем, а младшего кохаем, как того требует вежливость."
    show mi normal pioneer far at fleft with dspr
    "Мику подскочила к доске и нарисовала три японских иероглифа с переводом. Сен (саки) — раньше (первее), Ко (ато) — после, Хай — люди, человек (коллега)."
    show mi grin pioneer far at fleft with dspr
    mi "И возраст тут ни при чём, старший по возрасту может быть кохаем, если младший обладает б{i}о{/i}льшим опытом. Кто раньше поступил в школу, ученический кружок или преуспел в мастерстве, тот и сэмпай! Вот!"
    show mi smile pioneer at center with dspr
    "Мику, энергично стряхивая меловую пыль с ладоней, вернулась ко мне."
    me "Фух!.. Спасибо, теперь стало понятно."
    show mi normal pioneer at center with dspr
    mi "Не за что! А ты о чём подумал?"
    stop music fadeout 2
    me "Сложно сказать. У нас одним словом товарищ прекрасно обходятся. А то я, услышав про общие интересы, сначала подумал: «Муж и жена — одна сатана»."
    play music music_list["always_ready"] fadein 1
    show mi surprise pioneer at center with dspr
    mi "Что?! Муж и жена? Мы?.."
    show mi shy pioneer at center with dspr
    "Она густо покраснела и молниеносно села за рояль наигрывать какую-то мелодию невпопад, не глядя на клавиши и склонив голову так низко, словно хотела спрятать от меня смущение."
    show mi shy pioneer close at center with dspr
    "Я, немного запаниковав, приблизился к ней."
    me "Мику, Мику, ты чего? Я не о том!"
    "Но она решительно помотала головой, отказываясь говорить со мной. Надо признаться, это поставило меня в тупик."
    show mi surprise pioneer close at center with dspr
    "Я на миг перестал допытываться почему мои слова произвели на неё такое впечатление, как вдруг музыка споткнулась на высокой ноте, и Мику глянула на меня с непониманием на лице — любопытство перебороло стыд."
    mi "А почему сатана?"
    me "Это значит враг. Двое похожих людей как один противник."
    me "Когда два человека заодно, они одно и то же, у них общие интересы и цели, даже если между ними возникнет ссора. Ну да, обычно так говорят про мужа и жену или пару на самом деле, если они схожи характерами и поступками."
    show mi happy pioneer close at center with dspr
    mi "Я поняла. Сколько здесь живу, ни разу не слышала такой пословицы, но у нас тоже есть такое выражение, вот прямо один в один! Но попроще: «Нита моно фуфу». Муж и жена — похожие люди."
    stop music fadeout 2
    "Теперь Мику восприняла всё гораздо спокойней, но всё ещё было заметно, что мои слова до этого вогнали её в краску."
    play music music_list["lightness"] fadein 2
    me "Ну вот, прояснили все недоразумения.{w} Так чем вы тут занимаетесь? Что за мелодии ко Дню Нептуна?"
    show mi grin pioneer close at center with dspr
    mi "А, да-да-да! Совершенно верно! Это на морскую тему, будем играть под несколько моментов на мероприятии." 
    mi "Надо продолжать готовить, иначе завтра вожатые нас не похвалят."
    me "Такое чувство, будто вожатые средневековые монархи, а мы — шуты — должны их развлекать."
    show mi happy pioneer close at center with dspr
    mi "Да ладно тебе, Семён! Есть ещё другие пионеры, и кто-то должен выступать для них. Разве не интересно поучаствовать в самодеятельности? Посмотри на это с положительной стороны!"
    th "Я бы посмотрел с положительной стороны — это если я среди зрителей, а на сцене бы выступала стайка симпатичных девушек в форме группы поддержки."
    show mi normal pioneer at center with dissolve
    "Мику обошла расставленные на полу инструменты и достала с самой верхней полки белую книжку."
    show mi smile pioneer at center with dspr
    mi "Будешь сам готовиться по самоучителю или тебе нужна моя помощь, как Токареву?"
    "Я на секунду вспомнил о мимолётном желании, чтобы Мику поучила меня." 
    th "Может быть, после того разговора о неправильно понятой пословице это не самая лучшая идея, несмотря на то, что Мику быстро переключилась с одного на другое."
    me "Сам управлюсь. Я уже занимался гитарой, надо только вспомнить основы. Мои пальцы давно отвыкли от струн, так что я потренируюсь."
    show mi grin pioneer at center with dspr
    mi "Хорошо! Но если будут трудности, спрашивай, помогу! Хорошо?"
    me "Идёт."
    me "Кстати, я тебе не помешаю своим бренчанием?"
    show mi normal pioneer at center with dspr
    mi "Нисколько! Ты на акустике играть собрался? Могу принести!"
    me "Не надо, эта сгодится."
    "Девочка отдала мне гитару, а сама взяла флейту."
    hide mi with dissolve
    "Я подхватил стул и отнёс его с книжкой и гитарой к барабану возле меловой доски."
    "В этой комнате не было ни одного столика или парты, поэтому я положил раскрытый самоучитель прямо на барабан."
    "Даже прочитав одно введение, я ощутил громадный пробел в музыкальных знаниях. Ещё бы, всё было так давно, что сейчас вникал в тонкости словно в первый раз."
    "Самоучитель вежливо напоминал, как правильно держать левую руку. Как выяснилось, и это я тоже успешно забыл."
    th "О-окей!.."
    "Пальцы пробежались по струнам над розеткой гитары. Нейлон. Негромкое, глубокое звучание. Классика."
    "Но десять лет тому назад интереса к внешней стороне дела мне было недостаточно, чтобы заставить себя собрать волю в кулак и учиться дальше, я забросил, потому что откладывал на потом и занимался куда более простыми вещами, не требующими труда над собой."
    "Прежде чем освежить память об октавах, длительностях нот и пауз, я должен был снова привыкнуть жать струны, поэтому я сразу отыскал таблицу аккордов."
    "Для начала с меня, белоручки, хватит ставить пальцы на позиции. О хитровыдрюченных пассажах, героических позах для сцены и мотании головой в такт можно было только мечтать."
    "Практика, которую я себе выдумал, смахивала на обычные физкультурные упражнения, только вместо приседаний и отжиманий я делал подходы к аккордам."
    "Медленно и старательно, как того не понимал Токарев. По нескольку раз, чтобы безошибочное исполнение въелось в подкорку, но всё же основной задачей было привыкнуть к гитаре."
    "..."
    $ proficiencies ['kn_music']+=1
    "Аккорд за аккордом незаметно для меня утёк час."
    stop music fadeout 2
    th "Мику что-то там говорила про нормативы... Надеюсь, вожатые удовлетворятся, если я натренькаю им «Во поле берёзка стояла» и на том покончу с гитарой."
    play music music_list["miku_song_flute"] fadein 1
    "По комнате раздавались не только мои аккорды, которые я извлекал со страшной осторожностью, чтобы не помешать Мику. Её красивая мелодия на флейте звучала негромко, но так же переливно, как мне довелось услышать на пути к музклубу."
    show mi happy pioneer far at center with dissolve
    "Перестав бренчать, я отвлёкся."
    "Даже без аккомпанемента скрипки, гармоники и гитары музыка была самодостаточной, цельной."
    th "Потрясающе."
    "Мику играла безмятежно и легко, но с чувством, вызывая в уме живые образы: казалось, мелодия уносила меня куда-то на ветреный берег южного моря, где остаёшься один на один с природой. Музыка зачаровывала красотой и тайной."
    "Кое-что не оказалось обманом воображения — в самом деле ветерок гулял по классу из-за распахнутого настежь окна, возле которого сидела Мику, держа флейту боком. Ветер растрепал на лбу девочки чёлку голубо-зелёных волос."
    "От моего внимания не укрылось, что Мику была крайне миловидной лицом, не лишённым изящества."
    "Её прелестные губы приникли к дульцу флейты, чуть сжатые для римтичных дуновений, которыми рождался тот чудесный воздушный звук непрерывной мелодии."
    "Похоже, я поддался не только очарованию музыки, но и её исполнительницы..."
    th "Она безусловно талантлива. С талантом она, скорее всего, не пропадёт."
    "Я вспомнил, что хотел спросить у Мику — не связаны ли такие достижения с тем, что музыка её единственное занятие?"
    stop music fadeout 1
    "Девочка перестала играть, и я поймал момент."
    play music music_list["two_glasses_of_melancholy"] fadein 2
    me "Здорово получилось. Не будь мои глаза открытыми, я бы подумал, что нахожусь не в этом душном помещении, а у моря."
    show mi surprise pioneer far at center with dspr
    mi "А?! Спасибо-спасибо, Семён! Я даже не поняла, что ты меня слушал! Хотя должна была, ведь перестала звучать твоя гитара."
    me "Да, увлёкся тем, как... как ты играешь. Скажи, долго училась?"
    show mi grin pioneer far at center with dspr
    mi "С четырёх лет! Но не только на флейте, на других инструментах тоже."
    me "И кроме этого больше ничего?"
    show mi upset pioneer far at center with dspr
    me "Ни свободного времени, ни прогулок с друзьями? Знаешь, я бы на твоём месте не смог бы успеть всё. Даже безо всяких кружков я не заимел вменяемых приятелей."
    show mi scared pioneer far at center with dspr
    mi "Что ты, Семён, конечно у меня есть друзья и подруги!{w} И дома, и у вас, в СССР. Правда, в лагере их поменьше всё-таки, всего неделя прошла.{w} Но мы ладим!"
    me "Рад за тебя."
    show mi happy pioneer far at center with dspr
    mi "Спасибо!"
    th "Зря я надеялся услышать что-то другое и вообще судил о ней преждевременно."
    th "Но Мику не уловила язвительности моей интонации, просто поверила на слово. Странная девочка."
    show mi smile pioneer far at center with dspr
    "Я снова отгородился от неё гитарой."
    me "Ладно... Мику, если я разучу «Во поле берёзка стояла» и «Сел комарик на дубочек» — этого хватит вожатым?"
    show mi serious pioneer far at center with dspr
    mi "Ты не беспокойся, они не будут требовать от тебя сложного. Но если ты умеешь хорошо играть, то зададут что-нибудь посерьёзней, как мне вот сегодня к празднику Нептуна."
    mi "Но для меня и это очень-очень лёгкое поручение."
    th "Ага, после стольких лет занятий музыкой."
    me "Хорошо, я как выучу те две песни, попробую сыграть, а ты оценишь."
    show mi smile pioneer far at center with dspr
    "Мику с радостью покивала и снова взяла флейту."
    hide mi with dissolve
    "Я не пытался даже представить, что могу целиком посвятить себя чему-то. Мне бы «комарика» сначала осилить."
    "На примере упомянутой песни с двумя уже известными аккордами я попробовал другой метод боя по струнам — щипком, принцип которого вспомнил сразу. Не такая уж и дырявая у меня память."
    stop music fadeout 2
    "......"
    "........."
    play music music_list["get_to_know_me_better"] fadein 1
    "Я не имел понятия, сколько прошло времени, когда Мику перестала музицировать."
    mi "Семён... Семён..."
    show mi smile pioneer far at center with dissolve
    me "М?"
    show mi normal pioneer far at center with dspr
    mi "Хочешь, я тебе что-нибудь сыграю?"
    me "А я?"
    show mi smile pioneer far at center with dspr
    mi "Не спеши, успеешь! Ну так что, хочешь?"
    me "Давай. Только не знаю, что именно."
    show mi normal pioneer far at center with dspr
    mi "А что тебе нравится?"
    "Я пожал плечами."
    me "Слушаю всё, от чего кровь из ушей не идёт. Если вещь хорошая и нравится мне — я незамедлительно скачиваю её, чтобы иногда ставить в качестве лекарства от скуки."
    show mi happy pioneer far at center with dspr
    mi "Хорошо, тогда я сыграю свои любимые композиции."
    "Она сложила флейту в продолговатый кейс-футляр и села поближе к роялю."
    show mi grin pioneer far at center with dspr
    mi "Сначала то, что нашла у вас..."
    me "Так вот сразу стало любимым?"
    mi "По-другому быть не могло! Просто классный сборник, тут столько всего!"
    show mi smile pioneer far at center with dspr
    "Она светло улыбнулась мне и быстро перелистнула страницы нотной книжки."
    mi "Это из репертуара восьмидесятых."
    show mi normal pioneer far at center with dspr
    "Не называя произведения, девочка начала играть, покачивая головой в такт ритмичной мелодии."
    "Вдруг Мику запела."
    mi "Na-na-na-na-na..."
    "Я с изумлением поднял брови, силясь угадать песню, и только после нескольких повторившихся строк я узнал её. Мику выбивала пальцами на бело-чёрном переплетении клавиш скачущий, точно пульсирующий мотив, наполненный жизнью."
    "Девочка почти не смотрела на руки, лишь поглядывала в песенник и на меня, вкладывая весь дух в песню."
    mi "When we all give the power,{w}\nWe all give the best!"
    mi "Every minute of an hour{w}\nDon't think about the rest..."
    "Теперь я понял, за что ей полюбилась эта композиция."
    "У Мику был чудесный голос — слушать её было одно удовольствие. Удивительно приятный, дарящий мягкость строкам песни, но не умаляющий её энергичности."
    mi "Live is life, come on, stand up and dance!"
    th "...И нежный."
    "Я вздрогнул, когда подумал об этом, и запрятал мысль куда подальше, будто Мику могла прочесть её у меня на лице, но не в самый далёкий уголок памяти, чтобы не забыть."
    "Конечно, такая, гм, легкомысленная девочка вряд ли бы смогла понять, о чём я думал, разве что интуитивно... Я попытался принять самый безэмоциональный вид, на какой был способен. Получилось не очень."
    "А Мику, не обращая внимания на мои ужимки, играла, пока не закончила восклицанием «Live is life!», тем самым поставив точку в песне."
    "Тут я не стал сдерживать улыбку."
    me "Круто. Учитывая, что ты успела мне наговорить про музыку, песня тебе целиком подходит."
    show mi happy pioneer far at center with dspr
    me "Будешь исполнять её на Дне творческой самодеятельности?"
    show mi surprise pioneer far at center with dspr
    mi "Ой, Семён, я даже не задумывалась о таком! По правде, я хотела бы сыграть что-то своё, я пишу музыкальную композицию."
    me "Воу, не ожидал. Сыграешь?"
    show mi grin pioneer far at center with dspr
    mi "Она же ещё не готова! А что, мало было?"
    "Мику засмеялась."
    me "Признаюсь, да."
    show mi smile pioneer far at center with dspr
    mi "Ну хорошо, если так..."
    "Впервые в её голосе послышалось коварство."
    show mi normal pioneer far at center with dspr
    mi "Сыграю тебе одно продолжительное произведение, тоже из моих любимых, поэтому я прекрасно знаю его. Готовься, четырнадцать минут!"
    me "Что?!"
    "Я даже не смог возразить."
    show mi laugh pioneer far at center with dspr
    mi "Четырнадцать минут ещё ничего! Есть композиции подлинней, а самая рекордная симфония длится около пятнадцати часов."
    me "Бесспорно, разница есть. Спасибо за утешение!" 
    "Была у меня привычка иногда мучить плеер многократным проигрыванием плейлиста с самыми понравившимися треками, и б-г знает, сколько часов жизни это заняло у меня, но сейчас я призадумался, а смог ли бы я столько времени слушать только Мику?"
    show mi smile pioneer far at center with dspr
    mi "Я сыграю то, что я выучила несколько лет назад и исполняла на приёме в московской консерватории."
    "В голове родилась целая туча вопросов, но я задал самый глупый и очевидный, позабыв об остальных."
    me "Ты учишься у нас?"
    show mi grin pioneer far at center with dspr
    mi "Нет, но буду с сентября! Я здесь по обмену, а у отца как раз строительный проект в России, поэтому мы с родителями переехали сюда только на один год... А чтобы не терять время и практиковаться дальше, я в июне ходила на подготовительные занятия в одном из вузов, дающих музыкальное образование. Между прочим, там преподаёт очень хороший папин знакомый."
    "Многословность Мику лишила меня необходимости расспрашивать о подробностях, так что я просто кивнул."
    show mi normal pioneer far at center with dspr
    "Девочка поправила хвосты волос, выпрямилась и простёрла руки над клавишами."
    "Как объяснила Мику, она собиралась играть увертюру известного композитора, однако я о таком никогда не слышал даже в своём мире: я и классическая музыка существовали в разных плоскостях."
    "Композиция началась осторожными прикосновениями и негромким перебором нот, пока не переросла в заливистую трель — пальцы Мику порхали до самой паузы, завершавшей первый этап, вновь сменившийся игривой и беглой трелью в безудержно скором темпе."
    "Звонкая мелодия со временем угасла, а за ней полилась эпическая и берущая за душу, словно воспевалась чья-то борьба, а затем — триумф."
    "Мику была невероятно напряжена и даже ни разу не оглянулась в мою сторону, следя за своими руками, и то же волнение передалось мне, будто мы не в музыкальном кружке, а на важном концерте перед тысячами зрителей, и на ней лежит большая ответственность за выступление. И на мне, как её знакомом..."
    "Последняя часть этой необычной композиции совместила в себе приподнятый лейтмотив первой и торжественность третьей. Чувствуя завершение, Мику постепенно расслаблялась, но не прерывала строя интенсивной музыки. И, наконец, трижды прозвучал возвышенный заключительный аккорд."
    "Я был уверен, что тут прогремели бы овации публики, не будь я единственным слушателем Мику и в музыкальном кружке. Хотелось похлопать, но я постеснялся, представив, как глупо это будет выглядеть со стороны."
    "Оттого было неловко говорить «браво» в гордом одиночестве польщённой девочке." 
    show mi happy pioneer far at center with dspr
    me "Я вообще не поклонник классики... Всегда думал, что это для напыщенных зазнаек в пингвиньих костюмах, но..."
    show mi laugh pioneer far at center with dspr
    "Мне пришлось прервать слова похвалы, потому что насмешил Мику. Я, с трудом давя с чего-то вдруг возникшую улыбку и менторски покачивая пальцем, пытался снова обратить на себя внимание старосты."
    show mi grin pioneer far at center with dspr
    me "Так вот, Мику, так вот... Ты смогла изменить моё мнение. Мне кажется, если в будущем найдётся с чем сравнить твою игру, то первое впечатление останется самым лучшим."
    show mi cry_smile pioneer far at center with dspr
    mi "Спасибо!"
    "Похоже, я даже переборщил — Мику утёрла слезинку в уголке глаза. Или она это от смеха?"
    show mi smile pioneer far at center with dspr
    mi "Давай теперь ты. Выучил «комарика»?"
    me "Э-э, вроде бы, я думаю, что ещё не отработал упражнение как следует."
    play sound sfx_dinner_jingle_speaker
    "С улицы из динамиков громкоговорителя донёсся голос вожатой Инги Максимовны, возвещавший о том, что пионеры приглашаются в столовую. Объявление было спасительным во всех смыслах: я не стану вымучивать песенку на гитаре перед Мику и наконец поужинаю, а то желудок давно забыл о полднике."
    "Мимо нас к выходу прошли те две девочки, занимавшиеся невесть чем в соседнем классе. Я отложил гитару в сторону, а Мику закрыла клавиатуру рояля и окно."
    me "Давай я завтра ещё немного попрактикуюсь, а потом сыграю. Хорошо? Пора на ужин."
    "Мику бросила взгляд на часы."
    mi "Что-то сегодня рано нас позвали."
    me "Тем лучше, по-моему. Страсть как хочется поесть."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    scene bg ext_musclub_day
    with dissolve
    play music music_list["she_is_kind"] fadein 1
    window show
    show mi normal pioneer close at cleft with dissolve
    "Тем не менее, когда мы вышли наружу, я не побежал к столовой, как полоумный, а неторопливо пошёл рядом с Мику, потому что созрел до ответа на её предложения."
    me "Слушай, насчёт сэмпая и кохая...{w} Я согласен.{w} Как я должен обращаться к тебе? Мику-сэмпай?"
    show mi scared pioneer close at cleft with dspr
    mi "Не надо, Семён, я передумала."
    me "Как, уже?"
    show mi sad pioneer close at cleft with dspr
    mi "Я не сказала, что у нас такие отношения налагают обязанности: сэмпай руководит, а подчиняющийся исполняет указания..."
    "Мысли покатились в интимно-эротическом направлении, где властная девушка с невыносимо распутным взглядом сверху вниз касается моей щеки ножкой в чулке и приказывает действовать исключительно ртом и языком..."
    "Голос Мику дрогнул."
    mi "Любые, не только по делу, он может заставить выполнять мелочные или унизительные вещи, всё зависит от характера человека, оказавшегося в положении старшего." 
    th "Ну да, нетрудно представить: начальник просит офисного работника сделать ему кофе. В худшем случае, речь шла о дедовщине."
    mi "Конечно, я не стала бы поступать как нехорошие люди. Но я не об этом."
    show mi shy pioneer close at cleft with dspr
    mi "Мне долго пришлось привыкать общаться без употребления именных суффиксов, без них в Японии мы обращаемся лишь в семье и к очень близким друзьям. Или когда мальчик и девочка...{w=0.5} встречаются."
    th "Теперь ясно, почему она тогда смутилась.{w} Ох уж этот этикет!{w} Не могу судить обо всех японцах по ней, но если говорить конкретно про Мику, то я порвал бедняжке шаблон."
    mi "Я хотела поделиться с тобой тем, какие у нас обычаи, но потом засомневалась, когда ты сказал про товарищей и вообще...{w} Это ведь не ты у меня в гостях, а я у вас, и мне надо следовать вашим традициям и не навязывать своих. Извини меня, Семён!"
    show mi shy pioneer close at center with dspr
    "Она остановилась для поклона."
    me "Да ладно тебе, ничего преступного ты не сделала. Тем более, я узнал что-то новое."
    show mi happy pioneer close at cleft with dspr
    "Мику испытала большое облегчение, и мы тронулись с места."
    scene bg ext_square_day
    with dissolve
    show mi smile pioneer close at cleft with dspr
    mi "Вы так легко общаетесь без суффиксов и ограничений, будто все друг другу близкие братья и сёстры! Или будто у вас все равны.{w} Наверно, поэтому вы называете себя Советским Союзом?"
    "Моя радость испарилась."
    "Я умолчал, что всегда найдутся те, для кого одни люди равнее других, независимо от действующего порядка. Этим сейчас я бы сбил Мику с толку. Да и вообще, с ней о том не стоило говорить."
    me "Во многих странах нет такого, и это ещё не делает их Советским Союзом."
    me "Думаю, что наши языки и традиции просто сформировались в разных исторических условиях, всего-то. Я подозреваю, что в чём-то даже найти сходство, например, в официально-деловых отношениях, просьбах и приглашениях. Вон, даже нашли редкой пословице пару."
    show mi normal pioneer close at cleft with dspr
    mi "Да, у нас тоже есть слова, означающие «товарищ». Хобай и доси. Кандзи Хо может читаться как «томо» — друг, кандзи До — одинаковый, а Си — воля... или цель."
    scene bg ext_dining_hall_away_day
    with dissolve
    show mi normal pioneer close at cleft with dspr
    "Она перечислила ещё шесть слов, с похожим переводом, но разным контекстом, определяющимся мерой близости и обстоятельствами знакомства."
    show mi smile pioneer close at cleft with dspr
    mi "Как ты считаешь, которое больше подходит?"
    th "Раз мы в СССР, то в слове заложен политический смысл: все идут к общей цели — построению коммунизма."
    me "Правильно второе — «доси», оно официальное, партийное. Но мне оно кажется неудачным. Ну какие из нас члены партии? Или один человек борется за достижение коммунизма, а другой не хочет, и в обращении к нему появляется элемент принуждения к общей цели."
    show mi upset pioneer close at cleft with dspr
    "Я потёр нос."
    me "Короче, есть нюансы..."
    me "Лучше в значении «друг». Как там? «Ю», читающееся как «томо» в слове «томодачи».{w=0.8} Потому что со временем оно может превратиться в «синъю»."
    #Здесь можно было сделать всплывающую сноску с переводом, но это бы нарушило замысел и патетику момента.
    me "И вот это мне нравится больше всего."
    show mi shy pioneer close at cleft with dspr
    mi "Я поняла, Семён!"
    "Она притихла, отведя взгляд куда-то под ноги."
    "Если между нами была стена из множества отличий, разделяющих людей двух культур, то сейчас нам удалось отыскать в ней брешь."
    scene bg ext_dining_hall_away_day
    with dissolve
    show mi normal pioneer close at center with dspr
    "Мы примкнули к пионерам, выстроившимся в очередь на крыльце столовой."
    show mi happy pioneer close at center with dspr
    mi "Зачит, я должна говорить «товарищ Семён»?"
    me "Э-э, кажется, мы уже обсудили, что у нас можно без суффиксов и уточнений. Забыла?"
    show mi shy pioneer close at center with dspr
    mi "Ой."
    "Девочка вспыхнула краской смущения и отвернулась, как раз когда очередь двинулась вперёд. К Мику неожиданно присоединились её подружки из лагеря, которых я не знал. В их весёлый щебет я не стал вникать."
    hide mi with dissolve
    "Я устало шёл следом."
    th "Сэмпай! Какая ирония!"
    "Даже тут Мику была первой — она приехала сюда раньше."
    "Ей нипочём не догадаться, только если я не скажу, что сам в этой стране впервые и точно такой же гость, как и она. Но в то же время я совсем одинок, в отличие от неё."
    "Поэтому я не выбрал слов со значением равенства товарищей."
    "Мы не совсем «одно и то же», но «почти» не считается."
    stop music fadeout 4
    window hide
    scene black
    with dissolve
    window show
    "..."
    "......"
    "........."
    window hide
    $ d2_girls_event = (d2_girls_event) + (1)
    $ d2_mi_day = True
    $ lp_mi = lp_mi + 1
    $ disable_current_zone()
    jump d2_pre_event

label d2_green_theatre_day:

    $ reset_chibi("estrade")
    $ disable_current_zone()
    scene bg ext_square_day
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    window show
    "Послонявшись немного около площади, я решил сходить к сцене."
    if d2_times_been_to_green_theatre == 1:
        th "Место неплохое, можно побыть в одиночестве и притом не маячить перед вожатыми, которым лишь бы припрячь заняться делом."
    else:
        th "А ведь я там ещё не был ни разу... Интересно посмотреть."
    scene bg ext_stage_big_day
    with dissolve
    "Миновав укрытую меж соснами узенькую дорожку, я вышел к эстраде."
    "Как мне уже было известно, сцена и площадка с лавочками перед ней называлась «Зелёным театром». Очень подходяще, когда вокруг одни кусты да деревья."
    "Тихо, ведь никого не..."
    show dv normal pioneer2 far at center with dissolve
    "Я увидел Алису. Она читала стенгазету, приколотую к стенду канцелярскими кнопками."
    th "Наверно, ей все эти самые кружки до лампочки. Сачкует, как я."
    scene bg ext_stage_normal_day
    with dissolve
    show dv normal pioneer2 at center with dspr
    "Алиса то ли услышала меня, то ли почувствовала моё присутствие и с опаской обернулась, когда я подошёл ближе."
    dv "А, это ты..."
    show dv normal pioneer2 at cleft with dspr
    "Она расслабилась и чуть посторонилась."
    me "Что делаешь?"
    dv "Читаю, что делали пионеры до нас."
    "Я пробежал взглядом по стенгазете."
    "Гвоздём номера был концерт на Дне творческой самодеятельности, который провели дети с предыдущей смены."
    "Судя по развешанным заметкам, жизнь лагеря состояла из соревнований, игр, концертов и прочих увеселительных мероприятий. На снимках неизвестные пионеры играли в футбол, плыли куда-то на лодках, стояли на сцене и, видимо, пели хором."
    "Рассматривая центральную статью, я не смог не заметить некоторое сходство Алисы и девчонки на переднем плане фотографии и решил уточнить."
    me "Двачевская, а не ты ли тут на сцене с микрофоном? Фотка мутная, лица не видно."
    show dv angry pioneer2 at cleft with dspr
    dv "Ты спятил, эта девка страшная как война, вообще не похоже."
    me "Зато, наверное, хорошо спела, раз её всё же сфоткали. А ты совсем-совсем не поешь?{w} А-а, прокуренный голос... Понимаю. Но могла бы петь песни Высоцкого, там же можно с хрипотцой..."
    show dv rage pioneer2 at cleft with dspr
    if d2_dv_fight:
        me "Сеня, ты сейчас дошутишься — фальцетом запоёшь! Если мы опять подерёмся, то у тебя точно будет высокий тенор и карьера в опере."
    else:
        me "Сеня, ты сейчас дошутишься — фальцетом запоёшь! Если мы подерёмся, то у тебя будет высокий тенор и карьера в опере."
    th "...Эх, Алиска, для тебя опера — это музыка, а для меня — браузер!"
    #Под катом текст для времени действия в конце 80-ых: и это слово ты узнаешь только лет через десять. Да и в музыке тебе еще предстоит столько открытий, а для меня это будет лишь музыка прошлого десятилетия.. 
    me "Не стоит, я дорожу своим, кхм, голосом."
    show dv angry pioneer2 at cleft with dspr
    #"Я чуть не сказал: «Он тебе ещё пригодится!»."
    th "Спеть ей, что ли, песню про Элис?"
    me "А знаешь, Дваче..ХМ!..вская, я ведь вообще-то сам песни сочиняю и пою."
    show dv grin pioneer2 at cleft with dspr
    dv "Да ладно врать-то!"
    th "И правда, с сочинением я прихвастнул. Будто мне дома больше нечем заняться!"
    me "Ну хорошо, вот слушай, не моя песня, но сойдёт... Гхм-гхм..."
    show dv smile pioneer2 at cleft with dspr
    dv "Что ты всё кхекаешь да кашляешь-то, Семён? Язык проглотил?"
    "Не отшучиваясь в этот раз, я просто начал петь."
    me "С нами Вовка, с нами Вадим.\nОттянуться всей компанией хотим."
    me "И гитары взяли мы с собой, чтоб песни пелись."
    "Я ловко взбежал по скрипучим ступенькам на эстраду, изображая игру на невидимой басухе."
    show dv smile pioneer2 at center with dspr
    me "С нами Алла, с нами Филипп.\nЕго никто не звал, он как-то сам прилип."
    me "И тут один из нас сказал: а пойдемте к Элис!"
    me "А что это за девочка и где она живет?\nА вдруг она не курит, а вдруг она не пьет?"
    show dv angry pioneer2 at center with dspr
    "Тут Алиса перестала ухмыляться моему перфомансу и насупила брови." 
    me "Ну а мы в такой компании возьмем да и припремся к Элис!"
    me "Красиво одевается,\nКрасиво говорит.\nИ знает в совершенстве английский и иврит."
    show dv grin pioneer2 at center with dspr
    "На Двачевскую это подействовало успокаивающе."
    me "Ну а мы с такими рожами возьмем да и припремся к Элис..."
    show dv surprise pioneer2 at center with dspr
    "На лице Алисы отобразилось вполне настоящее изумление."
    dv "Вот это да-а, Сеня... Неплохо поёшь, в самом деле."
    show dv laugh pioneer2 at center with dspr
    dv "Теперь я на все сто уверена, потерей чего угрожать тебе!"
    "Я спрыгнул на землю."
    me "Э! Я тут всей душой, а ты! Где благодарность публики?"
    show dv grin pioneer2 at center with dspr
    "Девочка тряхнула хвостами-молниями."
    dv "Перепеть любой дурак может. А своё где?"
    me "А переделка считается за сочинение? Я вот хочу изменить следующий куплет, чтобы начинался словами «С нами Шурик, с нами Сергей — Он отличный парень, несмотря на то, что...» А дальше я ещё не придумал."
    show dv smile pioneer2 at center with dspr
    dv "Ха-ха, ты про всех так переделай на злобу дня, только смотри, если про меня ерунду сморозишь, попрощаешься с голосом." 
    me "Но я половину пионеров в глаза не видел, как я могу придумать что-то правдоподобное? Лучше про тех, с кем хорошо знаком. Вот одну Элис уже знаю, например. И зачем вообще..."
    show dv grin pioneer2 at center with dspr
    dv "Споёшь эту песню на концерте."
    th "Да меня за такое пионеры догонят и поколотят."
    me "А в нашу смену тоже дадут концерт?"
    show dv normal pioneer2 at center with dspr
    dv "Как минимум, участники музкружка. Они там будут петь свои унылые песни."
    "Она щёлкнула пальцем по листу стенгазеты, точно в нос поющей пионерке с фотографии."
    th "...Спеть им Шнура ради лулзов? Тогда меня уже сами вожатые посадят в карцер. Здесь же всяко есть карцер? Хотя кого я обманываю, какой концерт, какие песни, если меня в маршрутке-то не слышат, когда я прошу остановиться?"
    show dv scared pioneer2 at center with dspr
    dv "Тс-с, Шляпа идёт, прячься!"
    hide dv with dspr
    "Попадаться Ольге Дмитриевне и выслушивать её расспросы, почему мы не в кружках, я не хотел, поэтому машинально побежал за Двачевской."
    scene bg ext_stage_big_day
    with fade
    play sound sfx_hiding_in_bush
    "Мы укрылись в ближайшем рассаднике черники."
    show mt normal pioneer far at left with dissolve
    "Вожатая показалась у самых дальних лавочек, обошла их и сцену в поисках блудных пионеров. К счастью, нам хватило ума не прятаться в очевидном месте."
    show mt normal pioneer far at center with dissolve
    "Ольга Дмитриевна разок оглядела всю площадку и ушла ни с чем."
    scene bg ext_path2_day
    with dissolve
    "..."
    show dv normal pioneer2 at center with dissolve
    "Алиса осторожно вышла из-за куста, глядя вдаль, но возвращаться к стенду пока не решалась."
    me "Так, насчёт концерта — не вижу смысла участвовать. Лень надрываться."
    dv "Угу. Там же Мику будет первой звездой, наверное. Я и говорю — унылый праздник выйдет."
    me "Не нравится, как она играет?"
    show dv angry pioneer2 at center with dspr
    dv "Мне не нравится, что она гитару зажала. Она же просто так играть не даст, заданиями всякими парит. Да ну её, и кружок этот тоже."
    me "А куда ты вообще записалась?"
    show dv normal pioneer2 at center with dspr
    dv "В спортивный, как Ульяна."
    th "Breaking news!"
    me "Почему? Спортсменка-комсомолка?"
    show dv grin pioneer2 at center with dspr
    dv "Ты чего, просто Дмитрий Евгеньевич халявить позволяет, лучше кружка не придумаешь."
    me "Но ты в музклуб хочешь, я правильно понял? Ну так сдай Мику эти задания! Или что, это так сложно?"
    show dv normal pioneer2 at center with dspr
    dv "Сеня, смешно сдавать какого-нибудь «Кузнечика», когда играешь рок-н-ролл. И кому? Ей? Она только «Жёлтые тюльпаны» из трех нот поёт. Да лучше я стащу эту гитару, чем так вот."
    me "Ага, и будешь лабать втихушку на пеньке в лесочке. А дятлы на ударных."
    show dv angry pioneer2 at center with dspr
    dv "Очень смешно!"
    me "Я ведь могу поговорить с Мику, да ты и сама можешь, вы не враги ведь."
    show dv sad pioneer2 at center with dspr
    dv "Ни черта ты не понимаешь."
    "Алиса отвернулась и демонстративно вздёрнула нос."
    th "Да проще взять на время гитару по-тихому, чем убедить Алису записаться в музкружок! Тем более, там наверняка не одна гитара." 
    menu:
        "Предложить авантюру" if (sp_crg >= 2):
            $ sp_crg = sp_crg + 1
            $ lp_dv = lp_dv + 2
            th "Всё равно непонятно — может, все это не по-настоящему? По крайней мере, эта игра в пионеров мне начинает нравиться."
            th "Не привнести ли мне в неё ещё некоторого разнообразия? Может, это Алиса на меня так влияет, но сегодня я хочу немного побыть плохим, ужасным, отвратительным пионером (каким я на самом деле и являюсь)..."
            me "Ну хорошо, пойдем ночью стащим эту треклятую гитару, будешь играть подпольный рок ночами в котельной... Пока нас не поймают. Потом тюрьма, дурка — и вот мы уже идолы рок-музыки!" 
            show dv smile pioneer2 at center with dspr
            "Я проговорил всё это вполголоса и задумался — а почему бы и нет, чёрт возьми?"
            "Алиса пропустила мимо ушей мои фантазии, зато хорошо услышала про возможность заиметь гитару."
            show dv grin pioneer2 at center with dspr
            dv "Да ладно! И как ты думаешь стащить её?" 
            "...Я как-то взломал аккаунт одного Интернет-деятеля и написал ему там гадостей. Но на этом мой криминальный опыт кончался. Тем не менее, в голове есть сотни прочитанных детективов."
            me "Ну-у... Прежде всего, надо проследить, кто ходит в клуб, что там делает и во сколько уходит. Потом: узнать, куда девают ключ от замка. А дальше действовать по ситуации." 
            show dv smile pioneer2 at center with dspr
            dv "А что там следить? В клубе обычно только Мику, иногда несколько человек. Если она уходит, то клуб закрывает, после ужина ключи относят в админцентр."
            me "Тогда посмотрим, как можно проникнуть в кружок. Только пойдём через лес вдоль ограждения, чтобы нас не увидели."
            "..."
            "В лесу было тихо, свежо и прохладно, трава приятно шуршала под ногами. Как за деревьями мелькнул последний жилой домик, мы с Алисой перебежками двинулись через еловый перелесок к светлому зданию."
            stop music fadeout 2
            scene bg ext_musclub_day
            with fade
            play music music_list["always_ready"] fadein 2
            show dv normal pioneer2 close at cright with dissolve
            #show tok
            mi "Ты куда?! Подожди!"
            #hide tok
            "В нескольких метрах от дороги пришлось застыть на месте и подождать, пока мимо нас не пронесётся галопом Токарев. Что он забыл в музкружке?"
            "Ещё чуть погодя из помещения клуба стала доноситься музыка — похоже, Мику вернулась к роялю и снова стала что-то репетировать. Окно было открыто, и это привлекло внимание Алисы."
            show dv smile pioneer2 close at cright with dspr
            dv "Семён, отвлеки её, я в окно залезу."
            "Наша затея пробудила во мне азарт и дурашливое настроение, как вчера у Электроника на пристани."
            me "Зови меня... хм... Сиплый! Не произноси имен — мы теперь банда."
            show dv normal pioneer2 close at cright with dspr
            dv "Сеня, дурью не майся! Нам нужна гитара."
            hide dv with dissolve
            "Я вынужденно отправилася на веранду музклуба."
            th "Кому — гитара, а мне вот охота побыть Джеймсом Бондом, или хотя бы Розовой пантерой в шляпе, и вообще!" 
            th "Семён под прикрытием внедряется в ряды секты свидетелей советского джей-рока, и помогает адепту истинного митола Алисе выкрасть артефакт, замаскированный под гитару производства Ленинградского Завода Деревянных Предметов, дабы в далеком будущем миллиарды простых школьников не някали бы в соцсетях, а слушали песни Королей!"
            th "Или уже поздно, если вспомнить, какой сейчас год на дворе?"
            stop music fadeout 2
            th "Эх! Как бы отвлечь Мику?"
            play sound sfx_open_door_2
            $ renpy.pause(1)  
            "На мой стук никто не ответил, музыка внутри клуба не прекратилась, и я решил войти."
            window hide
            scene bg int_musclub_day
            with dissolve
            play music music_list["80s_youre_my_heart"] fadein 0
            play ambience ambience_music_club_day fadein 1
            show mi normal pioneer far at center with dissolve
            window show
            "Мику увлеченно играла на пианино, не глядя на входную дверь. Я без труда узнал песню группы Modern Talking." 
            th "Оу, дискотека восьмидесятых!"
            th "Хотя блин, а какой же ещё быть в ретрофутуристичном СССР?"
            show mi normal pioneer close at center with dissolve
            "Во мне снова взыграло детство. Я прокрался за спину девочки и дождался того момента, когда Мику начнёт припев, и зарычал гроулом."
            me "You're my heart! You're my soul!!!"
            show mi shocked pioneer close at center with dspr
            "Мику, бросив играть, выдала секунд десять визга, близкого к ультразвуку, который, я уверен, был слышен в космосе."
            show mi angry pioneer at center with dspr
            mi "СЕМЁ-ЁН!!! Ну ты зачем так меня пугаешь? Я думала, ко мне лезет инопланетное чудище!"
            th "Тем не менее, я же старался, тем более гроулом петь непросто!"
            me "А что, разве я плохо спел? Где-то в ноту не попал?"
            show mi dontlike pioneer at center with dspr
            mi "Этот рёв у тебя песней зовется? Необходимо срочно исправить твой вокал!"
            me "Но Мику, я же совсем неплохо пою! Вот слушай: «Сою-юз нер-р-рушиимый р-республик свабо-о-одных»..."
            show mi surprise pioneer at center with dspr
            mi "Это же ужас, Семён! Мой дедушка так храпит, как ты поёшь! Давай позанимаемся твоим вокалом! Если будет хорошо получаться, то сможешь выступить на концерте! Ты читал о прошлом концерте? Я слышала, там девчонки сделали такую песню, её весь лагерь потом пел! Я тоже..."
            "...Мику всё не смолкала. Алиса за окном отчаянно жестикулировала и что-то пыталась сообщить. Я смог прочесть по губам слова: «Уведи её!»."
            "Мой взгляд мельком остановился на гитарах в углу комнаты."
            th "А вот и они. Может, я смогу отвлечь девчонку."
            me "Мику, а спой что-нибудь? А я попытаюсь подпеть! Может, я не безнадёжен?"
            show mi smile pioneer at center with dspr
            mi "Только не рычи так страшно, хорошо?"
            me "Ну я постараюсь!"
            stop music fadeout 3
            "Мику сходила к полке с книжками и принесла мне песенник с текстами из советских кинофильмов и мультипликации."
            th "Что ж, попробую подвывать максимально мелодично."
            play music music_list["wonderful_future"] fadein 0
            show mi happy pioneer at center with dspr
            "Я уставился на открытую девочкой страницу песенника."
            th "О..."
            "И эта песня тоже была мне знакома — по кинофильму «Гостья из будущего»"
            mi "...Слышу голос из прекрасного далёка,\nГолос утренний в серебряной росе,"
            mi "Слышу голос, и манящая дорога\nКружит голову, как в детстве карусель..."
            "Неожиданно для себя я представил летящий сквозь время и пространство автобус, который увозит меня из уже такой далекой прошлой жизни.{w} Или будущей?{w} Когда я снова окажусь дома — всё вернётся на круги своя?" 
            "И я, пожалуй, впервые об этом задумался — а так ли мне хочется назад? Одно дело переждать пару недель, а другое — остаться здесь насовсем."
            mi "Прекрасное далёко! Не будь ко мне жестоко,\nНе будь ко мне жестоко, жестоко не будь!"
            mi "От чистого истока в прекрасное далёко,\nВ прекрасное далёко я начинаю путь..."
            "Мику пела настолько искренне и проникновенно, что я на время совершенно потерял чувство реальности и глубоко задумался. Уж очень точно песня передавала ощущения от всего со мной происходящего." 
            stop music fadeout 2
            "Сам я петь перестал ещё на «Слышу голос из пре...», совершенно не вытянув высокую ноту." 
            "Когда Мику допела, повисла некоторая пауза."
            me "Ну-у.. Если честно, Мику, я так никогда не спою."
            show mi normal pioneer at center with dspr
            mi "Может, тогда попробуем другую песню?"
            me "Давай."
            "Мику, не отбирая у меня песенника, перелистнула несколько страниц."
            show mi smile pioneer at center with dspr
            mi "Вот эту."
            play music music_list["song_about_bears"] fadein 1
            show mi happy pioneer at center with dspr
            "Девочка выпрямилась, вскинула одну руку, положив другую на грудь, и запела."
            mi "...Где-то на белом свете,\nТам, где всегда мороз,"
            mi "Трутся спиной медведи\nО земную о-ось..."
            play sound sfx_knock_door_closed_hard2
            "Сквозь голос Мику и свой недофальцет я услышал, как кто-то отбивает ритм ногой по двери."
            me "Мику, там кто-то стучится."
            show mi smile pioneer at center with dspr
            mi "Тебе кажется! Не сбивайся."
            play sound sfx_knock_door_closed_hard2
            show mi happy pioneer at center with dspr
            "Девочка продолжила самозабвенно петь, а Алиса — барабанить в такт по дверям."
            me "Нет-нет, Мику, пойдем посмотрим, кто там."
            stop ambience fadeout 1
            scene bg ext_musclub_day
            with dissolve
            show mi normal pioneer at center with dissolve
            "Мы вышли на крыльцо клуба и никого не обнаружили." 
            mi "Вот видишь, нет тут никого."
            me "Да я же слышал!"
            show mi grin pioneer at center with dspr
            mi "Лучше бы мы не отвлекались. Хочешь, я расскажу тебе про вокальные упражнения? Похоже, тебе надо начинать именно с этого..."
            "Я попытался отмахнуться, но Мику стала осыпать меня советами, что нужно делать и даже как правильно дышать."
            "Подождав с минуту, чтобы Двачевская уж точно успела вынести вожделённый ею музыкальный инструмент, я вернулся в комнату кружка, а со мной и Мику, точно привязанная."
            scene bg int_musclub_day
            with dissolve
            play ambience ambience_music_club_day fadein 1
            show mi normal pioneer at center with dissolve
            "Одной гитары не было."
            stop music fadeout 2
            th "Бинго!"
            play music music_list["lightness"] fadein 1
            th "Теперь можно расслабиться — Алиса получила, что хотела, а я свободен на все четыре стороны."
            me "Так что ты там говорила про борьбу с... э-э..."
            show mi scared pioneer at center with dspr
            mi "Ты даже не слушал меня! Про борьбу с постоянным занижением нот!"
            th "Ох, что же мне делать?"
            me "А повторить не затруднит?"
            show mi happy pioneer at center with dspr
            mi "Пожалуйста!"
            show mi grin pioneer at center with dspr
            "И Мику принялась объяснять мне премудрости вокальных тренировок."
            "Чему-то у неё стоило поучиться, несмотря на то, что Двачевская хорошо оценила мой недо-экспромт на сцене."
            window hide
            stop ambience fadeout 1
            stop music fadeout 1
            scene black
            with dissolve
            window show
            "......"
            $ proficiencies ['kn_music']+=1
            "........."
            window hide
            scene bg ext_musclub_day
            with dissolve
            play music music_list["my_daily_life"] fadein 1
            window show
            "Вскоре под надуманным предлогом я покинул клуб, на порядок раньше окончания занятий в кружках — как только Мику щедро поделилась основными рекомендациями по улучшению навыков пения."
            th "Интересно, Алиса уже терзает гитару?"
            "Раз я спел ей, то и она пусть исполнит что-нибудь мне."
            th "Если она умеет хорошо играть, то можно будет и подпеть. А если нет, потроллю немного, скажу, что быть форточницей-домушником у неё получается лучше."
            "..."
            window hide
            scene bg ext_stage_big_day
            with dissolve
            window show
            "Я вернулся к эстраде, сделав тот же самый крюк лесом за жилыми домиками."
            "Никого."
            me "Алиса, ты здесь?{w} Ау?.."
            "Никто не отозвался."
            "Поболтавшись у сцены, я убедился, что Двачевская не собиралась подшутить надо мной, её на самом деле тут не было."
            th "Может она ушла к себе?"
            "..."
            window hide
            scene bg ext_houses_day
            with fade
            window show
            "Я быстрым шагом поднялся на дорогу и двинулся через главную площадь к домику, где предположительно могла быть Алиса."
            "Как мне удалось выяснить заранее, Алиса и Ульяна жили вместе в одной из палат, располагавшихся на пятачке напротив прачечной, и по соседству с вожатой младшего отряда, явно присматривавшей за двумя самыми непослушными пионерками."
            scene bg ext_house_of_dv_day
            with dissolve
            "Опознавательным знаком домика был вывешенный пиратский флаг на одной половине двойных дверей. Другую половину закрывала большая картонка, а окно было наглухо зашторено."
            th "Предусмотрительно, фиг вожатые узнают, что происходит внутри, сунув нос к ним."
            th "Но это если дверь закрыта на шпингалет, когда кто-то в доме."
            play sound sfx_open_door_2
            "Я постучался и легко раскрыл дверь."
            "Комната пустовала — некому было запираться."
            th "Да что ж такое! Алиса как сквозь землю провалилась!"
            "Впрочем, я ещё не искал её по всему лагерю толком..."
            "..."
            scene bg ext_square_day
            with fade
            show mt smile pioneer far at center with dissolve
            "Задавшись этой целью, я обошёл несколько мест поблизости, пока не вернулся на площадь, где играла одна единственная компания пионерок-младшеотрядниц. Навстречу мне шла Ольга Дмитриевна."
            th "Вот блин!"
            "Остановившись на полпути, я резко развернулся на пятках, чтобы немедленно слинять отсюда."
            hide mt with dspr
            mt "Стой, Семён!"
            me "Стрелять будете?"
            show mt angry pioneer at center with dissolve
            "Вытянувшись стрункой, я заставил себя встретиться с вожатой лицом к лицу."
            mt "Только спрошу, почему ты не в кружке?"
            if mus_club:
                me "Я уже был там."
            me "Вообще-то я ищу Алису. Вы случайно не видели её?"
            show mt surprise pioneer at center with dspr
            mt "Нет, мне самой интересно, где она. Я вместе с Ингой Максимовной тоже прямо сейчас ищу её. Но в первую очередь надо найти Ульяну. А ты её видел?"
            me "Нет. Можно мне идти? А эти, мне кажется, вернутся сами, голод заест!"
            show mt grin pioneer at center with dspr
            "Ольга Дмитриевна усмехнулась."
            mt "Разумеется. Кстати, у нас ужин полвосьмого, так что приходи в столовую пораньше."
            me "Прийти в столовую пораньше? Всегда готов!"
            show mt laugh pioneer at center with dspr
            "Я отсалютовал."
            show mt smile pioneer at center with dspr
            "Не теряя времени, пока вожатая не надумала чем-то загрузить меня, я стремительно пошёл вперёд, всего раз оглянувшись на неё. Ольга Дмитриевна, улыбаясь, провожала меня взглядом."
            hide mt with dissolve
            th "Пронесло!"
            th "А ведь я правильно рассудил, можно подождать и выцепить Алису после ужина да спросить, где была."
            th "И правда, куда она могла подеваться?"
            window hide
            stop music fadeout 1
            $ d2_guitar_illegal = True
            $ d2_girls_event = (d2_girls_event) + (1)
            jump d2_pre_event
        "Проигнорировать желание Алисы":
            jump d2_green_theatre_ignore
        "Надо поговорить с Мику" if (mus_club == True) and (proficiencies ['sp_pers']>=2):
            th "Если вдуматься, то я не в лесу должен прохлаждаться, а быть на занятии музыкального кружка."
            th "А ведь я ещё могу успеть заскочить туда. Уговорить гостью из Японии всяко будет легче, чем Двачевскую."
            me "Ну, как знаешь, Алиса. Глупо из-за пустяка лишать себя возможности вдарить рок-н-роллом по всему лагерю."
            hide dv with dissolve
            scene bg ext_houses_day
            with dissolve
            "Не возвращаясь на дорогу к библиотеке, я побрёл к музыкальному клубу напрямик через домики."
            scene bg ext_musclub_day
            with dissolve
            "Я решил не утруждать себя вежливым стуком в дверь и просьбой войти — за раскрытым окном было видно, что Мику одна играет на рояле, и кроме неё в комнате больше никого нет. Остановившись у старой скамейки под окном, я позвал девочку."
            scene bg int_musclub_day
            with dissolve
            show mi normal pioneer at center with dissolve
            me "Мику!"
            show mi surprise pioneer at center with dspr
            mi "You're my...{w} Ой!{w} Привет, Семён!"
            show mi smile pioneer at center with dspr
            "Перестав играть, она вспорхнула с места ко мне и оперлась на подоконник, разделявший нас."
            me "Привет, хотя мы вообще-то уже виделись сегодня."
            show mi happy pioneer at center with dspr
            mi "Ну и что! А ты пришёл на занятие?"
            th "С какой надеждой в голосе она спросила!"
            me "Нет, я не за этим..."
            show mi sad pioneer at center with dspr
            mi "Очень жаль! Сегодня со всеми прямо беда какая-то! Репетировали морские мелодии, прибежал Токарев, просил научить его блатным аккордам, а я не знаю, что значит «блатные», занятие сорвано, все разбежались. Сижу теперь, понимаю себе настроение хитами восьмидесятых. Знаешь, что такое блатные аккорды?"
            "Я постарался объяснить Мику суть в двух предложениях. К счастью, или я говорил доходчиво, или она оказалась понятливой, так что вопрос мы решили быстро."
            show mi smile pioneer at center with dspr
            me "Но я пришёл сюда по другому делу."
            me "Скажи мне, а Алиса, которая Двачевская, случайно не хотела поступить в музыкальный кружок?"
            show mi normal pioneer at center with dspr
            mi "Нет, вроде, она никогда не приходила. Не знаю, почему, может быть, не хочет. Но когда у нас всем отрядом в начале смены был обход кружков, она вызывалась быть старостой кружка, как и я, но вожатые назначили меня: я им сказала, что с детства музыкой занимаюсь."
            me "!.."
            th "Двачевская — старостой? Не слишком ли ответственный пост для рыжей раздолбайки?"
            "Но я, кажется, догадался, что к чему."
            me "Мику, а староста вашего кружка должен сдавать нормативы?"
            show mi happy pioneer at center with dspr
            mi "Ну, меня ни разу не просили об этом."
            th "Всё ясно. Алиса намеревалась осуществить хитрый план — сократить себе обязанности, а других участников гонять на правах старосты."
            me "Если Двачевская вызывалась — это как раз и значит, что она хочет быть в кружке!"
            show mi scared pioneer at center with dspr
            me "Я недавно болтал с ней, она, не побоюсь сказать, прямо мечтает выступить на концерте, только у неё нет гитары, чтобы подготовиться."
            mi "Не понимаю! Что ей мешает приходить в музклуб и заниматься хоть до вечера?"
            me "Ну, во-первых, она в другом кружке, но по-моему, это не очень серьёзная проблема...{w} Алиса не хочет выполнять плановые задания от музыкального кружка... Это вожатые их требуют?"
            show mi grin pioneer at center with dspr
            mi "Да, чтобы нам не скучно было: баллы для отрядов и всё такое! Мне нравится их идея! Натуральное соревнование между отрядами, и в конце смены должно быть весело, когда будем выступать!"
            me "Ха, в том и дело, что для Алисы это скучно и детский сад. Она рок-н-ролл играть хочет, а нормативы сдавать — ни-ни.{w} Слушай, ты могла бы пригласить её в кружок."
            me "Я думаю, Алиса станет приходить, если вожатые переведут её к вам, а ты пообещаешь ей не требовать сдать «Кузнечика» или что-то такое."
            show mi scared pioneer at center with dspr
            mi "Тебе не кажется неправильным, что все сдавали, а она не будет?"
            show mi scared pioneer close at center with dspr
            "Я пожал плечами и наклонился к Мику, чтобы тоже опереться на подоконник."
            me "Слушай, я просто пришёл намекнуть, как можно заполучить ещё одного участника в кружок, а не торговаться. Ты уж сама поговори с Алисой."
            show mi happy pioneer close at center with dspr
            mi "Ладно, я попробую... В конце концов, хочется устроить настоящее представление!"
            "Я собрался уходить, отступив от подоконника."
            show mi scared pioneer at center with dspr
            mi "Подожди-подожди, Семён! А ведь ты тоже записан к нам, так что и тебе надо выучить и сдать несколько песенок на гитаре." 
            show mi grin pioneer at center with dspr
            mi "Заходи, пока кружок открыт!"
            me "Только не сегодня... Иначе я бы пришёл сразу после полдника."
            show mi shocked pioneer at center with dspr
            mi "Да ты ничуть не лучше Алисы!" 
            show mi laugh pioneer at center with dspr
            mi "Так, давай, заходи, буду учить! Делай, что велит староста!"
            me "Не-не-не!"
            show mi scared pioneer far at center with dspr
            "Не сдерживая улыбки, я развернулся и спешно ушёл от музклуба, слыша выкрики Мику в спину."
            hide mi with dissolve
            mi "Семё-ё-ён! Вернись!"
            "..."
            scene bg ext_house_of_mt_day
            with fade
            "Но теперь я уже был далеко от здания кружка, но рядом со своим домиком."
            th "Надеюсь, она простит меня."
            th "Каникулы же!"
            "Для меня это слово не было пустым звуком."
            th "Двадцатипятилетним тоже надо прерываться на отдых!"
            scene bg int_house_of_mt_day
            with dissolve
            "В палате царила тишина, Ольга Дмитриевна, очевидно, куда-то ушла."
            th "Не попасться бы ей на глаза!"
            "Желание прогуляться не оставило меня. На примете была ещё пара мест, кроме «Зелёного театра»."
            window hide
            stop music fadeout 1
            $ d2_dv_help = True
            $ d2_girls_event = (d2_girls_event) + (1)
            $ lp_dv = lp_dv + 1
            $ lp_mi = lp_mi + 1
            $ d2_day_places += 1
            jump d2_day_map

label d2_green_theatre_ignore:

    "А может я и правда чего-то не понимаю. Ну не хочет Алиса иметь дел с Мику, зачем тогда мне вмешиваться?"
    me "Ладно, пойду я..."
    "Двачевская смерила меня нерадостным взглядом."
    dv "Ага, иди, пока я разрешаю."
    "Слова прозвучали отталкивающе, и я спешно ретировался от сцены, посчитав за удачу хоть какое-то окончание разговора с Алисой, после которого ничего не болит."
    "Делать было нечего, и я остался верен себе — взялся прогуливать занятия в кружках сразу на второй день после прибытия."
    th "И нисколько не совестно, ведь я не пионер."
    "Но для вожатых я всё ещё был им, поэтому убивать время стоило где-нибудь подальше от их глаз."
    window hide
    stop music fadeout 1
    $ d2_day_places += 1
    jump d2_day_map

label d2_beach_day:
    
    scene bg oldmap
    window show
    if (d2_chess_agreement == False):
        th "Сейчас на речке наверняка никого из пионеров нет. Сходить проверить что ли?"
    "..."
    window hide
    $ reset_chibi("beach")
    $ disable_current_zone()
    scene bg ext_beach_day 
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    window show
    "Держа руки в карманах, я остановился на обочине рядом с душевыми."
    "На пляже было немного ветрено — это я понял сразу, даже не спускаясь на песчаный берег."
    show ug normal at center with dissolve
    "Отсюда я увидел, что тут по меньшей мере есть один человек.{w} Угрюмый пионер читал книгу, сидя под большим деревом на самом краю залива, омываемом синими волнами."
    "..."
    if d2_chess_decision:
        "Я вспомнил о нашем разговоре во время тихого часа."
        "И что меня дёрнуло записаться в кружок настольных игр, если даже обычные шахматы мне не интересны? А как участник я должен сыграть на турнире."
        "Угрюмый предложил помощь, а я засомневался, надо ли мне это."
        "И вот — он сейчас здесь, на пляже, и я всё ещё мог передумать насчёт шахмат."
        window hide
        menu:
            "Я уже принял решение отказаться":
                pass
            "Спуститься к пионеру":
                $ d2_chess_agreement = True

    if d2_chess_agreement:
        stop music fadeout 1
        scene black
        with dissolve
        show screen central_text("День 2 — Привилегия людей")
        $ renpy.pause(99, hard=False)
        hide screen central_text
        scene bg ext_beach_day 
        with dissolve
        play music music_list["so_good_to_be_careless"] fadein 1
        play ambience ambience_lake_shore_day fadein 1
        show ug normal at center with dissolve
        window show
        "Я обошёл песчаную насыпь пляжа и направился к Угрюмому по травянистой дорожке."
        "Заметивший меня пионер на мгновение поднял глаза от страниц книги и снова углубился в чтение."
        "С осторожностью я пригнулся под низкими ветвями и навис над Угрюмым, небрежно прислонившись к стволу дерева."
        me "Что читаешь?"
        ug "«Подполье» Фёдора Михайловича."
        me "А, читал это, правда очень давно, и не помню всех мелочей."
        "Подобной фразой я намеревался исключить возможное обсуждение и проверки, насколько правильно я усвоил содержание, но Угрюмый всё понял."
        ug "Плохо.{w} Дьявол в деталях. Упускать из прочитанного важную мелочь — всё равно что не читать вовсе."
        "Мне подумалось, что своим увлечением Угрюмый похож на Лену. Как говорят школьники на уроках английского: «Моё хобби есть чтение книг»."
        me "Любишь литературу?"
        ug "Да. Нашу классику девятнадцатого и двадцатого века. Чехова, Достоевского... На лето задали роман «О преступлении и наказании», я его уже прочёл, но эта повесть мне нравится больше."
        "Он постучал указательным пальцем по раскрытой странице книги."
        ug "И ещё что-нибудь потяжелей. Платонова, Короленко."
        #Под катом вариант этой реплики: "И ещё что-нибудь потяжелей, где умирают дети. Платонова, Короленко."
        ug "А ты что читаешь?"
        me "В основном, зарубежное... Контркультуру всякую и классику."
        ug "Например?"
        "Я мог бы перечислить всё, что читал, но обошёлся тем, что первым пришло на ум."
        me "Буковски, Паланик. Из классики — Мопассан, Бальзак... Марк Твен."
        ug "Твена я читал. Хороший писатель, толковый..."
        me "..."
        ug "Вижу, ты не слишком хочешь говорить об этом."
        ug "Ладно, я же обещал научить тебя шахматам. Сыграем?"
        me "Да, я только за, но разве не нужно сходить за доской?"
        "Я уж было собрался уйти с пляжа для этого."
        ug "Не надо, у меня с собой."
        "Он вынул из кармана миниатюрную металлическую доску."
        me "А, магнитные шахматы.{w} Я должен был догадаться!"
        ug "Именно. Присаживайся."
        "Я сполз по стволу дерева, занимая место рядом с полосой тени, куда Угрюмый, примяв траву, положил доску."
        if (chess_club == False):
            ug "Что ж, ты не записался к шахматистам, и это значительно упрощает дело."
            me "Почему?"
            ug "У них через два дня турнир, обязательный для участников кружка. Нет повода торопиться с обучением, просто воспринимай игру как отдых."
            me "С удовольствием."
            th "Особенно если этим можно занять время, которого у меня появилось выше крыши."
        ug "Я буду играть чёрными, так что расставляй свою кавалерию и ходи первым."
        me "Хорошо!"
        "Фигуры с магнитиками в основании со звучным щелчком прилипали к своим квадратам на маленьком поле. Я, точно спеша опередить Угрюмого, быстро достроил ряд пешек на своей половине."
        ug "Как видишь, я не взял часы с флажками — на первых порах играть в быстрые шахматы, а уж тем более — в блиц, ни к чему, и у тебя есть время на обдумывание ходов."
        "Мне вспомнилась волшебная кнопка «Undo» в шахматных программах."
        me "А можно будет отменить ход, если я не так пойду?"
        "Я осёкся, решив, что прошу слишком много поблажек для себя, но Угрюмый согласился."
        ug "Да, пожалуй, можно. Отменяй любой ход, заодно посмотришь, на чём чаще всего можно ошибиться, если не думать."
        ug "Как в бородатом анекдоте: «Доктор! Я сломал ногу в двух местах! — Вы запомнили эти места? Больше туда не ходите!»."
        "Я усмехнулся шутке — мрачно и не о шахматах, но получилось в тему. А Угрюмый лишь скривил губы, словно испытал глубочайшее отвращение к чему-то."
        "Этим пионер напомнил мне героя из повести о Незнайке — Пёстренького, который взял за правило в жизни ничему не удивляться. Так и Угрюмый, видимо, решил никогда не проявлять положительных эмоций, вроде радости, улыбки или смеха."
        stop music fadeout 2
        "Убийственно серьёзный и... угрюмый. Два слова, которыми пока что можно было выразить о нём всё."
        play music music_list["everyday_theme"] fadein 1
        "Мы начали игру. Я двинул королевскую пешку на два поля вперёд. Чёрные ответили тем же — Угрюмый не стал делать совсем уж нетрадиционный ход в моём понимании."
        "Постепенно наши фигуры заняли середину поля. Я просил отменять ходы, которые лишали меня весового преимущества или же были просто необдуманными, но соглашался на размен, когда он был очевиден и освобождал пространство для манёвров."
        "Угрюмый играл спокойно, предоставляя мне инициативу, и в то же время сохранял недосягаемость — я минутами ломал голову, как подступиться к его защите и ослабить короля."
        "Пионер не комментировал наши действия, не ругал меня, он последовательно записывал сделанные ходы в блокнот и молчал, из-за чего напряжение только возрастало."
        "Я настолько увлёкся, что позабыл обо всём: и об отдыхе, и о чудесной погоде, и о пребывании в пионерском лагере другого мира. Сейчас мои мысли занимало только желание обыграть Угрюмого."
        "Череда разменов, из которых особенно тяжело мне дались сокрушение ферзя чёрных и жертва своего, привела к тому, что в борьбу к оставшимся пешкам подключились короли."
        "Нам было ясно, что шансы на победу возрастут у того, кто проведёт свою пешку до конца поля и сделает ферзём. Но я всё ещё невозбранно пользовался правом отменить ход, когда терял шанс остановить вражескую пешку."
        "Всеми силами мы препятствовали друг другу, пока на поле не остались только две фигуры на расстоянии в три клетки."
        "Чёрный король и белый король."
        stop music fadeout 2
        me "Ничья."
        play music music_list["get_to_know_me_better"] fadein 1
        ug "По-моему, красиво получилось. Хорошая партия."
        "Он развернул ко мне пружинный блокнот с длинным протоколом игры на весь лист."
        me "Да, но мы играли несерьёзно, считай, понарошку. Я же отменял ходы, иначе партия закончилась бы намного раньше."
        ug "Это неважно."
        "Угрюмый отвернулся и скрестил ноги, полулёжа на траве."
        me "Пока я не буду сам просчитывать ходы наперёд, полноценной и честной партии не выйдет."
        ug "Думаешь, просто игра тебе поможет в этом?"
        me "Ну, разве шахматы не учат..."
        ug "Шахматы ничему не учат в принципе. Они только развивают до некоторого предела имеющиеся способности человека и навыки игры в рамках собственных правил.{w} Но это моё личное мнение."
        me "А как же терпение и усидчивость?"
        ug "Если бы. Я как-то играл целый месяц с одним очень невыдержанным типом, который страшно обижался на допущенные им и мною ошибки или просто скучал, из-за чего бросал партию на середине и возвращался к ней лишь через день или два. Сомневаюсь, что шахматы всё-таки исправят его характер. С возрастом пройдёт."
        "Он хотел сказать что-то ещё, но умолк."
        me "Ладно, а что насчёт принятия решений?"
        ug "Часть мышления. Мы делаем это всю жизнь, умеем без всякой игры. Взвешивание за и против, поиск альтернатив — методы. Ну а шахматы лишены морали и глубины ситуации."
        ug "Например, давить оппонента любыми способами, как на доске — это хорошо или плохо?"
        me "Кстати, я хотел спросить про мышление.{w} Но ты, наверно, скажешь, что шахматы не учат логике, а развивают её?"
        ug "Да. Разве что маленьких детей, и то, я считаю, что это заслуга родителей или тренеров, которые знакомят их с правилами игры. Шахматы — средство обращения к индивидуальным навыкам, они стимулируют их проявление на практике. А учить — это привилегия людей."
        ug "Хочешь освоить все типы логики — купи учебник по логике, займись математикой и другими точными науками, а не шахматами."
        me "В чём тогда смысл?.."
        "Угрюмый поднялся круче, оказавшись вровень с моим взглядом."
        ug "Смысл? Смысл в том, чтобы уничтожить соперника."
        "Угрюмый сжал левую руку в кулак."
        ug "На турнирах даже проще и тупее — захватить шестьдесят процентов доски или добиться той же цифры в фигурном перевесе. Из прагматических соображений."
        me "Знаешь, я сначала думал, что ты любишь шахматы, но теперь мне уже так не кажется. Разнёс в пух и прах."
        ug "Я пытаюсь быть объективным, хотя со мной можно и поспорить. Позитивное представление о шахматах возникло благодаря философским рассуждениям людей с хорошо подвешенным языком."
        ug "Но кто сказал, что к этому не надо стремиться? Без фанатизма, конечно."
        ug "Меня, например, интересует проблема творческого подхода..."
        ug "Однако слова, что жизнь подобна шахматам, и, наоборот, шахматы похожи на жизнь, не совсем верны и могут ввести новичка в заблуждение."
        ug "Шахматы не абсолютны и не универсальны. Да, по заданным правилам реально смоделировать некоторые жизненные ситуации, но невозможно всё разнообразие жизни натянуть на эту модель."
        ug "Я просто хочу, чтобы ты не переоценивал шахматы. Это всего лишь игра, но с богатой, шикарной историей."
        ug "К тому же, игра по большему счёту нерешённая. Число уникальных партий в ней примерно равняется десяти в сто двадцатой степени. Понимаешь, что это значит?"
        ug "Чтобы сыграть все существующие варианты игры, нам понадобятся тысячи лет.{w} Если б только можно было жить вечно..."
        "..."
        ug "Мне нравятся шахматы, но кроме них есть и другие игры."
        ug "Я люблю игры вообще. Игра как явление — лучшее открытие человечества."
        "Он закрыл глаза."
        "С лица пионера исчезло напряжение, казавшееся мне хмурой серьёзностью, его черты стали мягче, как у безмятежно спящего человека."
        "Угрюмый говорил искренне, и я поверил ему."
        me "Но я тогда не понимаю, почему тебе так не нравится в кружке, если не считать того, что ты обыграл всех?"
        ug "Я устал от кружков."
        ug "На протяжении шести лет я каждую неделю посещал пять разных коллективов и внешкольных клубов одновременно. Брался за всё подряд: что интересовало, туда продолжал ходить после уроков, в том числе и на занятия по развивающим шахматам для детей, пока не перешёл в спортивную секцию во Дворце пионеров..."
        "Хоть я и был далёк от всего этого, я сразу понял, что Угрюмый имел в виду те монументальные серые здания с типично советским архитектурным дизайном (или похожие на театры, если до революции принадлежали аристократии), к которым от автобусных остановок вели длинные аллеи, мощёные плитами."
        "В моём мире после распада СССР они стали называться Домами детского и юношеского творчества. Мне пару раз доводилось видеть их из окон общественного транспорта."
        ug "...По времени я дольше всего занимался именно шахматами — вот тебе ещё одно доказательство моей любви к ним."
        me "Что за спортивния секция, в которую ты перевёлся?"
        ug "Тоже по шахматам, разница с обучающей группой в том, что в спортивном кружке готовят разрядников."
        me "Понятно. И какой у тебя разряд?"
        ug "Официально, по билету, второй. Не совсем официально: мой рейтинг — две тысячи четыреста тридцать пять. То есть, я международный мастер по шахматам."
        th "Ого. Неужели не врёт?"
        me "Как так вышло?"
        ug "Ещё с двумя пионерами я должен был ехать на первенство по стране от нашего района, даже была составлена и подписана заявка от тренеров из секции, но я вспомнил все предыдущие соревнования и то, что мне стало известно о международных турнирах за титул..."
        ug "...И раздумал. Я выключил телефон, не явился к месту сбора у Дворца пионеров. К тому же, на улице начался сильный дождь."
        ug "Представляешь, как они там все взбесились?"
        "Гримаса отвращения снова заменила Угрюмому смех."
        ug "Если я когда-то надумаю вернуться на соревнования, сначала я должен буду защитить свой разряд."
        ug "Но зачем, когда я спокойно играю в на Интернет-порталах с привязкой к рейтингу Международной Шахматной Федерации или просто так, без неё?"
        me "Зарабатывать победами, например."
        ug "Не... Есть сетевые коммерческие турниры, но я в них тоже не участвую.{w} Вне Интернета я могу оказаться не таким уж сильным игроком по сравнению с профессионалами."
        me "..."
        ug "Так вот, мы начали спор о том, учат ли шахматы просчитыванию комбинаций."
        ug "Какое может быть просчитывание, если уже на третьем ходу возникает четыреста возможных позиций, а на четвёртом — в двадцать с лишним раз больше? Тут до тебя уже немного просчитали — дебюты называется."
        ug "Шахматы — игра скорее позиционная, чем на счёт. В середине партии анализируется текущая ситуация и выбирается лучший из имеющихся вариантов хода, а от соперника ждут ошибок."
        ug "Сначала все эти защиты-дебюты, потом борьба за центр, а в эндшпиле принуждение к форсированному мату или ничьей."
        ug "На твоём уровне игры бессмысленно просчитывать в миттельшпиле — это комбинаторика. Комбинационное зрение поможет развить быстрее не игра сама по себе, а шахматные этюды-задачи и разбор вот этих бумажек."
        "Угрюмый потряс блокнотом."
        ug "Анализ партий известных шахматистов — тоже здорово. И практика, без неё никуда."
        "Угрюмый заново расставил все фигуры и стал повторять игру по записи."
        ug "Как бы там ни было, большинство играющих зубрит дебюты, а профессионалы их просто обязаны знать и владеют своим набором, поэтому я расскажу тебе о началах совсем коротко."
        ug "Про точные разновидности дебютов почитаешь сам, а в общем начала бывают правильными и неправильными. Семь верных и тринадцать неверных ходов."
        ug "На турнирах так ходить не рискуют: возможна потеря преимущества из-за слабых полей или времени перед тем как сложится позиция из правильных начал. Это скорее для экспериментов в шахматах по переписке."
        "Он дал мне блокнот с ручкой, а сам продолжал развивать нашу партию по вырванным листкам."
        ug "Пиши неправильные: a3, a4, b4, c3, d3, e3, f3, g4, h3, h4, Кa3, Кc3, Кh3. Я не возражаю, чтобы ты попробовал ошибочные варианты даже под угрозой быстрого проигрыша. Так ходят или полные новички, или провокаторы, которые разбираются в дебютах."
        ug "Иногда за чёрных можно реагировать так и строить защиту на своё усмотрение, не забывая о действиях белых."
        ug "О таких началах нечасто распространяются в книгах, поэтому есть немаленькая вероятность, что играющий с тобой на том же уровне будет просто незнаком с ними."
        ug "Здесь, в лагерном кружке, только один пионер был в курсе, но всё же он отдавал предпочтение устоявшимся решениям, а на меня он посмотрел как на чокнутого, когда я сходил так."
        "Угрюмый привёл нашу партию в нужный вид, когда за бортом доски уже скопилось приличное количество фигур."
        ug "Со мной ты будешь учиться на ошибках и с конца, начнём с эндшпилей."
        me "Почему не с дебютов?"
        ug "Нет формальной точки, с которой можно начать освоение шахмат. Бери любую книгу в библиотеке, читай от и до, запоминай полезное. Есть ещё разные шахматные школы — откуда я знаю, чьи положения и методы тебе придутся по вкусу? Потом, всё имеет свойство устаревать."
        me "А ты к кому себя относишь?"
        ug "Ни к кому. Я — это я.{w} По личным взглядам на шахматы мне ближе всего гипермодернисты, но в игре приходится быть универсальным и менять тактику."
        "Он привлёк моё внимание к доске."
        ug "Смотри на позицию. Мы слишком увлеклись поеданием фигур друг друга, и между тем ты пропустил возможность сыграть ещё красивее и поставить мне мат в несколько ходов, а такой шанс действительно был."
        ug "Ну, сможешь отыскать более выгодный ход вместо устранения моего слона?"
        "Я тупо уставился на доску, пытаясь решить поставленную пионером задачу."
        th "Он говорил не бояться разменов, что я и сделал, но разве это был не лучший ход? Куда девать коня?"
        th "Если сдвину его, то потеряю контроль над полем g5."
        "Там был вражеский слон и простреливал диагональ до клетки, куда могла бы прийти моя пешка."
        "Ко мне пришло озарение, что сходить надо было именно ею — я бы успел провести её в ферзи."
        th "А если мне преградят путь?{w} Тогда подтянем коня."
        "Я сделал ход пешкой, и Угрюмый с согласием кивнул."
        ug "Мой король находится не в самом удобном положении. Я бы постарался нарушить твои планы, однако всё решит вилка — конь снова будет угрожать слону и одновременно сделает шах."
        ug "Самое интересное, что даже избежав вилки, я останусь в проигрыше по количеству фигур, и при умелом владении конём ты получишь долгожданного ферзя."
        ug "Дальше дело техники."
        ug "Но стоило бы тебе допустить хоть одну ошибку, и я бы тоже немедленно вернул себе ферзя, и игра превратилась бы в перетягивание каната..."
        ug "Так что для тебя ничья — это очень неплохо. Спасибо за игру!"
        me "И тебе."
        play sound sfx_dinner_jingle_speaker
        "Вдалеке послышалась мелодия горна — кончились занятия в кружках, пионеры приглашались на ужин. На дороге показалась ватага детей, возвращавшихся с футбольного поля."
        "Мы поднялись, когда все фигуры были свалены внутрь доски. Я отдал её Угрюмому."
        ug "Семён, мне вот чего хотелось бы: выучи шахматную нотацию, и тогда мы будем говорить на одном языке..."
        "Я ещё раз прокрутил в голове впечатления от сыгранной партии."
        me "Обязательно."
        window hide
        scene black
        with dissolve
        window show
        "........."
        window hide
        stop ambience fadeout 1
        stop music fadeout 2
        $ d2_ug_game = True
        $ fp_ug = fp_ug + 1
        jump d2_pre_event

    else:
        th "Нет, двум тиграм не ужиться на одной горе."
        th "То есть, на одном пляже."
        "Раз он занят, мне стоило поискать такое место, где меня никто не потревожит, и где я никого не отвлеку своим присутствием, только если мне того не захочется."
        window hide
        stop music fadeout 1
        $ d2_day_places += 1
        jump d2_day_map

label d2_boat_station_day:

    $ reset_chibi("boat_station")
    scene bg ext_boathouse_day 
    with dissolve
    play ambience ambience_boat_station_day fadein 2
    window show
    "Солнце палило уже не так сильно, как в полдень."
    "Не имея ни малейшего плана в голове, чем заняться, я спустился с дороги к плавучему дому."
    th "Отлично, там меня не найдут вездесущие вожатые, и в тени под плеск волн можно будет обдумать дальнейшие действия."
    "Лодки тихо покачивались на воде рядом с понтонами."
    "Дебаркадер казался необитаемым, но я всё равно старался как можно тише наступать на дощатый настил мостика. Я прошёл в самую затенённую часть этой плавучей конструкции, чтобы укрыться от солнца." 
    "Здесь обзору не мешали островки, и вдалеке виднелись очертания города. Хорошо знать, что где-то рядом всё-таки есть цивилизация."
    "Попытки добраться туда раньше, чем закончится смена, не имели смысла, так что я был вынужден запастись терпением."
    "А справа на берегу можно было кое-как разглядеть бревенчатый домик, построенный у самых деревьев на узкой опушке."
    th "Наверно, это и есть пресловутая баня."
    "Я мысленно установил себе напоминание: сходить туда, как выдастся возможность."
    ld_voice "Хорощий нынче денёк, а?"
    "Вздрогнув, я обернулся с лёгким испугом."
    #show ld
    "Хрипловатый голос принадлежал загорелому старику, который вчера прогнал нас с Электроником. Лодочник только что вышел из-за угла дебаркадера, пребывая в хорошем расположении духа."
    me "Извините, не узнал вас. Здрасте."
    "Старик будто бы с укором покачал головой, не дождавшись от меня ответа насчёт погоды."
    "Только сейчас я смог рассмотреть его как следует. Лодочник был одет в стёганый ватный жилет поверх тоненькой водолазки. На голове он носил шлем-панаму, вроде той, какие надевают туристы-исследователи джунглей и пустынь в кино."
    "От лодочника несло какой-то дикой смесью курева и химии, видимо, краски."
    "Глаза морщинистого старика были пронзительно синими, даже белки скрывала голубоватая дымка.{w} Оставалось только гадать, из-за чего они выглядели так."
    "В некотором смысле, глаза даже молодили его."
    "Вдруг лодочник указал на меня дрожащим пальцем."
    ld "Шойта я шовшем не могу припомнить тебя."
    "Говорил он плохо — беспрестанно покашливал, хрипел и шепелявил. Всё ещё усугублялось тем, что он не желал расставаться с почти докуренной папиросой, зажатой в зубах."
    th "Не буду напоминать ему, что это я с Сыроежкиным нарушил его спокойствие накануне, разозлится ещё."
    me "Я только вчера приехал, потому что опоздал."
    ld "А-а, то-то я не видел тебя ш пионерами на пляше. Гхм!"
    me "..."
    ld "Ну што, какими шудьбами к нам? За какие зашлуги?"
    "Я сощурился."
    th "Выясняет, как я путёвку получил, наверно. И как ему ответить?.. Уснул в автобусе, очнулся, пионер?"
    me "Да вот я сам не понимаю! Случайно."
    th "Проблема была в том, что я обычно не признавал случайностей, но в этой ситуации всё было настолько неясно, что я не выразил ответ по-другому. Может, сесть в автобус мог любой человек, если бы находился на остановке вместо меня."
    ld "Што, прям таки шлущайно? Во дела!"
    "Он тихонько засмеялся, стряхивая пепел с папиросы над водой."
    ld "Ну, бывай, пионер."
    "Снова сжав зубами самокрутку из газеты «Труд», лодочник скрылся за углом."
    #hide ld
    th "Чёрт... Неужели он всё понял и пошёл вызывать наряд милиции за мной? Или санитаров? Или всех вместе?"
    "Повинуясь разыгравшейся паранойе, я тайком последовал за ним."
    "На серёдке пристани старичок зашёл внутрь дебаркадера — через проём, который до этого был закрыт сдвижными деревянными воротами."
    th "Что же там находится?"
    "Я осторожно прошёл вперёд и заглянул в слабо освещённое помещение под крышей."
    #show ld
    "Конечно, не то чтобы я надеялся увидеть открытый портал в будущее или толпу зергов — но здесь я не обнаружил ничего необычного. Лишь спасательные круги, гору пробковых жилетов и всякое малоинтересное барахло на стенах — багры да рыболовные сетки."
    "У самого входа на полозьях с опорами покоились две свежепокрашенные лодки."
    "Лодочник сел у одной посудины на низенький табурет, вооружившись кистью с трафаретом, и собрался начать рисовать, как заметил меня."
    ld "Хотел што, пионер?"
    "Я быстро сочинил отмазку."
    me "Нет... Просто не мог понять, чем так едко пахнет."
    ld "А-а, нитроэмаль это."
    "Старик взял трафарет поудобней и стал наносить белой краской надпись. На соседней лодке уже было написано: «П/л Совёнок»."
    th "Да, навоображал я себе невесть чего."
    "Оценив часть сделанной надписи, лодочник брякнул кисть обратно в ведёрко на газете."
    ld "Рыбалку любишь, пионер?"
    me "А? Не сказать, что люблю. Я рыбачил-то всего два раза в жизни."
    ld "Ай-яй-яй, как ше так?{w} Хотя шего это я, вы, молодёшь, нетерпеливая, на рыбалке шебя ушидеть не заштавите... Как тебя звать, пионер?"
    me "Семён."
    "Он закивал головой."
    ld "Шемён, знащит."
    "Я поморщился, услышав, как лодочник исказил моё имя."
    ld "Ешли надумаешь порыбачить, Шемён, заходи, у меня и удочки, и вше шнашти ешть."
    "А вот этого я совсем не ожидал."
    me "Э-э... Спасибо за предложение."
    "Едва ли я мог представить себя на рыбалке, да ещё в компании этого странного дедка с трудным произношением и витающим вокруг него дурным ароматом самокрутки."
    "Лодочник, насвистывая под нос, вернулся к работе: помочил кисть в краске, обтёр по краю ведёрка и давай снова малевать по трафарету."
    th "Ну, не буду мешать ему. И запах тут с ума сводит."
    #hide ld
    "Я ушёл с лодочной станции, если не сказать уполз живым, радуясь чистому воздуху."
    th "Куда теперь?"
    window hide
    stop ambience fadeout 1
    $ d2_met_ld = True
    $ d2_day_places += 1
    $ disable_current_zone()
    jump d2_day_map

label d2_square_day:

    scene bg ext_square_day
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    play ambience ambience_camp_center_day fadein 1
    window show
    "Идти в кружок особо не хотелось. С большим удовольствием я бы подремал на свежем воздухе."
    "Я присел на лавочку в тени возле умывальника."
    th "Правда ли, что по требованию вожатых пионеры обязательно должны заниматься скучными делами в четырёх стенах, а не гулять?"
    "Впрочем, небольшая группа девчонок из младшего отряда опровергала мои размышления. Около памятника девочки, смеясь, играли в классики — расчерчивали по асфальту мелом квадраты с цифрами, а затем прыжками преодолевали рисунок от начала до конца."
    "Им никто не докучал. Сплошная идиллия до зубовного скрежета."
    th "Или у меня просто не самый везучий день."
    "Вдалеке, у крыльца административного здания показались две девушки, о чём-то говорившие. Вожатые Ольга Дмитриевна и Инга Максимовна решительным шагом направлялись по дорожке к главной улице." 
    th "Не ко мне, но к чему рисковать? Расселся тут, как барин."
    "Я поспешно встал с лавочки и пошёл куда глаза глядят."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ d2_day_places += 1
    $ disable_current_zone()
    jump d2_day_map

label d2_aidpost_day:

    scene bg ext_aidpost_day
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    window show
    "Идея посетить медпункт пришла в голову сама собой. Не иначе как солнцем напекло... Или же я просто захотел снова увидеть медсестру Виолу."
    "Я заполнил весь обходной лист, а значит, имею полное право!"
    "Но вот что я ей скажу, когда появлюсь на пороге медпункта?"
    th "Меня хватил солнечный удар, остудите же мой пыл прикосновением своих рук!"
    th "Нет, не так..."
    "Я фантазировал, а ноги уже несли меня к заветному дому с флагом красного креста."
    play sound sfx_knock_door2
    "Не подумав заглянуть в окна, я взлетел на крыльцо, постучался и нетерпеливо приоткрыл дверь."
    scene bg int_aidpost_day
    with dissolve
    play ambience ambience_medstation_inside_day fadein 2
    me "Можно войти?"
    "Но вместо Виолы на стуле сидел какой-то пионер из младшего отряда."
    boy "М? Да, можно."
    me "А где медсестра?"
    boy "Ушла куда-то, попросила побыть тут. Я сегодня на дежурстве."
    me "А-а, понятно."
    "Я с разочарованием закрыл дверь."
    scene bg ext_aidpost_day
    with dissolve
    "Да, вот так случаются обломы."
    if d1_genda_flag:
        "А ведь Сыроежкин что-то говорил такое, будто медсестра иногда уходит с поста."
    th "Значит, не судьба. Попытаем удачу где-нибудь ещё."
    window hide
    stop music fadeout 1
    $ d2_day_places += 1
    $ disable_current_zone()
    jump d2_day_map

label d2_forest_day:

    scene bg ext_path2_day
    with dissolve
    play ambience ambience_forest_day fadein 1
    window show
    "Ещё при обходе кружков за подписями я заметил, как близко находится лес. Он был в черте лагеря, не отделённый забором от жилой территории."
    "Манящее, притягательное место для любого пионера, желающего спрятаться от вожатых. А в моём случае — ото всех, чтобы побыть наедине с собой и мыслями."
    "К тому же, я сюда ещё не ходил."
    "..."
    scene bg ext_path_day
    with dissolve
    play music music_list["just_think"] fadein 1
    "Никуда не сворачивая с тропы, я всё дальше и дальше уходил в чащу леса."
    "Тут было довольно тихо, изредка слышался щебет птиц. В воздухе стоял чудный запах травы и хвои."
    th "Знал бы, взял бы с собой покрывало, чтобы разлечься и подремать на опушке возле деревьев! Или почитать книгу, раз нет компьютера с интернетами."
    scene bg ext_path_day
    with dissolve
    "Немного погодя тропа под ногами стала менее отчётливой, точно я попал на малохоженный, непротоптанный никем путь, но это не остановило меня — в лесу было приятно находиться."
    "Пять минут неспешной ходьбы не приблизили меня к цели. Я до сих пор не отыскал забора, который обозначил бы пределы лагеря. Лес оказался больше, чем я ожидал."
    "Даже при свете дня понемногу мне стало страшновато в настолько безлюдном месте."
    th "Кажется, к показной социофобии у меня прибавится боязнь открытых пространств — и вполне настоящая."
    th "Или как там точно называется страх пребывания в лесу?.."
    "Мои минутные размышления превратились в метания — не потерялся ли я? Не медля, я с беспокойством двинулся назад."
    stop music fadeout 2
    "..."
    play music music_list["my_daily_life"] fadein 1
    "На моё счастье, где-то совсем рядом послышались девичий голос и смех."
    "Я медленно пошёл на звук, решив никого не звать и не привлекать к себе внимания."
    th "А вдруг, как в историях с эротическим уклоном, я увижу небольшой водопад с тихой заводью, где купаются голые нимфы?"
    "Увы, здравый смысл и трезвая память подсказывали, что я в пионерлагере, а не в диких тропиках.{w} И эротический сюжет вряд ли светил мне в ближайшее время."
    scene bg ext_polyana_day
    with dissolve
    show sl smile pioneer far at center with dissolve
    #show hai
    #show iie
    #show ci
    "Так и вышло. Притаившись за кустарниками, я увидел поляну, на которой отдыхали пионеры — и мальчики, и девочки из обоих отрядов. С ними была Славя."
    th "Что они тут забыли?"
    "Понаблюдав чуть-чуть за ними, я всё понял."
    th "Да это же юннаты."
    "И они вовсе не отдыхали, а были заняты делом, как и полагается в пионерских кружках."
    if unnat_club:
        th "А я как раз сейчас прогуливаю их занятие. И зачем я записался к юннатам?"
        "С другой стороны, с ними я мог бы совершенно легально расслабляться на свежем воздухе, не боясь встреч с вожатыми..."
    th "Но сегодня я уже не присоединюсь к пионерам. Быть одному тоже неплохо."
    "И лучше уйти отсюда, пока они не заметили мои нечёсаные лохмы за кустами и не записали в свои тетради как очередной вид: «Zatvornik vulgaris. Примерно 17-25 лет от роду. Характер скверный. Пуглив. Девственник, не женат.»"
    hide sl with dissolve
    #hide hai
    #hide iie
    #hide ci
    "Я отпустил ветвь куста, из-за которой подсматривал за детьми, поднялся и отправился искать ту самую тропу, ведущую в лагерь."
    th "Ох, если я каким-то макаром заблужусь в трёх соснах, придётся возвращаться к юннатам."
    "..."
    scene bg ext_path_day
    with dissolve
    "Но я не потерялся и спустя некоторое время нашёл дорогу к лагерю. Кроме того, в последние минуты пребывания в лесу мне стало казаться, что кто-то издалека наблюдает за мной."
    th "Неужели после такого я в одиночку сюда ни ногой?.."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ d2_day_places += 1
    $ disable_current_zone()
    jump d2_day_map

label d2_me_mt_house_day:

    $ reset_chibi("me_mt_house")
    scene bg ext_house_of_mt_day
    with dissolve
    play music music_list["smooth_machine"] fadein 1
    window show
    "Мне никуда не хотелось идти, только к себе в домик."
    th "Ольга Дмитриевна наверняка будет против. Надеюсь, я смогу добиться её снисхождения."
    "..."
    scene bg int_house_of_mt_day
    with dissolve
    th "Сяду читать, прикинусь ветошью, и с меня уже ничего не взять."
    "Я выбрал ещё не читанную книгу и устроился на кровати."
    "Чтиво оказалось весьма увлекательным, и я ни на минуту не пожалел, что решил уединиться и не мучить себя занятиями в кружке."
    "......"
    play ambience ambience_int_cabin_day fadein 1
    show mt surprise pioneer at center with dissolve
    "Некоторое время спустя всё-таки пришла вожатая, и она неприятно удивилась тому, что я был здесь."
    show mt angry pioneer at center with dspr
    mt "Семён, разве ты не сейчас не должен быть в своём кружке со всеми пионерами?"
    me "Ольга Дмитриевна, разрешите мне сегодня пропустить. Завтра пойду, честное пионерское! Просто книга очень интересная, зачитался..."
    show mt grin pioneer at center with dspr
    mt "М-м, хорошо, Семён. Только смотри, обманешь, поручу что-нибудь общественно-полезное... Чтобы не бездельничал почём зря."
    $ d2_mt_promise = True
    me "Ох."
    show mt smile pioneer at center with dspr
    th "Вляпался. Что же меня заставят делать? Убирать территорию? Копать руду?"
    "На утренней линейке я слышал, что некоторым пионерам дали указания по дежурству, но почти никого не увидел за сложной работой."
    th "Или я плохо смотрел по сторонам, или в угрозе вожатой нет ничего страшного."
    "Я прогнал эти мысли и вернулся к чтению, а Ольга Дмитриевна, порывшись в сумке, снова отлучилась."
    hide mt with dissolve
    stop ambience fadeout 1
    "..."
    "......"
    $ proficiencies ['sp_pers']+=1
    "........."
    "Я просидел в одиночестве до тех пор, как раздался звук горна."
    play sound sfx_dinner_jingle_speaker
    play sound sfx_open_door_strong
    "Пока из динамиков с улицы играла мелодия, в палату ворвался запыхавшийся Сыроежкин."
    show el laugh pioneer far at center with dspr
    el "Михаил Ефграфович разрешил карточный турнир! После ужина будет! В столовой всё расскажу!"
    hide el with dspr
    "Выпалив это, он умчался, оставив проходную дверь открытой нараспашку."
    th "Ну, ужин всяко важней, а там посмотрим, что за турнир..."
    "Книга была отложена, я спешно вышел из домика, закрыв за собой дверь."
    window hide
    stop music fadeout 2
    $ disable_current_zone()
    jump d2_pre_event

#label d2_admin_center_day:

    #"Приближаться к логову администрации, когда я должен находиться с другими пионерами в кружке? Уж точно не сейчас!"
    #$ d2_day_places += 1
    #jump d2_day_map

label d2_pre_event:

    scene black
    with dissolve
    show screen central_text("День 2 — После ужина")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg int_dining_hall_people_day
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    window show
    "........."
    "Хоть я и был голоден, свою порцию я одолел не торопясь, наслаждаясь едой."
    show el normal pioneer at cleft with dissolve
    show mt normal pioneer at cright with dissolve
    "Ещё несколько пионеров со мной понесли сдавать тарелки на железный поднос поварам, и только Электроник, отужинавший раньше всех, на выходе из столовой о чём-то спорил с Ольгой Дмитриевной."
    scene bg int_dining_hall_day
    with dissolve
    if tech_club:
        "Похоже, вожатая не разделяла мнения Михаила Ефграфовича насчёт карт."
    #else: (Временно лишняя строка, здесь возможна доработка).
    "Я не мог уйти так просто, потому что выход уже перегородила целая толпа пионеров."
    show mi normal pioneer at left with dissolve
    show sh normal pioneer at right with dissolve
    show un normal pioneer at center with dissolve
    "Здесь были все мои новые знакомые: Мику, Лена, Шурик..."
    hide mi
    hide sh
    hide un
    with dissolve
    show mz normal glasses pioneer at cright with dissolve
    "Даже та пионерка Женя, не покидающая библиотеки весь день, была рядом."
    if (d2_mz_help == True) and (d2_mz_helped == False):
        show mz angry glasses pioneer at cright with dissolve
        "Вдруг она заметила меня, сердито поджала губы и отвернулась."
        th "Ох, блин, я не сдержал слово и не явился в библиотеку помочь!..{w} Женя имеет полное право злиться на меня."
        th "Иногда забытое обещание можно расценить как ложь."
        th "Пожалуй, мне стоит извиниться перед ней, если подвернётся случай. Главное, не забыть и об этом."
    hide mz with dissolve
    show el serious pioneer at cleft
    show mt angry pioneer at cright
    with dissolve
    "...А в центре стояли Ольга Дмитриевна и Электроник."
    "Он как раз с жаром доказывал плюсы своей затеи вожатой, а та стояла с недовольным видом, ничего не отвечала и только всё больше хмурилась."
    "Я попытался было протиснуться мимо этого импровизированного собрания, стараясь не быть замеченным, но мне не удалось."
    "Толпа была слишком плотной."
    "Я смог обойти только двух пионеров, стоявших последними, и оказался накрепко зажат между Шуриком и подоспевшими за мной пионерками."
    if (d1_dv_evening == True) or (d2_met_ug == True):
        show ug normal at fright with dissolve
        "Тут я увидел Угрюмого почти у самой двери. Он что-то сказал младшему пионеру, и тот посторонился, выпустив его из столовой на волю."
        hide ug with dissolve
        "И вообще, я бы даже не заметил исчезновения Угрюмого, если б не был знаком с ним подольше, чем с остальными."
        th "Мне бы так!"
        "Но вот некуда было двигаться."
    "Именно таким, застрявшим в толпе, меня и заметил Электроник."
    show el laugh pioneer at cleft with dspr
    "Едва завидя меня, он воодушевился и тут же замахал рукой, подзывая к себе, хотя это было явно бессмысленно."
    "Я не мог пошевелиться!"
    el "Семён!"
    show el smile pioneer at cleft with dspr
    el "Семён тоже будет с нами!"
    show mt normal pioneer at cright with dspr
    "Увидев, что Ольгу Дмитриевну это не впечатлило — она даже не посмотрела в мою сторону — он нашёл последний аргумент."
    show el laugh pioneer at cleft with dspr
    el "И вам ведь не придется ничего делать! Всю организацию я беру на себя!"
    show mt surprise pioneer at cright with dspr
    mt "М-м-м-м..."
    "Я думал, что она сейчас произнесёт свое «Нет!», и все разойдутся..."
    show el smile pioneer at cleft with dspr
    "Но, видимо, Электроник задел всё же какую-то тайную струну Ольги Дмитриевны."
    show mt smile pioneer at cright with dspr
    "Потому что та уже не казалась такой серьезной..."
    "Она не сдалась, но больше не хмурилась."
    mt "А Персунов согласится?"
    if tech_club:
        th "Верно, верно! Моего мнения не спросили! Хотя, после после того променада к Михаилу Ефграфовичу, я теперь соучастник Эла и вынужден остаться с ним, он мне все уши прожужжал игрой..."
    show mt grin pioneer at cright with dspr
    mt "Он, наверно, уже сбежал на пляж..."
    show us smile pioneer at center with dissolve
    "Тут раздался голос Ульяны, которая, оказывается, была здесь же неподалеку и теперь ехидно разглядывала меня."
    us "Не-е-е... Не успел ещё!"
    show mt smile pioneer at cright with dspr
    "Разглядывала, вытянув шею, потому что иначе не могла бы меня увидеть из-за чужих спин."
    hide us with dissolve
    #th "С чего они вообще взяли, что я хочу пойти на пляж?!"
    "Электроник пытался упрочить свою позицию."
    "Он явно понял, что вожатая пошла им навстречу."
    show el laugh pioneer at cleft with dspr
    el "Да конечно согласится! Пионеры должны выручать друг друга!"
    "И он с новыми силами начал убеждать вожатую."
    if (tech_club == False):
        "А до меня только дошло..."
        th "В чем это я соглашусь участвовать?!"
        "Я хотел прокричать это, но легкие мои все еще были сдавлены, сзади ко мне прижималась девичья..."
        "И я смог разве что с трудом выдохнуть."
    "На Ольгу Дмитриевну это заявление Электроника произвело совсем другой эффект."
    show mt sad pioneer at cright with dspr
    mt "Вот это меня и беспокоит..."
    show el normal pioneer at cleft with dspr
    mt "Разве дело для пионеров — в карты играть?"
    if tech_club:
        th "Так я и думал, что вожатой эта идея не нравилась с самого начала."
    elif d1_un_evening:
        th "Причем здесь карты?"
    else:
        "Покопавшись в памяти, я сообразил о чём речь."
        th "Да, Сыроежкин ещё вчера говорил мне о них, что сочинил правила и всё такое..."
    show el shocked pioneer at cleft with dspr
    el "Но Ольга Дмитриевна! Это не просто карты!"
    el "Это же совершенно новая игра. Я её придумал!"
    show el normal pioneer at cleft with dspr
    "Сыроежкин на секунду замолчал, явно подбирая слова, а потом начал палить, как из пушки."
    show el laugh pioneer at cleft with dspr
    el "И она тренирует внимание..."
    "Он явно сочинял это на ходу."
    el "...память..."
    el "И..."
    show el normal pioneer at cleft with dspr
    "Снаряды явно кончились."
    show us laugh pioneer at center with dissolve
    us "И ловкость рук!"
    show el smile pioneer at cleft with dspr
    show mt laugh pioneer at cright with dspr
    "Это снова проснулась Ульянка, на сей раз выручив Электроника."
    hide us with dissolve
    "Все рассмеялись."
    "И, кажется, в толпе стало свободнее."
    "Я смог вздохнуть полной грудью."
    show mt normal pioneer at cright with dspr
    "И как раз в это время Ольга Дмитриевна наконец заметила меня."
    "Похоже, спор, чем бы он ни был вызван, подходил к концу."
    show el normal pioneer at cleft with dspr
    "Толпа понемногу рассеялась, а я стоял, не в силах уйти, потому что вожатая все ещё смотрела на меня."
    "Наконец Ольга Дмитриевна на что-то решилась."
    show mt smile pioneer at cright with dspr
    mt "Хорошо..."
    mt "Делайте что хотите."
    mt "Проводите свой турнир."
    show el smile pioneer at cleft with dspr
    "И она снова обратилась к Электронику."
    show mt surprise pioneer at cright with dspr
    mt "Только от меня-то что вам нужно?"
    mt "Сами всё и организовывайте..."
    show el laugh pioneer at cleft with dspr
    "Электроник стоял теперь в победной позе и явно ликовал."
    el "Нам нужно четыре колоды карт."
    "Он невинно смотрел в лицо вожатой."
    el "И мы знаем, что они у вас есть..."
    show mt laugh pioneer at cright with dspr
    "А Ольга Дмитриевна расхохоталась."
    show el smile pioneer at cleft with dspr
    mt "Ах, чертенята!"
    show mt smile pioneer at cright with dspr
    mt "А ведь это нарушение правил."
    "Она покачала головой, хотя совсем не казалась рассерженной."
    mt "Ладно, раз уж в администрации приняли решение..."
    show mt grin pioneer at cright with dspr
    mt "Не спешите уходить, пионеры! Здесь пройдёт общелагерное мероприятие — карточный турнир. Все желающие могут остаться поучаствовать или поболеть за товарищей из своих отрядов."
    "По столовой разнёсся одобрительный гул, и стало ясно, что тут будет полно народу, когда начнётся соревнование."
    show mt normal pioneer at cright with dspr
    "И вожатая снова повернулась ко мне и позвала кивком головы."
    mt "Будешь участвовать? А то Сыроежкин за тебя высказался."
    if tech_club:
        "С Элом меня связывало какое-никакое общее дело, и было бы не по-дружески по отношению к нему сейчас взять и уйти. Тем более, он что-то говорил о новых правилах, и это, надо признаться, слегка интриговало."
        $ d2_in_game = True
    menu:
        "Почему бы и нет?":
            $ common_event = common_event + 1
            $ d2_in_game = True
        "Играйте без меня":
            me "Спасибо за предложение, но я не хочу. Играйте без меня."
            show el surprise pioneer at cleft with dspr
            el "Семён, может хотя бы останешься посмотреть?"
            me "Извини, у меня были другие планы."
            show el sad pioneer at cleft with dspr
            "Сыроежкин заметно огорчился."
            show el upset pioneer at cleft with dspr
            el "Я не знал... Я думал, ты не откажешься..."
            el "Ладно, если занят, иди. Но потом жалеть будешь, что пропустил!"
            me "Не исключено, кто знает?"
            "Пожав плечами, я ушёл."
            window hide
            stop music fadeout 2
            jump d2_skip_common_event
    if d2_in_game:
        me "Почему бы и нет? Я могу сыграть с кем-нибудь."
        show el grin pioneer at cleft with dspr
        el "Отлично, Семён! Я уже решил, как мы разделим участников на группы."
        show el smile pioneer at cleft with dspr
        el "Так что, Ольга Дмитриевна, не переживайте за организацию, я всё устрою."
        "У меня возникло странное ощущение, что вожатая сейчас что-нибудь потребует..."
        show mt smile pioneer at cright with dspr
        mt "Вот."
        "Она протянула мне небольшой вычурный ключ."
        mt "Это от верхнего ящичка в моём шкафу."
        mt "Там найдешь карты."
        show mt angry pioneer at cright with dspr
        "Она как могла грозно посмотрела сначала на меня, потом на Электроника..."
        mt "Под вашу ответственность!"
        "Я старался сохранять невозмутимость, но это было трудно, потому что я совсем не вовремя представил, чем ещё может быть забит её шкафчик..."
        show mt normal pioneer at cright with dspr
        "И, кажется, мой вид не убедил Ольгу Дмитриевну, потому что она слегка нахмурилась."
        mt "Или, может, Славе это поручить..."
        menu:
            "Сам справлюсь":
                me "Да я и сам справлюсь!"
                show mt surprise pioneer at cright with dspr
                "И я, не ожидав такого от себя, протянул руку и взял ключ. Надеюсь, это не выглядело так, будто я отобрал его у вожатой."
                hide mt with dissolve
                hide el with dissolve
                th "Ничего такого в том, чтобы сходить за картами в свой домик..."
                "Следом прозвучал голос Электроника."
                el "Поторапливайся, Семён!"
                window hide
                stop music fadeout 2
                jump d2_cards_walk_alone

            "Мы можем вместе сходить":
                me "Мы можем вместе сходить."
                me "Если вы мне не доверяете!"
                $ lp_sl = lp_sl + 1
                show mt surprise pioneer at cright with dspr
                "Ольга Дмитриевна как-то удивлённо посмотрела на меня."
                mt "Хорошо, раз так..."
                show sl smile pioneer at center with dissolve
                show mt normal pioneer at cright with dspr
                "Она дала ключ Славе, и мы с ней покинули столовую."
                window hide
                stop music fadeout 2
                jump d2_walk_sl

label d2_cards_walk_alone:

    scene bg ext_houses_day
    with dissolve
    play music music_list["i_want_to_play"] fadein 1
    window show
    "В очередной раз я исполнял какую-то нелепую просьбу Ольги Дмитриевны."
    "Но отказываться было уже поздно."
    if d1_un_evening:
        "Да и мне было немного любопытно."
        "Интересно, Электроник и вправду придумал новую игру?"
        "Когда-то мне нравился покер."
        "Так что я решил посмотреть, что из этого получится."
    scene bg ext_house_of_mt_day
    with dissolve
    "Перед своим домиком я остановился."
    "Почему-то я вспомнил, как в детстве мы рисовали на картах крестики, чуть сгибали уголки, чтобы знать потом, у кого тузы."
    th "Хм... А ведь это идея!"
    "Раз уж меня вынуждают играть — почему бы мне не выиграть?"
    "Откуда-то во мне проснулся давно забытый азарт."
    "Нужно только незаметно пометить карты..."
    "Никто и не узнает."
    "Улыбнувшись собственной непонятно откуда взявшейся хитрости я зашёл в домик."
    window hide
    stop music fadeout 2
    $ d2_walk = 0
    jump d2_ultimatum

label d2_walk_sl:

    scene bg ext_square_day
    with dissolve
    play music music_list["get_to_know_me_better"] fadein 1
    play ambience ambience_camp_center_evening fadein 1
    window show
    show sl smile pioneer at cright with dissolve
    "Мы шли вместе со Славей по залитой солнцем площади."
    "Я не знал, о чём заговорить, и мы оба молчали."
    "А вокруг был тихий вечер, ещё не окрасившийся в цвета заката. Лишь немногие пионеры не остались на мероприятии, решив провести свободное от кружков время на улице." 
    "Я немного с сожалением обернулся и посмотрел в сторону пляжа."
    th "Да, я до сих пор так и не урвал момента, чтобы искупаться."
    "И, кажется, Славя заметила мой взгляд, потому что тут же спросила об этом."
    show sl smile2 pioneer at cright with dspr
    sl "А ты и вправду хотел убежать на пляж?"
    me "Угу."
    me "И странно, что Ольга Дмитриевна догадалась. Я ведь никому не..."
    show sl normal pioneer at cright with dspr
    sl "Вовсе не странно!"
    "Славя вдруг перебила меня и..."
    "Говоря это, она улыбнулась, но почему-то с грустью."
    "Как будто вспомнила о чём-то."
    show sl smile2 pioneer at cright with dspr
    sl "Здесь многие только и думают о пляже."
    show sl surprise pioneer at cright with dspr
    sl "Ольге Дмитриевне часто приходится там караулить. Словом, чтобы пионеры кроме речки ещё чем-то были заняты."
    me "Так вот что она подразумевала под работой!.."
    show sl sad pioneer at cright with dspr
    "Я шутил, но Славя восприняла мои слова всерьез."
    sl "Да, трём вожатым и так приходится тяжело со всеми нами, и никто не помогает! А я..."
    me "Не остаёшься в стороне?"
    show sl smile pioneer at cright with dspr
    "Она кивнула."
    stop ambience fadeout 1
    scene bg ext_houses_day
    with dissolve
    show sl normal pioneer at cright with dissolve
    sl "Я здесь вроде помощницы вожатых."
    me "И что ты делаешь, например?"
    show sl surprise pioneer at cright with dspr
    sl "Помогаю с дежурством, иногда приходится заменять Ольгу Дмитриевну, если она вдруг отлучится..."
    sl "Вожусь с младшими, если Инга Максимовна попросит, занимаюсь с ними спортом. Проверяю, чтобы пионеры соблюдали режим дня."
    show sl smile2 pioneer at cright with dspr
    sl "Они такие забавные. Видно, кому чего не хватает, кто что любит."
    "Она снова улыбнулась."
    sl "Ещё придумываю с Ольгой Дмитриевной всякую всячину для конкурсов с мероприятиями и слежу, чтобы Саша не мешала другим в кружке."
    if (unnat_club == False):
        me "Саша?"
        sl "Девочка из младшего отряда, числится у меня юннатом."
    show sl normal pioneer at cright with dspr
    sl "В общем, работы много."
    me "Да уж. Действительно много! Как у тебя на всё хватает времени?"
    sl "Вот оно и уходит на всё это. Почти."
    "Почему-то я вспомнил, что Ольга Дмитриевна говорила о том, что сделает из меня пионера..."
    th "Как бы мне не надавали каких-нибудь обязанностей."
    me "Они заставили тебя этим заниматься?"
    show sl smile pioneer at cright with dspr
    "Сейчас я уже не шутил, но Славя улыбнулась — фраза и впрямь прозвучала глуповато."
    sl "Нет, конечно! Я сама вызвалась."
    show sl smile2 pioneer at cright with dspr
    sl "Мне нравится помогать."
    sl "И это здорово, что им нужна моя помощь."
    "И я не знал, что ответить."
    scene bg ext_house_of_mt_day
    with dissolve
    show sl smile pioneer at cright with dissolve
    "Но отвечать и не пришлось, потому что мы как раз пришли к семнадцатому домику."
    window hide
    stop music fadeout 2
    $ d2_walk = 1
    jump d2_ultimatum

label d2_ultimatum:

    scene black
    with dissolve
    show screen central_text("День 2 — Ультиматум")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_dining_hall_away_day
    with dissolve
    play music music_list["eat_some_trouble"] fadein 1
    window show
    if d2_walk == 0:
        "Я спешно возвращался к столовой с четырьмя колодами карт. Мне повезло, что одна уже была краплёна кем-то до меня понятным способом. Я же усовершенствовал другую колоду, а две оставшиеся не стал трогать — времени не было."
    else:
        show sl smile pioneer at cright with dissolve
        "Мы возвращались с картами к столовой, где должен был пройти турнир."
    scene bg ext_dining_hall_near_day
    with dissolve
    show dv normal pioneer2 at cleft with dissolve
    "А на крыльце со скучающим видом уже стояла Алиса."
    if d2_walk == 0:
        "Я толкнул дверь и..."
        show dv normal pioneer2 at center with dspr
        "Упёрся грудью прямо в руку Алисы, перегородившей мне вход."
    else:
        show sl serious pioneer at cright with dspr
        show dv angry pioneer2 at cleft with dspr
        "Славя прошла мимо Двачевской."
        "Мне ещё показалось, что они как-то странно взглянули друг на друга..."
        "Как будто между ними пролетела какая-то искра... И вряд ли то была искра дружеских чувств."
        th "Разве они хорошо знакомы?"
        hide sl
        show dv normal pioneer2 at center
        with dissolve
        "А потом я уперся грудью прямо в руку Алисы, перегородившей мне вход."
    dv "Торопишься куда-то?"
    "Она говорила тихо, но почему-то её тон был угрожающим."
    if d2_walk == 0:
        "Дверь в столовую медленно закрылась, и мы с Алисой остались наедине."
    else:
        "Дверь за Славей медленно закрылась, и мы с Алисой остались наедине."
    th "Чего она хочет?"
    show dv normal pioneer2 close at center with dspr
    "Алиса мягко, но настойчиво тыкала пальцем мне в грудь, отталкивая меня от входа и заставляя пятиться."
    "Так что я скоро оказался на пару ступенек ниже неё, а она нависла надо мной сверху."
    dv "Торопишься, значит..."
    show dv angry pioneer2 close at center with dspr
    if d2_guitar_illegal:
        me "Кстати, где ты была? После трюка с гитарой я нигде не мог отыскать тебя и решил дождаться ужина. Ну так, поведаешь, может быть?"
        dv "Не твоё дело, где."
    "Она явно злилась из-за чего-то."
    "На меня?!"
    th "В чём это я, интересно, виноват?"
    dv "Сказали карты принести, а ты и рад стараться?"
    me "Принёс. Ну и что?"
    dv "Тоже мне, пай-мальчик."
    if d2_walk == 0:
        th "С краплёными картами?"
        th "Скорее, доморощенный шулер." 
    dv "Да ты, наверно, в карты даже играть не умеешь..."
    me "Умею!{w} И получше тебя."
    show dv laugh pioneer2 close at center with dspr
    "И тут она звонко расхохоталась!"
    "Похоже, в этом лагере немногие осмеливались возражать Алисе, потому что она явно была удивлена моей наглостю."
    if sp_crg <= 1:
        "Впрочем, как и я сам."
    show dv grin pioneer2 close at center with dspr
    "А она вдруг перестала смеяться и спросила, хитро прищурившись и даже закусив в предвкушении губу."
    dv "А хочешь пари?"
    "Сейчас Алиса не напоминала грозу всего лагеря, она была похожа на озорную девчонку..."
    "Я помотал головой."
    me "Что ещё за пари?"
    th "Ничего я не хочу!"
    show dv smile pioneer2 close at center with dspr
    dv "Что ты не выиграешь!"
    th "Глупости! Я ведь даже не знаю, во что мы играем."
    me "А если выиграю? Перестанешь навязывать дурацкие пари?"
    "Конечно, Двачевская тогда сама поостережётся брать меня на слабо. Правда, я не очень был уверен в этом."
    if d2_walk == 0:
        th "Хотя почему это — «если»?"
        "Я ведь пометил карты."
        $ INVISIBLE = True
    else:
        $ INVISIBLE = False
    "Меня снова охватил какой-то непонятный азарт."
    if d2_walk == 0:
        "Как тогда, перед домиком Ольги Дмитриевны."
    "И не подчиниться ему не было никакой возможности."
    "Дваче стояла напротив меня, всё так же уперев палец мне в грудь, и её глаза теперь светились тем же азартом, в котором сгорал я сам."
    show dv grin pioneer2 close at center with dspr
    dv "Идёт!"
    "Я думал, что бы потребовать ещё..."
    show dv smile pioneer2 close at center with dspr
    "А она вскинула голову, взмахнув своими хвостами, и снова хитро улыбнулась."
    dv "А что если проиграешь?"
    me "Проиграю?"
    "Этого мне в голову не приходило."
    me "Что значит проиграю?"
    me "Да я чемпион в карточных играх! Я..."
    show dv surprise pioneer2 close at center with dspr
    th "Б-же, что я говорю?!"
    "Но было поздно."
    "Я просто не мог уже остановиться, меня несло."
    me "Я..."
    "Тут странный всплеск так же внезапно, как и появился, начал спадать, и я намного тише пробормотал."
    me "Я выиграю."
    show dv normal pioneer2 close at center with dspr
    "И уже без всякой уверенности."
    me "Обязательно..."
    "Азарт во мне медленно догорал, а я понемногу приходил в себя."
    show dv smile pioneer2 close at center with dspr
    "Алиса и не думала успокаиваться."
    dv "Ну, смотри!"
    "Девочка вдруг схватила меня за руку, у локтя."
    "И не успел я подумать, какая у неё тёплая... нет, жаркая ладонь, и сказать, что она делает мне больно, как Алиса чуть ли не прокричала восторженно."
    dv "Если проиграешь, я..."
    show dv grin pioneer2 close at center with dspr
    "Она на секунду задумалась, снова прикусив губу и не переставая при этом улыбаться, и выпалила, негромко, так, чтобы это услышал только я."
    dv "Скажу всем, что ты подглядывал за мной, когда я переодевалась!"
    dv "И..."
    show dv laugh pioneer2 close at center with dspr
    "Она расхохоталась, затем наклонилась к моему уху."
    show dv grin pioneer2 close at center with dspr
    dv "И лапал меня!"
    show dv smile pioneer2 close at center with dspr
    "Алиса победоносно глядела на меня!"
    me "ЧТО?!"
    show dv normal pioneer2 at center with dspr
    "Но Алиса, отпустив меня, уже целиком была погружена в мысли о предстоящем турнире и не обращала внимания ни на моё потрясение, ни на мои сбивчивые слова."
    me "Та... так же нельзя! Понимаешь, что может быть?"
    "Она уже ни о чём не беспокоилась."
    show dv smile pioneer2 at center with dspr
    dv "Так что играй в полную силу и берегись, если не выиграешь!"
    "И со звонким смехом, очень радостная, она взбежала по ступеням и скрылась в столовой, хлопнув на прощание дверью."
    hide dv with dspr
    th "Б-же, во что я ввязался?!"
    "Я медленно и нехотя поплёлся за ней."
    th "Ей никто не поверит.{w} Ей никто не поверит!"
    "И сам я при этом себе не верил."
    window hide
    stop music fadeout 2
    jump d2_cards_common_event

label d2_cards_common_event:
    
    scene black
    with dissolve
    show screen central_text("День 2 — Турнир")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_dining_hall_near_day
    with dissolve
    play music music_list["drown"] fadein 1
    "Перед самой дверью я остановился."
    "Зачем я вообще туда иду?"
    "Внезапно мне пришла в голову интересная идея."
    th "Что, если я сбегу?"
    "Прямо сейчас!"
    "Достаточно только развернуться и..."
    play sound sfx_open_door_2
    "Но даже не мысль о том, что Алиса осуществит свою угрозу, остановила меня, а то, что дверь отворилась и на порог вышел Электроник."
    show el angry pioneer at center with dissolve
    el "Тебя только за картами посылать!"
    "Без лишних слов он отобрал у меня принесённые колоды и, не останавливаясь на этом, потащил за собой туда, где меня ждало пари, которое я не заключал, и Алиса, видеть которую мне теперь совсем не хотелось..."
    window hide
    play sound sfx_close_door_1
    stop music fadeout 1
    scene bg int_dining_hall_day
    with dissolve
    play music music_list["i_want_to_play"] fadein 1
    window show
    "Внутри всё было готово к проведению турнира."
    "Народу было много, и царило какое-то праздничное настроение, которое я теперь совсем не хотел разделять с пионерами."
    "Стараниями дежурных столовые приборы убрали, а столы отодвинули чуть дальше к стенам, оставив стоять отдельно только пять из них."
    "Причём почти все места уже были заняты."
    "И все сидели парами."
    show us smile pioneer at cleft
    show sh upset pioneer at cright
    with dissolve
    "Шурик, как и я, не понимающий, что он здесь делает, сидел с Ульяной, которая в нетерпении ёрзала на стуле и явно пыталась вытянуть из Шурика какие-то сведения о предстоящей игре."
    "А он только недовольно хмурился и старался делать вид, что её не видит."
    "Удавалось ему это с переменным успехом... Вернее, совсем не удавалось."
    hide sh
    hide us
    with dissolve
    show sl smile2 pioneer at cleft
    show mz normal glasses pioneer at cright
    with dissolve
    "За следующим столом, тихо и скромно ожидая начала, сидела Славя, а напротив неё библиотекарша."
    "Той, казалось, вообще ничего не было интересно."
    th "Наверное, ее тоже заставили играть, как и меня..."
    hide sl
    hide mz
    with dissolve
    show dv smile pioneer at cleft
    show mi happy pioneer at cright
    with dissolve
    "Алиса..."
    "При виде её я невольно вздрогнул."
    "Алиса никуда не исчезла и сидела сейчас всё такая же воодушевлённая, поедая Мику глазами, горящими в безумном азарте."
    "Мику я невольно пожалел, хотя и обрадовавшись тому, что не мне сейчас предстояло играть с Алисой."
    "Судя по тому, как Алиса усмехнулась, заметив меня, о пари она не забыла."
    th "А я ведь так на это надеялся! И, похоже, о споре я сам нескоро забуду."
    hide dv
    hide mi
    with dissolve
    show un normal pioneer at center with dissolve
    "Пустовало только одно место — напротив Лены, однако я пока что не сел к ней."
    "А всё остальное пространство было занято, видимо, болельщиками и зрителями."
    hide un with dissolve
    show mt smile pioneer far at left with dissolve
    #show bt; show lk
    "Ольга Дмитриевна тоже была здесь, но стояла позади и, как и обещала, не вмешивалась, а только наблюдала за нами, о чём-то болтая с Ингой Максимовной."
    "Рядом с ними околачивался вожатый Дима, с задумчивой улыбкой прислушивавшийся к их разговору."
    hide mt with dissolve
    #hide bt; hide lk
    "Всё это я заметил, ещё не теряя надежды, что играть мне не придется и что я таким образом избавлюсь от необходимости участвовать в нелепом пари."
    "Один стол был немного отдельно от остальных, и на нём на подставке стоял широкий лист ватмана."
    "Как раз к нему и направился Электроник, потащив меня за собой."
    scene cg lvl_1
    with dissolve
    "Подойдя поближе, я заметил, что ватман изображал, и довольно подробно, схему предстоящего турнира."
    "Тут было и моё имя."
    th "Моя последняя надежда умерла."
    hide cg lvl_1
    scene bg int_dining_hall_day
    with dissolve
    "Делать больше было нечего, а протестовать уже совсем не было сил."
    "Так что, пока Электроник с важным видом считал карты, я просто занял своё место напротив Лены."
    show un normal pioneer at center with dissolve
    "Она робко сидела на самом краешке стула, боясь поднять глаза из-за окружающей ее толпы зрителей, и только ещё больше смутилась, когда я сел рядом с ней."
    "Увидев, что ей этот турнир так же мало нравится, как и мне, я почувствовал себя легче."
    hide un with dissolve
    show el smile pioneer at center with dissolve
    "Раздав на каждый стол по колоде, Электроник удовлетворенно кивнул головой, взглянул на ватман и с обычным для него оживлением обратился к нам."
    el "Карты у нас есть, все на местах, так что турнир можно начинать!"
    "Все заулыбались, а кое-кто из зрителей даже захлопал в ладоши."
    "И только я не разделял всеобщей радости."
    "Сыроежкин-Электроник тем временем отошёл к своему столу."
    "Важно подняв палец, он подождал, пока на него не обратят внимание, и принялся декламировать."
    el "Для начала о правилах."
    "Поочерёдно Электроник показал два ватмана."
    el "Это схема турнира и..."
    show dv normal pioneer at left with dissolve
    "Тут его перебила Алиса."
    dv "Мы это уже знаем!"
    dv "Ближе к делу!"
    "Я буквально физически ощущал её желание победить."
    "Вот только не понимал, почему она хотела победить именно меня."
    th "За что мне это?!"
    hide dv
    with dissolve
    show el sad pioneer at center with dspr
    show mt grin pioneer far at fleft with dissolve
    "Электроник же смутился и даже посмотрел на Ольгу Дмитриевну, но та не спешила придти ему на помощь..."
    "То ли она решила дать Электронику шанс самому разобраться, то ли просто не хотела ничем заниматься. Как и говорила: вся организация мероприятия на пионере."
    "Так или иначе, выкручиваться Сыроежкну пришлось самому."
    hide mt with dissolve
    show el normal pioneer at center with dspr
    "Но, нахмурившись и слегка сбившись с темпа, он всё же нашелся, что ответить."
    el "Так Семён пропустил все мои объяснения. Напомню ещё раз: мы проводим два турнира по четыре группы в каждом, сначала играет старший отряд, потом младший."
    "Он продемонстрировал вторую схему турнира на обороте ватмана."
    show el smile pioneer at center with dspr
    el "Затем финалисты отстаивают честь своего отряда в заключительном раунде."
    el "Отлично, раз схемы вы уже знаете..."
    show el serious pioneer at center with dspr
    el "Основное правило — проигравший вылетает!"
    "Электроник важно оглядел игроков."
    el "Так что слушайте внимательно, потому что никаких вторых шансов, переигровок и прочего — не будет!"
    show us surp2 pioneer at right with dissolve
    "Увидев, что Ульянка тянет руку, чтобы что-то спросить, Электроник только отмахнулся."
    show el normal pioneer at center with dspr
    el "Пока никаких вопросов! Слушайте правила!"
    th "Странно, что она не закричала с места, как всегда."
    show us normal pioneer at right with dspr
    "Видимо, на неё так подействовала атмосфера турнира, потому что, пусть и с неохотой, руку она опустила."
    hide us with dissolve
    "А Электроник продолжил."
    show el smile pioneer at center with dspr
    el "Каждый тур состоит из двух игр."
    el "Если и после них у игроков будет ничья, тогда исход решит третья, дополнительная."
    el "После этого проигравшие в туре из игры выбывают, и начинается следующий тур."
    el "Поскольку от каждого отряда восемь участников, то отборочных туров будет три."
    show el laugh pioneer at center with dspr
    el "А четвёртый тур — финальный!"
    "У него от восхищения, видимо, самим собой, загорелись глаза, и он снова важно поднял палец."
    el "После которого победителя ждёт огромный приз!"
    show us surp2 pioneer at right with dissolve
    "Даже самые равнодушные пионеры, наблюдавшие за мероприятием со стороны, оживились. Рука Ульянки тут же снова взмыла вверх."
    show el serious pioneer at center with dspr
    "Но Электроник опять только отмахнулся."
    el "Не сейчас!.."
    show us dontlike pioneer at right with dspr
    us "У-у-у!"
    "На этот раз Ульянка надула губки, явно обидевшись, а я пожалел Электроника."
    "После турнира ему это ещё припомнят."
    hide us with dissolve
    show el smile pioneer at center with dspr
    el "Итак, правила игры."
    el "Раз игра новая и никому не известная..."
    show el grin pioneer at center with dspr
    el "А как она может быть известна, если я её только на днях придумал!"
    show dv normal pioneer at left with dissolve
    dv "Ближе к делу!"
    show el normal pioneer at center with dspr
    "Это снова перебила Алиса."
    "Но было видно, что сейчас она слушает внимательно."
    hide dv with dissolve
    show el smile pioneer at center with dspr
    "Электроник же сделал вид, что прочищает горло."
    el "Так вот, игра своими комбинациями напоминает покер..."
    show mt surprise pioneer far at fleft with dissolve
    "Он посмотрел на Ольгу Дмитриевну и сразу добавил."
    show el shocked pioneer at center with dspr
    el "Но только слегка!"
    hide mt with dissolve
    show el normal pioneer at center with dspr
    "Я невольно почувствовал себя увереннее. Покер когда-то был моей любимой игрой."
    show el smile pioneer at center with dspr
    el "Итак, вам нужно собрать у себя лучшую комбинацию карт."
    el "Двойку, тройку, четверку..."
    show us surp1 pioneer at right with dissolve
    us "Пятерку!"
    "Это вставила Ульяна."
    "Ей надоело тянуть руку, и она снова стала собой — со своими высказываними с места... и не к месту."
    "Но Электроника это нисколько не смутило."
    hide us with dissolve
    show el laugh pioneer at center with dspr
    el "Если кто-то не знает, какая комбинация лучше, а какая хуже — вот тут нарисованы все комбинации."
    "И он показал на другую половину ватмана."
    show el normal pioneer at center with dspr
    el "Чтобы лучше понять правила, давайте разберём на примере."
    "И он обернулся к нам."
    show el laugh pioneer at center with dspr
    el "Участники, раздавайте пока карты."
    el "По шесть каждому участнику."
    el "И пусть карты никто пока не смотрит!"
    "Я небрежно потасовал колоду и начал раздавать карты себе и Лене, вспоминая всё то, что знал о покерной игре."
    show el normal pioneer at center with dspr
    "А Электроник принялся ходить вокруг, наблюдая, как мы раздаем."
    "У стола Шурика и Ульяны он вдруг остановился и закричал."
    show el shocked pioneer at center with dspr
    el "Я же сказал: {b}по  ш е с т ь{/b}!!!"
    el "Это значит, что каждому нужно сдать столько!"
    el "Не надо себе двенадцать сдавать!"
    show us dontlike pioneer at right with dissolve
    "Ульяна только фыркнула..."
    us "Пфф! А мне шести карт мало! Я хочу бо-ольше!"
    hide us with dissolve
    "Но после нескольких минут препирательств, в которые уже вмешались пионеры-болельщики, лишние карты девочка всё же убрала."
    show el normal pioneer at center with dspr
    "Когда Электроник наконец удовлетворился увиденным, а перед каждым лежало по шесть закрытых карт, он продолжил."

    $ d2_cardgame_block_rollback = True

    if persistent.AbcbCardsDemo:
        menu:
            "Пройти обучение":
                jump ii_demo_play
            "Пропустить обучение":
                jump d2_cards_tournament

label ii_demo_play:
    python:
        dialogs = {
                        (3, 'rival_select','call'):'ii_demo_play_intro',
                        (3, 'me_defend_1','call'):'ii_demo_play_me_defend_1',
                        (3, 'me_select_1','call'):'ii_demo_play_me_select_1',
                        (3, 'rival_defend','call'):'ii_demo_play_rival_defend',
                        (2, 'rival_select','jump'):'ii_demo_play_after_loop'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalUn(un_avatar_set, u"Пробная игра")
        VISIBLE = False
    jump cards_gameloop

label ii_demo_play_intro:
    
    show el laugh pioneer at center with dspr
    $ show_cards()
    el "Посмотрите на карты внимательно."
    $ show_cards()
    if d2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
        $ show_cards()
        "Я уже много лет не играл, но было приятно узнать, что пометки читаются так же, как и раньше."
        $ show_cards()
        "Все карты лежали передо мной, как открытые."
    $ show_cards()
    show el smile pioneer at center with dspr
    el "Теперь представьте, что это две армии и что вы сейчас готовитесь к сражению!"
    $ show_cards()
    show el smile pioneer at cleft with dspr
    $ show_cards()
    show us surp1 pioneer at right with dissolve
    $ show_cards()
    "По-моему, только Ульянка представила что-то подобное, остальные же просто ждали продолжения."
    $ show_cards()
    show el laugh pioneer at cleft with dspr
    "Но Электронику так понравилось, что хоть кто-то относится серьёзно к его игре, что он ещё больше воодушевился."
    $ show_cards()
    el "Теперь можете посмотреть карты."
    $ show_cards()
    show us smile pioneer at right with dissolve
    $ show_cards()
    "И Ульянка, недолго думая, схватила... карты Шурика и разом перевернула их!"
    $ show_cards()
    show sh scared pioneer at cright behind us with dissolve
    $ show_cards()
    show el shocked pioneer at cleft with dspr
    $ show_cards()
    el "{i}Свои{/i} карты, а не чужие!"
    $ show_cards()
    show us laugh pioneer at right with dspr
    $ show_cards()
    show sh upset pioneer at cright behind us with dspr
    $ show_cards()
    "Но Ульяна даже и не подумала извиняться!"
    $ show_cards()
    show us smile pioneer at right with dspr
    $ show_cards()
    us "А это была разведка!!!"
    $ show_cards()
    show el sad pioneer at cleft with dspr
    $ show_cards()
    "Она была совершенно неуправляема сейчас, и только Шурика, казалось, уже ничем нельзя удивить."
    $ show_cards()
    hide us with dissolve
    $ show_cards()
    "Он молча принялся собирать свои карты, которые ещё не видел разве только он сам."
    $ show_cards()
    hide sh with dissolve
    
    $ VISIBLE = True
    $ show_cards()
    show el normal pioneer at center with dspr
    $ show_cards()
    "Наконец, когда каждый разобрал карты, Электроник продолжил объяснять правила."
    $ show_cards()
    el "Итак, ваши карты — это армии, но сражение ещё только впереди, сначала нужно укрепить своих бойцов."
    $ show_cards()
    el "И чтобы это сделать..."
    $ show_cards()
    "Электроник выждал многозначительную паузу и выпалил."
    $ show_cards()
    show el laugh pioneer at center with dspr
    $ show_cards()
    el "Вы можете переманивать нескольких бойцов соперника на свою сторону!"
    $ show_cards()
    show us surp1 pioneer at right with dissolve
    $ show_cards()
    us "Можно красть карты?!"
    $ show_cards()
    "Кажется, Ульянка первая поняла, что имел в виду Электроник, и это привело её в полнейший восторг!"
    $ show_cards()
    show el normal pioneer at center with dspr
    $ show_cards()
    el "Д-да!.."
    $ show_cards()
    hide us with dissolve
    $ show_cards()
    "Хотя его определённо смутило такое определение."
    $ show_cards()
    show el serious pioneer at center with dspr
    $ show_cards()
    el "Но всё не так просто."
    $ show_cards()
    el "Первым ходом тот, кто сейчас собирается украсть карту... м-м... или завербовать чужого бойца — выбирает свою цель."
    $ show_cards()
    el "Окажется ли это солдат или офицер — это уже зависит во многом от удачи."
    $ show_cards()
    show us surp1 pioneer at right with dissolve
    $ show_cards()
    us "Мой дедушка офицер! А папа — генерал!"
    $ show_cards()
    show el sad pioneer at center with dspr
    $ show_cards()
    "Ульянка уже совсем не могла держать себя в руках."
    $ show_cards()
    hide us with dissolve
    $ show_cards()
    show el normal pioneer at center with dspr
    $ show_cards()
    el "Итак, противник тянется к карте, но и вы не должны дремать!"
    $ show_cards()
    show el laugh pioneer at center with dspr
    $ show_cards()
    el "У вас есть две попытки запутать врага, поменяв карты местами!"
    $ show_cards()
    el "Но можно и не пользоваться этим правом, если, например, собираются украсть ненужную карту."
    $ show_cards()
    show el smile pioneer at center with dspr
    $ show_cards()
    el "Естественно, что и смена карт помогает не всегда — ведь противник видит, какие карты меняются местами, и тоже может изменить свой выбор."
    $ show_cards()
    show el normal pioneer at center with dspr
    $ show_cards()
    "Электроник перевёл дух."
    $ show_cards()
    show el smile pioneer at center with dspr
    $ show_cards()
    el "После того, как соперник украл карту, ходите вы."
    $ show_cards()
    show el laugh pioneer at center with dspr
    $ show_cards()
    el "Всё повторяется с той лишь разницей, что теперь вы крадёте карту."
    $ show_cards()
    el "Вы можете попробовать вернуть свою карту или украсть какую-то другую."
    $ show_cards()
    el "Ещё вы можете следить за поведением своего соперника и узнать, какую карту он не хочет терять."
    $ show_cards()
    show el serious pioneer at center with dspr
    $ show_cards()
    el "Здесь очень важно быть осмотрительным."
    $ show_cards()
    show el grin pioneer at center with dspr
    $ show_cards()
    el "Так что следите внимательнее и хорошенько думайте, какую карту взять, а какую отдать."
    $ show_cards()
    show el smile pioneer at center with dspr
    $ show_cards()
    el "Ну вот!.."
    $ show_cards()
    "Электроник наконец остановился."
    $ show_cards()
    show el normal pioneer at center with dspr
    $ show_cards()
    "Похоже, даже для него, привыкшего постоянно говорить, это была большая речь."
    $ show_cards()
    el "Всё понятно?"
    $ show_cards()
    "Но никто не отозвался."
    $ show_cards()
    "Даже Ульянка промолчала."
    $ show_cards()
    "Электроник слегка нахмурился."
    $ show_cards()
    el "Да ведь всё очень просто!"
    $ show_cards()
    "И снова с ним согласилась лишь тишина."
    $ show_cards()
    el "Ну хорошо..."
    $ show_cards()
    show el smile pioneer at center with dspr
    $ show_cards()
    el "Сначала попробуйте сами."
    $ show_cards()
    el "Это пока ещё будет не турнир, а пробная игра, чтобы вы разобрались."
    $ show_cards()
    el "А я объясню, если что-то будет непонятно."
    $ show_cards()
    hide el with dissolve
    $ show_cards()
    "И он вернулся к столу, оставив нас один на один со своей, я был уже в этом полностью уверен, безумной игрой."
    $ show_cards()
    me "Первый ход твой."
    $ show_cards()
    "Я, как мог, разложил карты поудобней."
    $ show_cards()
    "И Лена, смутившись ещё больше обычного, потянулась к моим картам..."
    return

label ii_demo_play_me_defend_1:
    $ show_cards()
    "Но тут её рука застыла в нерешительности."
    $ show_cards()
    un "Т-ты будешь?.."
    $ show_cards()
    th "Точно! Я же должен защищать свою карту!"
    $ show_cards()
    "Я вспомнил, что там говорил Электроник."
    $ show_cards()
    "Чтобы попытаться запутать соперника, можно поменять карты местами — и так два раза. А можно и не менять."
    $ show_cards()
    "Защищать мне эту карту или нет?"
    window hide
    return

label ii_demo_play_me_select_1:
    window show
    "И Лена может изменить свой выбор, взяв другую карту, а может и не менять."
    $ show_cards()
    "Понемногу всё становилось понятно!"
    $ show_cards()
    me "Теперь моя очередь."
    $ show_cards()
    "Я могу вернуть украденную карту или выбрать любую другую."
    if d2_walk == 0:
        $ show_cards()
        "К счастью, нам досталась колода с помеченными рубашками карт. А зная карты противника, легко выбрать нужную."
        $ show_cards()
        "Никогда бы не подумал, что буду жульничать на турнире, но, возможно, как раз это меня и спасёт."
    window hide
    return

label ii_demo_play_rival_defend:
    $ show_cards()
    window show
    "Лена может попробовать защитить свою карту."
    $ show_cards()
    "Но если я буду внимательным, то всё равно возьму ту, что выбрал с самого начала."
    window hide
    return

label ii_demo_play_after_loop:
    $ show_cards()
    window show
    "Получилось!"
    window hide
    $ ui.jumpsoutofcontext('d2_cards_tournament')

label d2_cards_tournament:
    scene bg int_dining_hall_day
    with dissolve
    $ persistent.AbcbCardsDemo = True
    window show
    "Электроник, до этого наблюдавший за нами, удовлетворённо кивнул."
    "Похоже, теперь мы действительно разобрались в его игре."
    show el smile pioneer at center with dissolve
    el "Итак, во время игры противники три раза обмениваются своими бойцами, а потом карты открываются."
    el "И мы смотрим, чья армия сильнее."
    hide el with dissolve
    "Электроник отошёл к своему ватману, а Ульяна не выдержала и закричала."
    show us laugh pioneer with dissolve
    us "Моя армия будет самой сильной!"
    us "Давайте уже играть!"
    hide us with dissolve
    "И начался собственно турнир."
    window hide

    if persistent.AbcbCardsWon3:
        menu:
            "Играть турнир":
                jump ii_un_play
            "Пропустить турнир (выиграть у Алисы)":
                jump ii_dv_play_win
            "Пропустить турнир (проиграть Алисе)":
                jump ii_dv_play_fail
            "Пропустить турнир (проиграть Ульяне)":
                jump ii_us_play_fail
            "Пропустить турнир (проиграть Лене)":
                jump ii_un_play_fail
    elif persistent.AbcbCardsWon2:
        menu:
            "Играть турнир":
                jump ii_un_play
            "Пропустить турнир (проиграть Алисе)":
                jump ii_dv_play_fail
            "Пропустить турнир (проиграть Ульяне)":
                jump ii_us_play_fail
            "Пропустить турнир (проиграть Лене)":
                jump ii_un_play_fail
    elif persistent.AbcbCardsWon1:
        menu:
            "Играть турнир":
                jump ii_un_play
            "Пропустить турнир (проиграть Ульяне)":
                jump ii_us_play_fail
            "Пропустить турнир (проиграть Лене)":
                jump ii_un_play_fail
    elif persistent.AbcbCardsFail:
        menu:
            "Играть турнир":
                jump ii_un_play
            "Пропустить турнир (проиграть Лене)":
                jump ii_un_play_fail

label ii_un_play:
    if d2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    python:
        dialogs = {
                        (0, 'win','jump'):'ii_un_play_win',
                        (0, 'fail','jump'):'ii_un_play_fail',
                        (0, 'draw','jump'):'ii_un_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalUn(un_avatar_set, u"Лена")
    jump cards_gameloop


label ii_un_play_fail:
    $ persistent.AbcbCardsFail = True
    $ d2_fail = 1
    jump d2_loser

label ii_un_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump ii_un_play

label ii_un_play_win:
    $ persistent.AbcbCardsWon1 = True
    scene bg int_dining_hall_day
    with dissolve
    show un normal pioneer at center with dissolve
    window show
    "Я победил!"
    "Впервые я понял, как трудно играть в игру, придуманную едва ли не вчера, да ещё и не тобой..."
    "Но я выиграл!"
    "Правда, радость победы немного омрачило то, что я выиграл у Лены."
    "Она и так казалась неуверенной в себе."
    "Теперь мне было даже неудобно взглянуть на неё."
    "Возможно, следовало всё-таки проиграть, чтобы повысить её самооценку?.."
    "Дать ей выиграть, хоть раз!"
    hide un with dissolve
    "Но на кону было нечто очень важное!"
    "Если Алиса расскажет всем..."
    "Расскажет всем..."
    "Я всё ещё никак не мог поверить, что она говорила это всерьёз!"
    th "Я лапал её?"
    "Как кто-то может поверить в такое?!"
    if d1_runaway:
        "Вспомнилось, как я при нескольких пионерах оттянул рубашку Двачевской, оголив её грудь..."
        th "А ведь и правда могут, если за Алису вступятся свидетели. Только самого преступления я не совершал!"
        th "Но вожатым будет всё равно."
    if (d1_dv_evening == True) or (d1_un_evening == True):
        "Я вот никак не мог..."
        th "Впрочем, из лагеря меня не выпрут, Ольга Дмитриевна уверена, что мои родители будто бы в командировке. Но моего положения это совсем не облегчит."
    show el smile far at center with dissolve
    "Электроник тем временем с гордостью объявил, что первый тур из семи окончен."
    "Он снова восседал за столом с ватманом и дорисовывал схему для второго тура."
    hide el with dissolve
    "Это заставило меня наконец поинтересоваться, кто же выиграл и проиграл в первом."
    "Но сначала я взглянул на Лену..."
    show un surprise pioneer at center with dissolve
    "Странно, но она вовсе не выглядела расстроенной!"
    "Она словно была чем-то удивлена."
    "В её глазах теперь впервые за долгое время, не было видно ни толики страха."
    "И я искренне был рад тому, что не огорчил Лену."
    hide un with dissolve
    "А она уже поднялась со стула и, как всегда скромно, заняла место с краю от зрителей."
    "Что ж, теперь я мог немного расслабиться и вздохнуть чуть свободнее..."
    show cg lvl_2_semen_win with dissolve
    "Но только чуть-чуть, потому что Алиса тоже прошла во второй тур!"
    hide cg lvl_2_semen_win with dissolve
    show dv smile pioneer at cleft with dissolve
    "Судя по её улыбке можно было решить, что игра с Мику не была для неё ни капельки сложной."
    hide dv with dissolve
    show mi happy pioneer at cright with dissolve
    "Но и Мику вовсе не грустила!"
    show mi grin pioneer far at cleft with dissolve
    "...Она уже что-то весело и беззаботно рассказывала кому-то из зрительниц."
    th "Ну хоть кто-то в этом турнире участвовал без всяких пари и обязательств — просто ради удовольствия!"
    hide mi with dissolve
    "Электроник закончил рисовать схему второго тура."
    show cg lvl_2_semen_win with dissolve
    "Судя по новой картинке, в него прошли..."
    th "Женя!"
    th "Неожиданно!"
    th "Как она умудрилась обыграть..."
    hide cg lvl_2_semen_win with dissolve
    "Я поискал Славю глазами."
    show sl smile2 pioneer far at cleft with dissolve
    show mt smile pioneer far at fleft with dissolve
    "Она отошла к Ольге Дмитриевне, и они о чём-то мирно говорили."
    "Казалось, Славя восприняла своё поражение как нечто должное."
    "По её спокойному лицу нельзя было даже предположить, что она только что проиграла."
    hide sl
    hide mt
    with dissolve
    "А Жене теперь предстояло играть с Алисой. Вот будет номер, если Двачевская продует ей!"
    th "Интересно, а кто сейчас будет моим соперником?"
    show us grin pioneer at center with dissolve
    "И тут же на стул напротив буквально свалилась Ульяна!"
    us "Хы!"
    "С улыбкой до ушей она уставилась на меня."
    us "Как это ты Лену обыграл?"
    show us smile pioneer at center with dspr
    "Она прищурилась."
    us "Жульничал, наверное?"
    if d2_walk == 0:
        "Кажется, я немного покраснел."
    else:
        pass
    me "Ничего я не жульничал!"
    me "Просто я умею играть в карты."
    th "Эх... Если б я не сказал этого Алисе, может, ничего бы и не было."
    "Два освободившихся стола заняли младшеотрядники."
    me "Постой-ка, а что ты делаешь в турнирной части старшего отряда? Разве ты не должна быть за другим столом?"
    show us surp1 pioneer at center with dspr
    us "Я хотела с Алисой в одной группе играть!"
    us "Пока ты где-то шлялся, я попросила Сыроежкина..."
    show us laugh pioneer at center with dspr
    us "Вернее, пригрозила ему, что буду каждый день ломиться к нему в кружок!"
    me "А ты как Шурика обыграла?"
    show us upset pioneer at center with dspr
    us "А!.."
    "Она махнула рукой, показывая, что это было легко."
    us "Сказала ему то же, что и Элу. Представляешь, и он повёлся."
    us "Но если вдруг захочется наведаться к ним..."
    show us grin pioneer at center with dspr
    "И она снова улыбнулась так широко, что мне стало немного неуютно."
    "Ульяна и не думала сдерживать обещания и учить правила!"
    "Она просто собиралась выиграть, любыми способами!"
    "И вот теперь мне надо было играть с ней."
    show us smile pioneer at center with dspr
    us "Кстати, чем бы тебя припугнуть?"
    me "Ты это меня спрашиваешь?.."
    "От такой наглости я даже поперхнулся."
    us "Ну конечно!"
    show us normal pioneer at center with dspr
    us "А кого мне ещё спрашивать?"
    "Что характерно, её удивление, похоже, неподдельное."
    us "Ты новенький, о тебе никто ничего не знает."
    show us smile pioneer at center with dspr
    "Тут она хитро прищурилась и понизила голос до шёпота."
    us "Разве что Олька говорит, что ты ночью сопишь, как барсук!"
    show us laugh pioneer at center with dspr
    "Она засмеялась."
    me "Что за бред?!"
    show us grin pioneer at center with dspr
    us "А ещё встаёшь во сне и ходишь, как лунатик."
    show us smile pioneer at center with dspr
    us "А ещё..."
    me "Неправда!"
    me "И не называй её Олькой. Ты ей в дочери годишься."
    show us normal pioneer at center with dspr
    "Я смутился от сказанного."
    th "Зачем я ляпнул эту банальность?!"
    "Но Ульяна совершенно серьёзно ответила."
    show us upset pioneer at center with dspr
    us "А она говорит, что не гожусь. Потому что я слишком много балуюсь."
    show us surp1 pioneer at center with dspr
    us "А я всего лишь немного!"
    us "Разве можно баловаться слишком много?!"
    "Я не нашёл, что ответить, но она тотчас же снова вспомнила о турнире."
    show us surp2 pioneer at center with dspr
    us "Проиграешь мне, ладно?"
    us "Ну пожа-а-алуйста!"
    "Она решила подлизаться ко мне и разыграть невинную девочку?"
    show us upset pioneer at center with dspr
    "На меня это произвело совсем противоположный эффект. Ульянка насупилась, раздумывая, как ещё можно выторговать дёгкую победу."
    if d2_us_dv_day:
        show us smile pioneer at center with dspr
        "Внезапно что-то пришло ей в голову."
        us "А хочешь, я тебе кое-что покажу?"
        us "Ты только проиграй!"
        "И не дожидаясь ответа, она полезла рукой себе под рубашку..."
        show us grin pioneer at center with dspr
        us "Такого ты ещё не видел!"
        me "!.."
        th "Что же мне это напоминает?"
        show us smile pioneer at center with dspr
        th "Да они с Алисой вместе живут! А я-то гадаю, откуда такие приёмчики взялись?"
        "Если быть честным к самому себе, то Ульяне удалось на миг вызвать у меня мысли, как я после турнира наедине с ней говорю: «Ну давай, показывай, что у тебя там! И {i}там{/i} тоже...»"
        if (d2_no_shame == False):
            hide us with dissolve
            "Со стыдом я уставился себе под ноги, раздумывая, не сообщить ли Ульяне, что пол такой же плоский — разница небольшая, и этим меня не купить?"
            show us smile pioneer at center with dspr
        us "Семён! Гляди!.."
        "Я на автомате поднял голову, когда девчонка обеими руками взялась за края рубашки, вытянутые из-за пояса юбки с ремнём."
        show us grin pioneer at center with dspr
        us "Это понедельник..."
        "Ульяна потянула белые уголки рубашки на себя и скрутила их, оголив живот."
        show us smile pioneer at center with dspr
        us "Вторник!.."
        "Она приподняла рубашку ещё чуть выше."
        th "Б-же, что она собирается делать?!"
        th "Здесь же целый зал народа!"
        "Я должен был прошипеть ей: «Не тут! Не сейчас!»"
    "Меня спас Электроник, который громко объявил о начале второго тура, и к играющим снова подтянулись зрители."
    show us dontlike pioneer at center with dspr
    "Ульянка с неохотой облокотилась на стол, словно ничего не произошло, а я принялся раздавать карты, радуясь, что у меня есть, чем занять руки..."
    hide us with dissolve
    window hide

label ii_us_play:
    if d2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    python:
        dialogs = {
                        (3, 'me_defend_2','call'):'ii_us_play_me_defend_2',
                        (2, 'me_defend_2','call'):'ii_us_play_me_defend_2',
                        (1, 'me_defend_2','call'):'ii_us_play_me_defend_2',
                        (0, 'win','jump'):'ii_us_play_win',
                        (0, 'fail','jump'):'ii_us_play_fail',
                        (0, 'draw','jump'):'ii_us_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalDv(us_avatar_set, u"Ульяна")
    jump cards_gameloop

label ii_us_play_me_defend_2:
    $ show_cards()
    window show
    us "Эй, не мешай карты — это меня путает!"
    $ show_cards()
    me "М-м-м..."
    window hide
    return

label ii_us_play_fail:
    $ persistent.AbcbCardsWon1 = True
    $ d2_fail = 2
    jump d2_loser

label ii_us_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump ii_us_play

label ii_us_play_win:
    scene bg int_dining_hall_day
    with dissolve
    show us angry pioneer at center with dissolve
    window show
    us "Эй! Так не честно!"
    us "Ты должен был поддаться и проиграть!"
    show us dontlike pioneer at center with dspr
    "От недовольства она надула щёки и была похожа сейчас на колобка. Я едва смог сдержать смех."
    show us surp2 pioneer at center with dspr
    us "Давай переиграем, только ты теперь поддавайся, слышишь?!"
    "Но её слышал не только я, а весь зал и Электроник в том числе."
    show el serious pioneer far at right with dissolve
    el "Никаких переигровок!"
    hide el with dissolve
    show us fear pioneer at center with dspr
    "Но Ульяна не обратила на него ни малейшего внимания."
    us "Ты должен проиграть!"
    us "Должен!!!"
    "Похоже, вторая игра будет более напряжённой."
    hide us with dspr
    window hide

label ii_us2_play:
    if d2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    python:
        dialogs = {
                        (0, 'win','jump'):'ii_us2_play_win',
                        (0, 'fail','jump'):'ii_us2_play_fail',
                        (0, 'draw','jump'):'ii_us2_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalDv(us_avatar_set, u"Снова Ульяна")
    jump cards_gameloop

label ii_us2_play_fail:
    $ persistent.AbcbCardsWon1 = True
    $ d2_fail = 2
    jump d2_loser

label ii_us2_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump ii_us2_play

label ii_us2_play_win:
    $ persistent.AbcbCardsWon2 = True
    scene bg int_dining_hall_day
    with dissolve
    show us dontlike pioneer with dissolve
    window show
    th "Ура!"
    "Но выиграть у Ульяны оказалось легче, чем пережить последствия этой победы..."
    show us angry pioneer at center with dspr
    "Потому что она вдруг перегнулась через стол и принялась колотить меня своими маленькими кулачками."
    "И довольно сильно!"
    us "Ты ведь обещал проиграть!"
    "Она была так обижена, будто я её предал!"
    show us dontlike pioneer at center with dspr
    us "Обещал! Я ведь тебя просила!"
    th "Интересно, она понимает, что только что призналась в жульничестве?"
    if d2_walk == 0:
        "Впрочем, я и сам жульничал, но..."
    else:
        pass
    me "Ничего я не обещал!"
    show us surp2 pioneer at center with dspr
    "С трудом, но мне удалось вставить пару слов в перерыве между ударами."
    show us angry pioneer at center with dspr
    "И мне было не ясно только одно."
    th "Почему меня никто не спасает?!"
    "Где Ольга Дмитриевна, когда она так нужна?!"
    "Но, кажется, всем пионерам было настолько весело наблюдать, как меня убивают, что никто и не думал прекращать развлечение."
    #show bt
    "Заслышав вопли Ульяны, к нам подлетела её вожатая — Инга Максимовна — и буквально схватив девчонку со стола, поставила её на пол."
    bt "А ну перестань! Кто так себя ведёт? Сейчас отведу в баню и..."
    "К тому моменту, хоть я и отбивался от Ульяны, десяток случайных синяков на руках и голове она успела оставить."
    "Да и Ульяна явно устала лупить меня."
    show us dontlike pioneer with dspr
    "Но она всё ещё была, мягко говоря, недовольна."
    us "У-у-у!"
    "Она свирепо топнула ножкой, как только вырвалась из рук Инги Максимовны."
    us "Ладно-ладно!"
    us "Я это тебе ещё припомню."
    hide us with dissolve
    #hide bt
    "И с этими словами она резко развернулась и скрылась в толпе зрителей."
    show dv smile pioneer at center with dissolve
    "Я же обнаружил себя сидящим напротив Алисы, занявшей место Ульянки."
    "Близилась предпоследняя, если мне как-то удастся обыграть Двачевскую, битва."
    if d2_walk == 0:
        show dv normal pioneer at center with dspr
        "Но прежде, чем она началась, Алиса, делая вид, что тасует колоду, с подозрением оглядела карты, которыми мы играли."
        th "Неужели..."
        "По спине пробежал холодок."
        show dv smile pioneer at center with dspr
        "А она слегка наклонилась ко мне и, лукаво улыбаясь, спросила шёпотом — так, что слышать её мог только я."
        dv "Все пометил, да?"
        show dv grin pioneer at center with dspr
        dv "Предусмотрительный..."
        th "Она поняла, что я жульничал!!!"
        "Не знаю, что стало с моим лицом в ту секунду. Я то ли покраснел, то ли позеленел от страха."
        "Если сейчас она встанет и скажет всем..."
        "Это будет ужасно!!!"
        "Невыносимо!!!"
        "Кошмарно!!!"
        show dv smile pioneer at center with dspr
        "Но Алиса, кажется, и не думала выдавать меня..."
        "Она улыбалась!"
        dv "Надеялся и меня так обыграть?"
        "И я, проклиная свою честность, тоже ответил шёпотом."
        me "Да."
        show dv normal pioneer at center with dspr
        "Двачевская фыркнула, но совсем беззлобно."
        dv "Даже не думай об этом."
        "Незаметно для зрителей она достала из кармана совершенно новую колоду карт и поменяла её местами с помеченной мной."
        dv "Играть будем моими!"
        show dv smile pioneer at center with dspr
        "Она довольно улыбнулась."
        dv "Я тоже предусмотрительная."
        "Игра началась."
        hide dv with dspr
    else:
        pass
    window hide

label ii_dv_play:
    $ INVISIBLE = False
    python:
        dialogs = {
                        (0, 'win','jump'):'ii_dv_play_win',
                        (0, 'fail','jump'):'ii_dv_play_fail',
                        (0, 'draw','jump'):'ii_dv_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalDv(dv_avatar_set, u"Алиса")
    jump cards_gameloop

label ii_dv_play_fail:
    $ persistent.AbcbCardsWon2 = True
    $ d2_fail = 3
    jump d2_loser

label ii_dv_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump ii_dv_play

label ii_dv_play_win:
    $ persistent.AbcbCardsWon3 = True
    stop music fadeout 1
    scene bg int_dining_hall_day
    with dissolve
    play music music_list["heather"] fadein 1
    show dv surprise pioneer with dissolve
    window show
    "Я выиграл!"
    th "Выиграл?"
    th "Выиграл!!!"
    show dv normal pioneer at center with dissolve
    "Ещё полтора часа назад я не мог и представить себя таким счастливым!"
    "Я победно смотрел на Алису, ещё не веря до конца в свою удачу."
    "Словно и не было этих часов переживаний и напряжения."
    "Я стал лёгким, как пёрышко."
    "Я как будто научился летать!"
    "Я выиграл пари!!!"
    "Теперь девочка была обязана сдержать слово и не говорить вожатым о той безумной выдумке..." 
    th "Остаётся молиться, чтобы она не сделала так в отместку за проигрыш — этого можно было ожидать."
    "Я снова глянул на Двачевскую, но почти без опасений за дальнейшие последствия."
    "Сложно было что-то понять по её выражению лица, но..."
    show dv smile pioneer close at cleft with dspr
    "Алиса наконец поднялась со своего места и, с улыбкой проходя мимо меня, хлопнула по плечу."
    dv "Поздравляю!"
    "И от этих слов мне стало так радостно!"
    "Всё перемешалось в голове."
    th "Я выиграл Алису!!!{w} Тьфу, то есть, выиграл {i}у{/i} Алисы, конечно!" 
    th "Если б картами можно было выигрывать девушек, то я бы не пропускал ни одного турнира каждый день!"
    hide dv with dissolve
    show cg lvl_4_semen_win with dissolve
    "Электроник объявил меня победителем в отборочных турах от старшего отряда."
    "Несколько минут ожидания, когда закончится последний тур у младших, пролетели для меня в один момент."
    hide cg lvl_4_semen_win with dissolve
    "Алису сменил какой-то пионер из числа младших, и теперь мне надо было биться за честь своего отряда и некий обещанный Сыроежкиным приз."
    "Зрители — пионеры и вожатые, столпились около нас."
    "Я был в таком приподнятом настроении, что разбил соперника в финальном туре почти не глядя."
    th "Разве после Алисы будет сложно кого-то обыграть? На кой ляд мне честь отряда, если я победил Двачевскую?"
    "Я не принимал в расчёт удачу, я просто испытывал торжество."
    "А вокруг все уже поздравляли меня с победой, и Электроник писал моё имя в своей таблице!"
    "Моё имя!"
    "Я выиграл турнир!"
    window hide
    $ d2_cards_win = True
    stop music fadeout 3
    jump d2_event_prize
    
label d2_loser:
    stop music fadeout 1
    scene bg int_dining_hall_day
    with dissolve
    play music music_list["drown"] fadein 1
    #Здесь можно сделать CG или чиби-CG, где у Семёна Кайдзи-фейс: крупный нос и реки горючих слёз на щеках.
    "Я проиграл!"
    "Проиграл..."
    th "Всё кончено..."
    if (d2_walk == 0) and (d2_fail != 3):
        "И даже меченые карты не смогли меня спасти."
    else:
        pass
    "Я встал и на ватных, подкашивающихся ногах пошёл куда-то мимо зрителей, стараясь ни на кого не смотреть."
    "А особенно — на Алису..."
    "Но я чувствовал, что она наблюдает за мной!"
    "Её взгляд буквально прожигал мою спину."
    "Я не знал, что мне делать." 
    "Каждый мой шаг словно разносился гулом по столовой в тишине."
    th "Алиса ведь не станет говорить, что я лапал её, правда?!"
    "Но я уже ни на что не мог надеяться."
    "Разве что..."
    if d2_fail == 1:
        "Внезапно надежда вернулась ко мне!"
        "Алиса ведь тоже могла проиграть!"
        "Я развернулся, чтобы увидеть турнирную таблицу."
        "Первый раунд был завершён, и Электроник как раз заканчивал дописывать новые пары."
        "Вот он отошёл и..."
        show cg lvl_2_lena_win with dissolve
        "У меня опустились руки."
        "Алиса, конечно же, обыграла Мику, а теперь готовилась померяться силами с Женей."
        "Я посмотрел на таблицу внимательнее."
        "На секунду мне стало жаль Славю и Мику, проигравших в первом туре."
        "Но сами они, казалось, нисколько не были расстроены своим поражением и мирно стояли в толпе зрителей."
        "И только Шурик, проигравший Ульяне, был слегка подавлен."
        th "Видимо, намучился с ней. Однако не время переживать о Шурике."
        "Я снова сосредоточил всё своё внимание на предстоящем поединке Алисы и Жени."
        "И болел я, что удивительно, за ту черезмерно строгую активистку из библиотеки."
        "Потому что если Алиса проиграет..."
        "И я расплылся в улыбке, представив поражение Алисы, но вовремя спохватился — ещё ничего не было решено!"
        "Не стоило искушать судьбу, нужно было дождаться окончания второго тура, который как раз стартовал."
        hide cg lvl_2_lena_win
        scene bg int_dining_hall_day
        with dissolve
        "Но не прошло и десяти минут, как Женя поднялась из-за стола, признавая своё поражение."
        "Алиса снова победила!"
        "И теперь у меня оставалась только призрачная надежда, что Ульянка, обыгравшая и Лену тоже, сможет спасти меня от печальной участи."
        "................"
        "А ещё через пятнадцать минут умерла и эта надежда."
        "Зато нашёлся победитель турнира."
        window hide
        jump d2_loser2

    if d2_fail == 2:
        "У меня ещё была крохотная надежда, что Ульяне или удастся обыграть Алису."
        "................"
        "Но через пятнадцать минут она испарилась."
        jump d2_loser2

    if d2_fail == 3:
        "...только на чудо."
        th "Но я же не верю в чудо, поэтому..."
        jump d2_loser2

label d2_loser2:
    show dv smile pioneer at center with dissolve
    window show
    "Алиса победила и Ульяну, и паренька из младшего отряда. Все наперебой принялись её поздравлять."
    "Электроник взмахнул руками, ознаменовав окончание турнира, и дописал в таблицу её имя."
    "Алиса выиграла..."
    "А я проиграл и турнир, и пари."
    th "Что же будет?!"
    stop music fadeout 2
    "Я посмотрел на Алису. Казалось, на её лице не было и следа радости."
    play music music_list["awakening_power"] fadein 1
    show dv normal pioneer at center with dspr
    "С равнодушием, лениво бросив на меня прищуренный взгляд, Алиса..."
    show mt normal pioneer far at cleft behind dv with dspr
    show dv normal pioneer far at fleft with dissolve
    "Пошла прямо к Ольге Дмитриевне, стоявшей всё это время неподалёку от пионеров!"
    th "Неужели, она сделает это?!!"
    "Всё во мне словно перевернулось!"
    "Я бросился вслед за ней, но было уже поздно."
    show mt surprise pioneer far at center behind dv
    show dv smile pioneer far at cleft
    with dspr
    "Алиса стояла рядом с Ольгой Дмитриевной и что-то горячо шептала ей на ухо, весьма лукаво поглядывая на меня!"
    "Этого я не мог допустить!"
    "С громким криком я подлетел к ним."
    show mt surprise pioneer at center behind dv
    show dv smile pioneer at cleft
    with dspr
    me "Это неправда!"
    me "Всё, что она говорит обо мне — НЕ-ПРАВ-ДА!"
    show mt normal pioneer at center behind dv
    show dv smile pioneer at cleft
    with dspr
    "Ольга Дмитриевна спокойно посмотрела на меня."
    mt "А по-моему, всё верно."
    show mt grin pioneer at center behind dv with dspr
    mt "Ты совсем не умеешь играть в карты."
    "Такого позора я ещё никогда не испытывал..."
    window hide
    stop music fadeout 2
    jump d2_event_prize

label d2_event_prize:
    
    scene black
    with dissolve
    show screen central_text("День 2 — Время призов")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    with dissolve
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset
    with dissolve2
    play music music_list["smooth_machine"] fadein 2
    show mt smile pioneer at cright with dissolve
    window show
    mt "А теперь, самая приятная часть турнира для всех, кто присутствовал..."
    show el smile pioneer at cleft with dissolve
    el "Раздача призов!"
    all "Да-а-а!!!"
    "Тут дети были единодушны в возгласе. Однако младшие не так сильно радовались: соревнование они проиграли."
    show mt grin pioneer at cright with dspr
    mt "У нас как раз должен быть вечерний полдник, так что призы не простые, а вкусные!" 
    show mt smile pioneer at cright with dspr
    mt "Не булочки с кефиром, но кое-что послаще. Поэтому, скорей приводите столовую в порядок!"
    show mt smile pioneer at center with dspr
    show sl smile2 pioneer at cright
    show mz normal glasses pioneer at fright
    with dissolve
    $ renpy.pause(0.5, hard=True)
    hide mt
    hide sl
    hide mz
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show sh smile pioneer at cright with dissolve
    "Вместе с вожатой, Славя и Женя пошли на кухню за теми самыми призами, а Электроник с Шуриком и кучей малышей принялись расставлять столы, как было раньше."
    hide sh
    hide el
    with dissolve
    "..."
    play ambience ambience_dining_hall_full fadein 3
    "......"
    scene bg int_dining_hall_people_sunset
    with dissolve2
    "Очень скоро все сидели рядом друг с другом."
    "И только я ещё не мог поверить в то, что со мной произошло."
    stop ambience fadeout 1
    stop music fadeout 2
    play ambience ambience_medium_crowd_indoors_1 fadein 2
    "Атмосфера в столовой становилась всё более напряжённой — все чего-то ждали."
    show mt neutral pioneer at center with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    "Наконец, вышла Ольга Дмитриевна."
    show mt smile pioneer at center with dissolve
    "Она выглядела очень важной сейчас, но и довольной тоже."
    mt "Я очень рада, что сегодня вы все показали себя с лучшей стороны!"
    mt "Сами организовали и провели карточный турнир."
    show mt laugh pioneer at center with dspr
    mt "Молодцы!"
    #$ volume (0.7,'sound')
    play sound sfx_concert_applause fadein 1
    "Все дружно захлопали в ладоши."
    stop sound fadeout 1
    #$ volume (1.0,'sound')
    show mt smile pioneer at cright with dspr
    show el smile pioneer at cleft with dissolve
    "Теперь Ольга Дмитриевна обратилась к нам, глядя на меня и Сыроежкина."
    mt "Поэтому в награду за ваши старания, отряд победителя сегодняшнего турнира получает этот приз!"
    hide el with dissolve
    th "Интересно, мне одному послышалось: «за ваши страдания»?"
    show mt smile pioneer at left with dspr
    show sl smile pioneer at right
    show mz normal pioneer at center
    with dissolve
    "И тут в столовую Женя и Славя вынесли огромный торт!"
    "Малыши, конечно, закричали. Скорее всего потому, что торт достался не им."
    "Но у вожатой и на это нашёлся ответ."
    mt "А те, кто не участвовал или проиграл, получат утешительный приз — конфеты!"
    "Вот теперь радовались все."
    hide sl
    hide mz
    hide mt
    with dissolve
    "Кто-то уже побежал за ножом — резать торт. Повара успели заготовить всем стаканы чая на подносах..."
    show dv smile pioneer at cleft
    show un shy pioneer at cright
    with dissolve
    "Лена, почему-то со смущением косясь на Алису, принесла с ней блюдца и бумагу."
    hide dv
    hide un
    with dissolve
    show sl smile pioneer at cright with dissolve
    "Вскоре Славя разделила торт на восемь частей, и каждый, кто играл в турах старшего отряда, кроме Ульяны, стал перекладывать квадратиками резаной бумаги вместо салфеток свой кусочек на блюдце."
    hide sl with dissolve
    show el laugh pioneer at cright with dissolve
    el "...А вот тот, пожалуйста, мне!.."
    stop music fadeout 3
    show us dontlike pioneer far at left with dissolve
    "Но тут Ульяна, которая сидела неподалёку после своего поражения хмурая, как грозовая туча, вдруг с громким криком подбежала и..."
    play music music_list["always_ready"] fadein 0
    #Текущий cg временный. Возможно, его придётся обновлять по окончании работ над скриптом.
    scene cg d2_cake with dissolve
    with vpunch
    "Впилась в торт прямо зубами!"
    "Ольга Дмитриевна пыталась оттащить её, но Ульянка вырывалась и продолжала кусать и кусать торт!"
    "Изредка она ещё умудрялась что-то сказать, но с набитым ртом у неё выходили только еле понятные выкрики."
    us "Я долфна быфа выифрать!!!"
    us "Пофему я пфоигфала?!"
    "Остальное уже совсем нельзя было разобрать."
    "Наконец Ольге Дмитриевне удалось оттащить громко сопящую Ульяну подальше от половины торта со следами укусов по краю."
    mt "Как ты себя ведёшь? Угомонись!"
    "Но Ульянка была расстроена вовсе не из-за этого."
    "Она громко топнула ногой и выпалила всё, что думала."
    us "Это всё потому, что мне плохо поддавались!"
    us "Я должна была выиграть!"
    us "И торт мой!!!"
    scene bg int_dining_hall_sunset
    show mt angry pioneer at center
    show us angry pioneer at cright
    with dissolve
    show us angry pioneer:
        linear 1.0 xpos 1.2
    "С этими словами она вырвалась из рук Ольги Дмитриевны и, схватив в пригоршню ближайший кусок оставшегося торта, бросилась бежать!"
    hide us with dspr
    show mt surprise pioneer at cleft
    show el shocked pioneer at cright
    with dspr
    "Электроник вскочил с места, хватаясь за голову."
    el "Это же моё!.. Как организатору!.."
    show el sad pioneer at cright with dspr
    "Он с горестным вздохом опустился на стул, когда Ульяны след простыл."
    "Остальные стояли и не знали, что делать."
    show mt smile pioneer at cleft with dspr
    "Наконец, Ольга Дмитревна улыбнулась, и тут уж все засмеялись в голос, кроме Электроника."
    mt "Ну, Ульяна...{w} А тебе, Сыроежкин, я тоже дам конфет к чаю."
    "А я всё думал, как же поступить мне."
    th "Погнаться за Ульянкой?"
    window hide
    menu:
        "Конечно! Торт ещё можно спасти!":
            jump d2_us_try
        "Гнаться бессмысленно, но я могу всё исправить":
            "И правда, зачем мне бежать за ней?"
            jump d2_late_supper

label d2_late_supper:
    
    stop music fadeout 2
    scene bg int_dining_hall_sunset
    with dissolve
    play music music_list["everyday_theme"] fadein 1
    show mt grin pioneer at left with dissolve
    window show
    "Ольга Дмитриевна ещё поворчала добродушно, что завтра Ульяну ждёт кое-что особенное за столь некрасивый поступок."
    hide mt with dissolve
    show sl smile2 pioneer close at cright with dissolve
    sl "Вот..."
    "Славя помогла Мику, передав ей один из оставшихся кусочков, надкушенных Ульяной."
    show sl smile pioneer close at cright with dspr
    sl "А это тебе..."
    "И она с улыбкой протянула мне торт на бумажной салфетке."
    "Я кивнул, благодаря Славю."
    hide sl with dissolve
    "Мне повезло: он был покусан всего лишь чуть-чуть."
    th "Надо восполнить нервные клетки с калориями, нещадно потраченные из-за переживаний на турнире."
    th "Но не я один их потратил."
    "Я будто очнулся от потрясения."
    me "Сыроега, держи."
    show el surprise pioneer close at cleft with dissolve
    "Я пододвинул к нему блюдце с куском торта."
    el "Но ведь... Слушай, давай пополам?"
    show el smile pioneer close at cleft with dspr
    me "Да, можно и так."
    "Я разделил его на две части, и обрадовавшийся Электроник взял себе половинку."
    show el laugh pioneer close at cleft with dspr
    el "Большое-пребольшое спасибо, Семён!"
    hide el with dissolve
    $ fp_el_sh = fp_el_sh + 1
    "......"
    show mt normal pioneer at center with dissolve
    "После этого Ольга Дмитриевна оглядела нас всех и грозно объявила."
    mt "Что ж, оставляю вас до отбоя, возвращайтесь к себе не позже полдвенадцатого."
    show mt smile pioneer at center with dspr
    "Я мельком посмотрел в окно. Мы довольно долго играли, в лагере почти стемнело."
    mt "Торт с конфетками можно доесть и на улице."
    show mt angry pioneer at center with dspr
    mt "Но если увижу хоть одну бумажку на территории лагеря..."
    "Строгий взгляд Ольги Дмитриевны не сулил ничего хорошего тому, кто будет в этом замечен."
    th "Врагу не пожелаешь!"
    show dv normal pioneer at fright with dissolve
    $ renpy.pause(0.5, hard=True)
    hide dv with dissolve
    "Алиса немедленно покинула столовую с недоеденным кусочком торта."
    show mt smile pioneer far at fleft with dissolve
    #show bt
    "Вожатая отошла к Инге Максимовне.{w} Они собрали вокруг себя стайку детей из младшего отряда. По обрывкам фраз, доносившихся до меня, можно было понять, что этих пионеров по расписанию ожидают чистка зубов и отход ко сну."
    hide mt with dissolve
    #hide bt
    "На этом посиделки за чаем закончилсь."
    "Честно говоря, я был даже рад."
    "Сейчас, после всех случившихся событий, я просто хотел побыть один."
    "Чтобы подумать о том, что произошло за этот долгий-долгий день."
    "И отдохнуть от приключений."
    "Пионеры постепенно уходили из столовой, и я, повинуясь всеобщему движению, вышел на крыльцо, держа бумажной салфеткой небольшой кусочек торта в руке."
    window hide
    stop music fadeout 2
    jump d2_after_event
    
label d2_after_event:

    scene black
    with dissolve
    show screen central_text("День 2 — Вечер в лагере")
    $ renpy.pause(99, hard=False)
    hide screen central_text

    if (d2_us_try_fail == False):
        scene bg ext_dining_hall_near_sunset
        with dissolve
        play music music_list["you_won_t_let_me_down"] fadein 1
        window show
        "Я остановился у перил, обдумывая, чем бы занять грядущий вечер."
        "Торт был настолько вкусным, что я прерывался от размышлений и с удовольствием откусывал нежную кремовую начинку."
        el_voice "Ну, как тебе турнир?"
        show el smile pioneer close at right with dissolve
        show sh normal pioneer close at left with dissolve
        "Я обернулся на голос. Шурик и Сыроежкин, как видно, тоже решили не засиживаться со всеми в столовой и присоединились ко мне."
        if d2_cards_win:
            me "Было здорово! А что ещё можно сказать? Побеждать всегда приятно."
            show sh normal_smile pioneer close at left with dspr
            sh "Поздравляю, кстати!"
            me "Спасибо! Приз — объедение."
        else:
            "В памяти вслыла картинка: я подбегаю к Двачевской и вожатой с криком «Это неправда!» на всю столовую."
            me "Душераздирающе, в самом плохом смысле. Сегодняшний проигрыш я никогда не забуду."
            me "Зато приз объедение."
        show el grin pioneer close at right with dspr
        el "Не то слово!"
        show el smile pioneer close at right with dspr
        el "Ум-м!"
        "Электроник в один присест доел свой кусочек. Бумажку он выкинул только после того, как нашёл ведро, куда её можно бросить."
    
    if d2_us_try_fail:
        scene bg ext_dining_hall_away_sunset
        with dissolve
        play music music_list["you_won_t_let_me_down"] fadein 1
        window show
        "Я вернулся к столовой и припаркованной у крыльца «Волге»."
        #show bt
        show mt smile pioneer far at cleft with dissolve
        "Младшие пионеры одной колонной выходили на улицу, процессию возглавляла их вожатая Инга Максимовна, а Ольга Дмитриевна шла рядом."
        "Я сообразил, что у них скоро отбой по расписанию, и что детей вели на пятиминутку гигиены перед сном."
        #hide bt
        hide mt with dissolve
        scene bg ext_dining_hall_away_sunset
        with dissolve
        show el smile pioneer at cright with dissolve
        show sh normal pioneer at cleft with dissolve
        "Тем временем на крыльце показались Электроник с Шуриком."
        show el laugh pioneer at cright with dspr
        el "Э, Семён! Иди сюда!{w} Догнал Ульянку?"
        show el normal pioneer close at right with dspr
        show sh normal pioneer close at left with dissolve
        "Он перепрыгнул через перильца и уселся на лавочку, а Шурик предпочёл спуститься по ступенькам, как все нормальные люди."
        me "Не, она спряталась где-то, словно исчезла."
        me "Как чувствовал: бегать за Ульяной — дохлый номер."
        if d1_us_chase:
            th "Хотя вчера мне повезло."
        show el smile pioneer close at right with dspr
        el "Шурик со мной тортом поделился, а вот ты остался в накладе.{w} На!"
        "Он вынул из кармана пять конфет в ярких фантиках и отдал их мне."
        me "О, спасибо!.."
        "Честно говоря, я не ожидал от Электроника подобной щедрости. В некотором смысле за мной теперь должок ему."

    if tech_club:
        me "Между прочим, Эл, хоть ты и поборник штампов, сходство твоей игры с покером минимально. Вообще, она мне показалась необычной, даже слишком."
        me "По-моему, не все пионеры легко усвоили правила."
        show el normal pioneer close at right with dspr
        el "Да, я заметил это. Они оказались не готовы к такому. Пока тебя не было, мы еле набрали желающих, иначе бы вышло так, будто мы разыгрываем приз между собой."
        me "Значит, ты ещё тот оригинал, Сыроежкин."
        show el surprise pioneer close at right with dspr
        sh "Вот видишь, как бы ты ни копировал узнаваемое, рано или поздно захочешь прийти к чему-то своему."
        show el shocked pioneer close at right with dspr
        "Электроник слегка покраснел и развёл руками."
        el "Да бросьте вы меня хвалить! Сама по себе идея с вытягиванием карт совсем не новая. Знаете такую игру: из колоды убирают бубновую даму, тянут друг у друга карты, пары выбрасывают. Кто с пиковой дамой остался, проиграл. Вот это оно."
        show el normal pioneer close at right with dspr
        me "Ну не, больше похоже, чем на покер, но всё равно другое."
        sh "Совмещать тоже надо уметь. Не всем так удаётся."
        show el smile pioneer close at right with dspr
        "Хотя Сыроежкин и отмахивался от нас, было видно, что он страшно доволен тем, что смог организовать вечернее мероприятие, и пусть не все пионеры, а только мы оценили его выдумку."
    el "Что сейчас будешь делать?"
    me "Хм... Я собирался послоняться немного по лагерю. У меня ещё в палате есть дела."
    "Перебросившись ещё парой слов с каждым, я попрощался с кибернетиками."
    window hide
    stop music fadeout 2
    jump d2_pre_evening_slots
    
label d2_us_try:
    
    "Я, не слыша никого, пулей выбежал на крыльцо."
    scene bg ext_dining_hall_near_sunset
    with fade
    if d1_us_chase:
        "На выходе из столовую я ощутил странное чувство дежавю."
    else:
        th "Во что бы то ни стало, я должен догнать её!"
    scene bg ext_dining_hall_away_sunset
    with fade
    if d1_us_chase:
        "Так же, как и вчера, я гнался за Ульяной, только на этот раз всё было по-другому."
        "Передо мной мелькала белая пионерская форма, а не та красная майка, и когда я уже приготовился дать кросс до первого корпуса кружков, Ульяна побежала совсем в другую сторону..."
    else:
        "Не спуская глаз с девчонки, я нёсся изо всех сил. Удивительно, как она смогла оторваться так далеко даже не в кедах, а в обычных туфлях-сандалях!"
    scene bg ext_square_sunset
    with fade
    "Она бежала между прачечной и админцентром, мимо умывальников — к лесу."
    scene bg ext_path_sunset
    with fade
    if d1_us_chase:
        "И, похоже, сегодня Ульяне удалось скрыться — она нырнула в заросли справа, сойдя с тропы."
    else:
        "И, похоже, Ульяне удалось скрыться — она нырнула в заросли справа, сойдя с тропы."
    "Так что я сразу же упустил её из виду."
    play sound_loop sfx_run_forest fadein 1
    "Но о том, чтобы оставить погоню не могло быть и речи!"
    "Где-то впереди трещали ветки, изредка я умудрялся заметить девчонку и снова терял её." 
    scene bg ext_path_sunset
    with fade
    #$renpy.music.set_volume (0.6, channel=5)
    #play music sfx_run_forest fadein 2 channel 5
    "Я уже слишком далеко зашёл и рисковал потеряться. А Ульянка (я надеялся на это) наверняка знала дорогу обратно."
    window hide
    stop sound_loop fadeout 1
    stop music fadeout 1 #channel 5
    if (lp_us == 1) or (d2_us_dv_day == True):
        scene black
        with dissolve
        show screen central_text("День 2 — Наша сказка")
        $ renpy.pause(99, hard=False)
        hide screen central_text
        scene bg ext_playground_sunset
    with dissolve
    play music music_list["smooth_machine"] fadein 1
    window show
    "Через минуту я, тяжело дыша, вышел к спортивным площадкам. Что удивительно, я даже не осознавал, куда мы бежали." 
    "Выходит, едва ли не круг по лагерю намотали."
    "Я огляделся."
    "Но вокруг не было ни души!"
    th "Куда она делась?!"
    "Я отстал буквально на шесть-семь метров, но её уже не было!"
    th "Как будто улетела..." 
    "Я постоял пару минут, ожидая, не покажется ли она откуда-нибудь..."
    "Но спрятаться на голом футбольном поле было абсолютно негде. Разве что за площадкой для бадминтона, но Ульяна всё равно не успела бы добежать туда — я бы заметил её." 
    if (lp_us == 1) or (d2_us_dv_day == True):
        jump d2_us_evening_slot
    "Так что мне поневоле пришлось смириться."
    "Я ещё погрозил кулаком на прощание куда-то в кусты, где она могла бы сидеть, и побрёл к столовой, даром, что идти до неё было совсем немного."
    window hide
    stop music fadeout 2
    $ d2_us_try_fail = True
    jump d2_after_event


label d2_pre_evening_slots:

    scene bg ext_square_sunset
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    window show
    "Сегодня вечерняя площадь оказалась совсем пустой, все пионеры куда-то разбежались..."
    th "А, ну да, младшие сейчас будут ложиться спать."
    "В раздумьях я остановился в центре площади и в очередной раз поразился внушительному монументу."
    "С ужина памятник никуда не ушёл и всё так же поправлял очки."
    th "Как он только не устал, бедняга."
    if (d2_us_try_fail == False):
        "Может, разделить с ним тортик?"
    else:
        "Может, разделить с ним конфеты?"
    menu:
        "Почему нет?":
            th "М-м-м... Вкуснотища!"
            "Я протянул руку перед собой, точно предлагая статуе взять сладость."
            me "Будешь?"
            "Генда не ответил."
            me "Как хочешь, мне больше достанется."
            th "Не всегда же молчание — знак согласия..."
            me "Твоё здоровье, Генда!"
            "..."
        "Обойдётся":
            "Погуляю-ка я ещё."
    if (d2_us_try_fail == False):
        "Бумажку-салфетку я скомкал и сунул в карман, а сам отошёл всполоснуть руки в умывальнике рядом со скамейками."
    else:
        "Фантик я скомкал и сунул в карман, а сам отошёл всполоснуть руки в умывальнике рядом со скамейками."
    if (d2_dv_fight == False):
        "Я вспомнил о заначке, сделанной во время обхода кружков."
        th "Поел сладкого, теперь можно и покурить."
        scene bg ext_house_of_mt_sunset
        with fade
        "Бегом я вернулся к себе в домик, отыскал в недрах сумки коробок со спичками и затем уже не спеша двинулся в сторону речного берега, где меня дожидалась пачка «Родопи»."
        "..."
        window hide
        scene bg ext_houses_sunset
        with dissolve
        window show
        "Из леска на покатом берегу я мельком поглядывал на улицу с палатами пионеров младшего отряда."
        "На глаза сразу попался дом Ульяны и Алисы."
        th "Наверно, мне стоило спрятать сигареты в другом месте, где меньше вероятность натолкнуться на Двачевскую."
        "Но сейчас я остался тут: за кустами и деревьями в лёгкой полутьме заметить меня с улицы при всём желании было бы трудно."
        "Я снял галстук и рубашку, аккуратно сложил её и бросил её на траву рядышком."
        "Наконец-то долгожданный табачный дым наполнил нос, глотку и лёгкие."
        "«Родопи», конечно, не самый идеальный выбор, но очень сносный." 
        "Я повертел пачку сигарет, стряхивая пепел в сторону от рубашки."
        "А эти, с фильтром, доставшиеся мне случайным трофеем, оказались шикарными. Видимо, подлинный импорт, к тому же до сих пор существующий в две тысячи восьмом году."
        "Тут, похоже, производство шагнуло вперёд, и старое лишь стало лучше, а не было утеряно, переименовано или перепродано."
        "Изредка я выглядывал из-за дерева, проверяя, не идёт ли кто по улице." 
        "В какой-то момент мимо прошли малые пионеры, возвращавшиеся с пятиминутки гигиены, а за ними вожатые Дима и Банникова Инга."
        th "Смешно даже, мне давно за двадцать, а теперь я должен щемиться за кустами, словно школьник."
        th "Ну и что!"
        "Зато мне по-настоящему хорошо здесь — под соснами — в тёплый вечер на берегу Волги с неплохими сигаретами."
        "Подумаешь, что в шаге от двух вожатых. Так даже лучше, наглость — второе счастье."
        "..."
        $ night_time ()
        #scene bg ext_houses_night
        with dissolve
        "В лагере окончательно стемнело. Я спрятал пачку в том же месте и поднялся, надевая рубашку."
    else:
        "Стряхнув капли воды с рук, я помедлил перед тем как пойти к себе домой."
        "Захотелось курить."
        "Я перебрал в уме всех известных мне в лагере курильщиков."
        if d1_un_evening:
            th "Вот оказия, я ни одного такого не знаю!"
            if (d2_met_ld == True) or (tech_club == True):
                "...Только среди взрослых."
            th "Не ходить же от пионера к пионеру, спрашивая, есть ли у них сигареты!"
            th "А может, к вожатым обратиться?"
            th "Нет, они по шее накостыляют, чтобы здоровье себе не портил..."
            if d2_met_ld:
                "Возможно, и лодочник разделит их мнение."
            if tech_club:
                th "А кибернетиков и спрашивать не надо, они не курят, они больше по канифоли угорают."
                "Ещё были Михаил Евграфович с котом, но к ним я тем более не решился идти."
            "Оставалось только смириться, что в этот вечер мне покурить не удастся."
            th "Того гляди, брошу привычку!"
        else:
            th "Моделист Антон, Алиса, Токарев, Лирический..."
            if d2_met_ld:
                "Лодочник, судя по всему, забивает свои папиросы ядрёной махоркой — совсем не мой выбор."
            if tech_club:
                th "Финдиректор и даже его кот. Причём насчёт Михаила Ефграфовича я ещё сомневался: пепельница-то была на столе у кота."
                "Но этот вариант я отбросил."
            "К младшеотрядникам с такой просьбой я решил не обращаться. Надо было искать Антона или Двачевскую."
            if d1_dv_evening:
                th "Пойду к Антону, как вчера."
            if d1_un_evening:
                "Я не знал, где живёт Антон, поэтому спросил у одного из гулявших по улице пионеров, и мне помогли."
            scene bg ext_houses_sunset
            with dissolve
            "..."
            play sound sfx_knock_door7_polite
            "Я поднялся по ступенькам домика номер шесть и негромко постучал в дверь, зовя пионера по имени."
            $ renpy.pause(1)
            show mk at center with dissolve
            if d1_dv_evening:
                me "Привет. Сходим к «Зелёному театру»?"
                mk "Э-э, нет... Не хочу никуда идти сегодня."
                me "Ладно, а покурить есть? Я-то, дурак, не подумал купить себе перед отъездом."
            if (d1_un_evening == True) or (d1_genda_flag):
                if (modeller_club == False):
                    $ meet('mk', u"Антон")
                me "Извини, что беспокою. Есть покурить?"
            show mk smile at center with dspr
            mk "Ну я же не благотворительная лавка по раздаче табака всем страждущим."
            show mk at center with dspr
            mk "У меня самого три штуки осталось, буду на всю неделю растягивать."
            me "Понимаю. Жаль...{w} Не знаешь, где сейчас Двачевская?"
            "Он пожал плечами."
            mk "Нет, я после ужина сразу домой слинял.{w} Слушай, а если я тебе дам одну сигу, сможешь потом вернуть?"
            me "Да, верну. Какую марку?"
            mk "Забей, какую хочешь приноси, только не дамские. Погоди секунду."
            "Он принёс мне одну единственную сигарету, но сейчас мне и этого было достаточно."
            me "Спасибо."
            hide mk with dissolve
            th "Ну, хоть что-то."
            window hide
            $ d2_mk_deal = True
            scene black
            with dissolve
            "......"
            "........."
            $ night_time ()
            scene bg ext_square_night
            with dissolve
            window show
            "Пока я бегал взять спичками и ходил за эстраду, на лагерь опустилась вечерняя темнота."
    th "Куда бы теперь сходить, пока есть время до отбоя?"
    window hide
    stop music fadeout 2
    jump d2_evening_map_prep
        
label d2_evening_map_prep:

    #$renpy.music.set_volume (0.7, channel=7)
    #play music music_list["everyday_theme"] channel 7

    $ disable_all_zones()

    $ set_zone('music_club', 'd2_musclub_evening')
    if d2_dv_help:
        $ set_chibi("music_club",  "mi") #TODO: возможно, что при использовании карты в середине дня после полдника без получения d2_dv_help чибик всё равно есть. Проверить во всех возможных ответвлениях.
    $ set_zone('clubs', 'd2_clubs_evening')
    $ set_zone('camp_entrance', 'd2_camp_entrance_evening')
    if (d1_un_evening == True):
        $ set_chibi("camp_entrance",  "sl") #TODO: исправить — при использовании карты в середине дня после полдника без получения d1_un_evening чибик всё равно есть.
    else:
        $ set_chibi("camp_entrance",  "?")
    $ set_zone('dining_hall', 'd2_dining_hall_evening')
    $ set_zone('sport_area', 'd2_sport_area_evening')
    $ set_chibi("sport_area",  "?")
    $ set_zone('beach', 'd2_beach_evening')
    if (d2_us_dv_day == True) and (d1_river_flag == True):
        $ set_chibi("beach",  "dv")
    if (d2_dv_help == False) and (d1_river_flag == False):
        $ set_chibi("beach",  "?") #TODO: пофиксить месторасположение иконки ? — на середину пляжа.
    $ set_zone('me_mt_house', 'd2_me_mt_house_evening')
    $ set_chibi("me_mt_house",  "mt")
    $ set_zone('library', 'd2_library_evening')
    $ set_chibi("library",  "?")
    $ set_zone('medic_house', 'd2_aidpost_evening')
    $ set_chibi("medic_house",  "?")
    $ set_zone('estrade', 'd2_green_theatre_evening')
    $ set_chibi("estrade",  "?")
    $ set_zone('boat_station', 'd2_boathouse_evening')
    $ set_chibi("boat_station",  "?")

    jump d2_evening_map

label d2_evening_map:
    
    $ night_time()
    $ persistent.sprite_time = "night"

    if d2_evening_places != 3:
        $ show_map()
    else:
        jump d2_bed_time

label d2_skip_common_event:

    scene bg ext_dining_hall_near_day
    with dissolve
    play music music_list["my_daily_life"] fadein 1
    window show
    "На улице я уже в полной мере ощутил свободу — ни толпы, ни сборищ, только приятный ветерок и пустые дорожки."
    "Солнце клонилось к горизонту, но закат намечался ещё нескоро — ужин прошёл раньше обычного, не по расписанию."
    th "Значит, вечерней пятиминутки на гигиену и отбоя я буду ждать долго."
    "Пропуск мероприятия возвращал меня на колею безделья, ведь почти все мои новые знакомые остались в столовой."
    if (d1_dv_evening == True) or (d2_met_ug == True):
        th "Кроме Угрюмого, конечно."
        "Но сейчас я не собирался искать его."
    "Я загорелся идеей наведаться куда-нибудь, где ещё не бывал — в лагере или за его пределами."
    if (d2_day_us == False):
        if (d2_met_ld == True) or (d2_dv_fight == False):
            "Например, я не видел здешнюю баню."
            "Не то чтобы она должна была поразить моё воображение, просто хотелось побольше разузнать о месте, куда я попал."
            "..."
            window hide
            scene bg ext_square_day
            with dissolve
            $ renpy.pause(1)
            scene bg ext_houses_day
            with dissolve
            $ renpy.pause(1)
            scene bg ext_bathhouse_day
            with dissolve
            window show
            "Баня располагалась на укромной поляне, где лес граничил с пионерлагерем, буквально в шаговой доступности от реки."
            "Отсюда открывался вид на залив. Хоть с дебаркадера и было трудно заметить банный дом, но берег у поляны хорошо просматривался."
            th "Тайком здесь не искупаешься. Жаль!"
            "А ведь тут для купания даже сделали короткие мостки от бережка — грубо сколоченный настил из досок промеж двух опор."
            th "Интересно, а пионерам-то можно пользоваться баней?"
            "Я прошёл ко входу бревенчатого здания, напоминавшего сказочную избу. Вот только для сказочности ему недоставало ветхости. Баня выглядела совсем новой."
            "Внутри оказалось точно так же, когда я приоткрыл незапертую дверь — всё было красиво и аккуратно. Как в современных саунх при бассейне или в санатории."
            #Текст с более подробным описанием войдёт в лист с техзаданиями и будет использован в ивентах с посещением бани.
            th "Неплохо! Однако неудивительно, если учитывать, какой сейчас год на дворе."
            "Если бы не лень, я бы попробовал организовать себе посещение парилки."
            th "Да и разрешат ли мне?"
            "Я сомневался, что дети могли делать такое в одиночку, если даже на реку их не пускали без вожатых вне установленного режимом времени."
            "А для мытья всегда были душевые у спортплощадки."
            th "Ну, значит, не сегодня."
            $ d2_seen_bathhouse = True
            "Я закрыл дверь и сбежал по деревянным ступеням на тропинку."
            "Баня — дело хорошее, однако..."
        else:
            pass
    "Меня крайне интересовало, каким является мир за стеной забора. Сегодняшним утром я окончательно убедился, что СССР и пионерия тут не понарошку, но обо всём остальном я практически ничего не знал."
    th "И пока вожатые заняты мероприятием с детьми, мне легче лёгкого улизнуть ненадолго и вернуться незамеченным."
    "..."
    window hide
    scene bg ext_houses_day
    with dissolve
    $ renpy.pause(1)
    scene bg ext_clubs_day
    with dissolve
    $ renpy.pause(1)
    scene bg ext_no_bus
    with dissolve
    window show
    "Я задумал пройти как можно дальше от ворот лагеря по шоссе вдоль Волги." 
    th "Интересно же узнать, что находится поблизости! Я ведь не упрусь в невидимую стену, если попытаюсь?"
    scene bg ext_road_day
    with dissolve
    "И я начал свой путь к неизведанному."
    th "Миклухо-Маклай, как сказала вожатая! Отправился на поиски местных аборигенов."
    "Только не хватало узловатой палки-трости и вещмешка за спину..."
    th "А вот пионерский галстук надо спрятать, иначе сразу примут за беглого пионера."
    "Я запихал плат в карман."
    "Но на рукаве рубашки всё ещё горел красно-жёлтый шеврон со звездой и костром."
    th "Блин. Как-нибудь отделаюсь, если спросят."
    "Мне уже было не до переодеваний, я просто шёл вперёд, всё дальше удаляясь от лагеря."
    "Солнце грело меня. Было жарко, но не так, чтобы воздух над асфальтом плавился от зноя. Я был уверен, что не выдержал бы такой прогулки в тихий час, когда самое пекло."
    "Я глядел по сторонам и не обнаруживал ничего примечательного: одни кусты с деревьями да луга, вдоль которых тянутся провода ЛЭП."
    "В начале пути реки слева не было видно из-за леса. Но самое любопытное оказалось впереди. Там вдалеке синели горы. Невысокие, но вольготно раскинувшиеся за равниной, будто я попал на юга."
    #Горы находятся за пределами видимости на текущем бэкграунде, как и должно быть. Они могут быть видны на другом бэкграунде — на заглушке (в качестве примера) или на новом, если таковой нарисуют.
    if d1_tricked:
        "Ольга Дмитриевна говорила вчера, что мы в Подмосковье. На первый взгляд, совсем не похоже на правду."
        "Может, здесь оно именно такое, не как в моём мире."
    "Пейзаж был потрясающе красивым. Я уходил от лагеря всё дальше и дальше."
    "Выветрилось из головы беспокойство, и я задумался, что же лучше — лето или зима?"
    th "Летом здорово купаться, утолять жажду напитками, леденящими мозги, читать на свежем воздухе..."
    th "А зимой темнеет раньше, и за компьютером перед незашторенным окном сидишь дольше!"
    th "За это мне зима нравится больше, конечно."
    "..."
    scene bg ext_shed_day
    with dissolve
    "Пока я размышлял, я вышел к сараю, позади которого начинался гаражный кооператив."
    if d1_road_decision:
        "А вот и то самое место, про которое мне рассказала Славя. Значит, и дачный сектор где-то рядом."
    "Проезд к гаражам был широким и раздваивался, пыльная дорога без тупика вела под уклон и в сторону, а куда — я не имел понятия из-за деревьев и нескольких домов с ограждениями."
    if (d1_road_decision == False):
        th "Наверно, здесь находится какой нибудь посёлок или дачи..."
    th "Если я прав, то мне туда и надо!"
    "Я уверенно спустился к домам на участках и увидел приколоченную к забору дощечку с названием улицы."
    "Пройдя дальше, я обнаружил ещё несколько поворотов на другие улицы, гораздо длиннее этой, где ровными рядами были понастроены малоэтажные домики."
    th "Действительно, какое-то садово-дачное товарищество..."
    "Всё выглядело предельно аккуратно, я не заметил убитых и заброшенных домиков. Только похожие друг на дружку здания не выше пары этажей."
    th "Здесь определённо есть жизнь."
    "Я свернул на одну из таких тянувшихся вдаль улиц, с интересом глядя по сторонам и выискивая участок, где забор пониже, чтобы понаблюдать за местными жителями."
    "Где-то на середине улицы играли дети."
    "К ним я подходить не стал — мне в лагере хватило встреч с племенем младым и незнакомым."
    th "Хорошо бы найти хоть какие-то сведения о происходящем в мире..."
    "На ум пришёл образ, то ли из старого кинофильма, то ли из художественного произведения: герой достаёт из урны газету, чтобы забесплатно прочесть последние новости."
    "Шариться по урнам я не собирался, всё равно их тут не было. Очевидное решение нашлось само собой."
    "Я остановился у невысокого дощатого частокола с воротцами для автомобиля."
    th "Можно спросить у дачников газету — ничего страшного в просьбе нет."
    scene black
    with dissolve
    "......"
    "........."
    $ sunset_time ()
    scene bg ext_road_sunset
    with dissolve
    "На дорогу я вернулся при закате, держа под мышкой скрученную газету пятидневной давности."
    "Я уже прочёл её залпом, сидя на ступеньках одинокого гаража у шоссе."
    $ proficiencies ['kn_world']+=2
    "В первую очередь я узнал курсы валют, имена главных политических деятелей и события в мире за прошедшую неделю."
    "Советскую страну, в которой я оказался, не раздирали внутреннеполитические противоречия, хотя несколько государств давно стали бывшими для Союза республик."
    "Были, конечно, два локальных конфликта, однако длились они уже долго и нудно, без обострений. Я не обнаружил сведений хотя бы об одной горячей точке в настоящее время или намёка на затруднительные отношения, ставшие в моём мире причиной войны августа восьмого."
    "В целом, новости оставили благоприятное впечатление. Они внушади спокойствие."
    "Людей куда больше волновал съезд учитилей в Минске по вопросам инноваций в школьном образовании к грядущему учебному году."
    "В той же рубрике была заметка про открывшуюся секцию по фехтованию в новом Дворце пионеров."
    "Крайне любопытными оказались новости культуры. Особенно рецензия на только что вышедший фильм о привидении, которое засиделось в замке со своим другом филином и захотело узнать, как выглядит мир днём, но стало чёрным от солнечного света."
    "Я прочёл статью и глазам своим не поверил — утверждалось, что фильм является доподлинной {i}биографией{/i} реально существовавшего человека (а ныне призрака), но я-то помнил, что в моём мире это была обыкновенная детская сказка!"
    "Но нет, текст с непрошибаемой серьёзностью представлял всё как истину, пусть и с похвалами успешной кинокартине."
    "Я даже на всякий случай снова проверил название газеты — не «Спид-Инфо», а вполне солидное издание, и стоит рубль пятьдесят."
    "Не только это стало откровением для меня. Ещё в одной из статей я выловил между строк информацию, что в мире есть и другие расы, кроме человеческой."
    "Их происхождение не сообщалось: видимо, для читателей это было уже общеизвестным фактом. Чего стоил один снимок, где человеку голову заменял игральный кубик величиной с футбольный мяч!"
    th "Скорее всего, на нём просто была маска для эпатажа, правда?"
    "Но утром до зарядки я видел пионера с монитором вместо головы. Неужели это прямое доказательство, что здесь такое существует?"
    "Сомнения одолевали меня весь путь назад."
    if (sp_crg >= 1) and (proficiencies ['sp_pers']>= 1):
        "Зато помимо газеты я ещё уносил с собой в кармане рубашки сигарету, которую удалось стрельнуть у случайного прохожего."
    "......"
    scene bg ext_houses_sunset
    with dissolve
    "К счастью, вожатые не заметили моего исчезновения. Мне удалось вернуться к тому моменту, когда младших повели чистить зубы и по домам."
    "Перед отбоем нашего отряда я ещё мог побродить по лагерю, и даже не в одиночестве."
    th "Но сначала закину газету себе в сумку — важное вещественное доказательство!.."
    if (sp_crg >= 1) and (proficiencies ['sp_pers']>= 1):
        "...И возьму спичек, чтобы покурить. А там хоть трава не расти!"
    window hide
    $ night_time ()
    scene black
    with dissolve
    window show
    "..."
    "......"
    window hide
    stop music fadeout 2
    jump d2_evening_map_prep

label d2_us_evening_slot:

    "Я осторожно двинулся в сторону турников, поглядывая на безлюдную спортплощадку."
    th "Наверно, придётся смириться."
    "Я ещё погрозил на прощание кулаком в сторону кустов, где она могла прятаться, и пошёл было обратно в столовую, как сзади послышался сдавленный смешок."
    "Не узнать его было невозможно!"
    stop music fadeout 2
    "Я не имел понятия, откуда она выскочила, разве что с неба свалилась, потому что, когда я развернулся, она..."
    play music music_list["revenga"] fadein 0
    #show us grin pioneer far at center with dspr
    #Текущий cg временный. Возможно, его придётся обновлять по окончании работ над скриптом.
    scene cg d2_soccer
    with fade
    us "МЯЯЯЯЯЯЯЯЯЯЯЯСООООООООООООООООООООО!!!!!!"
    play sound sfx_soccer_ball_kick
    "...с задорным криком врезала по невесть откуда взявшемуся у неё мячу, да с таким размахом, что юбка пионерки задралась, засвечивая белизну трусиков..."
    "Неудивительно, что я словно прирос к месту, когда мяч полетел прямо в меня!"
    "А скорость у него была бешеная — ни уклониться, ни отскочить!"
    "Как в замедленной съёмке, я наблюдал летящий ко мне снаряд и через секунду мощным ударом уже был сбит на землю!"
    play sound sfx_soccer_ball_catch
    with vpunch
    scene bg ext_playground_sunset
    with dissolve
    show us laugh2 pioneer far at center with dissolve
    me "Ар-ргх!"
    th "Больно! Хорошо, что в живот, а не ниже..."
    "От удара у меня сбило дыхание, что, несомненно, спасло Ульянку от потока брани в её адрес."
    "Но она даже не думала убегать!.."
    stop music fadeout 3
    th "Наивная!"
    play music music_list["always_ready"] fadein 3
    show us laugh pioneer far at center with dspr
    "Ульяна засмеялась."
    th "И настолько же наглая!"
    us "РАНЕН!"
    "Вот тут-то я и пришёл в ярость!"
    th "У-У-У, НЕГОДЯЙСКАЯ «ЛОЛЯ»! НЕНАВИСТЬ-НЕНАВИСТЬ-НЕНАВИСТЬ!!!"
    "Однако в дыхалке спёрло, и я не мог ничего сказать. Но как же я хотел натянуть эту девчонку на флагшток с главной площади прямо сейчас!"
    show us grin pioneer at center with dspr
    "Она приблизилась, и вовсе не для того, чтобы помочь!"
    us "Эй, хватит валяться!"
    th "Дай только отдышаться, и я..."
    "С большим усилием я вынудил себя хотя бы сесть, всё ещё сгибаясь в три погибели."
    show us surp1 pioneer at center with dspr
    us "Столько бежал за мной?"
    show us grin pioneer at center with dspr
    us "Хы!"
    "Она осклабилась и показала руки, измазанные кремом."
    show us surp1 pioneer at center with dspr
    us "А торта-то и не осталось!"
    us "Опоздал! Опоздал!"
    show us smile pioneer at center with dspr
    "Бесцеремонно вытерев ладошки об юбку, она принялась носиться вокруг и кидать в меня мяч (вот дрянь!), прежде чем я наконец смог нормально вдохнуть и подняться на ноги."
    me "Ты что в столовой устроила?"
    show us normal pioneer at center with dspr
    me "Ольга Дмитриевна тебе завтра задаст!"
    th "А сегодня тебе задам я."
    show us dontlike pioneer at center with dspr
    "Ульянка надулась."
    us "Сами виноваты!"
    us "Надо было поддаваться!"
    "В отчаянии Ульяна плюхнулась на траву."
    show us angry pioneer at center with dspr
    us "Это я должна была выиграть!"
    us "Я!"
    "И она снова принялась с силой колотить мяч, теперь об землю."
    me "Может, в следующий раз повезёт."
    show us dontlike pioneer at center with dspr
    us "В следующий раз я тако-о-ое придумаю, что сразу всех обыграю!"
    me "Верю-верю."
    stop music fadeout 2
    play music music_list["i_want_to_play"] fadein 2
    show us laugh pioneer at center with dspr
    "Ульяна не поняла сарказма и, воодушевлённая моими словами, тут же вскочила. От детского гнева ничего не осталось, она снова стала той же взбалмошно весёлой пионеркой."
    show us grin pioneer at center with dspr
    "Она принялась чеканить мячик, и делала это неплохо, если учесть, что на ней пионерская форма и лаковые сандальки-туфли вместо кед."
    th "Так, Ульяна... Как бы тебя наказать?"
    "Я хрустнул пальцами, разминая кулаки. Идея с натягиванием на флагшток вместо флага определённо была лучшей. Но для полного комизма Ульянке недоставало маечки СССР, а в идеале — с серпом и молотом." 
    show us smile pioneer at center with dspr
    us "Поиграем?"
    th "Во что?"
    "Я опешил и даже не успел озвучить вопроса."
    show us grin pioneer at center with dspr
    play sound sfx_soccer_ball_kick
    "Ульяна остановилась и снова влупила по мячу, точно подгадав момент удара."
    play sound sfx_soccer_ball_catch
    "Но теперь я был готов и ловко поймал его, словно профессиональный вратарь."
    show us surp1 pioneer at center with dspr
    th "Попадись ты мне в другой раз, я тоже нападу со спины, будешь знать!"
    play sound sfx_soccer_ball_kick
    "Со всей силы я залимонил мяч обратно, прямо в девчонку."
    show us grin pioneer at center with dspr
    play sound sfx_soccer_ball_kick
    us "ЧА-А-АРДЖ!"
    show us laugh pioneer at center with dspr
    "Мяч прилетел обратно, и я остановил его прежде, чем мне съездило по лбу."
    me "Ах ты ж зараза. Смотри куда лупишь!"
    show us upset pioneer at center with dspr
    us "Крит не прошёл."
    show us grin pioneer at center with dspr
    us "Извини, мяч верни. Пожалуйста!"
    me "Ага. Щас."
    "Я пожалел что нечем его проколоть."
    me "Кстати, где мяч достала? Спортзал же закрыт вечером."
    show us laugh pioneer at center with dspr
    us "Ещё на той неделе стащила и припрятала, пока дядя Дима хлопал ушами!"
    "Ульяна более чем заслуживала расправы."
    me "Хочешь почувствовать себя в сказке?"
    "Крутя мяч в руках, я осмотрел близлежащую местность в поисках самого буйного и колючего куста."
    show us surp1 pioneer at center with dspr
    us "Да, я люблю сказки! Расскажешь одну? Только верни мяч."
    me "«Верни мяч, верни мяч». Я же сказал, что верну."
    "Я состроил самую хитрющую рожу, на какую был способен."
    menu:
        "Evil mode on: а вот и куст!":
            "Я наконец отыскал тот дремучий куст, куда следовало послать Ульяну за все пригрешения."
            play sound sfx_soccer_ball_kick
            "Прицелившись, я как следует наподдал мячу."
            "Пиу!"
            show us grin pioneer at center with dspr
            "Ульяна проводила взглядом полёт мяча в небеса, и тут я сообразил, что выбрал неправильную траекторию и не рассчитал силу." 
            "Мяч, не долетев до центра куста, плюхнулся рядом с ним, подскочив несколько раз." 
            "Было ясно, что пионерка сможет подобрать его, не залезая в самую гущу веток."
            show us laugh pioneer at center with dspr
            us "Мазила, мазила!"
            show us smile pioneer far at center with dspr
            "Смеясь, она побежала за мячом."
            stop music fadeout 2
            play music music_list["smooth_machine"] fadein 2
            "Моё настроение только сильнее ушло в минус."
            show us laugh2 pioneer at center with dspr
            me "Десять в третьей степени чертей.{w} Вот теперь ты можешь обижаться. Сказки про Братца Кролика не будет."
            show us surp2 pioneer at center with dspr
            us "Ты злой!" 
            show us grin pioneer at center with dspr
            us "Но у тебя ничего не получилось. Я выиграла."
            show us laugh pioneer at center with dspr
            us "Повторим? Мячик — это весело, играть в командную игру одной — скучно!"
            me "Да нет, пожалуй, я пойду."
            show us surp1 pioneer at center with dspr
            us "Ты сказал да, я слышала, что ты сказал да. Ура! Играем."
            show us grin pioneer at center with dspr
            us "И ещё один раз!"
            play sound sfx_soccer_ball_kick
            "Она сделала разбег и снова пнула мячик."
            "Я остановился, но с моей позиции закатное солнце так ярко светило в глаза, что я не разглядел мяча и поэтому приготовился к удару, сгруппировавшись."
            "Словом, я съёжился, стоя на одной ноге и прикрыв голову."
            show us laugh pioneer at center with dspr
            us "Трусишка, трусишка, в коротких штанишках!"
            "Мяч упал рядом и откатился немного дальше."
            show us normal pioneer at center with dspr
            "Ульяна пошла за ним, видя, что я не стал брать его, потому что зашагал к лавочкам."
            me "Я не хочу играть в футбол."
            show us smile pioneer at center with dspr
            us "Ты не умеешь играть в футбол."
            if d2_us_dv_day:
                me "А что я по-твоему делал сегодня в спорткружке? И гол забил."
                show us surp2 pioneer at center with dspr
                us "Нет, иначе мы бы победили!"
                show us upset pioneer at center with dspr
                us "Мне Токарев за ужином сказал, что наша команда в итоге продула."
                show us surp1 pioneer at center with dspr
                us "Ты не забил хотя бы семь голов! Ты не умеешь играть в футбол."
            me "Нет, я не хочу играть в футбол."
            show us grin pioneer at center with dspr
            us "Нет, ты не умеешь играть в футбол."
            me "Не умею и не хочу разные вещи."
            show us smile pioneer at center with dspr
            us "Да, я знаю. Ты пока не показал ни умения, ни заинтересованности."
            me "Зато про то, что такое чужое мнение, мама, видимо, тебе не говорила."
            show us laugh pioneer at center with dspr
            us "Больше дела, меньше слов!"
            th "В твоём случае я бы сказал «Больше слов, меньше мысли»."
            hide us
            scene bg ext_playground_night
            with dissolve2
            $ night_time ()
            $ persistent.sprite_time = "night"
            show us dontlike pioneer at center with dissolve2
            "Пока мы препирались, на площадке уже заметно стемнело, и на небе появились первые звёзды."
            me "Ты просить прощения собираешься?"
            show us angry pioneer at center with dspr
            "Но Ульянка только насупилась ещё больше."
            me "Пойдём, извинишься — и Ольга Дми..."
            "Но она перебила."
            us "Не собираюсь я ни перед кем извиняться, зануда!"
            "А вот теперь она здорово разозлилась!"
            play sound sfx_soccer_ball_kick
            "Ульяна со всей силы пнула по мячу, и он молнией улетел куда-то в темноту..."
            th "Хорошо, что не в меня, тогда Ульяне бы не поздоровилось."
            show us sad pioneer at center with dspr
            "Я был сердит до невозможности, а Ульяна обречённо плелась за мной, ничего не говоря."
            #show lk
            "На главной улице нам встретился Дмитрий Евгеньевич. Вожатый напомнил Ульяне, что у её отряда уже время отбоя, и мы разошлись."
            hide us with dissolve
            #hide lk
            "Мне уже больше ничего не хотелось делать, и я сразу отправился к себе в палату."
            window hide
            stop music fadeout 2
            jump d2_bed_time
        "Good mode on: я отдам мяч нормально":
            stop music fadeout 1
            play music music_list["so_good_to_be_careless"] fadein 1
            "Держа мяч, я направился к девчонке. Я намеревался отдать его, но не лишать Ульянку причитающегося ей возмездия."
            show us surp1 pioneer close at center with dspr
            me "Вот, лови."
            "Остановившись в двух шагах от девочки, уже протянувшей ко мне руки, я перекинул мяч через неё так, чтобы она не смогла поймать его, подпрыгнув."
            "Ульяна развернулась и схватила падающий мячик, а я одним рывком сцапал её."
            show us fear pioneer close at center with dspr
            th "Попалась!!! Обманулась, как за конфетку!"
            play sound sfx_bodyfall_1
            with vpunch
            "Я шлёпнулся в траву на пятую точку, утягивая за собой в тесных объятиях пионерку, не пожелавшую расставаться с мячом, только вскрикнувшую от неожиданности."
            show us dontlike pioneer close at center with dspr
            us "Так не честно!"
            me "А то! Нападать со спины очень и очень подло, как ты сделала это в первый раз. Теперь моя очередь."
            show us surp1 pioneer close at center with dspr
            us "А сказка? Ты обещал сказку!"
            me "Я такого не говорил! Я сказал, что ты {i}почувствуешь себя в сказке{/i}." 
            "Ульяна и не думала сопротивляться и убегать, она с нетерпением хотела услышать от меня что-нибудь интересное."
            show us surp2 pioneer close at center with dspr
            us "Ну-у-у! Расскажи пожалуйста!"
            me "Хорошо-хорошо."
            show us laugh2 pioneer close at center with dspr
            "Я крепче стиснул Ульянку, и коротко пересказал истории, когда-то прочитанные мной в детстве."
            me "Жили были Братец Лис и Братец Кролик, и один пытался изловить другого, чтобы слопать, да всё никак не получалось."
            me "Что только ни делал Лис для этого: и в гости приглашал, и мёртвым прикидывался. Однажды чуть не поймал, смастерив Смоляное Чучелко, к которому прилип Братец Кролик."
            me "Однако Братец Кролик был такой же хитрый, он близко к Лису не подходил, следы за собой заметал, и смекалка его постоянно выручала. В общем, они друг друга стоили."
            me "Но в {i}нашей{/i} сказке всё-о будет по-другому! И Лис — не Лис, а я, Семён!"
            me "И Братец Кролик не Кролик вовсе, а одна неугомонная пионерка, то есть ты, Ульяна."
            show us laugh pioneer close at center with dspr
            me "И вот мне как раз удалось поймать тебя."
            me "Только я тебя не зажарю и не съем..."
            "Я вдруг посомневался насчёт последней фразы, так как невольно уловил сладкий-сладкий запах от копны алых волос на макушке девочки. От Ульянки пахло тортом, что она утащила."
            th "Да она сама один большой лакомый кусочек!"
            stop music fadeout 2
            "Ульяна не понимала, отчего я выдержал такую паузу."
            show us surp1 pioneer close at center with dspr
            us "А что ты сделаешь?.. Ну?..."
            play music music_list["always_ready"] fadein 1
            "Мои пальцы быстро ощупали девочку."
            me "Я?..{w} Я защекочу тебя нахѣръ!"
            show us laugh pioneer close at center with dspr
            "Ульянка взвизгнула и начала безудержно смеяться, когда я привёл угрозу в исполнение. Девчонка извивалась, как угорь, пытаясь отделаться от меня, но смех и мои пальцы только мешали ей. Она даже выронила мяч, который прижимала к груди."
            "Пионерка целиком была в моей власти!"
            show us surp1 pioneer close at center with dspr
            us "Ой, ха-ха! Не могу, перестань!!! Ха-ха!"
            me "И под коленками, под коленками!"
            show us laugh pioneer close at center with dspr
            "Ульянка аж взбрыкнулась, не переставая смеяться, и мы вместе повалились набок."
            "Тут она смогла вырваться и поползла от меня, не успев даже вскочить, а я поймал её за лодыжку."
            me "Не уйдёшь!"
            "Сам не понимая, что творил, я стянул с Ульяны сандальку и пощекотал ногу."
            "Ульянка снова залилась смехом и едва не лягнула меня пяткой по носу, из-за чего я немедленно отпустил её и поднялся."
            show us laugh pioneer at center with dspr
            me "Ну, кто теперь ранен, а кто выиграл? Чего валяешься?"
            show us shy2 pioneer at center with dspr
            "Девчонка ещё лежала на траве с затихающим смехом и подрагивала в конвульсиях."
            us "Ха!.. Ха..."
            stop music fadeout 2
            scene bg ext_playground_night
            $ night_time ()
            $ persistent.sprite_time = "night"
            show us shy2 pioneer at center
            with dissolve2
            play music music_list["sweet_darkness"] fadein 1
            "Над полем уже заметно стемнело, и на небе зажглись первые звёзды."
            me "Всё на этом, предлагаю ничью."
            show us normal pioneer at center with dspr
            us "...Ты сумасшедший..."
            "Упёршись руками в колени, я с улыбкой склонился над поверженной девочкой."
            me "Почему же?"
            show us grin pioneer at center with dspr
            us "Я ни за что не соглашусь на ничью!"
            "Она приподнялась и отыскала снятую мной туфлю."
            me "Придётся, больше я сегодня играть не буду."
            show us normal pioneer at center with dspr
            "И точно в подтверждение моему ответу послышался мужской голос издалека, с аллеи."
            lk_voice "Ульяна! Ты там? Семён, это ты?"
            me "Да, Дмитрий Евгеньевич, мы здесь!"
            lk "Ульяна, у твоего отряда время отбоя! Отправляйся чистить зубы и к себе — спать!"
            show us surp2 pioneer at center with dspr
            us "А можно ещё погулять, а? Пожалуйста!"
            lk "Инга Максимовна будет недовольна!"
            show us upset pioneer at center with dspr
            us "Ла-адно! Сейчас пойду!"
            play sound sfx_soccer_ball_kick
            "Она встала, отряхнулась и запулила мяч куда-то в темноту, чтобы потом снова можно было найти его и поиграть."
            me "Ну как, понравилась моя сказочка?"
            show us shy pioneer at center with dspr
            us "Ты не просто злой, Семён! Ты очень злой!"
            "Даже в потёмках я углядел, что Ульяна чуть покраснела и надулась."
            th "Выходит, я не наказал её после всего, а поощрил, она ведь получила свою порцию веселья, хотя заслуживала трёпки."
            show us laugh2 pioneer at center with dspr
            th "Но ведь и я здорово повеселился..."
            th "Не о чем жалеть!"
            "Кроме того, что Ульяне сегодня уже больше не погулять. Как в детстве, когда родители загоняют домой, а уходить с улицы и прощаться с друзьями так не хочется..."
            #show lk
            "Вожатый дождался нас, и мы разошлись на дороге у площади."
            hide us with dissolve
            #hide lk
            "Мне уже больше ничего не хотелось делать — игра с Ульянкой вымотала меня, и поэтому я сразу отправился к себе в палату."
            window hide
            stop music fadeout 2
            $ d2_us_evening = True
            $ lp_us = lp_us + 1
            $ d2_girls_event = (d2_girls_event) + (1)
            jump d2_bed_time

label d2_musclub_evening:
   
    if d2_dv_help:
        jump d2_mi_dv_evening_slot
    scene bg oldmap
    window show
    th "Нет смысла туда идти, кружки и клубы закрываются перед ужином."
    window hide
    $ disable_current_zone()
    jump d2_evening_map

label d2_mi_dv_evening_slot:
    
    scene bg oldmap
    window show
    "Неизвестно, что меня сподвигло, но я решил сходить к Мику и узнать об успехах в переговорах с Алисой."
    th "Если кружок будет закрыт, то загляну в палату Лены и Мику, всё равно по пути к моему домику."
    "..."
    window hide
    $ reset_chibi("music_club")
    scene black
    with dissolve
    show screen central_text("День 2 — Фронтмен, который попался")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_musclub_night_fog
    with dissolve
    play music music_list["just_think"] fadein 2
    play ambience ambience_camp_center_night fadein 1
    show mi normal pioneer far at cleft
    show dv grin pioneer2 far at cright
    with dissolve
    window show
    "У веранды музыкального клуба я встретил и Мику, и Алису. Они беседовали негромко, но с явным напряжением, Мику всплёскивала руками, и луч фонарика, сжатого в кулаке, безумно летал в такт её жестам."
    th "Оп-па, это совсем не то, что я сейчас ожидал."
    "Я уж было приготовился уйти, как Двачевская заметила меня."
    show mi scared pioneer far at cleft
    show dv normal pioneer2 far at cright
    with dspr
    dv "А вот и сам виновник торжества! Иди-ка сюда... Мы как раз говорили о тебе..."
    "Страшно было предположить, что именно девчонки говорили."
    th "Если Алиса не оценила мою помощь тайком или Мику не убедила её, то мне хана."
    show mi smile pioneer at cleft
    show dv normal pioneer2 at cright
    with dspr
    "Я подошёл к ним с опаской."
    me "Ну?"
    show dv angry pioneer2 close at cright with dspr
    "Алиса приблизилась ко мне с угрожающим видом, и я упрекнул себя за слабоволие. Надо было драпать!"
    dv "Семён!..{w} Если ты не явишься утром на занятие нашего кружка, я тебя в бараний рог скручу."
    me "Э-э... Нашего? Ты уже перевелась?"
    dv "Нет, глупенький, мне ещё придётся тащиться в админку и просить о выходе из спортклуба. А ты... чтоб как штык после завтрака был в музклубе. Ясно выражаюсь?"
    th "Ох!"
    "Я отступил на шаг, примирительно выставив ладони, чтобы пресечь нападки рыжеволосой пионерки."
    me "Да приду я, куда мне деваться?"
    "Задним числом я подумал, что при плохом настроении я никуда не явлюсь, и будь что будет."
    "Алиса прямо воспылала патриотическими чувствами к этому кружку."
    th "С чего бы?"
    show mi grin pioneer close at cleft with dspr
    "К нам подскочила Мику."
    mi "Семён! Мы уже всё решили! Я тут рассказала Алисе, как ты сегодня убежал от меня, и ей это совсем не понравилось..."
    me "Не понимаю, почему её вообще заботит моё отношение к музклубу?"
    show dv guilty pioneer2 close at cright with dspr
    dv "Хм!"
    show mi happy pioneer close at cleft with dspr
    mi "Я же говорю, всё решено! Алиса сдаст мне половину нормативов, а вместо остальных будет учить тебя играть на гитаре... Мы с ней разделили обязанности по руководству кружком."
    me "Э-э?.. Но я умею, только забыл немного..."
    show dv angry pioneer2 close at cright
    show mi laugh pioneer close at cleft
    with dspr
    mi "Вот, значит будете вместе вспоминать, как! Только не отлынивай, Семён, мы договорились. Алиса обещала взяться за тебя!"
    "Я не без трепета взглянул на Двачевскую, всё ещё сердитую, но полную решимости."
    show mi happy pioneer close at cleft with dspr
    th "Ох, на что же я подписался? Дался мне этот кружок!"
    "Обычно в карикатурных историях ботаника на пути из музыкалки подстерегают гопники с гнусными намерениями, но тут Алиса никого не подстерегает, а сама будет ходить в музклуб..."
    show mi smile pioneer close at cleft with dspr
    mi "Скоро отбой, так что пойдёмте быстрей!"
    show dv surprise pioneer2 close at cright with dspr
    dv "Куда?"
    show mi grin pioneer close at cleft with dspr
    mi "Зубы чистить! Я сбегаю к себе за щёткой и пастой, встретимся около умывальников."
    show dv grin pioneer2 close at cright with dspr
    "Алиса перестала хмуриться из-за меня."
    dv "Ой, ну ведь рано же!"
    show mi happy pioneer close at cleft with dspr
    mi "Я хочу ещё немного поработать над песнями перед сном."
    show mi smile pioneer close at cleft with dspr
    mi "Увидимся!"
    "Она махнула нам рукой и убежала."
    hide mi with dissolve
    show dv normal pioneer2 close at center with dissolve
    me "Ну, я тоже собирался готовиться к отбою, всё равно других планов на вечер нет..."
    "Алиса пожала плечами."
    dv "Ладно, я приду через пять минут."
    hide dv with dissolve
    "Я зашагал в сторону жилых улиц, как вдруг..."
    dv "Семён!!!"
    me "Что ещё?!"
    show dv angry pioneer2 at center with dissolve
    "Я с тревогой обернулся."
    dv "Ты зачем Мику всё разболтал?"
    me "Всего лишь решил помочь, раз ты так хотела заполучить гитару. Видишь, с Мику несложно договориться, правда?"
    show dv shy pioneer2 at center with dspr
    dv "Ага... Но не то чтобы я тебя просила об этом!"
    "Она зарделась, а я переполнился самодовольством."
    me "Вот! Иногда к другим людям надо прислушиваться."
    show dv angry pioneer2 at center with dspr
    dv "Да ладно?{w=0.4} А тебе надо помнить, что не всем нравится, когда кто-то пытается решать вопросы за них."
    dv "Твоё счастье, что ты не попал в ситуацию, когда услужливый дурак опаснее врага."
    show dv normal pioneer2 at center with dspr
    "Выговорившись, она вздохнула."
    me "Значит, я прощён?"
    dv "Пока что да."
    "Буркнув это, она пошла к себе домой, как ни в чём не бывало."
    hide dv with dissolve
    "......"
    show mi normal pioneer far at center with dissolve
    "Навстречу мне уже возвращалась Мику с целлофановым пакетиком, где болтались щётка с тюбиком пасты."
    show mi scared pioneer at center with dspr
    mi "Как, почему ты ещё тут?"
    me "Пардон, мы с Алисой задержались на пару слов. Скоро буду!"
    hide mi with dissolve
    "Я сразу припустил бегом."
    window hide
    stop music fadeout 2
    scene black
    with dissolve
    "........."
    window hide
    #TODO (к этапу работ по графике): тут должен быть ночной bg с умывальниками (ext_washstand_night). Пока его нет, будет использоваться предыдущий фон.
    scene bg ext_musclub_night_fog
    with dissolve
    play music music_list["sweet_darkness"] fadein 2
    window show
    "К умывальникам из нас троих я пришёл последним."
    "Окружённая соснами площадка погрузилась бы в кромешную темноту, если б не одинокий фонарь поблизости, под яркой лампой которого вилась мошкара."
    show mi normal pioneer at cleft
    show dv normal pioneer2 at cright
    with dissolve
    "Кроме Алисы с Мику, ждавших меня, здесь были и другие пионеры. Один за другим или парами они задерживались у рукомойников, чтобы почистить зубы перед сном и уходили."
    show dv smile pioneer2 at cright with dspr
    dv "Явился, наконец. Ну, ты чего там застрял?"
    me "Снова не мог решить, что взять — зубную пасту или порошок. И снова оставил пасту."
    "Двачевская едва заметно наклонилась ко мне."
    show dv laugh pioneer2 at cright with dspr
    dv "Что, мазать кого-то собрался, хулиган?"
    me "Может быть... Для чего ещё паста в пионерлагере?"
    show dv normal pioneer2 at cright with dspr
    "Я встал за умывальником, доставая щётку с баночкой, Мику и Алиса тоже присоединились."
    show mi sad pioneer at cleft with dspr
    mi "А мне зубной порошок не нравится, он на зубах скрипит, и брызг много!.." 
    me "Так надо меньше болтать!"
    show dv smile pioneer2 at cright with dspr
    dv "Слишком неженка, Мику?"
    "Алиса с иронией посмотрела на девочку, а та почему-то начала смущаться."
    show mi shy pioneer at cleft with dspr
    mi "А...{w} Я... Ах...{w} Наверно, да!.."
    show dv normal pioneer2 at cright with dspr
    dv "Я считаю, порошок лучше отбеливает зубы, мне после сигарет самое то."
    show mi smile pioneer at cleft with dspr
    if (d2_dv_fight == False):
        show dv angry pioneer2 at cright with dspr
        dv "Сигарет, которые не так давно куда-то пропали."
        "...И если Двачевская подтрунивала над Мику, то я же был удостоен уничтожающего взгляда."
        th "Моя вина, но как Алиса догадалась?"
        "С полным безразличием на лице, не выдавая себя, я никак не ответил ей, заткнув рот зубной щёткой, чтобы не сболтнуть лишнего."
        th "Ох, вот оно что!"
        "Минут пятнадцать назад я курил, и от моих пальцев заметно тянуло табаком. Достаточно было немного постоять около меня, чтобы всё понять."
        th "Надо было сразу в душ сходить..."
        show dv normal pioneer2 at cright with dspr
        "И то, что Алиса ещё не прикончила меня на месте, слабо утешало."
    show mi laugh pioneer at cleft with dspr
    mi "Паста — другое дело! У нас в Японии продают кучу классных паст разных цветов и вкусов — это как с дешёвыми сластями. Мне нравится та, что со вкусом киви!"
    show mi sad pioneer at cleft with dspr
    mi "Обидно, что с зелёным луком до сих пор нет... Больше всего такую хочется!"
    me "Ха, всё правильно, как раз после острого, лука и чеснока обычно жуют жвачку или чистят зубы. Какой смысл в луковом аромате?"
    mi "В том, что он бы стал моим самым любимым!"
    "Огорчённая Мику крепко зажмурилась."
    me "Лучше расскажи, как тебе удалось уговорить Алису?"
    show dv angry pioneer2 at cright with dspr
    dv "Эй, Семён, я всё слышу. Не надо шептаться у меня за спиной!"
    me "Ну, или ты расскажи. Мне интересно!"
    show dv shy pioneer2 at cright with dspr
    dv "Вот ещё! Ничего особенного не было..."
    show mi grin pioneer at cleft with dspr
    mi "Неправда! Вообще-то я зыбыла запереть дверь кружка, поэтому сразу после чаепития вернулась к клубу...{w} И натолкнулась на выходящую Алиску с гитарой в руках!"
    show mi happy pioneer at cleft with dspr
    me "А, значит, ты всё-таки решила пойти разбойным путём?"
    show dv sad pioneer2 at cright with dspr
    "Я повернулся к Алисе. Она, похоже, болезненно восприняла свой фейл и молча чистила зубы."
    "Мику подождала, когда пара незнакомых мне пионеров не пройдёт мимо, но всё равно заговорила тише."
    show mi grin pioneer at cleft with dspr
    mi "Я ей сказала, что уносить гитару и готовить песню для концерта неправильно! Вне клуба наши ребята быстро разузнали бы про секрет, и сюрприз бы не получился. Правда, Алиса?"
    dv "Угу..."
    "Она склонилась к умывальнику."
    mi "Играть не в лагере не вариант, да, Алиса?"
    show dv normal pioneer2 at cright with dspr
    dv "Вообще-то, вариант."
    me "Могу напомнить про пенёк и дятлов."
    show dv angry pioneer2 at cright with dspr
    "Рыжая пионерка скривила лицо."
    show mi sad pioneer at cleft with dspr
    mi "А я не поняла..."
    "Я пересказал ей тот момент из нашего разговора с Двачевской у сцены."
    show dv normal pioneer2 at cright
    show mi laugh pioneer at cleft
    with dspr
    mi "А-а! Конечно, зачем играть, если некому слушать? Поэтому я в клубе открываю окно! Кто-то услышит, кому-то понравится! А одному всегда можно играть у себя дома до отбоя, но Алиса, наверно, устаёт и ей вечером будет лень разучивать песни на гитаре? Правда, Алиса?"
    show dv surprise pioneer2 at cright with dspr
    "Но Мику ошиблась, и Двачевская встретила её предположение с чистым удивлением."
    dv "Лень? Нет, играть на гитаре не будет лень.{w} Погоди, Мику, значит, я смогу носить её к себе в палату?"
    show mi grin pioneer at cleft with dspr
    mi "Ну, пока ты член музыкального кружка, я думаю, что да. Ольга Дмитриевна мне сказала, что за сохранность инструментов мы несём общую ответственность!"
    show dv smile pioneer2 at cright with dspr
    "Губы Алисы тронула победная улыбка."
    dv "Отлично! Ты не беспокойся, я не разломаю гитару."
    me "А на Дне самодеятельности? Для рок-концерта нужен вызывающий перфоманс и одобрительные вопли зрителей..."
    show dv laugh pioneer2 at cright
    show mi shocked pioneer at cleft
    with dspr
    dv "...И гневные крики вожатых. Мне нравится идея!"
    "Шокированная до глубины души Мику забормотала что-то вроде «С-семён! Так нельзя!»."
    me "Спокойно, спокойно! Мы всего лишь фантазируем."
    show dv grin pioneer2 at cright with dspr
    dv "Ничего подобного! Рок-концерт будет! И рок-бэнд!"
    me "Что? Какой бэнд? Я думал, ты исполнишь на сцене какую-нибудь хорошую песню соло под гитару, и всё на этом."
    show mi grin pioneer at cleft with dspr
    "Мику пришла в себя."
    mi "Ой, я тебе ещё не говорила? Мы с Алисой выступим вместе!"
    me "Да? Вы поразительно быстро {i}спелись{/i} за один вечер, или я что-то упускаю?"
    show mi happy pioneer at cleft
    show dv angry pioneer2 at cright
    with dspr
    "Алиса ткнула меня пальцем в щёку."
    dv "Это тебя не касается."
    "Я мельком взглянул на невинно улыбающуюся Мику, силясь понять, о чём не желает говорить Двачевская."
    show mi smile pioneer at cleft with dspr
    mi "Может быть, ты тоже хочешь с нами?{w} Давай, соглашайся!"
    show dv smile pioneer2 at cright with dspr
    me "Вы кого попало собирать в группу будете?"
    show mi angry pioneer at cleft with dspr
    "Мику обиделась."
    show mi rage pioneer at cleft with dspr
    mi "Почему кого попало? Ты ведь тоже участник музыкального кружка!"
    me "Но..."
    show mi grin pioneer at cleft with dspr
    mi "Алиса тебя натаскает, будешь играть не хуже меня!"
    th "Она предвидела мою отговорку!"
    show mi smile pioneer at cleft with dspr
    "Алиса перестала чистить зубы."
    show dv normal pioneer2 at cright with dspr
    dv "Я не против, чтобы ты присоединился, но если не будешь появляться в кружке, до конца смены не доживёшь."
    me "Избавь меня от этого, убей прямо сейчас."
    show dv rage pioneer2 close at right with dspr
    "Алиса схватила мою руку, потянув на себя." 
    dv "Слушай, я зря что ли вступила в клуб? Зачем ты впрягался за меня? Короче, будешь фронтменом группы!"
    "Она высказала это с такой яростью, что едва не перекусила зубную щётку."
    show mi surprise pioneer at cleft with dspr
    mi "!.."
    "Я заметил — Мику сильно удивилась напору и наглости Алисы."
    "...И еле видимую краску стыда на её лице — от Мику не укрылось не совсем приличное положение моей руки в объятиях Двачевской."
    stop music fadeout 1
    play music music_list["always_ready"] fadein 2
    "Мику будто боролась с какими-то мыслями в голове, а затем, решившись, точно так же схватила мою левую руку, и я дёрнулся в её сторону..."
    show mi laugh pioneer close at left
    show dv surprise pioneer2 close at right
    with dspr
    mi "Если Семён будет фронтменом, то кроме гитары ему понадобятся уроки вокала!{w} Я помогу тебе с этим!"
    show dv grin pioneer2 close at right
    show mi surprise pioneer close at left
    with dspr
    "Алиса опять дёрнула меня, но уже помягче."
    dv "Только пусть сначала выучится перебирать струны."
    show mi happy pioneer close at left with dspr
    "Мику потянула меня обратно."
    mi "Но вокалист может обойтись микрофоном, остальное на плечах музыкантов и подтанцовки!"
    show dv rage pioneer2 close at right
    show mi surprise pioneer close at left
    with dspr
    "Рывок Алисы был таким сильным, что ещё немного, и я бы сбил её с ног."
    dv "Это называется попса!"
    show mi angry pioneer close at left
    show dv surprise pioneer2 close at right
    with dspr
    "Мику понадобилось значительное усилие, чтобы вернуть меня назад."
    me "Разве я согласился на ваши безумные идеи?"
    show dv grin pioneer2 close at right
    show mi smile pioneer close at left
    with dspr
    "Я полетел направо."
    dv "Боюсь, тебе придётся."
    "А потом налево."
    show mi happy pioneer close at left with dspr
    mi "Вместе сочиним песни и название группы...{w} Неужели тебе никогда не хотелось подобного?"
    me "Э-э..."
    "Направо."
    show mi normal pioneer close at left with dspr
    "Налево."
    "Девочки почему-то улыбались." 
    "И я понял, что все мои беды — это всерьёз и надолго."
    window hide
    stop ambience fadeout 1
    stop music fadeout 2
    $ d2_mi_dv_evening = True
    $ lp_dv = lp_dv + 1
    $ lp_mi = lp_mi + 1
    $ d2_girls_event = (d2_girls_event) + (1)
    jump d2_bed_time

label d2_clubs_evening:

    scene bg oldmap
    window show
    th "Нет смысла туда идти, кружки и клубы закрываются до ужина."
    window hide
    $ disable_current_zone()
    jump d2_evening_map

label d2_camp_entrance_evening:
    
    scene bg oldmap
    window show
    if d1_un_evening:
        th "Схожу к стоянке, может быть, встречу Славю, если не поздно и она уже не закрыла ворота."
    else:
        th "Выйти на дорогу к лагерю что ли? Наверно, ворота уже заперли на замок."
    window hide
    $ reset_chibi("camp_entrance")
    scene black
    with dissolve
    show screen central_text("День 2 — Лесная дева")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_clubs_night
    with dissolve
    play music music_list["sweet_darkness"] fadein 2
    window show
    "По пути я ненадолго остановился у первого корпуса кружков, решив проверить, смогу ли попасть внутрь."   
    th "Хм. Закрыто. А утром казалось, что «юные техники» здесь даже ночуют."
    if (tech_club == False):
        "Впрочем, не нужно заниматься чужими роботами — и на этом спасибо."
    "..."
    scene bg ext_no_bus_night
    with dissolve
    "Я оказался прав: на воротах в петле чуть выше советской звезды висел замок."
    th "Чистая формальность, через такой забор переберётся и школьник."
    "Я, конечно, перелезать не стал, всего лишь прислонился к ограждению, чтобы посмотреть в узкую брешь между забором и аркой."
    "В темноте сумерек едва ли что-то можно было различить дальше гипсовых статуй пионеров, только силуэты деревьев на фоне звёздного неба, но я помнил, что днём здесь очень красиво."
    "За воротами в поздний час делать было нечего. Я мог представить себе, как бреду с фонариком куда подальше от лагеря в неизвестном направлении, но воплощать в жизнь скоропалительные решения я не собирался."
    "И, согласно расписанию лагеря, мне оставалось только почистить зубы, сходить в душ и готовиться ко сну."
    "Подумав немного, я пошёл назад."
    window hide
    stop music fadeout 2
    scene bg ext_clubs_night
    with dissolve
    play music music_list["gentle_predator"] fadein 3
    window show
    me "!.."
    "Не успел я подойти к зданиям кружков, где вчера меня встретили Ульяна с Леной, как у второго корпуса в свете лампы мелькнула чья-то фигура на повороте к домикам младшего отряда."
    show sl surprise pioneer far at cright with dissolve
    th "Славя?"
    hide sl with dissolve
    "Я узнал девочку, но не окликнул её, а двинулся следом."
    scene bg ext_path_night
    with dissolve
    play ambience ambience_forest_evening fadein 0
    show sl normal pioneer far at center with dissolve
    "Славя быстрым шагом уходила куда-то в темень леса за корпусом. Это вызвало у меня смутное беспокойство и в то же время любопытство."
    th "Что она забыла в глухом уголке лагеря, когда уже время отправляться на боковую?"
    scene bg ext_path2_night
    with dissolve
    show sl normal pioneer far at center with dissolve
    "С осторожностью, чтобы ненароком не привлечь её внимания, я неотступно шёл за Славей, пока впереди не блеснул маленький лучик фонаря."
    "Из-за этого мне пришлось спрятаться за ближайшим деревом."
    "Славя осветила себе частокол забора, к которому мы пришли. Пионерка отыскала нужную доску, сдвинула её и скрылась в образовавшемся проёме."
    hide sl with dissolve
    "Доска беззвучно стала на место."
    th "Надо поторопиться, чтобы не потерять Славю из вида!"
    "Я быстро нашёл скрытый лаз и выбрался за территорию лагеря."
    show sl normal pioneer far at center with dissolve
    "Пятнышко света ещё мелькало впереди, и я поспешил нагнать девочку, идя по обочине рядом с тропкой, оказавшейся протоптанной, словно тут ходили не раз..."
    th "Да это же нарушение всех мыслимых правил! И кем?"
    "От Слави я такого не ожидал."
    if d1_us_chase:
        "Сначала я решил, будто Славя хотела убежать из лагеря, но потом вспомнил её слова, как ей нравится здесь."
        "Нет, здесь явно была другая причина."
    "Мне казалось, что мы зашли далеко. Настолько далеко, что я всерьёз подумывал о том, чтобы развернуться и пойти обратно. Однако я был не в силах устоять перед манящей тайной."
    "Свет фонарика давно погас, пионерка уже несколько минут обходилась без него, но я смог проследить за ней."
    stop music fadeout 4
    "Славя на миг остановилась у едва заметного разветвления тропинки в чаще леса, и я бы даже не узнал о нём, если бы девочка не свернула на поляну, полную светлячков, из-за чего её стало очень хорошо видно."
    stop ambience fadeout 1
    scene cg d2_slavya_forest
    with dissolve2
    play music music_list["forest_maiden"] fadein 1
    "Вдруг Славя преобразилась..."
    "Её движения замедлились и стали ещё плавнее и грациознее."
    "Теперь она словно плыла сквозь заросли высокой травы."
    "Каждый шаг Слави делался всё более танцевальным."
    "Я продолжал преследовать её, но скрывался уже не только для того, чтобы остаться незамеченным, а ещё потому что не хотел разрушать гармонию момента."
    "Славя сейчас была частью природы..."
    "Вокруг неё со всех сторон кружились светлячки. Их зелёно-жёлтый свет окутывал Славю каким-то волшебным сиянием."
    "Мягкая трава нежно обнимала длинные ноги девочки."
    "Прикрыв глаза, Славя полностью отдалась власти танца. Она стала расстегивать рубашку, бросила мешавший ей пионерский галстук на траву, не останавливаясь ни на секунду."
    "Косы девочки струились в прохладном воздухе."
    "Я жадно ловил этот момент, стараясь запомнить всё без исключения, потому что я такое видел впервые."
    "...Я был свидетелем чего-то первобытного и по-своему прекрасного..."
    "Славя расстегнула последнюю пуговицу и и откинула белую рубашку на ветви куста с обочины, совсем недалеко от меня..."
    "За поляной следовал склон, по которому спустилась девочка, и только теперь я понял, куда мы пришли."
    #stop music fadeout 3
    scene bg ext_path2_night
    with dissolve
    "Я заставил себя остановиться. Дальше идти было нельзя, иначе меня бы заметили."
    "Это был травянистый берег реки, полосой устремлявшийся в темноту."
    "В ярком свете луны я разглядел на воде внушительных размеров остров с лесом."
    "Он находился так близко, что тем самым образовывал узкий, тесный пролив и удачно скрывал этот чудный уголок от посторонних глаз."
    "...Но не от моих..."
    show sl smile pioneer far at center with dissolve
    "Я, затаив дыхание, наблюдал за Славей."
    show sl smile swim far at center with dissolve
    "Под луной было видно, как девочка на ходу сняла туфли, выскользнула из юбки с трусиками..."
    "На траву к ним затем упал бюстгальтер."
    scene cg d2_sl_swim
    with dissolve2
    "Полностью нагая, Славя сошла в воду."
    "Сначала по щиколотки, остановилась, привыкая к прохладе реки. Славя, глядя вверх, подняла руку, точно приветствуя эту ночь, луну и небо, а природа отвечала ей, вторила бессловесно, принимая девочку."
    th "О чём она думает? Можно только догадываться, но я уверен — она восхищена тем, как прекрасно это место."
    "А я, не без чувства вины за подглядывание, восхищался тем, как стройно её тело."
    "Несколько шагов, и теперь она стояла в реке по пояс."
    "Поводив руками по тёмной глади, Славя зачерпнула воды, чтобы омыть плечи и грудь."
    th "Ох!.."
    "А потом, склонившись, она плавно оттолкнулась и поплыла вперёд, рассекая мелкие волны."
    "Казалось бы, пора брать ноги в руки и уходить отсюда незамеченным, пока есть возможность, но я словно прирос к земле, всё ещё пригибая ветвь куста, за которым прятался."
    "Глубокое, животрепещущее любопытство одержало верх над смущением, и я, поколебавшись, решил дождаться, когда Славя пойдёт назад."
    stop music fadeout 2
    th "Не будет же она тут всю ночь? Ольга Дмитриевна хватится меня..."
    if (d1_us_chase == False):
        "Что-то шевельнулось в памяти."
        scene bg ext_square_day_bw
        with fade
        show sl smile2 pioneer close bw at left
        show mt normal pioneer close bw at right
        with dissolve
        sl "Поешь — сразу силы вернутся! А потом и погулять можно, сходить искупаться... Ой!"
        show sl surprise pioneer close bw at left 
        show mt surprise pioneer close bw at right
        with dspr
        mt "Нет, Семён, у нас с этим строго. На пляж разрешено только утром в хорошую погоду, вечером — когда жарко. Я поведу весь старший отряд, когда будет время.{w} А ты, Славя, не сбивай пионера с графика. Я понимаю, что ты-то... Но не Семён."
        sl "Извините, Ольга Дмитриевна."
        scene cg d2_sl_swim
        with dissolve2
        th "Она знает, она знает!"
        "Я с ужасом представил, как вожатая с успехом выпытывает, где я был и что делал."
        "Но я быстро успокоился — я ни за что не признаюсь в этом, к тому же, вряд ли Ольга Дмитриевна была в курсе, что для Слави купальник ночью — абсолютно ненужная вещь."
    play music music_list["forest_maiden"] fadein 2
    #play music music_list["gentle_predator"] fadein 2
    "Сцена купания была откровением: помощница вожатой прямо-таки наслаждалась свободной минутой в беззастенчивом единении с окружающим миром."
    "В бликах серебристой дорожки на реке то и дело мелькала обнажённая спина, ягодицы и ноги."
    "Я заворожённо наблюдал, как Славя грациозно разворачивается и ныряет под воду."
    "Можно было подумать, она приходит сюда каждый день. О таком Славю не спросишь прямо!"
    "Чтобы убедиться, надо несколько вечеров заранее поджидать её у того забора и идти за ней по пятам."
    "И если сегодняшнее подсматривание было случайным, то последующие станут маленькими преступлениями."
    "Я тяжело сглотнул, поддаваясь соблазнительной мысли."
    "За эти минуты любования телом пионерки в моих шортах стало ужасно тесно."
    "Ещё немного, и молния на них сама расстегнётся..."
    "..."
    scene bg ext_path2_night
    with dissolve
    show sl shy body far at center with dissolve
    "Наконец, Славя вдоволь накупалась и вышла на берег, выжимая и оправляя свои длинные косы. Её мокрая кожа блестела в лучах почти полной луны."
    show sl normal body at center with dspr
    "Идя по траве босыми ногами, пионерка вернулась к одежде, подобрала нижнее бельё с юбкой и школьные туфли."
    "Славя была совсем рядом."
    "Меня словно током ударило."
    th "Сейчас перебегу туда, где она оставила рубашку, и тогда я увижу Славю ещё ближе..."
    stop music fadeout 3
    "Второпях позабыв об осторожности, я отпустил ветку."
    play sound sfx_bush_leaves
    "Шурх!"
    show sl surprise body at center with dspr
    "Славя замерла, инстинктивно прикрыв грудь, и на миг мне почудилось, что мы встретились взглядами."
    hide sl with dspr
    play music music_list["awakening_power"] fadein 1
    play sound_loop sfx_run_forest fadein 1
    "Я дёрнулся бежать. Что-то громко хрустнуло под ногой."
    sl "Кто..."
    "Но что она произнесла точно, я не расслышал, потому что со всего духу помчался назад, стараясь ни во что не влететь."
    th "Она не видела меня! Этого не могло случиться!"
    window hide
    scene bg ext_path_night with fade
    $ renpy.pause(1)
    scene bg ext_clubs_night with fade
    $ renpy.pause(1)
    scene bg ext_square_night with fade
    #scene bg ext_houses_night
    window show
    "......"
    scene bg ext_house_of_mt_night
    with fade
    "К дому номер семнадцать я прилетел на всех парах, чудом преодолев незнакомый мне путь назад не сбившись. Сердце бешено стучало в груди, грозясь сломать рёбра."
    th "Обеспечить...{w=0.5} себе...{w=0.5} алиби!.."
    stop sound_loop fadeout 1
    scene bg int_house_of_mt_night
    with fade
    play sound sfx_open_door_strong
    show mt surprise pioneer at center with dspr
    "Я ворвался в палату."
    mt "Семён, что с тобой?"
    me "...Я... в душ... Скоро вернусь!"
    "Немедленно отыскав полотенце для тела, я кинулся к выходу."
    scene bg ext_playground_night
    with fade
    stop music fadeout 3
    "Меньше, чем через минуту я был у спортплощадки, не доходя до неё, я зашёл в невысокое здание с раздевалками и душевыми."
    "..."
    play sound_loop sfx_water_sink_stream fadein 1
    #TODO (к этапу работ по графике): тут должен быть ночной bg с душевым помещением (int_showersroom_night).
    scene anim prolog_2
    with dissolve
    "........."
    "Б-г знает, сколько времени я провёл, стоя под душем, и сколько раз плескал воду ладонями себе на лицо, пытаясь успокоиться."
    "Вспоминать то приятное глазу купание девочки было трудно — всё перечеркнуло моё фиаско в конце. Я не смел фантазировать о Славе, предполагая, что она уже прекрасно знает, кто следил за ней."
    "Чувство стыда, ранее дремавшее, теперь проснулось и мучило меня."
    th "Блджад. Проклятье!"
    th "Надо было не оставаться там, а уходить, пока Славя плавала."
    "За стыдом последовала более крамольная мысль: после этого вечера пионерка вряд ли будет ходить на тот берег, и я больше не смогу наблюдать за её тайным единением с природой."
    th "Что же я наделал?!"
    "..."
    "......"
    stop sound_loop fadeout 1
    "Придя в себя, я закрутил душевые рукоятки, обтёрся и оделся. Рубашку я понёс в руке, а полотенце накинул на плечи."
    scene bg ext_playground_night
    scene bg ext_house_of_mt_night
    with fade2
    play music music_list["sweet_darkness"] fadein 0
    "Не спеша я вернулся к домику."
    show sl normal pioneer at center with dissolve
    "У меня ёкнуло сердце, когда я увидел Славю около зарослей сирени."
    show sl smile pioneer at center with dspr
    sl "Добрый вечер, Семён!"
    th "Главное не выдать себя, не подать виду...{w=0.4} Спасибо, что ты сейчас одетая!"
    me "Ага... добрый, хороший вечер, спать даже не хочется."
    th "Ещё бы, уснёшь после такой встряски."
    "Славя обратила внимание, что я тёр полотенцем волосы над ухом."
    show sl normal pioneer at center with dspr
    sl "Что делал? Купался?"
    "Она спросила это совершенно спокойно, и я даже не уловил бы подвоха, не будь свидетелем бегства Слави на речку."
    "Но я-то всё понял."
    th "Она подозревает меня!"
    me "Нет, я только что из душа."
    "Девочка чуть кивнула, будто соглашаясь с чем-то про себя."
    "Я чувствовал близость скорейшего разоблачения."
    show sl happy pioneer at center with dspr
    sl "А по мне так вечером самое время ходить купаться. Когда вода начинает остывать после жаркого дня, она как парное молоко."
    sl "Это расслабляет!"
    th "...И весьма раскрепощает..."
    show sl smile2 pioneer at center with dspr
    "Должно быть, я покраснел, слыша от неё такие слова, но после тёплого душа я был разгорячён, и Славя не заметила моей реакции."
    me "Откуда мне знать, я никогда так не делал."
    show sl surprise pioneer at center with dspr
    sl "Что, совсем-совсем никогда?"
    me "Именно так."
    show sl smile pioneer at center with dspr
    sl "Многое теряешь!.."
    me "Наверно."
    th "Шанс найти её завтра на том же месте и снова без одежды я точно потерял."
    me "По-моему, здесь в лагере не получится без нарушений: вожатые не разрешают самовольные купания, правильно?"
    "Славя почему-то замялась."
    sl "Ну, если предупредить Ольгу Дмитриевну, то я могла бы взять на себя ответственность и присмотреть за тобой."
    if d2_walk == 1:
        th "В самом деле, потому что Славя у вожатых на хорошем счету."
    "Но идею я не мог с лёгкостью одобрить. Я боялся, что внезапная заинтересованность выдаст меня с головой."
    th "А может, наоборот, отказываясь от заманчивого приключения, я только больше навлекаю на себя подозрение?"
    "Тревожась, я совсем запутался и не знал, как выйти сухим из этой ситуации."
    if (d1_us_chase == False):
        me "Ольга Дмитриевна вчера уже намекнула, что с купанием всё строго."
        sl "Я помню. И всё-таки, я бы поговорила с ней ещё раз."
    sl "...Или ты сам попробуй отпроситься."
    "Я задумался."
    me "У вожатой пока нет ко мне доверия.{w} Представь себе: заявляется в лагерь какой-то мальчик-пионер и тут же с первого дня хочет поблажки вопреки правилам, общим для всех."
    show sl sad pioneer at center with dspr
    me "Мне кажется, Ольга Дмитриевна из принципа не разрешит." 
    sl "Да, это в её духе."
    "Славя явно была не рада, что нельзя иначе."
    th "Неужели она вправду желает, чтобы я сходил на реку поздним вечером испытать, каково это?"
    th "Так, искренне, без мыслей о том, кто подсматривал за ней, и проверить меня. Чтобы я не терял многого..."
    th "Она ведь только что, получается, поделилась своей тайной."
    me "..."
    me "Может быть, потом я спрошу у Ольги Дмитриевны, когда буду точно уверен, что она согласится. Конец смены ещё не скоро."
    show sl smile pioneer at center with dspr
    sl "Только не забудь!"
    me "Хорошо."
    me "А сейчас...{w} А сейчас уже поздно."
    show sl surprise pioneer at center with dspr
    sl "Верно, режим дня нельзя нарушать."
    show sl normal pioneer at center with dspr
    sl "Спокойной ночи, Семён, утро вечера мудренее!"
    me "...Спокойной ночи."
    hide sl with dissolve
    "Разоблачения, которого я так опасался, не случилось, и я вздохнул с облегчением."
    if more_fiz:
        th "Утро вечера мудренее..."
        "Что-то побудило меня остановить Славю."
        me "Подожди!"
        show sl serious pioneer at center with dissolve
        sl "Да, Семён?"
        "Девочка посерьёзнела, наверно, ожидая от меня признания в содеянном."
        me "Я же совершенно забыл сообщить тебе хорошую новость..."
        show sl surprise pioneer at center with dspr
        me "Медсестра выписала мне разрешение на дополнительную физическую нагрузку, так что я могу бегать по утрам.{w} Для выработки силы воли!"
        show sl laugh pioneer at center with dspr
        "Славя вспомнила наш разговор около умывальников и рассмеялась."
        sl "А, ты об этом? Здорово!"
        show sl smile2 pioneer at center with dspr
        sl "Если что, я встаю полседьмого. Договорились?"
        me "Конечно..."
        show sl smile pioneer at center with dspr
        sl "До завтра, Семён."
        me "Пока."
        "Я махнул ей рукой на прощание."
        hide sl with dissolve
        "И только сейчас мне стало совсем легко."
    "Но всё равно одна загадка не давала покоя: догадалась ли Славя, кто за ней следил?{w} Вот же вопрос!"
    window hide
    stop music fadeout 2
    $ d2_sl_evening = True
    $ lp_sl = lp_sl + 1
    $ d2_girls_event = (d2_girls_event) + (1)
    jump d2_bed_time
    
label d2_dining_hall_evening:

    scene bg oldmap
    th "Спасибо, ужина мне вполне хватило."
    $ disable_current_zone()
    jump d2_evening_map
    
label d2_sport_area_evening:
    
    $ reset_chibi("sport_area")
    scene black
    with dissolve
    show screen central_text("День 2 — Редкое явление")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg ext_playground_night
    with dissolve
    play music music_list["sweet_darkness"] fadein 1
    play ambience ambience_camp_center_night fadein 2
    window show
    "Сейчас, поздним вечером, у спортивных площадок не слышалось гомона играющих пионеров, только стрекотание ночных насекомых."
    "Большинство из детей уже разошлось по домикам, и здесь я был аболютно один возле футбольного поля."
    "Дорога от ворот, разделявшая поле и пляж, оканчивалась здесь тупиком и высоким забором. Тут же отсутствовали фонарные столбы, так что вместо спасительных островков света повсюду царила темнота."
    "Лишь бледное свечение луны кое-как позволяло рассмотреть, куда я шёл."
    "Сначала передо мной выросла рама футбольных ворот с сеткой, а затем турники."
    th "И хорошо, что темно — никто не увидит моих фейлов. И-и... раз!"
    "Я подпрыгнул, схватился за турник и стал подтягиваться."
    "На счёт «семь» я выдохся и спрыгнул. Снова повторять эти телодвижения не хотелось — я наконец ощутил, насколько устал за день."
    "В иной ситуации я бы попинал мяч в одиночестве, да только где его взять? Крытый спортзал наверняка был заперт на ключ."
    "Убедившись, что сетка ворот крепко сплетена, я взобрался по ней и свесил уставшие ноги за перекладину."
    "Вечер был малооблачным, на небе уже ярко мерцали звёзды."
    th "Сейчас я к ним ближе, чем обычно...{w=.4} пусть всего на пару метров."
    "В свою прошлую жизнь я редко обращал внимания на звезды."
    "Я видел их либо мельком из окна, либо на нарисованном фоне какой-нибудь игры."
    "Но в городе, особенно в большом, небо всегда освещено иллюминацией. Здесь же всё было по-другому."
    "Ещё годы назад я мог бы проникнуться интересом к астрономии, но на сегодняшний день я оставил подобные увлечения где-то далеко, и потому не смог бы рассказать о звёздах что-то путное, только взглянув на небо."
    th "Да и какая разница? Болтаешь себе ногами в остывающем от дневного зноя воздухе и глядишь вверх — красота!"
    "Сидеть на сети было мягко, как в гамаке."
    "И тут на краю поля я заметил желтоватый свет фонарика и какое-то движение."
    show un normal pioneer far at left with dissolve
    "Я различил силуэт девочки, шедшей на футбольное поле — это была Лена."
    "Медленно шагая, в руке она несла продолговатую сумку, то ли от музыкального инструмента, то ли от чего-то ещё."
    show un normal pioneer at cleft with dissolve
    "Меня это заинтересовало."
    th "Может, скрасить ей вечер? Ей одной должно быть ужасно скучно."
    if d2_un_day:
        "А если вспомнить некоторую замкнутость Лены и мою собственную необщительность, то возник повод порасспрашивать девочку и разговорить её."
    "Глядя на Лену, я чувствовал, что у нас с ней есть что-то общее."
    "Мне тоже бывало неуютно посреди суеты, и я искал место, где можно побыть одному."
    stop music fadeout 2
    "Мы оба любили читать и..."
    "Я замечтался и моя рука поехала по перекладине!"
    hide un with dspr
    "Ничего не успев сообразить, я смачно шмякнулся с верхотуры — прямо на колени в песок!"
    play sound sfx_bodyfall_1
    with vpunch
    me "О, ч-чёрт!"
    "Ещё чуть-чуть, и я бы тюкнулся носом в землю."
    show un scared pioneer at cleft with dspr
    "Пионерка вскрикнула и от неожиданности едва не выронила сумку, неловко и с большим трудом прижав её к груди обеими руками, а в мою сторону метнулся луч фонарика."
    show un shocked pioneer at cleft with dspr
    un "А, п-привет, Семён..."
    show un sad pioneer close at center with dspr
    un "Не ожидала увидеть тебя здесь."
    play music music_list["lets_be_friends"] fadein 1
    "Она не сразу расслабилась, даже когда я поднялся и отряхнулся, взглянув на неё."
    "Глаза Лены выражали столько эмоций сразу!"
    "В них за нежностью и чувственностью была загадочность, а за испугом — даже капелька сострадания ко мне."
    "И что-то совсем уже тайное и невысказанное."
    th "Испуг!"
    me "Извини, что напугал. Я не хотел.{w} А... ап-чхи!"
    un "Всё нормально? Откуда ты... Честное слово, будто с неба упал!"
    me "Почти."
    "Я криво усмехнулся: так нелепо свалился, а Лена восприняла это как что-то возвышенное. Или я просто был чересчур хорошего мнения о себе."
    me "Забрался на футбольные ворота, не знаю, что меня надоумило...{w} Хотел на звёзды посмотреть."
    show un shy pioneer close at center with dspr
    un "Да? Вот совпадение!"
    "К Лене вроде вернулось самообладание, но она всё ещё чувствовала себя неуверенно."
    show un normal pioneer close at center with dspr
    un "Я... я тоже пришла сюда, чтобы поглядеть на звёздное небо."
    un "Вот... Даже принесла телескоп..."
    "Теперь она смогла взять сумку-чехол поудобней и больше не прижимала его к себе."
    me "Блин, а я-то и не понял сначала, думал, там саксофон или вообще оружие. Как в кино про гангстеров."
    show un smile2 pioneer close at center with dspr
    "Она повеселела."
    un "Не в этой жизни, поэтому сегодня у меня всего лишь телескоп."
    show un smile pioneer close at center with dspr
    me "Ох, я ведь сразу не спросил: тебе не тяжело нести его?"
    show un shy pioneer close at center with dspr
    un "Немного..."
    me "Помочь?"
    "Я машинально взялся за ручку сумки, коснувшись пальцев Лены, и между нами пробежала разряд тока."
    show un surprise pioneer close at center with dspr
    un "Ой!"
    me "Давай понесу."
    un "Спасибо... Но я уже на месте." 
    un "Я собиралась установить телескоп на краю поля. Вот здесь."
    show un shy pioneer at center with dspr
    "Мне показалось, что она не знала, куда деваться от смущения и поспешила скорей разложить наблюдательную технику."
    "Я пошёл за Леной. Она выбрала место на траве параллельно воротам и остановилась."
    show un normal pioneer at center with dspr
    "Присев на корточки, Лена отложила фонарик и раскрыла чехол." 
    me "Твой телескоп?"
    show un smile pioneer at center with dspr
    un "Нет, одолжила в кружке юных техников."
    show un normal pioneer at center with dspr
    un "Единственный телескоп на весь лагерь. Наверно, потому что здесь нет клуба по астрономии."
    "Я помог Лене поставить штатив и зажать трубу с оптикой в крепёжных петлях."
    me "Ну, клуб и при таких условиях можно сделать, был бы народ. Верно?"
    show un smile pioneer close at center with dspr
    un "Да, но я уже занята в стенгазете. Вряд ли я смогла бы потянуть кружок астрономии, я ведь просто любитель."
    un "Хотя, любители астрономии немало помогли развить эту науку. Да что там, многие серьёзные открытия принадлежат им."  
    "С направлением объектива и противовесами девочка справилась сама."
    me "А по-моему ты умело обращаешься с этой техникой. Не первый раз?"
    show un grin pioneer close at center with dspr
    un "У меня дома есть свой телескоп, но попроще."
    show un smile2 pioneer close at center with dspr
    un "Иногда я смотрю вечерами на звёзды просто так или когда запланированы какие-то интересные астрономические явления, как сегодня..."
    show un smile pioneer close at center with dspr
    "Лена пригнулась, чтобы поглядеть в окуляр телескопа, настраивая фокус."
    "Я не заметил на небе ничего особенного."
    th "Правда? Сегодня что-то должно быть?"
    "Только я хотел задать этот вопрос, как Лена позвала меня."
    show un smile2 pioneer close at center with dspr
    un "Вот, смотри, Полярная звезда! Она находится в созвездии Малой Медведицы..."
    show un smile pioneer close at center with dspr
    me "Это и я знаю. Малый Ковш и самая яркая звезда в хвосте."
    show un smile2 pioneer close at center with dspr
    un "А знаешь ли ты, что Полярная звезда — тройная звёздная система?"
    me "Разве?"
    show un smile pioneer close at center with dspr
    un "Пару лет назад выяснили, что у неё не один спутик, а два, просто второй расположен так близко, что для открытия понадобился космический телескоп."
    un "Дальний ты сам сможешь увидеть."
    hide un with dissolve
    "Девочка отошла, уступив мне место."
    scene anim stars_3o_bw
    with fade2
    "Я прильнул глазом к окуляру и увидел, как в маленьком тёмном диске среди россыпи точек-звёзд крестообразным бликом ярко мерцала белая звезда, а в некотором отдалении — ещё одна похожая, но гораздо меньше."
    un "Полярная звезда больше и ярче Солнца, и почти неподвижна для нас, потому чт..."
    "Лена вдруг снова вскрикнула, и я немедленно обернулся к ней."
    scene bg ext_playground_night
    with fade
    show un cry pioneer at center with dspr
    "Девочка села на траву, схватившись за ступню."
    un "К-кажется, ногу подвернула..."
    "Она всхлипула, а я включил фонарик. Оказалось, что пионерка наступила на увесистый неровный камень."
    "Если бы я с детства не играл в футбол во дворе и в школе, я бы не даже не понял, в чём дело, и списал бы всё на случайность. Этим камнем пионеры из спорткружка обозначали место пробивания углового, так как поле не было разлиновано белой краской."
    show un sad pioneer close at center with dspr
    "Отбросив злосчастный камень куда подальше, я присел рядом с Леной, на глазах у которой блестели слезинки."
    "Она выглядела по-детски беззащитной оттого, что ударилась в слёзы после малозначительной травмы, хоть и болезненной в первые секунды."
    me "Неудачное место мы выбрали..."
    if proficiencies ['sp_pers']>=2:
        me "Помассировать ногу? Станет лучше..."
        "Я почувствовал, как сердце ушло в пятки от своего внезапного предложения, потому что вспомнил слова матери из детства, когда я сам попал в такую же ситуацию, подвернув ногу."
        "Идея была неправильной, ведь окажись травма серьёзной, то я сделаю только хуже, осложнив её."
        show un cry_smile pioneer close at center with dspr
        "Но Лена слабо улыбнулась и согласилась."
        un "Если поможет, то пожалуйста!.."
        "Я решился, но только в качестве жеста внимания, чтобы отвлечь девочку."
        th "А если боль не пройдёт, поведу к медсестре."
        show un sad pioneer close at center with dspr
        "Лена согнула ногу в коленке, подставляя мне ступню."
        "Обладай я по-кошачьи острым зрением, я бы увидел белые трусики девочки."
        if sp_crg >= 2: 
            "Причём уже второй раз..."
        else:
            pass
        "Я мог небрежно бросить фонарик на траву так, чтобы его свет выхватывал для меня самый интересный вид, но сейчас, когда Лена в слезах, это было бы совсем неприлично с моей стороны."
        "Я снял сандалию и осторожно тронул стопу девочки. Интуитивно я пытался действовать как можно мягче, чтобы Лена снова не ощутила боль. Эту боль следовало загладить."
        show un surprise pioneer close at center with dspr
        "Через тонкий белый гольф пионерки я едва уловимыми прикосновениями растёр кожу по направлению к щиколотке и наоборот."
        show un sad pioneer close at center with dspr
        "Лена, борясь с неприятным ощущением, прислонила пальцы к губам, словно готовясь прикусить один из них, если станет больно."
        "Но этого так и не случилось."
    else:
        me "Подожди немного, должно пройти.{w} Если боль не утихнет, надо что-то делать..."
        un "Наверно... пойдём в медпункт?"
        me "Да, в таком случае без помощи Виолетты Церновны мы не обойдёмся."
        "..."
        "Лена чуть-чуть покачала ногой, проверяя, исчезла ли мучившая её боль."
    me "Всё нормально?"
    un "Похоже на то..."
    me "Значит, ничего плохого, и к медсестре являться не нужно, всё равно что оступилась."
    show un cry_smile pioneer close at center with dspr
    "Лена утёрла слёзы рукавом."
    un "Вот такая я неудачница."
    me "Неправда, я ничуть не лучше, брякнулся с ворот. С любым может случиться."
    th "Встретились два неудачника..."
    show un shy pioneer at center with dspr
    "Я помог Лене подняться и подобрал фонарик."
    me "Может, перенесём телескоп в другое место? В центр, например."
    show un sad pioneer close at center with dspr
    un "Там песок и будет неровно. Останемся тут."
    "Последние слова она произнесла так, будто спрашивала у меня разрешения, а не требовала. И ещё Лена теперь жалась так близко, словно только я был в состоянии уберечь её, если поблизости возникнет ещё одна напасть."
    me "Окей."
    stop music fadeout 1
    play music music_list["sweet_darkness"] fadein 2
    "Я вздохнул, и мы застыли около штатива с увеличительной трубой, не произнося ни слова. Между нами возникла та пауза, когда ни один, ни другой, не знал, как и чем нарушить молчание."
    if d2_un_day:
        th "Опять неловкая заминка."
    "Тому виной было не то стеснение, не то сложившаяся особенность характеров."
    "..."
    "Я скосил глаза на окуляр телескопа."
    me "Полярная звезда красивая..."
    show un shy pioneer close at center with dspr
    "На язык просился комплимент «Но не настолько, как ты...», однако я промолчал — это отдавало дешёвой романтикой из розово-мечтательных повестей для таких же розово-мечтательно настроенных девочек, учащихся в средней школе."
    "И к тому же, несмотря на всё, Лену я ещё недостаточно хорошо знал для подобных слов." 
    show un smile pioneer close at center with dspr
    un "Да... С неё я начинаю ориентироваться в карте созвездий."
    "Я уцепился за тему, чтобы помочь нам разговориться."
    me "Но ты ведь пришла глядеть не только на одну Полярную звезду? Ты что-то там говорила про астрономические явления. Расскажи мне о них."
    show un normal pioneer close at center with dspr
    un "Ну... Это любые изменения в космосе." 
    show un shy pioneer close at center with dspr
    un "Положение и видимость планет, расширение и сжатие звёзд..."
    "Она стала припоминать всё, что прочитала об этом."
    un "...Метеорные потоки, появление астероидов и комет, затмения..."
    show un smile2 pioneer close at center with dspr
    un "И так далее! Даже случайный и непонятный объект может оказаться уникальным, а любитель — стать первооткрывателем."
    un "Постоянные мы видим каждый день, например, фазы Луны, если не облачно. Вертятся и Земля, и её спутник."
    show un smile pioneer close at center with dspr
    un "Периодические видны нам только в какие-то определённые месяцы или времена года."
    un "А редкие явления становятся историческими, если их могут наблюдать не только астрономы с любителями, но и обычные люди."
    show un smile2 pioneer close at center with dspr
    un "Каждую неделю что-то да происходит! Вот сегодня как раз день исторического события, поэтому я и пришла сюда с телескопом..."
    me "Я вроде ничего не заметил."
    "Мне стало смешно."
    me "Звёзд слишком много!"
    show un laugh pioneer close at center with dspr
    un "Да, именно поэтому!"
    me "А что за событие?"
    show un smile pioneer close at center with dspr
    un "Сегодня в созвездии Лиры невооружённому глазу станет доступна знаменитая комета Мейля."
    me "Комета чего?"
    "Лена подняла палец и ответила мне серьёзным тоном, но с улыбкой. И сейчас она уже была не той заплаканной девочкой, а моим милым лектором по астрономии..."
    un "Не чего, а кого! Это по имени учёного, открывшего её полтора месяца назад."
    me "Ну я же не разбираюсь в теме и не слежу за новостями об исследовании космоса."
    me "Чем комета вдруг стала знаменита?"
    show un smile2 pioneer close at center with dspr
    un "По косвенным признакам астрономы считают, что это та самая Большая комета тысяча семьсот семнадцатого года, и теперь она снова возвращается к нам."
    un "Тогда комета была невероятно близка к Земле и произвела огромное впечатление на людей."
    un "Я писала об этом в заметке для стенгазеты на прошлой неделе, перед тем как попросила у кибернетиков телескоп."
    me "Да, но я не вижу тут радостных пионеров и ажиотажа."
    show un grin pioneer close at center with dspr
    un "Потому что событие пока интересно лишь любителям астрономии да учёным."
    show un smile pioneer close at center with dspr
    un "Комета только сутки назад проникла во внутреннюю область Солнечной системы, и стремительно приближается к орбите Марса. Историческим событием для случайных наблюдателей с Земли будет день, когда комета пройдёт самые близкие к нам и к Солнцу точки на своей орбите."
    show un smile2 pioneer close at center with dspr
    un "Если Солнце не помешает наблюдению, то с длинными светящимися хвостами комета в небе будет казаться больше обычных самолётов. Это должно быть невероятным зрелищем, если ожидания оправдаются."
    show un shy pioneer close at center with dspr
    un "Скорее всего, это случится через два месяца или немного раньше."
    me "А про то, что сегодня комета станет видна, ты где-то узнала?"
    show un shy pioneer close at center with dspr
    un "Ну да, я прочла о ней в приложении к журналу «Вестник юного астронома». Там пишут астрономический прогноз на месяц."
    show un sad pioneer close at center with dspr
    "Лена поднесла к лицу руки."
    un "Но лучше один раз увидеть...{w} Правда, Семён?..{w} Найдём комету?.."
    scene anim stars_1_north
    with dissolve
    "Я поднял голову."
    me "Давай. Где находится созвездие Лиры?"
    scene anim stars_3_south_east
    with dissolve
    "Лена осторожно тронула меня за плечо, и мы повернулись к телескопу спиной. Девочка указала куда-то вверх и влево."
    un "Смотри на юго-восток, видишь осенне-летний треугольник из трёх ярких звёзд?"
    me "Ага."
    un "Нам нужна самая высокая — это Вега, альфа созвездия Лиры. Где-то поблизости должна быть и комета..."
    me "Вот она."
    "Я заметил крохотную точку, за которой виднелся крайне размытый след, не длиннее самого ядра кометы больше, чем вполовину, как я предположил."
    "Небесное тело казалось неподвижным и не отливало блеском, как сотни звёздочек рядом. Спутать комету с одной из них ничего не стоило."
    un "Надо посмотреть на неё в увеличении, уверена, так будет интересней!"
    scene bg ext_playground_night
    with dissolve
    show un smile pioneer at center with dissolve
    "Лена отошла, чтобы развернуть монтировку телескопа на штативе, посмотрела в окуляр и зафиксировала оптику. Перед линзой Лена сменила фильтр на тот, что лежал в боковом кармашке чехла."
    un "Сейчас...{w} Вижу комету!.. Намного лучше, чем невооружённым глазом."
    show un smile pioneer close at center with dspr
    "Я наклонился рядом с Леной, когда она предложила полюбоваться этим явлением из космоса."
    #Пока что используется дефолтное cg со звёздами, без явных указаний на то, о чём говорится по тексту.
    #По идее, можно подправить cg в фотошопе и дописать команду зуммирования в скрипте. TODO под вопросом.
    scene anim stars_2o_bw
    with fade2
    "Комета выглядела не больше спичечной головки, окутанная чашей света с едва-едва приметным блеском, если смотреть чуть ниже и вкось."
    "Она точно прожигала себе путь в мёртвенно-чёрном пространстве."
    "Узкий, как игла, хвост-след только начинал раздваиваиваться позади, стрелкой направляя комету слева направо и вниз."
    un "Она такая яркая, хоть и далеко от нас, потому что газ вокруг ядра люминсценирует, а около Солнца реакции будут ещё красивее."
    me "Небольшая, а свет виден отсюда. Здорово."
    un "Да, она всего два километра в диаметре, для космоса это совсем ничтожная величина."
    "Я не мог оторваться от телескопа, точно загипнотизированный свечением небесного тела. Лена осторожно коснулась меня и попросила дать ещё немного посмотреть и ей."
    scene bg ext_playground_night
    with dissolve
    show un shy pioneer close at center with dissolve
    un "Подобные кометы нечасто увидишь... Эта обогнёт Солнце и вернётся только через триста лет, а другие могут странствовать тысячи и миллионы лет."
    show un smile pioneer close at center with dspr
    un "Но кроме них б{i}о{/i}льшую часть года множно наблюдать не менее красивые вещи. Если погодные условия хорошие..."
    un "Например, в созвездии Геркулеса, через которое пройдёт комета, есть скопление звёзд — М-тринадцать."
    "Она немного сместила трубу телескопа, выискивая нужное направление обзора."
    show un smile2 pioneer close at center with dspr
    un "Гляди!"
    me "Ну, что там?"
    hide un with dissolve
    "Я увидел тусклое пятно, похожее на бездну, к которой стремились окружавшие его сотни тысяч звёзд. Мириады белых точек напоминали огни на кончиках оптоволоконного цветка."
    "Но я чего-то не понимал."
    th "А где цвет? А где размах? Я же ставил такие клёвые обои на рабочий стол!"
    show un normal pioneer close at center with dissolve
    me "Почему мне всё кажется серым? Не только М-тринадцать, но и всё, что я увидел до этого."
    show un shy pioneer close at center with dspr
    un "Человеческий глаз ночью не позволяет видеть цвета и детали, как при свете." 
    show un smile pioneer close at center with dspr
    un "С обычным телескопом в цвете можно увидеть лишь планеты Солнечной системы — их яркость выше, чем у дальних объектов."
    show un sad pioneer close at center with dspr
    un "Цветное изображение далёкого космоса получают в астрофотографии, но между ней и рисованием я выбрала второе."
    "Мне взгрустнулось. Если бы я приобрёл телескоп в своё время, то обязательно забросил начинания в астрономии, столкнувшись с этим фактом."
    th "Выброшенные на ветер баксы и труба в шкафу."
    th "Или перед наблюдениями закинулся бы чем-то, чтобы перед глазами поплыли всякие цвета... Тогда вместо телескопа сгодился бы и стакан."
    show un smile2 pioneer close at center with dspr
    un "Хочешь увидеть Юпитер? Только я сначала сменю фильтр, а то засветка над Москвой помешает..."
    show un smile pioneer at center with dspr
    "Лена довольно сильно снизила направление объектива."
    "Я поглядел вдаль — над деревьями и правда виднелся рыжеватый отсвет городской иллюминации. Вскоре пионерка позвала меня."
    "С Юпитером вышло поинтересней — он был цветным: на расплывчатом по краям диске размером в два рубля можно было различить тёмные и светлые полосы. А рядом с планетой едва ли не в ряд располагались её спутники."
    "После наблюдений в южном небе Лена снова развернула телескоп на север."
    show un normal pioneer at center with dspr
    un "...Видел когда-нибудь июньские Боотиды?"
    me "Нет. Что это?"
    show un surprise pioneer at center with dspr
    un "Прости, запамятовала, что ты не увлекаешься астрономией... Это метеорный поток созвездия Волопаса в июне."
    show un shy pioneer at center with dspr
    un "Из периодических явлений мне больше всего нравятся звездопады." 
    show un smile2 pioneer at center with dspr
    un "Сегодня начинается поток Персеид, он сильный и яркий!" 
    show un sad pioneer at center with dspr
    un "Жаль, что пик будет не сейчас, а только в августе..."
    show un smile2 pioneer at center with dspr
    un "В пик можно насчитать больше пятидесяти метеоров в час!"
    show un smile pioneer at center with dspr
    un "Так что, если повезёт, мы увидим несколько падающих звёзд."
    un "По названию понятно, что надо смотреть на окрестности созвездия Персея."
    "Лена повернулась ко мне спиной и указала на участок неба заметно ниже и правей от Полярной звезды."
    stop music fadeout 2
    show un sad pioneer at center with dspr
    un "Надо подождать... Как увидишь сгорающий метеороид, успей загадать желание! Говорят, оно обязательно сбудется..."
    "Улыбка мгновенно сползла с моего лица."
    "Лена замерла, восторженно глядя в небо, где с минуты на минуту должен был мелькнуть шлейф метеора."
    "Я спрятал руки в карманах."
    th "Хм, загадать желание?"
    stop ambience fadeout 1
    "Я делал так много раз и даже вспоминал об этом совсем недавно, перед тем, как сесть в автобус."
    scene bg bus_stop_bw
    with dissolve2
    play music music_list["just_think"] fadein 1
    "......"
    "{i}...Мечты, надежды, цели. Я не хотел стать космонавтом, но я ни на секунду не сомневался, что стану важным.{w} Стану нужным.{/i}"
    "{i}Стану умным.{w} Красивым.{w} Встречу умницу-красавицу, которая полюбит меня с первого взгляда.{w} Я для неё, она для меня.{/i}"
    "{i}Я загадывал такие желания каждый день рожденья, когда задувал свечки.{/i}"
    "{i}Надо ли говорить, что ничего не сбылось?{/i}"
    scene bg ext_playground_night
    with fade
    play ambience ambience_camp_center_night fadein 4
    "Мои пальцы сами сжались в кулаки от промелькнувших воспоминаний."
    me "Чушь!.."
    show un shocked pioneer at center with dspr
    "Я сказал это так громко, что Лена испуганно обернулась ко мне."
    un "Ч-что?.."
    me "Да то, будто если загадать желание, оно непременно сбудется. Нельзя верить в такое!{w} Чем раньше перестанешь надеяться, что всё придёт само собой, тем лучше."
    show un surprise pioneer at center with dspr
    un "А...{w=0.5} а к-как же чудо?"
    "Этим она окончательно рассердила меня. Я махнул ладонью, как отрезал."
    me "Чудес не бывает!"
    show un sad pioneer at center with dspr
    me "Если я захочу иметь что-то, а сам запрусь в своей квартире и не буду предпринимать действий, появится ли у меня из ничего желаемое?"
    me "Мир сложен, мир требует большего, чем следование приметам.{w} Желание не сбудется только потому, что я загадал его и впоследствии забыл о нём.{w=0.5} Я не суеверный."
    show un cry pioneer at center with dspr
    "На глазах Лены снова заблестели слёзы."
    "От смятения и неуверенности она взялась за руку выше локтя, точно защищаясь. Девочка отвела взгляд."
    un "...Да, н-наверно..."
    un "Может, поэтому я не так серьёзно увлекаюсь астрономией, чтобы зарисовывать фазы Венеры в тетради или учить формулы по расчёту движения и свойств небесных тел..."
    show un cry_smile pioneer at center with dspr
    un "Мне достаточно просто наблюдать красоту явлений в космосе и находить в этом вдохновение..."
    "Лена снова посмотрела вверх, как раз вовремя, когда в иссиня-чёрном небе сверкнула прямая линия упавшей звезды."
    un "Мне нравится мечтать.{w} Иногда я фантазирую, будто я сама инопланетянка, а где-то там среди звёзд на какой-то планете есть жизнь, и другая такая же девочка, как я, смотрит в небо..."
    show un normal pioneer at center with dspr
    un "Но ты, наверно, не веришь в подобное и будешь прав. Это всё глупости, и ничего такого нет."
    "Я с трудом сдержал кашель в горле. Лена даже не подозревала, насколько её фантазии сейчас были близки к правде, а живое тому доказательство стояло рядом с ней."
    "Я же прибыл из другого мира."
    me "Нет, в {i}это{/i} я могу поверить."
    me "Всё может быть, вероятность существования других миров есть, просто учёные пока не совершили открытий, не нашли всему объяснений."
    show un shy pioneer at center with dspr
    un "Да?"
    me "Конечно. Я не привык придавать значения совпадениям и случайностям, всё зависит от обстоятельств."
    th "А моё перемещение сюда — случайность или нет? Сложный вопрос!"
    show un sad pioneer at center with dspr
    "Небо прочертила вторая падающая звезда и тут же исчезла."
    "Я замолчал, но и желания не стал загадывать, теперь они мне были ни к чему."
    "..."
    "......"
    #TODO: в будущем добавить sfx phone_timer
    show un shy pioneer at center with dspr
    "Послышался глухой писк. Лена вынула мобильник-раскладушку из кармана и отключила напоминание."
    show un normal pioneer at center with dspr
    un "Время отбоя... Мы задержались."
    "Она принялась собирать телескоп в чехол, и я снова помог ей."
    "..."
    window hide
    stop music fadeout 2
    #К этапу работ по графике. Тут должен быть ночной бэкграунд улиц с жилыми домиками — ext_houses_night.
    scene bg ext_square_night
    with dissolve
    play music music_list["smooth_machine"] fadein 1
    show un normal pioneer close at center with dissolve
    window show
    "Перед тем, как мы расстались около домиков, я наконец обратился к Лене."
    me "Извини, что нагрубил."
    un "Ничего страшного... Спасибо, что не ушёл раньше."
    show un grin pioneer close at center with dspr
    "К Лене вернулась улыбка."
    un "Стоять прохладной ночью у поля, когда вокруг ни души, а в лесу ухают совы — тот ещё кошмар."
    show un smile pioneer close at center with dspr
    un "Спокойной ночи!"
    me "И тебе."
    hide un with dissolve
    "..."
    "Дальше в планах у меня были душ и чистка зубов перед сном."
    scene bg ext_house_of_mt_night
    with dissolve
    "Я остановился у своего домика."
    th "Всё-таки Лена немного странная девочка. Застенчивая, ранимая во многих смыслах." 
    th "Да и я тоже с причудами — наговорил резких слов под конец."
    th "Вот дурак!"
    "Захотелось крепко стукнуть лбом о входную дверь, но я быстро раздумал наказывать себя."
    "Просто я не мог не высказать наболевшее. Это было важно."
    th "Мне, конечно, надо быть посмелей в общении, но в то же время знать меру."
    th "Может, завтра получится? Я ведь загадывал, что стану умным и нужным, какого могут полюбить!"
    th "Что ж, день, когда это случится, будет исключительно редким событием, сродни комете, приближающейся к Солнцу раз в тысячи лет."
    window hide
    stop ambience fadeout 1
    stop music fadeout 2
    $ d2_un_evening = True
    $ lp_un = lp_un + 1
    $ d2_girls_event = (d2_girls_event) + (1)
    jump d2_bed_time

label d2_beach_evening:
    
    $ reset_chibi("beach")

    if (d2_dv_help == False):
        scene black
        with dissolve
        show screen central_text("День 2 — Заплыв с перекуром")
        $ renpy.pause(99, hard=False)
        hide screen central_text
        scene bg ext_square_night
        with dissolve
        play music music_list["sweet_darkness"] fadein 2
        play ambience ambience_camp_center_night fadein 2
        window show
        "После такого напряжённого дня грех не искупаться или просто отдохнуть на пляже."
        "Идея сходить на реку для этого была очевидной и витала у меня в голове ещё с утра."
        "Вот только безумный день закрутил меня в круговороте своих невозможных событий."
        "Изнурительная зарядка с построением, обходной листок..."
        "Всё же я не без удовольствия вспомнил, как познакомился с оставшимися обитателями лагеря и даже выбрал себе кружок."
        "Но это было утром, а после обеда столько всего произошло, что о пляже некогда было и вспоминать! К тому же, меня могли подловить вожатые, обходившие лагерь."
        "Сейчас я мог по-быстрому и незаметно скупнуться."
        "Я надеялся, что на сегодня мои приключения закончились."
        if d2_cards_win:
            th "Я ведь победил в турнире! Самое время расслабиться и отпраздновать!"
        "И я наконец смог, пусть и под самый вечер, выбраться к берегу."
        window hide
        stop ambience fadeout 1
        stop music fadeout 2
        scene bg ext_beach_night
        with dissolve
        play music music_list["went_fishing_caught_a_girl"] fadein 0
        play ambience ambience_lake_shore_night fadein 1
        window show
        "Я прямо таки предвкушал, как сложу пионерскую форму у камня в песке и с разбегу прыгну в воду, чтобы растянуться на волнах, отдыхая от суеты и всяческих волнений."
        "Но..."
        show dv normal swim at center with dissolve
        "Спустившись на пляж, я увидел Алису. Она в одном купальнике стояла почти у самой воды, поджидая, когда волны прибьются к её ногам и снова отступят назад. Рядом с ней лежала автомобильная камера."
        "Я напрягся, невольно поймав себя на мысли, что загляделся на девочку — ещё бы, такой вид!"
        show dv smile swim at center with dissolve
        "Точно почувствовав моё присутствие, Двачевская оглянулась и встретилась со мной взглядом."
        th "Мне п-ц!"
        "Я совсем не хотел натыкаться на неё после всех стычек, что произошли за два дня между нами. Инстинкты требовали незамедлительно уйти с пляжа, но я замер, будто меня закопали в песок по колени."
        "Алиса молчала и с прищуром, оценивающе смотрела на меня."
        show dv grin swim at center with dspr
        dv "Купаться пришёл? Хм... Ну тогда...{w} поплаваем?"
        "Я вздрогнул. Я ожидал от неё чего угодно, только не этих слов."
        me "Угадала. На пляже сейчас больше нечего делать."
        show dv smile swim at center with dspr
        dv "Да неужели?"
        "Она усмехнулась, а я лениво стянул кеды."
        th "Какое блаженство — чувствовать, как серый ковёр песка сминается под ногами, хрустит и покалывает пятки маленькими камушками!"
        "За день солнце нагрело его так, что и сейчас он ещё приятно обжигал голую кожу!"
        "Правда я рассчитывал на удовольствие в одиночестве. Рядом с Алисой я никак не мог избавиться от напряжения, словно нёс тяжёлый груз на плечах."
        "Я расстегнул рубашку, сунув надоевший уже галстук в карман, и невольно обернулся, прежде чем стянуть шорты до конца."
        "Я забыл сходить к себе за плавками, так что купаться мне предстояло в семейниках."
        th "Слава б-гу, я не надел перед походом в «Макдональдс» те, что купила мать — в цветочек... Двачевская подняла бы меня на смех."
        show dv angry swim at center with dspr
        dv "Ты долго ещё будешь тормозить, копуша?"
        show dv normal swim far at center with dspr
        "Пионерка, устав ждать меня, полезла в реку."
        me "Секунду!"
        stop music fadeout 2
        th "...И чего я вдруг начал торопиться, услышав её голос?"
        play music music_list["that_s_our_madhouse"] fadein 2
        "Не думая об этом, я избавился от треклятой одежды и тоже спустился в воду."
        #Возможно, здесь потребуется срежиссировать сцену иначе — не показывать спрайт персонажа в воде. Так же поступить со всеми эпизодами плавания.
        #В этом случае помогло бы изображение лица говорящего слева от текстбокса. Но при текущем интерфейсе это лицо можно вынести в рамочку по центру.
        #Вернуться к этому моменту по окончании скрипта.
        show dv normal swim at center with dspr
        "Уже около берега начиналась глубина, поэтому я оттолкнулся от ила и поплыл рядом с Алисой."
        th "Как же давно я не плавал!"
        "Вода была потрясающей: вроде прохладная, а на самом деле ещё не остывшая после солнечного дня."
        show dv laugh swim at center with dspr
        dv "Кто первый до буйков?"
        show dv smile swim at center with dspr
        "Я принял вызов, не отвечая. Мы одновременно рассекли волны кролем, спеша к тёмным шарам, покачивавшимся на воде."
        "Двачевская ускорилась, а вот мои силы начали сдавать."
        me "Подож... Кха!"
        show dv surprise swim at center with dspr
        "Я ненароком хлебнул воды и едва не закашлялся."
        "Алиса остановилась, будто размышляя, надо ли спасать меня или нет."
        show dv grin swim at center with dspr
        dv "Слабак!.."
        th "Э? Щито? Это я-то слабак?!"
        "Я снова поплыл, да так быстро, не понимая, откуда у меня нашлись силы на это."
        show dv smile swim at center with dspr
        th "Правой! Левой!"
        hide dv with dissolve
        "Я сумел обогнать Алису и убедился в этом лишь когда хлопнул рукой по буйку."
        if (d2_dv_fight == False):
            "Лёгкие и горло жгло после курения, но я справился — на помолодевшем теле ещё не сказалась многолетняя привычка."
        "Еле переводя дыхание, я с торжествующим видом взобрался на шар, который почти целиком скрылся в воде под моим весом."
        me "Я первый! А ты говорила!.."
        show dv normal swim at center with dspr
        "Алиса нисколько не отстала от меня, хоть я оказался быстрее, поэтому она сразу подплыла к бую следом."
        "От меня не укрылось, что она, как и я, тяжело дышала после того рывка."
        show dv grin swim at center with dspr
        "Двачевская улыбнулась, и в этой улыбке не было ничего угрожающего или обидного."
        if d2_cards_win:
            dv "Опять ты выиграл у меня. Поздравляю!"   
        else:
            dv "Выходит, не такой уж ты слабак... Поздравляю!"
        "Казалось бы, похвалы были проще некуда, но из уст Алисы они будто стали значительными... Я совершенно расклеился и весело улыбнулся в ответ, чувствуя, что груз напряжения свалился с плеч."
        show dv grin swim close at center with dspr
        "Оказавшись совсем близко, Алиса вдруг положила свои ладони мне на колени, точно пыталась таким образом удержаться на поверхности воды."
        me "Эй, что ты делаешь?"
        show dv smile swim close at center with dspr
        "Пионерка ничего не сказала, только её улыбка из доброй стала ехидной. Тут и дурак бы догадался, что дело нечисто, но я прозевал момент истины."
        dv "Кто первый до берега?"
        "Алиса согнула ноги, уперевшись в буй, и оттолкнулась, аки спортсмен в бассейне на соревнованиях, изящно поплыв назад."
        hide dv with dspr
        "Всё произошло в одну секунду — после этого я с громким плеском свалился с шара в воду."
        th "Ах ты!.."
        show dv smile swim far at center with dissolve
        "Когда я вынырнул, отплёвываясь, Алиса уже была на полпути к берегу."
        "Я мысленно обругал её всеми нехорошими словами за неожиданную подлянку и с последними силами поплыл за ней."
        stop music fadeout 2
        th "У, я тебе покажу!"
        "Силы под конец заплыва покидали меня — я выдохся."
        play music music_list["smooth_machine"] fadein 1
        th "Хм, и в самом деле, что я покажу ей? Как махаю кулаками или грязно ругаюсь? Я выжат как мочалка, и в лучшем случае могу показать Двачевской только свои мокрые семейники."
        show dv smile swim at center with dspr
        "Алиса уже вышла из воды первой и наблюдала, как я преодолеваю последние метры и выбираюсь на песок." 
        me "Ха-а{font=fonts/DejaVuSansMono.ttf}~{/font}"
        show dv laugh swim at center with dspr
        dv "Победитель в общем зачёте — Алиса Двачевская! Можешь поздравить меня!"
        me "...Это было...{w} нечестно!.. Я бы тебя...{w} Дисквалифицировал!"
        show dv smile swim at center with dspr
        dv "Жизнь несправедлива!{font=fonts/DejaVuSansMono.ttf}♪{/font}"
        "Она была в таком хорошем настроении, что пропела эти слова, а я даже не смог заставить себя подняться, только повернулся лицом к речке и уставился вдаль."
        me "Видишь ли, не плавал тыщу лет, совсем забыл, как это делается. А тут ещё тебе вздумалось кинуть меня в воду."
        show dv grin swim at center with dspr
        dv "Да не, всё ты помнишь и нормально плаваешь. Просто я круче тебя!"
        me "Не зазнавайся."
        show dv laugh swim at center with dspr
        "Алиса рассмеялась и снова отошла к воде мочить ноги прибывающими барашками мелких волн."
        show dv normal swim at cright with dspr
        if d1_genda_flag:
            me "А могу я поинтересоваться, чем была вызвана столь жаркая встреча по приезду?"
            show dv normal swim at cright with dspr
            dv "Да что ты заладил об этом, как попугай?"
            me "Мне непонятен скрытый смысл того действа. О чём ты думала?"
            show dv grin swim at cright with dspr
            dv "Ну, как тебе объяснить, чебурашка?"
            show dv normal swim at cright with dspr
            dv "По лагерю посреди смены прётся явный новичок с вещами, опоздавший на цельную неделю... Ты бы сам как отреагировал?"
            me "Да никак, наверное?"
            show dv surprise swim at cright with dspr
            dv "Что значит «никак»? А может он буйный какой?"
            th "Кто буйный, я буйный?"
            show dv smile swim at cright with dspr
            dv "Может он устроит полный шухер, в щепки разнесет стул прямо во время ужина, а потом ещё и в одном домике с вожатой поселится? Будет шляться по лагерю, выискивать себе жертв на смену вперёд!" 
            if d2_guitar_illegal:
                dv "Предложит скоммуниздить гитару у несчастной Мику..."
            if d2_walk == 0:
                dv "Пометит все карты, чтобы обжулить всех честных пионеров..."
            th "Это она меня отчитывает, что ли? Когда Алиса успела стать родственницей Ольге Дмитриевне?"
            #show dv rage swim at cright with dspr #TODO (к этапу работ по графике): к body 5 нужен купальник для отображения эмоций rage, angry.
            show dv rage pioneer2 at cright with dspr
            with vpunch
            dv "{b}Это же КОНКУРЕНТ!{/b}"
            th "Ох ты ж!!!"
            "Я едва не брякнулся спиной на песок, с таким напором произнесла это Алиса."
            show dv smile swim at cright with dspr
            dv "Ну, сам подумай."
            me "Можешь не продолжать, я всё понял."
            show dv normal swim at cright with dspr
            "Двачевская отвернулась к Волге."
            hide dv with dissolve
            th "А ведь она в чём-то права, я никогда не считал себя особо примерным. И на всю местную детвору гляжу как бы свысока..." 
            th "Да и лагерь уже не страшное место за семью заборами, а плацдарм для безнаказанных развлечений. И эта вылазка на реку — одно из них."
        stop music fadeout 2
        play music music_list["sweet_darkness"] fadein 2
        "Растянув ноги на песке, я понемногу приходил в себя."
        "Я прикинул на глаз расстояние до буйков. Вроде не очень далеко от берега, а сколько энергии ушло на заплыв!"
        "Неудивительно — ещё день тому назад я сидел в кресле за компьютером."   
        "Но я не жаловался, заплыв принёс мне лишь бурю хороших чувств, а затем долгожданное облегчение. Приятно было знать, что можно прийти сюда снова и завтра, и послезавтра..."
        th "А как же Алиса?"
        scene cg d2_2ch_beach_night with dissolve:
            pos (0,-1920)
            linear 10.0 pos (0,0)
            linear 2.0 pos (0, -250)
        "А она... Она нисколько не устала, как будто и не было заплыва!"
        "Я сидел рядом, и в призрачном свете луны мне было видно, как Алиса смотрит то вдаль, то под ноги. Начертила что-то ногой на мокром песке, а вода залила и смыла неизвестный мне рисунок. Или надпись. Этого я не знал."
        "Её похожие на молнии хвосты чуть вздрагивали от малейшего движения."
        th "Как её волосы так быстро высохли?"
        "Но не это привлекло моё внимание."
        scene cg d2_2ch_beach_night_horizontal with dissolve
        "...А её открытая, слегка загорелая спина с завязками бикини." 
        "Влажный купальник очерчивал грудь и бёдра Алисы..."
        "А капли воды блестели на руках и под коленками..."
        if d2_in_game:
            "Неожиданно я вспомнил ультиматум Двачевской..."
            #scene bg ext_dining_hall_near_day_bw
            #show dv grin pioneer2 close bw at center
            #with dissolve2
            dv "{i}Если проиграешь, я скажу всем, что ты подглядывал за мной, когда я переодевалась!{/i}" 
            dv "{i}...И лапал меня!{/i}"
            #scene cg d2_2ch_beach_night with dissolve
            th "Ох, как ей вообще пришла в голову мысль угрожать этим?"
            if d2_us_dv_day:
                "Может быть, моя выходка с Ульяной задела её за живое?"
            "Ужасная догадка поразила меня."
            th "Если она придумала такое, то возможно, хотя бы на минутку представила себе, что я на самом деле подсматривал, а затем начал приставать к ней..."
            "Хорошо, что сейчас поздний вечер, и не слишком заметно, как сильно я покраснел от картинки, нарисовавшейся в моём воображении."
            th "А поступил бы я так, случись всё в реальности? Ну... только подсмотрел бы, на большее у меня не хватило бы духа."
        "Всё время, пока я думал, мой взгляд был неотрывно прикован к Алисе."
        "...Не сине-чёрные волны манили глаз, не песчаный изгиб у воды, а стройные ноги девочки, её природная, женская естественность."
        "Словом, тот самый вид, который удержал меня на пляже ещё когда я застал здесь Двачевскую."
        "Она снова обернулась, как при встрече, но не с подозрением на лице, а со светлой улыбкой."
        stop music fadeout 2
        scene bg ext_beach_night
        with dissolve
        play music music_list["you_won_t_let_me_down"] fadein 2
        show dv smile swim at cright with dissolve
        "Согнув ноги, я как бы невзначай прыкрыл странным образом натянувшиеся семейники."
        show dv normal swim far at cright with dspr
        "Алиса вспомнила о чём-то и прошла мимо меня к оставленной под увесистым камнем пионерской форме." 
        "Я подумал, что она собралась одеться и уйти, но ошибся. У лица Двачевской вспыхнула спичка. Через мгновение сигарета в поджатых губах девочки задымилась."
        show dv smile swim close at cright with dspr
        "Вытоптав новую дорожку следов на песке, Алиса остановилась рядом со мной."
        if (d2_dv_fight == False):
            if d2_dv_interrogation:
                show dv grin swim close at cright with dspr
                dv "А ты молодец, не раскололся!"
                th "О чём это она? А... Тот допрос с пристрастием!.."
                "Мои щёки помнили прикосновение острых ноготков Алисы."
            elif (d2_dv_interrogation == False):
                dv "Эх, не успела тебя прищучить до обеда, а надо было. Потом я подумала, может не ты... Но как чувствовала!"
                me "Ты про что?"
                dv "Ну-ну, не прикидывайся чистеньким, поздно уже. Про сигареты, Семён, про сигареты."
                "Моё сердце ушло в пятки."
            show dv normal swim close at cright with dspr
            dv "Я догадывалась, кто мою вещь присвоил и зажал, но когда ты завалился на пляж с этим амбре от «Родопи», всё стало ясно. Я за версту их узнаю!"
            if d1_genda_flag:
                show dv grin swim close at cright with dspr
                dv "Вот правда, самый настоящий конкурент."
            th "Как бы она не заставила меня расплачиваться за нанесённый ущерб в десятикратном размере..."
            me "А эта откуда?"
            "Я небрежно кивнул, имея в виду ту сигарету, что держала Двачевская."
            show dv normal swim close at cright with dspr
            dv "У Антона пришлось стрельнуть пару, а этого я совсем не хотела делать.{w} Но он расстался с ними легко. Короче, с тебя должок, Семён."
            me "Ну вот блин, я знал, что всё так и закончится."
            show dv laugh swim close at cright with dspr
            dv "Больше не будешь чужое тягать!"
            show dv smile swim close at cright with dspr
            "Заметив, что я снова напрягся, Алиса простодушно похлопала меня по макушке, немного растрепав волосы, ещё не до конца обсохшие."
            dv "Да ты не парься, я только хочу, чтобы ты вернул то, что принадлежит мне. Ну или скажи, где заныкал их, разделим добро на двоих за неделю, а то и меньше."
            me "Разделим? С чего бы вдруг такая щедрость? Не верится мне..."
            "Алиса выдохнула тонкую струйку дыма и снова потрепала мои волосы. Понравилось ей, что ли?"
            if d2_dv_interrogation:
                dv "Это за проявленную стойкость."
            else:
                dv "За удивительную наглость явиться сюда после этого."
            me "Хорошо... Я в следующий раз принесу четыре, стрельнешь у меня половину. Договорились?"
            show dv normal swim close at cright with dspr
            dv "Ах ты жук! Впрочем, я бы не предлагала, если б не была готова делиться..."
        else:
            show dv normal swim close at cright with dspr
            dv "Как видишь, на пляже можно не только купаться."
        show dv smile swim close at cright with dspr
        "Она заметила, что я впился глазами в тлеющую сигарету."
        dv "Что, хочешь?"
        me "Хочу!"
        show dv normal swim at center with dspr
        "Я вскочил с места, и Двачевская опять сходила к сваленной комом рубашке за сигаретой и спичками, но уже для меня."
        show dv smile swim close at center with dspr
        dv "Держи. Вот теперь за тобой точно должок."
        "Я не ответил, и не вслушивался особенно, потому что спешно прикуривал от огня спички."
        if (d1_dv_evening == False) and (d2_dv_fight == True):
            "Конечно, я так жадно хотел курить, потому что весь прошлый день провёл как человек без вредных привычек. Помолодел, а желание осталось."
            "Втянув и сильно выдохнув дым, я выдал мощный такой, основательный поток ругательств, что Двачевская успевела сменить множество самых разнообразных выражений лица и даже покраснеть пару раз, пока мой словогенератор не иссяк."
            show dv surprise swim close at center with dspr
            me "...Фу-у, ёпт, ё-моё, чтоб на меня Свиборг пырился всю жизнь, блин. Как будто бы домой вернулся... А?.."
            "Двачевская всё ещё смотрела на меня широко раскрытыми глазами, но потом едва слышно усмехнулась."
            show dv grin swim close at center with dspr
            dv "Так вот ты какой, северный олень!"
            me "Северный?"
            th "Если знать, сколько я просиживаю перед монитором в сутки, то олень из меня только серверный."
            "Я засмеялся."
            show dv smile swim close at center with dspr
            dv "А кто вчера приехал в буржуйском зимнем пальто?"
            me "Оно совсем лёгкое... Как раз для непогоды."
            th "Неуклюже объяснился. Ну не знал же я, что автобус привезёт меня в летний лагерь!"
        "Я пыхнул дымом и свободной от сигареты рукой попытался отряхнуть семейники."
        me "Пойду-ка я снова в воду, а то у меня трусы в песке."
        show dv normal swim close at center with dspr
        dv "И я, и я."
        show dv normal swim at right with dspr
        "Двачевская подобрала резиновую камеру, позабытую в сторонке."
        hide dv with dissolve
        stop music fadeout 1
        play music music_list["reflection_on_water"] fadein 1
        "Я осторожно сошёл в воду по плечи, чтобы не замочить и не потушить сигарету — сейчас она была так же дорога мне, как тростинка для разведчика, скрывающегося от преследования в речке."
        show dv smile swim at center with dissolve
        "Поблизости от меня тихо поплыла Алиса, развалившись на круге, аки царица на ложе, и нарочно перестала грести."
        show dv grin swim at center with dspr
        dv "Держи меня, а то унесёт течением!"
        "Я поймал камеру, а другой рукой отнял сигарету от губ."
        me "Не унесёт: мы в загоне из буйков."
        show dv smile swim close at center with dspr
        dv "Я могу перебраться через них."
        me "Увы, я без платочка, помашу на прощание. Тогда пляж останется в моём единоличном распоряжении."
        "Алису ответ позлил, но она всё ещё улыбалась, понимая, что в этих перебрасываниях незначительными колкостями много условного наклонения."
        show dv laugh swim close at center with dspr
        dv "В таком случае я бы обязательно вернулась. А ты бы здорово пожалел."
        "Не отпуская круга, я снова затянулся."
        me "Как пожалел бы? Ну?"
        show dv grin swim close at center with dspr
        dv "Тогда было бы всё."
        me "Что — всё?"
        show dv smile swim close at center with dspr
        dv "Просто всё. Привет."
        me "Не понимаю."
        show dv laugh swim close at center with dspr
        dv "И не надо. Лучше бойся. Неизвестная кара страшней и внезапней известной."
        show dv smile swim close at center with dspr
        "Алиса докурила свою сигарету и щелчком отправила бычок в сторону забора. Она устроилась на круге поудобней, почти склонившись ко мне."
        th "А вот довольная, с такой улыбкой, она... ужасно симпатичная..."
        "Странная дрожь прошла по моему телу, и я был уверен, что это не судороги от прохлады реки."
        "Чем-то ситуация напомнила мне сцену из «Титаника», в которой главные герои пытались уцелеть в воде после крушения лайнера."
        "Только паршивые и неромантичные из нас Джек и Роуз: оба с сигарками и всего лишь плаваем в неположенное время, а не драматично спасаемся."
        "Но по силе впечатлений, которые мне когда-либо доводилось испытывать, переживаемый сейчас момент с лёгкостью можно было сравнить с крушением знаменитого корабля."
        "В хорошем смысле..."
        me "Согласен. С другой стороны, неизвестность не так страшна, как можно подумать. Её проще игнорировать, но это всё от человека зависит."
        show dv normal swim close at center with dspr
        me "А осознание того, что впереди нет ничего хорошего — напротив, подогревает желание выйти в окно."
        me "Потому что жизнь несправедлива."
        show dv guilty pioneer2 close at center with dspr #TODO (к этапу работ по графике): к body 3 нужен купальник для отображения эмоций guilty, sad.
        me "Твои слова, кстати."
        show dv sad pioneer2 close at center with dspr
        "Алиса перестала улыбаться, радость в её глазах уступила грусти. Двачевская всё прекрасно поняла и, возможно, даже знала это лучше меня. На резиновой камере она перевернулась на спину."
        "Я чуть повернул круг, пока не увидел её в профиль, едва различимый в темноте. От моей сигареты осталось чуть меньше трети, и я ещё разок затянулся."
        dv "А у тебя всё хорошо там, впереди?"
        "Она спросила это, не глядя в мою сторону."
        me "Не знаю. Наверно, ничего, если верить большинству, ха."
        dv "Почему ты тут, а не на асфальте за окном?"
        me "У меня хорошо получается игнорировать неизвестность и то самое большинство."
        show dv guilty pioneer2 close at center with dspr
        "Алиса взглянула на меня."
        dv "Как ты это делаешь?"
        me "Ничего особенного: тунеядствую. Уверен, многие поступают так же."
        me "..."
        me "Хотя нет, ещё я прихожу сюда, вижу тебя, соглашаюсь плыть наперегонки, побаиваюсь, что ты треснешь меня за какую-нибудь глупость или косой взгляд..."  
        show dv laugh swim close at center with dspr
        stop music fadeout 1
        play music music_list["eat_some_trouble"] fadein 1
        "Алиса рассмеялась, словно не прозвучало моих сентенций о безрадостной реальности."
        dv "Правильно боишься!"
        "Она шутя показала мне кулак."
        me "Эй-эй!.."
        me "Лучше смотри... Оп!"
        show dv smile swim close at center with dspr
        "Я зажал фильтр докуренной сигареты между пальцами и точно так же запульнул его к забору."
        "И плевать, что увидеть, куда упал бычок, было невозможно даже под светом луны."
        show dv grin swim close at center with dspr
        dv "Ну и? По-моему, я закинула дальше."
        me "Ах, {i}по-твоему!{/i}"
        show dv angry pioneer2 close at center with dspr
        dv "Только не начинай возникать, Семён, это не обсуждается!"
        me "А {i}по-моему{/i} пора на берег."
        show dv normal swim close at center with dspr
        "Я потянул круг на себя, изо всех сил работая ногами."
        show dv laugh swim close at center with dspr
        "Алиса потешалась надо мной."
        dv "Тащи-тащи!"
        show dv smile swim close at center with dspr
        th "Она явно напрашивается! Только мне правда может влететь..."
        "Наконец я почувствовал ступнями толщу ила, и тянуть круг стало проще."
        "Но вместо этого я подхватил его снизу и с большим трудом вытряхнул Алису с импровизированного ложа в воду."
        show dv shocked swim close at center with dspr
        dv "А-а!"
        hide dv with dspr
        play sound sfx_water_splash
        "{b}*Бултых*{/b}"
        show dv rage pioneer2 at center with dspr
        "Она фурией вынырнула и поднялась..."
        me "Признай, ты этого совсем не ждала!"
        dv "К-козёл!.."
        me "Ну, с буйка я свалился не так здорово, как ты. Твоё выступление на десять баллов!"
        "Я чересчур разговорился, а должен был скорей делать ноги. Двачевская, видимо, думала о том же."
        hide dv with dspr
        "Убежать мне не удалось — я неудачно запнулся на бегу и едва не свалился в воду. Алисе ничего не стоило поймать меня."
        show dv rage pioneer2 close at cright with dspr
        with vpunch
        "Девчонка опять зажала мою многострадальную шею тем же хватом, как при нашем первом знакомстве."
        "Я ожидал, что она поколотит меня так, что вожатая не узнает, однако вместо старого доброго насилия Алиса лишь потрепала меня по макушке костяшками пальцев."
        "Так потрепала, что я аж взвыл."
        me "Что ты делаешь, пусти! Черепушку продырявишь же!"
        show dv angry pioneer2 close at cright with dspr
        dv "А-а, вот теперь по-другому запел! Это... это косяк, Семён. Серьёзный такой косяк."
        me "То есть, тебе можно, а мне нельзя?"
        dv "В точку!"
        me "Хоть что делай, я против..."
        "Алиса перестала мучить мою голову."
        dv "Хоть что? Хм. Семён, ты придумал своё последннее слово?"
        me "Лучше бы круг взяла."
        "Двачевская чуть-чуть подумала."
        dv "Верно, а то завтра приберут к рукам другие."
        show dv normal swim at left with dspr
        "Ей не хотелось делать очередной заплыв. Пионерка отпустила меня и сходила за автомобильной камерой, которую уже понесло к забору."
        "Я наконец выпрямился. Шея, что удивительно, не болела, а вот макушку жгло от алискиного кулака."
        show dv angry pioneer2 at center with dspr
        "Двачевская с кругом под мышкой двинулась к холмикам нашей одежды."
        dv "Из-за тебя у меня волосы опять мокрые..."
        me "Это же не смертельно. Я вот сейчас в душ схожу, иначе как объяснять Ольге Дмитриевне, чего у меня башка сырая, а ноги в песке?"
        show dv normal swim at center with dspr
        dv "Хорошая идея... А я спрячу круг где-нибудь неподалёку, в следующий раз, когда нас погонят на пляж, возьму его по пути."
        window hide
        stop ambience fadeout 1
        stop music fadeout 1
        scene bg ext_playground_night
        with dissolve
        play music music_list["sweet_darkness"] fadein 1
        play ambience ambience_camp_center_night fadein 1
        window show
        "Мы подобрали свои вещи и вернулись на аллею к зданию с душевыми."
        show dv normal swim at center with dissolve
        dv "И помни, за тобой должок."
        me "Могла бы не говорить, я не забыл."
        show dv smile swim at center with dspr
        "Она подмигнула и снова улыбнулась."
        dv "Ну, мы с тобой ещё посоревнуемся!"
        me "Пока..."
        hide dv with dissolve
        "Алиса ушла, не оборачиваясь, а я толкнул дверь в раздевалку."
        th "Эх, что за день!"
        "Но всё закончилось лучше, чем я надеялся, придя этим вечером на пляж."
        window hide
        stop ambience fadeout 1
        stop music fadeout 1
        $ d2_dv_evening = True
        $ lp_dv = lp_dv + 1
        $ d2_girls_event = (d2_girls_event) + (1) 
        jump d2_bed_time
    else:
        scene bg ext_beach_night
        with dissolve
        play music music_list["sweet_darkness"] fadein 0
        play ambience ambience_lake_shore_night fadein 1
        window show
        "Я нисколько не удивился тому, что не увидел пляже хоть кого-то из пионеров."
        "В позднее время им наверняка охотней сидеть в светлых и уютных палатах."
        "Впрочем, на улице тоже было неплохо — нежаркий вечерний воздух и полутьма приятно успокаивали."
        if d2_in_game:
            th "А может быть, мне искупаться? Я ведь думал об этом..."
        "Я спустился к воде и подставил пальцы набегавшей волне."
        th "Прохладно..."
        "Не ледяная вода, какая была сегодня в умывальнике утром, но всё же. Купаться расхотелось."
        "Меня тянуло пройтись где-нибудь ещё, а потом назад, на освещённую площадь и в конце-концов вернуться в дом по примеру других детей."
        th "И не забыть принять душ, почистить зубы перед сном..."
        "С этой мыслью я ушёл с пляжа."
        window hide
        stop ambience fadeout 1
        stop music fadeout 1
        $ d2_evening_places += 1
        $ disable_current_zone()
        jump d2_evening_map

label d2_me_mt_house_evening:
    
    scene bg oldmap
    window show
    th "Хватит прогулок на сегодня."
    "Мне нужен был отдых и мягкая постель под спиной. Спать не хотелось, но я мог занять себя чем-нибудь до того, как Ольга Дмитриевна выключит свет в палате."
    window hide
    $ disable_current_zone()
    jump d2_bed_time

label d2_library_evening:

    scene bg oldmap
    th "Нет смысла туда идти, библиотеку закрыли ещё перед ужином."
    $ disable_current_zone()
    jump d2_evening_map

label d2_aidpost_evening:
    
    scene bg ext_aidpost_night
    with dissolve
    play music music_list["sweet_darkness"] fadein 1
    play ambience ambience_camp_center_night fadein 2
    window show
    "Было видно, что в медпункте выключен свет."
    "У меня ничего не болело."
    th "Не стоит беспокоить медсестру в поздний час просто так."
    th "Да и что я скажу ей?"
    "И, вспомнив утренний прием, я не решился зайти."
    th "А ведь я убеждал себя, что, покончив с обходом кружков, буду заглядывать сюда каждый день!"
    th "Ну, этот день ещё не закончился, для меня такое оправдание сойдёт."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ d2_evening_places += 1
    $ disable_current_zone()
    jump d2_evening_map

label d2_green_theatre_evening:
    
    scene bg ext_stage_big_night
    with dissolve
    play music music_list["sweet_darkness"] fadein 1
    play ambience ambience_camp_center_night fadein 2
    window show
    "Наверно, это была бы самая тёмная часть лагеря ночью, если б не серебристый лунный свет, ложившийся на всю поляну со скамейками и эстрадой."
    "Даже без фонарика кое-что можно разглядеть."
    th "А тут красиво, надо заметить!"
    "И свежий, естественный запах леса..."
    "Всё-таки есть в лагере положительные моменты, вроде этой прогулки."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ d2_evening_places += 1
    $ disable_current_zone()
    jump d2_evening_map

label d2_boathouse_evening:
    
    scene bg ext_boathouse_night
    with dissolve
    play music music_list["sweet_darkness"] fadein 1
    play ambience ambience_camp_center_night fadein 2
    window show
    "Хоть уже и наступил вечер, но было по-прежнему тепло."
    "Река лениво текла, легко покачивая лодки, убаюкивая пристань."
    "Спокойствие и величественность Волги настраивали на лиричные мысли."
    "Постояв немного у перил, я вернулся на твёрдую почву суши. Я, конечно, мог проторчать здесь ночь, просто созерцая красоту природы, но мне хотелось пройтись куда-нибудь ещё."
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    $ d2_evening_places += 1
    $ disable_current_zone()
    jump d2_evening_map

label d2_bed_time:

    scene black
    with dissolve
    show screen central_text("День 2 — Мысли, стянутые в узел")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    scene bg int_house_of_mt_night
    with dissolve
    play music music_list["no_tresspassing"] fadein 2
    window show
    "В домик я вернулся только после того, как разделался с личной гигиеной — всё-таки за мной ещё остались какие-то хорошие привычки из повседневной жизни."
    "Пионерский галстук, который я не стал надевать после душа, был брошен спинку стула."
    "До сна оставалось немного времени (или сколько мне удастся отвоевать у вожатой), и в первую очередь я решил занести все впечатления за сегодняшний день в блокнот."
    "А день был крайне насыщенным, так что придётся быть достаточно кратким и зафиксировать самое главное..."
    "Резким движением я вытянул сумку из-под кровати, чтобы взять химический карандаш с записной книжкой."
    "Несколько минут моя рука летала над бумагой в клетку — я писал о том, кого сегодня встретил, что узнал о них."
    "Я сделал отрывочные заметки об устройстве лагеря и работе кружков. Если мне повезёт вернуться в свой мир, то из любопытства я обязательно сравню «Совёнок» с реальными пионерскими лагерями..."
    "Поставив точку, я отложил карандаш."
    th "Вроде всё."
    "Вот уже я отодвинул стул, чтобы подняться, но замер и нахмурился."
    "Нет. Я что-то упускал. Что-то не слишком очевидное и плохо объяснимое."
    scene bg ext_musclub_day_bw
    with dissolve
    th "{i}Как где?{/i}"
    scene bg int_house_of_mt_night
    with fade
    "Пальцы снова зажали карандаш в тисках, макнули грифельный стержень в гранёный стакан, из которого вожатая подливала воду комнатным растениям."
    "Чернильно-синим по белому я вывел: «Голоса в голове»."
    th "Или только один голос, но звучащий по-разному.{w=1} Вопросительно.{w=1} Скептически.{w=1} Подталкивающе.{w=1} Принуждающе."
    "С трудом давя зевок, я устало приложил к лицу ладони, глядя сквозь пальцы на строчки в блокноте."
    stop music fadeout 1
    "..."
    play music music_list["smooth_machine"] fadein 3
    th "Ерунда. Нет у меня ни раздвоения личности, ни шизофрении."
    "Дома, правда, лежала справка с нетяжёлым диагнозом для откоса, какую, если верить стереотипам, должен иметь всякий уважающий себя битард."
    "Но это лишь подтверждало, что я полностью здоровый человек."
    "Захлопнув блокнот и спрятав его в сумку, я окинул взглядом все свои вещи, разложенные на прикроватной тумбе и столике. Надо было отвлечься от гнетущих мыслей."
    th "Чем бы теперь заняться?"
    call what_to_read
    "........."
    $ persistent.sprite_time = "day"
    show mt normal pioneer at center with dissolve
    window show
    "Ольга Дмитриевна вернулась чуть позже назначенного времени отбоя для пионеров. Войдя в комнату, она положила картонную папочку с бумагами на стол."
    show mt smile pioneer at center with dspr
    mt "Ну, как у тебя прошёл первый день в лагере?"
    mt "Было что-то интересное?"
    "Я пожал плечами."
    me "Неплохо, получше вчерашнего. Вроде бы, ничего особенного не произошло..." 
    me "И в то же время столько всего!"
    show mt grin pioneer at center with dspr
    "Вываливать свои впечатления я поостерёгся — многое из того, что привлекло моё внимание, подвергалось сравнению с родным для меня миром — о нём Ольге Дмитриевне знать было ни к чему. А откровенности, вроде утреннего одевания, тем более."
    "Но кое-чем я поделился, и вожатая, присев на кровать с улыбкой выслушала мои нескладные попытки выразить мысли и обойти поводы для лишних вопросов."
    "Было и то, что хотел выяснить я сам."
    if d2_us_dv_day:
        me "...Кстати, а в чём провинилась Ульяна перед Ингой Максимовной?"
        show mt normal pioneer at center with dspr
        mt "Она ей земли в пакет с кофе насыпала."
        me "Вот же!.. Ульяна!"
        show mt laugh pioneer at center with dspr
        "Я с искренним негодованием всплеснул руками, и это рассмешило Ольгу Дмитриевну."
        show mt smile pioneer at center with dspr
        mt "Ты, Семён, иногда приглядывай за Ульяной на всякий случай, чтобы она не набедокурила нигде, хорошо?"
        me "Ага, но разве за ней уследишь..."
        show mt grin pioneer at center with dspr
        mt "Уж постарайся!"
    if d2_seen_bathhouse:
        "...Я у вас баню нашёл и подумал, можно ли обычным пионерам ею пользоваться, ну, как душем?"
        show mt normal pioneer at center with dspr
        mt "Можно, правда, если ты не знаешь, как растапливать её и приводить в порядок, лучше не надо."
        show mt smile pioneer at center with dspr
        mt "Всё равно в эту смену мы всех вас обязательно сводим в баню!"
        me "Понял."
    me "И ещё... Вот когда я по клубам ходил, видел, что кружки шитья и столярного дела закрыты. Не знаете, почему?"
    show mt sad pioneer at center with dspr
    mt "Наш трудовик уволился два года назад. Тогда случилась одна неприятная история... А Михаил Ефграфович так и не подыскал замену ему."
    me "Что за история?"
    show mt normal pioneer at center with dspr
    mt "К сожалению, Семён, я не имею права говорить об этом."
    mt "Много чего было. Последней каплей стала ссора между трудовиком и Ингой Максимовной."
    "Я не стал докапываться — в межличностные склоки не хотелось совать носа."
    show mt smile pioneer at center with dspr
    "Вместо этого я рассказал о самом ярком событии за день, а Ольга Дмитриевна с вниманием слушала."
    me "...Да...{w} Это был хороший день."
    show mt laugh pioneer at center with dspr
    mt "Думаю, завтра будет ещё интереснее!" 
    show mt surprise pioneer at center with dspr
    mt "Вообще-то, Семён, я ожидала, что ты уже спишь. Почему сам не разделся, не выключил свет и не лёг в постель?"
    me "Не привык ложиться так рано."
    show mt grin pioneer at center with dspr
    mt "У себя дома — пожалуйста, а у нас есть чёткое расписание. Раньше в некоторых лагерях общим рубильником сразу всем свет отключали."
    show mt smile pioneer at center with dspr
    mt "Ты ведь уже взрослый парень, мог бы и проявить самостоятельность."
    me "Увлёкся."
    show mt normal pioneer at cright with dspr
    "Вожатая стала убирать вещи со своей кровати."
    hide mt with dissolve
    "Динамики приставки «Электроника» были залеплены кусочками пластыря, и едва слышный пикающий звук вряд ли расшевелил бы меня утром, поэтому я выставил время срабатывания будильника на мобильном телефоне."
    "Хоть какая-то польза при том, что связь не ловится."
    "Я сел на кровати, собираясь раздеться. Тронул пуговицу рубашки, что чуть ниже расстёгнутого воротника, и остановился — вспомнил, как до построения вожатая ловко повязала мне галстук."
    "Всё случилось быстро, и я совсем не понял, каким образом надо затягивать узел... А завтра от меня потребуется то же самое. И придётся просить вожатую помочь."
    "Или не просить и на линейке получить выговор за неряшливость при всех. А у пионеров спрашивать — засмеют."
    th "Так не годится..."
    stop music fadeout 1
    play music music_list["she_is_kind"] fadein 2
    "Я поднялся и взял красный галстук."
    me "Ольга Дмитриевна!.."
    show mt normal pioneer at center with dissolve
    "Вожатая обернулась."
    mt "Что, Семён?"
    me "Утром вы завязали мне галстук, а я не понял, как это делается. Можете показать мне ещё раз, чтобы я завтра смог правильно надеть его?"
    show mt surprise pioneer at center with dspr
    "Удивление тронуло Ольгу Дмитриевну лишь на секунду, однако она не растерялась."
    show mt grin pioneer at center with dspr
    mt "Не вопрос! Садись-ка рядом. И воротник застегни до конца."
    show mt smile pioneer close at center with dspr
    "Я присел к ней на кровать, протягивая краснотканный плат."
    "Ольга Дмитриевна лёгким движением накинула его мне на шею, за поднятый ворот. Я вдруг обнаружил себя сидящим в каких-то жалких пятнадцати сантиметрах от неё."
    show mt grin pioneer close at center with dspr
    mt "Стыдно пионеру не знать, как завязывать галстук!"
    show mt surprise pioneer close at center with dspr
    mt "Или у тебя в школе другая форма?"
    me "Другая."
    show mt smile pioneer close at center with dspr
    "Я согласился, но не сказал больше этого — про здешние школы я не имел понятия."
    mt "Всё равно, пионеры на дежурстве обязательно надевают галстуки к парадной форме."
    mt "Есть пара способов завязать узел. Смотри внимательно!"
    "Она перекинула правый конец плата через левый."
    mt "Делаем петлю — раз..."
    "Как Ольга Дмитриевна и требовала — я смотрел внимательно, однако совсем не на галстук. Мой взгляд уплыл от её рук к лицу."
    "Хоть и было заметно, что Ольга Дмитриевна устала за день, в ней почти неиссякаемо дышала та жизнь, та энергия, которой вожатый располагает к себе подопечных."
    "Но я, как взрослый человек, помимо того видел ещё и красоту зрелой девушки."
    "В наклоне головы, в странном блеске чуть полноватых губ... И в полуприкрытых длинными ресницами глазах."
    "Цвет глаз был карим, вернее, глубоким красным, как чай."
    th "Интересно, сколько ей лет?"
    "Наверно, Ольга Дмитриевна была мне ровесницей, плюс-минус несколько лет. Единственная в лагере. Возможно, ещё та вожатая младшего отряда, а вот медсестра явно была старше."
    "Я уже давно не видел своих ровесниц, знакомых со школы или университета, и тем более не говорил с ними. Кто знает, где они сейчас и что с ними стало?{w} И так же давно это сделалось неважным."
    "А теперь, рядом с вожатой, моей соседкой по домику в лагере, под влиянием глубинного желания вперемешку с любопытством вопрос о возрасте приобрёл смысл."
    th "Она ведь скажет: «Неприлично пионеру такое спрашивать!»"
    th "Но я-то не пионер..."
    mt "...Делаем вторую петлю — два, и продеваем конец через первую петлю — это три. Готово."
    show mt grin pioneer close at center with dspr
    mt "Запомнил?"
    me "Угу."
    th "Нет, конечно! Я засмотрелся на вас!"
    me "А второй способ?"
    show mt smile pioneer close at center with dspr
    "Ольга Дмитриевна распустила узел моего галстука."
    mt "Он даже проще."
    "Я весь обратился в слух, чтобы моя просьба о помощи не стала пшиком только потому, что мне повезло быть соседом красивой вожатой."
    mt "Завязывается почти так же, но правый конец заводим под левый, а не сверху. И делаем узел."
    "Она стянула и левую, и правую сторону плата одним концом, продев его у воротника в петлю."
    me "В самом деле просто."
    me "Спасибо, Ольга Дмитриевна.{w} Я теперь сам."
    show mt surprise pioneer close at center with dspr
    mt "Не за... Семён!"
    stop music fadeout 2
    me "А?"
    "Я тут же понял, почему она возмутилась. Руки девушки задержались на концах галстука, а я, торопясь развязать узел, заключил её пальцы в обьятия своих ладоней."
    play music music_list["awakening_power"] fadein 0
    show mt angry pioneer close at center with dspr
    "Ольга Дмитриевна смутилась и отдёрнула руки, да и я сам был ошарашен своей ошибкой, превратившейся в романтический жест благодарности, едва-едва не преходящий границы дозволенного между пионером и вожатой."
    "Она внезапно посуровела, но злость и недовольство не могли скрыть смятение от возникшего недопонимания."
    mt "Так! Немедленно иди спать."
    me "А самому попробовать?"
    show mt rage pioneer close at center with dspr
    mt "Завтра попробуешь! А сейчас раздевайся и спать! И поторопись, пока я не достала свой молот."
    show mt angry pioneer close at center with dspr
    me "Молот?.."
    mt "Марш в постель!"
    menu:
        "Выдать пошлую шутку" if (d2_no_shame == True) and (sp_crg >= 2):
            me "В какую постель из двух?"
            "Я улыбнулся, надеясь, что Ольга Дмитриевна оценит игру слов и добродушно, без понуканий, даст мне спокойно лечь спать."
            show mt rage pioneer close at center with dspr
            "Она немедленно пригнулась за чем-то, лежавшим под кроватью, и вытащила огромный банхаммер."
            th "Напрасно надеялся!"
            stop music fadeout 0
            play sound sfx_armature_swish
            "Орудие просвистело в воздухе, и я не успел ни встать, ни увернуться, ни закричать, только сдавленно сказать «А...», перед тем молот впечатался мне в лицо."
            play sound sfx_body_bump
            scene black
            with dspr
            "..............."
            window hide
            $ sp_crg = sp_crg + 1
            $ d2_mt_banned = True
            return
        "Послушаться вожатую":
            $ lp_mt = lp_mt + 1
            pass
    "В голове ещё вертелись попытки глупо и скабрезно пошутить напоследок, но я не осмелился — вожатая достала из-под кровати здоровенный банхаммер."
    show mt rage pioneer close at center with dspr
    mt "Чтоб через минуту храпел. Или мне успокоить тебя?"
    th "Да такой штуковиной мамонта убить можно!"
    hide mt with dspr
    "Я мгновенно убрался с чужой постели, снимая злосчастный галстук и рубашку."
    "Еле стянув шорты и кинув их на стул, я прыгнул в кровать так, что она жалобно скрипнула сеткой, и накрылся простынёй."
    stop music fadeout 3
    "Шаги вожатой стали удаляться, а затем выключился свет."
    scene bg int_house_of_mt_night2
    #with dspr
    "Я позволил себе высунуть голову, оттянув простынь до плеч, но не повернулся к вожатой, уставившись в стенку."
    "Послышался шорох — видимо, Ольга Дмитриевна раздевалась следом, тоже готовясь ко сну."
    "Я закрыл глаза, заставляя себя унять волнение после встряски, но получалось это не очень."
    "Когда я вдруг зевнул, на тело накатила страшная усталость."
    "Что ни говори, а день вышел замечательным..."
    window hide
    if d2_girls_event >= 1:
        scene bg ext_square_day_bw
        with dissolve
        play music music_list["dance_of_fireflies"] fadein 1
        window show
        "Ждёт ли меня завтра такое же незабываемое утро?"
        "И та же самая зарядка — но во втором ряду, как мы обещали Шурику?"
        show el grin pioneer bw at cleft
        show sh upset pioneer bw at cright
        with dissolve
        sh "...будут упражнения с наклонами... По-моему, эти формы сзади не менее впечатляющи, чем груди."
        "Каким бы глупым сначала мне ни казался спор кибернетиков, всё равно что-то задело меня за живое.{w} Прозвучала та мысль, которой я нашёл развитие, но на зарядке она осталась без внимания."
        sh "...В женской фигуре всё должно быть прекрасно."
        scene anim prolog_2
        with dissolve
        "Эл и Шурик были неправы.{w} Нет, на грудь, ноги и талию безусловно приятно смотреть — я ведь парень всё-таки! Особенно лицемерно думать иначе после всех раздевающих взглядов, которые я ненароком бросал на вожатую с медсестрой и встреченных сегодня пионерок."
        "Но это ничто."
        "Ничто по сравнению с лицом."
        "Потому что большую часть времени людей приходится запоминать и знать в общении одетыми, и как, если не благодаря лицу?"
        "Один только голос или романтику анонимной связи я не считал: легко позволить чувствам выдать желаемое за действительное."
        "Те же чувства, вопреки всему, заставляют останавливать взгляд на той, чей образ вдруг уже так просто не выкинуть из головы."
        scene bg ext_square_day
        show mt smile panama pioneer far hidden at fleft
        show mz normal glasses pioneer far hidden at left
        show mi normal pioneer far hidden at cleft
        show us normal sport far hidden at center
        show un normal pioneer far hidden at cright
        show dv grin pioneer2 far hidden at right
        show sl normal pioneer far hidden at fright
        with dissolve2
        "Видеть лицо, когда она вдалеке, не замечая тебя, поворачивается и заговаривает с подругой, видеть живые блестящие глаза, улыбку, наметившую ямочками щёки, — всё внутри оставляет след, точно калёным железом."
        "Минуты длятся, словно часы, но за бурной чередой мероприятий, звонков на обед и отбоем не замечаешь, как скоротечно время."
        "И кому-то из двух надо успеть решиться на первый шаг, даже если у него или неё, воплощения невинности, и в мыслях нет ничего подобного."
        scene bg int_library_day
        show mt smile panama pioneer far hidden at fleft
        show mz normal glasses pioneer far hidden at left
        show mi normal pioneer far hidden at cleft
        show us normal sport far hidden at center
        show un normal pioneer far hidden at cright
        show dv grin pioneer2 far hidden at right
        show sl normal pioneer far hidden at fright
        with dissolve2
        "Сначала — неловкое знакомство, первые попытки обратиться за чем-то, начать действовать сообща."
        "И разговоры о неважном, и миллионы мелочей, вроде протянутой руки, подшучивания или справедливого упрёка."
        scene bg ext_stage_big_day
        show mt smile panama pioneer far hidden at fleft
        show mz normal glasses pioneer far hidden at left
        show mi normal pioneer far hidden at cleft
        show us normal sport far hidden at center
        show un normal pioneer far hidden at cright
        show dv grin pioneer2 far hidden at right
        show sl normal pioneer far hidden at fright
        with dissolve2
        "Потом — как будто случайно начинаешь чаще оказываться там же, где и она."
        "Слово за словом, игра за игрой, делается таким близким её дыхание, теперь вовсе не чужое, а знакомое..."
        scene bg ext_dining_hall_away_sunset
        show mt smile panama pioneer far hidden at fleft
        show mz normal glasses pioneer far hidden at left
        show mi normal pioneer far hidden at cleft
        show us normal sport far hidden at center
        show un normal pioneer far hidden at cright
        show dv grin pioneer2 far hidden at right
        show sl normal pioneer far hidden at fright
        with dissolve2
        $ renpy.pause(1)
        scene bg ext_dining_hall_away_night
        show mt smile panama pioneer far hidden at fleft
        show mz normal glasses pioneer far hidden at left
        show mi normal pioneer far hidden at cleft
        show us normal sport far hidden at center
        show un normal pioneer far hidden at cright
        show dv grin pioneer2 far hidden at right
        show sl normal pioneer far hidden at fright
        with dissolve2
        "Плывущий день незаметно сменяют вечер и прогулка наедине, и вы понемногу догадываетесь, что же происходит, какими словами выражается стеснение и волнение..."
        scene bg ext_beach_night
        show mt smile panama pioneer far hidden at fleft
        show mz normal glasses pioneer far hidden at left
        show mi normal pioneer far hidden at cleft
        show us normal sport far hidden at center
        show un normal pioneer far hidden at cright
        show dv grin pioneer2 far hidden at right
        show sl normal pioneer far hidden at fright
        with dissolve2
        "Когда кроме физического в права вступает душевное."
        "Когда в человеке на расстоянии ладони бьётся юность, испытываешь трепет и поневоле влюбляешься, как мальчишка."
        window hide
        scene anim prolog_2
        with dissolve
        window show
        th "...Я это могу.{w} Но я не должен."
        th "Не должен, пока не..."
        stop music fadeout 2
        scene black
        with fade
    elif d2_girls_event == 0:
        if tech_club:
            scene bg int_clubs_male_day_bw
            with dissolve2
            play music music_list["doubt_everyone"] fadein 1
            window show
            "Всё необыкновенное запало в память."
            "Казалось, с того момента, как я сел в автобус, начались чудеса. Прошло два дня, а чудеса всё не прекращались."
            "Пионерия в две тысячи восьмом году.{w} Дети с гетерохромией.{w} Роботы с самообучающимся искуственным интеллектом.{w} Прямоходящий кот зелёной окраски, который, ко всему прочему, не дурак выпить."
            th "И ведь мне точно это не снится!{w=0.5} Но внутри гложет чувство, будто я теряю границу между сказкой и реальностью."
            show el smile pioneer bw at center with dspr
            el "...Мы знаем секрет, а остальные ребята — нет. Устроим для них праздник, сказку."
            scene anim prolog_2
            with dissolve
            "Это не так, это неправда! Всё, что необыкновенно и чудесно здесь для меня, для них серая, обыденная реальность. У них не вызовет шока и онемения нечто из ряда вон выходящее по моим жалким представлениям."
            "А когда пройдёт время, и я привыкну ко всему, этот мир тоже станет по-своему обычным, плоским и серым, как мой родной."
            "К несчастью или нет, мне известно, в чём главное отличие реальности от сказки.{w} Рано или поздно оно проявит себя и здесь."
            "Может быть, я ещё вернусь домой прежде, чем найду подтверждение своей выдуманной теории..."
            stop music fadeout 2
            scene black
            with fade
        else:
            scene black
            with fade
            pass
    "И я, не в силах больше сопротивляться усталости, провалился в темноту."
    if (d2_girls_event == 0) and (tech_club == False):
        "С отчетливой надеждой на то, что завтра со мной случится что-то необыкновенное..."
    "Сон поглотил меня."
    "......................."
    window hide

return

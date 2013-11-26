# День 4.
# День ... .

init:
    $ day_4_necessary_done = 0

#Утро
label day_4_start:
    $ new_chapter(4, u"Утро")

    $ flash = Fade(.25, 0, .75, color="#fff")

    $renpy.music.set_volume (0.7, channel=7)
    #play music music_list["no_tresspassing"] channel 7
    play music music_list["just_think"] channel 7

    scene bg black
    "Темно."
    "Я попытался открыть глаза, но ничего не вышло."
    "Возможно, глаза уже открыты?"
    "Где... я?"
    "Откуда-то издалека, постепенно приближаясь, появляется тусклый свет."
    "Как будто зажигаются лампочки."
    "Точно! Это свет ламп аварийного освещения."
    "Наконец возле моего правого плеча загорелась еще одна и я смог разглядеть..."
    "Коридор."
    "Я был в каком-то странном месте."
    "Толстые стены, опутанные сетью трубопроводов."
    "В конце - массивная дверь. Даже не дверь, а задраенный люк."
    "Как на подводной лодке."
    "Я никогда не был здесь раньше, но..."
    "Каким-то образом я знал это место."
    "Я взглянул на потолок. {w=.4}Все те же переплетения труб, и никакого намека на яркий солнечный свет."
    "Я под землей. Почему то я был уверен в этом."
    "И еще знал, что пришел в этот подвал... нет, в этот бункер, за чем-то очень важным для меня."
    "И это \"что-то\"... {w=.3}Я пытался вспомнить, что именно, и не мог. Но..."
    "Все это было сейчас совершенно неважно. Потому что оно находилось прямо передо мной."
    "За этой закрытой дверью."
    "И нужно было только пройти пять метров, разделяющие нас, и открыть ее..."
    "#Небольшой зум."
    "Я сделал шаг и... {w=.3}Это было невыносимо трудно. Ноги отказывались подчиняться."
    "Все тело словно налили свинцом."
    "Но страшнее всего был голос."
    "Тихий, еле слышимый, голос вдруг раздался и разнесся по коридору."
    voice "Даже не думай..."
    "Его эхо отталкивалось от стен, усиливаясь."
    "Он исходил, казалось, отовсюду сразу."
    "#Небольшой зум."
    "С трудом я сделал еще шаг."
    "Я знал, что мне не дадут так просто добраться до этой двери!"
    "Что будут мешать, пытаться запутать, обмануть."
    "Но у них ничего не выйдет!"
    "Сейчас нужно было только идти вперед."
    "#Небольшой зум."
    "Еще шаг."
    "Чтобы подбодрить себя, я закричал:"
    me "Я смогу! Я доберусь!"
    "И не услышал собственного голоса..."
    "Я поднял ногу, чтобы сделать предпоследний шаг. До дверей оставалось совсем немного!"
    "Но чьи-то грубые руки схватили меня за плечи и сжали."
    "Тот же голос, что раздавался раньше, произнес уже испуганно:"
    voice "Семен! Семен!"
    "Он звал по имени и..."
    voice "Это же я! Семен!"
    "Нет! Только не слушать! Они будут пытаться обмануть!"
    "Нужно идти!"
    "Отбиваясь от невидимых рук, я сделал еще шаг. Последний!"
    "Внезапно руки, сдерживающие меня исчезли. Голос тоже пропал."
    "Дверь была прямо передо мной! Осталось только открыть ее и..."

    stop music fadeout 1 channel 7

    "*Звук бегущей воды."

    scene bg int_house_of_mt_day
    with flash
    show mt std
    "Я лежал в мокрой кровати, под сбившимся одеялом, а надо мной стояла Ольга Дмитриевна."
    "Она что-то говорила мне. Вот только я не слышал."
    "И еще в руках у нее был пустой графин... {w=.3}в котором еще вчера была вода."

    

    $renpy.music.set_volume (0.7, channel=7)
    #play music music_list["everyday_theme"] channel 7
    play music music_list["smooth_machine"] channel 7

    "Словно издалека, до меня стали долетать звуки."
    mt "Ты меня слышишь, Семен?"
    "Я кивнул."
    mt "Вчера проспал, сегодня проспал."
    "Я скосил глаза на столик."
    "10.34"
    "Сегодня я проснулся даже раньше обычного..."
    mt "А теперь еще и вожатую ударил!"
    "Она показала на свою руку, где был розовый след."
    "Я попытался собраться с мыслями."
    "Почему-то даже сейчас, несмотря на то, что все оказалось лишь сном, мне было грустно."
    "И вовсе не потому, что я ударил вожатую."
    "Мне не удалось добраться до двери! {w=.4}А она казалась такой реальной!"
    mt "Что скажешь в свое оправдание?"
    "Я только пожал плечами."
    "Видимо, Ольга Дмитриевна поняла мое состояние, потому что сказала:"
    mt "Кошмар, наверное, приснился."
    "Cовсем в этом неуверенный, я все же кивнул."
    me "Извините... за руку."
    mt "А за то, что проспал, значит, не извиняешься?"
    $ mt_emo = 'smile'
    "Она улыбнулась."
    mt "Ладно, даю тебе пять минут."
    mt "Вставай, одевайся и живо умываться."
    hide mt
    "И вышла из домика."
    pass
    scene bg int_house_of_mt_day
    with flash
    show mt std
    "Когда через пять минут она вошла снова, я был уже одет."
    mt "Ну, как? Ты в порядке?"
    "Я не знал, что ответить."
    "Грусть притупилась, но вместо нее возник стыд за то, что ударил вожатую и в очередной раз проспал все утро."
    "Честно говоря, я давно уже забыл, что это такое - стыд, но тут пришлось вспомнить."
    mt "Больше не будешь бить вожатую?"
    me "............."
    "Вся моя теперешняя жизнь походит черт знает на что!"
    "И еще у меня было странное предчувствие, потому что Ольга Дмитриевна принесла с собой большой пакет."
    if day_3_badmorning == 1:
        "Даже больше, чем вчера."
    else:
        pass
    "Ольга Дмитриевна заметила, куда я смотрю, и снова улыбнулась."
    mt "Да-да! Это тебе."
    mt "Проспал - будешь отрабатывать."
    "..................."
    mt "А заодно я тебе принесла бутерброд."
    me "Спасибо!"
    "Кажется, утро было не таким уж и плохим."
    "Я протянул руку..."
    mt "Даже не думай!"
    scene bg int_house_of_mt_day
    with flash
    show mt std
    "Голос из... из сна - так это была Ольга Дмитриевна!"
    "Я мотнул головой, а она продолжала."
    mt "...ле того, как умоешься!"
    mt "За работой и поешь."
    "Она поставила пакет на пол."
    "Ладно, сейчас она уйдет..."
    mt "Идем, я тебя провожу до умывальника."
    "Она хитро прищурилась."
    mt "А то, знаю я тебя! Еще потеряешься и не дойдешь."
    pass
    ".........."

    scene bg ext_washstand_day
    with dissolve
    "Пока мы шли, мне объясняли, что я должен буду сделать."
    mt "Посчитай столбики с цифрами и убедись, чтобы они совпадали. Их не так много."
    "Я с сомнением кивнул."
    if day_3_badmorning == 1:
        "Все как вчера, что ли?"
    else:
        pass
    "Когда мы вышли к умывальникам, Ольга Дмитриевна заметно повеселела."
    mt "Ну вот! Добрался целый и невредимый."
    mt "Все понял?"
    me "Проверить столбики..."
    mt "Молодец!"
    me "Да, но что, если..."
    "Она нетерпеливо махнула рукой."
    mt "Сам разберешься."
    "Развернулась и на прощанье сказала:"
    mt "Чао."
    "Хм... А почему она была в купальнике?"
    "......................."

    $ set_mode_nvl()
    "Дальше будет выбор. Делать работу за М-тян или не делать."
    "Если решили читать бухгалтерские книги СНОВА (попали в 3й день на бэд-ветку), то открывается небольшой секрет. Внимательность гг позволит ему найти в книгах информацию о том, что огромные средства выделяются... на медпункт. Он достанет старые книги (которые М-тян не выбросила, а свалила под своей кроватью) и узнает, что к этому причастна К-сенсей."
    "Разобравшись, что деньги перечисляются на секретную лабораторию, гг попытается шантажировать К-сенсей или просто проболтается об этом открытии. Та сделает ему уже описанный минет с кубиками льда... и угроза (в лице Семена) будет устранена. Секретная ветка пройдена. Начинайте игру заново или с места сохранения."
    $nvl_clear()
    "Если же герой отказывается от работы (либо устал от вчерашней, либо просто ленится и идет гулять), то он получает обычные блоки с девушками."
    "Вечером он врет М-тян о том, что сделал работу, и та несет ее своему начальству. Потому что эти книги были самыми настоящими и потому что ошибки не были выявлены - М-тян наказывают. И пятый день начинается, как и задумывалось, с того, что М-тян занята исправлением книг."
    "Если же герой исправляет ошибки, то М-тян уезжает по другой причине. Здесь событийная вилка."
    $ set_mode_adv()
    "......................."
    return

    jump day_4_map_prepare



#Утренние блуждания по карте

label day_4_map_prepare:
    $ disable_all_zones()

    $renpy.music.set_volume (0.7, channel=7)
    play music music_list["everyday_theme"] channel 7

    $ set_zone("music_club",   "day_4_event_music_club")
    $ set_zone("clubs",        "day_4_event_clubs")
    $ set_zone("camp_entrance","day_4_event_camp_entrance")
    $ set_zone("dv_us_house",  "day_4_event_dv_us_house")
    $ set_zone("dining_hall",  "day_4_event_dining_hall")
    $ set_zone("sport_area",   "day_4_event_sport_area")
    $ set_zone("beach",        "day_4_event_beach")
    $ set_zone("me_mt_house",  "day_4_event_me_mt_house")
    $ set_zone("library",      "day_4_event_library")
    $ set_zone("medic_house",  "day_4_event_medic_house")
    $ set_zone("estrade",      "day_4_event_estrade")
    $ set_zone("square",       "day_4_event_square")
    $ set_zone("boat_station", "day_4_event_boat_station") 

    $ day_4_necessary_done = 0
    jump day_4_map

#Условие для попадания на обед
label day_4_map:
    $ new_chapter(4, u"Знакомство с лагерем")
    if  day_4_necessary_done != 4:
        $ show_map() #day_4_map_prepare
    else:
        jump day_4_dinner

#Муз. клуб
label day_4_event_music_club:
    scene bg ext_musclub_day
    scene bg int_musclub_day
    show mi std with dissolve
    mi "Да ничего, его постоянно роняют."
    hide mi
    $ day_4_necessary_done += 1
    $ disable_current_zone()
    jump day_4_map
    
#Клуб
label day_4_event_clubs:
    if been_there()>1:
        scene bg ext_clubs_day
        "Нет, хватит! Больше никакой кибернетики на сегодня!"
        jump day_4_map
    scene bg ext_clubs_day
    $ day_4_necessary_done += 1
    jump day_4_map

#Ворота лагеря
label day_4_event_camp_entrance:
    if been_there()==1:
        scene bg ext_camp_entrance_day
        "Здесь я уже был вчера, когда приехал."
        jump day_4_map
    if been_there()==4:
        scene bg ext_camp_entrance_day
        "Я уже был здесь. Делать мне нечего - ходить туда-сюда."
        $ disable_current_zone()
        jump day_4_map

#Домики 4 (западные)
label day_4_event_dv_us_house:
    if been_there()>1:
        scene bg map
        "Идти туда, зная, что там живут Дваче и Ульянка? Да ни за что на свете!"
        $ disable_current_zone()
        jump day_4_map
    scene bg ext_houses_day
    scene bg ext_house_of_dv_day
    jump day_4_map

#Столовая
label day_4_event_dining_hall:
    scene bg map
    "Еще вчера я понял, что еда в лагере выдается только в строго определенное время."
    "Так что до обеда там делать абсолютно нечего, да и в бегунке столовая не указана."
    $ disable_current_zone()
    jump day_4_map

#Спорт. площадки
label day_4_event_sport_area:
    if been_there()>1:
        "В детство я возвращаться не собираюсь. У меня другие планы на вечер."
        $ disable_current_zone()
        jump day_4_map
    "На спортивной площадке какие-то малыши гоняли в футбол."
    jump day_4_map

#Пляж
label day_4_event_beach:
    scene bg ext_beach_day
    $ disable_current_zone()
    jump day_4_map

#Домики (северные)
label day_4_event_me_mt_house:
    if been_there()>1:
        scene bg ext_houses_day
        "Хм. И что я здесь забыл?"
        jump day_4_map
    scene bg ext_house_of_mt_day
    "Я вышел к своему домику и остановился."
    jump day_4_map

#Библиотека
label day_4_event_library:
    scene bg ext_library_day
    scene bg int_library_day
    $ day_4_necessary_done += 1
    $ disable_current_zone()
    jump day_4_map

#Медпункт
label day_4_event_medic_house:    
    if been_there()>1:
        scene bg ext_aidpost_day
        "Вот разберусь с бегунком - буду каждый день в медпункт заглядывать!"
        $ disable_current_zone()
        jump day_4_map
    scene bg ext_aidpost_day
    scene bg int_aidpost_day
    show cs std with dissolve
    $ day_4_necessary_done += 1
    jump day_4_map

#Эстрада
label day_4_event_estrade:
    scene bg ext_stage_big_day
    scene bg ext_stage_normal_day
    $ disable_current_zone()
    jump day_4_map

#Площадь
label day_4_event_square:
    $ rand_val = renpy.random.choice([1,4,3])
    if rand_val == 1:
        scene bg ext_square_day
        th "Странный памятник."
    else:
        if rand_val == 4:
            scene bg ext_square_day
            me "Похоже, это единственное место, где все по-прежнему."
        else:
            scene bg ext_square_day
            th "Странный памятник."
    jump day_4_map

#Причал
label day_4_event_boat_station:
    if been_there()>1:
        scene bg ext_boathouse_day
        "Я здесь уже был. Нужно отвязаться от этого бегунка. Тогда я смогу куда угодно пойти."
        $ disable_current_zone()
        jump day_4_map
    scene bg ext_boathouse_day
    "Приятно посидеть здесь, когда за тобой никто не гонится."
    scene bg ext_boathouse_day
    jump day_4_map


#ОБЕД

label day_4_dinner:
    $ new_chapter(4, u"Обед")

    $renpy.music.set_volume (0.7, channel=7)
    play music music_list["everyday_theme"] channel 7

    "Раздается сигнал на обед."
    scene bg black with fade
    scene bg ext_dining_hall_near_day
    show bg int_dining_hall_day
    scene bg black with fade


#Послеобеденный ивент
    $ new_chapter(4, u"Карточный турнир")

    jump day_4_mapAf_prepare

#Гуляния по карте после обеда
label day_4_mapAf_prepare:
    $ disable_all_zones()

    $renpy.music.set_volume (0.7, channel=7)
    play music music_list["everyday_theme"] channel 7

    $ set_zone("music_club",   "day_4_eventAf_music_club")
    $ set_zone("clubs",        "day_4_eventAf_clubs")
    $ set_zone("camp_entrance","day_4_eventAf_camp_entrance")
    $ set_zone("dv_us_house",  "day_4_eventAf_dv_us_house")
    $ set_zone("dining_hall",  "day_4_eventAf_dining_hall")
    $ set_zone("sport_area",   "day_4_eventAf_sport_area")
    $ set_zone("beach",        "day_4_eventAf_beach")
    $ set_zone("me_mt_house",  "day_4_eventAf_me_mt_house")
    $ set_zone("library",      "day_4_eventAf_library")
    $ set_zone("medic_house",  "day_4_eventAf_medic_house")
    $ set_zone("estrade",      "day_4_eventAf_estrade")
    $ set_zone("square",       "day_4_eventAf_square")
    $ set_zone("boat_station", "day_4_eventAf_boat_station") 

    $ day_4_necessaryAf_done = 0
    jump day_4_mapAf

label day_4_mapAf:
    $ new_chapter(4, u"Послеобеденные события")
    $ show_map() #day_4_mapAf_prepare

#Муз. клуб
label day_4_eventAf_music_club:
    if been_there()>1:
        scene bg map
        "Не хочу мешать. Лучше зайду в следующий раз."
        jump day_4_mapAf
    scene bg ext_musclub_day
    jump day_4_mapAf

#Клуб
label day_4_eventAf_clubs:
    if been_there()>1:
        scene bg map         
        "Клуб юного техника умеет ждать."
        jump day_4_mapAf
    scene bg ext_clubs_day
    "БГ вечерний."
    jump day_4_mapAf

#Ворота лагеря
label day_4_eventAf_camp_entrance:
    scene bg ext_camp_entrance_day
    "Б4. Сейчас начнется первый слот Дваче."
    scene bg black
    jump day_4_slot_dv

#Домики 4 (западные)
label day_4_eventAf_dv_us_house:
    scene bg ext_houses_day
    $ disable_current_zone()
    jump day_4_mapAf

#Столовая
label day_4_eventAf_dining_hall:
    scene bg map
    "Спасибо, ужина мне вполне хватило."
    $ disable_current_zone()
    jump day_4_mapAf

#Спорт. площадки
label day_4_eventAf_sport_area:
    show sl std
    "Славя. Б4. После него слот."
    scene bg black
    jump day_4_slot_sl

#Пляж
label day_4_eventAf_beach:
    scene bg ext_beach_day
    "БГ вечерний."
    scene bg black
    jump day_4_slot_un

#Домики (северные)
label day_4_eventAf_me_mt_house:
    scene bg map
    "Не идти же спать. Еще так рано, да и не ясно, что делать с тортом. "
    $ disable_current_zone()
    jump day_4_mapAf

#Библиотека
label day_4_eventAf_library:
    $ rand_val = renpy.random.choice([1,4,4])
    if rand_val == 1:
        scene bg ext_library_day
        "БГ вечерний."
        "Закрыто."
    else:
        if rand_val == 4:
            scene bg ext_library_day
            "Спят усталые игрушки, книжки спят? Ну-ну."
        else:
            scene bg ext_library_day
            "Почему библиотека закрыта? Я так хотел почитать на ночь Канта!"
    jump day_4_mapAf

#Медпункт
label day_4_eventAf_medic_house:
    scene bg ext_aidpost_day
    "У меня ничего не болит. Что я скажу... {w}Виоле?"
    "Я вспомнил утренний прием..."
    $ disable_current_zone()
    jump day_4_mapAf

#Эстрада
label day_4_eventAf_estrade:
    scene bg ext_stage_big_day
    show us std
    "Ульянка. Разговариваем, смеемся. Б4."
    scene bg black
    jump day_4_slot_us

#Площадь
label day_4_eventAf_square:
    scene bg ext_square_day
    $ disable_current_zone()
    jump day_4_mapAf

#Причал
label day_4_eventAf_boat_station:
    scene bg ext_boathouse_day
    $ disable_current_zone()
    jump day_4_mapAf



#УЖИН
    $ new_chapter(4, u"Ужин")
    scene bg int_dining_hall_day


#Гуляния по карте после ужина
    jump day_4_mapEv_prepare

label day_4_mapEv_prepare:
    $ disable_all_zones()

    $renpy.music.set_volume (0.7, channel=7)
    play music music_list["everyday_theme"] channel 7

    $ set_zone("music_club",   "day_4_eventEv_music_club")
    $ set_zone("clubs",        "day_4_eventEv_clubs")
    $ set_zone("camp_entrance","day_4_eventEv_camp_entrance")
    $ set_zone("dv_us_house",  "day_4_eventEv_dv_us_house")
    $ set_zone("dining_hall",  "day_4_eventEv_dining_hall")
    $ set_zone("sport_area",   "day_4_eventEv_sport_area")
    $ set_zone("beach",        "day_4_eventEv_beach")
    $ set_zone("me_mt_house",  "day_4_eventEv_me_mt_house")
    $ set_zone("library",      "day_4_eventEv_library")
    $ set_zone("medic_house",  "day_4_eventEv_medic_house")
    $ set_zone("estrade",      "day_4_eventEv_estrade")
    $ set_zone("square",       "day_4_eventEv_square")
    $ set_zone("boat_station", "day_4_eventEv_boat_station") 

    $ day_4_necessaryEv_done = 0
    jump day_4_mapEv

label day_4_mapEv:
    $ new_chapter(4, u"Вечерние события")
    $ show_map() #day_4_mapEv_prepare

#Муз. клуб
label day_4_eventEv_music_club:
    if been_there()>1:
        scene bg map
        "Не хочу мешать. Лучше зайду в следующий раз."
        jump day_4_mapEv
    scene bg ext_musclub_day
    jump day_4_mapEv

#Клуб
label day_4_eventEv_clubs:
    if been_there()>1:
        scene bg map         
        "Клуб юного техника умеет ждать."
        jump day_4_mapEv
    scene bg ext_clubs_day
    "БГ вечерний."
    jump day_4_mapEv

#Ворота лагеря
label day_4_eventEv_camp_entrance:
    scene bg ext_camp_entrance_day
    "Б4. Сейчас начнется первый слот Дваче."
    scene bg black
    jump day_4_slot_dv

#Домики 4 (западные)
label day_4_eventEv_dv_us_house:
    scene bg ext_houses_day
    $ disable_current_zone()
    jump day_4_mapEv

#Столовая
label day_4_eventEv_dining_hall:
    scene bg map
    "Спасибо, ужина мне вполне хватило."
    $ disable_current_zone()
    jump day_4_mapEv

#Спорт. площадки
label day_4_eventEv_sport_area:
    show sl std
    "Славя. Б4. После него слот."
    scene bg black
    jump day_4_slot_sl

#Пляж
label day_4_eventEv_beach:
    scene bg ext_beach_day
    "БГ вечерний."
    scene bg black
    jump day_4_slot_un

#Домики (северные)
label day_4_eventEv_me_mt_house:
    scene bg map
    "Не идти же спать. Еще так рано, да и не ясно, что делать с тортом. "
    $ disable_current_zone()
    jump day_4_mapEv

#Библиотека
label day_4_eventEv_library:
    $ rand_val = renpy.random.choice([1,4,4])
    if rand_val == 1:
        scene bg ext_library_day
        "БГ вечерний."
        "Закрыто."
    else:
        if rand_val == 4:
            scene bg ext_library_day
            "Спят усталые игрушки, книжки спят? Ну-ну."
        else:
            scene bg ext_library_day
            "Почему библиотека закрыта? Я так хотел почитать на ночь Канта!"
    jump day_4_mapEv

#Медпункт
label day_4_eventEv_medic_house:
    scene bg ext_aidpost_day
    "У меня ничего не болит. Что я скажу... {w}Виоле?"
    "Я вспомнил утренний прием..."
    $ disable_current_zone()
    jump day_4_mapEv

#Эстрада
label day_4_eventEv_estrade:
    scene bg ext_stage_big_day
    show us std
    "Ульянка. Разговариваем, смеемся. Б4."
    scene bg black
    jump day_4_slot_us

#Площадь
label day_4_eventEv_square:
    scene bg ext_square_day
    $ disable_current_zone()
    jump day_4_mapEv

#Причал
label day_4_eventEv_boat_station:
    scene bg ext_boathouse_day
    $ disable_current_zone()
    jump day_4_mapEv



#Слоты и/или сон, а потом новый день
label day_4_slot_us:
    show us std
    "Слот Ульянки. Поздравляю!!!"
    hide us
    "А сейчас можно повторить вечерние события."
    jump day_4_mapEv_prepare

label day_4_slot_un:
    show un std
    "Слот Лены. Поздравляю!!!"
    hide un
    "А сейчас можно повторить вечерние события."
    jump day_4_mapEv_prepare

label day_4_slot_dv:
    show dv std
    "Слот Дваче. Поздравляю!!!"
    hide dv
    "А сейчас можно повторить вечерние события."
    jump day_4_mapEv_prepare

label day_4_slot_sl:
    show sl std
    "Слот Слави. Поздравляю!!!"
    hide sl
    "А сейчас можно повторить вечерние события."
    jump day_4_mapEv_prepare

label loser4:
    scene bg ext_dining_hall_near_day
    "Черт! Так опозориться перед всем лагерем."
    "Нужно забыться. Поиграю-ка я в электронику."
    jump dream

label dream4:
    scene bg int_house_of_mt_night
    "Вы не выиграли слот. Может, повезет в следующий раз."
    "Сон и начало следующего дня."
    scene bg black
    "А сейчас можно повторить вечерние события."
    jump day_4_mapEv_prepare
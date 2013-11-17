init:
    $ prologue = 0

label prologue:

    $ make_names_unknown()

    $ backdrop = 'prologue'

    $ new_chapter(-1, u"Пролог")

    $ prolog_time()

    play music music_list["a_promise_from_distant_days_v2"] fadein 3

    $ renpy.pause(3)

    scene anim prolog_1 
    with fade3

    window show

    "Мне опять снился сон."
    "Один и тот же надоедливый сон преследовал меня уже пару недель. Или месяц?"
    "Не могу даже вспомнить, когда точно это началось."
    "Я зевнул, слегка потянулся."
    "В голове проносились расплывчатые обрывки сна, который я должен бы был уже выучить наизусть."
    "Стена. Ворота. И голос. Детский голос, спрашивающий меня:"
    window hide

    scene black 
    with fade3

    scene bg ext_camp_entrance_night 
    show owl 

    show prologue_dream 
    with fade3

    window show
    dreamgirl "Ты пойдешь со мной?"


    "Я отвечаю ей, в сотый раз."
    "Я всегда просыпаюсь после ответа."
    window hide

    $ renpy.pause(2)

    menu:
        "Да, я пойду с тобой":
            $ prologue = 1
        "Нет, я останусь здесь":
            pass

    $ renpy.pause(1)

    window show
    "Как мало мои слова значат хотя бы во сне..."


    stop music fadeout 5


    window hide

    scene bg black 
    with fade3

    $ renpy.pause(2)

    play sound_loop sfx_keyboard_mouse_computer_noise fadein 3

    scene anim 1 _prologue 
    with fade3

    $ renpy.pause(9.4, hard=True)

    scene anim 2 _prologue 
    with fade3

    $ renpy.pause(9.4, hard=True)

    scene anim 3 _prologue 
    with fade3

    $ renpy.pause(6.2, hard=True)

    window show
    "Электрический свет монитора бил мне в глаза."
    window hide

    show blinking  with dissolve

    $ renpy.pause(3.5)

    window show
    "Я вновь потянулся, моргнул пару раз, сгоняя остатки сна."
    hide blinking 
    "Я улыбнулся монитору, как старому другу."
    "Улыбка получилась чуть кривой. Но факт есть факт. Долгие годы он был моим верным и единственным собеседником."
    "Нет ников, нет имен. Только монитор и я."
    window hide
    show blinking  with dissolve

    $ renpy.pause(3.5)

    window show
    "Бывало, он резко менял свое мнение, противоречил сам себе. Бывало, я делал так же.{w} Но мы были одним. Родней."
    window hide

    hide blinking 

    $ renpy.pause(3)

    scene anim prolog_15 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_3 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_4 
    with fade
    $ renpy.pause(3, hard=True)

    stop sound_loop fadeout 4

    window show
    " Я отдавал себе отчет, что это могло быть слегка странноватым. Но факт есть факт – монитор был мне куда роднее и ближе всех тех обезьян, бродящих за моим окном."

    window hide

    $ renpy.pause(3)

    scene anim prolog_5 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_14 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_11 
    with fade
    $ renpy.pause(3, hard=True)

    window show
    "Мои глаза оббежали серые стены квартиры, очерченные серым светом из окна, за которым в сумерках проступал серый мегаполис. Неужели так должно все закончиться? "
    window hide

    play music music_list["farewell_to_the_past_edit"] fadein 5

    $ renpy.pause(3)

    scene anim prolog_2 
    with fade
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Раньше все это было по-другому.{w} Большой цветущий город, утопающий в зелени. Яркое солнце зимой и летом. Огни новогодних елок. Будущее.{w} А затем все начало меняться. Небо все чаще было затянуто болезненно-серыми тучами. Улыбки возникали на лицах людей все реже. А нерешенных вопросов в моей голове накапливалось все больше.{w} Я поступил в институт. Скорее дань традиции, чем действительный выбор. Ни у кого не было особых удивлений, когда я был выпнут оттуда, не дотянув даже до третьего курса.{w} И вот я здесь. Один, в темной квартире, без продуктов в холодильнике.{w} Без будущего."
    nvl clear
    window hide

    $ renpy.pause(3)

    window show
    "Я не был несчастлив. В своей запертой квартирке, дверь которой открывалась лишь во время еженедельных «вылазок за продуктами», я создал себе небольшой уютный мирок. В этом мне помог единственный друг. Монитор.{w} Я пытался работать, но много ли денег мне надо? Я был достаточно везуч – мои родители были все еще живы. Время от времени мной овладевала уверенность в том, что все это время во мне был скрыт гениальный писатель, или музыкант. Или хотя бы шахматист.{w} Что же, на сегодняшний момент я его еще не выкопал.{w} Зачем я здесь? Чего я хочу?{w} В последнее время я стал склоняться к мысли, что не хочу ничего."
    nvl clear
    window hide

    scene bg semen_room_window 
    with fade

    stop music fadeout 4

    play sound_loop sfx_street_traffic_outside fadein 2

    $ renpy.pause(3)

    window show
    "Нехотя я подошел к годами не мытому окну, за которым с трудом угадывались очертания соседних хрущевок. Серые сумерки сменились типичным зимним вечером. С неба лениво падали снежинки. Это вдохнуло в меня немного энергии."
    "Такие вечера всегда напоминали мне о детстве. О времени, когда вопросов не было."
    "Сегодня у меня был необычный день. Я был приглашен на встречу моих институтских «товарищей». И я ожидаемо не смог сказать «нет». Меня уговорил один из моих немногочисленных знакомых. Он хоть и неплохой парень, но все же не сравнится с монитором."
    "Но факт есть факт. Я еду. Целое приключение для меня, не правда ли?"
    window hide

    $ renpy.pause(4)

    stop sound_loop fadeout 3

    play ambience ambience_cold_wind_loop fadein 3

    $ set_mode_adv()

    play sound sfx_intro_bus_stop_steps

    scene anim intro_1 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_2 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_3 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_4 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_5 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_6 
    with fade
    $ renpy.pause(3, hard=True)

    play sound sfx_intro_bus_stop_sigh

    scene anim intro_8 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_7 
    with fade
    $ renpy.pause(3, hard=True)

    scene bg bus_stop 
    with fade

    window show
    "На остановке был только я."
    "Снегопад закончился, и я остался один на один с черным декабрьским холодом."
    "Автобус запаздывал, и мало-помалу я пришел к пониманию, что зима – не лучшее время года."
    "Не то, чтобы я любил лето. Или осень. Не то, чтобы я любил еще хоть что-либо. Даже монитор."
    "Я закрыл глаза в детской надежде согреться."
    window hide

    $ renpy.pause(3)

    scene anim prolog_2 
    with fade
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Яркое солнце, шелест листвы. Вокруг бегают дети.{w} Мои друзья. Смех, слезы, обида. Все такое настоящее."
    "Мечты, надежды, цели. Я не хотел стать космонавтом, но я ни на секунду не сомневался, что стану важным.{w} Стану нужным."
    "Стану умным. Красивым. Встречу умницу-красавицу, которая полюбит меня с первого взгляда. Я для нее, она для меня."

    nvl clear
    window hide

    play sound sfx_intro_bus_engine_start

    $ renpy.pause(3)

    play sound_loop sfx_intro_bus_engine_loop fadein 3

    $ set_mode_adv()

    scene anim intro_9 
    with fade2

    window show
    "Звук работающего двигателя прервал мой сеанс самоистязания."
    "Автобус. Несколько необычный, но ярко освещенная табличка «410» красовалась чуть выше лобового стекла. Мой маршрут."
    window hide

    $ renpy.pause(2)

    scene anim intro_10 
    with fade

    play sound sfx_intro_bus_door_open

    $ renpy.pause(3, hard=True)
    scene anim intro_11 
    with fade
    $ renpy.pause(1, hard=True)

    stop sound_loop fadeout 4

    scene anim intro_13 
    with fade2
    $ renpy.pause(3, hard=True)

    scene bg intro_xx 
    with fade

    stop ambience fadeout 2
    play sound_loop sfx_bus_interior_moving fadein 4

    window show
    "За стеклом проносились городские улицы, заполненные толпами людей, которых я так ненавижу."

    $ volume(0.5, 'music')

    play music music_list["lightness_radio_bus"] fadein 7

    "Бесконечный поток серых туш, и днем и ночью. Стекло автобуса, казалось, дрожало от непрекращающегося гула улья. Но внутрь он все же не проникал."
    "Потрескивающий радиоприемник наигрывал какую-то старую мелодию."
    "Пару минут я гонял в голове несвязные мысли о загнивающем обществе, пока огни рекламных вывесок не принудили меня раздраженно зажмуриться."
    "Мелодия из трещащего приемника, казалось, согревала пустой салон. Я не смог сдержать зевок."
    "Через несколько мгновений я поймал себя на мысли, что засыпаю."
    window hide

    stop music fadeout 3

    show blink  with dissolve
    $ renpy.pause(1.5)

    window show
    "Прикрыв глаза от очередного надоедливого потока света, я провалился в сон."
    window hide

    stop sound_loop fadeout 3

    scene bg black 
    with fade3

    $ renpy.pause(3)

    $ volume(1.0, 'music')

    jump opening

label opening:



    $ renpy.pause(2, hard=True)

    play music music_list["opening"] fadein 5

    scene black 

    $ renpy.pause(3, hard=True)

    scene op_back 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_sl 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_un 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_us 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_dv 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_mi 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_uv 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show logo_day 

    with dissolve2

    $ renpy.pause(2, hard=True)

    scene black 
    with dissolve2

    stop music fadeout 5

    $ renpy.pause(5, hard=True)

    jump day1

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

    "Мне опять снился {i}этот{/i} сон..."
    "Одно и то же надоедливое видение преследовало меня пару недель, если не месяц."
    "Не могу вспомнить, когда всё началось."
    "Проснувшись, я зевнул и слегка потянулся."
    "В голове мелькали расплывчатые обрывки сна, которые я успел запомнить."
    "Стена. Ворота. И голос незнакомой девочки." 
    "Детский голос, зовущий меня:"
    window hide

    scene black 
    with fade3

    scene bg ext_camp_entrance_night 
    show owl :
        pos (931, 88)
    show prologue_dream 
    with fade3

    window show
    dreamgirl "Ты пойдешь со мной?"
   
    
    "Я отвечаю ей в сотый раз."
    "После ответа я всегда просыпаюсь."
    window hide

    $ renpy.pause(2)

    menu:
        "Да, я пойду с тобой":
            $ prologue = 1
        "Нет, я останусь здесь":
            pass

    $ renpy.pause(1)

    window show
    "Как мало значат мои слова даже во сне..."
    

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
    "Я вновь потянулся, моргнул пару раз, прогоняя остатки сна."
    hide blinking 
    "Сев поудобнее, я криво улыбнулся экрану, как старому другу."
    "Факт есть факт: долгие годы он был моим верным и единственным собеседником."
    "В сети я бываю там, где нет ников и нет имен, среди людей, подобных мне."
    "В их обществе я растворяюсь."
    window hide
    show blinking  with dissolve

    $ renpy.pause(3.5)

    window show
    "Зачастую они резко меняли свое мнение, противореча своим убеждениям. Иногда и я грешил тем же.{w} Но мы были одним." 
    "Единомышленниками, родственными душами."
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
    "Я отдавал себе отчет, что другим это кажется слегка странноватым. Но факт есть факт – комп был мне куда ближе всех тех обезьян, бродящих по серым улицам города."
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
    "Мой взгляд оббежал невзрачные стены квартиры, очерченные бледным светом из окна, за которым в сумерках проступал силуэт мегаполис."  
    "Неужели я буду жить так до конца своих дней?"
    window hide

    play music music_list["farewell_to_the_past_edit"] fadein 5

    $ renpy.pause(3)

    scene anim prolog_2 
    with fade
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Раньше всё было по-другому.{w} Большой цветущий город, утопающий в зелени. Яркое солнце зимой и летом. Огни новогодних ёлок. Будущее.{w} А затем начались изменения. Небо чаще затягивалось болезненно-серыми тучами. Реже стали видны улыбки на лицах людей.  А нерешённые проблемы и нереализованные желания накапливалось долговым грузом в моей жизни.{w} Я поступил в институт. Скорее дань традиции, чем самостоятельный выбор. Никто из родных не удивился, когда я был выпнут оттуда, не дотянув до третьего курса.{w} И вот я здесь. Один, в тёмной квартире, без продуктов в холодильнике.{w} Без будущего."
    nvl clear
    window hide

    $ renpy.pause(3)

    window show
    "Я не был несчастлив в своей запертой крепости, дверь которой открывалась лишь во время еженедельных вылазок за продуктами. Здесь я создал себе небольшой уютный мирок, и в этом мне помог единственный друг. Монитор.{w} Я пытался работать, но много ли денег мне надо? Я достаточно везуч – мои родители до сих пор живы."
    "Периодически мной овладевала уверенность, что всё это время во мне был скрыт гениальный писатель или музыкант. Или хотя бы шахматист.{w} Увы, на сегодняшний момент я еще не выкопал его из зарытого в землю таланта.{w} Зачем я здесь? Чего я хочу?{w} В последние годы я стал склоняться к мысли, что не хочу ничего."
    nvl clear
    window hide

    scene bg semen_room_window 
    with fade

    stop music fadeout 4

    play sound_loop sfx_street_traffic_outside fadein 2

    $ renpy.pause(3)

    window show
    "Я с неохотой подошел к немытому окну, за которым с трудом угадывались очертания соседних хрущевок. Серые сумерки сменились типичным зимним вечером. С неба лениво падали снежинки. Это вдохнуло в меня немного энергии."
    "Такие вечера всегда напоминали мне о детстве. О беззаботном времени, когда ни вопросов, ни проблем не было."
    "Сегодня у меня необычный день. Я был приглашен на встречу моих институтских товарищей, которых я толком и не знал. И я ожидаемо не смог сказать «нет». Меня уговорил один из немногочисленных знакомых - бывший одногруппник. Он хоть и неплохой парень, но все же не сравнится с компьютером."
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
    "На остановке никого не было. Ледяной ветер пронизывал дешёвое пальто, поэтому я спрятался от него под навесом."
    "Снегопад закончился, и я остался один на один с чёрным декабрьским холодом."
    "Автобус запаздывал, и мало-помалу я пришел к пониманию, что зима – не лучшее время года."
    "Не то чтобы я любил лето или осень... Я вообще мало что любил. Даже свой образ жизни, если честно."
    "Переминаясь с ноги на ногу по скрипящему снегу, я закрыл глаза в детской надежде согреться."
    window hide

    $ renpy.pause(3)

    scene anim prolog_2 
    with fade
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Яркое солнце, шелест листвы. Вокруг бегают дети.{w} Мои друзья. Смех, слезы, обида. Всё такое настоящее."
    "Мечты, надежды, цели. Я не хотел стать космонавтом, но я ни на секунду не сомневался, что стану важным.{w} Стану нужным."
    "Стану умным.{w} Красивым.{w} Встречу умницу-красавицу, которая полюбит меня с первого взгляда.{w} Я для неё, она для меня."
    "Я загадывал такие желания каждый день рожденья, когда задувал свечки."
    "Надо ли говорить, что ничего не сбылось?{w} Вспоминать об этом было горько."
   
    nvl clear
    window hide

    play sound sfx_intro_bus_engine_start

    $ renpy.pause(3)

    play sound_loop sfx_intro_bus_engine_loop fadein 3

    $ set_mode_adv()

    scene anim intro_9 
    with fade2

    window show
    "Звук работающего двигателя прервал мой сеанс самоистязания.{w} Вновь поднялась метель после затишья.{w} Сколько я уже прождал? Наверно, как всегда опаздываю."
    "Автобус приехал. Несколько необычный, но ярко освещенная табличка «410» красовалась чуть выше лобового стекла. Мой маршрут."
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

    "Бесконечный поток серых туш и автомобилей и днём, и ночью. Стекло автобуса дрожало от тарахтящего мотора, но мне казалось, что это гул человеческого улья."
    "Потрескивающий радиоприемник наигрывал какую-то старую мелодию, чего раньше никогда не было в городских автобусах, однако в тот момент не обратил внимания на это."
    "Пару минут я гонял в голове несвязные мысли о загнивающем обществе, пока огни рекламных вывесок не принудили меня раздраженно зажмуриться."
    "Мелодия из трескучего приемника будто согревала пустой салон. Я не смог сдержать зевок."
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

    show logo_day :
        pos (400,150)
    with dissolve2

    $ renpy.pause(2, hard=True)

    scene black 
    with dissolve2

    stop music fadeout 5

    $ renpy.pause(5, hard=True)

    jump day1

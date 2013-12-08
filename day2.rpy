init 2:
    $ day2_map_necessary_done = 0
    $ day2_cards_with_sl = 0
    $ day2_dv_bet = 0
    $ day2_un = 0
    $ d2_gave_keys = False
    $ set_name('me',u"Семён")

label v17_day2_main1:

    $ backdrop = 'days'

    $ new_chapter(2, u"День второй")
    $ day_time()

    scene bg black 

    $ renpy.pause(2)

    window show
    "Мне снился сон…"
    "Я медленно плыл в океане пустоты. Совсем один."
    "В ожидании чего-то."
    "Возможно, это была картина всей моей жизни. Пустота и я, ждущий неизвестно чего."
    "И тут я услышал голос. Слишком тихий, чтобы разобрать слова, но такой успокаивающий. Родной."
    "Голос что-то говорил мне.{w} Знакомый голос."
    "Девушка из автобуса!{w} Девушка из моего сна."
    th "Кто она? Чего она хочет?"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_house_of_mt_day 
    with fade2

    window show
    "Я проснулся. Новый день. Новые вопросы без ответов."
    window hide

    play music music_list["my_daily_life"] fadein 5

    with flash

    window show
    "Яркие лучи солнца больно ранили мои заспанные глаза."
    "Я зевнул и с наслаждением потянулся. Будильник на окне показывал почти полдень."
    "Через пару минут бессмысленного наблюдения за ползущей по стене мухой, я неспеша поднялся с кровати."
    "Ко мне мало-помалу возвращалось понимание того, где я нахожусь."
    "Автобус. Мои новые знакомые. Странный лагерь."
    th "Сегодня я намерен раздобыть немного ответов."
    "Оглядевшись, я приметил висящую на спинке моей кровати пионерскую форму."
    "Я с долей брезгливости покрутил ее в руках, но все же решил примерить."
    "Неожиданно, она действительно была мне как раз в пору!"
    "Я недоверчиво заглянул в висящее на шкафу зеркало."

    "..."

    play sound sfx_open_cabinet_2

    window hide

    scene cg d2_mirror :
        pause 0.5
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
    with dissolve

    window show
    "Я несколько опешил."
    "Из зеркала на меня смотрел какой-то мерзкого вида подросток."
    "От моего не по годам изможденного лица не осталось и следа."
    "Куда пропали недельная небритость, мешки под глазами, морщины?!"
    "Похоже, меня не закинули назад во времени или в параллельную реальность, а просто поменяли с кем-то телами."
    th "Получается, я не просто попал в прошлое, но и поменялся телами с кем-то из тогдашних подростков? {w} Если задуматься, я когда-то видел сериал с похожим сюжетом..."
    "Однако чем больше я смотрел на свое новое отражение, тем сильнее я убеждался в том, что это мое тело. Просто несколько моложе."
    "Здесь мне лет шестнадцать."
    th "Господи, как сильно я изменился за это время."
    th "Сейчас я смотрю в глаза совершенно другому человеку."
    th "А я был...симпатичным."
    window hide

    play sound sfx_close_cabinet

    pause(1)

    $ persistent.sprite_time = 'day'
    scene bg int_house_of_mt_day 
    with dissolve

    window show
    "От вида старого себя во мне пробуждались мерзкие воспоминания, которые я пытался забыть навсегда. С отвращением я отошел от зеркала."
    th "Сейчас полдень. Навряд ли я успеваю на завтрак."
    th "Не хотелось бы опять полагаться на Славю..."
    "При воспоминании о ней я невольно улыбнулся. Ко мне редко относились так по-доброму."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "За день снаружи ничего не изменилось. Все такой же нестерпимый зной. По крайней мере, больше не нужно бродить вокруг в зимней одежде. "
    th "Не помню, когда последний раз я чувствовал себя так хорошо."
    "Прикрыв глаза, я несколько минут наслаждался тишиной и покоем этого места."
    "Но тут передо мной появилась Ольга Дмитриевна..."
    show mt normal panama pioneer at center   with dissolve
    mt "Доброе утро, Семен!"
    me "Доброе."
    "Я не чувствовал себя комфортно рядом с ней.{w} Пожалуй, из всех моих знакомых именно к Ольге Дмитриевне у меня было больше всего подозрений."
    mt "У тебя первый день только вчера был, поэтому я тебя будить не стала, но завтрак-то…"
    show mt smile panama pioneer at center   with dspr
    mt "Впрочем, ладно! Вот, держи!"
    "Она протянула мне бумажный сверток."
    "При ближайшем рассмотрении я определил, что это были бутерброды."
    me "Ох...спасибо, Ольга Дмитриевна."
    show mt normal panama pioneer at center   with dspr
    mt "А теперь марш умываться!"
    "Я двинулся было на поиски умывальника, но меня остановил возглас вожатой."
    mt "Ой, сейчас, подожди!."
    hide mt  with dissolve
    window hide

    pause(1)

    window show
    show mt normal panama pioneer at center   with dissolve
    "Забежав в домик, она через пару мгновений вернулась с каким-то пакетиком в руках."
    "Внутри была зубная щетка, мыло, небольшое полотенце и еще какая-то мелочь."
    show mt smile panama pioneer at center   with dspr
    mt "Пионер должен быть всегда чист и опрятен!"
    mt "Дай я тебе галстук правильно завяжу на первый раз, а то он у тебя болтается.{w} Потом научишься, сам будешь!"
    me "Да не надо, я же сейчас умываться пойду. Мешаться будет."
    th "Не думаю, что вообще хочу носить этот чертов галстук. Но сомневаюсь, что это вопрос выбора."
    show mt normal panama pioneer at center   with dspr
    mt "Да, пожалуй…{w} Ладно, тогда потом.{w} И не забудь про линейку."
    th "Вечно забываю, кстати…{w} Как и про карандаш. Вот, помнится, еще в школе...стоп."
    me "Какую линейку?"
    show mt angry panama pioneer at center   with dspr
    mt "Ну как же?!"
    "Она нахмурилась."
    mt "Сегодня ведь понедельник!"
    th "Странно, по моим подсчетам – сегодня должно быть воскресенье…"
    th "Пропажа одного дня - не самая большая проблема в моей ситуации, но...{w} это может пригодиться в дальнейшем."
    show mt normal panama pioneer at center   with dspr
    mt "Обычно у нас линейки рано утром, еще до завтрака, но сегодня, так как понедельник, она будет в 12 часов."
    mt "Не опаздывай!"
    me "Понял. А где линейка-то будет?"
    mt "На площади, где же еще!"
    "Вероятно, этого следовало ожидать."

    stop ambience fadeout 2

    "Я направился в сторону умывальников."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_washstand_day 
    with dissolve

    play music music_list["everyday_theme"] fadein 5

    window show
    "Полагаю, не стоило надеяться на отдельный душ и туалет. Монструозное кафельно-крановое нечто передо мной настраивало на мрачные мысли."
    "Видимо, даже у меня есть определенный уровень комфорта, обходиться без которого я не привык."
    "Выбора у меня особого не было, да и последнее, что стоило делать сейчас - это жаловаться на недостаток удобств."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_washstand2_day 
    with dissolve

    play sound sfx_open_water_sink

    $ renpy.pause(1)

    play sound_loop sfx_water_sink_stream

    window show
    "Я открыл кран.{w} Ледяная вода обжигала лицо и руки."
    "Вопреки моим ожиданием, зубной пасты в пакетике не оказалось. Вместо этого я наткнулся на круглую коробочку с гордой надписью «Зубной порошок»."
    th "И еще одно доказательство, что я сейчас в прошлом."
    "Мои сомнения в этом практически рассеялись. Неясно было лишь одно - что я буду делать, если это действительно так."
    window hide

    stop sound_loop
    play sound sfx_close_water_sink

    $ persistent.sprite_time = 'day'
    scene bg ext_washstand_day 
    with dissolve

    window show
    "Я уже собирался идти назад, но услышал рядом с собой звук чьих-то шагов."
    show sl normal sport at center   with dissolve
    "Передо мной стояла Славя, одетая в отлично сидящий на ней спортивный костюм."
    show sl smile sport at center   with dspr
    sl "Физкульт-привет!"
    me "А, да...доброе утро, Славя."
    "Наличие этой девочки поблизости оказывало явно негативное влияние на мою речь."
    show sl normal sport at center   with dspr
    sl "Почему на завтраке не был?"
    me "Я...э-э...проспал."
    me "Ольга Дмитриевна принесла мне бутерброды."
    show sl smile sport at center   with dspr
    sl "А, ну отлично тогда! Не забудь на линейку прийти!"
    me "Да, конечно."
    sl "Ладно, я побежала, не скучай!"
    hide sl  with dissolve
    "Она помахала мне на прощание и скрылась за поворотом тропинки."
    "Если я действительно хотел попасть на линейку, стоило поспешить."

    stop music fadeout 3

    "Перед линейкой я решил забросить пакет обратно в домик и заодно перекусить бутербродами."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    "Я поспешно распахнул дверь и вбежал внутрь."
    window hide

    if persistent.hentai:
        scene cg d2_mt_undressed 
        with dissolve
    else:
        scene black 
        with dissolve

    play music music_list["awakening_power"] fadein 0

    window show
    "Это было несколько необдуманно – посреди комнаты стояла Ольга Дмитриевна…"
    "И переодевалась!"
    "Я застыл, стараясь не дышать. По моему лицу потекли капли пота, предательски щекоча нос. С надеждой я начал тихо пятиться к двери, как вдруг..."
    if persistent.hentai:
        show cg d2_mt_undressed_2  with dspr
    mt "Семен!"
    "Я поспешно отвернулся."
    mt "Стучаться надо! А теперь выйди!"
    window hide

    stop music fadeout 2

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Красный как рак, я вылетел за дверь."
    th "Да, неудобно получилось. Но какая фигура..."
    "Через минуту показалась Ольга Дмитриевна."
    show mt normal panama pioneer at center   with dissolve
    mt "Вот, держи.{w} Теперь это и твой дом тоже."
    window hide

    play sound sfx_keys_rattle

    $ renpy.pause(1)

    window show
    "Она протянула мне ключ.{w} Задумчиво подержав в ладони, я бросил его в карман."
    th "Дом…"
    th "У человека не так много мест, которые можно назвать домом."
    th "А у меня - особенно."
    "При воспоминании о своем настоящем доме, я испытывал не столько ностальгию, сколько...боль .{w} Действительно ли я хочу туда вернуться?"
    mt "Ладно, пойдем, опаздываем."
    me "А как же бутерброды?.."
    mt "По дороге съешь!"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    window show
    "Мы поспешно шагали вдоль палаток. Я уплетал бутерброды с колбасой, Ольга Дмитриевна без умолку о чем-то говорила."
    "Потеряв нить разговора в самом начале, я решил всецело сосредоточиться на еде."
    show mt normal panama pioneer at center   with dissolve
    mt "Ты меня понял?"
    me "Хм?"
    show mt angry panama pioneer at center   with dspr
    mt "Ты не слушаешь!"
    me "Простите…"
    show mt normal panama pioneer at center   with dspr
    mt "Сегодня начинается твоя новая пионерская жизнь!"
    mt "И ты должен приложить все усилия, чтобы она стала счастливой!"
    me "А, да, конечно…"
    show mt surprise panama pioneer at center   with dspr
    mt "Я серьезно! У пионера много обязанностей, на него возложена большая ответственность – участвовать в общественной работе, помогать младшим, учиться, учиться и еще раз учиться!"
    mt "Мы все тут как одна большая семья.{w} И тебе предстоит стать ее частью."
    th "Необычнайно красивый голос...но какая же она нудная."
    show mt smile panama pioneer at center   with dspr
    mt "Надеюсь, что по окончании смены у тебя останутся самые лучшие воспоминания о нашем лагере."
    mt "Воспоминания на всю жизнь!"
    me "А когда заканчивается смена?"
    show mt normal panama pioneer at center   with dspr
    mt "Что ты постоянно глупые вопросы задаешь?"
    th "Черт. Ожидаемо."
    "Факт есть факт - Ольга Дмитриевна намеренно что-то скрывала от меня."
    th "Вопрос в том - что я буду с этим делать?"
    "Сейчас мой выбор - участие в этой нелепой театральной постановке."
    "Прекрасный лагерь с добрыми обитателями - пока я не заглядываю за картонные декорации."
    mt "Самое главное для тебя – использовать время, которое ты проведешь здесь, с пользой."
    me "Так точно."
    "Ее слова...мне на секунду показалось, что я начинаю что-то понимать.{w} Должно быть, это всего лишь мое воображение."

    stop ambience fadeout 2

    "..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    play music music_list["get_to_know_me_better"] fadein 5

    window show
    "Мы пришли на площадь."
    "Там уже стояли пионеры, выстроившись в шеренгу."
    "Неожиданно, но их было отнюдь не так много, как можно было бы предположить по числу палаток."
    show mt normal panama pioneer at center   with dissolve
    me "А что, еще не все пришли?"
    mt "Да вроде все."
    "Она окинула взглядом пионеров."
    mt "Ладно, иди становись."
    th "Ага...«спальных мест больше нет», да?"
    hide mt  with dissolve
    window hide

    scene cg d2_lineup 
    with dissolve

    window show
    "Вожатая начала рассказывать о недельных мероприятиях. Быстро потеряв интерес, я оглядел присутствующих."
    "В паре человек от меня стоял Электроник, чуть дальше – Лена и Славя, а в самом конце – Ульянка и Алиса."
    th "Мысли путаются. Нужно меньше спать."
    "Ольга Дмитриевна, казалось, заканчивать в ближайшее время не собиралась. Я, пытаясь подавить зевок, лениво шарил глазами по площади."
    th "«Генда»..."
    "Я никак не мог вспомнить ни одного революционера с похожей фамилией."
    th "Вероятно, какой-то местный деятель…"
    sl "О чем мечтаешь?"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    show sl normal pioneer at cright 
    show mt normal panama pioneer at cleft 
    with dissolve

    window show
    "Славя стояла передо мной. Рядом была Ольга Дмитриевна."
    "Я сглотнул. Обе они с ожиданием смотрели на меня."
    mt "Ты запомнил план на неделю?"
    me "Э-э...план, да?{w} Да...э-э...конечно, как я мог забыть план, хе-хе!"
    show mt smile panama pioneer at cleft   with dspr
    mt "Вот и отлично!"
    "Она посмотрела на Славю."
    show mt normal panama pioneer at cleft   with dspr
    mt "Принесла?"
    "Кивнув, Славя протянула мне какой-то листок."
    mt "Это обходной лист. Тут четыре позиции. За сегодня тебе нужно везде побывать."
    mt "Во-первых, записаться в клуб, они у нас в здании кружков и отдельно – музыкальный."
    mt "Во-вторых, зайти в медпункт."
    mt "Ну, и в-третьих – в библиотеку."
    mt "Все понял?"
    me "Да."
    "Лагерь оказался куда больше, чем я вчера предполагал. Возможно, в одном из этих мест я смогу раздобыть информацию."
    mt "Тогда давай, начинай прямо сейчас."
    me "А как же обед?"
    mt "Ничего страшного! Я тебе еще бутербродов принесу. Обходной лист важнее!"
    sl "Удачи тебе."
    hide sl 
    hide mt 
    with dissolve
    "Они ушли так быстро, что я и слова сказать не успел."
    th "Питаться бутербродами, да? Мало-помалу возвращаюсь в привычное русло."
    th "Хотелось бы все же успеть к обеду..."
    th "Обед в час, так что если я все же пойду в столовую - наверняка не успею обойти все места из списка."

    stop music fadeout 3

    th "Ладно, разберемся."
    window hide

    $ disable_all_zones()

    $ set_zone('music_club', 'v17_day2_musclub')
    $ set_zone('clubs', 'v17_day2_clubs')
    $ set_zone('library', 'v17_day2_library')
    $ set_zone('medic_house', 'v17_day2_aidpost')
    $ set_zone('dining_hall', 'v17_day2_dinner')

    jump v17_day2_map

label v17_day2_map:

    if day2_map_necessary_done == 5:
        jump v17_day2_main2
    if day2_map_necessary_done == 2:
        $ reset_zone('dining_hall')
        $ day2_map_necessary_done += 1

    $ show_map()

label v17_day2_musclub:

    play ambience ambience_camp_center_day fadein 3

    $ persistent.sprite_time = 'day'
    scene bg ext_musclub_day 
    with dissolve

    window show
    "Музыкальный клуб располагался в некотором отдалении от основных построек лагеря."
    "Небольшое одноэтажное здание, от которого, ожидаемо, веяло спокойствием и уютом."
    "Не долго думая, я зашел внутрь."
    window hide

    stop ambience fadeout 2
    play sound sfx_open_door_2

    $ renpy.pause(1)

    $ persistent.sprite_time = 'day'
    scene bg int_musclub_day 
    with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    "С удивлением я обнаружил внутри полный набор инструментов – барабаны, гитары, даже рояль."
    "Я решил, что по ним смогу примерно определить год, в котором я оказался, и подошел ближе."
    window hide

    scene cg d2_miku_piano2 
    with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5

    window show
    "При приближении я понял, что под роялем кто-то есть. Открывшийся мне вид надолго отбил у меня желание предпринимать какие-либо действия."
    "Девушка явно что-то сосредоточенно искала и не замечала меня. Спустя некоторое время я нашел в себе силы негромко кашлянуть."
    me "Кхе-км..."
    window hide

    scene cg d2_miku_piano 
    with dissolve

    window show
    mi "Ааа! Кто здесь?"
    window hide

    play sound sfx_piano_head_bump
    with vpunch

    $ renpy.pause(1)

    window show
    "Попытавшись вскочить, она с силой впечаталась в днище рояля."
    mi "Ой!"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_musclub_day 
    with dissolve

    show mi shocked pioneer at center   with dissolve
    window show
    "Стараясь больше не делать резких движений, она выбралась из-под рояля."
    me "Прошу прощения, если отвлекаю..."
    show mi normal pioneer at center   with dspr
    mi "Нет-нет, ничего! Вижу, у тебя обходной. Новенький, верно?"
    me "Да."
    show mi smile pioneer at center   with dspr
    mi "Меня Мику зовут."

    $ meet('mi', u"Мику")

    mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть, не то чтобы строил – он инженер…"
    mi "Разрабатывал! Я бы даже сказала, проектировал! Атомную станцию! Или плотину… Или мост… А может...{w} Но точно что-то большое!"
    "Воспользовавшись паузой, я представился."
    me "Я - Семен."
    show mi happy pioneer at center   with dspr
    mi "Отлично! Не хочешь к нам в клуб вступить? Ну, не совсем к нам...я тут пока одна, но с тобой нас будет уже двое! Ты на чем-нибудь играть умеешь?"
    "Пару лет назад я купил себе гитару и даже по самоучителям выучил пару аккордов, но потом ожидаемо забил на это дело. Слишком много усилий."
    me "Знаешь, я как-то не планировал особо…"
    show mi normal pioneer at center   with dspr
    mi "Да ладно тебе, я тебя научу играть! Хочешь на трубе, например? Или на скрипке? Контрабас? Фортепиано? Сямисэн, может быть? Я на всем умею, честно-честно."
    "Я хотел было что-то вставить, но каждое мое лишнее слово грозило спровоцировать еще одну словесную атаку."
    me "Я...э-э...подумаю, а пока...{w} не могла бы ты подписать?"
    show mi happy pioneer at center   with dspr
    mi "Да-да-да, конечно, давай! Ты заходи в любой день, не стесняйся! Я еще и неплохо пою! Послушаешь, как я пою японские народные песни! Не фанат? Могу что-нибудь из современного!"
    me "Обязательно… А сейчас мне пора, извини."
    show mi shy pioneer at center   with dspr
    mi "Конечно, приходи непременно, я всегда…"
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    $ renpy.pause(1)

    $ persistent.sprite_time = 'day'
    scene bg ext_musclub_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я безжалостно обрезал ее слова, захлопнув дверь клуба."
    "Я не был против снова взяться за гитару, но бесконечный словесный поток Мику меня изматывал."
    show dv normal pioneer close at center    with dissolve
    "Я побрел было дальше, как вдруг столкнулся нос-к-носу с Алисой."
    "Она одарила меня очередным тяжелым взглядом."
    dv "Зачем пришел?"
    me "Обходной…"
    dv "Подписал?"
    me "Да…"
    dv "Ну и катись!"
    hide dv  with dissolve
    "Она вошла внутрь, а я поспешил продолжить свой путь."
    window hide

    stop ambience fadeout 2

    $ disable_current_zone()
    $ day2_map_necessary_done += 1
    jump v17_day2_map

label v17_day2_clubs:

    play ambience ambience_camp_center_day fadein 2

    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day 
    with dissolve

    window show
    "Я пошел к зданию кружков."
    "Никогда не понимал удовольствия от общественной работы. Всегда под любым предлогом открещивался от работы в команде."
    "Меня никогда не интересовали какие-либо секции или кружки, так что сюда я пришел исключительно с целью отметиться."

    stop ambience fadeout 2

    "Не трятя времени, я вошел внутрь."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = 'day'
    scene bg int_clubs_male_day 
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "К моему удивлению, внутри никого не было."
    "В комнате повсюду валялись какие-то провода, микросхемы, прочие запчасти, о назначении которых я лишь догадывался."
    "Из соседнего помещения послышались голоса, и через секунду ко мне вошли два пионера."
    show el normal pioneer at cleft 
    show sh normal pioneer at cright 
    with dissolve
    "В одном я узнал Электроника, второй же мне был незнаком."
    el "Привет, Семен! А мы тебя ждали."
    th "Видимо, об обходном листе знают почти все."
    me "Ждали? Зачем?"
    el "Ну как же, ты ведь пришел в наш клуб кибернетиков записываться, так?"
    "Я хотел было возразить, но Электроник не дал мне ответить."
    show el smile pioneer at cleft   with dspr
    el "Знакомься, это Шурик, он у нас главный!"

    $ meet('sh', u"Шурик")

    me "Кхм. В клубе кроме вас двоих кто-то есть?"
    show el normal pioneer at cleft   with dspr
    el "Ну, можешь считать, что ты."
    "Шурик подошел ко мне и уверенно протянул руку."
    "Его лицо мне показалось смутно знакомым."
    show sh normal_smile pioneer at cright   with dspr
    sh "Добро пожаловать!"
    me "Угу…"
    show sh normal pioneer at cright   with dspr
    el "Давай я тебе тут все покажу!{w} Ты не стесняйся, располагайся."
    me "Да нет, ребята, я вообще-то…"
    show sh normal_smile pioneer at cright   with dspr
    sh "Всегда рады новым членам."
    "Шурик сказал это настолько торжественно, что я невольно проникся собственной важностью. Дело принимало скверный оборот."
    me "Да нет, мне бы просто обходной лист подписать."
    show sh normal_smile pioneer at cright   with dspr
    show el grin pioneer at cleft   with dspr
    el "Так ты к нам запишись, и мы тебе его подпишем."
    "Он хитро улыбнулся."
    "У меня опустились руки. Положение виделось мне безнадежным."
    show el normal pioneer at left 
    show sh normal pioneer at right 
    show sl normal pioneer at center 
    with dissolve
    "Входная дверь распахнулась, и в помещение, подобно ангелу, грациозно вошла Славя."
    sl "А, Семен! Надеюсь, они тут тебя не достают?"
    show sl angry pioneer at center   with dspr
    "Она строго посмотрела на гениев агитаторской работы."
    sl "А то я их знаю – они могут!"
    me "Да, понимаешь, на самом деле мне бы просто обходной подписать…"
    "Я чуть не плакал от счастья."
    show sl normal pioneer at center   with dspr
    sl "Так это не проблема, давай сюда."
    "Она взяла листок и подошла к Шурику."
    sl "Подписывай!"
    show sh upset pioneer at right   with dspr
    sh "Но подожди, мы же еще не закончили…"
    show sl angry pioneer at center   with dspr
    sl "Закончили! Подписывай!"
    "Под ее грозным взглядом Шурик, казалось, уменьшился вдвое."

    stop ambience fadeout 2

    "Он поставил свою закорючку, и я, сбивчиво поблагодарив Славю, поскорее направился дальше."
    window hide

    $ disable_current_zone()
    $ day2_map_necessary_done += 1
    jump v17_day2_map

label v17_day2_library:

    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = 'day'
    scene bg ext_library_day 
    with dissolve

    window show
    "Я не без удовольствия приближался к зданию библиотеки. Мне нравилась тамошняя атмосфера и запах книг."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = 'day'
    scene bg int_library_day 
    with dissolve

    play ambience ambience_library_day fadein 3

    window show
    "При входе меня захлестнули детские воспоминания."
    "Мне лет семь-восемь, я с матерью в библиотеке."
    "Столько новых интересных книг, я не понимаю, почему нельзя забрать их все."
    "Мама смеется и гладит меня по голове. Ее лицо такое молодое и беззаботное. Я, швыркая носом, тщательно выбираю книгу и гордо несу ее к столу библиотекаря..."
    "Как много прошло времени..."
    "В библиотеке, где я сейчас находился, повсюду висели навязчивые плакаты, знамена и прочая советская символика."
    "Книги, к моему огорчению, тоже в основном были соответствующей тематики."
    "Я огорченно вздохнул - творчества Маркса не было в моих планах на прочтение на ближайшие лет десять."
    "Я осмотрелся в поисках библиотекаря. Вскоре я обнаружил ее, спящую на столе неподалеку."
    window hide

    scene cg d2_micu_lib 
    with dissolve

    window show
    "Короткая, почти мальчишечья стрижка. Очки, невероятно подходящие к ее лицу."
    "Она так мило смотрелась спящей, что я не решился разбудить ее."
    th "Не то чтобы я куда-то торопился. Подожду полчасика..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_library_day 
    with dissolve

    window show
    "Просто так сидеть было скучно, и я взял с полки первую попавшуюся книгу."
    "Артур Шопенгауэр, «Мир как воля и представление»."
    "Я наугад раскрыл книгу и начал читать:"
    window hide

    $ set_mode_nvl()

    window show
    nvl clear
    "Жизнь человека с ее бесконечными трудами, нуждой и страданием следует рассматривать как объяснение и парафраз акта зачатия, т.е. решительного утверждения воли к жизни; с этим связано и то, что человек обязан природе смертью и с тоской думает об этом обязательстве."
    "Разве это не свидетельствует о том, что в нашей жизни заключена некая вина?"
    "И тем не менее, периодически расплачиваясь смертью за рождения и смерти, мы всегда существуем и испытываем все горести и радости жизни попеременно, когда ни одна из них не может нас миновать: таков результат утверждения воли к жизни."
    "При этом страх смерти, который, несмотря на все страдания жизни, удерживает нас в ней, становится, в сущности, иллюзией; но столь же иллюзорно и влечение, заманившее нас в жизнь."
    "Объективное выражение этого соблазна можно увидеть в обращенных друг на друга страстных взглядах влюбленных: они есть чистейшее выражение воли к жизни в ее утверждении. Как она здесь кротка и нежна!"
    "Она хочет благополучия, спокойного наслаждения и тихой радости для себя, для других, для всех."
    window hide

    $ set_mode_adv()

    play sound sfx_knock_door2

    window show
    "В дверь постучали."
    "Я машинально закрыл книгу и поставил на место."

    play sound sfx_open_door_clubs_2

    "В дверь вошла Лена."
    show un normal pioneer at cleft   with dissolve
    un "Ой…"
    show un shy pioneer at cleft   with dspr
    me "Привет."
    "Я постарался изобразить дружелюбную улыбку."
    un "Привет, а я вот книжку пришла отдать…"
    "У нее в руках была виденная мной вчера «Унесенные ветром»."
    un "Ой, Женя спит, тогда я попозже зайду…"

    $ meet('mz', u"Женя")

    mz "Уже не сплю."
    show mz normal glasses pioneer far at cright    with dissolve
    "Я оглянулся в сторону библиотекарши."
    "Она сидела за столом и пристально наблюдала за мной."
    show mz angry glasses pioneer far at cright   with dspr
    mz "А тебе чего?"
    me "Мне бы обходной…"
    show mz normal glasses pioneer at cright   with dissolve
    mz "Давай."
    "Она быстро расписалась и протянула мне его обратно."
    "Глядя на нее, было очевидно, что дальнейший разговор будет неуместен."
    "Я поблагодарил Женю и направился к выходу."
    window hide

    stop ambience fadeout 2

    $ disable_current_zone()
    $ day2_map_necessary_done += 1
    jump v17_day2_map

label v17_day2_aidpost:

    $ persistent.sprite_time = 'day'
    scene bg ext_aidpost_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Я не видел особого смысла в посещении медпункта. После моего загадочного омоложения жаловаться на что-либо было бы дурным тоном."
    th "Никогда не любил врачей. Надеюсь, это будет быстро."
    "Я вошел."
    window hide

    stop ambience fadeout 2

    play sound sfx_open_door_1

    $ renpy.pause(1)

    $ persistent.sprite_time = 'day'
    scene bg int_aidpost_day 
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    th "Довольно просторный медпункт, учитывая малочисленность населения лагеря."
    show cs normal stethoscope at center   with dissolve

    play music music_list["eternal_longing"] fadein 5

    "За столом сидела женщина средних лет."
    "Она бросила на меня пристальный, оценивающий взгляд, не прекращая что-то писать."
    cs "Ну, здравствуй… пионер."
    me "Добрый день… Мне бы вот…"
    cs "Ты присаживайся."
    "Я оглядел комнату."
    cs "На кушеточку."
    "Я сел."
    cs "Раздевайся."
    "Все это она говорила совершенно ровным тоном."
    me "Зачем?.."
    cs "Смотреть тебя будем, слушать, здоровье проверять."
    show cs smile stethoscope at center   with dspr
    cs "Меня, кстати, зовут Виолетта, но ты меня можешь звать просто Виолой."

    $ meet('cs', u"Виола")

    "Она повернулась в мою сторону."
    cs "Ну, чего сидишь? Раздевайся."
    me "Да я не жалуюсь ни на что. Мне бы вот…"
    "Я аккуратно протянул ей листок."
    cs "Потом."
    show cs smile at center   with dissolve
    "Она сняла с шеи стетоскоп с таким видом, будто собиралась меня препарировать."
    window hide

    stop music fadeout 3
    play sound sfx_knock_door7_polite

    $ renpy.pause(1)

    window show
    "К моему несказанному облегчению в дверь постучали."
    show cs normal at center   with dspr
    "Виола с видимой неохотой бросила:"
    cs "Входите!"

    play sound sfx_open_door_strong

    "В комнату вбежал Электроник."
    show el fingal pioneer far at left    with dissolve   
    show cs normal at center   with dspr
    el "Здрасьте! Я тут это… На футболе упал. Глупости, конечно, я бы и так, но меня Ольга Дмитриевна…"
    "У Электроника под глазом красовался здоровенный фингал."
    th "Упал на футболе? Глазом?"
    cs "Садись, сейчас посмотрим."
    "Она качнула головой в сторону свободной кушетки."
    show cs normal glasses at center   with dissolve
    cs "А ты давай сюда свой обходной."
    "Медсестра быстро подписала его и продолжила:"
    show cs smile glasses at center   with dspr
    cs "Если что заболит – сразу ко мне… пионер."

    stop ambience fadeout 2

    "Скомканно поблагодарив, я закрыл за собой дверь."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_aidpost_day 
    with dissolve

    window show
    th "Не уверен, что я обо всем этом думаю."
    window hide

    $ disable_current_zone()
    $ day2_map_necessary_done += 1
    jump v17_day2_map

label v17_day2_dinner:

    $ lp_us = (lp_us) + (1)

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Я, чувствуя себя виноватым, все же решил быстренько пообедать."
    th "Не думаю, что это займет много времени."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_day 
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Внутри почти никого не было – похоже, большинство пионеров уже пообедало."
    "Внушающая уважение своими габаритами повариха выдала мне шикарный обед: суп, нежно дразняший нос своим ароматом, какой-то непонятный салат, и сосиски с гречкой."
    "Я сел за ближайший стол и принялся сосредоточенно жевать, наслаждаясь восхитительным вкусом."
    window hide

    play sound sfx_punch_medium
    with vpunch

    play music music_list["eat_some_trouble"] fadein 5

    $ renpy.pause(1)

    window show
    "Моя пищевая медитация продлилась недолго. Многострадальная спина вновь приняла на себя чей-то звонкий удар."
    "Я обернулся и увидел Ульянку."
    show us laugh pioneer at center   with dissolve
    me "Я тебя когда-нибудь удушу!"
    show us laugh2 pioneer at center   with dspr
    us "Не догонишь!"
    "Она показала мне язык."
    show us grin pioneer at center   with dspr
    us "Один раз уже пытался – не догнал же."
    me "Дождешься, я тебя где-нибудь подкараулю!"
    show us surp2 pioneer at center   with dspr
    us "Так нечестно!"
    me "На себя посмотри, честная!"
    show us laugh pioneer at center   with dspr
    us "Ладно, подожди, сейчас обед возьму и подойду, вместе поедим."
    hide us  with dissolve
    "Перспектива была не самой радужной, я с феноменальной скоростью стал заглатывать оставшиеся сосиски."
    "Однако доесть я не успел, Ульянка вернулась буквально через полминуты."
    show us smile pioneer at center   with dspr
    "На ее тарелке лежал огромный кусок жареного мяса и несколько отварных картофелин."
    "Я с тоской посмотрел в свою тарелку."
    me "Это ты как?.. Откуда?.."
    show us laugh2 pioneer at center   with dspr
    us "Уметь надо!"
    "Она посмотрела на меня и широко улыбнулась."
    "Черное чувство зависти мало-помалу овладевало моим сознанием."
    "Постепенно в моей голове начал рождаться коварный план. Целая комбинация, на самом деле."
    me "Представляешь, если Ольга Дмитриевна узнает, что ты воруешь еду?"
    show us surp3 pioneer at center   with dspr
    us "Так я не ворую!"
    "Ее щечки окрасил румянец праведного гнева."
    me "А вот это ты ей будешь рассказывать. Думаешь, поверит?"
    show us surp2 pioneer at center   with dspr
    us "Ты...ты...{w}ты же не собираешься ей меня закладывать?!"
    me "Ну… это зависит от многих обстоятельств."
    show us calml pioneer at center   with dspr
    us "Например?"
    "Она внимательно посмотрела на меня."
    me "Принеси мне булочку. Сладкую."
    show us shy2 pioneer at center   with dspr
    us "Где я тебе ее возьму?"
    me "Там же, где взяла это."
    "Я показал на ее тарелку."
    "Ульянка замялась."
    show us dontlike pioneer at center   with dspr
    us "Ладно. Но только одну!"
    show us surp2 pioneer at center   with dspr
    us "И обещай, что после этого не расскажешь Ольге Дмитриевне!"
    me "Слово пионера."
    hide us  with dissolve
    "Она убежала в сторону буфета, а я, недолго думая, взял перечницу и, открутив крышку, со злорадной улыбкой высыпал все содержимое ей в компот."
    "Вскоре с булкой в руках вернулась Ульяна."
    show us laugh pioneer at center   with dissolve
    me "Держи, вымогатель!"
    th "Ульяна, это моя победа!"
    me "А теперь давай кто быстрее выпьет компот!"
    show us surp2 pioneer at center   with dspr
    us "Что еще за глупости!"
    me "Почему глупости? Я выиграю, вот увидишь!"
    show us dontlike pioneer at center   with dspr
    us "Не буду я с тобой в детские игры играть."
    me "У-у...ты просто боишься проиграть. Ладно, я тебя не виню..."
    "Я ехидно улыбнулся."
    show us angry pioneer at center   with dspr
    us "Ах так! Ладно! Раз, два, три!"
    "Она не дала мне времени даже взять чашку, а сама моментально, одним глотком, выпила весь свой компот."
    window hide

    show bg int_dining_hall_day :
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat 10
    stop music fadeout 0

    show us fear pioneer at center   with dspr

    play sound sfx_angry_ulyana

    with flash_red

    $ renpy.pause(5)

    window show
    "Через секунду у нее на лице появилось выражение первобытного ужаса, щеки покраснели, а глаза, казалось, готовы были вылезти из орбит."
    hide us  with dissolve
    "Она вскочила и побежала в сторону чайников с водой, яростно выкрикивая:"
    us "Ты! Ты! Ты…"

    stop ambience fadeout 2

    "Победно смахнув со щеки хлебные крошки, я вышел из столовой, на ходу дожевывая булочку."
    window hide

    $ disable_current_zone()
    jump v17_day2_map

label v17_day2_main2:

    scene black 
    with dissolve2

    window show
    "..."
    "Подписи собраны, надо было зайти к Ольге Дмитриевне, чтобы отдать листок."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show mt normal panama pioneer far at center    with dissolve
    window show
    "Вожатая сидела в шезлонге возле домика и читала книгу."
    "Я без особого удивления отметил, что сама она не особо соответствует пропагандируемому ей образу идеального пионера."
    "Не похоже, что у нее много обязанностей в этом лагере."
    show mt normal panama pioneer at center   with dissolve
    me "Вот…"
    "Я протянул ей обходной."
    "Она, не читая, сунула его в карман."
    th "Весь день моих превозмоганий!..{w} Насмарку..."
    show mt smile panama pioneer at center   with dspr
    mt "Молодец! Ну как, познакомился с нашей медсестрой?"
    me "Да…"
    "При воспоминании о ней я невольно вздрогнул."
    show mt normal panama pioneer at center   with dspr
    mt "В какой кружок записался?"
    me "Да пока ни в какой… Я...э-э...еще думаю..."
    show mt surprise panama pioneer at center   with dspr
    mt "Ну, что же ты так! Завтра обязательно запишись куда-нибудь!"
    th "Меня ожидает трудный день..."
    show mt normal panama pioneer at center   with dspr
    mt "Ладно, пора уже и на ужин идти."
    th "Золотые слова."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Вместе с Ольгой Дмитриевной мы направились к столовой."
    "Солнце постепенно склонялось к горизонту."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_near_day 
    with dissolve

    show dv normal pioneer at fright 
    show el normal pioneer at fleft 
    with dissolve
    window show
    "На крыльце уже стояло несколько человек: Алиса, Электроник..."
    show us normal pioneer at cleft 
    show sl normal pioneer at cright 
    with dissolve
    "Ульяна, Славя."
    show dv angry pioneer at fright   with dspr
    show el surprise pioneer at fleft   with dspr

    play music music_list["always_ready"] fadein 5

    "Когда мы подошли, я услышал, о чем они говорят:"
    dv "Не будешь за базаром следить - еще огребешь!"
    el "Да не говорил я ничего! Тебе показалось!"
    show us grin pioneer at cleft   with dspr
    us "Говорил-говорил, я все слышала!"
    show el angry pioneer at fleft   with dspr
    show sl normal pioneer at cright  behind el  with dspr
    el "Да тебя вообще там не было!"
    us "А вот и была! Я в кустах сидела!"
    hide us  with dissolve
    show sl angry pioneer at cright   with dspr
    show el angry pioneer at fleft  behind sl  with dspr
    sl "Хватит вам! Прекратите!"
    th "Футбол, да?"
    show mt normal pioneer at center   with dissolve
    "Ольга Дмитриевна подошла к ним и попыталась выяснить, что происходит:"
    mt "Что вы тут ругаетесь?"
    sl "Алиса Сыроежкину в глаз…"
    dv "Ничего я не делала!"
    hide dv  with dissolve
    "Алиса обиженно фыркнула и зашла внутрь."

    stop music fadeout 3

    mt "Ладно, пора ужинать уже."
    hide mt 
    hide el 
    hide sl 
    with dissolve
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Войдя последним, я огляделся."
    "Похоже, свободных мест осталось не так много."
    "Вдалеке виднелось несколько свободных стульев рядом с Алисой, но лучше поголодать недельку, чем рискнуть сесть рядом."
    "Также свободно было рядом с Ульяной, но я не был сторонником китайской кухни."
    "И, наконец, свободный стул был рядом с Мику."
    "Если выбирать из трех зол…"
    me "Не возражаешь, если я здесь присяду?"
    show mi normal pioneer at center   with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5

    mi "Ой, да, конечно! То есть нет, не возражаю! То есть да, садись конечно!"
    "Я сел."
    show mi smile pioneer at center   with dspr
    mi "Смотри, сегодня опять гречка. Ты любишь гречку? И вареная курица! Я вообще курицу не люблю. Ну, то есть не то что не люблю..."
    mi "Но если бы меня спросили, что бы мне больше всего хотелось, то бефстроганов или рагу… Нет, может быть, просто котлета! Или ромштекс! Ты любишь ромштексы?"
    me "Я не особо привередливый."
    "И это была сущая правда."
    mi "Вот как. Но вот десерты, знаешь, мне здесь не очень нравятся. Я мороженое люблю! Ты любишь мороженое? Такая вкуснятина! Особенно пломбир «48 копеек», но и «Ленинградское» тоже. Ой, прости, я все о себе!"
    mi "Может, ты больше эскимо любишь?"
    "Я едва слышно застонал."
    th "Не могу же я просто игнорировать ее? Обидится еще..."
    show mi upset pioneer at center   with dspr
    mi "Знаешь, я однажды купила вафельный рожок, начала есть, а там внутри шуруп! Представляешь? Настоящий такой шуруп! Или болт… Я, честно говоря, в них не разбираюсь! Хотя мой папа - инженер! Или это не связано..."
    show mi normal pioneer at center   with dspr
    mi "Шурупами закручивают гайки, а болты – отверткой, верно? Или я что-то путаю...Скажи, у тебя так когда-нибудь бывало - правильный ответ вертится на языке, но ты никак не можешь его поймать, как будто..."
    th "Мне кажется, я уже наелся."
    me "Ладно, я пойду. Приятного аппетита."
    "Я чуть ли не бегом направился к выходу из столовой."
    hide mi  with dissolve

    stop music fadeout 3

    stop ambience fadeout 2

    "Вслед мне неслись ее размышления о предназначении шурупов."
    window hide

    $ sunset_time()

    $ persistent.sprite_time = 'sunset'
    scene bg ext_dining_hall_near_sunset 
    with dissolve2

    play ambience ambience_camp_center_evening fadein 3

    window show
    "Выйдя из столовой, я присел на крыльце, наслаждаясь вечерней тишиной лагеря."
    "В городе постоянный шум не смолкал ни днем, ни ночью. Здесь же все было по-другому."
    "Ночной лагерь было словно другим миром. Миром, в котором существовали лишь я и негромкий треск сверчков."
    "Я жадно вдохнул сладкий вечерний воздух. Кто я? Чего я хочу?{w} Эти вопросы значили здесь так мало."
    "Не думать ни о чем. Просто сидеть и наслаждаться жизнью. Так легко."
    "..."
    window hide

    play sound sfx_pat_shoulder_hard

    $ renpy.pause(1)

    window show
    "Кто-то осторожно похлопал меня по плечу."

    play music music_list["lightness"] fadein 5

    "Я обернулся."
    show el normal pioneer at left   with dissolve
    "Это был Электроник."
    el "Пойдем в карты играть!"
    me "В карты?"
    el "Да! Я игру новую придумал. Интерееесную!"
    me "Хм, и какую же?"
    el "Ну, надо сначала карты найти, потом расскажу."
    me "Ну ладно, позовешь, когда найдешь."
    show el upset pioneer at left   with dspr
    el "Они есть только у Ольги Дмитриевны, а она мне не даст…"
    me "Почему?"
    el "Ну, в прошлый раз…"
    "На крыльцо вышли Ольга Дмитриевна и Славя."
    show el normal pioneer at left 
    show mt normal pioneer at center 
    show sl normal pioneer at right 
    with dissolve
    el "Ольга Дмитриевна! А Семен хотел как раз у вас карты попросить!"
    me "Нет, на самом деле..."
    mt "Зачем?"
    show el smile pioneer at left   with dspr
    el "Мы игру новую придумали!"
    th "Гадкий расчетливый засранец."
    show mt surprise pioneer at center   with dspr
    mt "Что за игра?"
    el "Будут карты – я покажу."
    show mt sad pioneer at center   with dspr
    mt "Ох, не нравится мне эта идея…{w} Но раз и Семен за, то, наверное, ничего страшного…"
    me "Да я вообще-то…"
    show sl smile pioneer at right   with dspr
    sl "Давайте я с ним схожу принесу!"
    window hide

    menu:
        "Пойти за картами со Славей":
            $ day2_cards_with_sl = 1
            $ lp_sl = (lp_sl) + (1)
            jump v17_day2_cards_with_sl
        "Пойти одному":
            jump v17_day2_cards_without_sl

label v17_day2_cards_with_sl:

    window show
    "Я не смог сдержать довольную улыбку."
    me "Ну, если ты не против…"

    stop ambience fadeout 2

    sl "Конечно! Пошли."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg ext_houses_sunset 
    with dissolve

    window show
    "Мы направились к домику вожатой, но, проходя мимо палаток, Славя вдруг остановилась."
    show sl normal pioneer at center   with dspr
    sl "Ой, я забыла! Карты у меня в домике!"
    me "Далеко?"
    show sl smile pioneer at center   with dspr
    sl "Да тут рядом, пойдем!"
    "..."
    window hide

    with fade

    window show
    "Мы подошли к небольшому домику, не отличимому от  пары соседних."
    show sl normal pioneer at center   with dspr
    sl "Подожди тут минутку, я сейчас!"
    hide sl  with dissolve
    show sl normal pioneer at center   with dissolve
    sl "Вот!"
    "Славя показала мне довольно потрепанную колоду карт."
    sl "Пойдем?"
    me "Ладно."
    hide sl  with dissolve
    "..."
    window hide

    with fade

    window show
    "На обратном пути я поймал себя на мысли, что так и не получил за весь день ни одного ответа:"
    show sl normal pioneer at center   with dissolve
    me "А ты давно приехала?"
    sl "Ну, уже неделю здесь."
    me "Понятно… А сама откуда?"
    sl "Я с севера."
    me "А поточнее?"
    show sl smile pioneer at center   with dspr
    sl "Холодного севера."
    "Она посмотрела на меня и улыбнулась."
    th "Это безнадежно. Никто в этом лагере не ответит мне что-либо, способное дать хоть малую толику информации.{w} Значит ли это, что они все здесь заодно?"
    "Я решил зайти с другой стороны."
    me "А что тебе нравится?"
    sl "В смысле?"
    me "Ну, чем ты увлекаешься?"
    show sl smile2 pioneer at center   with dspr
    sl "Ааа… Я природу люблю."
    th "Странно. Не сказал бы, что ей свойственна такая немногословность."
    me "Природу?.. Ясно.{w} Хочешь стать натуралистом?"
    sl "Скорее краеведом. Всегда интересовалась историей родной страны."
    th "Это на нее похоже."
    
    th "Есть ли вероятность, что она действительно оказалась здесь неделю назад? Подобно мне?"
    "Я решил прощупать почву:"
    me "А почему ты именно в этот лагерь поехала?"
    show sl normal pioneer at center   with dspr
    sl "Родителям путевку на работе дали."
    th "Опять облом."
    me "Ну а если бы, предположим, у тебя был выбор?"
    sl "Здесь хорошо.{w} Не думаю, что выбрала бы какое-нибудь другое место – здесь ты будто становишься другим человеком!"
    "Я не мог не отметить правдивость ее слов, но...имела ли она в виду то же, что и я?"
    me "Другим? Что ты имеешь в виду?"
    sl "Ну, столько возможностей, столькому можно научиться, стольких людей узнать!"
    "Это были слова, которые я слышал от Ольги Дмитриевны. Меня это насторожило."

    stop music fadeout 3

    "Я решил до поры прекратить расспросы."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg ext_dining_hall_near_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show sl normal pioneer at cleft 
    show mt normal pioneer at cright 
    with dissolve
    window show
    "Когда мы вернулись, Ольга Дмитриевна сказала Славе:"
    mt "Славя, карты-то остались у тебя!"
    sl "Да ничего, мы принесли."
    show mt smile pioneer at cright   with dspr
    mt "Ну и отлично!"

    jump v17_day2_pre_cards

label v17_day2_cards_without_sl:

    window show
    show sl normal pioneer at right   with dspr
    me "Да ладно, я и один могу сходить…"
    show mt normal pioneer at center   with dspr
    mt "Хорошо. Возьмешь у меня в домике в ящике стола."

    stop ambience fadeout 2

    stop music fadeout 3

    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg ext_houses_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "Да чем я вообще занимаюсь?"
    th "Впрочем, других идей у меня все равно не было."
    th "Может, хоть развлекусь немного."
    "Я отдавал себе отчет в том, что сейчас играть в карты - это последнее, что мне следовало делать. Но я попросту не мог найти альтернативу."
    th "Никто в лагере добровольно говорить мне ничего не собирается. Возможно, ждать и держать глаза открытыми - наилучший выбор на этот момент."
    th "Рано или поздно кто-нибудь проговорится. Или я наткнусь на ответы сам."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = 'sunset'
    scene bg int_house_of_mt_sunset 
    with dissolve

    play ambience ambience_int_cabin_evening fadein 2

    window show
    "Я открыл дверь своим ключом и зашел."
    "К моему удивлению, карт в ящике стола не оказалось."
    "Я перерыл все – столовые приборы, тарелки, клейкая лента, ножницы, пара садовых перчаток, моток веревки, несколько целлофановых пакетов, карандаш и пара сломанных ручек…"
    "Но карт не было."
    "Я решил посмотреть в шкафу."
    "Там в основном была женская одежда, но мое внимание привлек маленький ящичек с замочной скважиной."
    "Я потянул, но он не открылся."
    th "Шанс! Но навряд ли я смогу его открыть. Может, как-нибудь потом..."
    "Взламывать его было явно не лучшей идей, да и карт там, очевидно, не было."

    if d1_keys:
        $ d2_gave_keys = True
        "Я уже собирался уходить и даже сделал несколько шагов, как в кармане что-то зазвенело."
        "Я совсем забыл отдать Славе ключи!"
        th "Сомнительно, но попробывать стоит."
        "Воровато оглядевшись, я подошел к шкафу и начал прикидывать, какой ключ может подойти к замку."
        th "С какой стати у Слави будет ключ от личного ящика Ольги Дмитриевны..."
        "Но к моему удивлению, замок приветливо провернулся несколько раз, и я уже собирался потянуть на себя ручку..."
        window hide

        play sound sfx_open_door_kick

        $ renpy.pause(1)

        window show
        "Как вдруг сзади хлопнула дверь."
        "Я вскочил, готовясь к худшему, но, к моему облегчению, в домике никого не было."
        th "Ветер?{w} Или..."
        "Я с опаской выглянул на улицу, но и там не увидел ничего необычного."
        "Смертельный страх обуревал меня при мысли, что кто-то из местных меня заметил. Мое сердце стремительно стучало."
        window hide

        with fade2

        window show
        "После тщательного осмотра соседних кустов я кое-как успокоился и уже собирался закончить начатое..."
        sl "Семен, ты все еще здесь?"
        show sl normal pioneer at center   with dissolve
        me "А... я... да..."
        "Трясущимися руками я старался побыстрее закрыть ящик и вынуть ключ."
        "Славя подошла ближе."
        show sl smile pioneer at center   with dspr
        sl "Ой, мои ключи! А я их обыскалась! Где ты..."
        me "Да вот, по дороге... В кустах валялись..."
        "Я лихорадочно пытался скрыть проступивший пот. Оставалось лишь надеяться, что она ничего не заметила."
        me "Ну...э-э...пойдем?"
        "Моей единственной мыслью было - поскорее убраться отсюда."
        window hide

    else:
        window hide

    stop ambience fadeout 2        

    $ persistent.sprite_time = 'sunset'
    scene bg ext_dining_hall_near_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show mt normal pioneer at right 
    show sl normal pioneer at left 
    with dissolve
    window show
    "Когда я вернулся к столовой, Ольга Дмитриевна с невозмутимым видом сказала:"
    mt "Ой, извини, карты были у Слави в палатке.{w} Она сбегала, пока тебя не было."
    show sl smile2 pioneer at left   with dspr
    "Я посмотрел на Славю, она виновато улыбнулась."
    th "Эх, если бы я только мог заглянуть внутрь ящика..."

    jump v17_day2_pre_cards

label v17_day2_pre_cards:

    hide mt 
    hide sl 
    with dissolve
    "Славя и Ольга Дмитриевна зашли внутрь."
    "Я уже собирался последовать за ними, как вдруг меня кто-то резко дернул за руку."
    show dv normal pioneer at center   with dspr

    stop ambience fadeout 2

    play music music_list["you_won_t_let_me_down"] fadein 5

    "Это была Алиса."
    me "Тебе что-то надо?"
    "Я с осторожностью посмотрел на нее."
    dv "Что, тоже планируешь участвовать в этой дурацкой игре?"
    me "Ну... да, а что такого?"
    dv "Да нет, ничего."
    show dv smile pioneer at center with dspr:
        linear 0.5 xalign 0.72
    "Она уже собиралась уходить, но вдруг обернулась и внимательно посмотрела на меня, ухмыльнувшись."
    show dv smile pioneer at right:
        linear 0.5 xalign 0.5
    dv "А в карты-то играть умеешь?"
    me "Ну-у...немного умею."
    "Я никак не мог понять, к чему она клонит."
    dv "В дурака небось и все?"
    th "Вот ведь прикопалась."
    me "Ну, в принципе, да..."
    show dv normal pioneer at center   with dspr
    dv "Значит, тут ты без шансов."
    me "Почему?"
    show dv angry pioneer at center   with dspr
    dv "По кочану!"
    me "То есть, ты знаешь правила?"
    show dv smile pioneer at center   with dspr
    dv "А то!"
    me "Ну, э-э, повезло тебе."
    "Я не видел смысла в этом разговоре и сделал несколько шагов по направлению к двери."
    show dv angry pioneer at center   with dspr
    dv "Че ты все уйти-то пытаешься?!"
    th "Да что ей нужно?!"
    show dv smile pioneer at center   with dspr
    dv "Давай поспорим."
    me "Ты про что?"
    show dv normal pioneer at center   with dspr
    dv "Какой же ты тупой!{w} Про карты, про что же еще!"
    me "И в чем спор?"
    show dv smile pioneer at center   with dspr
    dv "Что я тебя обыграю!"
    me "Ну, это весьма вероятно."
    "У меня не было проблем с трезвой оценкой своих способностей. Да и спор с этой девочкой мало интересовал меня."
    show dv normal pioneer at center   with dspr
    dv "Значит, боишься?"
    me "Значит, боюсь...{w} Нет смысла в споре, если не уверен в победе."
    me "Ну я пошел..."
    show dv angry pioneer at center   with dspr
    dv "Нет уж!"
    me "Ну что еще?"
    "Я утомленно вздохнул. Неужели ей настолько нечем заняться?"
    show dv grin pioneer at center   with dspr
    dv "Если не согласишься спорить, я всем расскажу, что ты ко мне приставал!"
    me "Что?!"
    dv "Что слышал!"
    th "Она может..."
    me "Но это же глупо!{w} Тебе никто не поверит! Я же...я..."
    show dv normal pioneer at center   with dspr
    dv "Хочешь проверить?"
    me "Ну, хорошо, допустим...{w} И что будет, если я выиграю?"
    show dv smile pioneer at center   with dspr
    dv "Я никому ничего не скажу."
    me "А если проиграю?"
    show dv normal pioneer at center   with dspr
    dv "Какой же ты тупой!{w} Расскажу, что ты ко мне приставал, говорила же уже."
    me "Выбора у меня мало, как и смысла в этом споре."
    dv "Считай как хочешь."
    th "Глупо соглашаться - я не знаю правил, да и в картах никогда не блистал. Но если ей поверят..."
    th "Черт, как же все это глупо!"
    dv "Так что решил?"
    show un normal pioneer at right   with dissolve
    "Я уже было собирался ответить, как у меня из-за спины бесшумно вынырнула Лена."
    show dv angry pioneer at center   with dspr
    dv "Чего тебе?"
    show un scared pioneer at right   with dspr
    un "Ничего..."
    hide un  with dissolve
    "Лена поспешно забежала в столовую."
    show dv normal pioneer at center   with dspr
    dv "Ну?"
    window hide

    menu:
        "Поспорить с Алисой":
            $ day2_dv_bet = 1
            $ lp_dv = (lp_dv) + (2)
            $ lp_un = (lp_un) - (1)
            window show
        "Не спорить с Алисой":
            $ day2_dv_bet = 0
            $ lp_dv = (lp_dv) - (2)
            $ lp_un = (lp_un) + (1)
            window show

    if day2_dv_bet == 1:
        th "Спор так спор."
        me "Ладно, идет!"
        show dv smile pioneer at center   with dspr
        "Она улыбнулась."
        me "Помни, если я выиграю..."
        dv "Да-да, все честно, без обмана!"
        "Алиса поднялась по лестнице и вошла внутрь."
        hide dv  with dissolve
        th "Лишние проблемы на мою голову..."
    else:
        th "Да пусть говорит, что хочет. Мне наплевать."
        me "Нет...я не буду с тобой спорить."
        show dv angry pioneer at center   with dspr
        dv "Слабак!"
        "Она презрительно фыркнула, и двинулась к двери. Обернувшись, она бросила мне:"
        dv "Готовься к последствиям!"
        th "Лишние проблемы на мою голову..."
        hide dv  with dissolve

    stop music fadeout 3

    "Я тяжело вздохнул и направился за ней в столовую."
    window hide

label v17_day2_cards:

    $ persistent.sprite_time = 'sunset'
    scene bg int_dining_hall_sunset 
    with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    window show
    "Внутри все уже было готово."
    "Тут и там толпились пионеры, весело разговаривая о своем."
    "Часть помещения освободили для игроков и зрителей."
    "В дальнем углу вокруг одного из столов что-то происходило."
    "Подойдя ближе, я увидел большой лист ватмана с какой-то схемой."
    window hide

    show cg lvl_1  with dissolve

    window show
    "В списке участников обнаружилось и мое имя."
    me "Эй, и кто придумал такое распределение?"
    "Я толкнул стоящего рядом Электроника."
    el "Конечно же ваш покорный слуга!"
    "Он отвесил мне картинный поклон, даже не стараясь скрыть самодовольную улыбку."
    "Я разочарованно вздохнул."
    window hide

    hide cg lvl_1  with dissolve

    show el normal pioneer at center   with dissolve
    window show
    me "А призы какие-нибудь будут?"
    "Не то, чтобы меня действительно это интересовало."
    show us grin pioneer at left   with dissolve
    "Электроник только открыл рот, чтобы ответить, как откуда-то прибежала Ульяна и радостно начала прыгать вокруг него, выкрикивая:"
    us "Призы-призы!"
    show us grin pioneer at right   with dspr
    us "Я что-то слышала про призы!"
    me "Знаешь, какой главный принцип Олимпийских игр?"
    show us laugh pioneer at right   with dspr
    us "Нет, какой?"
    me "Вот вырастешь – узнаешь!"
    show us dontlike pioneer at left   with dspr
    "Она надула губки и обратилась к Электронику:"
    us "Так призы будут?"
    show el surprise pioneer at center   with dspr
    el "Ну... Я не знаю.{w} Не от меня это зависит."
    "Он обреченно развел руками."
    hide us  with dissolve
    "Ульянка, очевидно, уставшая от долгого пребывания на одном месте, куда-то убежала."
    me "Ну так что, правила объяснишь?"
    show el normal pioneer at center   with dspr
    el "Всему свое время!{w} Еще не все собрались."
    "Я окинул столовую взглядом и сразу же заметил Алису, Славю, Лену, Мику и Шурика."
    me "Вроде бы все..."
    show el surprise pioneer at center   with dspr
    el "Как же! Жени нет!"
    "Мне показалось, что он сказал это несколько взволнованным тоном."
    me "А она вообще придет?"
    me "Поставь вместо нее кого-нибудь другого."
    el "Нельзя..."
    "Растягивая каждую букву, ответил он."
    "Я не стал уточнять, почему именно нельзя."
    me "Может, тогда сходишь за ней?"
    show el normal pioneer at center   with dspr
    with None
    show mt normal pioneer at right   with dspr
    with dissolve
    mt "Не надо ему никуда ходить – он организатор, ему не положено!"
    "Словно из-под земли рядом с нами возникла вожатая."
    show el upset pioneer at center   with dspr
    el "Но Ольга Дмитриевна!"
    "Взмолился Электроник."
    show mt smile pioneer at right   with dspr
    mt "Семен сходит.{w} Так, Семен?"
    "Она посмотрела на меня и улыбнулась."
    th "Да с какой стати я...черт с ним, полагаю, сегодня вечером от меня ничего не зависит."
    me "И где мне ее искать?"
    show mt normal pioneer at right   with dspr
    mt "Наверное, в библиотеке."
    me "Иду..."
    "Протянул я и направился в сторону выхода из столовой."
    hide el 
    hide mt 
    with dissolve
    el "Только быстрее!"

    stop ambience fadeout 3

    "Донесся мне вслед крик Электроника."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg ext_dining_hall_away_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "Скоро и ночь уже."
    "Я медленно, насколько это возможно, побрел в сторону библиотеки."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg ext_square_sunset 
    with dissolve

    play music music_list["your_bright_side"] fadein 5

    window show
    "Проходя по площади, я заметил кого-то на лавочке."
    th "Да это же Женя!"
    show mz normal glasses pioneer at center   with dissolve
    me "Ты ведь в курсе, что тебя все ждут в столовой?"
    show mz angry glasses pioneer at center   with dspr
    mz "Допустим. И что?"
    "Она нахмурилась, но говорила скорее не сердито, а...смущенно?"
    show mz normal glasses pioneer at center   with dspr
    mz "Я не пойду."
    "Женя отвернулась от меня."
    me "Почему?"
    mz "Не хочу и все!"
    "Я присел рядом. Не то, чтобы мне было дело до того, пойдет она или нет."
    me "Они все ждут только тебя. Нехорошо будет, если ты не придешь."
    show mz bukal glasses pioneer at center   with dspr
    "Женя удивленно посмотрела на меня."
    mz "Только меня?"
    me "Да."
    show mz angry glasses pioneer at center   with dspr
    mz "Все равно нет!"
    "Она нахмурилась и снова отвернулась."
    me "А, делай, как знаешь!"
    "Я раздраженно вскочил со скамейки, и уже собирался уходить, как меня остановил ее смущенный шепот:"
    show mz shy glasses pioneer at center   with dspr
    mz "Я не умею играть в карты..."
    me "Ну...я тоже."
    show mz normal glasses pioneer at center   with dspr
    mz "Ну и как тогда играть?"
    me "Что мешает научиться в процессе?"
    show mz bukal glasses pioneer at center   with dspr
    mz "Готовым следует быть заранее!"
    "Она удивленно посмотрела на меня."
    me "Отнюдь не ко всему в жизни можно заранее подготовиться. Вот представь, попадаешь ты внезапно в Антарктиду...{w} ну, скажем, охотиться на белых медведей..."
    show mz smile glasses pioneer at center   with dspr
    mz "Белые медведи не живут в Антарктиде."
    "Женя улыбнулась."
    me "Не притворяйся, ты меня поняла!"
    me "В конце концов, не на корову же играем. Пойдем?"
    "Она задумалась и внимательно посмотрела на меня."
    show mz normal glasses pioneer at center   with dspr
    mz "Просто не хочу подводить ребят."
    me "Да-да."
    show mz angry glasses pioneer at center   with dspr
    mz "И не подумай ничего такого!"
    "Я даже и не знал, что она имела в виду."

    stop music fadeout 3

    stop ambience fadeout 2

    "Видимо, у любого человека есть свои слабые места."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg int_dining_hall_sunset 
    with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    window show
    "Через минуту мы уже стояли в столовой."
    show el normal pioneer at center   with dissolve
    "Электроник важно выступил вперед."
    el "Итак..."
    "Прокашлялся он."
    el "Каждый тур состоит из одной игры."
    el "Если будет ничья, то исход решит дополнительная партия."
    el "После этого проигравший выбывает, и начинается следующий тур."
    el "Поскольку добровольцев..."
    "Он с опаской покосился на меня."
    el "Поскольку участников – восемь, то туров будет три."
    el "Все понятно?"
    "Толпа пионеров весело загалдела."
    show us laugh pioneer at left   with dissolve
    us "А призы какие, призы?"
    show sl angry pioneer at right   with dissolve
    sl "Ульяна, хватит!"
    "Вперед выскочила Славя, тщетно пытаясь поймать Ульянку."
    show us laugh pioneer at right 
    show sl angry pioneer at left 
    with dissolve
    us "Пока не выиграю приз, не успокоюсь!"
    show us laugh pioneer at left 
    show sl angry pioneer at right 
    with dissolve
    us "Призы-призы!"
    "Как заведенная кричала Ульяна."
    sl "Прекрати."
    "Уговаривала ее выдохшаяся Славя."
    show el shocked pioneer at center   with dspr
    "Электроник, очевидно, не был готов к такому повороту событий."
    show us laugh pioneer at right 
    show sl angry pioneer at left 
    with dissolve
    me "Давайте начинать."
    "Я уже начинал уставать от всей этой затеи. Строго посмотрев на Ульяну, я добавил:"
    me "А то никаких призов не получишь."
    "Подействовало или нет мое увещевание, но все же она вернулась на свое место."
    hide us  with dissolve
    show sl smile pioneer at left   with dspr
    "За ней последовала и Славя, бросив мне на прощание улыбку благодарности."
    hide sl  with dissolve
    show el normal pioneer at center   with dspr
    "Электроник облегченно вздохнул."
    hide el  with dissolve
    "Я подошел к столу, где сидела Лена."
    show un normal pioneer at center   with dissolve
    me "Все в порядке?"
    "Она подняла на меня глаза и покраснела."
    show un shy pioneer at center   with dspr
    me "Не волнуйся, я плохо играю в карты."
    "Я присел напротив нее, неловко стараясь отвести взгляд от ее лица."
    me "Ну что, значит, первый тур мы с тобой играем."
    un "Да."
    "Некоторое время мы просидели в неловком молчании."

label v17_day2_cardgame:

    "Вскоре Электроник начал объяснять правила."

label v17_demo_play:
    python:
        dialogs = {
                        (3, 'rival_select', 'call'):'v17_demo_play_intro', 
                        (3, 'me_defend_1', 'call'):'v17_demo_play_me_defend_1', 
                        (3, 'me_select_1', 'call'):'v17_demo_play_me_select_1', 
                        (3, 'rival_defend', 'call'):'v17_demo_play_rival_defend', 
                        (2, 'rival_select', 'jump'):'v17_demo_play_after_loop'
                    }
        INVISIBLE = False
        VISIBLE = False
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalUn(un_avatar_set, u"Пробная игра")
    jump cards_gameloop

label v17_demo_play_intro:
    show el normal pioneer at center   with dissolve
    $ show_cards()
    el "Посмотрите на карты внимательно."
    $ show_cards()
    el "Перед вами их ровно шесть!"
    $ show_cards()
    th "Невероятно, на факт."
    $ show_cards()
    el "Теперь вы можете их открыть."

    $ VISIBLE = True
    $ show_cards()
    "Наконец, когда все посмотрели свои карты, Электроник продолжил объяснять."
    $ show_cards()
    el "Правила такие же, как в покере."
    $ show_cards()
    el "Думаю, все играть умеют?"
    $ show_cards()
    "Пожалуй, тут мне повезло. Я умел играть в покер."
    $ show_cards()
    el "Сначала идет самая старшая карта, потом пара, потом две пары, потом тройка...{w} Ну и так далее."
    $ show_cards()
    el "Первым ходом вы выбираете карту, которую хотите забрать у противника."
    $ show_cards()
    el "У него же, в свою очередь, есть две попытки поменять карты местами."
    $ show_cards()
    el "Но можно и не пользоваться этим, если собираются забрать ненужную карту."
    $ show_cards()
    el "Естественно, смена карт может помочь не всегда – ведь противник видит, какие карты меняются местами, и тоже может изменить свой выбор."
    $ show_cards()
    el "Далее соперник забирает у вас одну карту в соответствии с вышеописанным алгоритмом."
    $ show_cards()
    el "Ну, и так далее – думаю, все понятно."
    $ show_cards()
    "Чересчур запутанно, как по мне."
    $ show_cards()
    us "Эй, ты, Эйнштейн недоделанный!"
    $ show_cards()
    "Послышался издалека голос Ульянки."
    $ show_cards()
    us "Ничегошеньки не понятно!"
    $ show_cards()
    el "По ходу разберешься."
    hide el  with dissolve
    $ show_cards()
    "Электроник отошел к столу со схемой, оставив Ульяну злиться в одиночестве."
    $ show_cards()
    me "Ходи первая."
    $ show_cards()
    "Лена, смущенная еще больше обычного, потянулась к моим картам..."
    window hide
    return



label v17_demo_play_me_defend_1:
    $ show_cards()
    window show
    "Но на середине стола ее рука застыла..."
    $ show_cards()
    un "Ты будешь..."
    $ show_cards()
    th "Точно! Я же должен защищать свою карту!"
    $ show_cards()
    "Я вспомнил, что там говорил Электроник..."
    $ show_cards()
    "Чтобы попытаться запутать соперника, можно поменять карты местами.{w} И так два раза."
    $ show_cards()
    "А можно и не менять..."
    $ show_cards()
    "Защищать мне эту карту или нет?"
    $ show_cards()
    "К тому же я могу сразу согласиться и отдать ей карту, которую она выбрала."
    $ show_cards()
    "А Лена может изменить свой выбор, взяв другую карту, а может и не менять."
    window hide
    return



label v17_demo_play_me_select_1:

    window show
    "Понемногу все становилось понятно!{w} Или хотя бы понятнее..."
    $ show_cards()
    me "Теперь моя очередь."
    $ show_cards()
    "Я могу вернуть карту, которую она забрала, или выбрать любую другую..."
    window hide
    return



label v17_demo_play_rival_defend:
    $ show_cards()
    window show
    "Лена может попробовать защитить свою карту."
    $ show_cards()
    "Но если я буду внимателен, то все равно возьму ту, что выбрал с самого начала."
    window hide
    return



label v17_demo_play_after_loop:
    $ show_cards()
    window show
    "Получилось!"
    window hide

    $ ui.jumpsoutofcontext('v17_day_2_cards_continue')



label v17_day_2_cards_continue:
    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_day 
    with dissolve

    window show
    "Электроник, до этого лишь молча наблюдавший за игрой, удовлетворенно кивнул."
    "Похоже, теперь мы действительно немного разобрались, что к чему."
    show el normal pioneer at center   with dissolve
    el "Итак, во время игры противники три раза обмениваются картами, а потом вскрываются."
    th "Вдоль или поперек?"
    "Я не смог сдержать улыбку."
    show el angry pioneer at center   with dspr
    el "Что смешного?"
    me "Нет-нет, ничего."
    "Он пристально посмотрел на меня и продолжил."
    show el normal pioneer at center   with dspr
    el "И мы смотрим, у кого лучше карты."
    hide el  with dissolve
    "Электроник отошел к своему ватману."
    "И турнир начался."
    window hide

label v17_un_play:
    python:
        dialogs = {
                        (0, 'win', 'jump'):'v17_un_play_win', 
                        (0, 'fail', 'jump'):'v17_un_play_fail', 
                        (0, 'draw', 'jump'):'v17_un_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalUn(un_avatar_set, u"Лена")
    jump cards_gameloop


label v17_un_play_fail:
    $ day2_card_result = 0
    jump v17_day2_main3

label v17_un_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump v17_un_play

label v17_un_play_win:
    $ persistent.sprite_time = 'sunset'
    scene bg int_dining_hall_sunset 
    with dissolve

    window show
    "Я победил!"
    "Впервые я понял, как трудно играть в игру, только что придуманную, да еще и не тобой."
    "Но я выиграл!"
    "Правда, радость победы несколько огорчало то, что проигравшей оказалась Лена."
    "Она и так выглядит такой неуверенной в себе."
    th "Возможно, следовало все-таки проиграть, это бы ее взбодрило."

    if day2_dv_bet == 1:
        th "Но я же поспорил с Алисой..."

    "Электроник тем временем с гордостью объявил, что первый тур окончен."
    window hide

    scene cg lvl_2_semen_win 
    with dissolve

    window show
    "Через некоторое время на ватмане появилась схема участников второго тура."
    "Пары полуфиналистов составили: Алиса и Женя, Ульяна и..."
    "Я."
    "У меня вырвался обреченный вздох."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg int_dining_hall_sunset 
    with dissolve

    show us grin pioneer at center   with dissolve
    window show
    "И тут же на стул напротив уселась Ульяна!"
    us "Хы!"
    show us laugh pioneer at center   with dspr
    "С улыбкой до ушей она уставилась на меня."
    us "Как это ты Лену обыграл?"
    "Она прищурилась."
    us "Жульничал, наверное?"
    me "Я же не ты. Уметь нужно в карты играть."
    me "А ты как Шурика обыграла?"
    show us grin pioneer at center   with dspr
    us "А..."
    "Ульянка махнула рукой, показывая, как это было просто."
    us "Пригрозила, что вступлю в его клуб."
    show us laugh pioneer at center   with dspr
    "И снова широко улыбнулась."
    us "Будешь мне поддаваться?"
    me "И не надейся!"
    show us dontlike pioneer at center   with dspr
    us "Ну вот..."
    show us laugh pioneer at center   with dspr
    us "Тогда я сама буду выбирать, какую карту тебе отдать!"
    me "Ты правила слышала?"
    show us laugh2 pioneer at center   with dspr
    us "Да плевать!"
    "Похоже, ее действительно это мало волновало."
    me "Что же, тогда и я буду тебе отдавать только те карты, что выберу сам."
    show us laugh pioneer at center   with dspr
    us "Идет!"
    "Хоть мы и отошли от первоначальных правил, но мы с Ульяной все же были в равных условиях."
    "Конечно, можно было начать спор, позвать Электроника и в конце концов настоять на своем, но я был уверен в исходе этой партии."
    "Я посмотрел на Электроника."
    el "Время начинать второй тур!"
    "Скомандовал он."
    "Я взял карты, стараясь, чтобы Ульянке никак не было их видно."
    hide us  with dissolve
    window hide

label v17_us_play:
    python:
        dialogs = {
                        (3, 'me_defend_2', 'call'):'v17_us_play_me_defend_2', 
                        (2, 'me_defend_2', 'call'):'v17_us_play_me_defend_2', 
                        (1, 'me_defend_2', 'call'):'v17_us_play_me_defend_2', 
                        (0, 'win', 'jump'):'v17_us_play_win', 
                        (0, 'fail', 'jump'):'v17_us_play_fail', 
                        (0, 'draw', 'jump'):'v17_us_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalUs(us_avatar_set, u"Ульяна")
    jump cards_gameloop


label v17_us_play_me_defend_2:
    $ show_cards()
    window show
    us "Эй, не мешай карты – это меня путает!"
    window hide
    $ show_cards()
    window show
    "Ммм..."
    window hide
    return

label v17_us_play_fail:
    $ day2_card_result = 1
    jump v17_day2_main3

label v17_us_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump v17_us_play

label v17_us_play_win:

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_day 
    with dissolve

    show us dontlike pioneer at center   with dissolve
    window show
    us "Эй! Так нечестно!"
    us "Ты должен был поддаваться и проиграть!"
    "От недовольства она надула щеки и напоминала какого-то злобного колобка."
    us "Давай переиграем, только ты теперь поддавайся, слышишь?!"
    "Но ее слышал не только я, а весь зал."
    el "Никаких переигровок!"
    "Но Ульяна не обратила на него ни малейшего внимания."
    show us angry pioneer at center   with dspr
    us "Ты должен проиграть!"
    me "С чего ты вообще взяла, что я буду с тобой играть еще раз?."
    us "Ах, так?"
    me "Да, так."
    show us grin pioneer at center   with dspr
    us "Тогда я всем расскажу о том, что ты к Алисе приставал."
    "Сказала она шепотом."
    me "Эй! Ты чего?!"
    "Я перегнулся через стол и грозно посмотрел на нее."
    me "Значит, подслушивала?"
    us "Не подслушивала, а просто мимо проходила."
    "В конце концов, сыграть лишний раунд – это куда лучше, чем..."
    th "Да чтоб вас всех!.."
    "Я вздохнул и обратился к Электронику."
    me "Мы переиграем, все в порядке."
    el "Как знаете..."
    "Он пожал плечами."
    "Итак, матч-реванш начался."
    hide us  with dissolve
    window hide

label v17_us2_play:
    python:
        dialogs = {
                        (0, 'win', 'jump'):'v17_us2_play_win', 
                        (0, 'fail', 'jump'):'v17_us2_play_fail', 
                        (0, 'draw', 'jump'):'v17_us2_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalUs(us_avatar_set, u"Ульяна II")
    jump cards_gameloop


label v17_us2_play_fail:
    $ day2_card_result = 1
    jump v17_day2_main3

label v17_us2_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump v17_us2_play

label v17_us2_play_win:

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_day 
    with dissolve

    show us dontlike pioneer at center   with dissolve
    window show
    me "Даже проще, чем в первый раз."
    "Нарочито небрежно заявил я и вальяжно развалился на стуле."
    us "Так нечестно!"
    "Я ответил ей максимально насмешливым взглядом, на какой только был способен."
    us "У-у, ладно..."
    "Надувшись, она вышла из-за стола."
    hide us  with dissolve
    "Я внимательно посмотрел в сторону Электроника и схемы турнира, пытаясь установить, кто же мне достался в соперники по финалу."
    show dv normal pioneer at center   with dissolve
    "В ту же секунду ко мне за стол села Алиса."
    
    if day2_dv_bet == 0:
        show dv angry pioneer at center   with dspr
        dv "Ты еще пожалеешь, что струсил."
        "Пожалуй, я уже жалел. Но тогда отказ от спора казался мне наиболее здравой идеей."
    else:
        dv "Рассчитываешь выиграть?"
        me "Меньше слов - больше дела."

    show dv smile pioneer at center   with dspr
    dv "Что же, начнем!"
    hide dv  with dissolve
    window hide

    jump v17_dv_play

label v17_dv_play:
    python:
        dialogs = {
                        (0, 'win', 'jump'):'v17_dv_play_win', 
                        (0, 'fail', 'jump'):'v17_dv_play_fail', 
                        (0, 'draw', 'jump'):'v17_dv_play_draw'
                    }
        generate_cards('bg hall', dialogs)
        rival = CardGameRivalDv(dv_avatar_set, u"Алиса")
    jump cards_gameloop

label v17_dv_play_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте еще раз."
    window hide
    jump v17_dv_play

label v17_dv_play_fail:
    $ day2_card_result = 2
    jump v17_day2_main3

label v17_dv_play_win:
    $ day2_card_result = 3
    jump v17_day2_main3







label v17_day2_main3:

    if day2_card_result == 0:

        scene cg lvl_2_lena_win 
        with dissolve

        window show
        "Как обидно все-таки проигрывать..."
        window hide
        pass

    if day2_card_result == 1:
        window show
        "Хотя бы один раунд я выиграл."
        window hide
        pass

    if day2_card_result == 2:
        window show
        "Двачевской я проиграл."
        th "И это плохо. Очень, очень плохо."
        th "Если она действительно всем расскажет этот бред..."
        th "И почему я так уверен, что поверят наверняка ей, а не мне."
        "Я даже не знал точно почему, но был в этом уверен на 100\%."
        window hide
        pass

    if day2_card_result == 3:
        if day2_dv_bet == 1:
            $ lp_dv = (lp_dv) + (2)
            jump v17_day2_dv
        else:
            window show
            th "И неважно, что я не стал спорить с Алисой, главное – выиграл."
            th "Надеюсь, этого будет достаточно, чтобы она отказалась от своей дурацкой затеи..."
            th "Опозорила бы меня на линейке, рассказала бы Ольге Дмитриевне."
            th "Или просто пустила бы слухи по лагерю…"
            th "Причем я уверен, что поверили бы наверняка ей, а не мне. Ну да ладно..."
            window hide
            pass

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_away_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 2

    $ night_time()

    window show
    "Я вышел из столовой."
    "Спать ложиться было еще рано, так что небольшая прогулка показалась отличным вариантом."
    th "Куда бы направиться?"
    window hide

    stop ambience fadeout 3

    $ disable_all_zones()
    $ set_zone('medic_house', 'v17_day2_aidpost_eve')
    $ set_zone('square', 'v17_day2_square_eve')
    $ set_zone('beach', 'v17_day2_beach_eve')
    $ set_zone('boat_station', 'v17_day2_dock_eve')
    $ set_zone('camp_entrance', 'v17_day2_busstop_eve')
    $ set_zone('estrade', 'v17_day2_stage_eve')
    $ set_zone('sport_area', 'v17_day2_football_eve')
    $ show_map()

label v17_day2_aidpost_eve:

    $ persistent.sprite_time = 'night'
    scene bg ext_aidpost_night 
    with dissolve

    window show
    "Я наслаждался ночной тишиной и шел куда-то вперед, смотря на усыпанное звездами небо. Внезапно я понял, что оказался прямо перед медпунктом."
    "В мои планы на ближайшие дни никак не входила встреча с медсестрой, так что я поспешил убраться отсюда."
    "..."
    window hide

    jump v17_day2_main4

label v17_day2_square_eve:

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    window show
    "Оказавшись на площади, я с наслаждением плюхнулся на скамейку."
    "Запрокинув голову, я любовался прекрасным в своем совершенстве собранием миллиардов звезд."
    "..."
    window hide

    jump v17_day2_main4

label v17_day2_beach_eve:

    $ persistent.sprite_time = 'night'
    scene bg ext_beach_night 
    with dissolve

    stop ambience fadeout 2

    window show
    "Я вышел на пляж."
    "Я не собирался плавать, однако все же опустил руку в воду, измерив температуру."
    th "Вполне теплая."
    "Некоторое время я бросал камешки в воду, любуясь получающимся кругами. Почувствовав, что засыпаю, я поспешно двинулся дальше."
    "..."
    window hide

    jump v17_day2_main4

label v17_day2_dock_eve:

    $ persistent.sprite_time = 'night'
    scene bg ext_boathouse_night 
    with dissolve

    window show
    "Я пошел в сторону пристани."
    "Солнце уже едва виднелось из-за горизонта, и мало-помалу черное небо покрывалось белоснежной россыпью звезд."
    "Вспоминая детство, я протянул к звездам раскрытую ладонь, словно пытаясь поймать хоть одну. Никогда я еще не чувствовал себя таким старым."
    "Я медленно побрел назад, погруженный в свои мысли."
    window hide

    jump v17_day2_main4

label v17_day2_busstop_eve:

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "События прошедшего дня все еще ярко мелькали у меня в голове – чертов никому не нужный, глупый турнир…"
    "Я просто устал от всего, от всех сегодняшних разговоров, новых лиц, беготни..."
    "Я вышел на площадь, уселся на лавочку и бесцельно уставился на памятник Генде."
    "..."
    window hide

    with fade2

    window show
    "Не в силах больше выносить переполнявшие меня печальные мысли, я двинулся дальше."

    stop ambience fadeout 2 

    "..."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_no_bus_night 
    with dissolve

    play ambience ambience_camp_entrance_night fadein 3

    window show
    th "Автобусная остановка...{w} И вот я снова здесь."
    th "Неужто я жду, что автобус вернется забрать меня?"
    th "Вряд ли."
    "Некоторое время я простоял, наблюдая, как черная линия горизонта пожирает последние лучи солнца."
    "Возможно, лучшим выбором бы было бежать в поля, а не идти в лагерь?"
    "Возможно, тогда все было бы по-другому."

    if day2_cards_with_sl == 1:
        $ lp_sl = (lp_sl) + (1)
        jump v17_day2_sl

    stop ambience fadeout 2

    "Вздохнув, я решил, что пора возвращаться."
    "..."
    window hide

    jump v17_day2_main4

label v17_day2_stage_eve:

    if day2_card_result == 1:
        $ lp_us = (lp_us) + (1)
        jump v17_day2_us

    scene black 
    with dissolve

    window show
    "Я решил пойти на север (по крайней мере туда, где он по моим представлениям находился)."
    window hide

    scene bg ext_stage_big_night 
    with dissolve

    window show
    "Спустя пару минут я вышел на концертную площадку. Несколько рядов деревянных скамеек и деревянная же эстрада."
    "Я поднялся на сцену."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_stage_normal_night 
    with dissolve

    window show
    "Там было довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
    "Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьет слепящий свет прожекторов."
    "Я исполнил длинное красивое соло на воображаемой гитаре."
    "Представив, как же глупо я выгляжу со стороны, я поспешил убраться отсюда."
    th "Надеюсь, никто этого не видел."
    "..."
    window hide

    jump v17_day2_main4

label v17_day2_football_eve:

    if day2_card_result == 0 and day2_dv_bet == 0:
        $ lp_un = (lp_un) + (1)
        jump v17_day2_un

    $ persistent.sprite_time = 'night'
    scene bg ext_playground_night 
    with dissolve

    window hide
    "Ноги принесли меня к пустому футбольному полю. В голове всплыла пара расплывчатых воспоминаний из детства. Я поймал себя на мысли, что играть в футбол было не так уж и плохо."
    "..."
    window show

    jump v17_day2_main4

label v17_day2_dv:

    scene cg lvl_4_semen_win 
    with dissolve

    play music music_list["always_ready"] fadein 5

    window show
    "Это моя победа! Пускай Двачевская теперь знает, что со мной лучше не связываться!"
    if day2_dv_bet == 1:
        th "По крайней мере, не зря я с ней поспорил."
    "Теперь оставалось надеяться, что она сдержит свое обещание."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_beach_night 
    with dissolve

    $ night_time()

    stop ambience fadeout 2

    window show
    "Я решил остудить жар победы, бушующий в моей душе, и отправился поглазеть на упомянутый вчера Славей пляж."
    "Я не был лучшим в мире плавцом, но все же решил пару раз окунуться."
    "Сбросив все до трусов, я вошел в прохладную воду. Невероятное чувство радости разливалось по моему телу."

    stop music fadeout 3

    "Раззадоренный, я поплыл в сторону буйков."
    "Я плыл медленно и размеренно, следил за каждым движением рук и ног, за каждым вдохом и выдохом."
    window hide

    play music music_list["that_s_our_madhouse"] fadein 3

    scene bg ext_beach_night:
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        repeat
    window hide

    play sound sfx_shoulder_dive_water

    show blink 

    $ renpy.pause(1)

    window show
    "Я уже почти доплыл, как вдруг почувствовал сильный удар по спине, от которого ушел под воду."
    "Я начал захлебываться, но каким-то чудом удержался на воде, схватившись за буек."
    window hide

    scene cg d2_water_dan 
    show unblink 
    with dissolve

    play sound sfx_water_emerge

    $ renpy.pause(1)

    window show
    "Я обернулся и увидел беззаботно качающуюся на волнах Алису."
    me "Ты что делаешь?!"
    dv "Приветствую победителя."
    me "А если бы я утонул?!"
    dv "Ну, я бы тебя спасла."
    "Я с сомнением швыркнул носом, избавляясь от остатков воды."

    stop music fadeout 3

    "Факт есть факт - я совсем не чувствовал себя комфортно наедине с Двачевской в двадцати метрах от берега. Собрав последние силы, я что есть прыти погреб назад."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_beach_night 
    with dissolve

    play ambience ambience_boat_station_night fadein 3

    window show
    "Растянувшись на песке, я попытался отдышаться."
    show dv normal swim at center   with dissolve
    "Через некоторое время из воды вышла и Алиса."
    dv "Неплохо плаваешь!"
    th "У меня был хороший стимул."
    me "Ты тоже ничего."
    show dv smile swim at center   with dspr
    dv "Вторая твоя победа за сегодня.{w} Снимаю с тебя те два косяка."
    th "Она все еще помнит об этом..."
    me "Благодарю покорно…"
    "Похоже, у Двачевской было несколько личное понимание реальности."
    dv "Походу ты не такой уж и неудачник…"
    window hide

    scene cg d2_2ch_beach with dissolve:
        pos (0,-1920)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -250)
    window show
    "Ей все же удалось меня чуть удивить. Повернув голову в ее сторону, я обнаружил, что Алиса была одета в великолепно сидящий на ней оранжевый купальник, чертовски хорошо подчеркивающий ее природные данные."
    me "С чего это я неудачник?"
    "Она хитро улыбнулась."
    dv "А что, не так?"
    me "Нет конечно!"
    dv "И чем докажешь?"
    me "Опять? Не собираюсь я тебе ничего доказывать!"
    dv "Ах, вот как, значит..."
    "Непривычно, но в ее голосе на этот раз не было ни следов обычной злобы."
    "Внезапно в воздухе повисло неестественное молчание."
    "Понаблюдав пару мгновений за лениво наползающими на пляж волнами, я вновь повернулся в сторону Алисы."
    "К моему удивлению, та все так же смотрела словно сквозь меня, казалось, забыв, что я вообще все еще здесь."
    me "Кхе-хм...Алиса?"
    "Ее взгляд мигом прояснился."
    dv "Ладно, бывай."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_beach_night 
    with dissolve

    window show
    "Она забрала лежащую рядом одежду и ушла."
    "..."
    window hide

    with fade2

    window show
    "Не смотря на поздний час, я остался лежать на пляже, бездумно глядя на бесконечное небо, усыпанное мраморной крошкой звезд."
    window hide

    scene stars 
    with dissolve

    window show
    me "И почему я так редко смотрел на звезды раньше?"
    "Лежа сейчас в черт знает каком году черт знает где, я вдруг явственно понял, как несвободен я был."
    th "У меня было все время мира...но у меня постоянно нехватало времени осознать это."
    th "Я был доволен своей жизнью. Я сам выбрал ее...{w} Ведь так?"
    th "Что я буду делать, если вернусь домой? То же, что и всегда, или..."

    stop ambience fadeout 0

    play music music_list["that_s_our_madhouse"] fadein 1

    th "Стоп!{w} Она же и мою одежду забрала!"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_beach_night 
    with dissolve

    window show
    "Я вскочил и начал осматривать пляж."
    "Действительно, Алиса унесла и мою пионерскую форму."
    th "Черт возьми!"
    "А ведь я только начинал думать, что наши отношения начали налаживаться, но не-ет, куда там, с этой девкой можно нормально сосуществовать лишь одним способом - подальше от нее!!"
    "Надо было что-то срочно придумать. Перспектива возвращаться к Ольге Дмитриевне в одних мокрых трусах меня не прельщала. В какой палатке живет Алиса, я не знал."
    th "Стучаться во все подряд - не вариант…"
    th "Тогда к Славе? {w} Ночью, в одних трусах...рискую остаться непонятым."
    "С какой стороны ни посмотри, я попал, причем попал серьезно…"
    "Решив, что мой единственный шанс - догнать Алису, я бросился в погоню."

    stop music fadeout 3

    "... быстрее!"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Я выбежал на площадь."
    show dv normal pioneer2 at center   with dissolve
    "К моему огромному удивлению, Алиса сидела на лавочке и явно скучала."
    me "Отдай!"
    show dv guilty pioneer2 at center   with dspr
    dv "Да бери…"
    "Ответила она, как мне показалось, слегка виноватым тоном и протянула мне мою форму."
    me "…"
    show dv shy pioneer2 at center   with dspr
    dv "Только не думай, что я это специально тут тебя ждала и все такое..."
    hide dv  with dissolve
    "Алиса развернулась и неспеша пошла в сторону палаток."
    "Я остался стоять как вкопанный."
    "Ситуация была много выше моего понимания."
    th "Ну, видимо, даже у нее есть совесть…{w} Да?"

    stop ambience fadeout 2

    "Я направился к домику Ольги Дмитриевны."
    window hide

    jump v17_day2_main4

label v17_day2_sl:

    "Я уже собирался возвращаться в лагерь, как вдруг услышал звук шагов за воротами."
    th "И кого еще принесло?.."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_clubs_night 
    with dissolve

    window show
    "Быстро дойдя до здания кружков, я заметил, как кто-то идет по лесной тропинке."
    "Было темно, так что, кроме размытого силуэта, разглядеть ничего не удалось."
    "Для местных подобные ночные маневры были необычны."
    th "Может, стоит проследить."

    stop ambience fadeout 2

    "Я быстро, но по возможности осторожно направился за таинственной тенью."
    window hide

    play ambience ambience_forest_night fadein 3

    $ persistent.sprite_time = 'night'
    scene bg ext_path_night 
    with dissolve

    window show
    "Тропинки сменяли друг друга, и вскоре я оказался в чаще леса, окончательно потеряв из виду незнакомца."
    th "Похоже, я отстал."
    "Войдя в просвет между деревьями, я обнаружил перед собой восхитительный вид на небольшое лесное озеро."
    window hide

    scene cg d2_slavya_forest 
    with dissolve

    play music music_list["forest_maiden"] fadein 5

    "И тут я увидел Славю…{w} Она она вприпрыжку шла вдоль озера, даже не шла – порхала, на ходу стягивая пионерский галстук и расправляя рубашку."
    "Я не был ценителем живописи. Но я с уверенностью мог сказать, что лучшей натуры для картины не найти в целом мире."
    "Она настолько гармонировала с природой, что было бы невозможно представить это озеро, этот лес - без нее."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_path_night 
    with dissolve

    window show
    "Я бесшумно последовал за ней, не в силах оторвать глаз от ее совершенства."
    "Мало-помалу ко мне пришло понимание того, что я делаю. Я ощутил сильный укол совести, но сейчас было уже поздно останавливаться - мы шли обратно к лагерю."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    window show
    "Вскоре мы оказались на площади."
    "Славя остановилась и обернулась в мою сторону."
    show sl normal pioneer far at center    with dissolve 
    sl "Думаешь, я тебя не заметила?"
    "Моей первой мыслью было от стыда прыгнуть в ближайшие кусты, но я постарался сохранить хотя бы видимость спокойствия."
    me "И...э-э...как давно?"
    show sl normal pioneer at center   with dissolve
    sl "Не знаю..."
    "Славя подошла ближе."
    show sl smile pioneer at center   with dspr
    sl "Может быть, минут пять. Может - десять."
    me "То есть и там, на озере?.."
    show sl surprise pioneer at center   with dspr
    sl "На каком озере?"
    me "Ну как же..."
    "Она выглядела искренне удивленной. Я не мог понять, притворяется ли она, что ничего не произошло, или..."
    me "Ладно, забудь."
    "Я и так показал себя достаточно бестактным. Будет разумно остановиться на этом."
    show sl happy pioneer at center   with dspr
    sl "Хорошо."
    "Неожиданно легко согласилась она."
    sl "Какая сегодня ночь замечательная!"
    "Славя села на скамейку и подняла глаза на небо."
    me "Готов поспорить, здесь часто бывают такие ночи."
    show sl smile2 pioneer at center   with dspr
    sl "Ну, наверное..."
    me "Почему так неуверенно?"
    sl "Нет, просто задумалась."
    me "О чем?"
    show sl normal pioneer at center   with dspr
    "Она внимательно посмотрела на меня, словно что-то искала у меня на лице, но затем вновь вернулась к созерцанию звезд."
    sl "Просто иногда по ночам такое настроение бывает...{w} Днем – вся в делах, даже отдохнуть порой некогда, а ночью тут так тихо."
    me "Только ты и звездное небо...ничего лишнего."
    "Славя радостно улыбнулась."
    show sl smile pioneer at center   with dspr
    sl "Да! Ты меня понимаешь!"
    "Некоторое время мы тихо просидели, смотря на звезды."
    show sl normal pioneer at center   with dspr
    sl "Ладно!"
    "Она резким движением встала и поправила юбку."
    show sl smile pioneer at center   with dspr
    sl "Уже и спать пора!"
    me "Спокойной ночи!"
    hide sl  with dissolve
    "Я проводил ее взглядом."
    "Невольно для себя я отметил, что рад был встретить ее этим вечером. Возможно, у нее тоже есть свои секреты, но...{w} они есть у всех, верно?"
    "Возможно, мне стоит меньше играть в детектива и совать нос в чужие дела."
    th "Хорошая ночь."
    "..."
    window hide

    with fade2

    window show
    "..."

    stop ambience fadeout 2

    stop music fadeout 3

    "Вскоре меня начало клонить в сон."
    window hide

    jump v17_day2_main4

label v17_day2_un:

    $ day2_un = 1

    $ persistent.sprite_time = 'night'
    scene bg ext_playground_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Мне хотелось уйти подальше отсюда."
    th "Проиграть в первом же раунде…"
    "Нет, такого я сам себе простить не мог."
    "Тогда мне показалось, что самым подходящим местом уединения будет спортивная площадка."
    th "И правда, кому вечером взбредет в голову играть в футбол?"
    "Я расположился на лавочке, размышляя о произошедшем."
    "Через некоторое время мне послышались явственные звуки, доносившиеся со стороны площадки для бадминтона."

    play sound sfx_lena_plays_tennis_fail

    "Присмотревшись, я увидел, что кто-то отчаянно машет рукой."
    th "Тренируется? Так поздно?"
    "К моему удивлению, это была Лена."
    "Она подкидывала воланчик и пыталась попасть по нему ракеткой."
    "Однако выходило это у нее, честно говоря, паршиво."
    "Я некоторое время просто смотрел, но потом решил все же подойти."
    "Стараясь ступать как можно тише, я приблизился. Учитывая ее привычку пугаться даже малейшего шороха, я хотел избежать повтора прошлых ошибок."
    show un normal sport at center   with dissolve
    me "Привет!"
    "При звуках моего голоса Лена молниеностно спрятала за спину ракетку и воланчик."
    me "Тренируешься?"
    un "Ну, не то чтобы…"
    me "Смотрю, у тебя не очень получается.{w} Не против, если я попробую помочь?"
    "Я никогда не был хорош в бадминтоне, но, по крайней мере, основы знал."
    show un shy sport at center   with dspr
    un "Спасибо."
    "Она покраснела."
    un "Хочу попасть в команду по бадминтону, но, видишь, у меня не очень выходит…"
    un "Я бы сегодня и не пришла, но…"
    show un smile sport at center   with dspr
    "Она подняла глаза на меня."
    un "Мне никогда в карты не везло, а сегодня выиграла и подумала, что, может, и с этим получится…"
    "Я невольно испытал радость от того, что мой проигрыш помог хоть кому-то."
    me "Никогда бы не подумал, что ты увлекаешься спортом."
    show un shy sport at center   with dspr
    "Она опять покраснела."
    me "Кхе-кхм…{w} Вот, смотри!"
    "Я взял ракетку, подбросил воланчик и…"

    play sound sfx_tennis_serve_1

    show un surprise sport at center   with dspr
    "Ударил с такой силой, что он перелетел ограду и скрылся где-то между деревьями."
    me "Вот черт, перестарался!"
    "Сказалось ли то, что в бадминтон я не играл уже много лет, или же мое помолодевшее тело..."
    show un normal sport at center   with dspr
    un "Ничего…{w} Правда, это был последний…"
    me "Последний? Тогда придется идти искать."
    un "Нет, не стоит…{w} Там в лесу…"
    me "Что, волки по ночам бродят?"
    un "Может быть…"
    "Я-то шутил, а вот она, похоже, нет."
    me "Не бойся, никого там нет. Идем!"
    un "Ну, если только с тобой…"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_path_night 
    with dissolve

    window show
    "Мы вышли с площадки, и я начал осматриваться в поисках волана."

    play sound sfx_owl_far

    "Как вдруг поблизости раздалось пронзительное уханье совы."
    window hide

    stop ambience fadeout 2

    scene cg d2_sovenok 
    with dissolve

    play music music_list["confession_oboe"] fadein 5

    window show
    "Подпрыгнув от испуга Лена схватила меня сзади, обвив руками."
    "Настала моя очередь подпрыгивать, но желание схватиться за ближайшее дерево я в себе подавил."
    "Она так близко. Я чувствую ее тепло."
    "Ее тело такое мягкое..."
    "Лихорадочно хватая ртом воздух, я запрокинул голову, проваливаясь в почти осязаемое блаженство."
    "К своему удивлению, над собой я увидел сидящего на длинном суку крошечного совенка, державшего в клюве воланчик."
    "Подождав еще хоть пару секунд, я нехотя указал на него Лене."
    me "Это вот его ты боялась?"
    un "Угу…"
    me "Посмотри, он совсем не страшный."
    "Она выглянула у меня из-за спины, все так же продолжая крепко меня обнимать."
    un "Не страшный…"
    me "Сейчас, подожди."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = 'night'
    scene bg ext_path_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    show un shy sport at center   with dissolve
    window show
    "Я мягко освободился от ее объятий и подошел к совенку."
    "Удивительно, но при моем приближении он и не думал улетать.{w} Я аккуратно отобрал у совенка воланчик."
    me "Смотри, он будто ручной!{w} Хочешь его погладить?"
    un "В другой раз, может быть?.."
    "Я протянул Лене воланчик."
    show un smile sport at center   with dspr
    un "Спасибо."
    "Она еле заметно улыбнулась."
    show un normal sport at center   with dspr
    un "Мне пора."
    me "Успехов тебе в бадминтоне."
    show un smile sport at center   with dspr
    "Она вновь улыбнулась и побежала в сторону лагеря."
    hide un  with dissolve
    th "Какая же она все-таки милая."

    stop ambience fadeout 2

    "..."
    window hide

    jump v17_day2_main4

label v17_day2_us:

    scene black 
    with dissolve

    window show
    "События прошедшего дня проносились у меня в голове – чертов никому не нужный глупый турнир…"
    "Мне не хотелось никого сегодня видеть, и я отправился подальше от рядов палаток, обдумывая сегодняшний день."
    "Солнце скрылось за горизонтом, и на безоблачном небе надо мной начали робко зажигаться первые звезды."
    "Я замедлил шаг и уставился ввысь."
    "Неожиданно ночное небо резанула сияющая нить. Падающая звезда!"
    "Я горько усмехнулся. Уже давно у меня не было желаний, которые хотелось бы загадать."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_stage_big_night 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    "Вскоре я вышел к концертной площадке."
    "Несколько рядов деревянных скамеек и деревянная же эстрада."
    "Я поднялся на сцену."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_stage_normal_night 
    with dissolve

    window show
    "Там было довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
    "Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьет слепящий свет прожекторов."
    "Я исполнил длинное красивое соло на воображаемой гитаре."
    "Представив, как же глупо я выгляжу со стороны, я поспешил убраться отсюда."
    th "Надеюсь, никто этого не видел."

    stop ambience fadeout 2

    play music music_list["glimmering_coals"] fadein 5

    us "Ого!"
    "Голос доносился откуда-то сверху."
    show us laugh pioneer  with dissolve:
        xalign 0.5
        yanchor 0.116
        rotate 180
    "Я поднял глаза и увидел Ульянку, свесившуюся с балки под потолком сцены."
    us "Что это мы тут делаем?"
    me "Да не...я тут просто…"
    "Я беспомощно вздохнул. Оправдываться было бесполезно."
    me "Сама все видела."
    "Выдавил я и смущенно отвернулся."
    show us laugh2 pioneer  with dissolve:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Да ты у нас великий гитарист!"
    "Я ничего не ответил."
    show us smile pioneer  with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Ну, ладно тебе, не дуйся, смотрелось забавно!"
    "Она захихикала."
    "Хотелось провалиться сквозь землю."
    
    show us grin pioneer  with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Подойди-ка сюда."
    me "Куда?"
    us "Ко мне!"
    me "Я туда лезть не собираюсь, не думай даже!"
    "Последнее, что мне хотелось - навернуться с такой высоты."
    us "Да нет! Просто сюда."
    "Я почувствовал подвох, но медленно направился в ее сторону, тщательно смотря под ноги."
    "Когда я оказался точно под ней, она крикнула:"
    us "Лови!"
    window hide

    scene cg d2_ussr_falling 
    with dissolve

    window show
    "И прыгнула…"
    "В моей голове, подобно пулеметной очереди, проносились противоречивые мысли."
    th "Как я ее поймаю? А надо ли вообще ловить? А что, если она разобьется? Нет, наверняка себе что-то сломает! Почему именно я?!"
    th "Она сама виновата – нечего дурью маяться! А если я только хуже сделаю? Вряд ли я смогу ее поймать, даже если попытаюсь."
    "В конце концов, инстинкт самосохранения выиграл, и я отпрыгнул в сторону."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = 'night'
    scene bg ext_stage_normal_night 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    show us upset pioneer at center   with dissolve

    $ renpy.pause(1)

    show us sad pioneer at center   with dspr
    window show
    "Ульянка мягко приземлилась, перекувыркнулась, мгновенно вскочила на ноги и обиженно посмотрела на меня."
    us "Почему не поймал?"
    me "Да, ладно, не разбилась же..."
    "Ответил я, отведя взгляд."
    show us shy2 pioneer at center   with dspr
    us "А если бы разбилась?"
    me "Не разбилась!{w} Да и что это вообще было? Дешевых фильмов обсмотрелась?"
    show us grin pioneer at center   with dspr
    us "А что, волнуешься за меня?"
    "Ехидно прищурившись, она с ухмылкой смотрела прямо на меня."
    me "Ну...в такой ситуации...естественно, волнуюсь..."
    "Красный как рак, я изо всех сил старался не смотреть на нее."
    show us surp3 pioneer at center   with dspr
    us "Я польщена."
    me "Эй, ты не подумай…"
    show us laugh pioneer at center   with dspr
    us "Ладно-ладно. Прощаю тебе карты."
    me "А вот я тебе это прощать не…"
    hide us  with dissolve
    "Я не успел закончить – Ульянка спрыгнула со сцены и убежала в сторону лагеря."
    th "Очередная глупая выходка глупой девчонки. Когда-нибудь допрыгается - костей не соберет."
    th "Волнуюсь за нее? Естественно, я за нее волнуюсь! Творит что хочет, не думает ни о чем! Конечно, я испугался за нее! Это совершенно естественно!"
    th "Любой бы на моем месте…"
    "Чуть ли не подпрыгивая от злости, я направился в сторону своей палатки."
    window hide

    stop ambience fadeout 2

    jump v17_day2_main4

label v17_day2_main4:

    $ persistent.sprite_time = 'night'
    scene bg ext_house_of_mt_night_without_light 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    "На подходе к домику вожатой меня накрыла дикая усталость."
    "Свет в окне не горел, значит, Ольга Дмитриевна уже спала."
    th "Странно, вчера она меня ждала…"
    th "Я сегодня слишком поздно?"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg int_house_of_mt_night2 
    with dissolve

    window show
    "Я зашел, тихо разделся и лег на кровать."
    th "Если поразмыслить, то моя ситуация за сегодня совершенно не прояснилась."
    th "Я не узнал, ни где я, ни почему я здесь."
    th "Ни одного ответа, и лишь новые вопросы. Все эти девочки...кто они?"
    th "Каждый из местных что-то от меня скрывает. Но нужно ли мне знать правду?"
    th "Я несчастлив здесь? Хочу ли я домой? Что я намерен делать?"
    "Моя голова гудела от всех этих вопросов. Истощенный духовно и физически, я провалился в липкие объятья сна."
    "В последние секунды бодрствования я осознал, как же счастлив я здесь находиться."
    window hide

    stop music fadeout 3

    scene bg black 
    with fade3

    $ renpy.pause(3)

    jump v17_day3_main1

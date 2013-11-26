init:
    $ d1_keys = False

label day1:

    $ backdrop = 'days'

    $ new_chapter(1, u"День первый")
    $ day_time()

    $ make_names_unknown()

    scene bg black 

    play music music_list["no_tresspassing"] fadein 0

    $ renpy.pause(2)

    $ persistent.sprite_time = 'day'
    scene bg int_bus 
    with flash

    window show
    "Просыпаясь, я чувствовал теплое прикосновение солнца к щеке. Но не оно тормошило теперь меня, а смутное нехорошее предчувствие."
    "За джцать (подставить его возраст) лет жизни я не испытал ни забот, ни тревог, просто плывя по течению. Но все же кто-то внутри меня все эти годы словно ждал беды. И беда сама нашла меня…"
    th "Ну я и соня. Меня даже давешний скрип немазаных тормозов не…"
    th "…Разбудил. Стоп. Остановку, что ли, проехал?"
    "Я вскочил, кинулся к дверям."
    "Но двери не было…"
    "Я оглядел автобус и понял, что это больше не привычный видавший виды ЛиАЗ. Мягкие ворсистые панели, высокие спинки, занавески и неуловимый дух «братских стран» во всем — то явно был рейсовый «Икарус», который останавливается, только когда мальчикам нужно налево, девочкам — направо."
    "Мгновение я не знал, что и думать."
    th "Как?..{w} Что?..{w} Но я же?.."
    th "Похищен?"
    th "Жив ли вообще?"

    play sound sfx_punch_medium

    with vpunch
    "Я хлопнул себя по щеке. Наваждение не думало проходить, и пришлось приложиться о спинку ближайшего кресла."


    "Нет, такая боль не может быть плодом воображения."
    #TODO или "Нет, эта боль точно не кажется мне."
    th "Итак, все же похищение?"
    th "С чего бы? Едва ли я нужен кому-то, даже своим родным."
    th "Что несомненно — во сне меня вывезли черт знает куда, факт."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_bus 
    with dissolve

    window show
    "Второй раз за день я изумленно огляделся. Опять неизвестно где; к тому же ни следа автобуса, из которого только что не чаял выбраться."
    "Ясно было лишь одно: вокруг меня…"

    th "Лето!{w} Век сгущенки не видать — настоящее лето!{w} Как такое возмо…"
    "Голову пронзила боль — то ли от непривычных мне умственных усилий, то ли от того, как я треснулся в автобусе".
    "Постепенно воспоминания все же стали проясняться…"

    window hide
    scene anim intro_14 
    with fade2

    play sound sfx_intro_bus_transition
    $ renpy.pause(3, hard=True)
    scene anim intro_15 
    with fade
    $ renpy.pause(3, hard=True)

    play ambience ambience_day_countryside_ambience fadein 5
    scene anim intro_16 
    with fade
    $ renpy.pause(3)

    window show
    "Дорога, уходящая за горизонт, леса и луга, сливающиеся в мутное желто-зеленое пятно."
    "Девушка…{w} Ее губы шевелятся, но я ничего не слышу."

    stop ambience fadeout 3

    "Голова раскалывается!"
    window hide

    $ renpy.pause(2)

    $ persistent.sprite_time = 'day'
    scene bg ext_bus 
    with fade2

    window show
    th "Эта девушка…"
    th "Она что, привиделась мне? Я брежу?"
    "Но стоило подумать о ней, как стало гораздо спокойнее, головная боль слегка ослабла."
    th "Если она реальна, то, очевидно,  причастна к моему похищению. Во всяком случае, знает, кто и зачем…"
    th "Тут я заметил, что никто не сторожит меня."
    th "Сейчас или никогда!"
    "Не тратя время на раздумья, я бросился назад, надеясь, что привезли меня оттуда."

    stop music fadeout 3

    "…"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_road_day 
    with dissolve2

    play ambience ambience_ext_road_day fadein 3

    window show
    "..."
    "Никогда не был силен в физкультуре. То есть совсем."
    "Неполные сто метров вызвали одышку и непреодолимое желание сесть передохнуть."
    "Может, оно и к лучшему, так как разумно было лишь одно: сесть и думать. "
    th "Как же выбраться отсюда на своих двоих?"
    "Ландшафт не нарушало ничто рукотворное.
    "За исключением дороги, по которой, очевидно, меня и привезли."
    "Кругом одно море трав и листвы."
    "Листвы!.. Ни одной ели или сосны. Как же далеко меня забросили!"
    me "Пейзаж был достоин кисти Репина. Или Шишкина? Не знаю, никогда не увлекался ни 3D-природой, ни 2D."
    "Солнце впервые за бессчетные дни касалось лица. Зрелище плывущих облаков и шелест листьев наводили на странную мысль, что человеку для счастья не нужны экран и наушники."
    "Но куда более насущная мысль:"
    th "Что же делать?"
    "Страх с новой силой захлестнул меня."
    Кто знает, как долго идти до населенного пункта? Дойду ли?"
    "Диванная логика, помноженная на боевики детства, подсказывает, что  похитители не дадут мне уйти, раз уже зашли так далеко."

    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_camp_entrance_day 
    with dissolve2

    window show
    "Автобус остановился у кирпичной стены."
    "Над воротами красовалась нелепая надпись «Совенок»."
    th "Шрифт, правда, выглядит подозрительно современным."
    "По бокам возвышались статуи, в которых легко можно было угадать пионеров."
    me "Заброшенный пионерский лагерь. Просто здорово."
    "По спине пробежал холодок."
    "Я припомнил все виденные мной ужастики и вызывающие прохладный пот истории, где действие происходило в заброшенной гостинице или парке. Самое приятное, что мне грозит, — работа в котельной за еду без нормированного рабочего дня."
    "А я уже очень давно не работал и даже не умею играть на гитаре и не пробовал мацы."
    th "Видимо, снова садиться в автобус не стоило."
    "Однако это место совсем не выглядело заброшенным: ржавчина на воротах недавно закрашена в десятый слой, гипс статуй бел и гладок."
    me "«Совенок»…"
    th "И правда скрыта за вратами..."
    "Я, невольно стараясь ступать тише, направился к воротам."
    "Мне оставалось сделать последние пару шагов, как вдруг ворота приоткрылись, и мне навстречу вышла...{w} девочка?"

    show sl normal pioneer far at center    with dissolve

    "Девчонка лет четырнадцати. Длинные светлые волосы...{w} пионерская форма."
    th "Что ж, это было ожидаемо."
    th "Ну, по крайней мере, некоторая извращенная логика здесь присутствует."
    "Все мои силы ушли на то, чтобы не заорать при неожиданном появлении незнакомки, так что теперь я стоял, как истукан."

    show sl smile pioneer at center   with dissolve

    "Она подошла ближе. Я невольно отметил великолепие ее голубых глаз, как у чистокровных японок в т о м мире."
    sl "Привет, я вижу ты новичок."

    window hide

    menu:
        "Не отвечать ей":
            window show
            "Я настороженно наблюдал за девчонкой."
            "От нее не исходило явной угрозы, но дураку понятно, что все здесь не так просто."
            th "Не стоит действовать наобум."
            show sl normal pioneer at center   with dspr
            sl "Что молчишь?"
            "Я как можно непринужденнее ответил:"
            me "Ну… да…"

        "Ответить":
            $ lp_sl = (lp_sl) + (1)
            window show
            me "Кхм, да, только приехал."

    show sl smile2 pioneer at center   with dspr

    sl "Что же, добро пожаловать!"
    "Она широко улыбнулась."
    "Пока все шло неплохо...или?"
    th "Не стоило возвращаться. Нужно было идти."
    "Я продолжал пялиться, судорожно вспоминая, как же выглядит дружелюбная улыбка. "

    show sl normal pioneer at center   with dspr

    sl "Что смешного?"
    "Девочка окинула меня взглядом с ног до головы."
    "Значит, вышло все же неправильно. 3D-мир чересчур сложен. Я  невольно от–ступил на шаг:"
    me "Н-ничего..."

    show sl smile pioneer at center   with dspr

    sl "Ну и славно."
    th "Сомнительно; к тому же еще в школе говорили «славно» только нянечки. Подозрительно."
    me "А ты, наверное, знаешь…"

    show sl normal pioneer at center   with dspr

    sl "Тебе к вожатой надо сразу, она все расскажет!"
    sl "Смотри.{w} Сейчас идешь прямо-прямо, доходишь до площади, затем сворачиваешь налево, там будут домики."
    "Она показала в сторону ворот, как будто я знал, что за ними."
    sl "Ну спросишь у кого-нибудь, где домик Ольги Дмитриевны!"
    me "Я… эээ…"
    sl "Надеюсь, все понял?"
    th "Понял бы, не мешай путаница в мыслях."
    sl "А мне пора."

    hide sl  with dissolve

    "Девочка помахала мне рукой и скрылась за воротами."
    th "Вожатая, да?"
    th "Меня все меньше радует происходящее, но хуже вряд ли станет."
    th "Итак, вперед, навстречу ответам!"

    stop ambience fadeout 2

    "Я побрел в указанном направлении."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show
    stop music fadeout 5

    "Я уже было собирался подойти поближе..."

    play sound sfx_open_door_clubs fadein 0

    show un normal pioneer far at left   with dissolve   

    "…Как дверь открылась, и вышла еще одна девочка."
    "Мне сразу бросилось в глаза ее невероятно грустное лицо. Весьма симпатичное."
    "Девочка остановилась, неподвижно глядя сквозь меня."

    show un surprise pioneer far at left   with dspr

    "Я вновь застыл, не зная, как лучше поступить."

    play music music_list["i_want_to_play"] fadein 5

    show us grin sport far at right   with dissolve 

    play sound sfx_bush_leaves fadein 0

    "Неожиданно из соседних кустов выскочила очередная девчонка. На этот раз совсем мелкая."
    "На ее ярко-красной майке гордо красовалась надпись «СССР»."
    th "У одной из них наверняка можно спросить направление."
    
    show un surprise pioneer far at left   with dspr
    show us surp3 sport far at right  #TODO# with dspr

    "Тем временем девчонка в красной майке подскочила к грустной девочке и, энергично жестикулируя, начала что-то бойко той рассказывать."
    
    show un shy pioneer far at left   with dspr
    
    "Та явно смутилась и ничего не ответив, потупила взгляд."
    "Мелкая достала что-то из кармана и встряхнула перед лицом подруги."
    window hide

    scene cg d1_grasshopper 
    with dissolve

    window show
    un "Ииииии-иии-иииииии!"
    "По внешнему виду нельзя было предположить, что ее голос может быть настолько громким."
    "Пронзительный вопль затих за поворотом."

    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day 
    show us grin sport at left  #TODO# with dspr
    with dissolve

    "Мелкая хитро улыбнулась мне и побежала за ней."

    hide us 

    th "Они выглядят… обычно? Для трехмерных, начиненных требухой, разумеется."
    th "Не знаю, что я собирался увидеть внутри лагеря, но явно не э т о…"

    stop music fadeout 5

    th "Снова со мной творится непонятно что, факт."
    "Я бросил последний взгляд на здание."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    window show
    "Ворота скрылись из виду, а направление я забыл. Осталось брести дальше."
    "По обе стороны дорожки расположились, очевидно, те самые домики.{w} Непохоже, чтобы кто-то был внутри."
    "Как ни странно, все выглядело таким… уютным. Я никогда не был пионером, так что сравнивать было не с чем. Но представлял я пионерлагерь несколько по-другому."
    "Атмосферные гнилые деревянные бараки, внутри, разумеется — скрипучие ржавые койки. Глупые, взятые с потолка правила. Сигареты как валюта. Подъем в шесть утра, построение…"
    
    play sound sfx_punch_medium

    with vpunch
    
    "Хотя ни там, ни там я не был, так что мог и перепутать."
    "Не успел я так подумать, как получил сильный удар в спину."
    "Я пошатнулся, Но устоял."
    th "Ну, вот и дедушки…"
    
    show dv angry pioneer2 at center   with dissolve
    
    "Девочка… опять."
    "Я опять уставился, вконец потерянный."
    "Все та же пионерская форма, хотя и надетая, мягко говоря, иначе."
    "Я мог бы назвать ее настоящей красавицей, если б не по-настоящему злобный взгляд."
    dv "Челюсть с пола подними."
    dv "Новенький, значит?"
    me "…"
    show dv normal pioneer2 at center   with dspr
    dv "Черт с тобой, иди, куда шел!"
    "Пихнув меня плечом, она прошла мимо."
    
    hide dv  with dissolve
    
    "Я не хотел признавать, что боюсь девочки младше меня лет на пять, однако счел нужным подождать, пока она скроется за поворотом."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "Я вышел на безлюдную площадь."
    th "Куда же мне сказала идти та девчонка?{w} Налево...{w} нет, направо?"
    th "Пусть будет направо. Я везучий."
    
    window hide
    $ persistent.sprite_time = 'day'
    scene bg ext_path_day 
    with dissolve

    stop music fadeout 5

    window show
    "Через небольшой пролесок..."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = 'day'
    scene bg ext_boathouse_day 
    with dissolve

    play ambience ambience_boat_station_day fadein 5

    window show
    "Я вышел на пристань."
    th "Везучий, как же."
    "Я уже собирался повернуть назад, как…"
    sl "Ой, так тебе не сюда!"

    play music music_list["take_me_beautifully"] fadein 5

    show sl smile swim at center   with dissolve

    "Передо мной стояла светловолосая девочка, которую я встретил самой первой."
    sl "Я же тебе сказала повернуть налево на площади, а ты куда пошел?"
    sl "Ой, я же так и не представилась!{w} Меня Славя зовут!"
    sl "Вообще, полное имя Славяна, но все зовут Славей."

    $ meet('sl', u"Славя")

    me "А… да…"
    "Ее купальник несколько мешал обстановке. Я не мог собраться с мыслями."
    sl "А тебя?"
    "Казалось, ее взгляд пронизывает меня насквозь."
    me "А… я… да… Семен…"

    show sl smile2 swim at center   with dspr

    sl "Очень приятно, Семен."
    sl "Ладно, я уже заканчиваю.{w} Ты подожди меня тут минутку, я сейчас переоденусь, и вместе пойдем к Ольге Дмитриевне, хорошо?"
    me "Хорошо…"
    hide sl  with dissolve
    "В ожидании я уселся на мостик, свесив ноги в воду."
    th "Это не слишком похоже на похищение."
    sl "Пошли?"
    show sl smile pioneer at center   with dissolve
    "Я обернулся. Передо мной стояла Славя, вновь одетая в пионерскую форму."
    me "Пошли…"
    "Почему-то я был уверен, что на нее можно положиться."

    stop ambience fadeout 4

    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "Мы вышли обратно на площадь."

    show dv smile pioneer2 far at left    with dissolve   
    show us grin sport far at right    with dissolve

    "Теперь по ней бегали «СССР» и девочка, ударившая меня по спине."

    show sl angry pioneer at center   with dissolve

    sl "Ульяна, хватит бегать! Я все Ольге Дмитриевне расскажу!"

    $ meet('us', u"Ульяна")

    show us laugh sport far at right   behind sl  with dspr

    us "Есть, гржнинначаник!"
    "Обе девочки убежали."

    hide dv 
    hide us 
    with dissolve
    show sl normal pioneer at center   with dspr

    "Я решил пока не задавать Славе лишних вопросов."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    stop music fadeout 5

    play ambience ambience_camp_center_day fadein 5

    window show
    "Мы остановились перед домиком вожатой."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    "Если от всего лагеря веяло уютом, то домик был его воплощением. Пышные кусты сирени довершали картину."
    "Один из тех домиков, в которых принято хотеть прожить до старости."

    show sl normal pioneer at center   with dissolve

    sl "Ну что, пошли?"
    mt_voice "… и хватит издеваться над Реной…"
    window hide

    play sound sfx_scary_sting
    scene cg d1_rena_sunset 

    with vpunch
    with hpunch

    $ renpy.pause(2)

    window show
    "Реной?!"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    show sl normal pioneer at center 
    with dissolve

    window show
    play sound sfx_open_dooor_campus_1 fadein 0

    show us grin sport far at left   behind sl  with dissolve   

    "Внезапно из домика выскочила Ульяна и, все так же хитро скалясь, унеслась в неизвестном направлении."

    hide us  with dissolve
    show un normal pioneer far at left   behind sl  with dissolve   

    "За ней я увидел еще одно знакомое лицо. Бедняжка выглядела еще печальнее, чем прежде."
    sl "Лена, не обижайся ты на нее!"

    $ meet('un', u"Лена")

    th "Значит, Лена? Годы в наушниках не пощадили мой слух."

    show un shy pioneer at left  behind sl  with dissolve

    un "Да я не…"
    "Она покраснела, и, потупив взгляд, прошла мимо."

    hide un  with dissolve

    "Я неосознанно обернулся, но Славя сказала:"

    stop ambience fadeout 3

    sl "Пойдем."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_house_of_mt_day 
    with dissolve

    play music music_list["smooth_machine"] fadein 5

    window show
    "Внутри домик выглядел именно так, как можно было предположить по фасаду."
    "Ничего особенного, но казалось, что все здесь прямо-таки кричит «Уют!». Как будто к бабушке приехал. Правда, в плане порядка комнатка недалеко ушла от моей квартиры."

    show mt normal pioneer far at center    with dissolve   

    "Возле окна стояла девушка. Старше прочих. Я бы дал ей лет двадцать пять."
    th "Эта фигура..."
    mt "Пришел-таки!{w} Отлично!{w} Меня Ольга Дмитриевна зовут, я вожатая."
    th "Этот голос..."

    $ meet('mt', u"Ольга Дмитриевна")

    me "Очень приятно, я Семен."

    show mt normal pioneer at center   with dissolve

    "Она подошла ближе. Слишком близко."
    mt "Мы тебя с утра ждем."
    me "Ждете? Меня?.."
    show mt smile pioneer at center   with dspr
    mt "Да, конечно!"
    me "А где мы находимся?{w} Ну, в смысле, какой адрес?"

    show mt surprise pioneer at center   with dspr   

    me "Я родителям хочу письмо написать, что удачно добрался."

    show mt normal pioneer at center   with dspr

    mt "Так мне твои родители полчаса назад звонили! Тебе привет передавали."
    th "Ага…"
    me "О, значит, я могу им позвонить! Я забыл сказать кое-что перед отъездом!"

    show mt smile pioneer at center   with dspr

    mt "У нас телефона нет."
    me "…"
    me "Но мои родители...полчаса назад?"
    mt "Я только из райцентра вернулась, там с ними и поговорила."
    th "Угу. Все интереснее."
    me "А мне можно как-нибудь в этот райцентр?"
    mt "Нет."
    "Она все так же улыбалась."
    me "Кхм...почему?"
    mt "Потому что следующий автобус будет только через неделю."
    "Как она тогда сумела добраться туда и обратно, я решил не спрашивать. Уже очевидно, что ответа я бы не получил."
    show mt normal pioneer at center   with dspr
    show sl normal pioneer at right   with dissolve
    "Все это время Славя стояла рядом со мной и, казалось, не находила в нашем диалоге ничего особенного."

    show mt surprise pioneer at center   with dspr

    mt "Ой, надо тебе форму подобрать!"
    "Вряд ли шорты подойдут моей (пробивающейся) бороде, но ходить минимум неделю в зимней одежде мне не улы–балось также."
    me "Да, спасибо…"

    show mt smile pioneer at center   with dspr

    mt "Ладненько, я побежала, а ты пока можешь осмотреть лагерь!{w} Вечером приходи на ужин, не забудь!"

    hide mt  with dissolve

    "С этими словами она вышла из домика."

    show sl smile pioneer at right  #TODO# with dspr

    "Я остался наедине со Славей."
    sl "Мне тоже пора — дела."
    sl "Ты походи, осмотрись.{w} Вечером увидимся."

    hide sl  with dissolve

    th "Похоже, ответы не дадутся мне просто так. И что за дела?" 

    stop music fadeout 5

    th "Возможно, стоит поспрашивать других."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show
    "Проходя мимо домиков, я не без удивления заметил идущего навстречу пионера."
    show el normal pioneer far at center    with dissolve
    "Именно пионера. Это был единственный юноша за сегодня."

    play music music_list["eat_some_trouble"] fadein 2

    el "Привет, ты новенький? Семен, верно?"
    me "Да, а ты откуда…"

    show el grin pioneer at center   with dissolve 

    el "Да уже все знают! Я, кстати, Электроник. Настоящий. Можешь так меня и звать."

    $ meet('el', u"Электроник")

    th "Электроник. Настоящий. Великолепно…"
    me "М-м, ясно…"

    show el smile pioneer at center   with dspr

    el "Ульянка меня еще Сыроежкой зовет."
    me "Сыроежкой?"
    el "Фамилия у меня такая — Сыроежкин."
    me "М-м, ясно…"
    el "Давай я тебе тут все покажу!"
    "Почему бы и нет?"
    me "Давай, буду рад."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "Похоже, площадь служила центром общественной жизни лагеря."
    "На одной из лавочек сидела Лена и читала книжку.{w} Электроник уверенным шагом подошел к ней."

    show el normal pioneer at cleft   with dspr
    show un normal pioneer at cright   with dspr
    with dissolve

    el "Лена, привет! Это новенький, Семен, знакомься!"
    "Бойко начал он."
    me "Привет.{w} Ну, мы уже заочно знакомы."
    show un shy pioneer at cright   with dspr
    un "Да…"
    "Она на секунду посмотрела на меня, покраснела и вновь уткнулась в книгу."
    el "Ладно, пойдем дальше."
    th "Я слегка опешил от его напора."
    me "Пошли."
    window hide

    stop music fadeout 5

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    show el normal pioneer at center   with dissolve

    el "А вот это…"
    me "Столовая, не правда ли?"


    show el smile pioneer at center   with dspr
    show el normal pioneer at center   with dspr
    show dv normal pioneer2 far at left    with dissolve   

    "На крыльце столовой околачивалась та, что недавно врезала мне по спине."
    "Только ее сейчас не хватало."

    show el scared pioneer at center   with dspr

    el "Алиса Двачевская. Всегда в плохом духе."

    $ meet('dv', u"Алиса")

    "Он говорил шепотом."

    stop ambience fadeout 2

    el "А назовешь ее ДваЧе, так вообще закипит!"

    play music music_list["awakening_power"] fadein 2

    show dv angry pioneer2 far at left   with dspr

    "Непонятно как услышав нас, Алиса сиганула с крыльца."

    show el shocked pioneer at center   with dspr

    el "Ну...э-э...ладно, дальше  ты сам как-нибудь…"
    "Пробормотав еще что-то, Электроник бросился бежать."

    hide el  with dissolve
    window hide

    menu:

        "Побежать за ним":
            stop music fadeout 3

            window show
            "Отложив разговор с Алисой до лучших времен, я поспешил вслед за ним."
            window hide

            $ persistent.sprite_time = 'day'
            scene bg ext_square_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 5

            window show
            "Добежав до площади, я уже потерял Электроника из виду."
            "Двачевской также здесь не было."
            th "Зря. Ну агрессивная...{w} Но зачем бежать-то было?.."

            stop ambience fadeout 2

            "Сев на ближайшую лавку, я некоторое время оправдывался перед собой."
        "Ничего не делать":
            $ lp_dv = (lp_dv) + (1)
            show dv angry pioneer2 at left   with dissolve
            window show
            "Поравнявшись со мной, она бросила на меня злобный взгляд:"
            dv "А с тобой я еще поговорю!"
            me "Но я же..."
            "Однако Алисы рядом уже не было."

            stop music fadeout 5

            hide dv  with dissolve

    "..."
    window hide

    with fade

    window show
    "Похоже, оставшееся время до ужина мне предстояло коротать в одиночестве."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_playground_day 
    with dissolve

    play ambience ambience_soccer_play_background fadeout 2

    play music music_list["went_fishing_caught_a_girl"] fadein 5

    window show
    "Спустя некоторое время я оказался около футбольного поля."
    "Матч был в разгаре."
    "Я решил немного понаблюдать издали."
    "Дети резво носились по полю. Особенно выделялась одна девочка."
    th "Девочка…{w} Ульяна!"
    th "Ну, этого стоило ожидать."
    "Должно быть, я выглядел так глупо, что она признала меня издали."

    show us laugh sport far at center    with dissolve   

    us "Эй, ты!"
    us "Играть будешь?"
    "Я не знал, что ответить. Никогда тяготел к футболу — видимо, взаимно, — хотя в школе пришлось научиться."
    me "В другой раз!"

    hide us  with dissolve

    stop music fadeout 5

    "Она что-то вопила мне вслед, но я не стал вслушиваться."
    window hide

    stop ambience fadeout 2

    scene bg black 
    with dissolve2

    play ambience ambience_camp_center_evening fadeout 2

    window show
    "..."
    "Жаркий день постепенно перетекал в не менее жаркий вечер."
    "..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve2

    window show
    "В который раз за сегодня я обнаружил себя на площади."
    th "Плана нет. Сведений нет. "
    th "Вожатая знает, видимо, много, но говорит мало."
    th "Все остальные ведут себя предельно естественно, что позволяет считать, что они здесь добровольно."
    th "Или, возвращаясь к моей гипотезе психотронной тюрьмы, они тут так давно, что уже привыкли."
    th "Со мной будет так же? Забуду, кто я, откуда, начну отзываться на глупое имя?.."
    th "Я так подумал, как будто что-то хорошее оставил позади."
    th "Мое имя и так никогда мне не нравилось, хотя в последнее время даже стало редким."
    th "Завтра я с новыми силами приступлю к поиску ответов."

    play sound sfx_dinner_jingle_speaker

    "Из динамиков заиграла музыка."
    th "Сигнал к ужину?"
    "Я поспешил к столовой."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    stop sound fadeout 2

    window show
    "На крыльце стояла Ольга Дмитриевна."

    show mt normal pioneer far at center    with dissolve   

    "..."

    show mt normal pioneer at center   with dissolve

    mt "Семен, что стоишь? Проходи!"
    "Желудок отнюдь не возражал."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 5

    window show
    "Мы вместе зашли внутрь."
    "До переплавки в титан я бывал в заводской столовой…{w} Эта была почти неотличима, разве что почище и поно-вее."
    "Ну, и контингент несколько другой."

    show mt normal pioneer at center   with dissolve

    mt "Семен, сейчас мы тебе место найдем…"
    "Она окинула взглядом помещение."

    show mt rage pioneer at center   with dspr

    mt "Стой, Двачевская!"
    "Ольга Дмитриевна прикрикнула на проходящую мимо Алису."

    show dv normal pioneer2 at left   with dissolve

    dv "А что такое?"
    mt "Ты как одета?"
    dv "А как я одета?"
    mt "Немедленно приведи в порядок форму!"

    show dv sad pioneer2 at left   with dspr

    dv "Ладно-ладно…"
    show dv normal pioneer at left   with dissolve
    "Алиса поправила рубашку и прошла мимо, косо глянув на меня."

    hide dv  with dissolve

    show mt normal pioneer at center   with dspr

    mt "Итак, куда бы нам тебя посадить?"
    "Она обвела взглядом столовую."
    mt "Давай вот сюда, к Ульяне!"

    show mt smile pioneer at center   with dspr

    "Мне не оставалось ничего другого, кроме как согласиться."
    "В конце концов, все, что мне хотелось — это поскорее поесть."

    play music music_list["i_want_to_play"] fadein 0

    "Я повернулся к своей тарелке и обнаружил, что котлета пропала."

    show us grin pioneer at center   with dissolve

    me "Отдай котлету!"
    us "В большой семье клювом не щелкай!"
    me "Ах ты!.."
    window hide

    menu:
        "Попытаться отнять котлету":
            $ lp_us = (lp_us) + (1)
            window show
            "Я грозно посмотрел на нее и уже было вытянул вперед руку..."
        "Ничего не делать":
            window show

    us "Нету у меня ее, смотри!"
    "Действительно, ее тарелка была пуста …"

    show us laugh pioneer at center   with dspr

    us "Ты не расстраивайся, сейчас что-нибудь придумаем!"

    hide us  with dissolve

    "Молниеносным движением она схватила мою тарелку и куда-то слиняла."
    "В один миг я лишился и котлеты, и гарнира."
    "Спустя пару минут Ульяна вернулась с котлетой."
    window hide

    scene cg d1_food_normal 
    with dissolve

    window show
    us "Держи."
    me "Спасибо…"
    th "Хотя за что?"

    stop music fadeout 3

    "Многочасовой голод дал о себе знать. Не тратя больше времени на Ульяну, я бодро подцепил вилкой котлету и…"
    window hide

    scene cg d1_food_skolop 
    with vpunch

    play music music_list["doomed_to_be_defeated"] fadein 0

    window show
    th "Она живая! Живая! "
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day 
    with dissolve

    play sound sfx_broken_dish
    play sound2 sfx_dropped_chair

    window show
    "Я с детским визгом рухнул на кафельный пол."

    show us laugh2 pioneer far at center    with dissolve   

    "Ульяна уже стояла далеко у выхода и заливалась радостным детским смехом."

    stop ambience fadeout 2

    "Тихо бубня ругательства вперемежку с молитвами о безвременно ушедшей от меня тарелке, я ринулся вслед за девчонкой."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Мы выбежали из столовой."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "Мы пробежали мимо площади…"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day 
    with dissolve

    window show
    "…Помещения клубов…"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_path_day 
    with dissolve

    window show
    "…Выбежали на лесную тропинку."

    stop music fadeout 5

    "Я потерял Ульяну из виду."
    th "Не смог догнать маленькую девочку!"
    th "Не смог…"
    "Ффффу-ф."
    "..."
    window hide

    with fade2

    window show
    "Стемнело."
    th "Дорогу в раже не запомнил. Придется наугад."
    "..."
    window hide

    with fade2

    window show
    "..."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg ext_no_bus_sunset 
    with dissolve2

    $ sunset_time()

    play ambience ambience_camp_center_evening fadein 2

    window show
    "Через некоторое время я вышел к воротам лагеря."
    me "Автобус исчез..."
    th "Не думаю, что мне позволили бы уехать на нем, в любом случае."
    "Кстати, водителя я так и не видел."
    th "Чертовщина какая-то."
    window hide

    with fade2

    window show
    "..."
    "Был поздний вечер, и искать впотьмах не имело смысла."

    stop ambience fadeout 2

    "..."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_no_bus_night 
    with dissolve2

    $ night_time()

    play ambience ambience_camp_center_night fadein 2

    window show
    "Внезапно…"
    
    show sl normal pioneer at center   with dissolve
    
    sl "Привет, что тут так поздно делаешь?"
    "Я вздрогнул. Сегодняшний день не пошел на пользу моим нервам."
    
    show sl smile pioneer at center   with dspr
    
    sl "Не догнал Ульяну?"
    "Я кивнул."
    
    sl "Неудивительно.{w} Никто еще не догонял."
    
    show sl normal pioneer at center   with dspr
    
    sl "Ты, наверное, есть хочешь, поужинать-то тебе не удалось…"

    play sound sfx_stomach_growl channel 7

    th "Еще как."
    
    show sl smile pioneer at center   with dspr
    
    sl "Ну, тогда пойдем."
    me "Уже поздно. Разве столовая не закрыта?"
    sl "Ничего, у меня ключи."
    me "Ключи?"
    sl "Да, у меня все ключи есть."
    sl "Я здесь вроде помощницы вожатой. Идем?"
    me "Да. Спасибо."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    window show
    "Когда мы вышли на площадь, Славя внезапно остановилась."
    
    show sl normal pioneer at center   with dissolve
    
    sl "Слушай, мне надо соседку предупредить, что я вернусь позже, а то она такая пунктуальная — будет волноваться."
    sl "Ты иди пока, а я через минутку, хорошо?"
    me "Да…"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_away_night 
    with dissolve

    window show
    "К моему удивлению, у двери столовой уже кто-то был."

    play sound sfx_campus_door_rattle

    "И явно пытался открыть дверь. Безуспешно."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_near_night 
    with dissolve

    window show
    "Я, тактично стараясь топать погромче, поднялся на крыльцо."
    
    show dv normal pioneer at center   with dissolve
    
    "Алиса."
    "Некоторое время она сверлила меня взглядом. Затем сказала:"
    dv "Что стоишь, помоги, что ли!"
    me "Что?"
    
    show dv angry pioneer at center   with dspr
    
    dv "Что-что… Дверь открыть, что!"
    me "Зачем?"
    dv "Сам угадаешь, или помочь?"
    me "Э-э…{w} А может, не стоит все же?"
    
    show dv smile pioneer at center   with dspr
    
    dv "Сам жрать не хочешь, а? "
    "Она ехидно ухмыльнулась."
    me "Так сейчас Славя придет и…"
    
    show dv rage pioneer at center   with dspr
    
    dv "ЧЕГО?!"
    th "Похоже, я нарушил табу?.."
    
    show dv angry pioneer at center   with dspr
    
    dv "С тебя я еще спрошу!{w} Уже второй твой косяк!"
    "С этими словами она скрылась в ночи."
    
    hide dv  with dissolve
    
    th "...{w} Когда был первый?"
    window hide

    with fade

    window show
    "Через некоторое время пришла Славя."
    
    show sl normal pioneer at center   with dissolve

    stop ambience fadeout 2

    sl "Ну что, пойдем?"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg int_dining_hall_night 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    "Мы зашли в темную столовую."
    
    show sl normal pioneer at center   with dissolve
    
    sl "Подожди здесь, я сейчас что-нибудь принесу."
    
    hide sl  with dissolve
    
    "Дневные злоключения буквально обессилили меня. Я впервые за долгое время сел, ощущая усталость, а не как альтернативу лежанию."
    window hide

    show cg d1_sl_dinner 
    with dissolve

    window show
    "Ужин был нехитрым: несколько булочек и стакан кефира."
    "Не то чтобы мой обычный ужин чем-то превосходил сегодняшний."
    "Пока я ел, Славя сидела напротив, наблюдая."
    me "Что-то у меня на лице?"

    show cg d1_sl_dinner_0  with dspr

    sl "Нет, просто…"
    "Она улыбнулась."
    sl "И как тебе первый день в лагере?"
    me "Ну, я даже не знаю…"
    sl "Ничего, скоро привыкнешь!"

    show cg d1_sl_dinner  with dspr

    "Славя мечтательно уставилась в окно."
    th "Привыкну..."
    th "Как привыкли все они? Или же..."
    me "Ну а так, вообще, здесь мило."
    "Сказал я, пытаясь прервать неловкое молчание."
    sl "Да?"
    "Без интереса спросила она."
    me "Да. Здесь так..."
    "Хотелось сказать «необычно», но я сдержался."
    "Обитатели лагеря, очевидно, не замечали ничего необычного.{w} Или не показывали виду."
    sl "Как?"
    "Она вдруг внимательно посмотрела на меня.{w} Так, как будто от моего ответа зависело что-то серьезное."
    me "…Уютно. Очень уютно."

    show cg d1_sl_dinner_0  with dspr

    sl "Пожалуй."
    "Она вновь улыбнулась."

    show cg d1_sl_dinner  with dspr

    sl "Прости, надо было показать тебе лагерь, а я совсем забегалась сегодня."
    me "Да я сам… вроде осмотрел все."
    th "Пляж, футбольное поле… ведь так было во всех пионерлагерях?"
    "Было… Меня вдруг осенило."
    "Возможно ли, что я попал в прошлое?"
    "Да, это бы все объяснило."
    me "А можно задать глупый вопрос?"
    sl "Да, конечно, но..."
    window hide

    stop music fadeout 5

    $ persistent.sprite_time = 'night'
    scene bg int_dining_hall_night 
    show sl normal pioneer at center 
    with dissolve

    window show
    "Славя быстро встала из-за стола."
    sl "Ой, уже так поздно... Сам дорогу до Ольги Дмитриевны найдешь?"
    me "Найду, конечно, но зачем?"
    sl "В домик подселит к кому-нибудь."
    sl "Ладно, я побежала тогда.{w} Спокойной ночи!"
    me "Спокойной..."

    hide sl  with dissolve

    th "Это мое воображение, или она убежала слишком внезапно? И именно когда..."
    "Мое внимание привлекла связка ключей, торчавшая из двери."
    "Я хотел было броситься за Славей, но рассудил, что понятия не имею, где она живет."
    window hide

    menu:
        "Взять ключи":
            window show
            $ d1_keys = True
            th "Возьму с собой, а завтра отдам."
            window hide
        "Не трогать":
            window show
            th "Потеряю еще. Пусть тут будут."
            window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_near_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 5

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    window show
    "Проходя мимо площади, я с удивлением увидел Лену. Она, как и днем, читала."

    play music music_list["lets_be_friends"] fadein 5

    show un normal pioneer far at center    with dissolve   
    show un normal pioneer at center   with dissolve
    
    me "Э-э...привет, читаешь, да?"
    
    show un surprise pioneer at center   with dspr
    
    "Лена от удивления аж подпрыгнула на лавочке."
    me "И-извини, не хотел тебя напугать!"
    
    show un shy pioneer at center   with dspr
    
    un "Ничего…"
    "Она покраснела и снова уставилась в книжку."
    me "Что читаешь?"
    "Она показала обложку — «Унесенные ветром»."
    window hide

    menu:
        "Похвалить книгу":
            $ lp_un = (lp_un) + (1)
            window show
            me "Хорошая книжка…"
            un "Спасибо…"
            th "Даже мне было ясно, что в таком случае положено спросить, читал ли, но она промолчала."
        "Ничего не говорить":
            window show
            pass

    "Лена, похоже, не собиралась продолжать разговор."
    
    show un normal pioneer at center   with dspr
    
    me "Я присяду?"
    
    show un surprise pioneer at center   with dspr
    
    un "Зачем?"
    th "Действительно — зачем? Не похоже, чтобы я мог у нее хоть что-то выпытать."
    "После такого разговора мне меньше всего хотелось вообще находиться здесь, но и встать и уйти было как-то не-удобно."
    me "Как-то нехорошо получилось..."
    "Лена ничего не ответила."
    "Я выставил себя дураком. Одно из моих хобби, похоже."
    "Будь на ее месте, допустим, Ульянка, наверняка бы меня засмеяла."
    me "А тебе здесь нравится?"
    "Я вспомнил вопрос Слави и решил, что он как нельзя лучше подойдет для начала разговора."
    
    show un smile pioneer at center   with dspr
    
    un "Да."
    "Она едва заметно улыбнулась."
    
    show un normal pioneer at center   with dspr
    
    "Было очевидно, что Лена не станет непринужденно болтать ни о чем, как Славя."
    "Но в то же время было в ней что-то особенное."
    "Что-то незаметное на первый взгляд, но такое родное и естественное. Это как узнавать через несколько лет в тексте отрывок пасты, написанной тобой."
    
    show un shy pioneer at center   with dspr
    
    un "Поздно уже, мне пора…"
    me "Да, поздновато…"
    un "Спокойной ночи."
    me "Спокойной…"
    
    hide un  with dissolve

    stop music fadeout 5
    "..."
    window hide

    with fade2

    window show

    stop ambience fadeout 2

    "Я снова направился к домику вожатой."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_house_of_mt_night 
    with dissolve
    
    $ persistent.sprite_time = 'sunset'
    scene bg int_house_of_mt_noitem_night 
    with dissolve

    play music music_list["smooth_machine"] fadein 5

    show mt normal pioneer at center   with dissolve

    window show

    mt "Привет, Семен!{w} Что-то ты долго!"
    "Спать будешь здесь."
    "Она указала на одну из кроватей."
    me "Здесь?.."
    "Я недоверчиво моргнул."
    
    show mt surprise pioneer at center   with dspr
    
    mt "Ну да, а что такого?{w} Все равно других свободных мест нет."
    
    show mt smile pioneer at center   with dspr
    
    "А теперь спать!"
    "Я подивился ее безразличию в вопросе права и лева, но недолго — слишком хотел спать."
    window hide

    stop music fadeout 5

    scene bg black 
    with fade2

    window show
    "Я рухнул на кровать. В голове теснились впечатления дня."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_bus 
    show prologue_dream 
    with fade

    window show
    "Автобус..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    show prologue_dream 
    with fade

    window show
    "Площадь. Памятник..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day 
    show us laugh pioneer at center 
    show prologue_dream 
    with fade

    window show
    "Столовая, полная народу...{w} Довольное лицо Ульяны."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_boathouse_day 
    show sl smile swim at center 
    show prologue_dream 
    with fade

    window show
    "Славя..."
    window hide

    scene bg ext_square_night 
    show un night at center 
    show prologue_dream 
    with fade

    window show
    "Лена..."
    window hide

    scene bg ext_houses_day 
    show dv angry pioneer2 at center 
    show prologue_dream 
    with fade
    $ persistent.sprite_time = 'day'

    window show
    "Алиса..."
    window hide

    scene black 
    with fade3

    window show
    th "А почему я вообще хочу выбраться отсюда?"
    window hide

    $ renpy.pause(3)

    jump day2_main1

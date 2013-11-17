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
    "Я проснулся, почувствовав согревающее прикосновение солнца."
    "Что-то было не так."
    "Я машинально подскочил и ринулся к двери."
    me "Черт, моя остановка!"
    "Но двери не было…"
    "Я оглядел автобус и понял, что это не привычный мне потрепанный ЛИаЗ, а самый настоящий Икарус!"
    "На несколько мгновений я утратил связь с реальностью."
    th "Как?..{w} Что?..{w} Но я же?.."
    th "Меня похитили?"
    th "Нет, я...умер?"

    play sound sfx_punch_medium

    with vpunch
    "Я недоверчиво хлопнул себя по щеке. Не сочтя это достаточной проверкой, я с силой приложился о подголовник кресла."
    "Очевидно, способность воспринимать внешние раздражители меня не покинула."
    th "Итак, все же похищение?"
    th "Крайне сомнительно. Я не уверен, что нужен хотя бы своим родным."
    th "Но факт есть факт - меня вывезли черт знает куда, пока я спал."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_bus 
    with dissolve

    window show
    "Выбравшись наружу, я огляделся."
    "Мое окружение не оставляло мне большого простора для мыслей."
    th "Лето!{w} Настоящее хреново лето!{w} Невозможно..."
    "Я приложил руку ко лбу{w} Голова ужасно болела."
    "Постепенно в ней проявлялись воспоминания."
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
    "Длинная дорога, кажущаяся бесконечной, леса и поля, сливающиеся в единое желто-зеленое месиво."
    "Девушка...{w} Она говорила мне что-то!"

    stop ambience fadeout 3

    "Боль в голове была нестерпимой."
    window hide

    $ renpy.pause(2)

    $ persistent.sprite_time = 'day'
    scene bg ext_bus 
    with fade2

    window show
    th "Эта девушка..."
    th "Галлюцинации?"
    "Чем больше я думал о ней, тем сильнее меня охватывало спокойствие.{w} Головная боль потихоньку отступала."
    th "Если она реальна, то, очевидно, она причастна к моему похищению."
    th "Не вижу никого вокруг."
    th "Это шанс. Нужно выбираться отсюда!"
    "Быстро прикинув в уме, я торопливо бросился в сторону, откуда, судя по всему, приехал автобус."

    stop music fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_road_day 
    with dissolve2

    play ambience ambience_ext_road_day fadein 3

    window show
    "..."
    "В конце концов, физические упражнения никогда не были моей сильной стороной."
    "Не пробежав и ста метров, я устало рухнул на землю."
    "Как бы то ни было, моя неоконченная стометровка позволила мне еще раз обдумать произошедшее."
    th "Я и правда собираюсь выбраться отсюда на своих двоих?"
    "Поверх успокаивающе-зеленых красок открывающегося мне пейзажа я не мог разглядеть ни одного строения."
    me "Никого в радиусе нескольких километров..."
    "Я узнавал дорогу, змеей вытянувшуюся к линии горизонта.{w} По этой дороге меня привезли сюда."
    th "Привезти меня сюда на автобусе - нереально."
    "Это, очевидно, не моя страна."
    "Это даже не мой чертов климатический пояс!"
    "Меня везли самолетом. Это единственное объяснение."
    "Сняли с моего автобуса, посадили в самолет, затем опять автобус и сейчас я...где?"
    "Я никогда не называл себя любителем природы.{w} Но сейчас я невольно наслаждался почти нереальной красотой моего окружения."
    "Солнце согревало мое бледное лицо, шелест листьев приятно успокаивал. Я испытал сильное желание просто лежать и смотреть, как по кристально-голубому небу лениво плывут облака."
    "Однако я не мог себе позволить этой роскоши."
    th "Что мне делать?"
    "Страх с новой силой захлестнул меня."
    th "Эти ЛЭП...по ним я смогу выйти к людям."
    "Хотя кто знает, как долго я могу идти по ним, не встретив ни одного населенного пункта?"
    "А ведь меня будут преследовать. Слишком много сил они затратили на мою доставку сюда!"
    "Я вздохнул. И вот я снова вернулся к первоначальному вопросу."
    "Зачем?{w} Зачем я вообще кому-то сдался?"
    th "До сегодняшнего дня у меня было предостаточно вопросов, на которые я не мог получить ответа.{w} Не стоит прибавлять к ним новые."
    "Я медленно направился назад к автобусу."
    "Страх ушел, осталась лишь какая-то безразличная решимость. Много ли мне терять?"


    "..."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_camp_entrance_day 
    with dissolve2


    window show
    "За автобусом пролегала виденная мной ранее кирпичная стена."
    "Над воротами красовалась нелепая надпись «Совенок»."
    "По бокам возвышались статуи, в которых легко можно было угадать пионеров."
    me "Заброшенный пионерский лагерь. Просто здорово."
    "По моей спине пробежал холодок."
    "В памяти проносились все виденные мной ужастики и прочитанные истории."
    th "Возможно, возвращаться сюда было не лучшим выбором."
    "Однако это место совсем не выглядело заброшенным – на воротах не было ни следа ржавчины, белоснежные статуи задорно сверкали на солнце."
    me "«Совёнок»…"
    th "И правда скрыта за вратами..."
    "Я, невольно стараясь ступать тише, направился к воротам."
    "Мне оставалось сделать последние пару шагов, как вдруг ворота приоткрылись, и мне навстречу вышла...{w} девочка?"
    show sl normal pioneer far at center      with dissolve
    "Девчонка лет четырнадцати. Длинные светлые волосы...{w} пионерская форма."
    th "Что ж, это было ожидаемо."
    th "Ну, по крайней мере, некоторая извращенная логика здесь присутствует."
    th "Впрочем, девочки {i}здесь{/i}..."
    "Все мои силы ушли на то, чтобы не завизжать при неожиданном появлении незнакомки, так что теперь я стоял, не смея пошевелить и рукой."
    show sl smile pioneer at center     with dissolve
    "Незнакомка подошла ближе. Я невольно отметил великолепие ее голубых глаз."
    sl "Привет, наверное, только что приехал?"
    window hide

    menu:
        "Не отвечать ей":
            window show
            "Я настороженно наблюдал за девчонкой."
            "От нее не исходило явной угрозы, но дураку понятно, что все здесь не так просто."
            th "Не стоит совершать необдуманных действий в этой ситуации."
            show sl normal pioneer at center     with dspr
            sl "Чего молчишь?"
            "Я как можно непринужденнее ответил:"
            me "Ну… да…"
        "Ответить":
            $ lp_sl = (lp_sl) + (1)
            window show
            me "Кхм, да, только что..."

    show sl smile2 pioneer at center     with dspr
    sl "Что же, добро пожаловать!"
    "Она широко улыбнулась."
    "Пока все шло неплохо...или?"
    th "Не стоило возвращаться. Нужно было идти по ЛЭП."
    "Я продолжал глупо смотреть на свою собеседницу. Титаническими усилиями я попытался выдавить из себя дружелюбную улыбку. "
    show sl normal pioneer at center     with dspr
    sl "Что смешного?"
    "Девочка окинула меня взглядом с ног до головы."
    "Я взрогнул и невольно отступил на шаг назад."
    me "Н... ничего..."
    show sl smile pioneer at center     with dspr
    sl "Ну и славно."
    th "Сомневаюсь. Но пора что-то предпринимать."
    me "А ты, наверное, знаешь…"
    show sl normal pioneer at center     with dspr
    sl "Тебе к вожатой надо сразу, она все расскажет!"
    sl "Смотри.{w} Сейчас идешь прямо-прямо, доходишь до площади, затем сворачиваешь налево, дальше будут палатки."
    "Она показала в сторону ворот, как будто я знал, что за ними."
    sl "Ну спросишь у кого-нибудь, где домик Ольги Дмитриевны!"
    me "Я… эээ…"
    sl "Надеюсь, все понял?"
    "Мои мысли путались."
    sl "А мне пора."
    hide sl  with dissolve
    "Девочка помахала мне рукой и скрылась за воротами."
    th "Вожатая, да?"
    th "Меня все меньше радует происходящее."
    th "Итак, вперед, навстречу ответам!"

    stop ambience fadeout 2

    "Я побрел в указанном направлении."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show
    "Метров через пятьдесят я наткнулся на небольшое одноэтажное здание.{w} Вывеска рядом с дверью гласила «Клубы»."
    "Ниже что-то было подписано неразборчивым почерком."

    stop music fadeout 5

    "Я уже было собирался подойти поближе..."

    play sound sfx_open_door_clubs fadein 0

    show un normal pioneer far at left     with dissolve   
    "Как дверь открылась, и оттуда вышла еще одна девочка в пионерской форме."
    "Мне сразу бросилось в глаза ее невероятно грустное лицо. Весьма симпатичное."
    "Девочка остановилась, неподвижно глядя в мою сторону."
    show un surprise pioneer far at left     with dspr
    "Я застыл на месте, думая, как лучше поступить."

    play music music_list["i_want_to_play"] fadein 5

    show us grin sport far at right     with dissolve 

    play sound sfx_bush_leaves fadein 0

    "Неожиданно из соседних кустов выскочила очередная девчонка. На этот раз совсем мелкая."
    "На ее ярко-красной майке гордо красовалась надпись «СССР»."
    th "У одной из них наверняка можно спросить направление."
    show un surprise pioneer far at left     with dspr
    show us surp3 sport far at right   

    "Тем временем девчонка в красной майке подскочила к грустной девочке и, энергично жестикулируя, начала что-то бойко той рассказывать."
    show un shy pioneer far at left     with dspr
    "Та явно смутилась и ничего не ответив, потупила взгляд."
    "Я, до того тактично стоявший в стороне, решил уже было приблизиться, как вдруг мелкая достала что-то из кармана и начала трясти этим перед лицом своей подруги."
    window hide

    scene cg d1_grasshopper 
    with dissolve

    window show
    un "Ииииии-иии-иииииии!"
    "По внешнему виду нельзя было и предположить, что голос этой девочки может быть настолько громким."
    "Пронзительный вопль затих вдали, когда его обладательница скрылась за поворотом."

    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day 
    show us grin sport at left   

    with dissolve

    "Мелкая посмотрела на меня, хитро улыбнулась и побежала за ней."
    hide us 
    th "Они выглядят...обычно?"
    th "Не знаю, что я собирался увидеть внутри лагеря, но явно не {i}это{/i}..."

    stop music fadeout 5

    "Мне ничего не оставалось, кроме как дальше брести наугад."
    th "Факт есть факт - на данный момент я не могу объяснить происходящее."
    "Я бросил последний взгляд на здание."

    th "Не похоже, чтобы там еще кто-то был..."
    "На свежем воздухе я чувствовал себя в относительной безопасности, так что до поры я постараюсь избегать неизвестных зданий."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    window show
    "Я продолжил свой путь в направлении, которое давно забыл."
    "По обе стороны дорожки расположились, очевидно, палатки местных обитателей.{w} Не могу сказать, был ли кто-то внутри."
    "Неожиданно, но все окружение выглядело таким...уютным. Я никогда не был пионером, так что мне не с чем было сравнивать. Но представлял я пионерлагерь несколько по-другому."
    "Хорошо прогнившие деревянные бараки, внутри - скрипучие и проржавевшие койки. Глупые, взятые с потолка правила. Сигареты как валюта. Подъем в шесть утра, построение..."
    th "Кхм, возможно, я что-то с чем-то путаю."

    play sound sfx_punch_medium

    with vpunch
    "В ту же секунду я получил сильный удар в спину."
    "Достаточно сильный, чтобы ощутимо пошатнуть меня. Но я устоял на ногах."
    th "Началось! Я так и знал!"
    "Вся моя уверенность в миг улетучилась. Ноги стали ватными и подкашивались. Кое-как я заставил себя обернуться."
    show dv angry pioneer2 at center     with dissolve
    "Девочка...опять."
    "С широко распахнутым ртом я уставился на новую знакомую."
    "Ожидаемая пионерская форма, хотя и сидящая на этот раз...вызывающе."
    "Я мог бы назвать ее настоящей красавицей, если б не явно читавшаяся в ее глазах злоба."
    dv "Челюсть с пола подними."
    dv "Новенький, значит?"
    me "…"
    show dv normal pioneer2 at center     with dspr
    dv "Черт с тобой, иди, куда шел!"
    "Пихнув меня плечом, она прошла мимо."
    hide dv  with dissolve
    "Я не хотел признавать, что боюсь девочки младше меня лет на пять, однако счел нужным подождать, пока она скроется за поворотом."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "Очевидно, я был на площади."
    "Если не брать в расчет меня, площадь была совершенно пуста."
    "В центре возвышался памятник неизвестному мне товарищу."
    th "Вероятно, партийный деятель или типа того."
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
    th "Везучий, да."
    "Я уже собирался повернуть назад, как…"
    sl "Ой, так тебе не сюда!"

    play music music_list["take_me_beautifully"] fadein 5

    show sl smile swim at center     with dissolve
    "Передо мной стояла светловолосая девочка, которую я встретил самой первой."
    sl "Я же тебе сказала повернуть налево на площади, а ты куда пошел?"
    "Пионерская форма на ней сменилась на купальник. Я сглотнул."
    sl "Ой, я же так и не представилась!{w} Меня Славя зовут!"
    sl "Вообще, полное имя Славяна, но все зовут Славей."

    $ meet('sl', u"Славя")

    me "А… да…"
    "Ее купальник несколько мешал обстановке. Я не мог собраться с мыслями."
    sl "А тебя?"
    "Казалось, ее взгляд пронизывает меня насквозь."
    me "А… я… да… Семен…"
    show sl smile2 swim at center     with dspr
    sl "Очень приятно, Семен."
    sl "Ладно, я уже заканчиваю.{w} Ты подожди меня тут минутку, я сейчас переоденусь, и вместе пойдем к Ольге Дмитриевне, хорошо?"
    me "Хорошо…"
    hide sl  with dissolve
    "В ожидании я уселся на мостик, свесив ноги в воду."
    "Не то, чтобы я боялся промокнуть в моей зимней обуви, в конце концов."
    th "Это не слишком похоже на похищение."
    th "Может, меня с кем-то перепутали?"
    th "Наверняка это какое-то недоразумение.{w} Надеюсь, все не будут слишком злиться, когда оно раскроется."
    sl "Пошли?"
    "Я обернулся."
    show sl smile pioneer at center     with dissolve
    "Рядом со мной стояла Славя, вновь одетая в пионерскую форму."
    me "Пошли…"
    "Почему-то эта девочка казалась мне очень...надежной."

    stop ambience fadeout 4

    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "Вследь за ней я вышел обратно на площадь."
    show dv smile pioneer2 far at left      with dissolve   
    show us grin sport far at right      with dissolve
    "Теперь по ней бегали «СССР» и девочка, ударившая меня по спине."
    th "Это у них игра такая?"
    show sl angry pioneer at center     with dissolve
    sl "Ульяна, хватит бегать! Я все Ольге Дмитриевне расскажу!"

    $ meet('us', u"Ульяна")

    show us laugh sport far at right    behind sl  with dspr
    us "Есть, гржнинначаник!"
    "Обе девочки убежали."
    hide dv 
    hide us 
    with dissolve
    show sl normal pioneer at center     with dspr
    "Я решил пока не задавать Славе лишних вопросов."
    th "Дождусь сперва встречи с этой...вожатой."
    th "Ольга Дмитриевна, верно?"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    stop music fadeout 5

    play ambience ambience_camp_center_day fadein 5

    window show
    "Пройдя через ряды палаток, мы остановились перед небольшим одноэтажным домиком."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    "Если от всего лагеря веяло уютом, то домик был самой его концентрацией. Пышные кусты сирени, обрамляющие его, довершали картину."
    "Один из тех домиков, в которых хочешь прожить до старости."

    show sl normal pioneer at center     with dissolve
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
    th "Хе-хе...невозможно, так ведь?"

    play sound sfx_open_dooor_campus_1 fadein 0

    show us grin sport far at left    behind sl  with dissolve   

    "Внезапно из домика выскочила Ульяна и, все так же хитро скалясь, унеслась в неизвестном направлении."
    hide us  with dissolve
    show un normal pioneer far at left    behind sl  with dissolve   
    "За ней я увидел еще одно знакомое лицо. Бедняжка выглядела еще печальнее, чем прежде."
    sl "Лена, не обижайся ты на нее!"

    $ meet('un', u"Лена")

    th "Значит, Лена? Годы в наушниках не пощадили мой слух."
    show un shy pioneer at left   behind sl  with dissolve
    un "Да я не…"
    "Она покраснела, и, потупив взгляд, прошла мимо меня."
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
    "Ничего особенного, но казалось, будто все здесь прямо-таки кричит «Уют!». Я отметил, что в плане порядка комнатка не сильно далеко ушла от моей квартиры."
    show mt normal pioneer far at center      with dissolve   
    "Возле окна стояла девушка. Старше прочих."
    "Я бы дал ей лет двадцать пять."
    th "Эта фигура..."
    mt "Пришел-таки!{w} Отлично!{w} Меня Ольга Дмитриевна зовут, я вожатая."
    th "Этот голос..."

    $ meet('mt', u"Ольга Дмитриевна")

    me "Очень приятно, я - Семен."
    show mt normal pioneer at center     with dissolve
    "Она подошла ближе. Слишком близко."
    mt "Мы тебя с утра ждем."
    me "Ждете? Меня?.."
    show mt smile pioneer at center     with dspr
    mt "Да, конечно!"
    me "А когда автобус следующий будет, а то я…"
    show mt surprise pioneer at center     with dspr
    mt "А тебе зачем?"
    th "Возможно, нужно действовать тоньше."
    th "Узнаю ситуацию. Узнаю, как отсюда выбраться."
    me "Нет-нет, простое любопытство!"
    me "А где мы находимся?{w} Ну, в смысле, какой адрес?"
    me "Я родителям хочу письмо написать, что удачно добрался."
    show mt normal pioneer at center     with dspr
    mt "Так мне твои родители полчаса назад звонили! Тебе привет передавали."
    th "Ага…"
    me "О, значит, я могу им позвонить! Я забыл сказать кое-что перед отъездом!"
    show mt smile pioneer at center     with dspr
    mt "Нет."
    "Она мило и непринужденно улыбнулась."
    me "...{w} Почему?"
    mt "А у нас телефона нет."
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
    show mt normal pioneer at center     with dspr
    show sl normal pioneer at right     with dissolve
    "Все это время Славя стояла рядом со мной и, казалось, не находила в нашем диалоге ничего особенного."
    show mt surprise pioneer at center     with dspr
    mt "Ой, надо тебе форму подобрать!"
    "Последнее, что я хотел - это наряжаться в пионерские шортики и завязывать нелепый красный галстук. Но идея продолжать ходить в зимней одежде мне также не импонировала."
    me "Да, спасибо…"
    show mt normal pioneer at center     with dspr
    th "Я один считаю, что ходить в такую погоду в зимнем плаще и ботинках - странновато?{w} Один, да..."
    show mt smile pioneer at center     with dspr
    mt "Ладненько, я побежала, а ты пока можешь осмотреть лагерь!{w} Вечером приходи на ужин, не забудь!"
    hide mt  with dissolve
    "С этими словами она вышла из домика."
    show sl smile pioneer at right   

    "Я остался наедине со Славей."
    sl "Мне тоже пора – дела."
    sl "Ты походи, осмотрись.{w} Вечером увидимся."
    hide sl  with dissolve
    th "Факт есть факт - ответов мне давать никто не собирается. Ладно, поживем - увидим."
    "С нервным смешком я отправился на осмотр территории."

    stop music fadeout 5

    th "Возможно, стоит попытаться задать вопросы кому-то еще."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show
    "Проходя мимо палаток, я не без удивления заметил идущего навстречу мне пионера."
    show el normal pioneer far at center      with dissolve
    "Именно пионера. Это был единственный встреченный мной за сегодня представитель мужского пола."

    play music music_list["eat_some_trouble"] fadein 2

    el "Привет, ты новенький? Семен, верно?"
    me "Да, а ты откуда…"
    show el grin pioneer at center     with dissolve 
    el "Да уже все знают! Я, кстати, Электроник. Настоящий. Можешь так меня и звать."

    $ meet('el', u"Электроник")

    th "Электроник. Настоящий. Великолепно…"
    me "М-м, ясно…"
    show el smile pioneer at center     with dspr
    el "Ульянка меня еще Сыроежкой зовет."
    me "Сыроежкой?"
    el "Фамилия у меня такая – Сыроежкин."
    me "М-м, ясно…"
    el "Давай я тебе тут все покажу!"
    "Определенные плюсы в его предложении были."
    me "Давай, буду рад."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day 
    with dissolve

    window show
    "И вновь я оказался на площади."
    "На одной из лавочек сидела Лена и читала какую-то книжку.{w} Электроник уверенным шагом подошел к ней."
    show el normal pioneer at cleft     with dspr
    show un normal pioneer at cright     with dspr
    with dissolve
    el "Лена, привет! Это новенький, Семен, знакомься!"
    "Бойко начал он."
    me "Привет.{w} Ну, мы уже заочно знакомы."
    show un shy pioneer at cright     with dspr
    un "Да…"
    "Она на секунду оторвала глаза от книжки, посмотрела на меня, покраснела и вновь принялась за чтение, очевидно стараясь не замечать наше присутствие."
    el "Ладно, пойдем дальше."
    "Даже я опешил от такого «знакомства», однако, принимая во внимание неуемную активность Электроника и явно бросающуюся в глаза скромность Лены...{w} Вероятно, по-другому бы не получилось."
    me "Пошли."
    window hide

    stop music fadeout 5

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Мы вышли к очередному строению, в котором я тут же опознал столовую."
    show el normal pioneer at center     with dissolve
    el "А вот это…"
    me "Столовая, не правда ли?"
    show el smile pioneer at center     with dspr
    show el normal pioneer at center     with dspr
    show dv normal pioneer2 far at left      with dissolve   
    "На крыльце столовой околачивалась та девка, что недавно врезала мне по спине."
    "Не тот человек, которого я сейчас хотел бы видеть."
    show el scared pioneer at center     with dspr
    el "Алиса Двачевская. Всегда в плохом духе."

    $ meet('dv', u"Алиса")

    "Он говорил шепотом."

    stop ambience fadeout 2

    el "А назовешь ее ДваЧе, так вообще закипит!"

    play music music_list["awakening_power"] fadein 2

    show dv angry pioneer2 far at left     with dspr
    dv "Ты что-то сказал?!"
    "Невероятно, но она услышала."
    "В мгновение ока Алиса спрыгнула с крыльца и метнулась в нашу сторону."
    show el shocked pioneer at center     with dspr
    el "Ну...э-э...ладно, дальше ты сам как-нибудь…"
    "Пробормотав еще что-то несвязное, Электроник бросился бежать."
    hide el  with dissolve
    window hide

    menu:

        "Побежать за ним":
            stop music fadeout 3

            window show
            "Решив, что сейчас не самое подходящее время для разговора с Алисой, я рванул вслед за ним."
            window hide

            $ persistent.sprite_time = 'day'
            scene bg ext_square_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 5

            window show
            "Выбежав на площадь, я понял, что потерял Электроника из виду."
            "Двачевской также здесь не было."
            "Отдышавшись, я ощутил нечто, похожее на стыд."
            th "Ну девочка... Ну агрессивная...{w} Но зачем бежать-то было?.."

            stop ambience fadeout 2

            "Сев на ближайшую лавку, я некоторое время оправдывался перед собой."
        "Ничего не делать":
            $ lp_dv = (lp_dv) + (1)
            show dv angry pioneer2 at left     with dissolve
            window show
            "Поровнявшись со мной, она бросила на меня злобный взгляд:"
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
    "Я неспеша побрел в противоположную от столовой сторону."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_playground_day 
    with dissolve

    play ambience ambience_soccer_play_background fadeout 2

    play music music_list["went_fishing_caught_a_girl"] fadein 5

    window show
    "Спустя некоторое время, я оказался около футбольного поля."
    "Там вовсю шел матч."
    "Я встал в сторонке и решил немного понаблюдать."
    "Когда-то давно, помнится, я весьма неплохо играл. Пока не решил, что все это вряд ли стоит падений и ушибов."
    "Дети резво носились по полю. Особенно выделялась одна девочка."
    th "Девочка…{w} Ульяна!"
    th "Ну, этого стоило ожидать."
    "Я стоял достаточно далеко от поля, но Ульяна все же заметила меня."
    show us laugh sport far at center      with dissolve   
    us "Эй, ты!"
    us "Играть будешь?"
    "Я не знал, что ответить."
    "Я не питал особой любви к футболу. Но сейчас делать мне было решительно нечего."
    "Однако навряд ли то, что было на мне, можно было назвать подходящей одеждой."
    me "В другой раз!"
    "Я развернулся и пошел назад."
    hide us  with dissolve

    stop music fadeout 5

    "Она что-то вопила мне вслед, но я сомневался в важности этого."
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
    th "Нет плана. Нет информации. Нет еды."
    th "Вожатая, очевидно, что-то скрывает."
    th "Все остальные ведут себя предельно естественно, что, учитывая их возраст, позволяет с уверенностью предположить, что они здесь добровольно."
    th "Или так давно, что уже привыкли."
    th "Ждет ли это и меня тоже?"
    th "Ну, посмотрим. Сейчас основная моя задача - поесть."
    th "Завтра я с новыми силами приступлю к поиску ответов."

    play sound sfx_dinner_jingle_speaker

    "Из динамиков заиграла музыка."
    th "Сигнал к ужину, быть может? Мое почтение Павлову."
    "Я поспешил к столовой."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    stop sound fadeout 2

    window show
    "На крыльце была Ольга Дмитриевна."
    show mt normal pioneer far at center      with dissolve   
    "..."
    show mt normal pioneer at center     with dissolve
    mt "Семен, чего стоишь? Проходи!"
    "Мой желудок явственно потребовал последовать ее совету."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 5

    window show
    "Мы вместе зашли внутрь."
    "Столовая представляла из себя…{w} столовую."
    "Одно время я частенько бывал в заводской столовой…{w} Эта была почти неотличима, разве что почище и поновее."
    "Ну, и контингент несколько другой."
    show mt normal pioneer at center     with dissolve
    mt "Семен, сейчас мы тебе место найдем…"
    "Она окинула взглядом помещение."
    show mt rage pioneer at center     with dspr
    mt "Стой, Двачевская!"
    "Ольга Дмитриевна прикрикнула на проходящую мимо Алису."
    show dv normal pioneer2 at left     with dissolve
    dv "А что такое?"
    mt "Ты как одета?"
    dv "А как я одета?"
    "Неплохо - невольно подумал я."
    mt "Немедленно приведи в порядок форму!"
    show dv sad pioneer2 at left     with dspr
    dv "Ладно-ладно…"
    show dv normal pioneer at left     with dissolve
    "Алиса поправила рубашку и прошла мимо, косо глянув на меня."
    hide dv  with dissolve
    show mt normal pioneer at center     with dspr
    mt "Итак, куда бы нам тебя посадить?"
    "Она обвела взглядом столовую."
    mt "Давай вот сюда, к Ульяне!"
    me "Это… А может…"
    show mt smile pioneer at center     with dspr
    mt "Да, точно, как раз уже и еда стоит!"
    "Мне не оставалось ничего другого, кроме как согласиться."
    "В конце концов, все что мне хотелось - это поскорее поесть."
    hide mt  with dissolve
    show us normal pioneer at center     with dissolve
    us "Эй!"
    "Я повернулся."
    me "Чего тебе?"
    show us dontlike pioneer at center     with dspr
    us "Почему с нами в футбол не стал играть?"
    me "Одежда не та."
    "Я указал на свое облачение."
    show us grin pioneer at center     with dspr
    us "А, ну тогда ладно, ешь."
    hide us  with dissolve

    play music music_list["i_want_to_play"] fadein 0

    "Я повернулся к своей тарелке и обнаружил, что котлета пропала."
    th "Дважды два равно четыре, параллельные линии не пересекаются, котлету сперла Ульяна!"
    show us grin pioneer at center     with dissolve
    me "Отдай котлету!"
    us "В большой семье клювом не щелкай!"
    me "Ах ты мелкая..!"
    window hide

    menu:
        "Попытаться отнять котлету":
            $ lp_us = (lp_us) + (1)
            window show
            "Я грозно посмотрел на нее и уже было вытянул вперед руку..."
        "Ничего не делать":
            window show

    us "Нету у меня ее, смотри!"
    "Действительно, ее тарелка была пуста – похоже, она уже все съела…"
    show us laugh pioneer at center     with dspr
    us "Ты не расстраивайся, сейчас что-нибудь придумаем!"
    hide us  with dissolve
    "Молниеностным движением она схватила мою тарелку и куда-то слиняла."
    "В один миг я лишился и котлеты, и гарнира. Моя жизнь - страдание."
    "Спустя пару минутту Ульяна вернулась с моей тарелкой, на которой лежала дымящаяся котлета."
    window hide

    scene cg d1_food_normal 
    with dissolve

    window show
    us "Держи, голодающий!"
    me "Спасибо…"
    "Хотя я не был уверен, что ее есть за что благодарить."

    stop music fadeout 3

    "Многочасовой голод дал о себе знать. Не тратя больше времени на Ульяну, я бодро подцепил вилкой котлету и…"
    window hide

    scene cg d1_food_skolop 
    with vpunch

    play music music_list["doomed_to_be_defeated"] fadein 0

    window show
    th "Ох, черт, это еще что за хрень?!{w} Она живая!!!"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day 
    with dissolve

    play sound sfx_broken_dish
    play sound2 sfx_dropped_chair

    window show
    "Я с детским визгом рухнул на кафельный пол. В паре метров от меня приземлилась тарелка."
    "Не то, чтобы я так боялся ползучей инопланетной дряни. Однако все было череcчур внезапно для моего голодного сознания."
    th "И каждому воздастся по делам его..."
    me "Ах ты, мелкая…"
    show us laugh2 pioneer far at center      with dissolve   
    "Ульяна уже стояла далеко у выхода и заливалась радостным детским смехом."

    stop ambience fadeout 2

    "Тихо бубня ругательства вперемежку с молитвами о безвременно ушедшей от меня тарелке, я ринулся вслед за девчонкой."
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Мы выбежали из столовой."
    "Между нами была пара десятков метров, но я не считал, что это будет проблемой."
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
    "Помещения клубов…"
    window hide

    $ persistent.sprite_time = 'day'
    scene bg ext_path_day 
    with dissolve

    window show
    "Выбежали на лесную тропинку."
    "Я начал задыхаться."
    th "Чертов Колумб! А, впрочем, виноват тут только я."

    stop music fadeout 5

    "Я потерял Ульяну из виду."
    th "Я не смог догнать маленькую девочку!"
    th "Не смог..."
    "Я стоял и пытался отдышаться."
    "..."
    window hide

    with fade2

    window show
    "Стемнело."
    th "Сомневаюсь, что знаю, куда идти."
    th "Придется наугад."
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
    "Я задумался о том, что обошел за сегодня весь лагерь, но водителя так и не видел."
    th "А был ли вообще водитель? Чертовщина какая-то."
    window hide

    with fade2

    window show
    "..."
    "Был поздний вечер и искать что-либо впотьмах не имело смысла."
    th "Нужно узнать, где здесь я смогу поспать."

    stop ambience fadeout 2

    "..."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_no_bus_night 
    with dissolve2

    $ night_time()

    play ambience ambience_camp_center_night fadein 2

    window show
    "Я уже собирался идти назад, как вдруг..."
    show sl normal pioneer at center     with dissolve
    sl "Привет, что тут так поздно делаешь?"
    "Я взрогнул."
    "Ох, это Славя. Сегодняшний день не пошел на пользу моим нервам."
    show sl smile pioneer at center     with dspr
    sl "Не догнал Ульяну?"
    "Она улыбнулась."
    "Я кивнул."
    sl "Неудивительно.{w} Никто не может."
    th "Впечатляет…"
    show sl normal pioneer at center     with dspr
    sl "Ты, наверное, есть хочешь, поужинать-то тебе не удалось…"

    play sound sfx_stomach_growl channel 7

    "Еще как. При одной лишь мысли о еде мой желудок мечтательно заурчал."
    show sl smile pioneer at center     with dspr
    "Славя улыбнулась."
    sl "Ну, тогда пойдем."
    me "Уже поздно. Разве столовая не закрыта?"
    sl "Да ничего, у меня ключи есть."
    me "Ключи?"
    sl "Да, у меня от всех помещений лагеря ключи есть."
    me "Почему?"
    sl "Ну, я здесь что-то вроде помощницы вожатой. Идем?"
    me "Да. Спасибо."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    window show
    "Когда мы вышли на площадь, Славя внезапно остановилась."
    show sl normal pioneer at center     with dissolve
    sl "Слушай, мне надо соседку предупредить, что я вернусь позже, а то она такая пунктуальная – будет волноваться."
    sl "Ты иди пока к столовой, а я через минутку, хорошо?"
    me "Да…"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_away_night 
    with dissolve

    window show
    "Неожиданно, но у двери столовой уже кто-то был."

    play sound sfx_campus_door_rattle

    "Этот кто-то явно пытался открыть дверь. Безуспешно."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_near_night 
    with dissolve

    window show
    "Я, тактично стараясь топать погромче, поднялся на крыльцо."
    show dv normal pioneer at center     with dissolve
    "Алиса."
    th "Возможно, стоило подождать в сторонке..."
    "Некоторое время она, прищурившись, смотрела на меня. Затем сказала:"
    dv "Че ты стоишь, помоги, что ли!"
    me "Что?"
    show dv angry pioneer at center     with dspr
    dv "Что-что… Дверь открыть, что!"
    me "Зачем?"
    dv "Сам угадаешь, или помочь?"
    me "Эээ…{w} А может, не стоит все же?"
    show dv smile pioneer at center     with dspr
    dv "А че, сам ты жрать не хочешь, а?{w} Ульянка-то тебе поужинать нормально не дала!"
    "Она ехидно ухмыльнулась."
    me "Так сейчас Славя придет и…"
    show dv rage pioneer at center     with dspr
    dv "ЧЕГО?!"
    th "Похоже, не стоило мне этого говорить."
    show dv angry pioneer at center     with dspr
    dv "Я сваливаю!"
    dv "А с тебя я еще спрошу!{w} Уже второй твой косяк!"
    "С этими словами она скрылась в ночи."
    hide dv  with dissolve
    th "...{w} Когда был первый?"
    window hide

    with fade

    window show
    "Через некоторое время пришла Славя."
    show sl normal pioneer at center     with dissolve

    stop ambience fadeout 2

    sl "Ну что, пойдем?"
    window hide

    $ persistent.sprite_time = 'night'
    scene bg int_dining_hall_night 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    "Мы зашли в темную столовую."
    show sl normal pioneer at center     with dissolve
    sl "Подожди здесь, я сейчас что-нибудь принесу."
    hide sl  with dissolve
    "Я обессилено упал на стул и принялся покорно ждать свою спасительницу."
    window hide

    show cg d1_sl_dinner 
    with dissolve

    window show
    "Ужин был нехитрым – несколько булочек и стакан кефира."
    "Не то, чтобы мой обычный ужин чем-то превосходил сегодняшний."
    "Пока я ел, Славя сидела напротив, смотря прямо на меня."
    me "Что-то у меня на лице?"

    show cg d1_sl_dinner_0  with dspr

    sl "Нет, просто…"
    "Она улыбнулась."
    sl "И как тебе первый день в лагере?"
    me "Ну, я даже не знаю..."
    "Сегодняшний день не был именно плохим. На самом деле, все, происходящее вокруг, меня...{w} радовало?"
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
    "Обитатели лагеря, очевидно, не находили ничего здесь необычным.{w} Ну, или не показывали виду."
    sl "Как?"
    "Она внимательно посмотрела на меня.{w} Так, как будто от моего ответа зависело что-то серьезное."
    me "Ну, я не знаю... уютно. Очень уютно."

    show cg d1_sl_dinner_0  with dspr

    sl "Пожалуй."
    "Она вновь улыбнулась."
    sl "Очень хорошо, что ты так думаешь."
    me "Почему?"
    sl "Ну, не всем здесь нравится..."
    me "А тебе?"
    sl "Мне?"
    me "Да..."
    sl "Нравится, тут здорово."
    "Славя тихо засмеялась."
    "Я поражался, как естественно себя ведут все здешние обитатели."
    "Я вдруг явственно почувствовал, что нахожу Славю...{w} милой?"
    "Я украдкой посмотрел на нее, не зная, что еще добавить."

    show cg d1_sl_dinner  with dspr

    sl "Прости, надо было показать тебе лагерь, а я совсем забегалась сегодня."
    me "Да я сам... Вроде осмотрел все более-менее."

    show cg d1_sl_dinner_0  with dspr

    sl "Прям-таки все-все?"
    "Она улыбалась так, что мне приходилось от смущения прятать глаза."
    me "Ну почем я знаю – все или нет, я здесь первый день."
    sl "Ну хорошо, и что видел уже?"
    me "Площадь, столовую вот видел, футбольную площадку..."
    sl "А пляж?"
    me "Пляж?"
    sl "Обязательно сходи! Или давай вместе сходим!"
    me "А... ну да, хорошо... сходим..."
    th "Одно место лучше другого. Пляж, футбольное поле...так было во всех пионерлагерях?"
    "Было...в мою голову вдруг закралась одна идея, к которой я должен был прийти еще много часов назад."
    "Может ли быть, что я попал в прошлое?"
    "Да, это дало бы ответы. Это бы все объяснило."
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
    sl "В палатку тебя поселит к кому-нибудь."
    me "Зачем?"
    show sl laugh pioneer at center     with dspr
    sl "Тебе не помешает изрядка где-то спать!"
    me "Разумно..."
    show sl smile pioneer at center     with dspr
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
            th "Мало ли, что может произойти. Возьму с собой, а завтра отдам при встрече."
            window hide
        "Не трогать":
            window show
            th "Потеряю еще. Пусть тут будут."
            window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_dining_hall_near_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 5

    window show
    "Это был насыщенный день. Глаза слипались, и я поспешно двинулся к домику вожатой."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_square_night 
    with dissolve

    window show
    "Проходя мимо площади, я с удивлением увидел Лену. Она, как и днем, сидела на одной из лавочек и читала книгу."

    play music music_list["lets_be_friends"] fadein 5

    show un normal pioneer far at center      with dissolve   
    "Я решил подойти и поговорить."
    "Она единственная, с кем мне не удалось сегодня перекинуться и парой слов."
    show un normal pioneer at center     with dissolve
    me "Э-э...привет, читаешь, да?"
    show un surprise pioneer at center     with dspr
    "Лена от удивления аж подпрыгнула на лавочке."
    me "И-извини, не хотел тебя напугать!"
    show un shy pioneer at center     with dspr
    un "Ничего…"
    "Она покраснела и снова уставилась в книжку."
    me "Что читаешь?"
    "Она показала обложку – «Унесенные ветром»."
    window hide

    menu:
        "Похвалить книгу":
            $ lp_un = (lp_un) + (1)
            window show
            me "Хорошая книжка…"
            un "Спасибо..."
        "Ничего не говорить":
            window show
            pass

    "Лена, похоже, не собиралась продолжать разговор."
    me "Ох, похоже, что я тебе мешаю..."
    show un normal pioneer at center     with dspr
    un "Нет."
    "Не отрывая взгляд от книжки, сказала она."
    me "Я присяду?"
    show un surprise pioneer at center     with dspr
    un "Зачем?"
    th "Действительно - зачем? Не похоже, чтобы я мог у нее хоть что-то выпытать."
    show un shy pioneer at center     with dspr
    "Я внимательно осмотрел Лену, от чего та покраснела."
    th "Возможно, стоит уйти."
    me "Я все же мешаю, так что..."
    un "Нет, не мешаешь."
    me "Да нет, я могу и уйти..."
    un "Все в порядке."
    "Ситуация становилась нелепой."
    me "Ну, раз так..."
    "Я аккуратно сел на край лавочки."
    "После такого разговора мне меньше всего хотелось вообще находиться здесь, но и встать и уйти было как-то неудобно."
    me "Как-то нехорошо получилось..."
    "Лена ничего не ответила."
    "Я выставил себя дураком. Одно из моих хобби, похоже."
    "Будь на ее месте, допустим, Ульянка, наверняка бы меня засмеяла."
    me "А тебе здесь нравится?"
    "Я вспомнил вопрос Слави и решил, что он как нельзя лучше подойдет для начала разговора."
    show un smile pioneer at center     with dspr
    un "Да."
    "Она едва заметно улыбнулась."
    me "И мне, наверное, нравится..."
    show un normal pioneer at center     with dspr
    "Было очевидно, что Лена не очень общительна и вряд ли в состоянии поддержать непринужденную беседу ни о чем, как Славя."
    "Но в то же время было в ней что-то, что привлекало внимание."
    "Что-то, скрытое от глаз, но такое родное и естественное."
    show un shy pioneer at center     with dspr
    un "Поздно уже, мне пора…"
    me "Да, поздновато…"
    un "Спокойной ночи."
    me "Спокойной…"
    hide un  with dissolve
    "Что-то с ней не так."
    th "Вроде бы обычная скромная девочка, но..."
    "Еще один вопрос без ответа. Как неожиданно."

    stop music fadeout 5
    "..."
    window hide

    with fade2

    window show

    stop ambience fadeout 2

    "Я продолжил свой путь к домику вожатой."
    window hide

    $ persistent.sprite_time = 'night'
    scene bg ext_house_of_mt_night 
    with dissolve

    window show
    "В окне горел свет."
    window hide

    $ persistent.sprite_time = 'sunset'
    scene bg int_house_of_mt_noitem_night 
    with dissolve

    play music music_list["smooth_machine"] fadein 5

    show mt normal pioneer at center     with dissolve

    window show

    mt "Привет, Семен!{w} Что-то ты долго!"
    me "Да…{w} Гулял, с лагерем знакомился."
    mt "Хорошо.{w} Спать будешь здесь."
    "Она указала на одну из кроватей."
    me "Здесь?.."
    "Я недоверчиво моргнул."
    show mt surprise pioneer at center     with dspr
    mt "Ну да, а что такого?{w} Все равно других свободных мест нет."
    show mt smile pioneer at center     with dspr
    mt "Ты же хочешь стать порядочным пионером?"
    "Она акцентировала внимание на слове «порядочным»."
    me "Да… Конечно…"
    "Я задумался на мгновение."
    me "Но ты-то не против?"
    show mt surprise pioneer at center     with dspr
    "Она как-то странно на меня посмотрела.{w} В ее взгляде смешались удивление и что-то вроде обиды."
    show mt angry pioneer at center     with dspr
    mt "Пионер должен уважать старших!"
    "Грозно сказала она."
    me "Должен, конечно, кто же спорит…"
    "Пролепетал я в ответ, не понимая, что же не так."
    mt "Или ты?.."
    show mt rage pioneer at center     with dspr
    "Она пристально посмотрела на меня."
    "Я почувствовал, как по щеке пробежала капелька пота."
    me "Я? А что я?{w} Да что не так-то?!"
    "Из-за слегка панического состояния я невольно перешел на тон выше."
    mt "Взрослых надо называть на Вы!"
    "Я внимательно на нее посмотрел. Неужели она настолько манерная? Если она и старше меня, то максимум на пару лет."
    th "Возможно, сейчас не лучшее время для споров."
    "Да и, положа руку на сердце, меня не слишком волновало, на «ты» или на «Вы» мне к ней обращаться. Так что я смущенно промямлил:"
    me "Э-э...извините, виноват..."
    show mt smile pioneer at center     with dspr
    mt "Так-то лучше!{w} Так и должен вести себя порядочный пионер!"
    mt "А теперь спать!"
    "У меня не было планов по становлению пионером, но при упоминании сна я растерял последнюю охоту о чем-либо спорить."
    window hide

    stop music fadeout 5

    scene bg black 
    with fade2

    window show
    "Я облегченно рухнул на кровать. В голове проносились расплывчатые воспоминания о сегодняшнем дне."
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

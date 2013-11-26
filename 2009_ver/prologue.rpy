# Пролог.
# Часть 1 из 1.
# Знакомство.

label prologue:
    $ new_chapter(-1, u"Пролог")
    $ prolog_time()

    $renpy.music.set_volume (0.4, channel=7)    
    play music music_list["drown"] fadein 3 channel 7
    scene anim prolog_1
    with fade
    "Я помню каждое свое пробуждение."
    scene anim prolog_2
    with dissolve
    "Помню так отчетливо, как если бы оно было вырезано у меня в зрачках или на обратной стороне век."
    scene anim prolog_3
    with fade
    "Даже сейчас, не открывая глаз, я вижу все тот же нависающий надо мной потолок, который не стал за ночь ни выше, ни ниже."
    "Не стал другим."
    "И который, конечно же, никуда не исчез."
    scene anim prolog_4
    with dissolve
    "Я помню каждое свое пробуждение - просто потому, что каждый день всю мою жизнь начинался одинаково."
    "Радость сна уходила, оставляя меня наедине с реальностью, и открытые глаза не делали эту жизнь понятнее."
    scene anim prolog_5
    with dissolve
    "Все куда-то уходили. {w=.2}Всегда."
    "А я оставался. {w=.2} Всегда."
    scene anim prolog_6
    with dissolve
    "Оставался в пустой квартире, занимался и даже не запоминал - чем."
    "Потому что сами дни не отличались друг от друга."
    scene anim prolog_7
    with dissolve
    "Так же, как и одинаковое утро, они были лишь квинтэссенцией дня."
    "В конце концов они все слились воедино."
    "Слились в один день, когда я уже не мог сказать, что было в прошлый четверг, а что два года назад."
    "Я словно попал в безвременье, где ничто не имело значения."
    scene anim prolog_8
    with dissolve
    "Дни текли, и не было ничего, что придавало бы этому течению смысл."
    "Раньше, когда я еще учился, были обязанности."
    scene anim prolog_9
    with dissolve
    "Ходить на учебу, слушать и запоминать сухие лекции, сдавать экзамены."
    scene anim prolog_10
    with fade
    "Но это быстро ушло."
    "Я бросил университет на первом же курсе."
    scene anim prolog_11
    with dissolve
    "Почему? {w=.2}Не знаю."
    "Наверное, я просто не выдержал того, что люди вокруг меня неслись в круговороте жизни, а я..."
    "Я оставался прежним. И никак не мог измениться."
    scene anim prolog_12
    with dissolve
    "Учеба ушла в небытие."
    "Когда это произошло - несколько лет назад? Это уже не имело значения."
    "Теперь я оставался дома."
    scene anim prolog_13
    with dissolve
    "Какие-то редкие попытки работать давали возможность существовать, но не более."
    "Мать изредка звонила мне, пытаясь ободрить, но..."
    "В конце концов вся работа прекращалась, и я вновь оставался в пустой квартире."
    "Я оставался. {w=.2} Всегда."
    scene anim prolog_14
    with dissolve
    "Пожалуй, единственным, что еще окрашивало мою жизнь в какие-то полутона, были прогулки."
    "Я мог выходить только по вечерам."
    "Потому что днем потоки людей еще тягуче струились по улицам."
    "Они сталкивались. Извиняясь или рыча вслед."
    scene anim prolog_15
    with dissolve
    "Извивались, чтобы обойти другой поток, и неслись дальше."
    "Вынести этого я уже не мог."
    "И только вечер успокаивал."
    #stop music fadeout 2 channel 7
    "Люди расходились по домам, а я, словно в сумасшедшем желании отличиться от них, наоборот, выходил."
    "И вчера я снова вышел..."
    scene anim intro_1
    with fade
    $ renpy.pause(2)
    #"Холодный городской воздух "
    scene anim intro_2
    with dissolve
    #"город"
    $ renpy.pause(3)
    scene anim intro_3
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_4
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_5
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_6
    with dissolve
    #"город"
    $ renpy.pause(3)
    scene anim intro_7
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_8
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_9
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_10
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_11
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_12
    with dissolve
    #"город"
    $ renpy.pause(3)
    scene anim intro_13
    with fade
    #"город"
    $ renpy.pause(3)
    scene anim intro_14
    with dissolve
    #"город"
    $ renpy.pause(3)
    scene anim intro_15
    with dissolve
    #"город"
    $ renpy.pause(3)
    scene anim intro_16
    with dissolve
    #"город"
    
    stop music fadeout 2 channel 7
    $ renpy.pause(2)

    jump day_1_start
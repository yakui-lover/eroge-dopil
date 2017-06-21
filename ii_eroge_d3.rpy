python:
    d3_wake_early = false
    d3_accept_Neptune = false
    d3_busted = false

label ii_eroge_d3:
    # 7:00-ish
    call d3_early_morning
    if d3_wake_early:
        call d3_sl_run
    else:
        call d3_sleep
    # 8:00
    call d3_morning
    # 8:30-45?
    call d3_morning_meet
    # 9:00
    call d3_breakfast
    # 9:30
    call d3_cleaning
    # 10:00
    call d3_morning_free
    # 11:00?
    if d3_busted:
        call d3_potatoes
    else:
        call d3_event_preparations
    # 13:00
    call d3_supper
    # 14:00
    if d3_accept_Neptune:
        call d3_Neptune
    else:
        call d3_event_skip
    # 21:00
    call d3_dinner
    # 21:40
    call d3_evening_meet
    # 22:00
    call d3_evening_freetime
    # 23:30
    call d3_night
    jump ii_eroge_d4

label d3_early_morning:
    "Кажется, раннее утро, и ты проснулся."
    "Дрыхнуть или делать зарядку?":
        "Дрыхнуть":
            # GOTO d3_sleep
            "ЗОЖ переоценён"
        "Турнички!":
            # GOTO d3_sl_run
            "Бодрячком!"
            $ sp_str += 1
    return

label d3_sl_run:
    # IN d3_early_morning
    "Пока ты работал над своим бодрым и мускулистым телом, тебя заметила пробегающая мимо Слава!"
    sl "О, привет, Семён! Тоже занимаешься физкульту-"
    "Но она уже убежала дальше"
    $ sl_lp += 1 #?
    # GOTO d3_morning_meet
    return

label d3_morning:
    # IN d3_early_morning
    di "Пионеры, подъём! На зарядку!"
    "Да, хватит спать. И умойся сначала."
    "А как хлебнёшь холодной воды, иди на линейку"
    # GOTO d3_morning_meet
    return

label d3_morning_meet:
    # IN d3_morning, d3_sl_run
    "Зарядка прошла без особых происшествий.Никто даже не выколол другу глаза на \"Мельнице\""
    mt "Пионеры, сегодня вы будете драить асфальт и играть в морских богов!"
    th "Надеюсь, это не включает очистку дна озера от рыбьего помёта"
    # GOTO d3_breakfast
    return

label d3_breakfast:
    # IN d3_morning_meet
    sh "Семён, хочешь исследовать кладовку? Будет весело!"
    me "Э, я подумаю."
    # GOTO d3_cleaning
    return

label d3_cleaning:
    # IN d3_breakfast
    mt "Пионер! Твой участок - вон тот угол у Генды. Остальные уже разобрали"
    "*щыр* *щыр*" 
    # GOTO d3_morning_free
    return

label d3_morning_free:
    # IN d3_cleaning
    "Я пойду в:":
         "Спортивный кружок":
             jump d3_sports_club
         "Кружок юных натуралистов":
             jump d3_unnat_club
         "Кружок не геев, блджад!":
             jump d3_cybernetics
         "Кружок модельстроя":
             jump d3_mod_club
         "Кружок модельстроя":
             jump d3_mod_club
         "Музкружок":
             jump d3_k_on
         "*кхм* Караганду!":
             jump d3_stay_home_club
    "I AM ERROR"
    return

label d3_sports_club:
    # IN d3_morning_free
    us "Кияаа!"
    "Turns out, sports are gay, because balls do touch. And it hurts like hell"
    "На радостях ты выпинываешь мяч в окно"
    "Ольге Модестовне новый кондиционер пришёлся не по вкусу. Ты с лолификацией прошлого этой страны идёте чистить картошку"
    # GOTO d3_potatoes
    return

label d3_potatoes:
    # IN d3_sports_club
    $ us_lp += 1
    # GOTO d3_supper
    return

label d3_unnat_club:
    # IN d3_morning_free
    yes "Что значит, если моей знакомой пионер подарил букет роз?"
    sl "Он хочет её {w}обрадовать."
    # GOTO d3_event_preparations
    return

label d3_cybernetics_club:
    # IN d3_morning_free
    el "Отлично, Семён! Втроём мы наконец-то сможем открыть сокровенную кладовку!"
    me "На кой вам вообще третий для этого???"
    sh "А это, пионер, сюжетный момент, понимаешь? Вон, смотри, генератор низких частот стоит, будем через пару дней Алису пугать."
    # GOTO d3_event_preparations
    return

label d3_mod_club:
    # IN d3_morning_free
    uk "Ландан из зе кэпитал ов Грейт Британ!"
    mt "Собирайтесь, пионеры, надо для Нептуна хвосты русалок к девчатам шить"
    # GOTO d3_event_preparations
    return

label d3_k_on:
    # IN d3_mod_club
    mi "Семён, нет времени объяснять, тут слишком много флагов идей и моего непрописанного рута, лабай blow with the fires, только быстрее, у нас сегодня сокращённые занятия из-за подготовки к дню Нептуна, а мы с Двачевской посмотрим"
    # GOTO d3_event_preparations
    return

label d3_stay_home_club:
    # IN d3_mod_club
    th "Надо бы прописать такой вариант развития событий"
    # GOTO d3_event_preparations
    return

label d3_event_preparations:
    # IN d3_morning_free clubs
    mt "Боги моря требуют жертв в виде бесплатного детского труда! Идите, помогайте"
    lm "И хвостов к русалкам! И полуголых русалок!"
    "Семён же хочет участвовать во всём этом?":
        "Конечно! Полуголые русалки! Желательно, нижней частью!":
            $ d3_accept_Neptune = True
        "Да ну нафиг!":
            pass
    lm "А в прочем, без разницы. Найди мне в лесу трезубец. Вот скоч, вот рубанок, вот золотинки, делай что хочешь"
    # GOTO d3_supper
    return

label d3_supper:
    # IN d3_event_preparations
    "Суп, сосисочки, чай вкусный, утоляет жажду"
    # GOTO d3_event_skip d3_Neptune
    return

label d3_event_skip:
    # IN d3_supper
    "Семён, думаешь, что можно так просто забить на лагерные мероприятия?"
    th "Ага"
    dv "А вот хрен тебе, Нептунов бастард! Участие обязательное!"
    jump d3_Neptunes_son

label d3_Neptunes_son:
    # IN d3_event_skip
    lm "Смотри, недотёпа: конкурс: стянуть с головы русалки бандану. Не лифчик! Отличишься - будет приз."
    me "Точно не лифчик?"
    "Лифчик?":
        "Нет":
            jump d3_Neptune_unsuccessful
        "Бандану":
            jump d3_Neptune_successful

label d3_Neptune:
    # IN d3_event_preparations
    lm "В общем, ползучие твари суши: вы или участвуете в конкурсах или идёте ко дну! Ну как, что выбираете?"
    "Семён: ":
        "Кормит рыб":
            jump d3_Neptune_unsuccessful
        "Каким-то образом побеждает во всех конкурсах":
            jump d3_Neptune_unsuccessful # This is not a bug per se, that's how it is in pastebin

label d3_Neptune_unsuccessful:
    # IN d3_Neptune
    "Мокрый и грустный Семён проводит время в остатках конкурса и пустоте непрописанного эвента"
    # GOTO d3_dinner
    return

label d3_Neptune_successfull:
    # IN d3_Neptune d3_Neptunes_son
    lm "От эт малаца, батя одобряет."
    lm "Лады, проявил себя, выбирай невестку себе."
    "Я поеду с...":
        "Улей":
            jump d3_island_ul
        "ЧЧ":
            jump d3_island_dv
        "Славой":
            jump d3_island_sl
        "Айдору":
            jump d3_island_mi
        "Унывашкой":
            jump d3_island_un
        "Мацой":
            jump d3_island_mz

label d3_island_ul:
label d3_island_dv:
label d3_island_sl:
label d3_island_mi:
label d3_island_un:
label d3_island_mz:
    "TO BE FINISHED SOON"
    # GOTO d3_supper
    return

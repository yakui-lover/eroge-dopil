# Отладочный скрипт.
# Список эпизодов.

label show_me_game:
    $ new_chapter(-1, u"Выбор эпизода","nvl")

label days_choice:
    menu:
        "ВНИМАНИЕ: Доступно только при config.developer = True\nМногое еще предстоит сделать, но есть и готовые эпизоды.\nХочешь к ним перейти?"
        "Нет, не хочу. Буду играть с самого начала.":
            return
        "Заставка":
            jump intro
        "Песочница":
            jump sandbox
        "День 1":
            menu:
                "Автобус":
                    jump day_1_start
                "Прибытие":
                    jump day_1_arrival
                "Пристань":
                    jump day_1_dock
                "Мод-тян":
                    jump day_1_mod_tan
                "Электроник":
                    jump day_1_elektron
                "Обед":
                    jump day_1_dining_room
                "Вечер":
                    jump day_1_afterday
                "Выбрать другой день":
                    jump days_choice
        "День 2":
            menu:
                "Пробуждение":
                    jump day_2_start
                "Утреннее знакомство с лагерем":
                    jump day_2_map_prepare
                "Обед, карточный турнир и ужин":
                    jump day_2_dinner
                "Вечернее блуждание в поисках слота":
                    jump day_2_mapEv_prepare
                "Выбрать другой день":
                    jump days_choice
        "День 3":
            jump day_3_start
        "День 4":
            jump day_4_start
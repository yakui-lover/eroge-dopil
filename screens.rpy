init:
    python:
        
        
        config.thumbnail_width = 318
        config.thumbnail_height = 179
        
        
        
        
        
        
        
        style.file_picker_ss_window.xpos = 0
        style.file_picker_ss_window.ypos = 0
        
        
        
        style.file_picker_text = Style(style.default)
        style.file_picker_text.color = "#4f4ea9"
        style.file_picker_text.size = 150
        
        
        
        
        
        style.save_load_button = Style(style.button)
        style.save_load_button.background = get_image("gui/save_load/blank_idle.png")
        style.save_load_button.hover_background = get_image("gui/save_load/blank_hover.png")
        style.save_load_button.selected_background = get_image("gui/save_load/blank_hover.png")
        style.save_load_button.selected_hover_background = get_image("gui/save_load/blank_hover.png")
        style.save_load_button.selected_idle_background = get_image("gui/save_load/blank_hover.png")
        
        style.save_load_button.top_margin = 20
        style.save_load_button.right_margin = 100
        
        
        
        
        
        style.base_font = Style(style.default)
        style.base_font.font  = "fonts/calibri.ttf"
        style.base_font.size = 28
        style.base_font.line_spacing = 2
        
        
        
        
        
        style.say_dialogue = Style(style.base_font)
        style.say_label = Style(style.base_font)
        style.say_label.size = 28
        style.say_label.drop_shadow=(2, 2)
        style.say_label.drop_shadow_color = "#000"
        
        style.chapter = Style(style.base_font)
        style.chapter.font  = "fonts/corbel.ttf"
        style.chapter.size = 120
        style.chapter.color = "#fff"
        
        style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]
        
        style.daynum = Style(style.chapter)
        style.daynum.font  = "fonts/corbel.ttf"
        style.daynum.size = 45
        
        style.normal_day = Style(style.base_font)
        style.normal_day.color = "#ffdd7d"
        style.normal_day.drop_shadow=(2, 2)
        style.normal_day.drop_shadow_color = "#000"
        style.narrator_day = Style(style.normal_day)
        style.narrator_day.italic = False
        style.thoughts_day = Style(style.normal_day)
        style.thoughts_day.bold = False
        
        style.normal_sunset = Style(style.base_font)
        style.normal_sunset.color = "#ffdd7d"
        style.normal_sunset.drop_shadow=(2, 2)
        style.normal_sunset.drop_shadow_color = "#000"
        style.narrator_sunset = Style(style.normal_sunset)
        style.narrator_sunset.italic = False
        style.thoughts_sunset = Style(style.normal_sunset)
        style.thoughts_sunset.bold = False
        
        style.normal_night = Style(style.base_font)
        style.normal_night.color = "#ffdd7d"
        style.normal_night.drop_shadow=(2, 2)
        style.normal_night.drop_shadow_color = "#000"
        style.narrator_night = Style(style.normal_night)
        style.narrator_night.italic = False
        style.thoughts_night = Style(style.normal_night)
        style.thoughts_night.bold = False
        
        style.normal_prolog = Style(style.base_font)
        style.normal_prolog.color = "#ffdd7d"
        style.normal_prolog.drop_shadow=(2, 2)
        style.normal_prolog.drop_shadow_color = "#000"
        style.narrator_prolog = Style(style.normal_prolog)
        style.narrator_prolog.italic = False
        style.thoughts_prolog = Style(style.normal_prolog)
        style.thoughts_prolog.bold = False
        
        style.cards_button = Style(style.button)
        style.cards_button.background = RoundRect("#000", False)
        style.cards_button.hover_background = RoundRect("#555", False)
        style.cards_button.insensitive_background = RoundRect("#404040", False)
        
        style.cards_button_text = Style(style.button_text)
        style.cards_button_text.color = "#FFF"
        style.cards_button_text.selected_color = "#777"
        style.cards_button_text.insensitive_color = "#c8c8c8"
        
        style.log_button = Style(style.button)
        style.log_button.child = None
        style.log_button.focus_mask = None
        style.log_button.background  = None
        
        style.log_button_text = Style(style.normal_day)
        style.log_button_text.selected_color = "#115bc0"
        style.log_button_text.hover_color = "#115bc0"
init:
    python:
        
        _main_menu_screen = "main_menu"
        renpy.music.register_channel("test_one", "sfx", False)
        renpy.music.register_channel("test_two", "sfx", False)
screen main_menu:
    tag menu
    modal False
    $ owl_played = 1
    imagemap:
        auto 'images/1080/gui/title_menu/mainmenu_%s.png'
        hotspot ((439, 265, 318, 621)):
            clicked Start()
        hotspot ((787, 261, 270, 537)):
            clicked ShowMenu('load')
        hotspot ((1067, 748, 252, 312)):
            clicked ShowMenu('preferences')
        hotspot ((1083, 258, 229, 538)):
            clicked ShowMenu('gallery')
        hotspot ((1459, 532, 149, 295)):
            clicked ShowMenu('quit')
            hovered (Play('test_one', 'sound/sfx/menu_gate.ogg'))
        if config.developer:
            hotspot ((1578, 953, 342, 127)):
                clicked ShowMenu('show_me_game')
        hotspot ((170, 609, 111, 152)):
            clicked ShowMenu('history')
            hovered (Play('test_two', 'sound/test.ogg'))

init:
    $ _game_menu_screen = "game_menu_selector"
screen game_menu_selector:
    tag menu
    modal True
    $ timeofday = persistent.timeofday
    imagemap:
        auto (get_image((('gui/ingame_menu/' + timeofday) + '/ingame_menu_%s.png')))
        hotspot ((630, 390, 660, 70)):
            clicked MainMenu()
        hotspot ((630, 455, 660, 70)):
            clicked ShowMenu('load')
        hotspot ((630, 520, 660, 70)):
            clicked ShowMenu('preferences')
        hotspot ((630, 585, 660, 70)):
            clicked ShowMenu('save')
        hotspot ((630, 650, 660, 70)):
            clicked Return()

screen save:
    tag menu
    modal True
    window:
        background get_image('gui/save_load/save_bg.jpg')
        imagebutton:
            action ShowMenu('load')
            auto get_image('gui/save_load/load_%s.png')
            yalign 0.08
            xalign 0.1
        imagebutton:
            action ShowMenu('preferences')
            auto get_image('gui/save_load/settings_%s.png')
            yalign 0.08
            xalign 0.9
        imagebutton:
            action Return()
            auto get_image('gui/save_load/back_%s.png')
            yalign 0.92
            xalign 0.03
        imagebutton:
            action ((FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot)))
            auto get_image('gui/save_load/savegame_%s.png')
            yalign 0.92
            xalign 0.5
        imagebutton:
            action FileDelete(selected_slot)
            auto get_image('gui/save_load/delete_%s.png')
            yalign 0.92
            xalign 0.97
        vbox:
            xalign 0.05
            yalign 0.5
            for i in range(0, 10):
                if (i == 0):
                    textbutton u'\u0410\u0432\u0442\u043e':
                        style 'log_button'
                        text_style 'log_button_text'
                        action FilePage('auto')
                        text_size 40
                else:
                    textbutton str(i):
                        style 'log_button'
                        text_style 'log_button_text'
                        action FilePage(i)
                        text_size 40
        window:
            right_padding 200
            bottom_padding 160
            top_padding 130
            left_padding 230
            background None
            grid 4 3:
                transpose True
                xfill True
                for i in range(1, 13):
                    button:
                        action (SetVariable('selected_slot', i))
                        style 'save_load_button'
                        yfill False
                        xfill False
                        vbox:
                            add FileScreenshot(i):
                                xpos 3
                                ypos 8
                            text ((((((' %2d. ' % i) + FileTime(i, format='%d.%m.%y, %H:%M', empty=_('Empty Slot.'))) + '\n') + ' ') + FileSaveName(i))):
                                style 'log_button_text'
                                xpos -4
                                ypos 15
                                size 22

init:
    $ _load_prompt = "load"
screen load:
    tag menu
    modal True
    window:
        background get_image('gui/save_load/load_bg.jpg')
        imagebutton:
            action ShowMenu('save')
            auto get_image('gui/save_load/save_%s.png')
            yalign 0.08
            xalign 0.1
        imagebutton:
            action ShowMenu('preferences')
            auto get_image('gui/save_load/settings_%s.png')
            yalign 0.08
            xalign 0.9
        imagebutton:
            action Return()
            auto get_image('gui/save_load/back_%s.png')
            yalign 0.92
            xalign 0.03
        imagebutton:
            action ((FunctionCallback(on_load_callback, selected_slot), FileLoad(selected_slot)))
            auto get_image('gui/save_load/loadgame_%s.png')
            yalign 0.92
            xalign 0.5
        imagebutton:
            action FileDelete(selected_slot)
            auto get_image('gui/save_load/delete_%s.png')
            yalign 0.92
            xalign 0.97
        vbox:
            xalign 0.05
            yalign 0.5
            for i in range(0, 10):
                if (i == 0):
                    textbutton u'\u0410\u0432\u0442\u043e':
                        style 'log_button'
                        text_style 'log_button_text'
                        action FilePage('auto')
                        text_size 40
                else:
                    textbutton str(i):
                        style 'log_button'
                        text_style 'log_button_text'
                        action FilePage(i)
                        text_size 40
        window:
            right_padding 200
            bottom_padding 160
            top_padding 130
            left_padding 230
            background None
            grid 4 3:
                transpose True
                xfill True
                for i in range(1, 13):
                    button:
                        action (SetVariable('selected_slot', i))
                        style 'save_load_button'
                        vbox:
                            add FileScreenshot(i):
                                xpos 3
                                ypos 8
                            text ((((((' %2d. ' % i) + FileTime(i, format='%d.%m.%y, %H:%M', empty=_('Empty Slot.'))) + '\n') + ' ') + FileSaveName(i))):
                                style 'log_button_text'
                                xpos -4
                                ypos 15
                                size 22

screen preferences:
    tag menu
    modal False
    $ bar_null = Frame(get_image('gui/settings/bar_null.png'), 12, 12)
    $ bar_full = Frame(get_image('gui/settings/bar_full.png'), 12, 12)
    window:
        background get_image('gui/settings/preferences_bg.jpg')
        imagebutton:
            action ShowMenu('save')
            auto get_image('gui/save_load/save_%s.png')
            yalign 0.08
            xalign 0.1
        imagebutton:
            action ShowMenu('load')
            auto get_image('gui/save_load/load_%s.png')
            yalign 0.08
            xalign 0.9
        imagebutton:
            action Return()
            auto get_image('gui/save_load/back_%s.png')
            yalign 0.92
            xalign 0.03
        vbox:
            xalign 0.5
            null:
                height 345
            grid 3 1:
                xalign 0.5
                imagebutton:
                    action (Preference('display', 'window'))
                    auto get_image('gui/settings/window_%s.png')
                null:
                    width 50
                imagebutton:
                    action (Preference('display', 'fullscreen'))
                    auto get_image('gui/settings/fullscreen_%s.png')
            null:
                height 90
            grid 3 1:
                xalign 0.5
                imagebutton:
                    action (Preference('skip', 'all'))
                    auto get_image('gui/settings/all_%s.png')
                null:
                    width 50
                imagebutton:
                    action (Preference('skip', 'seen'))
                    auto get_image('gui/settings/seen_%s.png')
            null:
                height 70
            grid 1 6:
                xalign 0.5
                imagebutton:
                    action (Play('sound', 'sound/test.ogg'))
                    auto get_image('gui/settings/music_%s.png')
                    xalign 0.5
                bar:
                    xalign 0.5
                    right_bar bar_null
                    xmaximum 700
                    value (Preference('music volume'))
                    left_bar bar_full
                imagebutton:
                    action (Play('sound', 'sound/test.ogg'))
                    auto get_image('gui/settings/sounds_%s.png')
                    xalign 0.5
                bar:
                    xalign 0.5
                    right_bar bar_null
                    xmaximum 700
                    value (Preference('sound volume'))
                    left_bar bar_full
                imagebutton:
                    action (Play('sound', 'sound/test.ogg'))
                    auto get_image('gui/settings/voice_%s.png')
                    xalign 0.5
                bar:
                    xalign 0.5
                    right_bar bar_null
                    xmaximum 700
                    value (Preference('voice volume'))
                    left_bar bar_full
            null:
                height 80
            grid 1 3:
                xalign 0.5
                bar:
                    xalign 0.5
                    right_bar bar_null
                    xmaximum 700
                    value (Preference('text speed'))
                    left_bar bar_full
                null:
                    height 60
                bar:
                    xalign 0.5
                    right_bar bar_null
                    xmaximum 700
                    value (Preference('auto-forward time'))
                    left_bar bar_full
    imagebutton:
        action ShowMenu('preferences2')
        auto get_image('gui/dialogue_box/day/forward_%s.png')
        yalign 0.5
        xalign 0.8

screen preferences2:
    tag menu
    modal False
    $ bar_null = Frame(get_image('gui/settings/bar_null.png'), 12, 12)
    $ bar_full = Frame(get_image('gui/settings/bar_full.png'), 12, 12)
    window:
        background get_image('gui/settings/preferences_bg2.jpg')
        imagebutton:
            action ShowMenu('save')
            auto get_image('gui/save_load/save_%s.png')
            yalign 0.08
            xalign 0.1
        imagebutton:
            action ShowMenu('load')
            auto get_image('gui/save_load/load_%s.png')
            yalign 0.08
            xalign 0.9
        imagebutton:
            action Return()
            auto get_image('gui/save_load/back_%s.png')
            yalign 0.92
            xalign 0.03
        vbox:
            xalign 0.5
            null:
                height 345
            grid 3 1:
                xalign 0.5
                imagebutton:
                    action (SetField(persistent, 'font_size', 'small'))
                    auto get_image('gui/settings/normal_%s.png')
                null:
                    width 50
                imagebutton:
                    action (SetField(persistent, 'font_size', 'large'))
                    auto get_image('gui/settings/large_%s.png')
    imagebutton:
        action (ToggleField(persistent, 'foobar', true_value=True, false_value=False))
        auto get_image('gui/settings/check_%s.png')
        yalign 0.9
        xalign 0.71
    imagebutton:
        action ShowMenu('preferences')
        auto get_image('gui/dialogue_box/day/backward_%s.png')
        yalign 0.5
        xalign 0.2

screen history:
    tag menu
    modal False
    $ screen_endings = [(u'\u0421\u0435\u043c\u0451\u043d, \u0445\u043e\u0440\u043e\u0448\u0430\u044f', persistent.endings['main_good']), (u'\u0421\u0435\u043c\u0451\u043d, \u043f\u043b\u043e\u0445\u0430\u044f', persistent.endings['main_bad']), (u'\u0421\u043b\u0430\u0432\u044f, \u0445\u043e\u0440\u043e\u0448\u0430\u044f', persistent.endings['sl_good']), (u'\u0421\u043b\u0430\u0432\u044f, \u043f\u043b\u043e\u0445\u0430\u044f', persistent.endings['sl_bad']), (u'\u0410\u043b\u0438\u0441\u0430, \u0445\u043e\u0440\u043e\u0448\u0430\u044f', persistent.endings['dv_good']), (u'\u0410\u043b\u0438\u0441\u0430, \u043f\u043b\u043e\u0445\u0430\u044f', persistent.endings['dv_bad']), (u'\u041b\u0435\u043d\u0430, \u0445\u043e\u0440\u043e\u0448\u0430\u044f', persistent.endings['un_good']), (u'\u041b\u0435\u043d\u0430, \u043f\u043b\u043e\u0445\u0430\u044f', persistent.endings['un_bad']), (u'\u0423\u043b\u044c\u044f\u043d\u0430, \u0445\u043e\u0440\u043e\u0448\u0430\u044f', persistent.endings['us_good']), (u'\u0423\u043b\u044c\u044f\u043d\u0430, \u043f\u043b\u043e\u0445\u0430\u044f', persistent.endings['us_bad']), (u'\u041c\u0438\u043a\u0443', persistent.endings['mi']), (u'\u042e\u043b\u044f', persistent.endings['uv_unknown_fucken_shit']), (u'\u0412\u0441\u0435 \u0432\u043c\u0435\u0441\u0442\u0435', persistent.endings['uv_city'])]
    $ void = '??????????'
    window:
        background get_image('gui/settings/history_bg.jpg')
        imagebutton:
            action Return()
            auto get_image('gui/save_load/back_%s.png')
            yalign 0.92
            xalign 0.03
        vbox:
            xalign 0.5
            null:
                height 190
            text u'\u041a\u043e\u043d\u0446\u043e\u0432\u043a\u0438':
                xalign 0.5
                style 'base_font'
                color '#3e2b15'
                size 50
            null:
                height 15
            grid 1 13:
                xalign 0.6
                for i, k in screen_endings:
                    if k:
                        text i:
                            xalign 0.5
                            style 'base_font'
                            color '#3e2b15'
                            size 50
                    else:
                        text void:
                            xalign 0.5
                            style 'base_font'
                            color '#3e2b15'
                            size 50

screen choice:
    modal True
    python:
        choice_colors_hover = {'day': '#9dcd55', 'night': '#3ccfa2', 'sunset': '#dcd168', 'prologue': '#98d8da'}
        choice_colors = {'day': '#466123', 'night': '#145644', 'sunset': '#69652f', 'prologue': '#496463'}
    window:
        right_padding 75
        bottom_padding 50
        yalign 0.5
        top_padding 50
        xfill True
        background (Frame(get_image((('gui/choice/' + persistent.timeofday) + '/choice_box.png')), 50, 50))
        left_padding 75
        vbox:
            xalign 0.5
            for caption, action in items:
                if (action and caption):
                    button:
                        action action
                        background None
                        text caption:
                            hover_size 37
                            color choice_colors[persistent.timeofday]
                            xcenter 0.5
                            hover_color choice_colors_hover[persistent.timeofday]
                            font 'fonts/corbel.ttf'
                            size 37
                else:
                    text caption:
                        color choice_colors[persistent.timeofday]
                        font 'fonts/corbel.ttf'
                        size 37

screen yesno_prompt:
    modal True
    $ ui.image(get_image('gui/o_rly/base.png'), id=_1)
    text _(message):
        xalign 0.5
        yalign 0.46
        color '#64483c'
        text_align 0.5
        font 'fonts/corbel.ttf'
        size 30
    imagebutton:
        action yes_action
        auto get_image('gui/o_rly/yes_%s.png')
        yalign 0.65
        xalign 0.3
    imagebutton:
        action no_action
        auto get_image('gui/o_rly/no_%s.png')
        yalign 0.65
        xalign 0.7

screen say:
    modal False
    window:
        id 'window'
        background None
        $ timeofday = persistent.timeofday
        if (persistent.font_size == 'large'):
            imagebutton:
                action ShowMenu('text_history')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/backward_%s.png')))
                xpos 38
                ypos 924
            add (get_image((('gui/dialogue_box/' + timeofday) + '/dialogue_box_large.png'))):
                xpos 174
                ypos 866
            imagebutton:
                action HideInterface()
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/hide_%s.png')))
                xpos 1508
                ypos 883
            imagebutton:
                action ShowMenu('save')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/save_%s.png')))
                xpos 1567
                ypos 883
            imagebutton:
                action ShowMenu('game_menu_selector')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/menu_%s.png')))
                xpos 1625
                ypos 883
            imagebutton:
                action ShowMenu('load')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/load_%s.png')))
                xpos 1682
                ypos 883
            imagebutton:
                action Skip()
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/forward_%s.png')))
                xpos 1768
                ypos 924
            text what:
                xpos 194
                line_spacing 1
                xmaximum 1541
                ypos 914
                id 'what'
                size 35
            if who:
                text who:
                    xpos 194
                    line_spacing 1
                    ypos 877
                    id 'who'
                    size 35
        elif (persistent.font_size == 'small'):
            imagebutton:
                action ShowMenu('text_history')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/backward_%s.png')))
                xpos 38
                ypos 949
            add (get_image((('gui/dialogue_box/' + timeofday) + '/dialogue_box.png'))):
                xpos 174
                ypos 916
            imagebutton:
                action HideInterface()
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/hide_%s.png')))
                xpos 1508
                ypos 933
            imagebutton:
                action ShowMenu('save')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/save_%s.png')))
                xpos 1567
                ypos 933
            imagebutton:
                action ShowMenu('game_menu_selector')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/menu_%s.png')))
                xpos 1625
                ypos 933
            imagebutton:
                action ShowMenu('load')
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/load_%s.png')))
                xpos 1682
                ypos 933
            imagebutton:
                action Skip()
                auto (get_image((('gui/dialogue_box/' + timeofday) + '/forward_%s.png')))
                xpos 1768
                ypos 949
            text what:
                xpos 194
                line_spacing 2
                xmaximum 1541
                ypos 964
                id 'what'
                size 28
            if who:
                text who:
                    xpos 194
                    line_spacing 2
                    ypos 931
                    id 'who'
                    size 28

screen nvl:
    modal False
    $ timeofday = persistent.timeofday
    window:
        right_padding 175
        xfill True
        yalign 0.5
        top_padding 150
        background (Frame(get_image((('gui/choice/' + timeofday) + '/choice_box.png')), 50, 50))
        yfill True
        left_padding 175
        bottom_padding 150
        vbox:
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if (persistent.font_size == 'large'):
                            if (who is not None):
                                text who:
                                    id who_id
                                    size 35
                            text what:
                                id what_id
                                size 35
                        elif (persistent.font_size == 'small'):
                            if (who is not None):
                                text who:
                                    id who_id
                                    size 28
                            text what:
                                id what_id
                                size 28
            if items:
                vbox:
                    id 'menu'
                    for caption, action, chosen in items:
                        if action:
                            button:
                                action action
                                style 'nvl_menu_choice_button'
                                text caption:
                                    style 'nvl_menu_choice'
                        else:
                            text caption:
                                style 'nvl_dialogue'
    imagebutton:
        action ShowMenu('text_history')
        auto (get_image((('gui/dialogue_box/' + timeofday) + '/backward_%s.png')))
        xpos 38
        ypos 924

init:
    python:
        
        def gallery_tab_action_inner(mode):
            persistent.gallery_mode = mode
            persistent.gallery_page = 0
            renpy.restart_interaction()
        def gallery_tab_action(mode):
            return lambda: gallery_tab_action_inner(mode)
        
        def gallery_page_action_inner(dp):
            persistent.gallery_page += dp
            renpy.restart_interaction()
        def gallery_page_action(dp):
            return lambda: gallery_page_action_inner(dp)
        
        def gallery_image_action_inner(item):
            persistent.gallery_item = item
            return ShowMenu("gallery_item")()
        def gallery_image_action(item):
            return lambda: gallery_image_action_inner(item)
        
        gallery_grid = {}
        gallery_grid["bg"] = [
                    ["bus_stop", "ext_aidpost_day", "ext_aidpost_night"],
                    ["ext_bathhouse_night", "ext_beach_day", "ext_beach_night"],
                    ["ext_beach_sunset", "ext_boathouse_day", "ext_boathouse_night"],
                    ["ext_bus", "ext_bus_night", "ext_camp_entrance_day"],
                    ["ext_camp_entrance_night", "ext_clubs_day", "ext_clubs_night"],
                    ["ext_dining_hall_away_day", "ext_dining_hall_away_night", "ext_dining_hall_away_sunset"],
                    ["ext_dining_hall_near_day", "ext_dining_hall_near_night", "ext_dining_hall_near_sunset"],
                    ["ext_house_of_dv_day", "ext_house_of_dv_night", "ext_house_of_mt_day"],
                    ["ext_house_of_mt_night", "ext_house_of_mt_night_without_light", "ext_house_of_mt_sunset"],
                    ["ext_house_of_sl_day", "ext_house_of_un_day", "ext_houses_day"],
                    ["ext_houses_sunset", "ext_island_day", "ext_island_night"],
                    ["ext_library_day", "ext_library_night", "ext_musclub_day"],
                    ["ext_no_bus", "ext_no_bus_night", "ext_no_bus_sunset"],
                    ["ext_old_building_night", "ext_old_building_night_moonlight", "ext_path_day"],
                    ["ext_path_night", "ext_path_sunset", "ext_path2_day"],
                    ["ext_path2_night", "ext_playground_day", "ext_playground_night"],
                    ["ext_polyana_day", "ext_polyana_night", "ext_polyana_sunset"],
                    ["ext_road_day", "ext_road_night", "ext_road_night2"],
                    ["ext_road_sunset", "ext_square_day", "ext_square_day_city"],
                    ["ext_square_night", "ext_square_night_party", "ext_square_night_party2"],
                    ["ext_square_sunset", "ext_stage_big_night", "ext_stage_normal_day"],
                    ["ext_stage_normal_night", "ext_washstand_day", "ext_washstand2_day"],
                    ["int_aidpost_day", "int_aidpost_day_apple", "int_aidpost_night"],
                    ["int_bus", "int_bus_black", "int_bus_night"],
                    ["int_bus_people_day", "int_bus_people_night", "int_catacombs_door"],
                    ["int_catacombs_entrance", "int_catacombs_hole", "int_catacombs_living"],
                    ["int_catacombs_living_nodoor", "int_clubs_male_day", "int_clubs_male_sunset"],
                    ["int_clubs_male2_night", "int_clubs_male2_night_nolight", "int_dining_hall_day"],
                    ["int_dining_hall_night", "int_dining_hall_people_day", "int_dining_hall_sunset"],
                    ["int_house_of_dv_day", "int_house_of_dv_night", "int_house_of_mt_day"],
                    ["int_house_of_mt_night", "int_house_of_mt_night2", "int_house_of_mt_noitem_night"],
                    ["int_house_of_mt_sunset", "int_house_of_sl_day", "int_house_of_un_day"],
                    ["int_house_of_un_night", "int_liaz", "int_library_day"],
                    ["int_library_night", "int_library_night2", "int_mine"],
                    ["int_mine_coalface", "int_mine_crossroad", "int_mine_door"],
                    ["int_mine_exit_night_light", "int_mine_exit_night_nolight", "int_mine_exit_night_torch"],
                    ["int_mine_halt", "int_mine_room", "int_musclub_day"],
                    ["int_old_building_night", "intro_xx", "semen_room"],
                    ["semen_room_window"]
                ]
        gallery_grid["cg"] = [
                    ["d1_food_normal", "d1_food_skolop", "d1_grasshopper"],
                    ["d1_rena_sunset", "d1_sl_dinner", "d1_sl_dinner_0"],
                    ["d1_uv", "d1_uv_2", "d2_2ch_beach"],
                    ["d2_lineup", "d2_micu_lib", "d2_miku_piano"],
                    ["d2_miku_piano2", "d2_mirror", "d2_mt_undressed"],
                    ["d2_mt_undressed_2", "d2_slavya_forest", "d2_sovenok"],
                    ["d2_ussr_falling", "d2_water_dan", "d3_disco"],
                    ["d3_dv_guitar", "d3_dv_scene_1", "d3_dv_scene_2"],
                    ["d3_sl_bathhouse", "d3_sl_dance", "d3_sl_evening"],
                    ["d3_sl_library", "d3_soccer", "d3_un_dance"],
                    ["d3_un_forest", "d3_us_dinner", "d3_us_library_1"],
                    ["d3_us_library_2", "d3_us_library_3", "d3_us_library_4"],
                    ["d3_ussr_catched", "d4_catac", "d4_catac_dv"],
                    ["d4_catac_sl", "d4_catac_un", "d4_catac_us"],
                    ["d4_catac_us_2", "d4_dv_mt", "d4_el_wash"],
                    ["d4_mi_guitar", "d4_mi_sing", "d4_sh_sit"],
                    ["d4_sh_stay", "d4_us_cancer", "d4_us_morning"],
                    ["d4_uv", "d4_uv_1", "d5_boat"],
                    ["d5_boat_2", "d5_cake", "d5_clubs_robot"],
                    ["d5_cs", "d5_dv_argue", "d5_dv_argue_2"],
                    ["d5_dv_argue_3", "d5_dv_island", "d5_dv_us_wash"],
                    ["d5_dv_us_wash_2", "d5_dv_us_wash_3", "d5_dv_us_wash_4"],
                    ["d5_mi", "d5_sh_us", "d5_sl_sleep"],
                    ["d5_sl_sleep_2", "d5_strawberry_race", "d5_un_island"],
                    ["d5_un_sleep", "d5_us_ghost", "d5_us_ghost_2"],
                    ["d5_us_kiss", "d5_us_sit", "d5_uv"],
                    ["d5_uv_2", "d6_dv_fight", "d6_dv_fight_2"],
                    ["d6_dv_fight_3", "d6_dv_hentai", "d6_dv_hentai_2"],
                    ["d6_pioneer", "d6_sl_forest", "d6_sl_forest_2"],
                    ["d6_sl_swim", "d6_sl_hentai_1", "d6_sl_hentai_2"],
                    ["d6_un_evening_1", "d6_un_evening_2", "d6_un_punch"],
                    ["d6_us_film", "d6_us_night_2", "d6_uv"],
                    ["d6_uv_2", "d7_dv", "d7_dv_2"],
                    ["d7_pioneers_leaving", "d7_pioneers_leaving_without_us", "d7_sl_morning"],
                    ["d7_sl_morning_2", "d7_un_hentai", "d7_un_hentai_3"],
                    ["d7_un_suicide", "d7_uv", "day4_us_morning"],
                    ["epilogue_dv_2", "epilogue_dv_3", "epilogue_mi_1"],
                    ["epilogue_mi_2", "epilogue_mi_3", "epilogue_mi_4"],
                    ["epilogue_mi_5", "epilogue_mi_6", "epilogue_mi_7"],
                    ["epilogue_mi_8", "epilogue_mi_9", "epilogue_sl"],
                    ["epilogue_sl_2", "epilogue_un", "epilogue_un_bad"],
                    ["epilogue_un_good", "epilogue_us", "epilogue_us_3_a"],
                    ["epilogue_us_alone", "epilogue_uv", "epilogue_uv_2"],
                    ["epilogue_uv_3", "miku_h_1_cenz", "miku_h_2_cenz"],
                    ["final_all_2", "uvao_h_cenz", "d2_sl_swim"]
                ]
        gallery_grid["sp"] = [
                    [("sl normal pioneer","normal"), ("sl serious pioneer","serious"), ("sl smile pioneer","smile")],
                    [("sl laugh pioneer","laugh"), ("sl shy pioneer","shy"), ("sl smile2 pioneer","smile2")],
                    [("sl happy pioneer","happy"), ("sl angry pioneer","angry"), ("sl sad pioneer","sad")],
                    [("sl surprise pioneer","surprise"), ("sl tender pioneer","tender"), ("sl scared pioneer","scared")],
                    [("un normal pioneer","normal"), ("un shy pioneer","shy"), ("un smile pioneer","smile")],
                    [("un angry pioneer","angry"), ("un evil_smile pioneer","evil_smile"), ("un smile2 pioneer","smile2")],
                    [("un cry pioneer","cry"), ("un scared pioneer","scared"), ("un shocked pioneer","shocked")],
                    [("un surprise pioneer","surprise"), ("un sad pioneer","sad"), ("un cry_smile pioneer","cry_smile")],
                    [("un rage pioneer","rage"), ("un serious pioneer","serious"), ("un grin pioneer","grin")],
                    [("un laugh pioneer","laugh"), ("un smile3 pioneer","smile3"), ("dv rage pioneer","rage")],
                    [("dv cry pioneer","cry"), ("dv scared pioneer","scared"), ("dv shocked pioneer","shocked")],
                    [("dv surprise pioneer","surprise"), ("dv laugh pioneer","laugh"), ("dv guilty pioneer","guilty")],
                    [("dv sad pioneer","sad"), ("dv shy pioneer","shy"), ("dv grin pioneer","grin")],
                    [("dv normal pioneer","normal"), ("dv smile pioneer","smile"), ("dv angry pioneer","angry")],
                    [("us sad pioneer","sad"), ("us grin pioneer","grin"), ("us laugh pioneer","laugh")],
                    [("us laugh2 pioneer","laugh2"), ("us normal pioneer","normal"), ("us smile pioneer","smile")],
                    [("us angry pioneer","angry"), ("us calml pioneer","calml"), ("us dontlike pioneer","dontlike")],
                    [("us fear pioneer","fear"), ("us upset pioneer","upset"), ("us cry pioneer","cry")],
                    [("us cry2 pioneer","cry2"), ("us shy pioneer","shy"), ("us shy2 pioneer","shy2")],
                    [("us surp1 pioneer","surp1"), ("us surp2 pioneer","surp2"), ("us surp3 pioneer","surp3")],
                    [("mt normal pioneer","normal"), ("mt scared pioneer","scared"), ("mt surprise pioneer","surprise")],
                    [("mt sad pioneer","sad"), ("mt smile pioneer","smile"), ("mt angry pioneer","angry")],
                    [("mt laugh pioneer","laugh"), ("mt rage pioneer","rage"), ("mt grin pioneer","grin")],
                    [("mt shocked pioneer","shocked"), ("mi normal pioneer","normal"), ("mi serious pioneer","serious")],
                    [("mi smile pioneer","smile"), ("mi grin pioneer","grin"), ("mi upset pioneer","upset")],
                    [("mi angry pioneer","angry"), ("mi rage pioneer","rage"), ("mi happy pioneer","happy")],
                    [("mi surprise pioneer","surprise"), ("mi sad pioneer","sad"), ("mi shocked pioneer","shocked")],
                    [("mi shy pioneer","shy"), ("mi scared pioneer","scared"), ("mi laugh pioneer","laugh")],
                    [("mi dontlike pioneer","dontlike"), ("mi cry pioneer","cry"), ("mz normal glasses pioneer","normal")],
                    [("mz bukal glasses pioneer","bukal"), ("mz laugh glasses pioneer","laugh"), ("mz angry glasses pioneer","angry")],
                    [("mz rage glasses pioneer","rage"), ("mz shy glasses pioneer","shy"), ("mz smile glasses pioneer","smile")],
                    [("uv normal","normal"), ("uv smile","smile"), ("uv dontlike","dontlike")],
                    [("uv rage","rage"), ("uv sad","sad"), ("uv shocked","shocked")],
                    [("uv grin","grin"), ("uv laugh","laugh"), ("uv surprise","surprise")],
                    [("uv upset","upset"), ("uv guilty","guilty"), ("uv surprise2","surprise2")],
                    [("cs smile","smile"), ("cs normal", "normal"), ("cs shy", "shy")],
                    [("el grin pioneer","grin"), ("el smile pioneer","smile"), ("el normal pioneer","normal")],
                    [("el laugh pioneer","laugh"), ("el sad pioneer","sad"), ("el scared pioneer","scared")],
                    [("el shocked pioneer","shocked"), ("el surprise pioneer","surprise"), ("el upset pioneer","upset")],
                    [("el angry pioneer","angry"), ("el serious pioneer","serious"), ("sh normal pioneer","normal")],
                    [("sh smile pioneer","smile"), ("sh scared pioneer","scared"), ("sh upset pioneer","upset")],
                    [("sh laugh pioneer","laugh"), ("sh cry pioneer","cry"), ("sh rage pioneer","rage")],
                    [("sh normal_smile pioneer","normal_smile"), ("sh surprise pioneer","surprise"), ("sh serious pioneer","serious")],
                    [("pi",""), ("pi smile","")]
                ]
screen gallery_item:
    tag menu
    modal False
    $ img = ImageReference(persistent.gallery_item)
    imagebutton:
        action ShowMenu('gallery')
        idle img
        hover img

screen gallery:
    tag menu
    modal False
    $ persistent.sprite_time = 'day'
    if (persistent.gallery_mode not in ['bg', 'cg', 'sp']):
        $ persistent.gallery_mode = 'bg'
        $ persistent.gallery_page = 0
    if (not isinstance(persistent.gallery_page, int)):
        $ persistent.gallery_page = 0
    $ ui.image(get_image((('gui/gallery/gallery_' + persistent.gallery_mode) + '.jpg')), id=_1)
    $ (gallery_l, gallery_r) = {'bg': ('cg', 'sp'), 'cg': ('sp', 'bg'), 'sp': ('bg', 'cg')}[persistent.gallery_mode]
    imagebutton:
        action gallery_tab_action(gallery_l)
        auto (get_image((('gui/gallery/' + gallery_l) + '_%s.png')))
        yalign 0.08
        xalign 0.1
    imagebutton:
        action gallery_tab_action(gallery_r)
        auto (get_image((('gui/gallery/' + gallery_r) + '_%s.png')))
        yalign 0.08
        xalign 0.9
    if (persistent.gallery_mode in ['bg', 'cg']):
        $ (gallery_min, gallery_max) = ((persistent.gallery_page * 3), ((persistent.gallery_page * 3) + 3))
        for i, gallery_line in enumerate(gallery_grid[persistent.gallery_mode][gallery_min:gallery_max]):
            for j, gallery_item in enumerate(gallery_line):
                $ (x, y) = ((0.3 + (j * 0.25)), (0.3 + (i * 0.25)))
                if ((persistent.gallery_mode, gallery_item) in persistent._seen_images):
                    python:
                        _t = im.Crop(ImageReference((persistent.gallery_mode, gallery_item)), (0, 0, 1920, 1080))
                        th = im.Scale(_t, 320, 180)
                        img = im.Composite((336, 196), (8, 8), im.Alpha(th, 0.5), (0, 0), im.Image(get_image('gui/gallery/thumbnail_idle.png')))
                        imgh = im.Composite((336, 196), (8, 8), th, (0, 0), im.Image(get_image('gui/gallery/thumbnail_hover.png')))
                    imagebutton:
                        xalign x
                        hover imgh
                        yalign y
                        idle img
                        action (gallery_image_action((persistent.gallery_mode, gallery_item)))
                else:
                    imagebutton:
                        action ShowMenu('gallery')
                        auto get_image('gui/gallery/not_opened_%s.png')
                        yalign y
                        xalign x
    if (persistent.gallery_mode in ['sp']):
        $ (gallery_min, gallery_max) = (persistent.gallery_page, (persistent.gallery_page + 1))
        for j, gallery_item in enumerate(gallery_grid[persistent.gallery_mode][gallery_min]):
            $ (x, y) = ((0.28 + (j * 0.22)), 0.55)
            if ((gallery_item[0] in persistent._seen_images) or (tuple(gallery_item[0].split(' ')) in persistent._seen_images)):
                window:
                    xalign x
                    yalign y
                    ymaximum 750
                    top_padding 0
                    xmaximum 270
                    background Solid('#ffffff80')
                    left_padding 0
                    add ImageReference(gallery_item[0]):
                        zoom 0.69
                        crop ((250, 0, 390, 1080))
                        ypos 7
                python:
                    img = im.Image(get_image('gui/gallery/thumbnail_sp_idle.png'))
                    imgh = im.Image(get_image('gui/gallery/thumbnail_sp_hover.png'))
                imagebutton:
                    xalign x
                    hover imgh
                    yalign y
                    idle img
                    action gallery_image_action(gallery_item[0])
            else:
                imagebutton:
                    action ShowMenu('gallery')
                    auto get_image('gui/gallery/not_opened_sp_%s.png')
                    yalign y
                    xalign x
    if (persistent.gallery_page > 0):
        imagebutton:
            action gallery_page_action(-1)
            auto get_image('gui/gallery/backward_%s.png')
            yalign 0.5
            xalign 0.05
    if (gallery_max < len(gallery_grid[persistent.gallery_mode])):
        imagebutton:
            action gallery_page_action((+1))
            auto get_image('gui/gallery/forward_%s.png')
            yalign 0.5
            xalign 0.95
    imagebutton:
        action Return()
        auto get_image('gui/gallery/back_%s.png')
        yalign 0.92
        xalign 0.03
    python:
        _a = (len(gallery_grid[persistent.gallery_mode]) / 3)
        if (persistent.gallery_mode == 'sp'):
            _a = len(gallery_grid[persistent.gallery_mode])
        pages = ((str((persistent.gallery_page + 1)) + '/') + str(_a))
    text pages:
        xalign 0.5
        style 'normal_day'
        yalign 0.92

label quit:
label _compat_confirm_quit:
    python:
        
        ex_map_points = (
                        (980, 520, 1150, 640, True),
                        (1400, 520, 1570, 640, False),
                        )
        result = renpy.imagemap(
                        get_image("maps/exit.jpg"),
                        get_image("maps/exit_selected.jpg"),
                        ex_map_points
                    )
    if result:
        $ renpy.quit()
    else:
        if renpy.context()._main_menu:
            $ renpy.transition(config.game_main_transition)
            jump _main_menu_screen
        else:
            return
init -3:
    python:
        
        
        
        
        
        style.readback_window = Style(style.nvl_window)
        '''style.readback_window.xmaximum = 760
            style.readback_window.ymaximum = 500
            style.readback_window.align = (.5, .5)'''
        
        style.readback_frame.background = None
        style.readback_frame.xpadding = 10
        style.readback_frame.xmargin = 5
        style.readback_frame.ymargin = 5
        
        style.readback_text.color = "#ffdd7d"
        
        '''style.create("readback_button", "readback_text")
            style.readback_button.background = None
            
            style.create("readback_button_text", "readback_text")
            style.readback_button_text.selected_color = "#f12"
            style.readback_button_text.hover_color = "#f12"'''
        
        style.readback_label_text.bold = True
        style.readback_label_text.color = "#ffffff"
        
        
        config.locked = False 
        
        
        config.readback_buffer_length = 100 
        config.readback_full = False 
        config.readback_disallowed_tags = ["size"] 
        config.readback_choice_prefix = ">> "   
        
        
        config.locked = True
init -2:
    python:
        
        
        
        class ReadbackADVCharacter(ADVCharacter):
            def do_done(self, who, what):
                store_say(who, what)
                store.current_voice = ''
                return
        
        class ReadbackNVLCharacter(NVLCharacter):
            def do_done(self, who, what):
                store_say(who, what)
                store.current_voice = ''
                return
        
        
        def say_wrapper(who, what, **kwargs):
            store_current_line(who, what)
            return renpy.show_display_say(who, what, **kwargs)
        
        config.nvl_show_display_say = say_wrapper
        
        adv = ReadbackADVCharacter(show_function=say_wrapper)
        nvl = ReadbackNVLCharacter()
        NVLCharacter = ReadbackNVLCharacter
        
        
        def voice(file, **kwargs):
            if not config.has_voice:
                return
            
            _voice.play = file
            
            store.current_voice = file
        
        
        
        def menu(items, **add_input): 
            
            newitems = []
            for label, val in items:
                if val == None:
                    narrator(label, interact=False)
                else:
                    newitems.append((label, val))
            
            rv = renpy.display_menu(newitems, **add_input)
            
            
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
        
        def nvl_screen_dialogue(): 
            """
                 Returns widget_properties and dialogue for the current NVL
                 mode screen.
                 """
            
            widget_properties = { }
            dialogue = [ ]
            
            for i, entry in enumerate(nvl_list):
                if not entry:
                    continue
                
                who, what, kwargs = entry
                
                if i == len(nvl_list) - 1:
                    who_id = "who"
                    what_id = "what"
                    window_id = "window"
                
                else:
                    who_id = "who%d" % i
                    what_id = "what%d" % i
                    window_id = "window%d" % i
                
                widget_properties[who_id] = kwargs["who_args"]
                widget_properties[what_id] = kwargs["what_args"]
                widget_properties[window_id] = kwargs["window_args"]
                
                dialogue.append((who, what, who_id, what_id, window_id))
            
            return widget_properties, dialogue
        
        
        def nvl_menu(items):
            
            renpy.mode('nvl_menu')
            
            if nvl_list is None:
                store.nvl_list = [ ]
            
            screen = None
            
            if renpy.has_screen("nvl_choice"):
                screen = "nvl_choice"
            elif renpy.has_screen("nvl"):
                screen = "nvl"
            
            if screen is not None:
                
                widget_properties, dialogue = nvl_screen_dialogue()        
                
                rv = renpy.display_menu(
                        items,
                        widget_properties=widget_properties,
                        screen=screen,
                        scope={ "dialogue" : dialogue },
                        window_style=style.nvl_menu_window,
                        choice_style=style.nvl_menu_choice,
                        choice_chosen_style=style.nvl_menu_choice_chosen,
                        choice_button_style=style.nvl_menu_choice_button,
                        choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                        type="nvl",                      
                        )
                
                for label, val in items:
                    if rv == val:
                        store.current_voice = ''
                        store_say(None, config.readback_choice_prefix + label)
                return rv
            
            
            ui.layer("transient")
            ui.clear()
            ui.close()
            
            ui.window(style=_m1_screens__s(style.nvl_window))
            ui.vbox(style=_m1_screens__s(style.nvl_vbox))
            
            for i in nvl_list:
                if not i:
                    continue
                
                who, what, kw = i            
                rv = renpy.show_display_say(who, what, **kw)
            
            renpy.display_menu(items, interact=False,
                                   window_style=_m1_screens__s(style.nvl_menu_window),
                                   choice_style=_m1_screens__s(style.nvl_menu_choice),
                                   choice_chosen_style=_m1_screens__s(style.nvl_menu_choice_chosen),
                                   choice_button_style=_m1_screens__s(style.nvl_menu_choice_button),
                                   choice_chosen_button_style=_m1_screens__s(style.nvl_menu_choice_chosen_button),
                                   )
            
            ui.close()
            
            roll_forward = renpy.roll_forward_info()
            
            rv = ui.interact(roll_forward=roll_forward)
            renpy.checkpoint(rv)
            
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
        
        
        readback_buffer = []
        current_line = None
        current_voice = None
        
        def store_say(who, what):
            global readback_buffer, current_voice
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()
        
        def store_current_line(who, what):
            global current_line, current_voice
            current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
        
        
        disallowed_tags_regexp = ""
        for tag in config.readback_disallowed_tags:
            if disallowed_tags_regexp != "":
                disallowed_tags_regexp += "|"
            disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
        
        import re
        remove_tags_expr = re.compile(disallowed_tags_regexp) 
        def preparse_say_for_store(input):
            global remove_tags_expr
            if input:
                return re.sub(remove_tags_expr, "", input)
        
        def readback_prune():
            global readback_buffer
            while len(readback_buffer) > config.readback_buffer_length:
                del readback_buffer[0]
        
        
        def readback_catcher():
            ui.add(renpy.Keymap(rollback=(SetVariable("yvalue", 1.0), ShowMenu("text_history"))))
            ui.add(renpy.Keymap(rollforward=ui.returns(None)))
        
        if config.readback_full:
            config.rollback_enabled = False
            config.overlay_functions.append(readback_catcher)    
init:
    python:
        
        yvalue = 1.0
        class NewAdj(renpy.display.behavior.Adjustment):
            def change(self,value):
                
                if value > self._range and self._value == self._range:
                    return Return()
                else:
                    return renpy.display.behavior.Adjustment.change(self, value)
        
        def store_yvalue(y):
            global yvalue
            yvalue = int(y)
screen text_history:
    tag menu
    modal False
    if ((not current_line) and (len(readback_buffer) == 0) and d2_cardgame_block_rollback):
        $ lines_to_show = []
    elif ((not current_line) and (len(readback_buffer) == 0)):
        $ lines_to_show = []
    elif (current_line and (len(readback_buffer) == 0)):
        $ lines_to_show = [current_line]
    elif (current_line and (not ((current_line == readback_buffer[-1]) or False) if (len(readback_buffer) == 1) else (current_line == readback_buffer[-2]))):
        $ lines_to_show = (readback_buffer + [current_line])
    else:
        $ lines_to_show = readback_buffer
    $ adj = NewAdj(changed=store_yvalue, step=300)
    window:
        style_group 'readback'
        side ('c r'):
            frame:
                $ vp = ui.viewport(mousewheel=True, offsets=(0.0, yvalue), yadjustment=adj)
                vbox:
                    null:
                        height 10
                    python:
                        count = 1
                        total = 0
                        mass = lines_to_show
                        for i in mass:
                            if i[1]:
                                if (not i[2]):
                                    total+=1
                    for line in lines_to_show:
                        if (line[0] and (line[0] != ' ')):
                            label line[0]
                        if line[1]:
                            if (not line[2]):
                                python:
                                    cn = (total - count)
                                    count+=1
                                if (persistent.font_size == 'small'):
                                    textbutton line[1]:
                                        style 'log_button'
                                        text_style 'log_button_text'
                                        action (FunctionCallback(do_rollback, cn))
                                        text_size 28
                                elif (persistent.font_size == 'large'):
                                    textbutton line[1]:
                                        style 'log_button'
                                        text_style 'log_button_text'
                                        action (FunctionCallback(do_rollback, cn))
                                        text_size 35
                                else:
                                    null:
                                        height 1
                            else:
                                textbutton line[1]:
                                    action (Play('voice', line[2]))
                        null:
                            height 10
                    python:
                        count = None
                        total = None
                        mass = None
                    imagebutton:
                        action Return()
                        auto get_image('gui/save_load/back_%s.png')
                        align ((0.03, 1.0))


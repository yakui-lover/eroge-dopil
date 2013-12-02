init 2:

    $ lp_mt = 0
    image ug normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "sample.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "sample.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "sample.png") )
    
init 2 python:
    global DynamicCharacter
    global _show_two_window
    global nvl
    global store
    global time_of_day
    th_prefix = "«"
    th_suffix = "»"
    colors['ug'] = {'night': (109, 45, 175, 255), 'sunset': (109, 45, 175, 255), 'day': (109, 45, 175, 255), 'prolog': (109, 45, 175, 255)}
    store.names_list.append('ug')
    make_names_unknown()
    set_mode_adv()
    reload_names()
    
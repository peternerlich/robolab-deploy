def build_call(password):
    #the command that reloads the python modules in tmux and attaches to the
    # session afterwards
    tmux_command = 'tmux -S /tmp/tmux/shared send -t ev3-robolab-startup \
    "reloader.enable(blacklist=[\'ev3dev\',\'ev3dev.ev3\',\'ev3\',\'typing\'])" ENTER \
    "reloader.reload(main)" ENTER \
    "main.run()" ENTER; \
    tmux -S /tmp/tmux/shared attach -t ev3-robolab-startup'

    tmux_cls = '"import os" ENTER "os.system(\'clear\')" ENTER'
    #tmux_cls = '"import os" ENTER "os.system(\'tmux -S /tmp/tmux/shared send-keys -t ev3-robolab-startup -R\; send-keys -t ev3-robolab-startup C-l\;\')" ENTER'

    # hey, I just met you and this is crazy...
    systemd_error = "\"beautiful_statement_and_noone_will_use_this_var = \'\
    \\033[31m################################################################################\\n\
    \\033[31m#\\033[0m\\033[93m                                                                              \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m          NOTICE - THE TMUX SESSION OR PYTHON WAS NOT RUNNING. SAD!           \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m                                                                              \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m It looks like you\\'ve somehow messed with our systemd service. DUH!           \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m                                                                              \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m Please stop doing so. Simply detach from the tmux session by pressing        \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m >>>>>>>>>>>>>>>>>>>>>> CTRL + B followed by hitting D <<<<<<<<<<<<<<<<<<<<<< \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m                                                                              \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m Thank you, we appreciate your cooperation. :)                                \\033[31m#\\n\
    \\033[31m#\\033[0m\\033[93m                                                                              \\033[31m#\\n\
    \\033[31m################################################################################\\033[0m\'\" ENTER"

    systemd_error_print =  '"print(beautiful_statement_and_noone_will_use_this_var)" ENTER'
    
    ig0r_msg = "\"beautiful_statement_and_noone_will_use_this_var_either = \'\
    \\033[31m____  ______   \\033[37m_______\\033[31m ________ \\n\
    )  ( /  ____\ \\033[37m/  ___  \\\\\\\\\\033[31m)   __  \ \\n\
    |  |/  /  ___\\033[37m|  /   \  |\\033[31m  |__)  ) \\n\
    |  |  |  )_  \\033[37m| | \\033[35m[\\033[31m0\\033[35m]\\033[37m | |\\033[31m   _   /    \\033[35m[\\033[31m0\\033[35m]\\033[35m \\n\
    |  |\  \__/  \\033[37m|  \___/  |\\033[31m  | \  \ \\n\
    )__( \_____/_|\\033[37m\_______/\\033[31m|__|  \__\ \\n\
    \\n\
    \\033[0m   \`       [    \\033[31mOBEY.\\033[0m   ]       \` \'\" ENTER"

    ig0r_msg_col = "\"beautiful_statement_and_noone_will_use_this_var_either = \'\
    \\033[31m____  ______   \\033[30m_______ \\033[31m________ \\n\
    \\033[40;31m)  (\\033[00;31m \\033[40;31m/  ____\\\\\\\\\\033[00;37m \\033[41;30m/  ___  \\\\\\\\\\033[40;31m)   __  \\\\\\\\\\033[00;31m \\n\
    \\033[40;31m|  |/  /\\033[00;31m  ___\\033[41;30m|  /\\033[00;30m   \\033[41;30m\  |\\033[40;31m  |\\033[00;31m__\\033[40;31m)  )\\033[00;31m \\n\
    \\033[40;31m|  |  |\\033[00;31m  \\033[40;31m)_  \\033[41;30m| |\\033[00;30m \\033[47;35m[\\033[47;31m0\\033[47;35m]\\033[00;30m \\033[41;30m| |\\033[40;31m   _   /\\033[00;35m    \\033[47;35m[\\033[31m0\\033[35m]\\033[00;35m \\n\
    \\033[40;31m|  |\  \\\\\\\\\\033[00;31m__\\033[40;31m/  \\033[41;30m|  \\\\\\\\\\033[00;30m___\\033[41;30m/  |\\033[40;31m  |\\033[00;31m \\033[40;31m\  \\\\\\\\\\033[00;31m \\n\
    \\033[40;31m)__(\\033[00;31m \\033[40;31m\_____/_|\\033[41;30m\_______/\\033[40;31m|__|\\033[00;31m  \\033[40;31m\__\\\\\\\\\\033[00;0m \\n\
    \\n\
    \\033[1;0m   \`       [   \\033[40;31m OBEY.\\033[00;0m   ]       \` \'\" ENTER"

    ig0r_msg_print =  '"print(beautiful_statement_and_noone_will_use_this_var_either)" ENTER'


    # command = "; ".join((backup_command, tmux_command))
    #systemd_command ='if ! (tmux -S /tmp/tmux/shared has-session -t \
    #"ev3-robolab-startup" 2> /dev/null); \
    systemd_command_if = 'if ! (systemctl status ev3-robolab-startup \
    | grep "python" 1> /dev/null); \
    then echo "{}" | sudo -S systemctl restart ev3-robolab-startup'.format(password)

    tmux_send = 'tmux -S /tmp/tmux/shared send -t ev3-robolab-startup'
    tmux_blacklist = '"reloader.enable(blacklist=[\'ev3dev\',\'ev3dev.ev3\',\'ev3\',\'typing\'])" ENTER'
    tmux_reload = '"reloader.reload(main)" ENTER'
    tmux_run = '"main.run()" ENTER'

    tmux_attach = 'tmux -S /tmp/tmux/shared attach -t ev3-robolab-startup'

    command = "; ".join((systemd_command_if, tmux_send + ' ' +
                         systemd_error + ' ' + tmux_cls, tmux_send + ' ' + systemd_error_print + ' ' + tmux_run, 'sleep 15s',
                         'else ' + tmux_send + ' ' + tmux_blacklist + ' '+ tmux_reload + ' ' + ig0r_msg + ' ' + tmux_cls + ' ' + ig0r_msg_print + ' ' + tmux_run, 'fi',
                        tmux_attach))
    return command
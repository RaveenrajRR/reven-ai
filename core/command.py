from control.apps import *
from control.volume import *
from control.system import *
from web.browser import *
from core.voice import speak
from control.youtube import *
from control.keyboard import *
from control.window import *
from core.assistant import *



def execute(command):


    if "youtube" in command:
        youtube()


    elif "screenshot" in command:
        screenshot()

    elif "close" in command:
        app=command.replace(
            "close",
            ""
        ).strip()

        close_app(app)

    elif "mute" in command:
        mute()

    elif "increase" in command:
        volume_up()

    elif "decrease" in command:
        volume_down()

    elif "shutdown" in command:
        shutdown()

    elif "restart" in command:
        restart()

    elif "lock" in command:
        lock()

    elif "open" in command:
        app=command.replace(
            "open",
            ""
        ).strip()
        open_app(app)

    elif "play" in command or "play" in command:
        playpause()

    elif "fullscreen" in command or "full screen" in command:
        fullscreen()

    elif "mute video" in command or "mutevideo" in command:
         mute()

    elif "next video" in command or "nextvideo" in command:
        next_video()

    elif "forward" in command:
        forward()

    elif "backward" in command:
        backward()

    elif "captions" in command:
        captions()

    elif "theater mode" in command:
        theater_mode()

    elif "enter" in command:
        enter()
    
    elif "escape" in command:
        esc()

    elif "tab" in command:
        tab()

    elif "backspace" in command or "back space" in command:
        backspace()

    elif "delete" in command:
        delete()

    elif "insert" in command:
        insert()

    elif "home" in command:
        home() 

    elif "end" in command:
        end()

    elif "pageup" in command or "page up" in command:
        page_up()

    elif "pagedown" in command or "page down" in command:
        page_down()

    elif "up" in command:
        up()

    elif "down" in command:
        down()

    elif "left" in command:
        left()

    elif "right" in command:
        right()

# ----------------------------
# Function Keys
# ----------------------------

    elif "f1" in command or "f 1" in command:
        f1()

    elif "F2" in command or "f 2" in command:
        f2()

    elif "F3" in command or "f 3" in command:
        f3()

    elif "f4" in command or "f 4" in command:
        f4()

    elif "f5" in command or "f 5" in command:
        f5()

    elif "f6" in command or "f 6" in command:
        f6()

    elif "f7" in command or "f 7" in command:
        f7()

    elif "f8" in command or "f 8" in command:
        f8()
    
    elif "f9" in command or "f 9" in command:
        f9()

    elif "f10" in command or "f 10" in command:
        f10()

    elif "f11" in command or "f 11" in command:
        f11()

    elif "f12" in command or "f 12" in command:
        f12()

# ----------------------------
# CTRL Shortcuts
# ----------------------------  

    elif "select all" in command:
        select_all()

    elif "copy" in command:
        copy()

    elif "paste" in command:
        paste()

    elif "cut" in command:
        cut()

    elif "undo" in command:
        undo()

    elif "redo" in command:
        redo()

    elif "save" in command:
        save()

    elif "open file" in command:
        open_file()

    elif "new file" in command:
        new_file()

    elif "print file" in command:
        print_file()

    elif "find" in command:
        find()

    elif "replace" in command or "re place" in command:
        replace()

    elif "refresh" in command or "re fresh" in command:
        find()

    elif "zoom in" in command:
        zoom_in()

    elif "zoom out" in command:
        zoom_out()

    elif "rest zoom" in command:
        reset_zoom()

# ----------------------------
# Browser
# ----------------------------

    elif "new tab" in command:
        new_tab()

    elif "close tab" in command:
        close_tab()

    elif "reopen tab" in command:
        reopen_tab()
    
    elif "next tab" in command:
        next_tab()

    elif "previous tab" in command:
        previous_tab()

# ----------------------------
# Windows
# ----------------------------
     
    elif "alt tab" in command:
        alt_tab()

    elif "task manager" in command:
        task_manager()

    elif "lock pc" in command:
        lock_pc()

    elif "run" in command:
        run()

    elif "explorer" in command:
        explorer()

    elif "settings" in command:
        settings()

    elif "desktop" in command:
        desktop()

    elif "screen short" in command:
        screenshot()

    elif "emoji" in command:
        emoji()

    elif "minimize window" in command:
        minimize_window()

    elif "maximize window" in command:
        maximize_window()

    elif "restore window" in command:
        restore_window()

    elif "close window" in command:
        print(">>> CLOSE WINDOW MATCHED <<<")
        close_window()

    elif "switch window" in command:
        switch_window()

    elif "next window" in command:
        next_window()

    elif "previous window" in command:
        previous_window()

        activate_assistant()

    elif "deactivate" in command:
        deactivate_assistant()

    elif "stop listening" in command:
        deactivate_assistant()

    elif "go to sleep" in command:
        sleep_mode()

    elif "wake up" in command:
        wake_up()

    elif "exit assistant" in command:
        exit_assistant()


    




        
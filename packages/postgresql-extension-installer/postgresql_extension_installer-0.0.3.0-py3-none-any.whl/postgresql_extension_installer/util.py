from textlog import log as tlog

def append_log(text, is_print):
    is_no_file = True if is_print is False else False
    tlog("installer", text, is_print, is_no_file)

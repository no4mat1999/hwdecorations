# -*- coding: utf-8 -*-
from gtk.gdk import *
active_window = window_foreign_new((get_default_root_window().property_get("_NET_ACTIVE_WINDOW")[2][0]))
if active_window.get_decorations() == 0 :
	active_window.set_decorations(DECOR_ALL)
	active_window.focus()
else:
	active_window.set_decorations(0)
window_process_all_updates()

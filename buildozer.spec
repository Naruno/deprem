[app]
title = Deprem-Decentra-Network
package.name = deprem_decentra_network
package.domain = org.decentra_network
source.dir = decentra_network_deprem/
source.include_exts = py,png,jpg,kv,atlas
version = 0.1.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
icon.filename = decentra_network_deprem/gui_lib/images/logo.ico
p4a.local_recipes = recipes/src/python-for-android/recipes/
android.api = 27

[app@gui]
title = Deprem-Decentra-Network-GUI
package.name = deprem_decentra_network_gui
source.dir = decentra_network_deprem/gui/
requirements =  decentra_network==0.43.0, decentra_network_gui==0.43.0

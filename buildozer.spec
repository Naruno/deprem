[app]
title = Deprem-Decentra-Network
package.name = deprem_decentra_network
package.domain = org.decentra_network
source.dir = decentra_network_deprem/
source.include_exts = py,png,jpg,kv,atlas
version = 0.43.0
orientation = landscape
fullscreen = 0
android.permissions = INTERNET
icon.filename = decentra_network_deprem/gui_lib/images/logo.ico
p4a.local_recipes = recipes/src/python-for-android/recipes/
android.api = 27

[app@gui]
title = Deprem-Decentra-Network-GUI
package.name = deprem_decentra_network_gui
source.dir = decentra_network_deprem/gui/
requirements =  decentra_network==0.43.0, Kivy==2.1.0, kivymd==0.104.2, qrcode==7.3.1, kivymd_extensions.sweetalert==0.1.5, plyer==2.1.0, pillow==9.1.1

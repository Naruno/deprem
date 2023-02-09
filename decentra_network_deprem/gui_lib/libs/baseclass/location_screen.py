#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.button import MDFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivymd_extensions.sweetalert import SweetAlert

from decentra_network.lib.settings_system import the_settings, save_settings



class LocationScreen(MDScreen):
    pass



class LocationBox(MDGridLayout):
    cols = 2
    all_wallets = ["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]
    the_location_text = ""
    
    the_dn_settings = the_settings()
    
    print(the_dn_settings)
    #Check the location element is in dic

    if not "location" in the_dn_settings:
        the_location_text = "Yok, Ayarlamak İçin Tıklayın"
    else:
        the_location = the_dn_settings["location"]
        the_location_text = f"{the_location}"

    text = StringProperty(the_location_text)

    FONT_PATH = f"{os.environ['DECENTRAD_ROOT']}/gui_lib/fonts/"

    def reflesh_balance(self):

        self.text = f"{the_settings()['location']}"

    def callback_for_menu_items(self, *args):
        
        a_settings = the_settings()
        the_city = LocationBox.all_wallets[args[0]]

        a_settings["location"] = the_city
        save_settings(a_settings)
        self.reflesh_balance()

    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet(radius=25, radius_from="top")
        data = {}
        

        for wallet in LocationBox.all_wallets:
            number = LocationBox.all_wallets.index(wallet)
            address = wallet
            data[number] = address


        for item in data.items():
            bottom_sheet_menu.add_item(
                f"{str(item[0]+1)} : {item[1]}",
                lambda x, y=item[0]: self.callback_for_menu_items(y),
            )

        bottom_sheet_menu.open()


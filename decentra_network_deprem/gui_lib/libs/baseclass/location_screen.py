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
    text = "Lokasyon: "
    the_dn_settings = the_settings()
    if "location" is not the_dn_settings:
        text += "Yok, Ayarlamak İçin Tıklayın"
    else:
        text += the_dn_settings["location"]



    FONT_PATH = f"{os.environ['DECENTRAD_ROOT']}/gui_lib/fonts/"


    def callback_for_menu_items(self, *args):
        a_settings = the_settings()
        a_settings["location"] = args[0]
        save_settings(a_settings)
        self.text = f"Lokasyon: {args[0]}"

    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet(radius=25, radius_from="top")
        data = {}
        all_wallets = sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]

        for wallet in all_wallets:
            number = all_wallets.index(wallet)
            address = wallet
            data[number] = address


        for item in data.items():
            bottom_sheet_menu.add_item(
                f"{str(item[0])} : {item[1]}",
                lambda x, y=item[0]: self.callback_for_menu_items(y),
            )

        bottom_sheet_menu.open()


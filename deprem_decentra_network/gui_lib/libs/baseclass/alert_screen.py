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

from deprem_decentra_network.decentra_network_integration import Integration
from decentra_network.lib.settings_system import the_settings, save_settings


from plyer import gps

class AlertScreen(MDScreen):
    pass


class Create_Alert_Box(MDGridLayout):
    cols = 2



class AlertBox(MDGridLayout):
    cols = 2

    wallet_alert_dialog = None
    set_pass_dialog = None

    FONT_PATH = f"{os.environ['DECENTRAD_ROOT']}/gui_lib/fonts/"

    def read_pass(self):
        the_current_settins = the_settings()
        return the_settings()["dppas"] if "dppas" in the_current_settins else "123"
    def write_pass(self, widget):
        for obj in self.set_pass_dialog.content_cls.children:
            for sub_obj in obj.children:
                new_settigs = the_settings()
                new_settigs["dppas"] = sub_obj.text
                save_settings(new_settigs)
                self.set_pass_dialog.dismiss()

                sub_obj.text = ""



    def set_pass(self):
        self.set_pass_dialog = SweetAlert()
        self.set_pass_dialog.fire(
            text="Şifre Ayarlama",
            input="Decentra Netwrrk Şifreni Yaz",
            buttons=[MDFlatButton(
                        text="TAMAM",
                        font_size="18sp",
                        font_name=f"{self.FONT_PATH}Poppins-Bold",
                        on_press=self.write_pass,
                    ),]            
        )              

    def show_wallet_alert_dialog(self):
        if not self.wallet_alert_dialog:
            self.wallet_alert_dialog = SweetAlert(
                title="DEPREM OLDU",
                type="alert",
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="İPTAL",
                        on_press=self.dismiss_wallet_alert_dialog,
                        font_size="18sp",
                        font_name=f"{self.FONT_PATH}Poppins-Bold",
                    ),
                    MDFlatButton(
                        text="TAMAM",
                        font_size="18sp",
                        font_name=f"{self.FONT_PATH}Poppins-Bold",
                        on_press=self.create_the_wallet,
                    ),
                ],
            )

        self.wallet_alert_dialog.open()


    def dismiss_wallet_alert_dialog(self, widget):
        self.wallet_alert_dialog.dismiss()

    def create_the_wallet(self, widget):
        try:
            Integration.send(
            action="deprem_decentra_network_deprem_oldu",
            app_data=the_settings()["location"],
            password=self.read_pass(),
            to_user="decentranetworkcommunity"
            )
            SweetAlert().fire(
                title="BAŞARILI",
                text="Gönderildi",
                type="success",
            )            
        except:
            SweetAlert().fire(
                title="HATA",
                text="Gönderilemedi",
                type="error",
            )

        self.dismiss_wallet_alert_dialog(widget)



    def Alert_Create(self):
        self.show_wallet_alert_dialog()







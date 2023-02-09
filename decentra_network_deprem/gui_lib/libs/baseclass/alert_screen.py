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

from decentra_network.accounts.get_balance import GetBalance
from decentra_network.blockchain.block.get_block import GetBlock
from decentra_network.lib.qr import qr
from decentra_network.lib.settings_system import change_wallet
from decentra_network.lib.settings_system import the_settings
from decentra_network.wallet.get_saved_wallet import get_saved_wallet
from decentra_network.wallet.wallet_create import wallet_create
from decentra_network.wallet.wallet_delete import wallet_delete
from decentra_network.wallet.wallet_import import wallet_import

from kivy.clock import mainthread
from plyer import gps

class AlertScreen(MDScreen):
    pass


class Create_Alert_Box(MDGridLayout):
    cols = 2



class AlertBox(MDGridLayout):
    cols = 2


    wallet_alert_dialog = None

    FONT_PATH = f"{os.environ['DECENTRAD_ROOT']}/gui_lib/fonts/"









    def show_wallet_alert_dialog(self):
        if not self.wallet_alert_dialog:
            self.wallet_alert_dialog = SweetAlert(
                title="Creating a wallet",
                type="custom",
                auto_dismiss=False,
                content_cls=Create_Alert_Box(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_press=self.dismiss_wallet_alert_dialog,
                        font_size="18sp",
                        font_name=f"{self.FONT_PATH}Poppins-Bold",
                    ),
                    MDFlatButton(
                        text="OK",
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
        for obj in self.wallet_alert_dialog.content_cls.children:
            for sub_obj in obj.children:
                wallet_create(sub_obj.text)
                self.dismiss_wallet_alert_dialog(widget)

                sub_obj.text = ""

    def Alert_Create(self):
        self.show_wallet_alert_dialog()

    def dismiss_delete_wallet_alert_dialog(self, widget):
        self.delete_wallet_alert_dialog.dismiss()

    def show_delete_wallet_alert_dialog(self):
        if not self.delete_wallet_alert_dialog:
            self.delete_wallet_alert_dialog = SweetAlert(
                title="Deleting a wallet",
                type="custom",
                auto_dismiss=False,
                content_cls=Delete_Alert_Box(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_press=self.dismiss_delete_wallet_alert_dialog,
                        font_size="18sp",
                        font_name=f"{self.FONT_PATH}Poppins-Bold",
                    ),
                    MDFlatButton(
                        text="OK",
                        font_size="18sp",
                        font_name=f"{self.FONT_PATH}Poppins-Bold",
                        on_press=self.delete_the_wallet,
                    ),
                ],
            )

        self.delete_wallet_alert_dialog.open()





"""#!/usr/bin/env python3"""

import bit
import config
import pyqrcode
from bit import Key
from bit.network import get_fee

import time
import guizero
from guizero import App, Text

import scanner

# For images
# filepath = "C:/Users/tbrun/Documents/Dev/Btc_Faucet/"  # windows
filepath = "/home/pi/App/images/"  # rpi


class Faucet:

    """Initializes and controls dedicated btc faucet wallet"""

    def __init__(self):
        self.key = Key(config.private_key)
        self.address = self.key.address
        self.balance = self.key.get_balance("btc")
        self.fee = get_fee(fast=False)

    def send(self, wallet_address):
        # minimum amount that can be sent is .00000546 satoshi's
        self.key.send(wallet_address, 0.00000546, "btc")

    def latest_transaction(self):
        return self.key.get_transactions()[0]

    def generate_qr_hash(self):
        hash = latest_transaction()
        pyqrcode.create("https://blockstream.info/tx/" + hash)
        latest_transaction.png("latest_transaction.png", scale=2.5)


class Picture(guizero.Picture):
    def start_animation(self):
        self.image = self.value.replace(".png", ".gif")

    def stop_animation(self):
        self.image = self.value.replace(".gif", ".png")

    def swap_animation(self):
        if self.value.endswith(".png"):
            self.start_animation()
        else:
            self.stop_animation()

    def timed_stop(self, ms):
        self.after(ms, self.stop_animation)


def transition(img, func, time=None, click=True):
    icon.image = filepath + img
    if click:
        icon.when_clicked = func
        if time:
            icon.timed_stop(time)
    else:
        icon.after(time, func)
    app.update()


def boot():
    transition("boot.gif", start, 2600)


def start():
    transition("start.gif", wait_for_code, 3600, False)


def wait_for_code():
    def scanning_run():
        if scanning.code:
            app.cancel(scanning_run)
            scan()

    scanning = scanner.App()
    scanning.run()
    app.repeat(200, scanning_run)


def scan():
    transition("scanned.gif", complete)


def complete():
    transition("complete.gif", boot, 2000)


app = App(bg="white")
icon = Picture(app)
app.set_full_screen()
boot()
app.display()

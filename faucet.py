"""#!/usr/bin/env python3"""

import bit
import config
import pyqrcode
from bit import Key
from bit.network import get_fee


import guizero
from guizero import App, Text
from threading import Thread


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
        return self.key.send([(wallet_address, 0.00000546, "btc")])

    def generate_qr_hash(self, hash):
        latest_transaction = pyqrcode.create("https://blockstream.info/tx/" + hash)
        latest_transaction.png(filepath + "latest_transaction.png", scale=5.5)


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


def transition(img, func=None, time=None, click=False):
    icon.image = filepath + img
    if click:
        icon.when_clicked = func
        if time:
            icon.timed_stop(time)
    elif func:
        icon.after(time, func)
    app.update()


def boot():
    transition("boot.gif", start, 2600, click=True)


def start():
    transition("start.gif", wait_for_code, 3600)


def wait_for_code():
    def scanning_run():
        if scanning.code:
            app.cancel(scanning_run)
            scanned(scanning.code)

    transition("start.png")
    scanning = scanner.App()
    scanning.run()
    app.repeat(200, scanning_run)


def scanned(wallet_code):
    def send_satoshis():
        faucet = Faucet()
        hash = faucet.send(wallet_code)
        faucet.generate_qr_hash(hash)

    satoshis = Thread(target=send_satoshis)
    satoshis.start()
    transition("scanned.gif", complete, 9000)


def complete():
    transition("complete.gif", show_transaction, 3000)


def show_transaction():
    icon.hide()
    message.show()
    app.update()
    transaction.show()


def restart():
    message.hide()
    transaction.hide()
    icon.show()
    boot()


app = App(bg="white")
app.set_full_screen()
icon = Picture(app)
message = Text(
    app,
    size=26,
    font="Quicksand Medium",
    color="green",
    text="Satoshi's are on the way!",
    visible=False,
)
transaction = Picture(
    app, image=filepath + "latest_transaction.png", align="bottom", visible=False
)
transaction.when_clicked = restart
boot()
app.display()

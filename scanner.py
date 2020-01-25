import cv2
import time
import numpy as np

from pyzbar.pyzbar import decode, ZBarSymbol
from imutils.video import VideoStream


qr = [ZBarSymbol.QRCODE]
check = cv2.imread("/home/pi/App/images/checkmark.png")


class Cam(VideoStream):
    """Initializes the pi camera for capturing frames"""

    def __init__(self):
        self.boot = VideoStream(usePiCamera=True, resolution=(480, 352))  # 480, 352
        self.stream = self.boot.start()
        self.frame = None

    def capture(self):
        self.frame = self.stream.read()

    def stop(self):
        self.stream.stop()


class Effects(Cam):
    """Visual effects that can be applied to captured frames"""

    def __init__(self):
        super().__init__()

    def remove_color(self):
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

    def add_text(self, text):
        cv2.putText(
            self.frame, text, (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1.4, (26, 147, 247), 2
        )

    def add_border(self):
        # get frame dimensions
        # height, width, _ = frame.shape
        color, thickness = (255, 255, 255), 20
        cv2.rectangle(self.frame, (0, 0), (480, 352), color, thickness)

    def bounding_box(self, code):
        (x, y, width, height) = code.rect
        cv2.rectangle(self.frame, (x, y), (x + width, y + height), (0, 0, 255), 2)

    def checkmark(self):
        # if charmark size != frame size then app will freeze
        cv2.addWeighted(self.frame, 1, check, 1, 0, self.frame)


class Window(Effects):
    """Full screen pop up window for viewing frames"""

    def __init__(self):
        super().__init__()

    def fullscreen(self):
        cv2.namedWindow("scanner", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("scanner", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def display(self):

        cv2.imshow("scanner", self.frame)
        cv2.waitKey(5)

    def close(self):
        cv2.destroyAllWindows()
        cv2.waitKey(1)


class App(Window):
    """QR scanning app to use with GUI"""

    def __init__(self):
        super().__init__()
        self.fullscreen()

    def run(self):
        self.code = ""
        while not self.code:
            self.capture()
            self.code = decode(self.frame, symbols=qr)
            self.add_border()
            self.add_text("Scan Wallet Now")
            self.display()
        self.bounding_box(self.code[-1])
        self.display()
        time.sleep(2.5)
        self.checkmark()
        self.display()
        time.sleep(5)
        self.code = self.code[-1]
        self.close()
        self.stop()

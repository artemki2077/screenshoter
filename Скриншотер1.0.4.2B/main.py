import sys
import decimal
from PIL import Image, ImageFont, ImageDraw, Image
from PIL.ImageQt import ImageQt
import pretty_errors
from pycoingecko import CoinGeckoAPI
import random
import datetime as dt
import decimal
from typing import Union
import requests
from io import BytesIO
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFormLayout, QGroupBox, \
    QLineEdit, QPushButton, QDoubleSpinBox
from ui import Ui_Screenshoter
from PyQt5.QtGui import QPixmap, QImage
import os


ctx = decimal.Context()

ctx.prec = 18


def float_to_str(f):
    d1 = ctx.create_decimal(repr(f))
    answ = format(d1, 'f')
    return answ


def norm_vid(e: Union[float, int]) -> str: return '{0:,}'.format(decimal.Decimal(str(e))).replace(',', " ")

def cleaning(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def gen_datetime(min_year=1900, max_year=dt.datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = dt.datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + dt.timedelta(days=365 * years)
    return start + (end - start) * random.random()

class Screenshoter(QMainWindow):
    def __init__(self):
        super(Screenshoter, self).__init__()
        self.ui = Ui_Screenshoter()
        self.ui.setupUi(self)

        self.ui.check_meta.setChecked(True)
        self.ui.check_trust.setChecked(True)
        # self.ui.radio_meta.setChecked(True)

        # CONSTS

        self.ui.select_net.addItems(['Ethereum Main Metwork', 'Binance Smart Chain', 'Polygon Mainnet', 'Cronos'])
        self.nets = {'Ethereum Main Metwork': "ERC20", 'Binance Smart Chain': 'BEP20', 'Polygon Mainnet': 'MATIC', 'Cronos': 'CRO'}

        # CORDS

        self.c_net = [[(0, 0), (0, 0)]]
        self.c_name = [[(0, 0), (0, 0)]]
        self.c_full_name = [[(0, 0), (0, 0)]]
        self.c_lost = [[(0, 0), (0, 0)]]
        self.c_price = [[(0, 0), (0, 0)]]

        # ???????????????? ????????????????????

        self.net = 'Ethereum Main Metwork'
        self.name = 'MVL'
        self.full_name = "Mass Vehicle Ledger"
        self.check_metamask = True
        self.check_trustwallet = True
        self.font_var = 1
        self.id_api = 'mass-vehicle-ledger'
        self.link = 'https://assets.coingecko.com/coins/images/3447/small/ONT.png'
        self.lost = 0
        self.price_coin = 0

        # ???????????????????? ????????????????????

        self.index = 0
        self.state = True
        self.coin_img = None
        self.m_img = Image.open("etc/metamask.png")
        self.t_img = Image.open("etc/trustwallet.png")
        self.img = self.m_img

        # ?????????????????? scrollArea

        first = QDoubleSpinBox()
        first.setMaximum(1_000_000)
        first.setValue(7777.77)
        first.valueChanged.connect(lambda: self.edit(first))
        self.usds = [first]
        first_btn = QPushButton('-')
        self.usds_buttons = [first_btn]

        self.formlayout = QFormLayout()
        self.groupbox = QGroupBox("USDs")
        for i in range(len(self.usds)):
            self.formlayout.addRow(self.usds[i], self.usds_buttons[i])
        self.groupbox.setLayout(self.formlayout)
        self.ui.scrollArea.setWidget(self.groupbox)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setFixedHeight(400)

        self.ui.plus.clicked.connect(self.plus)
        self.ui.input_id_api.setText('mass-vehicle-ledger')

        # ??????????????????

        self.ui.input_name.setText('MVL')
        self.ui.input_full_name.setText('Mass Vehicle Ledger')

        self.ui.select_net.activated.connect(self.selector)
        self.ui.input_name.textChanged.connect(self.change)
        self.ui.input_full_name.textChanged.connect(self.change)
        self.ui.get_price.clicked.connect(self.get_price_coin)
        self.ui.font_index.valueChanged.connect(self.change)
        self.ui.input_link_img.textChanged.connect(self.change)

        self.ui.forward.clicked.connect(lambda: self.navigation(True))
        self.ui.back.clicked.connect(lambda: self.navigation(False))
        self.ui.input_price.valueChanged.connect(self.change)
        self.ui.input_lost.valueChanged.connect(self.change)

        # self.ui.input_link_img.

        self.ui.generate.clicked.connect(self.generate)

        self.get_price_coin()

        self.cords_var = True

        self.ui.x_full_name.valueChanged.connect(self.cords)
        self.ui.y_full_name.valueChanged.connect(self.cords)
        self.ui.x_lost.valueChanged.connect(self.cords)
        self.ui.y_lost.valueChanged.connect(self.cords)
        self.ui.x_name.valueChanged.connect(self.cords)
        self.ui.y_name.valueChanged.connect(self.cords)
        self.ui.x_net.valueChanged.connect(self.cords)
        self.ui.y_net.valueChanged.connect(self.cords)
        self.ui.x_price.valueChanged.connect(self.cords)
        self.ui.x_price.valueChanged.connect(self.cords)
        self.ui.btn_state.clicked.connect(self.change_state)
        # self.ui.radio_meta.buttonClicked.connect(self.change_state)
        # self.ui.radio_trust.buttonClicked.connect(self.change_state)
        # QtCore.QObject.connect(self.consultRadioButton, QtCore.SIGNAL("currentIndexChanged(QString)"), self.call_Consult)

        self.castom()

    def change_state(self):
        # self.state = self.ui.radio_meta.isChecked()
        self.state = not self.state
        self.img = self.m_img if self.state else self.t_img
        self.ui.btn_state.setText(['MetaMask', 'Trust Wallet'][self.state])
        self.set_values()
        self.castom()

    def cords(self):
        if self.cords_var:
            self.c_full_name[self.index][self.state] = (self.ui.x_full_name.value(), self.ui.y_full_name.value())
            self.c_name[self.index][self.state] = (self.ui.x_name.value(), self.ui.y_name.value())
            self.c_net[self.index][self.state] = (self.ui.x_net.value(), self.ui.y_net.value())
            self.c_lost[self.index][self.state] = (self.ui.x_lost.value(), self.ui.y_lost.value())
            self.c_price[self.index][self.state] = (self.ui.x_price.value(), self.ui.y_price.value())

        self.castom()

    def castom(self):
        img = self.img.copy()
        draw = ImageDraw.Draw(img)
        usd = self.usds[self.index].value()
        name = self.name
        full_name = self.full_name
        price_coin = self.price_coin
        net = self.net
        font_var = self.font_var
        lost = self.lost
        tim_now = gen_datetime().strftime('%H:%M')

        if self.state:
            font_coin = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', int(font_var * 45))
            font_usd = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 25)
            font_net = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 15)
            font_ful_coin_name = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)
            font_time = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)

            usd_str = f'${usd:.2f}'
            if price_coin != 0:
                price = round(usd / price_coin, 4)
            else:
                price = 0

            draw.text((40, 21), tim_now, (0, 0, 0), font=font_time)
            draw.text(self.c_full_name[self.index][self.state], f'{name}', (0, 0, 0), font=font_ful_coin_name)
            draw.text(self.c_name[self.index][self.state], f'{price} {name}', (0, 0, 0), font=font_coin)
            draw.text((300 - (len(usd_str) * 8), 325), usd_str, (118, 118, 118), font=font_usd)
            draw.text(self.c_net[self.index][self.state], net, (118, 118, 118), font=font_net)
            x = self.c_net[self.index][self.state][0] - 10
            y = 114
            r = 4
            draw.ellipse((x - r, y - r, x + r, y + r), fill=((12, 210, 166) if 'Ethereum Main Metwork' == net else (118, 118, 118)))
        else:
            font_coin = ImageFont.truetype("font/DIN Next W10 Medium.otf", int(font_var * 45))
            font_usd = ImageFont.truetype("font/DIN Next W10 Medium.otf", 25)
            font_net = ImageFont.truetype("font/DIN Next W10 Medium.otf", 22)
            font_ful_coin_name = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)
            font_time = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)

            usd_str = f'~ {usd:.2f} $'
            if price_coin != 0:
                price = round(usd / price_coin, 4)
            else:
                price = 0
            draw.text((40, 21), tim_now, (255, 255, 255), font=font_time)
            draw.text(self.c_full_name[self.index][self.state], f'{full_name}', (255, 255, 255), font=font_ful_coin_name)
            draw.text(self.c_name[self.index][self.state], f'{norm_vid(price)} {name}'.replace(".", ","), (255, 255, 255), font=font_coin)
            draw.text((300 - (len(usd_str) * 8), 365), usd_str.replace(".", ","), (108, 119, 139), font=font_usd)
            draw.text((300 - (len(usd_str) * 8), 370), "~", (108, 119, 139), font=font_usd)
            draw.text(self.c_net[self.index][self.state], self.nets[net], (108, 119, 139), font=font_net)
            draw.text(self.c_price[self.index][self.state], f"${float_to_str(price_coin)}", (108, 119, 139), font=font_net)
            draw.text(self.c_lost[self.index][self.state], f"{'+' if lost > 0 else ''}{lost}%", (143, 57, 72) if lost <= 0 else (113, 196, 107), font=font_net)
            if self.coin_img:
                img.paste(self.coin_img, (249, 198), self.coin_img)

        pixmap = QPixmap.fromImage(ImageQt(img).copy())
        self.ui.image.setPixmap(pixmap)
        self.ui.image.adjustSize()

    def set_values(self):
        self.cords_var = False
        self.ui.x_full_name.setValue(int(self.c_full_name[self.index][self.state][0]))
        self.ui.y_full_name.setValue(int(self.c_full_name[self.index][self.state][1]))
        self.ui.x_name.setValue(int(self.c_name[self.index][self.state][0]))
        self.ui.y_name.setValue(int(self.c_name[self.index][self.state][1]))
        self.ui.x_net.setValue(int(self.c_net[self.index][self.state][0]))
        self.ui.y_net.setValue(int(self.c_net[self.index][self.state][1]))
        self.ui.x_lost.setValue(int(self.c_lost[self.index][self.state][0]))
        self.ui.y_lost.setValue(int(self.c_lost[self.index][self.state][1]))
        self.ui.x_price.setValue(int(self.c_price[self.index][self.state][0]))
        self.ui.y_price.setValue(int(self.c_price[self.index][self.state][1]))
        self.cords_var = True

    def navigation(self, b):

        if 0 <= self.index + (-1, 1)[b] < len(self.usds):
            self.index += (-1, 1)[b]
            self.set_values()
            self.castom()
        if self.index >= len(self.usds):
            self.index = len(self.usds) - 1
            self.set_values()
            self.castom()

    def selector(self, index):
        self.net = self.ui.select_net.itemText(index)
        self.change()

    def change(self):
        self.font_var = self.ui.font_index.value()
        self.name = self.ui.input_name.text()
        self.full_name = self.ui.input_full_name.text()
        self.price_coin = self.ui.input_price.value()
        self.lost = self.ui.input_lost.value()
        self.link = self.ui.input_link_img.text()
        try:
            self.coin_img = Image.open(BytesIO(requests.get(self.link).content)).convert("RGBA").resize((93, 93))
        except BaseException as e:
            print(e)
            self.coin_img = None
        self.update()
        self.set_values()
        self.castom()
    
    def generate(self):
        
        name = self.name
        full_name = self.full_name
        price_coin = self.price_coin
        net = self.net
        font_var = self.font_var
        lost = self.lost
        tim_now = gen_datetime().strftime('%H:%M')

        if self.ui.check_meta.isChecked():
            cleaning('out/meta_mask')
            for i_m in range(len(self.c_net)):
                tim_now = gen_datetime().strftime('%H:%M')
                img = self.m_img.copy()
                draw = ImageDraw.Draw(img)
                usd = self.usds[i_m].value()
                font_coin = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', int(font_var * 45))
                font_usd = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 25)
                font_net = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 15)
                font_ful_coin_name = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)
                font_time = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)

                usd_str = f'${usd:.2f}'
                price = round(usd / price_coin, 4)

                draw.text((40, 21), tim_now, (0, 0, 0), font=font_time)
                draw.text(self.c_full_name[i_m][1], f'{name}', (0, 0, 0), font=font_ful_coin_name)
                draw.text(self.c_name[i_m][1], f'{price} {name}', (0, 0, 0), font=font_coin)
                draw.text((300 - (len(usd_str) * 8), 325), usd_str, (118, 118, 118), font=font_usd)
                draw.text(self.c_net[i_m][1], net, (118, 118, 118), font=font_net)
                x = self.c_net[i_m][1][0] - 10
                y = 114
                r = 4
                draw.ellipse((x - r, y - r, x + r, y + r), fill=((12, 210, 166) if 'Ethereum Main Metwork' == net else (118, 118, 118)))
                img.save(f"out/meta_mask/{i_m + 1}.png")

        if self.ui.check_trust.isChecked():
            cleaning('out/trust_wallet')
            for i_t in range(len(self.c_net)):
                tim_now = gen_datetime().strftime('%H:%M')
                img = self.t_img.copy()
                draw = ImageDraw.Draw(img)
                usd = self.usds[i_t].value()
                font_coin = ImageFont.truetype("font/DIN Next W10 Medium.otf", int(font_var * 45))
                font_usd = ImageFont.truetype("font/DIN Next W10 Medium.otf", 25)
                font_net = ImageFont.truetype("font/DIN Next W10 Medium.otf", 22)
                font_ful_coin_name = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)
                font_time = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)

                usd_str = f'~ {usd:.2f} $'
                price = round(usd / price_coin, 4)
                draw.text((40, 21), tim_now, (255, 255, 255), font=font_time)
                draw.text(self.c_full_name[i_t][0], f'{full_name}', (255, 255, 255), font=font_ful_coin_name)
                draw.text(self.c_name[i_t][0], f'{norm_vid(price)} {name}'.replace(".", ","), (255, 255, 255), font=font_coin)
                draw.text((300 - (len(usd_str) * 8), 365), usd_str.replace(".", ","), (108, 119, 139), font=font_usd)
                draw.text((300 - (len(usd_str) * 8), 370), "~", (108, 119, 139), font=font_usd)
                draw.text(self.c_net[i_t][0], self.nets[net], (108, 119, 139), font=font_net)
                draw.text(self.c_price[i_t][0], f"${float_to_str(price_coin)}", (108, 119, 139), font=font_net)
                draw.text(self.c_lost[i_t][0], f"{'+' if lost > 0 else ''}{lost}%", (143, 57, 72) if lost <= 0 else (113, 196, 107), font=font_net)
                if self.coin_img:
                    img.paste(self.coin_img, (249, 198), self.coin_img)
                img.save(f"out/trust_wallet/{i_t + 1}.png")

    def update(self):
        usd = self.usds[self.index].value()
        name = self.name
        price_coin = self.price_coin
        net = self.net
        font_var = self.font_var
        # if self.state:
        # font_coin = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', int(font_var*45))
        # font_usd = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 25)
        # font_net = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 15)
        # font_ful_coin_name = ImageFont.truetype('font/EuclidCircularB-Medium.ttf', 23)

        price = round(usd / price_coin, 4)
        self.c_full_name[self.index][1] = [285 - (len(f'{name}') * 7.6), 70]
        self.c_name[self.index][1] = [270 - (len(f'{price} {name}') * (10 * font_var)), 270]
        self.c_net[self.index][1] = [300 - (len(net) * 4.5), 105]

        self.c_full_name[self.index][0] = [300 - (len(f'{self.full_name}') * 6), 85]
        self.c_name[self.index][0] = [290 - (len(f'{norm_vid(price)} {name}') * (10 * font_var)), 310]
        self.c_net[self.index][0] = [20, 160]
        self.c_price[self.index][0] = [370, 160]
        self.c_lost[self.index][0] = [500, 160]

        # self.castom()
        # pixmap = ImageQt(img)
        # self.ui.image.setPixmap(QPixmap(QImage(pixmap)))

    def get_price_coin(self):
        try:
            answ_json = CoinGeckoAPI().get_coin_ticker_by_id(id=self.ui.input_id_api.text())
            self.price_coin = answ_json['tickers'][0]['converted_last']['usd']
            self.lost = answ_json['tickers'][0]['last']
        except BaseException:
            self.price_coin = 1
            self.lost = 1
        self.ui.input_price.setValue(self.price_coin)
        self.ui.input_lost.setValue(self.lost)

    def edit(self, i):
        n = self.usds.index(i)
        copy_index = self.index
        self.index = n
        self.update()
        self.index = copy_index

    def delete(self, i):
        n = self.usds_buttons.index(i)
        del self.usds[n]
        del self.usds_buttons[n]
        del self.c_net[n]
        del self.c_name[n]
        del self.c_full_name[n]
        del self.c_lost[n]
        del self.c_price[n]

        self.formlayout = QFormLayout()
        self.groupbox = QGroupBox("USDs")
        for i in range(len(self.usds)):
            self.formlayout.addRow(self.usds[i], self.usds_buttons[i])
        self.groupbox.setLayout(self.formlayout)
        self.ui.scrollArea.setWidget(self.groupbox)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setFixedHeight(400)

    def plus(self):
        self.c_net.append([(0, 0), (0, 0)])
        self.c_name.append([(0, 0), (0, 0)])
        self.c_full_name.append([(0, 0), (0, 0)])
        self.c_lost.append([(0, 0), (0, 0)])
        self.c_price.append([(0, 0), (0, 0)])

        new = QDoubleSpinBox()
        new.setMaximum(1_000_000)
        new.setValue(0.0)
        new.valueChanged.connect(lambda: self.edit(new))
        self.usds.append(new)
        new_btn = QPushButton('-')
        count = len(self.usds_buttons)
        new_btn.clicked.connect(lambda: self.delete(new_btn))
        self.usds_buttons.append(new_btn)
        self.formlayout.addRow(self.usds[-1], self.usds_buttons[-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Screenshoter()
    window.show()
    sys.exit(app.exec())

from time import sleep
import pyautogui as pg
from mss import mss
import numpy as np
import telebot
import sys

def txt_settings():
    openfile = open('settings.txt', 'r')
    readfile = openfile.read()
    read_dict = dict(el.split() for el in readfile.split('\n'))
    openfile.close()
    return read_dict
def create_settings():
    createfile = open('settings.txt', 'w+')
    bot_token = input('Enter your Telegram bot token. Can be taken from BotFather : ')
    chat_id = input('Enter your Telegram chat id. Can be taken from MyChatID bot : ')
    resolution = input('Chose your resolution. 1 - 1366x768, 2 - 1600x900 , 3 - 1920x1080 : ')
    makesettings = 'bot_token ' + bot_token + '\nchat_id ' + chat_id + '\nresolution ' + resolution
    createfile.write(makesettings)
    createfile.close()
    sys.exit()
try: 
    txt_settings()
except:
    create_settings()
setts = txt_settings()


### Func that contains ur telegram bot token and chat id. Plus coordinates to click ACCEPT button
### Telegram bot token you can take from Botfather, chat_id from GetMyID bot ### 
def message():
    token = setts['bot_token']
    bot = telebot.TeleBot(token)
    chat_id = setts['chat_id']
    text = 'game is ready'
    bot.send_message(chat_id, text)
def accept():
    if setts['resolution'] == '1':
        pg.click(628, 369)
    elif setts['resolution'] == '2':
        pg.click(729, 439)
    elif setts['resolution'] == '3':
        pg.click(855, 736)

mss = mss()
def screens():
    if setts['resolution'] == '1':
        monitor = {'top': 377, 'left': 637, 'width': 1, 'height': 1}
    elif setts['resolution'] == '2':
        monitor = {'top': 444, 'left': 743, 'width': 1, 'height': 1}
    elif setts['resolution'] == '3':
        monitor = {'top': 536, 'left': 889, 'width': 1, 'height': 1}
    monitor_grab = mss.grab(monitor)
    img = np.array(monitor_grab)
    convertation = img[0][0]
    rgb_colors = list(convertation)
    return(rgb_colors)

def main():
    while screens() != [255, 255, 255, 255]:
        sleep(15)
if __name__ == '__main__':
    main()

accept()
message()
sleep(3)

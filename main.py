from PIL import Image
from time import sleep
import keyboard, telebot, os, sys, pyautogui

if os.path.exists("configure.txt"):
    with open('configure.txt') as file:
        chat_id = int(file.readline())
        token = file.readline()
else:
    token = input("Введите токен своего бота от BotFather: ")
    chat_id = int(input("Введите свой chat_id (https://t.me/getmyid_bot): "))
    with open("configure.txt", "w") as f:
        f.write(f"{chat_id}\n{token}")
bot = telebot.TeleBot(token)
while True:
    if keyboard.is_pressed('j'):
        while True:
            screen = pyautogui.screenshot('screenshot.png',region=(905, 531, 1, 1))
            im = Image.open('screenshot.png', 'r')
            width, height = im.size
            pixel_values = list(im.getdata())
            if pixel_values == [(255, 255, 255)]:
                pyautogui.click(905, 531)
                screendone = pyautogui.screenshot('screenshotdone.png',region=(0, 0, 1920, 1080))
                file = open('screenshotdone.png', 'rb')
                bot.send_message(chat_id, text="Катка нашлась!, Беги к компу")
                bot.send_message(chat_id, text="Катка нашлась!, Беги к компу")
                bot.send_message(chat_id, text="Катка нашлась!, Беги к компу")
                sleep(2)
                bot.send_photo(chat_id, file)
                break
            sleep(0.5)
    if keyboard.is_pressed("esc"):
        sys.exit()
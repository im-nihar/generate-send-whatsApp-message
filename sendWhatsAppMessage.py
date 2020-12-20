import schedule
import time
import webbrowser as web
import pyautogui as pg
import random


def random_message():
    print("Generating Random Message Func ")
    message_library = ["I love you", "I miss you", "I wish you were here", "My heart belongs to you",
                       "All that I do, I do for you", "Thinking about you", "My world revolves around you",
                       "You are mine and I am yours", "You are perfect for Me", "I will always be there for You",
                       "I miss the scent of your hair, the feel of your skin.",
                       "When I look into your eyes, I just know we were meant to be",
                       "Life would be impossible without You", "You make me happy",
                       "You are all that I need and will ever need", "Ours is a love so real, so true, so deep...",
                       "I treasure every moment we spent together", "You are special",
                       "You are mine to love and care for", "I appreciate You", "Without You, my world is empty"]
    a = random.randint(1, len(message_library))
    return message_library[a]


def call_whats_app():
    print("Open Whats App Func ")
    message = random_message()
    phone_no = "+919423646351"
    parsed_message = message
    web.open_new('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + parsed_message)
    time.sleep(2)
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(15)
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('ctrl', 'w')
    pg.alert('Message sent was: ' + parsed_message, title=phone_no, timeout=4000)
    time.sleep(2)
    pg.press('OK')


def job():
    print("Start Job ")
    call_whats_app()
    print("End Job ")


schedule.every(1).minutes.do(job)
# schedule.every(1).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(4)

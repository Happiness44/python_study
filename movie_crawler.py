import os
import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

load_dotenv(verbose=True)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_USER_ID = os.getenv('CHAT_USER_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date=20210720'


def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=CHAT_USER_ID, text=title + '> IMAX 예매가 열렸습니다.')
        sched.pause()


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()

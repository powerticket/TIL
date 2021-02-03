import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


telegram_token = '1372867727:AAEsQ2_FusJgHp6IXoOVDTuNWSQcGk7zAh4'
telegram_chat_id = 1389690724
bot = telegram.Bot(token = telegram_token)

def job_function():
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200826'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    title_list = soup.select('div.info-movie')
    imax = soup.select_one('span.imax')
    if imax:
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a >strong').text.strip()
        bot.sendMessage(chat_id=telegram_chat_id, text=title + " IMAX 예매가 열렸습니다.")
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()
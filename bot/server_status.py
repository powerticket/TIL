import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


telegram_token = '1372867727:AAEsQ2_FusJgHp6IXoOVDTuNWSQcGk7zAh4'
telegram_chat_id = 1389690724
bot = telegram.Bot(token = telegram_token)
def job_function():
    bot.sendMessage(chat_id=telegram_chat_id, text="라즈베리파이 서버가 잘 작동하고 있습니다.")

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=60)
sched.start()
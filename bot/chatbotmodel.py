import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 1389690724
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class TeleBot(TelegramBot):
    def __init__(self):
        self.token = '1372867727:AAEsQ2_FusJgHp6IXoOVDTuNWSQcGk7zAh4'
        TelegramBot.__init__(self, 'Notification_bot', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('Notification bot is activated.')
        self.updater.start_polling()
        self.updater.idle()
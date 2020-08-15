import telegram


telegram_token = '1372867727:AAEsQ2_FusJgHp6IXoOVDTuNWSQcGk7zAh4'
telegram_chat_id = 1389690724
bot = telegram.Bot(token = telegram_token)
bot.sendMessage(chat_id=telegram_chat_id, text="라즈베리파이 서버가 재부팅 되었습니다.")
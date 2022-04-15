import telebot
import requests

#5372323243:AAE6x6kuWs-ek_ornjJo6COOTrdqsyi9EYE
bot = telebot.TeleBot("5372323243:AAE6x6kuWs-ek_ornjJo6COOTrdqsyi9EYE")

def request_to_fastkore(uri, data):
    response = requests.post(uri, data=data)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
        # inJson = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
        # inDict = json.loads(inJson)
        # return inDict
    else:
        return -1



@bot.message_handler(commands=['start'])
def send_info(message):
    bot.reply_to(message, "Введите номер заказа.")

@bot.message_handler(func=lambda m: True)
def give_order_list(message):
    if message.text.isdigit():
        byteresult = request_to_fastkore("http://cloud.fastkore.ru:27026/sdgijpxjknfg/load", message.text)
        byteArr = []
        for byte in (byteresult).split(','):
            byteArr.append(int(byte))
        result = bytes(byteArr)
        bot.reply_to(message, result)

bot.polling()
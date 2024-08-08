from telebot import TeleBot
from word import init, get_placement

init_word, word_dict = init()
similarities = []
TOKEN = '7100336321:AAFLQghZU2dDd7zsqGJulqbG4MwGiNapLZs'
bot = TeleBot(TOKEN)


def get_sring_words(similarities):
    end_string = ""
    for sim, count in similarities:
        end_string += f"{sim}: {count}\n"
    return end_string

print(init_word)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Вводите любое слово, чтоб поиграть)")


@bot.message_handler(commands=['w'])
def send_word(message):
    global similarities
    if len(message.text.split(" ")) > 2:
        bot.send_message(message.chat.id, "больше 1 слово нельзя")
        return
    _, word = message.text.split(" ")
    if word == init_word:
        bot.send_message(message.chat.id, "Победа")
        return
    place = get_placement(word, word_dict)
    if place == -1:
        bot.send_message(message.chat.id, "Очень далеко")
        return
    similarities.append((word, place))
    similarities.sort(key=lambda tup: tup[1])
    msg = get_sring_words(similarities)
    bot.send_message(message.chat.id, msg)


if __name__ == '__main__':
    bot.polling(none_stop=True)
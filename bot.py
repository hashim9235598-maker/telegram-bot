import telebot

TOKEN = 8401688576:AAEdOZBqESNukypPGwk9F5LBJDBrmDcqxBc

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ البوت يعمل بنجاح على Railway")

print("Bot is running...")

bot.infinity_polling()
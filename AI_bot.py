from openai import OpenAI
import telebot

token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(token)

client = OpenAI(
    base_url="BASE_URL_FROM_OPENROUTER",
    api_key="API_KEY_OF_CLIENT",
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! \n"
                          "I'm your artificial assistant. What do you want to know today? \n"
                          "To ask a question, follow the instructions: /tell <question>")

@bot.message_handler(commands=['tell'])
def tell(message):
    question = message.text.split(' ', 1)[1]
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "API_KEY_OF_CLIENT",
            "X-Title": "Tg_Bot",
        },
        extra_body={},
        model="API_OF_MODEL",
        messages=[
          {
            "role": "user",
            "content": f"{question}"
          }
        ]
    )
    bot.reply_to(message, completion.choices[0].message.content)

bot.polling(none_stop=True)



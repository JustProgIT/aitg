import telebot
import google.generativeai as genai
bot = telebot.TeleBot("7199521180:AAGBFPSAT2leM1Cuxmhda8PlM0QvPC2-rsk", parse_mode=None)

genai.configure(api_key="AIzaSyA4ffKUGXd581HRwGhdThEQye7hJWdoGr4")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    bot.reply_to(message, convo.last.text)

bot.infinity_polling()

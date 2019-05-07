from pyrogram import Client, Filters, Emoji
import random


from typing import Optional, List








app = Client('835349563:AAEraMgAMwRFzOdv7kMLVOYSRgYBL-mlTwA')





id = '-1001356076506'
target = "zearn"  # Target channel/supergroup

with app:
    for member in app.iter_chat_members(target):
        
   Client.send_message(message.chat.id, member.user.first_name)













MENTION = "[{}](tg://user?id={})"
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.ml/)'s group chat {}!"

chats_filter = Filters.chat(["PyrogramChat", "PyrogramLounge"])


@Client.on_message(chats_filter & Filters.new_chat_members)
def welcome(client, message):
    new_members = [MENTION.format(i.first_name, i.id) for i in message.new_chat_members]
    text = MESSAGE.format(Emoji.SPARKLES, ", ".join(new_members))
    message.reply(text, disable_web_page_preview=True)









@app.on_message(Filters. command('toss'))
def randheadtain( client, message) :
    message.reply(random.choice(['💫 Result : Tail ', '💫 Result : Head ']))

        








@app.on_message(Filters. command('gun'))
def randheadtain( client, message) :
    message.reply(random.choice(['💫 Result : AK47 😎', '💫 Result : Muflis 💥 ']))





@app.on_message(Filters. command('side'))
def randheadtain(client, message):
            message.reply(random.choice(['💫 Result : Up 👆 ', '💫 Result : Down 👇 ','💫 Result : Left 👈','💫 Result : Right 👉']))






@app.on_message(Filters. command('sps'))
def randheadtain(client, message):
            message.reply(random.choice(['💫 Result : Paper ', '💫 Result : Stone ','💫 Result : Sessiors']))

            
@app.on_message(Filters. command('decide'))
def randheadtain(client, message):
            message.reply(random.choice(['💫 Result : Yes ', '💫 Result : Maybe ','💫 Result : No ']))

app.on_message(Filters. command('start'))
def randheadtain(client, message):
    message.reply( 'Get /help to help for buy Contact - @google_console ')


@app.on_message(Filters.command('roll'))
def ran(client, message):
 if len(message.text.split(' ')) > 1:
  message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
 else:
  message.reply('Please set a range!')


@app.on_message(Filters. command('dice'))
def randheadtain(client, message):
    message.reply(random.choice(['👨‍🎓 Your Luck : 1⃣','👨‍🎓 Your Luck : 2⃣','👨‍🎓 Your Luck : 3⃣','👨‍🎓 Your Luck : 4⃣','👨‍🎓 Your Luck  : 5⃣','👨‍🎓 Your Luck : 2⃣','👨‍⚕ Your Luck : 6⃣']))


@app.on_message(Filters. command('help'))
def randheadtain(client, message):
    message.reply('My commands : /toss , /gun , /side , /roll {range} ,/sps , /dice , /dice2 , /show , /show1 , /show2 , /decide Need Help Contact - @google_console ')









 

@app.on_message(Filters. command('show'))
def show(client, message):
    message.reply(random.choice([ '👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 3⃣','👨‍🎓 Your Card : 4⃣','👨‍🎓 Your Card : 5⃣','👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 6⃣','👨‍🎓 Your Card : 7⃣','👨‍🎓 Your Card : 8⃣','👨‍🎓 Your Card : 9⃣','👨‍🎨 Your Card : 🔟','🧛‍♂ Your Card : 🇦​','🤴 Your Card : 🇰','👨‍🎨 Your Card : 🇯​','👸 Your Card : 🇶​']))
    message.reply(random.choice([ '👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 3⃣','👨‍🎓 Your Card : 4⃣','👨‍🎓 Your Card : 5⃣','👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 6⃣','👨‍🎓 Your Card : 7⃣','👨‍🎓 Your Card : 8⃣','👨‍🎓 Your Card : 9⃣','👨‍🎨 Your Card : 🔟','🧛‍♂ Your Card : 🇦​','🤴 Your Card : 🇰','👨‍🎨 Your Card : 🇯​','👸 Your Card : 🇶​'])) 
    message.reply(random.choice([ '👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 3⃣','👨‍🎓 Your Card : 4⃣','👨‍🎓 Your Card : 5⃣','👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 6⃣','👨‍🎓 Your Card : 7⃣','👨‍🎓 Your Card : 8⃣','👨‍🎓 Your Card : 9⃣','👨‍🎨 Your Card : 🔟','🧛‍♂ Your Card : 🇦​','🤴 Your Card : 🇰','👨‍🎨 Your Card : 🇯​','👸 Your Card : 🇶​']))


@app.on_message(Filters. command('dice2'))
def randheadtain(client, message):
    message.reply(random.choice(['👨‍🎓 Your Luck : 1⃣','👨‍🎓 Your Luck : 2⃣','👨‍🎓 Your Luck : 3⃣','👨‍🎓 Your Luck : 4⃣','👨‍🎓 Your Luck  : 5⃣','👨‍🎓 Your Luck : 2⃣','👨‍⚕ Your Luck : 6⃣']))
    message.reply(random.choice(['👨‍🎓 Your Luck : 1⃣','👨‍🎓 Your Luck : 2⃣','👨‍🎓 Your Luck : 3⃣','👨‍🎓 Your Luck : 4⃣','👨‍🎓 Your Luck  : 5⃣','👨‍🎓 Your Luck : 2⃣','👨‍⚕ Your Luck : 6⃣']))


@app.on_message(Filters. command('show2'))
def show(client, message):
    message.reply(random.choice([ '👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 3⃣','👨‍🎓 Your Card : 4⃣','👨‍🎓 Your Card : 5⃣','👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 6⃣','👨‍🎓 Your Card : 7⃣','👨‍🎓 Your Card : 8⃣','👨‍🎓 Your Card : 9⃣','👨‍🎨 Your Card : 🔟','🧛‍♂ Your Card : 🇦​','🤴 Your Card : 🇰','👨‍🎨 Your Card : 🇯​','👸 Your Card : 🇶​']))
    message.reply(random.choice([ '👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 3⃣','👨‍🎓 Your Card : 4⃣','👨‍🎓 Your Card : 5⃣','👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 6⃣','👨‍🎓 Your Card : 7⃣','👨‍🎓 Your Card : 8⃣','👨‍🎓 Your Card : 9⃣','👨‍🎨 Your Card : 🔟','🧛‍♂ Your Card : 🇦​','🤴 Your Card : 🇰','👨‍🎨 Your Card : 🇯​','👸 Your Card : 🇶​'])) 

@app.on_message(Filters. command('show1'))
def show(client, message):
    message.reply(random.choice([ '👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 3⃣','👨‍🎓 Your Card : 4⃣','👨‍🎓 Your Card : 5⃣','👨‍🎓 Your Card : 2⃣','👨‍🎓 Your Card : 6⃣','👨‍🎓 Your Card : 7⃣','👨‍🎓 Your Card : 8⃣','👨‍🎓 Your Card : 9⃣','👨‍🎨 Your Card : 🔟','🧛‍♂ Your Card : 🇦​','🤴 Your Card : 🇰','👨‍🎨 Your Card : 🇯​','👸 Your Card : 🇶​']))
    


app.run()

while 1:
    time.sleep(10)

from pyrogram import Client, Filters
import random

app = Client('835349563:AAEraMgAMwRFzOdv7kMLVOYSRgYBL-mlTwA')







@app.on_message(Filters. command('toss'))
def promote(bot: Bot, update: Update, args: List[str]) -> str:
    chat_id = update.effective_chat.id
    message = update.effective_message  # type: Optional[Message]
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]

    user_id = extract_user(message, args)
           
   
if user_member.status == 'administrator' or user_member.status == 'creator':
        message.reply_text("How am I meant to promote someone that's already an admin?")
        return ""








 message.reply(random.choice(['🤷 Coin flipped: Head', '🤷 Coin flipped: Tail']))
















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
    message.reply('My commands : /toss , /roll {range} ,/sps , /dice , /dice2 , /show , /show1 , /show2 , /decide Need Help Contact - @google_console ')









 

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

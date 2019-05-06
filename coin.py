from pyrogram import Client, Filters
import random

app = Client('835349563:AAEraMgAMwRFzOdv7kMLVOYSRgYBL-mlTwA')
@app.on_message(Filters. command('toss'))
def randheadtain(client, message):
    message.reply(random.choice(['Coin flipped: Head', 'Coin flipped: Tail']))

@app.on_message(Filters.command('roll'))
def ran(client, message):
 if len(message.text.split(' ')) > 1:
  message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
 else:
  message.reply('Please set a range!')


@app.on_message(Filters. command('dice'))
def randheadtain(client, message):
    message.reply(random.choice(['Result: 1','Result: 3','Result: 4','Result: 5' ,'Result: 6' , 'Result: 2']))



@app.on_message(Filters. command('show'))
def show(client, message):
    message.reply(random.choice([ '❤️ Your Card : 1⃣','❤️ Your Card : 2⃣','❤️ Your Card : 3⃣','❤️ Your Card : 4⃣','❤️ Your Card : 5⃣','❤️ Your Card : 2⃣','❤️ Your Card : 6⃣','❤️ Your Card : 7⃣','❤️ Your Card : 8⃣','❤️ Your Card : 9⃣','❤️ Your Card : 🔟','❤️ Your Card : 🇦​','❤️ Your Card : 🇰','❤️ Your Card : 🇯​' ]))
    message.reply(random.choice([ '❤️ Your Card : 1⃣','❤️ Your Card : 2⃣','❤️ Your Card : 3⃣','❤️ Your Card : 4⃣','❤️ Your Card : 5⃣','❤️ Your Card : 2⃣','❤️ Your Card : 6⃣','❤️ Your Card : 7⃣','❤️ Your Card : 8⃣','❤️ Your Card : 9⃣','❤️ Your Card : 🔟','❤️ Your Card : 🇦​','❤️ Your Card : 🇰','❤️ Your Card : 🇯​' ]))
    message.reply(random.choice([ '❤️ Your Card : 1⃣','❤️ Your Card : 2⃣','❤️ Your Card : 3⃣','❤️ Your Card : 4⃣','❤️ Your Card : 5⃣','❤️ Your Card : 2⃣','❤️ Your Card : 6⃣','❤️ Your Card : 7⃣','❤️ Your Card : 8⃣','❤️ Your Card : 9⃣','❤️ Your Card : 🔟','❤️ Your Card : 🇦​','❤️ Your Card : 🇰','❤️ Your Card : 🇯​' ]))


@app.on_message(Filters. command('dice2'))
def randheadtain(client, message):
    message.reply(random.choice(['Result: 1','Result: 3','Result: 4','Result: 5' ,'Result: 6' , 'Result: 2']))
    message.reply(random.choice(['Result: 1','Result: 3','Result: 4','Result: 5' ,'Result: 6' , 'Result: 2']))







app.run()

while 1:
    time.sleep(10)

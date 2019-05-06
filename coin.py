from pyrogram import Client, Filters
import random

app = Client('835349563:AAEraMgAMwRFzOdv7kMLVOYSRgYBL-mlTwA')
@app.on_message(Filters. command('coin'))
def randheadtain(client, message):
    client.send_message(message.chat.id, random.choice(['head', 'tail']))


@app.on_message(Filters.command('roll'))
def ran(client, message):
 if len(message.text.split(' ')) > 1:
  client.send_message(message.chat.id, random.choice(range(1, int(message.text.split(' ')[1]))))
 else:
  message.reply('add a number bro')




@app.on_message(Filters. command('show'))
def randheadtain(client, message):
    client.send_message(message.chat.id, [random.choice(['A','1','2','3','4','5','6','7','8','9','10','J','K','Q'])for i in range(3)])



app.run()

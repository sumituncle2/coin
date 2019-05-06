from pyrogram import Client, Filters
import random

app = Client('835349563:AAEraMgAMwRFzOdv7kMLVOYSRgYBL-mlTwA')
@app.on_message(Filters. command('coin'))
def randheadtain(client, message):
    client.send_message(message.chat.id, random.choice(['head', 'tail']))
app.run()

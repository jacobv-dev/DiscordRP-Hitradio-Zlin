from pypresence import Presence # Discord Presence
import time # Refresh
import requests # Otevře stránku a collectne JSON
import simplejson as json # Práce s JSON

client_id = ''  # Discord Dev ID
RPC = Presence(client_id)  # Initialize the Presence
RPC.connect()  # Start the handshake loop

print('Success!')

while True:
    # Vezme JSON kód z URL
    raw_json = requests.get("https://radia.cz/data/pravehraje/new-322-currentnext.json").json()

    # Převede do proměnných
    interpret = raw_json['current']['interpret']
    song = raw_json['current']['song']

    detail = interpret + ' - ' + song

    RPC.update(details= song, state= interpret ,large_image= 'hitradio_zlin1', large_text= detail, buttons=[{"label": "Poslouchat", "url": "https://radia.cz/radio-hitradio-zlin-playlist"}])
    time.sleep(10) # Refresh

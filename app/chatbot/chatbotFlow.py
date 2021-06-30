from app.helpers import sender_graph
from random import choice

def initial_message(**kwargs):
    # https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies
    return sender_graph(recipient_id=kwargs['recipient_id'], 
            message={
                "text": "Bienvenido Cesar, escriba un artista o canción"
            }
    )

def tracks_message(**kwargs):
    # https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic
    elements = []

    for track in kwargs["tracks"]['tracks']["items"][:5]:
        print(track["id"])
        if len(track["album"].get("images")) > 0:
            image_url = track["album"].get("images")[0].get("url")
        else:
            image_url = 'https://askleo.askleomedia.com/wp-content/uploads/2004/06/no_image-300x245.jpg'
        element = {
            "title":track["album"]["name"],
            "image_url":image_url,
            "subtitle": "canción",
            "buttons":[
                {
                    "type":"web_url",
                    "url": track["album"]["external_urls"]["spotify"],
                    "title": "Abrir en Spotify"
                },
                {
                    "type":"postback",
                    "title":"Agregar a Playlist",
                    "payload":track["id"]
                }                   
            ],
                  
        }
        elements.append(element)
    
    return sender_graph(recipient_id=kwargs["recipient_id"], message={
        "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements": elements
            }
        }
    })

def send_playlist(**kwargs):
    for e in range(1, 7):
        sender_graph(recipient_id=kwargs['recipient_id'], 
            message={
                "text": f"Song {e}"
            })
    return True

def random_messages(**kwargs):
    palabras = ['que tal', 'no hay de que', 'no molestes', 'te observo']
    return sender_graph(recipient_id=kwargs['recipient_id'], message=choice(palabras))
















############################# artists graph printer


    # for artist in kwargs["tracks_artists"]['artists']["items"][:3]:
    #     if len(artist.get("images")) > 0:
    #         image_url = artist.get("images")[0].get("url")
    #     else:
    #         image_url = 'https://askleo.askleomedia.com/wp-content/uploads/2004/06/no_image-300x245.jpg'
    #     element = {
    #         "title":artist["name"],
    #         "image_url":image_url,
    #         "subtitle": "artista",
    #         "buttons":[
    #             {
    #                 "type":"web_url",
    #                 "url": artist["external_urls"]["spotify"],
    #                 "title": "Abrir en Spotify"
    #             },
    #             # {
    #             #     "type":"web_url",
    #             #     "url": artist["external_urls"]["spotify"],
    #             #     "title": "Agregar"
    #             # },         
    #         ],
                  
    #     }
    #     elements.append(element)

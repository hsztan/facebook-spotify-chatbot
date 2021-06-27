from app.helpers import sender_graph
from random import choice

def initial_message(**kwargs):
    # https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies
    return sender_graph(recipient_id=kwargs['recipient_id'], 
            message={
                "text": "Bienvenido xxxxx, escriba un artista o canción"
            }
    )

def artist_choice_message(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        'text': f'Escribe un artista'
    })

def color_message(**kwargs):
    palabras = ['que tal', 'no hay de que', 'no molestes', 'te observo']
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        'text': f'Escogiste el color {kwargs["color"]}'
    })

def template_message(**kwargs):
    # https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"Google",
                        "image_url":"https://www.google.com.pe/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
                        "subtitle":"We have the right hat for everyone.",
                        "buttons":[
                            {
                                "type":"web_url",
                                "url":"https://www.google.com.pe",
                                "title":"View Website"
                            }         
                        ]      
                    },
                    {
                        "title":"Amazon",
                        "image_url":"http://pngimg.com/uploads/amazon/amazon_PNG13.png",
                        "subtitle":"We have the right hat for everyone.",
                        "buttons":[
                            {
                                "type":"web_url",
                                "url":"https://www.amazon.com",
                                "title":"View Website"
                            }         
                        ]      
                    },
                    {
                        "title":"Youtube",
                        "image_url":"https://logodownload.org/wp-content/uploads/2014/10/youtube-logo-5-2.png",
                        "subtitle":"We have the right hat for everyone.",
                        "buttons":[
                            {
                                "type":"web_url",
                                "url":"https://www.youtube.com",
                                "title":"View Website"
                            }         
                        ]      
                    }
                ]
            }
        }
    })

def artists_tracks_message(**kwargs):
    # https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic
    elements = []
    print("INSIDE MESSSAGE SENDER")
    for artist in kwargs["tracks_artists"]['artists']["items"][:3]:
        if len(artist.get("images")) > 0:
            image_url = artist.get("images")[0].get("url")
        else:
            image_url = 'https://askleo.askleomedia.com/wp-content/uploads/2004/06/no_image-300x245.jpg'
        element = {
            "title":artist["name"],
            "image_url":image_url,
            "subtitle": "artista",
            "buttons":[
                {
                    "type":"web_url",
                    "url": artist["external_urls"]["spotify"],
                    "title": "Abrir en Spotify"
                },
                # {
                #     "type":"postback",
                #     "title":"Start Chatting",
                #     "payload":"DEVELOPER_DEFINED_PAYLOAD"
                # }              
            ],
                  
        }
        elements.append(element)

    for track in kwargs["tracks_artists"]['tracks']["items"][:3]:
        print(track["album"]["name"])
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
                # {
                #     "type":"postback",
                #     "title":"Start Chatting",
                #     "payload":"DEVELOPER_DEFINED_PAYLOAD"
                # }              
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

def random_messages(**kwargs):
    palabras = ['que tal', 'no hay de que', 'no molestes', 'te observo']
    return sender_graph(recipient_id=kwargs['recipient_id'], message=choice(palabras))

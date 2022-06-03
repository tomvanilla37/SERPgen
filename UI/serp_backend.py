import requests
import random

def list_collection():
    goods = ['buy', 'purchase', 'order', 'sale', 'shop', 'discover', 'acquire', 'get', 'take']

    servives = ['come', 'enjoy', 'feel', 'try', 'benefit', 'appreciate', 'relish']

    online = ['register', 'subscribe', 'join', 'be a part', 'try out', 'broadcast', 'discover', 'download', 'develop', 'invest', 'secure']

    famous = ['inform', 'check out', 'get to know', 'discover', 'find', 'locate', 'light on', 'come across']

    appealing = ['sexy', 'hot', 'cute', 'wild', 'stimulating',
                        'seductive', 'intriguing', 'tempting', 'provocative',
                        'appealing', 'desirable', 'sensual', 'exciting']

    urgent = ['now', 'fast', 'quick', 'hurry', 'rapidly', 'close', 'approaching', 'never', 'seconds', 'again', 'over',
              'instant', 'today', 'limited', 'few left', 'last']

    strong = ['shine', 'enlight', 'follow', 'reveal', 'absorb', 'advance', 'govern', 'gravitate', 'alter', 'scan',
              'amplify', 'attack', 'guide', 'beam', 'free', 'heighten', 'shine', 'shock', 'boost', 'broadcast', 'intensify',
              'capture', 'smash', 'launch', 'lead', 'locate', 'magnify', 'command', 'modify', 'multiply', 'steer', 'storm',
              'direct', 'perceive', 'picture', 'place', 'plant', 'engage', 'enlarge', 'transform', 'treat', 'position',
              'escort', 'power', 'expand', 'explore', 'explode', 'uncover', 'untangle', 'extend', 'unveil', 'extract',
              'refashion', 'usher', 'refine', 'weave', 'reveal', 'fuse', 'revitalize', 'revolutionize', 'gaze', 'rise',
              'train', 'fit', 'model', 'unlock', 'grow']

    targets = ['future', 'goal', 'dream', 'aim', 'cause', 'career', 'path', 'freedom', 'independence', 'will', 'success',
               'advantage', 'journey', 'power', 'knowledge', 'deal']

def key_to_text(key_list):
    '''
    a funtion to get the list of keys and return a text
    input:
        key_list: list of str
    output
        text_out: strls
    '''
    key_list = (map(lambda x: x.lower(), key_list))
    key_list=",".join(key_list)

    url = 'https://api-serpgen-kw3vzvzkiq-ew.a.run.app/predict'
    params = {
        'key_list': key_list
    }
    response = requests.get(url, params=params)
    text=response.json()

    return text['prediction']

import requests
import json
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *


def fun_fact():
    clear()
    # put_html("<p><h2>Fun Fact Genrator</h2></p>")
    put_html("<p align = 'left'><h2><img src='https://icons.iconarchive.com/icons/icons8/windows-8/512/Messaging-Happy-icon.png' width='7%'>Fun Fact Genrator</h2></p>")
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.request('GET',url)

    if response.status_code == 200:
        data = json.loads(response.text)
        fun = data['text']
        style(put_text(fun),'color:blue;font-size:30px')
        put_button(label='Click me',onclick=fun_fact)

    else:
        put_text(f"Error {response.status_code}")


    # style(put_text(fun),'color:blue;font-size:30px')
    # put_button([dict(label='Click me',value = 'outline-success',color='outline-success')],onclick=fun_fact)

if __name__ == '__main__':
    put_html("<p align = 'left'><h2><img src='https://icons.iconarchive.com/icons/icons8/windows-8/512/Messaging-Happy-icon.png' width='7%'>Fun Fact Genrator</h2></p>")
    put_button(label='Click me',onclick=fun_fact)
    # put_button([dict(label='Click me',value = 'outline-success',color='outline-success')],onclick=fun_fact)

hold()
"""
This is the template server side for ChatBot
"""
from bottle import route, run, response, template, static_file, request
from datetime import datetime, timedelta
import json
import requests
import pyowm
import curses_list
curses_list = curses_list.curses





@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')

def chat():
    been_before = request.get_cookie("last_visited")
    if been_before:
        been_before = int(request.get_cookie("last_visited"))
        been_before += 1
        response.set_cookie(name="last_visited", value=str(been_before))
    else:
        response.set_cookie(name="last_visited", value=str(1))


    user_message = request.POST.get('msg')
    print been_before
    if (been_before==None):
        user_response = name(user_message)
        return json.dumps(user_response)

    if ("love" in user_message):
        user_response = love(user_message)
        return json.dumps(user_response)

    if ("thank you" in user_message):
        user_name = request.get_cookie("name")
        return json.dumps({"animation": "giggling", "msg": "fuck you {}".format(user_name)})

    if ("joke" in user_message):
        user_response = joke()
        return json.dumps({"animation": "giggling", "msg": user_response})

    if ("weather in" in user_message):
        user_response = get_weather_around_world(user_message)
        return json.dumps({"animation": "ok", "msg": "the weather is {} celius".format(user_response)})

    if ("weather" in user_message):
        user_response = get_weather_tlv(user_message)
        return json.dumps({"animation": "ok", "msg": "the weather in Tel Aviv is {} celius".format(user_response)})


    else:
        user_response = checking_curses(user_message)
        return json.dumps(user_response)


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": "working"})


def love(user_msg):
    name = request.get_cookie("name")
    return {"animation": "inlove", "msg": "and i love you {}".format(name)}

def name(user_msg):
    temp=0
    word_list=user_msg.split()
    capital_word_list=[]
    for word in word_list:
        if (word[0].isupper()):
            temp+=1
            capital_word_list.append(word)
    if (temp==1):
        response.set_cookie(name="name", value=capital_word_list[0])
        return {"animation": "excited", "msg": "{} is a cool name".format(capital_word_list[0])}

    elif (temp==2):
        response.set_cookie(name="name", value=capital_word_list[1])
        return {"animation": "excited", "msg": "{} is a cool name".format(capital_word_list[1])}

    elif (len(word_list)==1):
        response.set_cookie(name="name", value=word_list[0])
        return {"animation": "excited", "msg": "hmmmm i think your name is {}".format(word_list[0])}

    else:
        response.set_cookie(name="name", value="doctor")
        return {"animation": "excited", "msg": "you have a wierd ass name, i'm just gonna call you doctor"}

def joke():
    url = 'http://api.icndb.com/jokes/random'
    r = requests.get(url)
    datastore = json.loads(r.text)
    random_joke = datastore['value']['joke']
    return random_joke

def get_weather_tlv(usr_msg):
    owm = pyowm.OWM('e2127e27bebf766102636701292d8402')
    observation = owm.weather_at_place('Tel Aviv, IL')
    w = observation.get_weather()
    temperture = w.get_temperature('celsius')['temp']
    return temperture

def get_weather_around_world(usr_msg):
    try:
        owm = pyowm.OWM('e2127e27bebf766102636701292d8402')
        city_name = usr_msg.split('weather in')[1][1:].capitalize()
        print city_name
        observation = owm.weather_at_place(city_name)
        w = observation.get_weather()
        temperture = w.get_temperature('celsius')['temp']
        return temperture
    except:
        case_of_error = "couldnt find the weather for this shit place"
        return case_of_error


def checking_curses(user_message):
    for curse in curses_list:
        if curse in user_message:
            return {"animation": "no", "msg": "watch it! im the only one allowed to curse here"}
    else:
        name = request.get_cookie("name")
        return {"animation": "dog", "msg": "i dont have a good answer for you {}".format(name) }

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()

import requests
import json
import pyttsx3
while True:
    city = input("Enter the name of the city:")
    url = f"http://api.weatherapi.com/v1/current.json?key=9327b8b3e49840faa5740242240901&q={city}"
    r = requests.get(url)
    # print(r.text)
    wdict = json.loads(r.text)
    engine=pyttsx3.init()
    engine.setProperty('rate', 150) 
    weather = wdict["current"]["temp_c"]
    print(f"weather of {city} is:{weather}")
    engine.say(f"weather of {city} is:{weather}")
    engine.runAndWait()
from django.shortcuts import render
from django.http import HttpResponse
from colorama import init, Fore, Back
from .models import game
import random
import requests
import json
init()

# Create your views here.
def gameinputs(request):
    loop = True
    # response = requests.get("http://api.open-notify.org/astros.json").content
    # print(response)
    # return HttpResponse(response)
     


    emp = game.objects.all()
    wordone = random.choice(emp)
    response=json.dumps([{'wordlist':wordone.word}])
    response_info = json.loads(response)
    response_data = response_info[0]['wordlist']

    # word_list = ["crown", "build", "logic", "plane", "focus", "money", "plant", "plate", "pound", "other", "input", "horse", "green", "group", "beans", "guide", "layer", "mayor", "lunch", "limit", "model", "point", "scope", "score", "title", "total", "world"]
  
    wordl = response_data  
    
    # word = 'crown'
    while loop:
        print("Start a new game? (y/quit)")
        command = input()
        if command == "quit":
            loop = False
        elif command == "y":
            inner_loop = 0
            print("Enter a word")
            while inner_loop < 6:
                attempt = input()

                   
                output = ""
                for i in range(wordl.__len__()):
                    if attempt[i] == wordl[i]:
                        output = output + Back.GREEN + attempt[i] + Back.RESET
                    elif attempt[i] in wordl:
                        output = output + Back.YELLOW + attempt[i] + Back.RESET
                    else:
                        output = output + attempt[i] + Back.RESET
                print(output)
                if wordl == attempt:
                    print("Congrats")
                    inner_loop = inner_loop + 6 
                    

                    inner_loop = inner_loop + 1
                    
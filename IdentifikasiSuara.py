# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:26:40 2021

@author: HP
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                if 'play' in command:
                     song = command.replace('play', '')
                     talk('playing ' + song)
                     pywhatkit.playonyt(song)
                elif 'find' in command:
                     found = command.replace('find','')
                     talk('searching' + found)
                     pywhatkit.search(found)
                elif 'business model canvas' in command:
                    talk('The Business Model Canvas was proposed by Alexander Osterwalder based on his earlier book: Business Model Ontology. It outlines nine segments which form the building blocks for the business model in a nice one-page canvas. The Business Model Canvas reflects systematically on your business model, so you can focus on your business model segment by segment. This also means you can start with a brain dump, filling out the segments the spring to your mind first and then work on the empty segments to close the gaps. The following list with questions will help you brainstorm and compare several variations and ideas for your next business model innovation.')
                elif 'key patners' in command:
                    talk('Who are your key partners/suppliers? What are the motivations for the partnerships?')
                elif 'key activities' in command:
                    talk('What key activities does your value proposition require? What activities are important the most in distribution channels, customer relationships, revenue stream…?')
                elif 'value proposition' in command:
                    talk('What core value do you deliver to the customer? Which customer needs are you satisfying?')
                elif 'customer relationship' in command:
                    talk('What relationship that the target customer expects you to establish? How can you integrate that into your business in terms of cost and format?')
                elif 'customer segment' in command:
                    talk('Which classes are you creating values for? Who is your most important customer?')
                elif 'key resource' in command:
                    talk('What key resources does your value proposition require? What resources are important the most in distribution channels, customer relationships, revenue stream…?')
                elif 'distribution channel' in command:
                    talk('Through which channels that your customers want to be reached? Which channels work best? How much do they cost? How can they be integrated into your and your customers’ routines?')
                elif 'cost structure' in command:
                    talk('What are the most cost in your business? Which key resources/ activities are most expensive?')
                elif 'revenue stream' in command:
                    talk('For what value are your customers willing to pay?What and how do they recently pay? How would they prefer to pay? How much does every revenue stream contribute to the overall revenues?')
                else:
                    talk('Please say the command again.')
            else:
                talk('please call me master')
    except:
        pass
    return command


while True:
    take_command()
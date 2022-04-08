import requests
import json
import time
import os

import openai
import cv2
import pytesseract
from deep_translator import GoogleTranslator
from PIL import Image
# CATEGORY COORDINATES

# ANSWER COORDINATES

# START GAME COORDINATES

# OPENAI API
openai.api_key = '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'

def get_text_from_image(img):
    img = cv2.imread(img)
    return pytesseract.image_to_string(img)

def translate_german_to_english(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

def get_answer_from_gpt3(question):
    print('Creating Api Call')
    response = openai.Completion.create(engine='davinci', prompt=question)
    answer = response.choices[0]['text']
    return answer

# Go through the answers and return the one with most similarity
def get_best_answer(answers):
    pass

# Click on random category
def click_random_category():
    pass

# Click on right answer
def click_right_answer():
    pass

# Click on start game
def click_start_game():
    pass


# TESTING
test = 'Was ist die Hauptstadt von Deutschland?'
kek = translate_german_to_english(test)
print(kek)
kek2 = get_answer_from_gpt3(kek)
print(kek2)


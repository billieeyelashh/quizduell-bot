from sre_parse import CATEGORIES
import time
import os

import openai
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

from deep_translator import GoogleTranslator
from PIL import Image

import pyautogui

# QUESTION COORDINATES for Screenshot
QUESTION_TOP_X = 1587
QUESTION_TOP_Y = 160
QUESTION_Y = 140
QUESTION_X = 280


# ANSWER COORDINATES SCREENSHOT
#1
ANSWER_1_X = 1586
ANSWER_1_Y = 354
#2
ANSWER_2_X = 1740
ANSWER_2_Y = 354
#3
ANSWER_3_X = 1586
ANSWER_3_Y = 435
#4
ANSWER_4_X = 1740
ANSWER_4_Y = 435

ANSWERS_X = 130
ANSWERS_Y = 65


# CONTROL COORDINATES
START_GAME_X = 1660
START_GAME_Y = 420

START_PLAYER_X = 1570
START_PLAYER_Y = 620

PLAY_BUTTON_X = 1670
PLAY_BUTTON_Y = 750

CATEGORIES_X = 1665
CATEGORIES_Y = 400


# OPENAI API
openai.api_key = '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'

# Locate an image with pyautogui
def locate_image(img):
    return pyautogui.locateCenterOnScreen(img)

# take a screenshot of a specific area with pyautogui
def take_screenshot(x1, y1, x2, y2,filename):
    # Get the screenshot
    img = pyautogui.screenshot(region=(x1, y1, x2, y2))
    # Save the screenshot
    img.save(filename)
    return img


def get_text_from_image(img):
    img = cv2.imread(img)
    return pytesseract.image_to_string(img)

def translate_german_to_english(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

def get_answer_from_gpt3(question):
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: {}".format(question) ,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
        )
    answer = response.choices[0]['text']
    return answer

# Click on specific coordinates
def click_on_coordinates(x, y):
    pyautogui.click(x, y)

def delete_all_jpg():
    for file in os.listdir("."):
        if file.endswith(".jpg"):
            os.remove(file)


# TESTING
#test = 'Welche Kriegerin aus der Mangaserie "Sailor Moon" ist die Hueterin von Raum und Zeit? '
#kek = translate_german_to_english(test)
#print(kek)
#kek2 = get_answer_from_gpt3(kek)
#print(kek2)


#take_screenshot(ANSWER_1_X, ANSWER_1_Y, ANSWERS_X, ANSWERS_Y, "answer1.jpg")
#question = get_text_from_image("answer.jpg")
#print(question)
#Location = locate_image('buttons/next.PNG') # only works with png weird  champ
#print(Location)
#click_on_coordinates(Location[0], Location[1])
def play():
            time.sleep(1)
            print('[OP] Taking Screenshot of the Question')
            # Take screenshot of the question
            take_screenshot(QUESTION_TOP_X, QUESTION_TOP_Y, QUESTION_X, QUESTION_Y,'question.jpg')
            print('[INFO] Screenshot taken')
            time.sleep(1)

            print('[OP] Taking Screenshot of the Answer')
            # Take screenshot of the answers(inefficient)
            take_screenshot(ANSWER_1_X, ANSWER_1_Y, ANSWERS_X, ANSWERS_Y,'answer1.jpg')
            take_screenshot(ANSWER_2_X, ANSWER_2_Y, ANSWERS_X, ANSWERS_Y,'answer2.jpg')
            take_screenshot(ANSWER_3_X, ANSWER_3_Y, ANSWERS_X, ANSWERS_Y,'answer3.jpg')
            take_screenshot(ANSWER_4_X, ANSWER_4_Y, ANSWERS_X, ANSWERS_Y,'answer4.jpg')
            print('[INFO] Screenshots taken')
            time.sleep(1)
            # Extract text from the question
            question_de = get_text_from_image('question.jpg')
            print('[TEXT] Question DE: ' + question_de)

            # Extract text from the answers
            answer1_de = get_text_from_image('answer1.jpg')
            print('[TEXT] Answer 1 DE: ' + answer1_de)
            answer2_de = get_text_from_image('answer2.jpg')
            print('[TEXT] Answer 2 DE: ' + answer2_de)
            answer3_de = get_text_from_image('answer3.jpg')
            print('[TEXT] Answer 3 DE: ' + answer3_de)
            answer4_de = get_text_from_image('answer4.jpg')
            print('[TEXT] Answer 4 DE: ' + answer4_de)

            # Translate the question
            question_en = translate_german_to_english(question_de)
            print('[TEXT] Question EN: ' + question_en)

            # Translate the answers
            answer1_en = translate_german_to_english(answer1_de)
            print('[TEXT] Answer 1 EN: ' + answer1_en)
            answer2_en = translate_german_to_english(answer2_de)
            print('[TEXT] Answer 2 EN: ' + answer2_en)
            answer3_en = translate_german_to_english(answer3_de)
            print('[TEXT] Answer 3 EN: ' + answer3_en)
            answer4_en = translate_german_to_english(answer4_de)
            print('[TEXT] Answer 4 EN: ' + answer4_en)
            time.sleep(1)
            # Make GPT-3 call
            print('[INFO] Making GPT-3 call')
            gpt3_answer = get_answer_from_gpt3(question_en)
            print('[TEXT] GPT-3 Answer: ' + gpt3_answer)
            time.sleep(1)

            print('[OP] Checking which answer is correct ')
            if answer1_en in gpt3_answer:
                print('[INFO] Answer 1 is correct')
                click_on_coordinates(1651, 382)
                print('[INFO] Clicked on Answer 1')
            elif answer2_en in gpt3_answer:
                print('[INFO] Answer 2 is correct')
                click_on_coordinates(1775,382)
                print('[INFO] Clicked on Answer 2')
            elif answer3_en in gpt3_answer:
                print('[INFO] Answer 3 is correct')
                click_on_coordinates(1651, 464)
                print('[INFO] Clicked on Answer 3')
            elif answer4_en in gpt3_answer:
                print('[INFO] Answer 4 is correct')
                click_on_coordinates(1803, 464)
                print('[INFO] Clicked on Answer 4')
            else:
                print('[WARN] No correct answer found')
            # Clean up
            print('[INFO] Cleaning up')
            # Delete all jpg images
            delete_all_jpg()
            time.sleep(5)


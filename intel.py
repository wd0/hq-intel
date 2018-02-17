from PIL import Image
import webbrowser
import tesserocr
import time 
import os

# TODO: Is screenshot timestamp sufficiently precise?

def ocr_region(img, coords):
    cropped = img.crop(coords)
    return tesserocr.image_to_text(cropped).strip().replace('\n', ' ')

def ocr_question(img):
    question_coords = (100, 275, 980, 700)
    return ocr_region(img, question_coords)

def ocr_answer(img, answerno):
    initial_answer_coords = (64, 680, 1000, 880)
    question_offset = 200
    x1, y1, x2, y2 = initial_answer_coords
    answer_coords = (x1, y1 + question_offset*answerno,
                     x2, y2 + question_offset*answerno)
    return ocr_region(img, answer_coords) 

answer_keys = 'abc'
class Quiz:
    def __init__(self, filename=""):
        self.filename = filename
        self.question = str()
        self.answers = dict()
        if self.filename:
            with Image.open(self.filename) as img:
                self.question = ocr_question(img)
                for i, ak in enumerate(answer_keys):
                    self.answers[ak] = ocr_answer(img, i)

    def google(self):
        base_url = 'http://www.google.com/search?q={}'
        fmt = self.question + ' ' + ' '.join(self.answers.values()) 
        webbrowser.open(base_url.format(fmt))

    def run(self):
        print(self.question)
        for ak in answer_keys:
            print(ak + ": " + self.answers[ak])
        self.google()

def is_quiz_file(filename):
    return filename.endswith('.png')

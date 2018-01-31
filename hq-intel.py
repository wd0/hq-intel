from PIL import Image
import webbrowser
import tesserocr
import pdb
import time 
import os

SEARCH_SLEEP_DURATION = 0.5
DELETE_SEEN_IMAGES = False
SCREENSHOT_PATH = '/home/mike/hq-intel'

# Is screenshot timestamp sufficiently precise?

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

class Quiz:

    def __init__(self, img=None):
        self.question = str()
        self.answers = dict()
        if img is not None:
            answer_keys = 'abc'
            self.question = ocr_question(img)
            self.answers = dict()
            for i, ak in enumerate(answer_keys):
                self.answers[ak] = ocr_answer(img, i)

def run_quiz(quiz_filename):
    img = Image.open(quiz_filename)
    quiz = Quiz(img)
    print(quiz.question)
    for ak in 'abc':
        print(ak + ": " + quiz.answers[ak])
    google_quiz(quiz)

def google_quiz(quiz):
    base_url = 'http://www.google.com/search?q={}'
    webbrowser.open(base_url.format(quiz.question + " " +  ' '.join(quiz.answers.values()))) 

def is_quiz_file(filename):
    return filename.endswith('.png')

def main():
    os.chdir(SCREENSHOT_PATH)
    seen = []
    while True:
        unseen = [f for f in os.listdir() if f not in seen] 
        for f in unseen:
            if is_quiz_file(f):
                run_quiz(f)
                if DELETE_SEEN_IMAGES:
                    os.remove(f)
        seen += unseen
        break
        time.sleep(SEARCH_SLEEP_DURATION) 

def main2():
    from PIL import Image
    img = Image.open('nc.png')
    quest = ocr_question(img)
    print(quest)

if __name__ == "__main__":
    main()

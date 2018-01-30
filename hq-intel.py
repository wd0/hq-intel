from PIL import Image
import tesserocr
import pdb
import time 
import os

SEARCH_SLEEP_DURATION = 0.5
SCREENSHOT_PATH = '/home/mike/hq-intel'

# Is screenshot timestamp sufficiently precise?

def ocr_region(img, coords):
    cropped = img.crop(coords)
    return tesserocr.image_to_text(cropped)

def ocr_question(img):
    question_coords = (100, 275, 980, 700)
    return ocr_region(img, question_coords).strip().replace('\n', ' ')

class Quiz:
    def __init__(self, img=None):
        self.question = str()
        self.answers = dict()
        if img is not None:
            self.question = ocr_question(img)
            self.answers = {'a':'', 'b':'', 'c':'', 'd':''}

def run_quiz(quiz_filename):
    img = Image.open(quiz_filename)
    quiz = Quiz(img)
    print(quiz.question)

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
            else:
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

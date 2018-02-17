#!/usr/bin/python3

from intel import *

QUIZ_DELAY = 35 # Seconds to wait for the next HQ question to happen.
SEARCH_DELAY = 0.5 # Seconds until we search SCREENSHOT_PATH for more files.
SCREENSHOT_PATH = '/home/mike/hq-intel/shots' # Pathname where screenshots appear.

def main():
    os.chdir(SCREENSHOT_PATH)
    seen = []
    unseen = os.listdir()
    while True:
        for f in unseen:
            if is_quiz_file(f):
                quiz = Quiz(f)
                quiz.run()
                time.sleep(QUIZ_DELAY)
        unseen = [f for f in os.listdir() if f not in seen] 
        seen += unseen
        time.sleep(SEARCH_DELAY)

if __name__ == "__main__":
    main()

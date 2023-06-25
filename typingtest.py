import time
import random
import curses
from nltk.corpus import words

WORDS = [word for word in words.words('en') if len(word) >= 5]

def generate_sentence(word_count):
    return ' '.join(random.choice(WORDS) for _ in range(word_count))

def main(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

    while True:
        sentence = generate_sentence(10)

        stdscr.clear()
        stdscr.addstr("\n" + "*" * 80 + "\n", curses.color_pair(1))
        stdscr.addstr("🚀 Welcome to the typing speed test! Type the sentence below:\n", curses.color_pair(1))
        stdscr.addstr("*" * 80 + "\n\n", curses.color_pair(1))
        stdscr.addstr(sentence + "\n\n", curses.color_pair(3))

        correct_count = 0
        user_input = ""

        start_time = time.time()

        while len(user_input) != len(sentence):
            c = stdscr.getch()
            if c == 127 or c == 8:  # handle backspace
                user_input = user_input[:-1]
                stdscr.addstr("\b \b")
            elif c < 256:  # ignore non-ascii input
                if len(sentence) > len(user_input) and chr(c) == sentence[len(user_input)]:
                    stdscr.addstr(chr(c), curses.color_pair(4))
                    correct_count += 1
                else:
                    stdscr.addstr(chr(c), curses.color_pair(2))
                user_input += chr(c)

        end_time = time.time()

        time_taken = end_time - start_time

        wpm = (correct_count / 5 / time_taken) * 60
        accuracy = (correct_count / len(sentence)) * 100

        stdscr.addstr("\n\n" + "-" * 80 + "\n", curses.color_pair(1))
        stdscr.addstr(f"🎉 Typing speed: {wpm:.2f} words per minute.\n", curses.color_pair(1))
        stdscr.addstr(f"🎯 Typing accuracy: {accuracy:.2f}%.\n", curses.color_pair(1))
        stdscr.addstr("Press any key to try again, 'q' to quit.\n", curses.color_pair(1))
        stdscr.addstr("-" * 80 + "\n", curses.color_pair(1))

        c = stdscr.getch()
        if chr(c).lower() == 'q':
            break

if __name__ == "__main__":
    curses.wrapper(main)

import time
import requests
import curses
from difflib import SequenceMatcher

API_URL = "https://zenquotes.io/api/random"

def get_random_quote():
    response = requests.get(API_URL)
    data = response.json()
    return data[0]['q'] if data else "The quick brown fox jumps over the lazy dog."

def main(stdscr):
    curses.curs_set(0)

    # Initialize color pairs
    for i in range(1, 8):
        curses.init_pair(i, i, curses.COLOR_BLACK)

    color_counter = 1

    while True:
        quote = get_random_quote()

        stdscr.clear()

        # UI enhancements with colors and structure
        stdscr.addstr("\n" + "*" * 80 + "\n", curses.color_pair(1))
        stdscr.addstr("🚀 Welcome to the typing speed test!\n", curses.color_pair(1))
        stdscr.addstr(f"Type the quote below:\n\n", curses.color_pair(1))
        for c in quote:
            stdscr.addstr(c, curses.color_pair(color_counter))
            color_counter = color_counter % 7 + 1
        stdscr.addstr("\n\n", curses.color_pair(1))

        user_input = ""
        start_time = time.time()

        while len(user_input) != len(quote):
            c = stdscr.getch()
            if c == 127 or c == 8:  # handle backspace
                user_input = user_input[:-1]
                stdscr.addstr("\b \b")
            elif c < 256:  # ignore non-ascii input
                stdscr.addstr(chr(c), curses.color_pair(4 if quote[len(user_input)] == chr(c) else 2))
                user_input += chr(c)

        end_time = time.time()
        time_taken = end_time - start_time
        accuracy = SequenceMatcher(None, user_input, quote).ratio() * 100  # calculate accuracy based on similarity
        wpm = (len(user_input) / 5 / time_taken) * 60

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

if __name__ == "__main__":
    curses.wrapper(main)


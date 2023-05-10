import time
import random
import curses

# Random sentences to type
SENTENCES = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "Jackdaws love my big sphinx of quartz",
    "How vexingly quick daft zebras jump",
    "Bright vixens jump; dozy fowl quack",
    "Sphinx of black quartz, judge my vow",
]


def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Color setup
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        # Randomly select a sentence
        sentence = random.choice(SENTENCES)

        # Clear screen
        stdscr.clear()
        stdscr.addstr("Type this sentence: \n", curses.color_pair(1))
        stdscr.addstr(sentence + "\n\n", curses.color_pair(1))

        correct_count = 0
        incorrect_count = 0
        user_input = ""

        start_time = time.time()

        while len(user_input) != len(sentence):
            c = stdscr.getch()
            # Handle backspace
            if c == 127 or c == curses.KEY_BACKSPACE:
                user_input = user_input[:-1]
                stdscr.clear()
                stdscr.addstr("Type this sentence: \n", curses.color_pair(1))
                stdscr.addstr(sentence + "\n\n", curses.color_pair(1))
                stdscr.addstr(user_input, curses.color_pair(1))
            elif chr(c) == sentence[len(user_input)]:
                user_input += chr(c)
                stdscr.addstr(chr(c), curses.color_pair(1))
                correct_count += 1
            else:
                user_input += chr(c)
                stdscr.addstr(chr(c), curses.color_pair(2))
                incorrect_count += 1

        end_time = time.time()

        # Calculate the typing speed: (correct letters / total time) * 60
        speed = (correct_count / (end_time - start_time)) * 60

        stdscr.addstr("\n\nTyping speed: {:.2f} correct letters per minute.".format(
            speed), curses.color_pair(1))
        stdscr.addstr("\nPress any key to try again, 'q' to quit.",
                      curses.color_pair(1))

        c = stdscr.getch()
        if chr(c).lower() == 'q':
            break


if __name__ == "__main__":
    curses.wrapper(main)

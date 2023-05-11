# Typing Speed Test

A Python script that measures typing speed and accuracy by generating random sentences for the user to type. It provides real-time feedback on typing speed in words per minute (WPM) and accuracy percentage.

## Dependencies

- `curses`: A library for creating terminal-based user interfaces.
- `nltk`: A library for natural language processing.

## Installation

1. Clone the repository or download the `typingtest.py` file to your computer.
2. Open a terminal or command prompt.
3. Install the required libraries using the following command:

'''
pip3 install curses nltk
'''

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where the `typingtest.py` file is located.
3. Run the script using the following command:

'''
python3 typingtest.py
'''

## User Interface

The script uses different colors to highlight the sentence, your input, and any typing errors. The color scheme is as follows:

- **Green**: The sentence to be typed.
- **Blue**: The letters you type correctly.
- **Red**: The letters you type incorrectly.

The interface also provides instructions and displays the typing speed and accuracy results.

## Notes

- The script measures typing speed in words per minute (WPM), assuming a word length of 5 characters.
- The script uses the NLTK corpus of English words to generate random sentences. The first run may require an internet connection to download the corpus.

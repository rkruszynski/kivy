import json
import random
from datetime import datetime
from datetime import timedelta
from settings import LEVELS
from settings import words_dictionary


def set_difficulty(mode, word, difficulty):
    with open(words_dictionary, mode) as json_words:
        words = json.loads(json_words.read())
        words[word]["difficulty"]["level"] = difficulty
        words[word]["difficulty"]["next_active"] = datetime.now() + timedelta(minutes=LEVELS[difficulty])
        return words


def return_random_word():
    with open(words_dictionary, 'r') as json_words:
        words = json.loads(json_words.read())
        a = [x for x in words.keys() if words[x]["difficulty"]["next_active"] is None]  # for words that wasn't answered yet
        b = [x for x in words.keys() - a if datetime.strptime(words[x]["difficulty"]["next_active"], "%Y-%m-%d %H:%M:%S.%f") < datetime.now()]
        possible_words = a + b
        if len(possible_words) < 1:
            return "Congratulation, there is no more words to practice!"
        return random.choice(possible_words)


def return_spain_translation(word):
    with open(words_dictionary, 'r') as json_words:
        words = json.loads(json_words.read())
        return words[word]["spanish"]


def save_file(mode, content):
    with open(words_dictionary, mode) as file:
        json.dump(content, file, indent=4, default=str)



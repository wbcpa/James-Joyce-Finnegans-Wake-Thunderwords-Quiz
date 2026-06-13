"""
Thunderword Quiz  CS50P Final Project
Finnegans Wake by James Joyce contains ten 100-letter "thunderwords",
built from words for thunder (and other sounds) in many languages.
This quiz asks you to match each fragment to its language of origin.
"""

import json
import random
import sys

DATA_FILE = "thunderwords.json"

def load_thunderword(filepath):
    """Load the thunderword data from a JSON file."""
    with open(filepath) as f:
        return json.load(f)

def check_answer(guess, correct):
    """Return True if guess matches correct (case-insensitive)."""
    return guess.strip().lower() == correct.strip().lower()

def calculate_score(correct, total):
    """Return the result as a dict with percent and a rating text."""
    if total == 0:
        return {"percent": 0, "rating": "No questions played."}
    percent = round(correct / total * 100)
    if percent == 100:
        rating = "Perfect! You are a true polyglot of thunder!"
    elif percent >= 50:
        rating = "Good! You hear the thunder in many languages!"
    else:
        rating = "Keep listening – the thunder is still distant."
    return {"percent": percent, "rating": rating}

def generate_options(correct_language, all_languages, count):
    """Return count shuffled languages, always including the correct one."""
    wrong = [lang for lang in all_languages if lang != correct_language]
    options = random.sample(wrong, count - 1)
    options.append(correct_language)
    random.shuffle(options)
    return options

def ask_number(prompt, low, high):
    """Ask until the user enters a number between low and high."""
    while True:
        answer = input(prompt).strip()
        if answer.isdigit() and low <= int(answer) <= high:
            return int(answer)
        print(f"Please enter a number from {low} to {high}.")

def main():
    try:
        data = load_thunderword(DATA_FILE)
    except FileNotFoundError:
        sys.exit(f"Error: {DATA_FILE} not found.")

    # All languages in the data form the pool of multiple-choice options.
    languages = sorted({s["language"] for tw in data for s in tw["segments"] if s["explained"]})

    print("\n⚡  THUNDERWORD QUIZ – Finnegans Wake  ⚡")
    print("Match each fragment of Joyce's thunderwords to its language!\n")

    for tw in data:
        print(f"  [{tw['number']:2d}] page {tw['page']:3d}  {tw['word'][:24]}...")
    thunderword = data[ask_number("\nChoose a thunderword (1-10): ", 1, len(data)) - 1]

    print("\nDifficulty: [1] Easy (2 options)  [2] Medium (4)  [3] Hard (6)")
    option_count = 2 * ask_number("Choose a difficulty (1-3): ", 1, 3)

    # Only segments with a documented language source are quizzed.
    questions = [s for s in thunderword["segments"] if s["explained"]]
    print(f"\nThunderword #{thunderword['number']} (page {thunderword['page']}), split into segments:")
    print("\n  " + " · ".join(s["text"] for s in thunderword["segments"]))

    score = 0
    for i, seg in enumerate(questions, 1):
        print(f"\nRound {i}/{len(questions)}: What language is \"{seg['text']}\" from?\n")
        options = generate_options(seg["language"], languages, option_count)
        for j, option in enumerate(options, 1):
            print(f"  [{j}] {option}")
        chosen = options[ask_number("\nYour answer: ", 1, len(options)) - 1]
        if check_answer(chosen, seg["language"]):
            score += 1
            print(f"✓ Correct! \"{seg['text']}\" → {seg['language']}: {seg['meaning']}")
        else:
            print(f"✗ Wrong! \"{seg['text']}\" → {seg['language']}: {seg['meaning']}")

    result = calculate_score(score, len(questions))
    print(f"\nQuiz complete! Correct: {score}/{len(questions)} ({result['percent']}%)")
    print(result["rating"] + "\n")


if __name__ == "__main__":
    main()

# Thunderword Quiz

#### Video Demo: <YOUR VIDEO URL HERE>
#### Author: <YOUR NAME> (GitHub/edX: <YOUR USERNAME>)
#### Location: <City, Country>
#### Date: <DD Month YYYY>

## Overview

*Finnegans Wake* by James Joyce contains ten famous 100-letter words known as
"thunderwords" (the tenth has 101 letters, for a total of exactly 1001 –
a nod to *One Thousand and One Nights*). Each thunderword imitates the sound
of thunder while hiding real words from dozens of languages – words for
thunder, clapping, coughing, shutting doors, and Norse gods.

This project is a command-line quiz: the player picks one of the ten
thunderwords, sees it split into its segments, and must match each
documented segment to its language of origin in a multiple-choice quiz.
Three difficulty levels control how many answer options are shown:
Easy (2), Medium (4), or Hard (6).

## How to Run

```bash
pip install -r requirements.txt   # installs pytest
python project.py                 # play the quiz
pytest test_project.py            # run the tests (7 tests)
```

## How It Works

`project.py` contains `main` and five top-level functions:

- **`load_thunderword(filepath)`** – Reads the JSON data file and returns a
  list of thunderwords; a missing file raises `FileNotFoundError`.
- **`check_answer(guess, correct)`** – Compares the player's choice with the
  correct language, ignoring case and surrounding whitespace.
- **`calculate_score(correct, total)`** – Converts the result into a percent
  value and a rating sentence; safely handles `total == 0`.
- **`generate_options(correct_language, all_languages, count)`** – Builds a
  shuffled list of `count` answer options that always includes the correct
  language; `count` is set by the chosen difficulty level.
- **`ask_number(prompt, low, high)`** – Re-prompts until the user enters a
  valid number in the given range; used for both menus to avoid duplicated
  input-validation loops.

`main` ties these together: load the data, let the player pick a
thunderword and a difficulty, ask the questions, print the final score.

## The Data

`thunderwords.json` holds all ten thunderwords. Every word is split into
segments that together reproduce the original word letter for letter
(validated: 9 × 100 + 1 × 101 = 1001 letters). Each segment is either

```json
{"text": "tonnerr", "explained": true, "language": "French", "meaning": "thunder (tonnerre)"}
```

or, for pure onomatopoeia, `{"text": "onn", "explained": false}`. Only
explained segments are quizzed.

Building this dataset was a substantial part of the project: all 109
explained segments across 32 languages were manually compiled from the
scholarly annotations in Raphaël Slepon's *Fweets of Finnegans*
(fweet.org, based on Roland McHugh's *Annotations to Finnegans Wake*),
matched to the correct letters of each thunderword, and validated so
that every segmentation reproduces Joyce's original words exactly.

## Design Decisions

- **Only documented segments are quizzed.** Segments without a source in
  the fweet annotations are shown but never asked, so every quiz answer is
  verifiable.
- **Multiple choice instead of free text.** Players cannot be expected to
  spell "Kiswahili" or "Lettish"; selectable difficulty (2, 4, or 6
  options) keeps the game fast, fair, and replayable.
- **Data and code are separated.** All literary content lives in one JSON
  file; the Python code would work unchanged with any other word-segment
  dataset.

## References

- Joyce, James. *Finnegans Wake*. Faber and Faber, 1939.
- Slepon, Raphaël. *Fweets of Finnegans*. https://fweet.org/
- McHugh, Roland. *Annotations to Finnegans Wake*. Johns Hopkins University Press, 1980.

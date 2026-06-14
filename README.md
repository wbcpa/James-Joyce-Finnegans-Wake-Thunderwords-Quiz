# Thunderword Quiz

#### Video Demo: https://youtu.be/FSqG7K5FF2M
#### Author: Wolfgang Bossle (GitHub/edX: wbcpa)
#### Location: Germany
#### Date: 14 June 2026

## Overview

Finnegans Wake by James Joyce contains ten thunderwords totaling exactly
1001 letters – a nod to One Thousand and One Nights. Each thunderword
imitates the sound of thunder while hiding real words from dozens of
languages – words for thunder, clapping, coughing, shutting doors, and
Norse gods.

This project starts with the first three thunderwords (300 letters, 33
documented segments across 25 languages); because the quiz is purely
data-driven, the remaining seven can be added to thunderwords.json later
without changing a single line of code.

The player picks one of the three thunderwords, sees it split into its
segments, and must match each documented segment to its language of
origin in a multiple-choice quiz with four options per question.

## How to Run

```bash
pip install -r requirements.txt   # installs pytest
python project.py                 # play the quiz
pytest test_project.py            # run the tests (7 tests)
```

## How It Works

project.py contains main and five top-level functions:

- load_thunderword(filepath) – Reads the JSON data file and returns a
  list of thunderwords; a missing file raises FileNotFoundError.
- check_answer(guess, correct) – Compares the player's choice with the
  correct language, ignoring case and surrounding whitespace.
- calculate_score(correct, total) – Converts the result into a percent
  value and a rating sentence; safely handles total == 0.
- generate_options(correct_language, all_languages, count) – Builds a
  shuffled list of count answer options that always includes the correct
  language; the quiz uses four options per question.
- ask_number(prompt, low, high) – Re-prompts until the user enters a
  valid number in the given range; used for the thunderword selection menu.

main ties these together: load the data, let the player pick a
thunderword, ask the questions, print the final score.

## The Data

thunderwords.json holds the three thunderwords. Every word is split into
segments that together reproduce the original word letter for letter
(validated: 3 × 100 = 300 letters). Each segment is either

```json
{"text": "tonnerr", "explained": true, "language": "French", "meaning": "thunder (tonnerre)"}
```

or, for pure onomatopoeia, {"text": "onn", "explained": false}. Only
explained segments are quizzed.

Building this dataset was a substantial part of the project: all 33
explained segments across 25 languages were manually compiled from the
scholarly annotations in Raphaël Slepon's Fweets of Finnegans
(fweet.org, based on Roland McHugh's Annotations to Finnegans Wake),
matched to the correct letters of each thunderword, and validated so
that every segmentation reproduces Joyce's original words exactly.

## Design Decisions

- Only documented segments are quizzed. Segments without a source in
  the fweet annotations are shown but never asked, so every quiz answer
  is verifiable.
- Multiple choice instead of free text. Players cannot be expected to
  spell "Kiswahili" or "Lettish"; four answer options per question keep
  the game fast, fair, and replayable.
- Data and code are separated. All literary content lives in one JSON
  file; the Python code would work unchanged with any other word-segment
  dataset.

## References

- Joyce, James. Finnegans Wake. Faber and Faber, 1939.
- Slepon, Raphaël. Fweets of Finnegans. https://fweet.org/
- McHugh, Roland. Annotations to Finnegans Wake. Johns Hopkins University Press, 1980.

"""
test_project.py – pytest tests for the Thunderword Quiz.

Run with: pytest test_project.py
"""

import pytest
from project import load_thunderword, check_answer, calculate_score


def test_load_thunderword_returns_list():
    assert isinstance(load_thunderword("thunderwords.json"), list)


def test_load_thunderword_missing_file():
    with pytest.raises(FileNotFoundError):
        load_thunderword("missing.json")


def test_check_answer_correct():
    assert check_answer("French", "French") == True


def test_check_answer_wrong():
    assert check_answer("French", "Italian") == False


def test_check_answer_case_insensitive():
    assert check_answer("french", "French") == True


def test_calculate_score_perfect():
    result = calculate_score(10, 10)
    assert result["percent"] == 100
    assert "Perfect" in result["rating"]


def test_calculate_score_no_questions():
    assert calculate_score(0, 0)["percent"] == 0

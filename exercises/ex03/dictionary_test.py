__author__: str = "730676777"
"""Tests for Dctionary Functions"""

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

"""Invert tests"""


def test_invert_use_case():
    """Invert test using use case"""
    assert invert({"a": "z", "b": "y", "c": "x"})


def test_invert_edge_case_one():
    """Tests invert with Key error when there are duplicate values"""
    with pytest.raises(KeyError):
        invert({"kris": "jorda", "michael": "jordan"})


def test_invert_edge_case_two():
    """Tests invert using one key and one value"""
    assert invert({"dog": "bird"}) == ({"bird": "dog"})


"""Count tests"""


def test_count_use_case():
    """Test count with duplicates"""
    assert count(["red", "blue", "blue", "green", "red", "blue"]) == {
        "red": 2,
        "blue": 3,
        "Green": 1,
    }


def test_count_edge_case_one():
    """Test count with empty list"""
    assert count([]) == {}


def test_count_edge_case_two():
    "Test count with tie"
    assert count(["red", "orange", "green"]) == {"red": 1, "orange": 1, "green": 1}


"""Favorite_Color Tests"""


def test_favorite_color_use_case():
    """Tests Favorite Color with specific Dictionary and 2 duplicate values"""
    assert (
        favorite_color(
            {"Jack": "red", "Sofia": "blue", "Daniel": "red", "Marcus": "orange"}
        )
        == "red"
    )


def test_favorite_color_edge_case_one():
    """Tests Favoirte Color with tie"""
    assert (
        favorite_color(
            {"Jack": "red", "Sofia": "blue", "Daniel": "red", "Marcus": "blue"}
        )
        == "red"
    )


def test_favorite_color_edge_case_two():
    """Test Favorite Color with 1 value inputed"""
    assert favorite_color({"Jack": "red"}) == "red"


"""Bin Len Tests"""


def test_bin_len_use_case():
    assert bin_len(["I", "like", "big", "cats", "and", "owls"]) == {
        1: {"I"},
        4: {"like", "cats", "owls"},
        3: {"big", "and"},
    }


def test_bin_len_edge_case_one():
    assert bin_len([]) == {}


def test_bin_len_edge_case_two():
    assert bin_len(["I", "like", "like", "cats", "and", "owls"]) == {
        1: {"I"},
        4: {"like", "cats", "owls"},
        3: {"and"},
    }

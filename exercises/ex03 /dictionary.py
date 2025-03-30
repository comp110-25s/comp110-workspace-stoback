__author__: str = "730676777"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Swaps the Key and Value portions of a dictionary"""
    invert_dict = {}
    for key, value in d.items():
        if value in invert_dict:
            raise KeyError("Duplicated keys were found when inverting dictioanry!")
        invert_dict[value] = key
    return invert_dict


def count(items: list[str]) -> dict[str, int]:
    """Function counts the occurances of each string within the input list"""
    count_dict = {}
    for item in items:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color(people_colors: dict[str, str]) -> str:
    """Determines the most common favorite color. If tied returns first color"""
    color_counts = count(list(people_colors.values()))
    max_count = max(color_counts.values())

    for color in people_colors.values():
        if color_counts[color] == max_count:
            return color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Makes a list of strings into a dictionary, with the keys as the lengths and values are sets of strings with that associated length"""
    length_bins = {}
    for word in words:
        length = len(word)
        if length not in length_bins:
            length_bins[length] = set()
        length_bins[length].add(word)
    return length_bins


"""Testing Case for Functions """
if __name__ == "__main__":
    import pytest

    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})
        count(["red", "blue", "green", "blue", "orange"])
        favorite_color(
            {"John": "red", "Daniel": "blue", "Sofia": "red", "Marcus": "Orange"}
        )

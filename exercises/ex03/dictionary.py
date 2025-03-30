__author__: str = "730676777"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Swaps the Key and Value portions of a dictionary"""
    inverted_dictionary = {}
    for key, value in d.items():
        if value in inverted_dictionary:
            raise KeyError("Duplicated keys were found when inverting dictioanry!")
        inverted_dictionary[value] = key
    return inverted_dictionary


def count(items: list[str]) -> dict[str, int]:
    """Function counts the occurances of each string within the input list"""
    dict_result = {}
    for item in items:
        if item in dict_result:
            dict_result[item] += 1
        else:
            dict_result[item] = 1
    return dict_result


def favorite_color(people_colors: dict[str, str]) -> str:
    """Determines the most common favorite color. If tied returns first color"""
    color_counts = count(list(people_colors.values()))
    max_count = max(color_counts.values())
    result = str("")
    for color in people_colors.values():
        if color_counts[color] == max_count:
            result = color
    return result


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Makes a list of strings into a dictionary, with the keys as the lengths"""
    """and the value s are sets of strings with that associated length"""
    length_bins = {}
    for word in words:
        length = len(word)
        if length not in length_bins:
            length_bins[length] = set()
        length_bins[length].add(word)
    return length_bins

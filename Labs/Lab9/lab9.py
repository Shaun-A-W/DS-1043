"""Lab 9: Fuzzy Matching

Implements "comp" function that will provide completions for objects in the current scope.
Comp function utilizes several rudimentary functions, such as ngrams(), to
build the resulting conclusion.

"""
import inspect
from collections import defaultdict


_FUDGE = 1 # comp returns all matches with length >= longest match - fudge


def ngrams(word: str) -> list[str]:
    """Returns a list of n-grams of word for all relevant n, in descending order of n."""
    return [word[i:i+n] for n in range(len(word), 0, -1) for i in range(0, len(word) - n + 1)]


def add_to_index(option: str, index: dict[str, list[str]]) -> None:
    """Adds a valid option to the n-gram index."""
    opt_ngrams = ngrams(option)
    for ngram in opt_ngrams:
        index[ngram].append(option)


def build_index(options: list[str]) -> dict[str, list[str]]:
    """Creates an n-gram index from options.
    The n-gram index will be a dictionary with n-grams as keys, and lists of corrosponding options as values."""
    index = defaultdict(list)
    for option in options:
        add_to_index(option, index)
    return index


def fuzzy_pick(query: str, index: dict) -> dict[str,str]:
    """Returns suggestions for valid options based on the query string.
    Suggestions will take the form of a dictionary with suggestions as keys and longest matching ngram as the value"""
    suggestions = {}
    q_grams = ngrams(query)
    for ngram in q_grams:
        if ngram in index:
            for match in index[ngram]:
                if match not in suggestions:
                    suggestions[match] = ngram
                else:
                    if len(index[match]) > len(suggestions[match]):
                        suggestions[match] = match
        else: continue
    return suggestions


def comp(query: str, dunders=False) -> None:
    """Provides completions for all objections in the current Python REPL session.
    By default, objects starting with underscores are excluded, but this behavior can be adjusted by passing dunders=True"""
    options = dict(inspect.getmembers(inspect.stack()[len(inspect.stack()) - 1][0]))["f_globals"]
    if 'inspect' in options:
        options.pop('inspect')
    targets = [obj + '.' + attr
               for obj in options.keys()
               for attr in dir(options[obj])
               if dunders or not (obj.startswith('_')
                                  or attr.startswith('_'))]
    index = build_index(targets)
    suggestions = fuzzy_pick(query, index)
    if len(suggestions) == 0:
        return
    sorted_suggestions = sorted(suggestions.keys(), key=lambda x: len(suggestions[x]), reverse=True)
    longest_match = len(suggestions[sorted_suggestions[0]])
    for suggestion in sorted_suggestions:
        if len(suggestions[suggestion]) >= longest_match - _FUDGE:
            print(suggestion, '(' + suggestions[suggestion] + ')')
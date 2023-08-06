# Word Search Puzzle Generator

## Introduction
The mission of this package is to generate a word search puzzle. The requirements are a list of the word and the dimensions of the puzzle.


## Install
You can install it using pip tool [word-search-puzzle](https://pypi.org/project/word-search-puzzle/).

For example:
- Given list of words `['Cat', 'Bear', 'Tiger', 'Lion']`
- Generated panel:
```python
#   _______________
#  | l  w  m  e  r |
#  | i  w  c  e  x |
#  | o  v  g  a  q |
#  | n  i  n  i  t |
#  | t  b  e  a  r |
#   ---------------

panel.cells = {
    (0, 0): 'l', (0, 1): 'w', (0, 2): 'm', (0, 3): 'e', (0, 4): 'r', 
    (0, 0): 'i', (0, 1): 'w', (0, 2): 'c', (0, 3): 'e', (0, 4): 'x', 
    (0, 0): 'o', (0, 1): 'v', (0, 2): 'g', (0, 3): 'a', (0, 4): 'q', 
    (0, 0): 'n', (0, 1): 'i', (0, 2): 'n', (0, 3): 'i', (0, 4): 't', 
    (0, 0): 't', (0, 1): 'b', (0, 2): 'e', (0, 3): 'a', (0, 4): 'r', 
}


```
- With the corresponding hidden words:
```json
{
    "words": [
        {
            "value": "cat",
            "positions": [
                { "r": 1, "c": 2 },
                { "r": 2, "c": 3 },
                { "r": 3, "c": 4 }
            ]
        },
        {
            "value": "bear",
            "positions": [
                { "r": 4, "c": 1 },
                { "r": 4, "c": 2 },
                { "r": 4, "c": 3 },
                { "r": 4, "c": 4 }
            ]
        },
        {
            "value": "tiger",
            "positions": [
                { "r": 4, "c": 0 },
                { "r": 3, "c": 1 },
                { "r": 2, "c": 2 },
                { "r": 1, "c": 3 },
                { "r": 0, "c": 4 }
            ]
        },
        {
            "value": "lion",
            "positions": [
                { "r": 0, "c": 0 },
                { "r": 1, "c": 0 },
                { "r": 2, "c": 0 },
                { "r": 3, "c": 0 }
            ]
        }
    ]
}
```


## Generate a puzzle
All what you need is de define a list of words and provide the dimensions of the panel.
Please make sure that the number and the length of the words fit the dimensions of the panel.

```python
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel

words = ['Cat', 'Bear', 'Tiger', 'Lion']

result = create_panel(height=5, width=5, words_value_list=words)

print('Attempts: {}'.format(result.get('attempts')))
print('Solution took: {} ms'.format(result.get('elapsed_time')))
display_panel(result.get('panel'))

# Output:
#   Attempts: 2
#   Solution took: 31 ms
#
#   l  w  m  e  r
#   i  w  c  e  x
#   o  v  g  a  q
#   n  i  n  i  t
#   t  b  e  a  r
```


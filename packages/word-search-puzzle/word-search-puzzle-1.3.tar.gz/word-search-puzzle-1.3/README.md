# Word Search Puzzle Generator

## Introduction
The mission of this package is to generate a word search puzzle. The requirements are a list of the word and the dimensions of the puzzle.


## Install
You can install it using pip tool [word-search-puzzle](https://pypi.org/project/word-search-puzzle/).

![Panel example](panel.png)


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


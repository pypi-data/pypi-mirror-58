<h1 align="center">Cmd colorizer</h1>

Python library for using color text in cmd

[![CodeFactor](https://www.codefactor.io/repository/github/kochan-s/cmd_colorizer/badge)](https://www.codefactor.io/repository/github/kochan-s/cmd_colorizer)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7cf6bb397e724ea3819262339f12c316)](https://www.codacy.com/manual/leskapopp/cmd_colorizer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=KoChan-s/cmd_colorizer&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/cmd-colorizer.svg)](https://badge.fury.io/py/cmd-colorizer)

## Getting started
***Installation***:
`pip install cmd_colorizer` or `pip install git+git://github.com/KoChan-s/cmd_colorizer.git`

***Import***:
```python
from cmd_colorizer import colored
```

## Using
```python
print(colored("Some text", "red", "blue", ["bold", "underline"]))
```

`1 param - text that should be colored`  
`2 param - color of the text **(grey, red, green, yellow, blue, magenta, cyan, white)**`  
`3 param - background color **(grey, red, green, yellow, blue, magenta, cyan, white)**`  
`4 param - attributes the text **(bold, dark, underline, blink, reverse, concealed)**`  

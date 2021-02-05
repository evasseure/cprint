[![Build Status](https://travis-ci.org/EVasseure/cprint.svg?branch=master)](https://travis-ci.org/EVasseure/cprint)

## cprint

Do you find it annoying when you have to search for a certain debug, or error, line in your console? Have you ever dreamed of a simple and quick way to make your debug print truly visible? Well here is your solution!  
cprint is a minimalist python library which gives you the possibility to print in color.  

## Install

`pip install cprint`

## Usage

```python
from cprint import *

cprint(arg) 							# WHITE
cprint.ok(arg)							# BLUE
cprint.info(arg)						# GREEN
cprint.warn(arg)						# YELLOW
cprint.err(arg, interrupt=False)		# BROWN
cprint.fatal(arg, interrupt=False)		# RED
```

![Demo](/img/screen.png)

In case you have issues under Windows, try installing colorama with `pip install colorama`.

[![Build Status](https://travis-ci.org/EVasseure/cprint.svg?branch=master)](https://travis-ci.org/EVasseure/cprint)

## Cprint

cprint is a small and simple python library which gives you the possibility to print in color.  

## Install

python setup.py install  

## Usage

```python
from cprint import *

cprint(str) 							# WHITE
cprint.ok(str)							# BLUE
cprint.info(str)						# GREEN
cprint.warn(str)						# YELLOW
cprint.err(str, interrupt=False)		# BROWN
cprint.fatal(str, interrupt=False)		# RED
```

![Demo](/img/screen.png)
# [PyCtrl](http://hammie217.github.io/PyCtrl)
[![Build Status](https://travis-ci.com/Hammie217/PyCtrl.svg?token=2HV22j5ihLUf9pzgZL6y&branch=master)](https://travis-ci.com/Hammie217/PyCtrl)
[![Coverage Status](https://coveralls.io/repos/github/Hammie217/PyCtrl/badge.svg?branch=master)](https://coveralls.io/github/Hammie217/PyCtrl?branch=master)
## Functions:
### singleChoice

Takes 1-3 inputs:

  1 - Array to be listed  
  2 - Set cursor color (See accepted colors below) - Default "Blue"  
  3 - Return array as postion value ("Val") or text ("Text") - Default: "Val"  

#### Example:

```
valArray=["Choice1","Choice2","Choice3"]  
print(singleChoice(valArray,"Magenta","Text"))
```
### MultiChoice
  1 - Array to be listed  
  2 - Set cursor color (See accepted colors below) - Default "Blue"  
  3 - Return array as postion value ("Val") or text ("Text") - Default: "Val"  
  4 - Selected display character (Sets the selected character. "T" sets a tick, "X" sets a cross. Anything else is used directly as the character)  
  5 - Sets the displayed selecter character color (Same accepted colors as previous)  
#### Example:

```
valArray=["Choice1","Choice2","Choice3"]  
print(*multiChoice(valArray,"Red","Text","X","Magenta"), sep='\n')  
```

## Accepted colors :
Black  
Red  
Green  
Yellow   
Blue  
Mangenta 
Cyan  
White  
Reset  

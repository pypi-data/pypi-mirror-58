# brainfuck-interpreter
An object-oriented highly flexible brainfuck interpreter.

## Why?
Even though there are probably countless of other options,
I've made this because I found other projects were too high-level for me
and didn't provide much control over the interpreter.
This module, however, allows the developer to access, modify and
control every piece of how the brainfuck is evaluated, making this
program superior to other projects.

It was also a fun project to work on in general.

## Features
* Object-oriented
* Easy to use
* Logging integration
* Allows streaming of brainfuck code
* Manual input/output stream control
* Manual interpreter stepping

## Examples
A basic example which should suit most usages of this library:
```python
import brainfuck

bf = '+[----->+++<]>+.---.+++++++..+++.[--->+<]>----.'
print(brainfuck.evaluate(bf))  # hello!
```
For examples featuring more control over the interpreter,
check out [the examples directory](examples).
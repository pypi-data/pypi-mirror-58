# Logfast

## Purpose
Just a simple python package which does logging initialization in a certain way.

```
17|12|19|00:18:58|+0100  14474:MainThread  INFO       |__init__.py.21  |   This is an example
17|12|19|00:18:58|+0100  14474:MainThread  WARNING    |__init__.py.22  |   Another one
```
As one can see it provides the filename where the log has been created, the Process ID
, the Thread Name, and the full time (including).
This is a package I created for my own benefit, as i found myself tired of always doing the same logging initalization.

Now i can just ```pip install logfast``` whereever i am. 

Most likely you will want to a have different logging format than me(so this package might be of no use to you).
But if you want the same format feel free to use it.

## Installation

```pip install logfast```

## Usage Guide
Make sure this is the first module you import in your application.
This makes sure no other call is made first to logging.
Otherwise other modules/libraries might overwrite the logging settings.
This allows you to have multiple application entrypoints but have the same logging configuration.

```
import logfast
import logging

logger = logging.getLogger()


logger.info("This is an example")
logger.warning("Another one")
```

# rlogger

A convenient encapsulation of Python logging

## Install

```shell
pip install rlogger
```

## Use

```python
from rlogger import RLogger
# Set log file path
RLogger.init('file.log', screen_log=True)
RLogger.log('your message', RLogger.INFO)
RLogger.log('your message', RLogger.DEBUG)
RLogger.log('your message', RLogger.WARNING)
RLogger.log('your message', RLogger.ERROR)
# Close log when you not need
RLogger.close()
RLogger.log('your message', RLogger.ERROR) # Will not print
```

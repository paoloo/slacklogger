# SLACKLOGGER
**A logger/notifier that writes, through a bot, into any [Slack](https://slack.com/) channel.**

It contains a module importable on python to act as a remote logger(similar to logging
lib) and, also, a stand-alone unix-style pipe-friendly application that sends text
through a bot to any [Slack](https://slack.com/) channel configured. 

[Slack](https://slack.com/) is a modern real-time messaging platform, similar to IRC,
but focused on teamwork.

[![BSD License](https://img.shields.io/badge/license-BSD-blue.svg)](LICENSE)

### REQUIREMENTS
- python 2.7+
- pyOpenSSL
- websocket-client

But everything installed via [setuptools](https://pypi.python.org/pypi/setuptools)

### INSTALATION

  `$ pip install slacklogger`

### USAGE

  First, register a bot on desired organization/channel here: https://my.slack.com/services/new/bot
and get its APIKEY. Then grab channel id on slack interface and add the bot to the channel. From
this point on, you can use it as a python import or a stand-alone message sender.

#### - As a module
```
>>>  from slacklogger import Notify
>>>  info=Notify('xoxb-MYTOKEN','CHANNEL-ID')
>>>  info.write("Any text written here will be sent to slack channel!")
>>>  info.write("Thix text too!")
>>>  # ...
>>>  info.close()
```
#### - As a stand-alone bash application
```
   $ export SLACKTOKEN=xoxb-MYTOKEN
   $ export SLACKCHAN=A0B1C2D3E
```
*then*
```  
   $ slacklogger -t "text to send"
```
*or*
```
   $ echo "text to send" | slacklogger -
```  
*for help:*
```    
   $ slacklogger -h

   Usage: slacklogger -t "text to send" or  echo "text to send" | slacklogger -

   SLACK notifier app. It uses the environment variables SLACKTOKEN and SLACKCHAN
   to work.

   Options:
     --version             show program's version number and exit
     -h, --help            show this help message and exit
     -t TEXT, --text=TEXT  Text to send to slack channel. Use - to redirect pipe
                        or use stdin.
```

### TO DO
- Use channel name instead of channel ID, consulting API https://slack.com/api/users.list and extracting all channels for organization;
- create a logging.log()-like interface to write warnings, errors with colors and attachments, to debug applications from a slack channel.

### Tested on
- Linux raspberrypi 3.10.25+ #622 PREEMPT Fri Jan 3 18:41:00 GMT 2014 armv6l GNU/Linux
- FreeBSD macabeus 10.2-RELEASE FreeBSD 10.2-RELEASE #0 r286666: Wed Aug 12 15:26:37 UTC 2015 amd64
- Linux avellgpu 3.13.0-85-generic #129-Ubuntu SMP Thu Mar 17 20:50:15 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

### License
[BSD License](LICENSE).

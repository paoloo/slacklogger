#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slacklogger import Notify

def main():
    from optparse import OptionParser
    import sys, os
    desc='SLACKLOGGER uses the environment variables SLACKTOKEN and SLACKCHAN to work.'
    uso='%prog -t "text to send" or  echo "text to send" | %prog -'
    parser = OptionParser(usage=uso, version="%prog 0.1.5", description=desc)
    parser.add_option('-t', '--text', dest='text', help='Text to send to slack channel. Use - to redirect pipe or use stdin.')

    (opts,args)=parser.parse_args()
    if opts.text:
        if opts.text == '-':
            _text = sys.stdin.read()
        else:
            _text = opts.text
        # === verify enviroinment variables =======================================
        if os.environ.get('SLACKTOKEN') != None and os.environ.get('SLACKCHAN') != None:
            _msg = Notify(os.environ.get('SLACKTOKEN') , os.environ.get('SLACKCHAN'))
            _msg.write(_text)
            _msg.close()
        else:
            print 'environment variables SLACKTOKEN and SLACKCHAN must be defined with, respectivelly,\nthe token and the channel id, got from Slack.'
            exit(-1)
    else:
        # print 'No text to send. -h to help'
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    main()

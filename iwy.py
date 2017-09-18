import time
import commands
import datetime
import telepot

from telepot.loop import MessageLoop

from pprint import pprint


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']


    print 'Got command: %s' % command
    print 'message by : %s' % chat_id
    if command == '/log':
        bot.sendMessage(chat_id, str(commands.getoutput('tail /var/log/mysql/error.log')))
    elif command == '/status':
        bot.sendMessage(chat_id, str(commands.getoutput('systemctl status mysql.service')))
    elif command == '/running':
        bot.sendMessage(chat_id, str(commands.getoutput('systemctl status mysql.service | grep running')))
    elif command == '/date':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    else:
    	bot.sendMessage(chat_id, str("no conozco esa instruccion"))


bot = telepot.Bot('440619284:AAFvygLY53ZjqgGuk8DJB399Xfu2Rx8YT-s')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
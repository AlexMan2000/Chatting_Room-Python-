import socket
import time

# use local loop back address by default
#CHAT_IP = '127.0.0.1'
CHAT_IP = socket.gethostbyname(socket.gethostname())
# CHAT_IP = ''#socket.gethostbyname(socket.gethostname())

CHAT_PORT = 1112
SERVER = (CHAT_IP, CHAT_PORT)

menu = "\n++++ Choose one of the following commands\n \
        time: calendar time in the system\n \
        who: to find out who else are there\n \
        c _peer_: to connect to the _peer_ and chat\n \
        ? _term_: to search your chat logs where _term_ appears\n \
        p _#_: to get number <#> sonnet\n \
        q: to leave the chat system\n\n"

S_OFFLINE   = 0
S_CONNECTED = 1
S_LOGGEDIN  = 2
S_CHATTING  = 3

SIZE_SPEC = 5

CHAT_WAIT = 0.2

def print_state(state):
    print('**** State *****::::: ')
    if state == S_OFFLINE:
        print('Offline')
    elif state == S_CONNECTED:
        print('Connected')
    elif state == S_LOGGEDIN:
        print('Logged in')
    elif state == S_CHATTING:
        print('Chatting')
    else:
        print('Error: wrong state')

def mysend(s, msg):
    #append size to message and send it
    #明确单次发送文件的字节流长度信息(自定义协议)
    msg = ('0' * SIZE_SPEC + str(len(msg)))[-SIZE_SPEC:] + str(msg)
    msg = msg.encode()
    total_sent = 0
    while total_sent < len(msg) :
        sent = s.send(msg[total_sent:])
        if sent==0:
            print('server disconnected')
            break
        total_sent += sent

def myrecv(s):
    #receive size first（防止数据粘包问题）
    size = ''
    while len(size) < SIZE_SPEC:
        text = s.recv(SIZE_SPEC - len(size)).decode()
        #如果获取不到size数据，说明没有信息发送过来，表明客户端丢失连接
        if not text:
            print('disconnected')
            return('')
        size += text
    size = int(size)
    #now receive message（确保信息完全接收)
    msg = ''
    while len(msg) < size:
        text = s.recv(size-len(msg)).decode()
        if text == b'':
            print('disconnected')
            break
        msg += text
    #print ('received '+message)
    return (msg)


def text_proc(text, user):
    #Seems to be different from the requirement in UP3 spec?
    # ctime = time.strftime('%d.%m.%y,%H:%M', time.localtime())
    ctime = time.strftime('%H:%M:%S', time.localtime())
    # #Also different from the UP3 Spec?
    # return('(' + ctime + ') ' + user + ' : ' + text) # message goes directly to screen
    return ('('+user+')'+ctime+' ' + text)


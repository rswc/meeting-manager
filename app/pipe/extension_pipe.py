#!/usr/bin/env python

import sys
import json
import struct
import os

PATH = os.path.dirname(os.path.realpath(__file__))[:-4] + 'event'
print(PATH)
sys.path.insert(1, PATH)
import event

# Python 3.x version
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    with open ("yomama.txt", 'a') as debug:
        debug.write(len(raw_length), message)
    return json.loads(message)

# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

def read_message() -> str:
    return getMessage()
    
def send_message(message: str):
    sendMessage(encodeMessage(message))

send_message("[PIPE] starting pipe process.")
while True:
    web_extension_request = read_message()
    event_response = event.pass_request(web_extension_request)
    send_message(event_response)
send_message("[PIPE] ending pipe process.")
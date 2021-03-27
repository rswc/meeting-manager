from queue import PriorityQueue
from event import event as ev
import json, os, datetime

MAX_QUEUE_TIME =  datetime.datetime.now().timestamp() + 53

def build_que():
    que = PriorityQueue()
    for x in ev.get_events_for_queue(): #Put all events on que TODO max_que_forward_time_limit
        que.put(x)


    for x in range(50):
       if que.qsize()>0: print(que.get())
       else: exit("Queue is empty")

if __name__ == "__main__":
    build_que()


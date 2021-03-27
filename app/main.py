from queue import PriorityQueue
from event import event as ev
import json, os, datetime
from multiprocessing import Process

MAX_QUEUE_TIME =  datetime.datetime.now().timestamp() + 53


def build_que(que):
    for x in ev.get_events_for_queue(): #Put all events on que TODO max_que_forward_time_limit
        if x[0] - datetime.datetime.now().timestamp() > 0:
            que.put(x)

def que_loop(arg):
    print(arg)
    while(True):

        que = PriorityQueue()
        build_que(que)

        if que.qsize() == 0: exit("Queue is empty")
        else: 
           e = que.get()
           t = datetime.datetime.fromtimestamp(e[0]) - datetime.datetime.now()
           print(f"Time to the next event: {int(t.total_seconds()/60/60)}h {int((t.total_seconds()/60)%60)}m" )

        import time
        time.sleep(5)



if __name__ == "__main__":
    p = Process(target=que_loop, args=('Peter',), name="YOOO")
    p.start()
    print("yo")
    
    
    

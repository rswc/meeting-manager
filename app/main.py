from queue import PriorityQueue
from event import event as ev
import json, os, datetime
from multiprocessing import Process
import time
import runner.launch_meeting as rl

MAX_QUEUE_TIME =  datetime.datetime.now().timestamp() + 53


def build_que(que):
    for x in ev.get_events_for_queue(): #Put all events on que TODO max_que_forward_time_limit
        if x[0] - datetime.datetime.now().timestamp() > 0:
            que.put(x)
        #print(x)

def que_loop(arg):
    #print(arg)
    while(True):

        que = PriorityQueue()
        build_que(que)

        if que.qsize() == 0: exit("Queue is empty")
        else: 
            e = que.get()
            t = datetime.datetime.fromtimestamp(e[0]) - datetime.datetime.now()
            print(f"Time to the next event: {int(t.total_seconds()/60/60)}h {int((t.total_seconds()/60)%60)}m {t}s" )
            time.sleep(5)
            
            if t.total_seconds() <= 30:
                rl.notify(f"You have a meeting: {ev.get_displayname(e[1])} in {int(t.total_seconds())} seconds")
                time.sleep(10)
                rl.launch_meeting(ev.get_link(e[1]), browser="firefox")
                exit()
            
            if t.total_seconds() > 600:
                exit()
    



if __name__ == "__main__":

    tmp = datetime.datetime.now() + datetime.timedelta(0, 70)
    print(tmp)
    A = {
        "cmd":"EDIT",
        "data":{
                "db9c66e3cf0a49c6a6ee": {
            "Title": "Systemy Operacyjne",
            "Link": "https://zoom.us/wc/6866658590/join?pwd=Y0d3c29OakpKQk1MT01ZbW5GVWpudz09",
            "Comment": "Moje ulubione zajęcia",
            "Date": f"28/03/2021 {str(tmp.hour)}:{str(tmp.minute)}:{str(tmp.second)}",
            "Recurring": "EVERY_WEEK",
            "Type": "TYPE_BBB"
            }
        }
    }
    print(ev.pass_request(json.dumps(A, ensure_ascii=False, indent=4)))


    p = Process(target=que_loop, args=('Peter',), name="YOOO")
    p.start()
    #print("yo")
    
    
    

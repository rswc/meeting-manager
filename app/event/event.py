import datetime, json, uuid, os
"""
Types: TYPE_ZOOM, TYPE_BBB
Date: datetime format
Recurrent options: NO, EVERY_WEEK, EVERY_OTHER_WEEK, DAILY, MONTHLY

"""
JSON_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\event\events.json"
JSON_TEST_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\event\test.json"

class Event:
    '''Holds data of a specific event'''
    def __init__(self, json_data):
        '''Pass serialized json string'''
        self.s_json = json_data
        self.raw_dic = json.loads(json_data)

    def save(self):
        '''Save event to main file'''
        m_json = {}
        if not os.path.isfile(JSON_PATH): #If file doesn't exist - create
            with open(JSON_PATH, "w") as outfile:
                json.dump(m_json, outfile, indent=4, ensure_ascii=False)

        with open(JSON_PATH, encoding='utf8') as outfile: #Read json and append 
            m_json = json.load(outfile)
        m_json[str(uuid.uuid4().hex)[0:20]] = self.raw_dic #append new json object
        self.__save(m_json)

    def get_all_events(self):
        '''Return all events (serialized) saved in events.json'''        
        with open(JSON_PATH, encoding='utf8') as outfile:
            return json.load(outfile)

    def update_json(self, event_to_change):
        '''Update particular event (or events) in events.json'''
        m_json = self.get_all_events()
        
        d_changes = event_to_change
        for e_key in event_to_change.keys(): #Get key from event json
            m_json[e_key] = d_changes[e_key] #Update all
        
        self.__save(m_json)
        
    def __save(self, dic):
        with open(JSON_PATH, "w", encoding='utf8') as outfile: #Save file
            json.dump(dic, outfile, indent=4, ensure_ascii=False)

    def delete_event(self, event_to_delete):
        '''Delete passed event(s) '''
        m_json = self.get_all_events()
        for key in event_to_delete.keys():
            del m_json[key]

        self.__save(m_json)
    

def pass_request(json_string):
    req = json.loads(json_string)
    command = req["cmd"]
    j_data = req["data"]
    if command.lower() == 'add':
        a = Event(json.dumps(j_data, ensure_ascii=False))
        a.save()
        return "Saved succesfully"
    return "Command not found"

def get_timestamp(x):
    # a,b = x[1].split(' ')
    # day, month, year = a.split('/')
    # hour,minute = b.split(':')
    # t = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    format_ = r'%d/%m/%Y %H:%M'
    dt_object = datetime.datetime.strptime(x[1], format_)
    return (dt_object.timestamp(), x[0])

def get_events_for_queue():
    '''Return list of tuples (timestamp, event_id)''' 
    events = {}       
    with open(JSON_PATH, encoding='utf8') as outfile:
        events = json.load(outfile)

    ret = list()

    for key in events.keys():
        ret.append((key, events[key]['Date']))
        #print(key, events[key]['Date'])
    ret = list(map(lambda x: get_timestamp(x), ret))
    return ret



# A = {
#     "cmd":"ADD",
#     "data":{
#         "Link":"https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage",
#         "Title":"Window.sessionStorage - Web APIs | MDN",
#         "Date":"27/02/2021 21:12",
#         "Reccurring":"NO",
#         "Comment":"YO",
#         "Type":"TYPE_ZOOM"}
#         }

# dumped=  json.dumps(A, indent=4, ensure_ascii=False)
# pass_request(dumped)
# # get_events_for_queue()
# data ={}
# data['Title'] = "Sysopsy"
# data['Link'] = r"https://cwww.google.com"
# data['Comment'] = "Moje ulubione zajęcia"
# data['Date'] = '28/03/2021 12:30'
# data['Recurring'] = "EVERY_WEEK" #TODO recurrent
# data['Type'] = "TYPE_BBB"

# s = { "d13b404a95544b6eb4f4" : data}
# test_json = json.dumps(data, indent=4, ensure_ascii=False)
# a = Event(test_json)
# a.save()
# # a.edit_json(s)

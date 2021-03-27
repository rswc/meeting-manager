import datetime, json, uuid, os
"""
Types: TYPE_ZOOM, TYPE_BBB
Date: datetime format
Recurring options: EVERY_WEEK, EVERY_OTHER_WEEK, DAILY, MONTHLY

"""
JSON_PATH = "events.json"

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

    def edit_json(self, event_to_change):
        '''Update particular event (or events) in events.json'''
        m_json = self.get_all_events()
        
        d_changes = event_to_change
        for e_key in event_to_change.keys(): #Get key from event json
            m_json[e_key] = d_changes[e_key] #Update all
        
        self.__save(m_json)
        
    def __save(self, dic):
        with open(JSON_PATH, "w", encoding='utf8') as outfile: #Save file
            json.dump(dic, outfile, indent=4, ensure_ascii=False)



# data ={}
# data['Title'] = "Sysopsy"
# data['Link'] = r"https://www.google.com"
# data['Comment'] = "Moje ulubione zajęcia"
# data['Date'] = str(datetime.datetime.now()) #TODO date
# data['Recurring'] = "EVERY_WEEK" #TODO recurrent
# data['Type'] = "TYPE_BBB"

# s = { "d13b404a95544b6eb4f4" : data}
# test_json = json.dumps(data, indent=4, ensure_ascii=False)
# a = Event(test_json)
# a.save()
# a.edit_json(s)

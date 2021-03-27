import datetime, json, uuid, os
"""
Types: TYPE_ZOOM, TYPE_BBB
Date: datetime format
Recurrent options: EVERY_WEEK, EVERY_OTHER_WEEK, DAILY, MONTHLY

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
                json.dump(m_json, outfile, indent=4)

        with open(JSON_PATH,) as outfile: #Read json and append 
            m_json = json.load(outfile)
        m_json[str(uuid.uuid4().hex)[0:20]] = self.raw_dic #append new json object
        
        with open(JSON_PATH, "w") as outfile: #Save file
            json.dump(m_json, outfile, indent=4)

    def get_all_events(self):
        '''Return all events (serialized) saved in events.json'''        
        with open(JSON_PATH,) as outfile:
            return json.load(outfile)


data ={}
data['Title'] = "Angielski"
data['Link'] = r"https://www.google.com"
data['Comment'] = "Moje ulubione zajęcia"
data['Date'] = str(datetime.datetime.now()) #TODO date
data['Recurrent'] = "EVERY_WEEK" #TODO recurrent
data['Type'] = "TYPE_ZOOM"

#print(data)

test_json = json.dumps(data, indent=4)
#print(test_json)
a = Event(test_json)
a.save()
print(a.get_all_events())

# date = datetime.datetime.now()
# print(date.weekday())
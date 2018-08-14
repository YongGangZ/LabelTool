import json


class JSON:
    def __init__(self):
        pass

    def JSONRead(self,path):
        with open(path, 'r') as json_f:
            data = json.load(json_f)
        return data

    def JSONWrite(self,path,dict_info):
        with open(path,'w') as json_f:
            json.dump(dict_info, json_f)



j = JSON()
h = j.JSONRead('E:/python_project/MyGUI/test.json')
print(h)
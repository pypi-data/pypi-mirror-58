import json


class Instance:
    def __init__(self, content):
        for i in range(len(content)):
            del content[i]['_id']

        self.instance = content

    def pack(self):
        return json.dumps({
            "instance": self.instance
        })

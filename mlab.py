import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds129402.mlab.com:29402/thuoclao

host = "ds129402.mlab.com"
port = 29402
db_name = "thuoclao"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
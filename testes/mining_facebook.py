import json 
import facebook 

def main():
    token = '{EAALxQPbRkCoBAOGsKzm08QsKBnFayYtb7ESbwFeJXOPKvbRcqVg11He3lHAMKhc7bHAbKCXsUAGWk3hQCCN5ckUUSlZAtTj5jT3Y3fsYVJ24IchBnxNcPnTaUYq5IExS5ucED3nC9YlpiibZCTm09s6QQ7tQWp4mYzjizBZAPO3kzDuOx2Ul2BcnqJ8cKWGHB8HZB1Bh3hhGDBjhPREL}'
    graph = facebook.GraphAPI(token)
    perfil = graph.get_object('me', fields = 'first_name')
    print(json.dumps(perfil, indent=4))
    
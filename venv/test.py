import requests

def request_to_fastkore(uri, data):
    headers = {
        "Content-Type": "text/html"
    }
    response = requests.post(uri, data=data, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response
        # inJson = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
        # inDict = json.loads(inJson)
        # return inDict
    else:
        return -1


print(requests.post("http://cloud.fastkore.ru:27026/sdgijpxjknfg/load", data="8531").text)
# print(request_to_fastkore("http://cloud.fastkore.ru:27026/sdgijpxjknfg/load", 8511))
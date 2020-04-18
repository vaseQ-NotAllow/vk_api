import requests
import json


def api_request(method_name, params):
    r = requests.get(f'https://api.vk.com/method/{method_name}', params=params)
    if r.status_code == requests.codes.ok:
        return json.loads(r.text)
    else:
        return f"code of response {r.status_code}"


def check_error(answer):
    if "error" in answer:
        print(answer["error"]['error_msg'])
        return True
    return False


def get_friends(params):
    result = api_request("friends.get", params)
    if check_error(result):
        return
    print(json.dumps(result["response"]["items"], indent=4))

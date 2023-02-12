import requests
import json

class Integration:
    cache = []

    def send(action, app_data, password, to_user) -> bool:
      data = {
        "action": action,
        "app_data": app_data
      }

      data = json.dumps(data)


      request_body = {
        "password": password,
        "to_user": to_user,
        "data": data,
      }

      response = requests.post('http://0.0.0.0:8000/send/', data=request_body)

      return True if response.text != "false" else False




    def get():

      response = requests.get('http://0.0.0.0:8000/transactions/received')
      transactions = response.json()

      new_dict = {}

      for transaction in transactions:
        if transaction in Integration.cache:
          continue
        else:
          new_dict[transaction] = transactions[transaction]
          Integration.cache.append(transaction)
      for transaction in new_dict:

        new_dict[transaction]["transaction"]["data"] = json.loads(new_dict[transaction]["transaction"]["data"])
        if new_dict[transaction]["transaction"]["data"]["action"] == "app_name_action_name":
          print(new_dict[transaction]["transaction"]["data"]["app_data"])

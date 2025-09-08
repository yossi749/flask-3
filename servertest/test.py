import requests
import time

url = "http://app:5000/add"
data = {"title": "נאיף זה גס Flask"}

start_time = time.time()
success = False

while time.time() - start_time < 60:  # עד דקה
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Success!")
            success = True
            break
    except requests.exceptions.ConnectionError:
        pass
    time.sleep(2)

if not success:
    print("Error: not working")

import requests
import json

db_name = "XXXX" #データベースの名前を指定
coll_name = "XXXX" #コレクションの名前を指定

url = 'http://XXXX' #データベースがある場所のURLを入力
payload = {
    "db_name": db_name,
    "coll_name": coll_name,
    "need": "dist", # x / y / distの中から一つ選ぶ
    "ans": { #正解の座標を入力
        "x": 100,
        "y": 200,
        "z": 68,
    },
    "ble": ( #9つのBLEビーコンの配置した座標を入力
        0,
        (0,150,70),
        (0,0,70),
        (0,300,70),
        (150,0,70),
        (150,300,70),
        (300,0,66),
        (300,300,66),
        (300,150,66),
        (150,150,53)
    )
}
header = {'Content-Type' : 'application/json'} 
#APIのpostリクエストを飛ばして，ペイロードをutf-8形式で返す
response = requests.post(url, data = json.dumps(payload).encode("utf-8"), headers = header)
for res in response:
    print(res)
response.close()
from datetime import datetime, timedelta
import json

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

tomorrow = now + timedelta(days=1)
print(tomorrow.strftime("%Y-%m-%d %H:%M:%S"))

tomorrow = now + timedelta(days=-1)
print(tomorrow.strftime("%Y-%m-%d %H:%M:%S"))

date = { "name" : "张三" , "scores" : [ 90 , 85 , 88 ]}
json_str = json.dumps(date, ensure_ascii=False)

parsed = json.loads(json_str)

# 直接读写文件 
with open ( "data.json" , "w" , encoding= "utf-8" ) as f:
    json.dump(data, f, ensure_ascii= False ) 
with open ( "data.json" , "r" , encoding= "utf-8" ) as f:
    loaded = json.load(f)
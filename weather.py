# 날씨 정보를 요청해서 csv저장하는 코드 
import requests
import csv
import os
from datetime import datetime


# key는 나중에 암호화
My_Api_Key = os.getenv("WEATHER_API_KEY")
City_Name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={City_Name}&appid={My_Api_Key}"
url += "&units=metric" # 온도가 기본값이 k이기 떄문에 mertic을 사용해서 C로 바꿔줌

response = requests.get(url)
result = response.json()
temp = result["main"]["temp"] #main->temp
hum = result["main"]["humidity"]
weather = result["weather"][0]["main"]

# %Y-%m-%d
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 현재시간

# weather.csv를 만들자
# 최초 생성 시 -> 헤더도 추가
# 파일이 존재하면 덮어쓰기

csv_exist = os.path.exists("weather.csv")
header = ["current_time","temp","humidity","weather_state"]

with open("weather.csv","a", newline="") as f :
    writer = csv.writer(f)

    if not csv_exist:
        writer.writerow(header)
    
    writer.writerow([current_time,temp,hum,weather])
print("날씨 저장 완료")

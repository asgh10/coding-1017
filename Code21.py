'''
import datetime
import random

menus = ["김밥", "라면", "돈까스", "떡볶이", "초밥"]
today_menu = random.choice(menus)

now = datetime.datetime.now()
time_string = now.strftime("%Y-%m-%d")

result_text = f"[{time_string}] 오늘의 추천 메뉴: {today_menu}\n"
print(result_text)

with open("menu_log.txt", "a", encoding="utf-8") as f:
  f.write(result_text)
'''

# 현재 연도, 월, 일, 시, 분, 초, 밀리초까지 지금 이 순간의 모든 정보를 가져온다
# 아래 코드처럼 지금이 몇년도인지 알수도 있다

import datetime

now = datetime.datetime.now()

now_month = now.month

print(f"지금은 {now_month}월입니다")

# 이 기능은 now로 지금 시간을 가져올 수도 있지만 내가 시간을 지정해 활용할 수도 있다
# 아래 코드처럼 입력하면 내가 시간을 지정할 수 있다

day  = datetime.datetime(2026, 12, 25)
print(day)

# 미래 날짜에서 과거 날짜를 빼면, 그 사이의 간격(timedelta 객체)이 나온다
# 그래서 아래 코드 처럼 쓴다면 어떤 날이 몇일 남았는지 알려준다

today = datetime.datetime.now()
christmas = datetime.datetime(2026, 12, 25)

left_day = christmas - today
print(f"크리스마스까지 {left_day.days}일 남았습니다")

# strftime은 "String Format Time"의 줄임말인데 쉽게 말해 "시간을 내가 원하는 글자 모양으로 바꿔줘"라는 뜻이다
# 아래 코드처럼 쓰게 된다면 내가 원하는 모양으로 쓸 수 있다
now = datetime.datetime.now()

pretty_time = now.strftime("%Y년 %m월 %d일 %H시 %M분")
print(pretty_time) 

'''
%Y: 네 자리 연도 (예: 2026)

%m: 월 (예: 10)

%d: 일 (예: 17)

%H: 24시간 형식 시간

%M: 분

%S: 초
'''
'''
import random

booms = []

while True:
    my_booms = input("벌칙을 입력해주세요(exit 입력 시 종료): ")

    if my_booms == "exit":
        break
    else:
        booms.append(my_booms)

random_booms = random.choice(booms)
print(f"이번 벌칙은 {random_booms} 입니다")

'''

import datetime

text = input("당신의 생일이 지났습니까 (yes/no): ")

if text == "no":
  year = 2026
elif text == "yes":
  year = 2027
else:
  print("yes or no 로 대답 해주세요 (대소문자도 맞춰 주세요)")
  exit() 

month = int(input("당신 생일의 달을 적어주세요 (숫자만): "))
day = int(input("당신 생일의 날을 적어주세요 (숫자만): "))

birthday = datetime.datetime(year, month, day)
today = datetime.datetime.now()
d_day = birthday - today

print(f"생일까지 총 {d_day.days}일 남았습니다!")




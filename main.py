import os
import requests

while True:
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check.(seperate by comma)")
  URL = input("")
  URL = URL.split(",")
  #마지막 글자가 닷컴이 아니면 유효한 주소가 아니다
  for i in URL:
    i=i.strip()
    if i[-4:] != ".com": 
      print("{} is not a valid URL".format(i))
  #맨 앞글자가 http://가 아니면 URL에 추가해준다
    elif i[:7] != "http://":
      i = "http://"+i
    try: #URL 주소를 get한다
      response = requests.get(i) 
      print("{} is up".format(i)) #정상 URL
    except :
      print("{} is down!".format(i))

  start=input("Do you want to start over? y/n : ")
  if start == "n":
    print("종료합니다")
    break
  elif start == "y":
    print("다시 시작 합니다.")
    os.system('clear')
  else :
    print("ERROR, y혹은n을 눌러주세요")
    break


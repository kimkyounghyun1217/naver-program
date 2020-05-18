import requests
from bs4 import BeautifulSoup

url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
# 크롤러 아닌척 하기(?)
custom_header = {
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
req = requests.get(url, headers=custom_header)

# 접속이 잘 되엇는가
if req.status_code != requests.codes.ok:
  print("접속실패")
  exit()

# 데이터를 잘 받아왔다 그다음 할것은?
html = BeautifulSoup(req.text, "html.parser")
rank = html.select('.ranking_item .item_title') # 그룹 요소를 찾을때
#html.selectone()  # 특정요소 하나 찾을때
for rank in rank:
  print(rank.text)
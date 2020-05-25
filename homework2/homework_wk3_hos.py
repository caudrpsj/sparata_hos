import requests
from bs4 import BeautifulSoup
# pip install requests
# pip install bs4
# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
#//*[@id="body-content"]/div[4]/div/table/tbody/tr[1]/td[5]/a[1]
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
#//*[@id="body-content"]/div[4]/div/table/tbody/tr[3]/td[2]
musics = soup.select('#body-content > div.newest-list > div > table> tbody>tr.list')
# print(musics)
# movies (tr들) 의 반복문을 돌리기
for music in musics:
    # 노래제목
    a_tag = music.select_one('td.info>a')
    #랭킹 가져오기
    number_tag = music.select_one('td.number')
    number_tag_list = number_tag.text.split()
    number_tag_list_first = number_tag_list[0]
    #가수이름 가져오기
    #//*[@id="body-content"]/div[4]/div/table/tbody/tr[1]/td[5]/a[2]
    name_tag = music.select('td.info>a')
    # print (name_tag[1].text)
    # print (number_tag_list_first)
    if a_tag is not None:
        # a의 text를 찍어본다.
        print (number_tag_list_first,a_tag.text.strip(),name_tag[1].text)
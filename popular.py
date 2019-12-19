import requests
import bs4

html = requests. get('https://www.naver.com/')
soup = bs4.BeautifulSoup(html.text,'html.parser')

keyword = soup.select('span.ah_k')

#print(keyword) 첫번쨰 물어본것
#print(len(keyword))
#keywords = ['a', 'b', 'c'] 근데 우리는 text가지고 있어
#for keyword in keyword:
#    print(keyword.text)
#a
#b
#c
#->>두번 반복되는 걸 확인했어. 

#배열[0:n]->배열의 0번쨰 인댁스부터 n-1번째 인덱스들의 요소를 가져와서 배열로 만든다.
real_keywords = keyword[0:20]
#가공하자 ㄱ
real_real_keywords = [keyword.text for keyword in real_keywords]
#print(real_real_keywords)
#가나다순으로 정렬이 되는 문법, 무엇이1등인지 모름ㄱ
problem = sorted(real_real_keywords)

print('아래의 보기 중에서 1위를 고르세요')
print(problem)
#print(problem)
#사용자에게 입력을 받기 위해 파이선에서 쓰이는 게 있어
#''에 뭘 적으면 저장이 되는 거야 ㄱ
answer = input('당신이 입력한 답')
if answer == real_real_keywords[0]:
#==:같은지 틀린지 묻는 것, 0은 realrealkeyword는 배열인데 배열[0]:배열의 첫번쨰 요소
   print('정답입니다!')
else:
    print('오답입니다!')

#0-19까지 배열되 ㄱ
#for i in range(0,20)
#    print(i)
#예를 들어 [0,1,2,3,4,5,....,100]을 손으로 다 쓰려니까 힘듦. 
#그래서 도입문법은 numbers
#numbers = [i for i in range(0,101)]
#print(numbers)

#좀더 쉬운 방법으로는 
#numbers = []
#for i in range(0,101):
 #   numbers.append(i)
#print(numbers)
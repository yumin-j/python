# 로또 번호를 랜덤으로 뽑아주는 프로그램을 짜고 싶다.
import random

numbers = range(1,46)
# 마치 [1,2,.....,45]과 비슷하다.

#6개의 숫자를 뽑아 출력해주는 프로그램을 작성해주세요.
lotto = random.sample(numbers, 6)
print(sorted(lotto))
#alt+shift+위또는 아래방향키->복사복붙느낌
#alt+위또는 아래->위아래로 움직여
#아래와 같이 하면 중복되어서 나올 수 있어.
#print(random.choice(numbers))
#print(random.choice(numbers))
#print(random.choice(numbers))
#print(random.choice(numbers))
#print(random.choice(numbers))
#print(random.choice(numbers))


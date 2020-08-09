score = input("score:")
score = int(score)
if 81<= score <=100:
    print("grade is A")
elif 61<= score <=80:
    print("grade is B")
elif 41<= score <=60:
    print("grade is C")
elif 21<= score <=40:
    print("grade is D")
else:
    print("grade is E")

data =input("입력:")
tokens =data.split()
amount,currency=tokens
amount =float(amount)

if currency == "달러":
    print(amount * 1167)
elif currency == "엔":
    print(amount * 1.096)
elif currency == "유로":
    print(amount * 1.268)
else:
    print(amount * 171)

num1 =input("number1:")
num2 =input("numver2:")
num3 =input("number3:")
num1=int(num1)
num2=int(num2)
num3=int(num3)


if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

number =input("number:")
comp=number[:3]
if number == "011":
    comp="SKT"
elif number == "016":
    comp = "KT"
elif number == "019":
    comp="LGU"
else:
    comp="NONE"
print(f"당신은 {comp} 사용자입니다.")

#
우편번호 = input("우편번호: ")
우편번호 = 우편번호[2]
if 우편번호 in ["0", "1", "2"]:
    print("강북구")
elif 우편번호 in ["3","4", "5", "6"]:
    print("도봉구")
else:
    print("노원구")

id=input("입력:")
token=id.split("-")
data2= token[1]
if data2[0] == '1 ' or data2[0] =='3':
    print("남자")
if data2[0] == '3 ' or data2[0] =='4':
    print("여자")

id =input("입력:")
back=id.split("-")[1]
if back[1:3] in ['00','01','02','03','04','05','06','07','08']
    print("서울입니다.")
else:
    print("서울이 아닙니다.`")

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")


for 변수  in [10,20,30]:
    print(변수)

for 변수 in [10, 20, 30]:
  print(변수)
  print("-------")

for 변수 in [10, 20, 30]:
  print("+++")
  print(변수)

for 변수 in [1, 2, 3, 4]:
  print("-------")
리스트 = [100, 200, 300]
for 변수 in 리스트:
    print("변수+10")

리스트 = ["김밥", "라면", "튀김"]
for 변수 in 리스트:
    print("오늘의 메뉴:"+변수)


리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 주식 in 리스트:
   print(len(주식))

리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
  print(동물, len(동물))

리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])

리스트 = [1, 2, 3]
for i in 리스트:
    print("3x",i)

리스트 = [1, 2, 3]
for i in 리스트:
    print("3x",i, "=",i*3)

리스트 = ["가", "나", "다", "라"]
나다라 =리스트[1:]
for i in 나다라:
    print(i)

리스트 = ["가", "나", "다", "라"]
가다= 리스트[: :2]
for i in 가다:
    print(i)

리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[: :-1]:
    print(변수)
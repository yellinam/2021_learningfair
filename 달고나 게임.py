print("안녕하세요. 오징어 게임에 오신 것을 환영합니다. 게임을 시작하시겠습니까?")
print('1. 예')
print('2. 아니요.')

number=int(input('번호를 선택하세요.:'))
if number==1:
    print('게임을 시작합니다.')
elif number==2:
    print('과반수 이상이 동의했으므로 게임을 시작합니다.')
    
print("첫 번째 게임은 달고나 게임입니다.")
print("4가지 모양 중 하나를 선택해주세요. 프론트 맨과 같은 모양을 선택한 사람이 첫 단계의 승자가 됩니다.")
print("삼각형, 사각형, 원, 별")
import random

pro = random.choice(["삼각형", "사각형", "원", "별"])
user = input("선택 :")
print("프론트맨 : ", pro)

if user == "삼각형" :
    import turtle as t
    t.shape("turtle")

    #삼각형 그리기
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    
if user == "사각형" :
        import turtle as t
        t.shape("turtle")
        
        #사각형 그리기
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        
if user == "원" :
        import turtle as t
        t.shape("turtle")
        
        t.circle(60)
        
if user == "별" :
        from turtle import *
        up()
        goto(-100,0)
        down()
        for n in range(1,6):
            fd(100)
            left(72)
            fd(100)
            right(144)

    
if user == pro :
        print ("축하합니다. 첫 단계를 통과하였습니다.")
else :
        print("안타깝게도 당신은 게임에서 패배했습니다. 탕.")



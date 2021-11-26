print ('1단계를 통과하신 참가자 여러분 축하합니다. 2단계는 징검다리 게임입니다. 징검다리는 총 4칸으로 왼쪽은 1번 오른쪽은 2번을 눌러 선택하면 됩니다.')

while True :
    import random as r
    c=0
    for i in range(4):
        k=r.randint(1,2)
        a=int(input('방향입력(왼쪽1, 오른쪽2):'))
        if k==a:
            c=c+1
        else:
            break
        
    if c==4:
        print('축하합니다. 당신은 두 번째 게임에서 승리했습니다. 상금 456억을 얻게 되신 걸 축하드립니다.')
    else:
        print('당신은 추락했습니다.')
    

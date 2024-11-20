import random 
ycp = 0
ccp = 0
tie = 0
rounds = int(input("how many rounds do you want :"))
for i in range (rounds):

    print("1.rock")
    print("2.paper")
    print("3.scissors")
    
    yc = int(input("what do you choose"))
    cc = random.randint(1,3)
    
    if yc == 1 and cc == 2:
        ccp = ccp + 1
        print("the computer won the score is :","your score",ycp,"computer score",ccp)
        
    elif yc == 1 and cc == 3:
        ycp = ycp + 1
        print("you won the score is :","your score",ycp,"computer score",ccp)
    
    elif yc == 2 and cc == 1:
        ycp = ycp + 1
        print("you won the score is :","your score",ycp,"computer score",ccp)

    
    elif yc == 2 and cc == 3:
        ccp = ccp + 1
        print("the computer won the score is :","your score",ycp,"computer score",ccp)

    elif yc == 3 and cc == 1:
        ccp = ccp + 1
        print("the computer won the score is :","your score",ycp,"computer score",ccp)

    elif yc == 3 and cc == 2:
        ycp = ycp + 1
        print("you won the score is :","your score",ycp,"computer score",ccp)

    elif yc == cc:
        tie = tie + 1
        print("it is a tie")
if ycp > ccp:
    print ("you won great job")
elif ycp < ccp:
    print("too bad the computer won")
elif ycp == ccp:
    print("it is a tie") 


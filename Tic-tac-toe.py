p1 = " "
p2 = " "
p3 = " "
p4 = " "
p5 = " "
p6 = " "
p7 = " "
p8 = " "
p9 = " "

def board(a, b):

    global p1, p2, p3, p4, p5, p6, p7, p8, p9
    if b == 1:
        if a == 1:
            p1 = "o"
        if a == 2:
            p2 = "o"
        if a == 3:
            p3 = "o"
        if a == 4:
            p4 = "o"
        if a == 5:
            p5 = "o"
        if a == 6:
            p6 = "o"
        if a == 7:
            p7 = "o"
        if a == 8:
            p8 = "o"
        if a == 9:
            p9 = "o"
            
    if b == 2:
        if a == 1:
            p1 = "x"
        if a == 2:
            p2 = "x"
        if a == 3:
            p3 = "x"
        if a == 4:
            p4 = "x"
        if a == 5:
            p5 = "x"
        if a == 6:
            p6 = "x"
        if a == 7:
            p7 = "x"
        if a == 8:
            p8 = "x"
        if a == 9:
            p9 = "x"
    
    print(p1 + p2 + p3 + "\n" + p4 + p5 + p6 +"\n"+ p7 + p8 + p9)

def check():
    if (p1=="o" and p2=="o" and p3=="o")  or (p4=="o" and p5=="o" and p6=="o")  or  (p7=="o" and p8=="o" and p9=="o")  or  (p1=="o" and p4=="o" and p7=="o")  or  (p2=="o" and p5=="o" and p8=="o")  or   (p3=="o" and p6=="o" and p9=="o")  or  (p1=="o" and p5=="o" and p9=="o")  or  (p3=="o" and p5=="o" and p7=="o"):  
           return "user1 win!"
        
    elif (p1=="x" and p2=="x" and p3=="x") or (p4=="x" and p5=="x" and p6=="x")  or (p7=="x" and p8=="x" and p9=="x")  or (p1=="x" and p4=="x" and p7=="x")  or (p2=="x" and p5=="x" and p8=="x")  or (p3=="x" and p6=="x" and p9=="x")  or(p1=="x" and p5=="x" and p9=="x")  or (p3=="x" and p5=="x" and p7=="x"): 
           return "user2 win!"
    elif p1!=" " and p2!=" " and p3!=" " and p4!=" " and p5!=" " and p6!=" " and p7!=" " and p8!=" " and p9!=" ":
           return "Tie"
    else:
        return False
    

    
       
    
        
while True:
    print("User ones turn to input now.")
    n1=eval(input("Select input position 1~9 :"))

    while n1<1 or n1>9 or globals()["p"+str(n1)] != " " :
        print("wrong input ! User ones turn to input now.")
        n1=eval(input("Select input position 1~9 :"))

    board(n1, 1)
    result = check()
    if result != False:
        print(result)
        break

    print("User twos turn to input now.")
    n2=eval(input("Select input position 1~9 :"))

    while n2<1 or n2>9 or globals()["p"+str(n2)] != " " :
        print("wrong input ! User twos turn to input now.")
        n2=eval(input("Select input position 1~9 :"))

    board(n2, 2)
    

    


        

print ("\n\n*****WELCOME TO CUSTOMER PAYMENT MANAGEMENT SYSTEM*****\n")

'''
rt=''
r=0
t=0
p=0
s=0
a=1800
name=''
address=''
cindate=''
coutdate=''
rno=100
'''
def inputdata():
    global rno
    rno+=1
    name=    input("\nEnter your name         : ")
    address= input("\nEnter your address      : ")
    cindate= input("\nEnter your check in date: ")
    coutdate=input("\nEnter your checkout date: ")
    print("Your room no.:",rno,"\n")
    
    
def roomrent():

    print ("We have the following rooms for you:-")

    print ("1.  type A---->rs 6000 PN\-")

    print ("2.  type B---->rs 5000 PN\-")

    print ("3.  type C---->rs 4000 PN\-")

    print ("4.  type D---->rs 3000 PN\-")

    x=int(input("Enter Your Choice Please->"))

    n=int(input("For How Many Nights Did You Stay:"))

    if(x==1):

        print ("you have opted room type A")

        s=6000*n

    elif (x==2):

        print ("you have opted room type B")

        s=5000*n

    elif (x==3):

        print ("you have opted room type C")

        s=4000*n

    elif (x==4):
        print ("you have opted room type D")

        s=3000*n

    else:

        print ("please choose a room")

    print ("your room rent is =",s,"\n")


def restaurentbill():

    print("*****RESTAURANT MENU*****")

    print("1.water----->Rs20","2.tea----->Rs10","3.breakfast combo--->Rs90","4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")

    global r
    while (1):

        c=int(input("Enter your choice:"))


        if (c==1):
            d=int(input("Enter the quantity:"))
            r=r+20*d

        elif (c==2):
             d=int(input("Enter the quantity:"))
             r=r+10*d

        elif (c==3):
             d=int(input("Enter the quantity:"))
             r=r+90*d

        elif (c==4):
             d=int(input("Enter the quantity:"))
             r=r+110*d

        elif (c==5):
             d=int(input("Enter the quantity:"))
             r=r+150*d

        elif (c==6):
            break;
        else:
            print("Invalid option")

    print ("Total food Cost=Rs",r,"\n")


def laundrybill():
    global t
    
    print ("******LAUNDRY MENU*******")

    print ("1.Shorts----->Rs3","2.Trousers----->Rs4","3.Shirt--->Rs5","4.Jeans---->Rs6","5.Girlsuit--->Rs8","6.Exit")

    while (1):
        

        e=int(input("Enter your choice:"))

        if (e==1):
            f=int(input("Enter the quantity:"))
            t=t+3*f

        elif (e==2):
            f=int(input("Enter the quantity:"))
            t=t+4*f

        elif (e==3):
            f=int(input("Enter the quantity:"))
            t=t+5*f

        elif (e==4):
            f=int(input("Enter the quantity:"))
            t=t+6*f

        elif (e==5):
            f=int(input("Enter the quantity:"))
            t=t+8*f
        elif (e==6):
            break;
        else:

            print ("Invalid option")


    print ("Total Laundary Cost=Rs",t,"\n")


def gamebill():
    global p
    
    print ("******GAME MENU*******")

    print ("1.Table tennis----->Rs60","2.Bowling----->Rs80","3.Snooker--->Rs70","4.Video games---->Rs90","5.Pool--->Rs50==6","6.Exit")



    while (1):

        
        g=int(input("Enter your choice:"))


        if (g==1):
            h=int(input("No. of hours:"))
            p=p+60*h

        elif (g==2):
            h=int(input("No. of hours:"))
            p=p+80*h

        elif (g==3):
            h=int(input("No. of hours:"))
            p=p+70*h

        elif (g==4):
            h=int(input("No. of hours:"))
            p=p+90*h

        elif (g==5):
            h=int(input("No. of hours:"))
            p=p+50*h
        elif (g==6):
            break;

        else:

            print ("Invalid option")



    print ("Total Game Bill=Rs",p,"\n")

def display():
    print ("******HOTEL BILL******")
    print ("Customer details:")
    print ("Customer name:",name)
    print ("Customer address:",address)
    print ("Check in date:",cindate)
    print ("Check out date",coutdate)
    print ("Room no.",rno)
    print ("Your Room rent is:",s)
    print ("Your Food bill is:",r)
    print ("Your laundary bill is:",t)
    print ("Your Game bill is:",p)

    rt=s+t+p+r

    print ("Your sub total bill is:",rt)
    print ("Additional Service Charges is",a)
    print ("Your grandtotal bill is:",rt+a,"\n")
    
def main():

   while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate room rent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            inputdata()

        if (b==2):

            roomrent()

        if (b==3):

            restaurentbill()

        if (b==4):

            laundrybill()

        if (b==5):

            gamebill()

        if (b==6):

            display()

        if (b==7):

            quit()

rt=''
r=0
t=0
p=0
s=0
a=1800
name=''
address=''
cindate=''
coutdate=''
rno=100

main()

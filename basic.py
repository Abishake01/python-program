abi="""
 1   =Temp swap 
 2   =Tuple swap 
 3   =Add,Sub,Mul.Three No 
 4   =Canteen Items 
 5   =Armstrong Numbers
 6   =boolen use to find greatest 
 7   =Double n print single line 
 8   =Numbers in same line 
 9   =Int+float 
 10  =len,app,exe,intsert
 11  =Star low to up
 12  =Family earn 
 13  =len to string 
 14  =List Odd and Even Numbers 
 15  =To find types 
 16  =Boolen is find digit or Numbers  
 17  =splite a word in single letter 
 18  =Break Continue 
 19  =List break 
 20  =Multiple a,b 
 21  =list remove,pop 
 22  =Ascending,Dscending 
 23  =Basic sep,end 
 24  =String slice,find 
 25  =Slice find index value
 26  =rstrip,lstrip... 
 27  =Add,sub 
 28  =To find list index 
 29  =To find tuple index 
 30  =Use _*#.. 
 31  =is upper,space 
 32  =College fees 
 33  =list index 
 34  =Leap year 
 35  =Find greatest of 4 Numbers
 36  =check for vote 
 37  =Say Hello in all 
 38  =Engineering Cutoff calculate 
 39  =Medical cutoff calculate 
 40  =Calendar 
 41  =For use Table 
 42  =Loop Odd num,Even num 
 43  =Circulating 
 44  =Def use to add 
 45  =Def area of circle 
 46  =Def leap year 
 47  =Def vote 
 48  =Great of 4 value 
 49  =Type Identify
 50  =About You
"""

print(abi)
single=int(input("Which Programm You Want Enter the Number: "))
#Temprary a and b number change.....
if single==1:
    print("*It is a temp swaping")
    a=int(input("Enter a  number: "))
    b=int(input("Enter b  number: "))
    a=a+b
    b=a-b
    a=a-b
    print("a is",a,",","b is ",b)
#Tupulerf
elif single==2:
    print("*it is a tuple swap")
    a=int(input("Enter a  number: "))
    b=int(input("Enter b  number: "))
    a,b=b,a
    print("swapping a to  b", a)
    print("swapping b to a", b)
#arithmetic 3 number  exchange...
elif single==3:
    print("*add,sub,mul..in three numbers..")
    a=int(input("Enter a 1 number: "))
    b=int(input("Enter a 2 number: "))
    c=int(input("Enter a 3 number: "))
    x=a+b+c
    y=a-b-c
    z=a*b*c
    print("Add a,b,c ",x)
    print("Sub a,b,c ",y)
    print("Mul a,b,c ",z)
    print(a,",",b,",",c)
    
#canadin code.......
elif single==4:
    print("*college canteen....")
#Code for college canteen......

    print("welcome to the Jaya Engineering college Canteen.....")

#Items
    items='''Available Items= [egg_pups/ veg_pups/ juice/ maggi/ veg_rice/ non_veg/ laze/ tea/ biscuits/ ice_cream]'''
    print(items)
    want=(input("Enter you want: "))
    egg_pups=20
    veg_pups=15
    juice=15
    maggi=30
    veg_rice=50
    non_veg=60
    laze=10
    tea=10
    biscuits=15
    ice_cream=10
#Find Rate
    if   want=="egg_pups":
        print("egg pups is" ,egg_pups)
    elif want=="veg_popes":
        print("veg pups is" ,veg_pups)
    elif want=="juice":
        print("juice is" ,juice)
    elif want=="maggi":
        print("maggi is" ,maggi)
    elif want=="veg_rice":
        print("veg rice is" ,veg_rice)
    elif want=="non_veg_rice":
        print("non_veg_rice is" ,non_veg)
    elif want=="laze":
        print("laze is" ,laze)
    elif want=="tea":
        print("tea is" ,tea)
    elif want=="biskcuts":
        print("Biscuits is" ,biscuits)
    elif want=="ice_cream":
        print("Ice cream is",ice_cream)
    else:
    	print("SORRY this  items are not available in this canteen....")
#To find armstrong number.....
elif single==5:
    print("*armstrong number...1634,")
    n=int(input("Enter a value: "))
    s=n
    b=len(str(n))
    sum=0
    while n!=0:
        r=n%10
        sum=sum+(r**b)
        n=n//10
    if s==sum:
        print("The given number", s ,"is armstrong numbber")
    else :
        print("The given number", s ,"is not armstrong  number")

elif single==6:
    print("*greatest value two num...it will print true or false...")
    a=int(input("Enter A Number: "))
    b=int(input("Enter B Number: "))
    print(a>b)
    print(a==b)
    print(a<b)

elif single==7:
    print("*In two line code in same line...")
#same line code....
    a="code"
    b="io"
    print(a,'.',sep='',end='')
    print(b)

#from stringprep import in_table_c5
elif single==8:
    print("*all number in one line....")

    a=int(input("Enter a number: "))
    for i in range(a):
        print(i,end='')
        
elif single==9:
    print("*integer+float....")
#int + float
    a=int(input("Enter a Number: "))
    b=float(input("Enter a Number: "))
    print(a+b)

elif single==10:
    print("*max,len,min,append,insert,extend")
    lst=[1,3,4,5]
    print(max(lst))
    print(len(lst))
    print(min(lst))
    lst.append(6)
    print(lst)
    lst.insert(1,2)
    print(lst)
    lst.extend([7,8,9])
    print(lst)
    
elif single==11:
    print("*Star Lower to Upper...")
#Birthday
#HAPPY BIRTHDAY 
    row=int(input("Enter a row: "))
    for i in range(row):
        print(("*"*(row-i)))
    	
#family earn 
elif single==12:
    print("*How much a family earn...")
    dad=int(input("Enter father salary: "))
    mom=int(input("Enter mother salary: "))
    son=int(input("Enter son salary: "))
    daughter=int(input("Enter daughter salary: "))
    total=dad+mom+son+daughter
    emi=32000
    earn=total-emi
    print("The family earn per month",earn)
    
elif single==13:
    print("....")

    x=len('hello world!')
    y=len(str(x))
    z=y^0
    print(z)
elif single==14:
    print("*odd and Even number print...")
#range short...

    a=int(input("Enter a number: "))
    b=[i for i in range(1,a+1,2)]
    c=[j for j in range(2,a+1,2)]
    print(b)
    print(c)
    
elif single==15:
    print("*identify the types...")
    a=10
    print(type(a))
    b=1.3
    print(type(b))
    c="any one"
    print(type(c))

elif single==16:
    print(" *boolen is functions...to find the numbers and variables..")
    str="hi hello welcome you all"
    string="12345"
    print(str.isdigit())
    print(str.isalnum())
    print(str.isspace())
    print(string.isdigit())
    print(string.isalnum())
    print(string.isspace())
    stri="hel lo"
    i=stri.isupper() and stri.isspace()
    j=stri[0:3].isupper() or stri.isspace()
    print(int(i)+ int(j)+5)

elif single==17:
    print("*splite a single letter in list")
    lst=list('Hi Everyone')
    print(lst)
    
elif single==18:
    print("*continue and break...")
#loop break concept...

    for i in range(0,10):
        if i==3:
           continue
        if i==9:
            break
        print(i)
    print("hello""world")

#break...com
elif single==19:
    print("*list break...")
    lst=[10,20,30,40,60]
    for i in lst:

        if i==30:
           break
        else:
           print(i)
           
elif single==20:
    print("*multiple maths...")
#multiple the a*b .....
    a=int(input("Enter a Number: "))
    b=int(input("Enter b Number: "))
#a=6,b=6
    print(a*b)

#insert....
elif single==21:
    print("*insert,append,remove,pop..list...")

    ls=[1,2,3,4]
    ls.insert(1,4)
    print(ls)
#pop...

    lst=[1,2,3]
    lst.append([4,5,6])
    print(lst)
    lst.remove(2)
    print(lst)
    element=lst.pop(1)
    #it is remove the index of the number
    print(lst)
    print(element)

elif single==22:
    print("*acending,decending...")

#reverse....

    lst=[1,3,2,4]
    lst.sort()
    print(lst)
#decending order
    lst.sort(reverse=True)
    print(lst)
    
elif single==23:
    print("*sep,end,start basic...")
#basic....
    print('hello','world',sep='_')
    print('hello','world',sep='_',end='\t')
    print('troll geek')

elif single==24:
    print("*string slice,find,sub...")
#string slice....

    str="hi hello welcome you all"
    sub='all'
    print(str)
    print(len(str))
    print(str.find(sub))
    print(str.find(sub,10,24))#is a range....you give an range of the index then they search
    s='abc'
    print(str.find(s)) 
    
elif single==25:
    print("*slice...identify the index")
#slice......

    a='troll geek'
    print(a[0])
    print(a[0:5])
    print(a[:])
    print(a[0:])
    print(a[:10])
    print(a[0:10:2])
    print(a[10:0:-2])
    
elif single==26:
    print("*string slice...")
#string split....
#sting split is a seprate a word in  the string........
    str=("hello world welcome to you")
    lst=str.split()
    print(lst)
#rstrip is right side remove
    print(str.strip())
    print(str.rstrip('uo'))
#lstrip is left side remove
    print(str.lstrip('he'))
    
elif single==27:
    print("*sub,add...")
#sub...
#subract the a-b....

    a=int(input("Enter a Number: "))
    b=int(input("Enter b Number: "))
#a=8,b=5

    print(a-b)
    print(a+b)

#result is 3...
elif single==28:
    print("*transe,list index...")

    lst=[10,30,40,60]
    print((10*3) in lst)
    print(lst[-1] ,lst[1])

elif single==29:
    print("*tuple index value...")
#tuple

#tuple is a inmutable...
    tup=([1,2,3])
    tup1=tuple('Hi Everyone')
    print(tup[0])
    print(len(tup))
    print(tup1)
#youtube...
elif single==30:
    print("*simbol use")

    text='EPIC'
    print(text)
    print(f'{text:#<20}')
    print(f'{text:_>20}')
    print(f'{text:.^20}')
elif single==31:
    print("*is upper,space...")
    
    str="HEL LO"
    i=str.isupper() and str.isspace()
    j=str[0:3].isupper() or str.isspace()
    print(int(i)+ int(j)+5)

elif single==32:
    print("*fun college fees...")
#college fees...

    print("Welcome To The Jaya Engineerring College")
    course=input("Enter the Department:  ")
    cse=50000
    it=45000
    ece=35000
    eee=38000
    mech=28000
    civil=25000
    aero=37000
    if course=="cse":
        print(f"your fees is {cse}")
    elif course=="it":
        print(f"your fees is {it}")
    elif course=="ece":
        print(f"your fees is {eee}")
    elif course=="ece":
        print(f"your fees is {ece}")
    elif course=="mech":
        print(f"your fees is {mech}")
    elif course=="civil":
       print(f"your fees is {civil}")
    elif course=="aero":
        print(f"ypur fees is {aero}")
    else:
        print("you choose wronge department.....")
elif single==33:
    print("*It is list index value")
#list

    lst=[1,2,3,4]
    print(lst[2])
    print(lst[0])
    print(lst[3])
    
#leap calculater
elif single==34:
    print("*leap year...")
#leap year
    year=int(input("Enter the year: "))
    if year%4==0:
        print("It is a Leap year...")
    else:
        print("It is Not a Leap year")
#find the great of four number...
elif single==35:
    print("greatest number of four value...")
    
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=int(input("Enter c number: "))
    d=int(input("Enter d number: "))
    if a>b and a>c and a>d:
        print("a is greater...")
    elif b>a and b>c and b>d:
        print("b id greater...")
    elif c>a and c>b and c>d:
        print("c is greater...")
    else:
        print("d is greater...")
#voteing...      
elif single==36:
    print("*check you eligible to vote...")
    
    age=int(input("Enter your age: "))
    if age>18:
        print("Eligible to voting...")
    elif age==18:
        print("Apply for voting...")
    else:
        print("Not Eligible to voting...")
        
#tell hii in all
elif single==37:
    print("*loop of say hello")
    
    name=["Nagi","Vairamuthu","Mohan","Thiru Murugan","It's me"]
    for i in range(len(name)):
        print("Hello",name[i],"bro!")
#loop
elif single==38:
    print("*Cutoff calulate Engineering...")
#cuttoff mark find...

    m=int(input("Enter Maths Mark: "))
    p=int(input("Enter Physics Mark: "))
    c=int(input("Enter Chemistry Mark: "))
    total=(m+p/2+c/2)

    print("ypur Cutoff Mark is ",total)

elif single==39:
    print("*Medical Cutoff calculate...")

    b=int(input("Enter Biology Mark: "))
    p=int(input("Enter Physics Mark: "))
    c=int(input("Enter Chemistry Mark: "))
    total=(b+p/2+c/2)

    print("ypur Cutoff Mark is ",total)

elif single==40:
    print("*calendar check...")
#calendar...
    import calendar
    year=int(input("Enter a year: "))
    month=int(input("Enter a month: "))
    print(calendar.month(year,month))    

elif single==41:
    print("*For loop table...")
#while table...
    a=int(input("Enter a Table: "))
    b=int(input("Enter a Size: "))
    for i in range(1,b+1):
        print(a,"X",i,"=",a*i)

elif single==42:
    print("*odd num,even num...")
#odd number and even number...
    for i in range(0,100):
        if (i%2==0):
            print(i+1,end='\t')
            
            print(i+2)
elif single==43:
    print("circulating the value end...")

#circulate ....give minmum 10..It is cirulate what are you give the value...

    number_of_terms=int(input("Enter the Number of values: "))
    list1=[]
    for val in range (0,number_of_terms,1):
       ele=int(input("Enter integer: "))
       list1.append(ele)
       print("circulating the element off list", list1)
    for val in range (0,number_of_terms,1):
       ele=list1.pop(0)
       list1.append(ele)
       print(list1)
#def function...
elif single==44:
    print("*def function...")

    def call_me():
        a=int(input("Enter the number: "))
        b=int(input("Enter the number: "))
        result=a+b
        return(result)
    print(call_me())

elif single==45:
    print("*area of circle")
#area of the circle...
    def area():
        r=int(input("Enter radius number: "))
        circle=3.14*r*r
        return('The area of the circle',int(circle))
    print(area())

elif single==46:
    print("*leap year...")
#leap year...
    def year():
        y=int(input("Enter a year: "))
        if y%4==0:
           
           return("leap year")
        else:
            return("not a leap year")
    print(year())

elif single==47:
    print("*voting...")
#voteing
    def vote():
        vote=int(input("Enter your age: "))
        if vote>18:
           return("Eligible to voting...")
        elif vote==18:
           return("Apply for voting...")
        else:
            return("Not Eligible to voting...")
    print(vote())

#greateat value of 4 no
elif single==48:
    print("great of 4 number")

    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=int(input("Enter c number: "))
    d=int(input("Enter d number: "))

    if a>b and a>c and a>d:
        print("A is greatest")
    elif b>a and b>c and b>d:
        print("B is greatest")
    elif c>a and c>b and c>d:
        print("C is greatest")
    else:
        print("D is greatest")
elif single==49:
    print("Type identify")
    no=89
    bye="Hello"
    point=54.6
    print(type(no),no)
    print(type(bye),bye)
    print(type(point),point)

elif single==50:
    print("About You")
    name=input("Enter your Name: ")
    age=int(input("Enter Your Age: "))
    study=input("Enter your Department: ")
    college=input("Enter your College Name: ")
    print("Your Name: ",name)
    print("Your Age: ",age)
    print("You are studying: ",study)
    print("Your College: ",college)
    
    

else: print("SORRY,You Enter the wrong number,PLEASE ENTER CORRECT NUMBER...")


                                    #500 line codeing.....


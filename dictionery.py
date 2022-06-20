import os


myfamily={
    1:{"id":"1","fname":"eitan","lname":"cohen","phone":"1111111"},
    2:{"id":"2","fname":"hadas","lname":"cohen","phone":"2222222"},
    3:{"id":"3","fname":"shaked","lname":"cohen","phone":"3333333"},
    4:{"id":"4","fname":"uri","lname":"benyamin","phone":"4444444"},
    5:{"id":"5","fname":"tamar","lname":"benyamin","phone":"5555555"},
    6:{"id":"6","fname":"hagit","lname":"edri","phone":"6666666"},
    7:{"id":"7","fname":"haim","lname":"falak","phone":"7777777"},
    8:{"id":"8","fname":"barak","lname":"cohen","phone":"8888888"},
    9:{"id":"9","fname":"eitan","lname":"israel","phone":"9999999"},
    10:{"id":"10","fname":"hadas","lname":"benyamin","phone":"1111110"},
    11:{"id":"11","fname":"barak","lname":"benyamin","phone":"1111101"},
    
}

def func1(key,value):
    try:
        for y, x in myfamily.items():
            if myfamily[y][key]==value:
                print(myfamily[y]["fname"],myfamily[y]["lname"],myfamily[y]["phone"])
        x=input("press Enter for another search")
        os.system('cls') #change to 'clear' if you using linux os
    except:
        print("key or value not correct, please try again")
        

i=0

while i<10:
    
    key= input("Type in which key you would like to find or press 0 to exit: ")
    if key=="0" or key=="exit" or key=="out":
        break
    value= input("Enter a " + key + " for search: ")

    if key== "last name" or key == "family":
        key="lname"
    if key== "first name" or key == "name":
        key="fname"
    
    
    func1(key,value)
    
    
    
    
 

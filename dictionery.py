myfamily={
    1:{"id":"1","fname":"eitan","lname":"cohen","phone":"1111111"},
    2:{"id":"2","fname":"hadas","lname":"cohen","phone":"2222222"},
    3:{"id":"3","fname":"shaked","lname":"cohen","phone":"3333333"},
    4:{"id":"4","fname":"uri","lname":"benyamin","phone":"4444444"},
    5:{"id":"5","fname":"tamar","lname":"benyamin","phone":"5555555"},
    6:{"id":"6","fname":"hagit","lname":"edri","phone":"6666666"},
    7:{"id":"7","fname":"haim","lname":"falak","phone":"7777777"},
    8:{"id":"8","fname":"barak","lname":"cohen","phone":"8888888"},
}

def func1(kay,value):
    
    for y, x in myfamily.items():
        if myfamily[y][kay]==value:
            print(myfamily[y]["fname"],myfamily[y]["lname"],myfamily[y]["phone"])


i=0

while i<10:
    kay= input("Enter a kay for search: ")
    if kay=="0" or kay=="exit":
        break
    value= input("Enter a " + kay + " for search: ")

    if kay== "last name":
        kay="lname"
    if kay== "first name":
        kay="fname"
    
    
    func1(kay,value)
    
    
    
    
    
 
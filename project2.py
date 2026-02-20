print("welcome to medical shop")
import pyodbc as sql
con=sql.connect(driver='SQL Server',server='DESKTOP-EQGK6VQ\\SQLEXPRESS',database='project2',user='sa',password='abc')
cur=con.cursor()
d2={}
ch = int(input("Enter 1 to add medicine, 2 to check stock, 3 to buy medicine: "))
while ch==1:
    mid=int(input("enter the mid: "))
    mname=input("enter the mname: ")
    pcost=eval(input("enter the pcost"))
    scost=eval(input("enter the scost"))
    aval=int(input("enter the aval: "))
    q1 = "select * from medicine"
    cur.execute(q1)
    res = cur.fetchall()
    print(res)
    for i in res:
        if mid==i[0]:
            stored=i[4]
            
            stack=stored+aval


            q="update medicine set availability=?,pcost=?,scost=? where mid=?"
            t=(stack,pcost,scost,mid)
            cur.execute(q, t)
            con.commit()
            print("updated")
            break
    else:
        print("no value")
        q1 = "insert into medicine values(?,?,?,?,?)"
        t1 = (mid, mname, pcost, scost, aval)
        cur.execute(q1, t1)
        con.commit()
        print("value inserted")
    ch = int(input("If you want to continue adding medicine, press 1: "))

while ch==2:
    q1 = "select * from medicine where availability <=5"
    cur.execute(q1)
    res = cur.fetchall()
    print(res)
    # for i in res:
    #     print(i[1])
    ch = int(input("If you want to continue, press 2: "))

while ch==3:
    c='y'
    while c=='y':
        q8="select * from medicine"
        cur.execute(q8)

        r=cur.fetchall()
        for i in r:
            print(i)
        mid=input("enter the medicine ID: ")

        q1 = "select * from medicine where mid=?"
        t1=(mid)
        cur.execute(q1,t1)
        res = cur.fetchall()
        print(res)
        cname=res[0][1]
        pcost=res[0][2]
        amt=res[0][3]
        print(amt)
        available=res[0][4]
        qun = int(input("enter the quantity :"))
        if available >=qun:

            print("selling cost is :",amt)
            bill=qun*amt
            print(bill)
            profit=(amt-pcost)*qun
            bal_qun = available - qun
            d2[mid]=[qun,amt,bill,profit,bal_qun,cname]

        else:
            print("stack not that much avalible")
        print(d2)
        c=input("if you want to continue press Y or N ")
    ch = int(input("if you want to continue print press 4 or 0 : "))
while ch==4:
    print("total amount")
    # orderid=int(input("enter the orderid"))
    customername=input("enter the customer name: ")
    phon=int(input("enter customer phone number: "))
    q3="insert into customer(customername,phon) values(?,?)"
    t3 = (customername,phon)
    cur.execute(q3, t3)
    con.commit()
    q8="select top 1 * from customer order by orderid desc "
    cur.execute(q8,)
    res1 = cur.fetchall()
    orderid=res1[0][0]
    print(orderid)


    print("customer table inserted")
    # d2={'do': [50,25.0000,1250.0000,250.0000, 15], 'dolo': [4,12.0000,48.0000,8.0000, 1]}
    #d2={'dolo': [2, Decimal('25.0000'), Decimal('50.0000'), Decimal('10.0000'), 3]}
    #d2={'7': [2, Decimal('60.0000'), Decimal('120.0000'), Decimal('20.0000'), 108]}
    tot=0
    pro=0
    for i in d2:
        
        mid=i
        print(mid)
        q=d2[i][0]
        cost=d2[i][1]
        tot=tot+d2[i][2]
        bill=d2[i][2]
        pro=pro+d2[i][3]
        stack=d2[i][4]
        mname=d2[i][5]
        print(stack)

        q4="insert into orders(orderid,mname,pcost,quantity,bill) values(?,?,?,?,?)"
        t4=(orderid,mname,cost,q,bill)
        cur.execute(q4,t4)
        con.commit()
        q6 = "update medicine set availability=? where mid=? "
        t6=(stack,mid)
        cur.execute(q6, t6)
        con.commit()
        print("value inserted")
    print(tot)

    q7="insert into profit values(?,?,getdate())"
    t7=(orderid,pro)
    cur.execute(q7,t7)
    con.commit()
    q5="update customer set totalbill=? where orderid=?"
    t5=(tot,orderid)

    cur.execute(q5,t5)
    con.commit()
    ch = int(input("Enter 5 to close: "))

con.close()
print("connection closed")
print(d2)
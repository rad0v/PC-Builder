import mysql.connector as sq
import uuid
import random

p=input("Enter your password to access database: ")
mycon = sq.connect(host='localhost',user='root', passwd=p)
if mycon.is_connected:
    print("Connected Successfully")

cur=mycon.cursor(buffered=True)
cur.execute("create database if not exists comp_project")
cur.execute("use comp_project")

#User database
print(" Creating user_accounts table")
sql="create table if not exists user_accounts(fname varchar(100),\
lname varchar(100),user_name varchar(100) ,\
password varchar(100) primary key, phno varchar(15),\
gender varchar(50),dob varchar(50),age varchar(4))"
cur.execute(sql)
print(" user_accounts Table created")

#Order database
print(" Creating orders table")
sql="create table if not exists orders(order_id int,\
phno int primary key,cpu varchar(255),gpu varchar(255), \
mobo varchar(255),storage varchar(255),ram varchar(255),cabinet varchar(255))"
cur.execute(sql)
print(" Orders database created")

l="""LOGGING IN...
→→→ [■□□□□□□□□□] 10%
→→→ [■■□□□□□□□□] 20%
→→→ [■■■□□□□□□□] 30%
→→→ [■■■■□□□□□□] 40%
→→→ [■■■■■□□□□□] 50%
→→→ [■■■■■■□□□□] 60%
→→→ [■■■■■■■□□□] 70%D
→→→ [■■■■■■■■□□] 80%
→→→ [■■■■■■■■■□] 90%"""
print(l)

print("\n****************************************************************")
print(r"""██████╗░░█████╗░  ███████╗░█████╗░██████╗░  ██╗░░░██╗░█████╗░██╗░░░██╗
██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗  ╚██╗░██╔╝██╔══██╗██║░░░██║
██████╔╝██║░░╚═╝  █████╗░░██║░░██║██████╔╝  ░╚████╔╝░██║░░██║██║░░░██║
██╔═══╝░██║░░██╗  ██╔══╝░░██║░░██║██╔══██╗  ░░╚██╔╝░░██║░░██║██║░░░██║
██║░░░░░╚█████╔╝  ██║░░░░░╚█████╔╝██║░░██║  ░░░██║░░░╚█████╔╝╚██████╔╝
╚═╝░░░░░░╚════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░""")
print("\n****************************************************************")  

def menu():
    con=True
    while con==True:
        li='-'
        print("",li*100,"")
        h1="WELCOME TO THE CUSTOM PC BUILDING PROGRAM"
        H1=h1.center(110)
        print(H1)
        print("",li*100,"")
        print("")
        h2="╔════════════════════════════╗"
        H2=h2.center(110)
        h7="║ Select the desired option: ║"
        H7=h7.center(110)
        h3="╠════════════════════════════╣"
        H3=h3.center(110)
        h4="║ 1. LOGIN                   ║"
        H4=h4.center(110)
        h5="║ 2. REGISTER                ║"
        H5=h5.center(110)
        h6="║ 3. DELETE YOUR ACCOUNT     ║"
        H6=h6.center(110)
        h8="║ 4. EXIT                    ║"
        H8=h8.center(110)
        h9="╚════════════════════════════╝"
        H9=h9.center(110)
        print(H2)
        print(H7)
        print(H3)
        print(H4)
        print(H5)
        print(H6)
        print(H8)
        print(H9)
        ch1=int(input("Enter your choice: "))
#
        if ch1==1:
            a=sign_in()
            if a==True:
                main()
            else:
                continue
#
        elif ch1==2:
            a=sign_up()
            if a==True:
                main()
            else:
                print('PLEASE LOGIN NOW!')

                continue
#            
        elif ch1==3:
            c=delete()
            if c==True:
                print('ACCOUNT DELETED') 
                continue           
            else:
                print('YOUR PASSWAORD OR USER_NAME IS INCORRECT')
            
                continue
#
        elif ch1==4:
            print('THANK YOU')

            break
#        
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break
##        
def sign_in():
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cur.execute(c1)
        data1=cur.fetchall()[0]
        
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cur.execute(s1)
        data=cur.fetchall()[0]
        data=list(data)[0]
        if data==a:
            print(' Welcome ',data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
##
def main():        
    c=True
    while c==True:
        f1="╔════════════════════════════╗"
        f2="║ Select the desired option: ║"
        f3="╠════════════════════════════╣"
        f4="║ 1.CUSTOM RIG               ║"
        f5="║ 2.ORDER TRACKING           ║"
        f6="║ 3.ORDER CANCELLING         ║"
        f7="║ 4.ACCOUNT DETAILS          ║"
        f8="║ 5.LOG OUT                  ║"
        f9="╚════════════════════════════╝"
        F1=f1.center(110)
        F2=f2.center(110)
        F3=f3.center(110)
        F4=f4.center(110)
        F5=f5.center(110)
        F6=f6.center(110)
        F7=f7.center(110)
        F8=f8.center(110)
        F9=f9.center(110)
        print(F1)
        print(F2)
        print(F3)
        print(F4)
        print(F5)
        print(F6)
        print(F7)
        print(F8)
        print(F9)
        ch=int(input('enter ur choice:'))
        if ch==1:
            custom_rig()
        elif ch==2:
            order_tracking()
        elif ch==3:
            order_cancelling()
        elif ch==4:
            account_details()        
        elif ch==5:
            print('THANK YOU')
            c=False
        break
    else:
        print('ERROR 404: ERROR PAGE NOT FOUND')
##
def custom_rig():
    mycon.autocommit=True
    cur.execute("use products")
    order_id=uuid.uuid4()
    var=True
    if var==True:

        print("Please select your hardware")
    #Selecting CPU
        li="*"
        print("",li*100,"")
        print("CPU:")
        print("1. INTEL CORE I3 10100f-₹7000")
        print("2. INTEL CORE I3-12100F-₹9,970 / *BEST SELLER */")
        print("3. INTEL CORE I5-11400F-₹13000")
        print("4. INTEL CORE i5 12400F-₹16,800")
        print("5. INTEL CORE i7-12700K-₹41,339")
        print("6. INTEL CORE i9-12900K-₹49,500 /*CHOICE OF BEAST*/")
        print("7. AMD Ryzen 3 3600-₹9,999")
        print("8. AMD Ryzen 5 5600X-₹16,298")
        print("9. AMD Ryzen 7 3700X-₹23,999")
        print("10. AMD Ryzen 7 3800XT-₹24,999")
        print("11. AMD Ryzen 7 5800X-₹28,790 / *HOT SELLLER*")
        print("12. AMD Ryzen 9 5900X-₹35,900 ")
        print("13. AMD Ryzen 9 5950X-₹49,999")
        print("14. AMD Ryzen Threadripper 3990X-₹2,16,000 /* GOD SIP *" )
        print("",li*100,"")
        cpu = int(input("Enter the CPU that you want: "))
        if cpu==1:
            q=("select product_name from product where sno=23")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==2:
            q=("select product_name from product where sno=24")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==3:
            q=("select product_name from product where sno=25")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==4:
            q=("select product_name from product where sno=26")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==5:
            q=("select product_name from product where sno=27")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==6:
            q=("select product_name from product where sno=28")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==7:
            q=("select product_name from product where sno=29")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==8:
            q=("select product_name from product where sno=30")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==9:
            q=("select product_name from product where sno=31")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==10:
            q=("select product_name from product where sno=32")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==11:
            q=("select product_name from product where sno=33")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==12:
            q=("select product_name from product where sno=34")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==13:
            q=("select product_name from product where sno=35")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
        elif cpu==14:
            q=("select product_name from product where sno=36")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cpu=res
    
    #Selecting Cabinet
        li="*"
        print("",li*100,"")
        print("Choose your OP cabinets- ")
        print("1. Ant Esports ICE-130AG-₹2,178")
        print("2. Ant Esports ICE-120AG-₹2,789")
        print("3. CHIPTRONEX GX3000 RGB-₹3,799")
        print("4. Ant Esports ICE-200TG-₹3,619")
        print("5. Cooler Master MasterBox K501L-4,799")
        print("6. Antec Torque Mid Tower-₹31,075")
        print("",li*100,"")
        cabi = int(input("copy ur cabinet here: "))
        if cabi==1:
            q=("select product_name from product where sno=1")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cabi=res
        elif cabi==2:
            q=("select product_name from product where sno=2")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cabi=res
        elif cabi==3:
            q=("select product_name from product where sno=3")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cabi=res
        elif cabi==4:
            q=("select product_name from product where sno=4")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cabi=res
        elif cabi==5:
            q=("select product_name from product where sno=5")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cabi=res
        elif cabi==6:
            q=("select product_name from product where sno=6")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            cabi=res
        else:
            print("ERROR")
            custom_rig()

    #Selecting Graphic Card
        print("",li*100,"")
        print("BEST GPU BRANDS :")
        print("1.MSI NVIDIA N730K-4GD3 4 GB DDR3-₹6,099 ")
        print("2.MSI AMD Radeon RX 6500 XT MECH 2X 4G OC 4 GB GDDR6-₹21,999")
        print("3.MSI NVIDIA GeForce RTX 3050 GAMING X 8G 8 GB GDDR6-₹32,999/* BEST SELLER*/")
        print("4.MSI NVIDIA RTX 3060 Ti 8 GB GDDR6-₹37,499")
        print("5.MSI NVIDIA GeForce RTX 3080 VENTUS 3X PLUS-₹78,499")
        print("6.MSI NVIDIA RTX 3090 Ti GAMING X TRIO 24G 24 GB GDgpuDR6X-₹2,13,956/* Those Who Dare*/")

        print("7.PowerColor AMD Radeon RX 6400 ITX 4GB GDDR6-₹14,990.00")
        print("8.PowerColor AMD Radeon RX 6400 Low Profile 4GB GDDR6-₹16,390")
        print("9.PowerColor Fighter AMD Radeon RX 6600 8GB GDDR6- ₹29,000")
        print("10.PowerColor Hellhound AMD Radeon RX 6600 8GB GDDR6-₹31,970 /#sweetchilli/")
        print("11.PowerColor Hellhound AMD Radeon RX 6600 XT OC 8GB GDDR6-₹39,290")
        print("12.PowerColor Fighter AMD Radeon RX 6700 XT 12GB GDDR6-₹44,610")

        print("13.ZOTAC NVIDIA GeForce GT 1030 2 GB DDR5-₹8,480")
        print("14.ZOTAC NVIDIA GeForce GTX 1650 OC 4 GB GDDR6-₹16,999")
        print("15.ZOTAC NVIDIA RTX 2060 Twin Fan 12 GB GDDR6-₹22,499")
        print("16.ZOTAC NVIDIA RTX 3060 Twin Edge 12 GB GDDR6-₹33,499/* DEAL OF DECADE*/")
        print("17.ZOTAC NVIDIA GAMING GeForce RTX 4090 Trinity OC 24GB GDDR6X-₹1,67,999 /* BEST BUDGET 4090*/")

        print("18.ASUS NVIDIA GT730 2 GB GDDR5-₹5,800")
        print("19.ASUS AMD/ATI Dual RX 6500XT OC 4 GB GDDR6-₹17,499")
        print("20.ASUS NVIDIA GeForce GTX 1050Ti 4GB OC Edition GDDR5-₹21,999")
        print("21.ASUS NVIDIA 1660s 6 GB GDDR6-₹55,000")
        print("22.ASUS NVIDIA DUAL-RTX3060-O12G 12 GB GDDR6-₹85,000")

        print("23.GIGABYTE NVIDIA NVIDIA GeForce GT 730 2 GB DDR3-₹5,400")
        print("24.GIGABYTE NVIDIA GV-N1650OC-4GD 4 GB GDDR5-₹17,299")
        print("25.GIGABYTE AMD/ATI GV-R65XTEAGLE-4gD 4 GB GDDR6-₹23,969")
        print("26.GIGABYTE NVIDIA GV-N3060WF2OC-12GD 12 GB GDDR6-₹33,099")
        print("27.GIGABYTE AMD/ATI GV-R66EAGLE-8GD 8 GB GDDR6-₹42,215")
        print("28.GIGBAYTE AMD/ATI GV-R66XTEAGLE-8GD 8 GB GDDR6-₹49,347")
        print("",li*100,"")
        GD = int(input("Copy card name here: "))
        if GD==1:
            q=("select product_name from product where sno=37")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==2:
            q=("select product_name from product where sno=38")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==3:
            q=("select product_name from product where sno=39")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==4:
            q=("select product_name from product where sno=40")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==5:
            q=("select product_name from product where sno=41")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==6:
            q=("select product_name from product where sno=42")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==7:
            q=("select product_name from product where sno=43")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==8:
            q=("select product_name from product where sno=44")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==9:
            q=("select product_name from product where sno=45")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==10:
            q=("select product_name from product where sno=46")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==11:
            q=("select product_name from product where sno=47")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==12:
            q=("select product_name from product where sno=48")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==13:
            q=("select product_name from products where sno=49")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==14:
            q=("select product_name from product where sno=50")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==15:
            q=("select product_name from product where sno=51")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==16:
            q=("select product_name from product where sno=52")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==17:
            q=("select product_name from product where sno=53")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==18:
            q=("select product_name from product where sno=54")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==19:
            q=("select product_name from product where sno=55")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==20:
            q=("select product_name from product where sno=56")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==21:
            q=("select product_name from product where sno=57")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==22:
            q=("select product_name from product where sno=58")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==23:
            q=("select product_name from product where sno=59")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==24:
            q=("select product_name from product where sno=60")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==25:
            q=("select product_name from product where sno=61")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==26:
            q=("select product_name from product where sno=62")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==27:
            q=("select product_name from product where sno=63")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        elif GD==28:
            q=("select product_name from product where sno=64")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            GD=res
        else:
            print("ERROR")
            custom_rig()

    #Selecting Motherboard
        print("",li*100,"")    
        print("Motherboard:")
        print("1. ASUS Prime H510M-E-₹6,469")
        print("2. MSI MAG B460 Tomahawk-₹16,030 ")
        print("3. ASUS TUF DDR4 Gaming Z590-Plus-₹23,375")
        print("4. Gigabyte B450 AORUS ELITE-₹10,319")
        print("5. ASUS ROG Strix B550-F Gaming-₹20,990")
        print("6. ASUS TUF Gaming B650-PLUS-₹23,599")
        print("",li*100,"")
        mobo = int(input("Enter the Mother Board that you want: "))
        if mobo==1:
            q=("select product_name from product where sno=7")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            mobo=res
        elif mobo==2:
            q=("select product_name from product where sno=8")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            mobo=res
        elif mobo==3:
            q=("select product_name from product where sno=9")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            mobo=res
        elif mobo==4:
            q=("select product_name from product where sno=12")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            mobo=res
        elif mobo==5:
            q=("select product_name from product where sno=10")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            mobo=res
        elif mobo==6:
            q=("select product_name from product where sno=11")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            mobo=res
        else:
            print("ERROR")
            custom_rig()

    #Selecting Storage
        print("",li*100,"")
        print("Storage:")
        print("1. Samsung 870 EVO 500GB-₹4,300 ")
        print("2. Samsung 980 1TB-₹7,999")
        print("3. Kingston Q500 240GB-₹1,749 ")
        print("4. Seagate One Touch 2TB External HDD-₹5,299")
        print("5. Crucial MX500 500GB-₹3,664")
        print("6. XPG S40G 512GB RGB 3D NAND PCIe GEN2X4 NVMe1.3- ₹4,375")
        print("",li*100,"")
        storage = int(input("Enter the SSD or HDD that you want: "))
        if storage==1:
            q=("select product_name from product where sno=12")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            storage=res
        elif storage==2:
            q=("select product_name from product where sno=13")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            storage=res
        elif storage==3:
            q=("select product_name from product where sno=14")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            storage=res
        elif storage==4:
            q=("select product_name from product where sno=15")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            storage=res
        elif storage==5:
            q=("select product_name from product where sno=16")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            storage=res
        elif storage==6:
            q=("select product_name from product where sno=17")
            cur.execute(q)
            res=cur.fetchone()[0]
            storage=res
        else:
            print("ERROR")
            custom_rig()
        
    #Selecting Ram
        print("",li*100,"")
        print("RAM:")
        print("1. Corsair Vengeance LPX 8GB-₹2,499")
        print("2. Corsair Vengeance LPX 16GB-₹4,570")
        print("3. XPG ADATA GAMMIX D30 DDR4 8GB-₹2,199")
        print("4. XPG ADATA GAMMIX D30 DDR4 16GB-₹4,179")
        print("5. G.SKILL Trident Z Neo 32GB (2x16GB) DDR4 3600MHz-₹12,990")
        print("",li*100,"")
        ram = int(input("Enter you RAM here:"))
        if ram==1:
            q=("select product_name from product where sno=18")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            ram=res
        elif ram==2:
            q=("select product_name from product where sno=19")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            ram=res
        elif ram==3:
            q=("select product_name from product where sno=20")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            ram=res
        elif ram==4:
            q=("select product_name from product where sno=21")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            ram=res
        elif ram==5:
            q=("select product_name from product where sno=22")
            cur.execute(q)
            res=cur.fetchone()[0]
            print(res)
            ram=res
        else:
            print("ERROR")
            custom_rig()

        print("\n****************************************************************")
        print("Your beast looks likely to have:")
        print("Your processor",cpu)
        print("Your motherboard",mobo)
        print("Your cabinet",cabi)
        print("Your GPU",GD)
        print("Your Storage",storage)
        print("Your RAM",ram)
        print("\n----------------------------------------------------------------")
        print("YOUR TRACKING/ORDER ID:",order_id)
        print("\n----------------------------------------------------------------")
        print("\n****************************************************************")

        var=False
    
    phno=input("Enter your contact number: ")
    
    print("1. VIA BHIM/UPI")
    print("2. CASH ON DELIVERY")
    print("3. OTHER NET BANKING")
    pay=int(input("Choose method of payment:"))

    if pay==1 or pay==3:
        print("https://business.bharatpe.com/payment-link")
        print("Thanks for the purchase")
    else:
        print("Thanks for the purchase")

    print("\n****************************************************************")
    print("ORDERED SUCCESSFULLY")
    print("You will be contacted withing 8 hrs of your order placing")
    print("you will have direct contact to the builders and testers of your machine")
    print("please visit again in future")
    print("LOOK FOR MORE COMPONENTS LIKE MOUSE , KEYBOARD ,HEADSETS AND MANY MORE AT REASONABLE PRICES...")
    print("\n****************************************************************")
    
    val="use comp_project"
    cur.execute(val)
    sql="insert into orders values('{}','{}','{}','{}','{}','{}','{}','{}')".format(cpu,GD,mobo,storage,ram,cabi,phno,order_id)
    cur.execute(sql)
    main()
##
def order_tracking():
    mycon.autocommit=True
    try:
        li="-"
        print("",li*100,"")
        print("PLEASE KEEP YOUR ORDER ID HANDY")
        print("",li*100,"")
        id=input('enter your order id: ')
        s1="select * from orders where order_id='{}'".format(id)
        cur.execute(s1)
        data=cur.fetchall()
        for i in data:
            li="-"
            print("",li*100,"")
            print("CPU         ::::",i[0])
            print("GPU         ::::",i[1])
            print("MOTHERBOARD ::::",i[2])
            print("RAM         ::::",i[3])
            print("CABINET     ::::",i[4])
            print("PH. NO      ::::",i[6], "\n")
            print("",li*100,"")
            TERMS=['SHIPPED','PACKED','PLACED','DELIVERED']
            print("THE ORDER HAS BEEN",random.choice(TERMS),"SUCCESSFULLY")
            print("",li*100,"")
    except:
        print('ORDER DOES NOT EXISTS')
    main()
##
def order_cancelling():
    mycon.autocommit=True
    try:    
        id=input('enter your order id number: ')
        s1="delete from orders where order_id='{}'".format(id)
        cur.execute(s1)
        print('ORDER CANCELLED')
        main()
            
    except:
        print('PLEASE GIVE US YOUR VALUABLE FEEDBACK')
        main()
##
def account_details():
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cur.execute(c1)
        data1=cur.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cur.execute(s1)
        data=cur.fetchall()[0]
        data=list(data)
        if data[0]==a:
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
            cur.execute(s1)
            data=cur.fetchall()[0]
            data=list(data)
            li='-'
            print("",li*100,"")
            print(x[0],':::',data[0])
            print(x[1],':::',data[1])
            print(x[2],':::',data[2])
            print(x[3],':::',data[3])
            print(x[4],':::',data[4])
            print(x[5],':::',data[5])
            print("",li*100,"") 
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
    main()
##
def sign_up():
    mycon.autocommit=True
    f=input("FIRST NAME:")
    l=input("LAST NAME:")
    con=True
    a=input("USER NAME: ")
    b=input('PASS WORD:')
    c=input('RE-ENTER YOUR PASS WORD:')
    ph=input("PHONE NUMBER:")
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gen=input('ENTER YOUR GENDER:')
    print("ENTER YOR DATE OF BIRTH")
    d=input("DD:")
    o=input("MM:")
    p=input("YYYY:")
    dob=d+'/'+o+'/'+p
    age=int(input('YOUR AGE:'))
    if b==c:
        c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,gen,dob,age)
        cur.execute(c1)
        print('WELCOME!',f,l)       
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
##
def delete():
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    z=1
    if z==1:
        b1="delete from user_accounts where user_name = '{}'".format(a)
        cur.execute(b1)
        return True  
    else:
        print("ACCOUNT DOES NOT EXIST")
    return True

menu()

"""
==========================================================CODE WRITTEN BY==============================================================

░█▀▀█ ▒█▀▀█ ▒█░░▒█ ░█▀▀█ ▒█▄░▒█ 　 ▒█▀▀▀█ ▒█▀▀█ ▀█▀ ▒█░░▒█ ░█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█░░▒█ ░█▀▀█ 　 
▒█▄▄█ ▒█▄▄▀ ▒█▄▄▄█ ▒█▄▄█ ▒█▒█▒█ 　 ░▀▀▀▄▄ ▒█▄▄▀ ▒█░ ░▒█▒█░ ▒█▄▄█ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ ░▒█▒█░ ▒█▄▄█ 　 
▒█░▒█ ▒█░▒█ ░░▒█░░ ▒█░▒█ ▒█░░▀█ 　 ▒█▄▄▄█ ▒█░▒█ ▄█▄ ░░▀▄▀░ ▒█░▒█ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ░░▀▄▀░ ▒█░▒█ 　 

▀▄▒▄▀ ▀█▀ ▀█▀ ░░ ░█▀▀█ 　 ▄▀ █▀▀█ █▀▀ ▀▄ 
░▒█░░ ▒█░ ▒█░ ▀▀ ▒█▄▄█ 　 █░ █▄▀█ ▀▀▄ ░█ 
▄▀▒▀▄ ▄█▄ ▄█▄ ░░ ▒█░▒█ 　 ▀▄ █▄▄█ ▄▄▀ ▄▀

=======================================================================================================================================

"""
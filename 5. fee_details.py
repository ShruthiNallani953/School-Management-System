import main_menu
import pymysql as co

def FEE_MENU():
        while True:
              print("\t\t-----------------------------------------------------------")
              print("\t\t**** WELCOME TO FEE MANAGEMENT****")
              print("\t\t-----------------------------------------------------------")
              print("\t\t------------------------------------------------------------")
              print("1 : Insert Fees for New Admission")
              print("2 : Show Fee details")
              print("3 : Update Fees")
              print("4 : Exempt Fees")
              print("5 : Exit")
              choice=int(input("Enter your choice:"))
              if choice==1:
                    add_fee_details()
              elif choice==2:
                    show_fee_details()
              elif choice==3:

                    update_fee_details()
              elif choice==4:
                    delete_fee_details()
              elif choice==5:
                    break
              else:
                    print("Error : Invalid choice ..... Try Again .....")
                    cont=input("Press any key to continue:")


def add_fee_details():
        mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
        cursor=mycon.cursor()
        admno=int(input("Enter Admission Number :"))
        sname=input("Enter Student Name :")
        fees=int(input("Enter amount of fees to be paid per quarter :"))
        query="insert into fees values ({ },'{ }',{ });".format(admno, sname, fees)
        cursor.execute(query)
        mycon.commit()
        print("Record has been saved in the fees table...")
        mycon.close()


def show_fee_details():
        mycon=co.connect(host="localhost",user="root", password="123", database="smsdb")
        cursor=mycon.cursor()
        query="select * from fees ;"
        data=cursor.execute(query)
        data=cursor.fetchall()
        for rec in data:
              print(rec)
        mycon.close()


def update_fee_details():
        mycon=co.connect(host="localhost",user="root", password="123", database="smsdb")
        cursor=mycon.cursor()
        admno=int(input("Enter Admission Number :"))
        fees=int(input("Enter amount of fees to be updated :"))
        query="update fees set Amount_of_Fees={} where Admission_No='{ }' ;" .format(fees,admno)
        cursor.execute(query)
        mycon.commit()
        print("Record updated successfully")
        mycon.close()


def delete_fee_details():
        mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
        cursor=mycon.cursor()
        admno=int(input("Enter Admission Number :"))
        query="delete from fees where Admission_No={ };".format(admno)
        cursor.execute(query)
        mycon.commit()
        print("Fees record deleted successfully...")
        mycon.close()

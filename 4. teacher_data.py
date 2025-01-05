import main_menu
import pymysql as co

def TCH_MENU():
       while True:
            print("\t\t----------------------------------------------------------------")
            print("\t\t**** WELCOME TO TEACHER MANAGEMENT ****")
            print("\t\t----------------------------------------------------------------")
            print("\t\t-----------------------------------------------------------------")
            print("1 : Add new teacher record")
            print("2 : Show teacher details")
            print("3 : Search teacher record")
            print("4 : Delete teacher record")
            print("5 : Exit")
            print("\t\t---------------------------------------------------------------------")
            choice=int(input("Enter your choice :"))
            if choice==1:
                  add_teacher_details()
            elif choice==2:
                  show_teacher_details()
            elif choice==3:
                  search_teacher_details()
            elif choice==4:
                  delete_teacher_details()
            elif choice==5:
                  break
            else:
                  print("Error : Invalid choice ..... Try Again .....")
                  cont=input("Press any key to continue:")


def add_teacher_details():
       mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
       cursor=mycon.cursor()
       tno=int(input("Enter teacher Number :"))
       tname=input("Enter teacher Name :")
       tjob=input("Enter teacher's Designation :")
       query="insert into teacher values ({ },'{ }','{ }');".format(tno, tname, tjob)
       cursor.execute(query)
       mycon.commit()
       mycon.close()
       print("Record has been saved in the teacher table...")


def show_teacher_details():
       mycon=co.connect(host="localhost", user="root",password="123", database="smsdb")
       cursor=mycon.cursor()
       query="select * from teacher;"
       cursor.execute(query)
       data=cursor.fetchall()
       for rec in data:
            print(rec)
       mycon.close()


def search_teacher_details():
       mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
       cursor=mycon.cursor()
       tno=int(input("Enter teacher number :"))
       query="select * from teacher where Teacher_No=%s;"%(tno)
       cursor.execute(query)
       data=cursor.fetchall()
       print(data)
       mycon.close()


def delete_teacher_details():
       mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
       cursor=mycon.cursor()
       tno=int(input("Enter teacher Number :"))
       query="delete from teacher where Teacher_No=%s;"%(tno)
       cursor.execute(query)
       mycon.commit()
       print("Teacher record deleted successfully...")
       mycon.close()

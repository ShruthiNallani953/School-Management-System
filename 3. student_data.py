import main_menu
import pymysql as co

def STU_MENU():
        while True:
              print("\t\t--------------------------------------------------------------------------")
              print("\t\t******WELCOME TO STUDENT MANAGEMENT ******")
              print("\t\t--------------------------------------------------------------------------")
              print("\t\t--------------------------------------------------------------------------")
              print("1 : Add student record")
              print("2 : Show student details")
              print("3 : Search student record")
              print("4 : Delete Student record")
              print("5 : Exit")
              print("\t\t---------------------------------------------------------------------------")
              choice=int(input("Enter your choice:"))
              if choice==1:
                     add_student()
              elif choice==2:
                     show_student_details()
              elif choice==3:
                     search_student_details()
              elif choice==4:
                     delete_student_details()
              elif choice==5:
                     break
              else:
                     print("Error : Invalid choice ..... Try Again .....")
                     cont=input("Press any key to continue:")


def add_student():
        mycon=co.connect(host="localhost", user="root",password="123", database="smsdb")
        cursor=mycon.cursor()
        sroll=int(input("Enter roll number :"))
        sname=input("Enter student name :")
        sub1=input("Enter subject1 :")
        sub2=input("Enter subject2 :")
        sub3=input("Enter subject3 :")
        query="insert into student_12A values ({ },'{ }','{ }','{ }','{ }');" .format(sroll, sname, sub1, sub2, sub3)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        print("Record has been saved in the student table...")


def show_student_details():
        mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
        cursor=mycon.cursor()
        query="select * from student_12A;"
        cursor.execute(query)
        data=cursor.fetchall()
        for rec in data:
              print(rec)
        mycon.close()


def search_student_details():
        mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
        cursor=mycon.cursor()
        r_no=int(input("Enter Roll Number :"))
        query="select * from student_12A where Roll_No=%s;"%(r_no)
        cursor.execute(query)
        data=cursor.fetchall()
        print(data)
        mycon.close()


def delete_student_details():
        mycon=co.connect(host="localhost",user="root",password="123", database="smsdb")
        cursor=mycon.cursor()
        rno=int(input("Enter Roll Number :"))
        query="delete from student_12A where Roll_No=%s;"%(rno)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        print("Student record deleted successfully...")

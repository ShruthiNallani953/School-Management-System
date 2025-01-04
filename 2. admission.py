import main_menu
import pymysql as co

def ADM_MENU():
         while True:
             print("\t\t------------------------------------------------------------")
             print("\t\t***** WELCOME TO ADMISSION MANAGEMENT *****")
             print("-----------------------------------------------------------------")
             print("\t\t------------------------------------------------------------")
             print("1 : New Admission")
             print("2 : Show Admission Details")
             print("3 : Search the admission record")
             print("4 : Issue TC (Deletion of admission record)")
             print("5 : Exit")
             print("\t\t------------------------------------------------------------")
             choice=int(input("Enter your choice :"))
             if choice==1:
                   new_admin()
             elif choice==2:
                   show_admin_details()
             elif choice==3:
                   search_admin_details()
             elif choice==4:
                   delete_admin_details()
             elif choice==5:
                   break
             else:
                   print("Error : Invalid choice ..... Try Again .....")
                   cont=input("Press any key to continue :")


def new_admin():
         mycon=co.connect(host="localhost", user="root", password="123", database="smsdb")
         cursor=mycon.cursor()
         adminno=int(input("Enter Admission Number :"))
         sname=input("Enter student name :")
         clas=int(input("Enter class :"))
         fname=input("Enter Father's Name :")
         mname=input("Enter Mother's Name :")
         query="insert into admission values ({ },'{ }',{ },'{ }','{ }') ;" .format (adminno, sname, clas,fname, mname)
         cursor.execute(query)
         mycon.commit()
         print("New Admission record added successfully.")


def show_admin_details():
         mycon=co.connect(host="localhost", user="root", password="123", database="smsdb")
         cursor=mycon.cursor()
         query="select * from admission;"
         cursor.execute(query)
         data=cursor.fetchall()
         for rec in data:
                   print(rec)
         mycon.close()


def search_admin_details():
         mycon=co.connect(host="localhost", user="root", password="123", database="smsdb")
         cursor=mycon.cursor()
         adminno=int(input("Enter Admission No. to be searched :"))
         query="select * from admission where Admission_Number=%s; " % (adminno)
         cursor.execute(query)
         data=cursor.fetchall()
         print(data)
         mycon.close()


def delete_admin_details():
         mycon=co.connect(host="localhost", user="root", password="123", database="smsdb")
         cursor=mycon.cursor()
         adminno=int(input("Enter Admission No to be deleted :"))
         query="delete from admission where Admission_Number=%s;"%(adminno)
         cursor.execute(query)
         mycon.commit()
         print("Admission record deleted successfully.")

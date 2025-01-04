import main_menu
import admission
import student_data
import teacher_data
import fee_details


while True:
         print("\t\t-----------------------------------------------------------------------")
         print("\t\ **WELCOME TO SCHOOL MANAGEMENT SYSTEM** ")
         print("\t\------------------------------------------------------------------------")
         print("\t\t-----------------------------------------------------------------------")
         print("\t\t ***KENDRIYA VIDYALAYA TIRUMALAGIRI, SECUNDERABAD*** ”)
         print("\t\t-----------------------------------------------------------------------")
         print("1 : Admission Management")
         print("2 : Student Data")
         print("3 : Teachers Data")
                  print("4 : Fee Details")
         print("5 : Exit")
         print("\t\t-----------------------------------------------------------------------")
         choice=int(input("Enter your choice:"))
         if choice==1:
                admission.ADM_MENU()
         elif choice==2:
                student_data.STU_MENU()
         elif choice==3:
                teacher_data.TCH_MENU()
         elif choice==4:
                fee_details.FEE_MENU()
         elif choice==5:
                print("***Thanks for visiting School Management***")
                break
         else:
                print("Error : Invalid choice ...... Try Again ......")
                cont=input("Press any key to continue:")

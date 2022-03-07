import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer =csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number","E-mail ID"])

        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter student information for student #{} in the following format\n(Name Age Contact_No E-Mail_ID) : ".format(student_num))
        student_info_list =  student_info.split(' ')
        
        choice_check= input("Is the entered values are correct? (yes\ no): ")

        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("enter (yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check =="no":
            print("\nPlease re-enter the values: ")

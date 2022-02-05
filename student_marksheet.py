# Program for student marksheet

#student Information
name = input('Enter Student Name: ')
roll_no = input('Enter Student roll no.: ')
standard = input('Enter the Student class: ')
marathi = int(input('Mark\'s obtained in Marathi - '))
hindi = int(input('Mark\'s obtained in Hindi - '))
english = int(input('Mark\'s obtained in English - '))
math = int(input('Mark\'s obtained in Math - '))
science = int(input('Mark\'s obtained in Science - '))
total_marks = int(input('Enter Total out Off marks: '))
total_marks_obtained = marathi + english + hindi + math + science
percentage = total_marks_obtained*100/total_marks
print()
# print marksheet
print('-------------STUDENT\'S MARKSHEET-------------')
print()
print('Student name is: ',name)
print('Student Roll No. is: ',roll_no)
print( 'Student class is: ',standard)
print('Mark\'s Obtained in Marathi : ',str(marathi))
print('Mark\'s Obtained in Hindi : ',str(hindi))
print('Mark\'s Obtained in English : ',str(english))
print('Mark\'s Obtained in Math : ',str(math))
print('Mark\'s Obtained in Science : ',str(science))
print('Total Mark\'s Obtained',str(total_marks_obtained))
print('Enter Total out Off marks: ',total_marks)
print('Percentage Obtained',str(percentage))
print()
print('-----RESULT-----')
# failed subjects
i = 0
failed_subject = ''
if marathi <= 35:
    i += 1
    failed_subject += 'Marathi '
if hindi <= 35:
    i += 1
    failed_subject += 'Hindi '
if english <= 35:
    i += 1
    failed_subject += 'English '
if math <= 35:
    i += 1
    failed_subject += 'Math '
if science <= 35:
    i += 1
    failed_subject += 'Science '
print()
#grade and remark
if i == 0 :
    if percentage >= 90:
        print('Grade O')
        print('Remark : Excellent keep it up')
    elif percentage >= 80:
        print('Grade A')
        print('Remark : Very Good keep going')
    elif percentage >= 65:
        print('Grade B')
        print('Remark : Good push more')
    elif percentage >= 50:
        print('Grade C')
        print('Remark : Not bad try harder')
    elif percentage >=35:
        print('FAIL')
        print('Remark : Improve Performance')
else:
    print('FAIL')
    print('Failed Subjects : ', str(i))
    print('Subject\'s Failed :',failed_subject)

import sys, os, time
from colorama import Fore as Color
import myClasses

os.system('clear')
#####################################‌‌  Main Module added to the program 
myClasses.Introduce()
all_students = ['سنایی', 'علی اکبری', 'عبدی', 'خلیلی', 'فتوح نژاد', 'علی زاده', 'عسکری', 'فرمانی', 'فصیح القلم', 'فضلی نیا', 'فیروزبین', 'نجف آبادی', 'رحیمی', 'رنجبر', 'غضنفری', 'سعیدنیا', 'سلطانی', 'رهنما', 'ظریف خواه', 'خلقی', 'محمد زارعی', 'رفعت بخش', 'زارعی', 'ضمیر', 'روزیطلب', 'داوری', 'داودیان', 'رسول زاده', 'زینلی','']
#Top Here is the list of all students which are in the Class 
Present_student = []

#Open the File with the list of names

with open('check.txt','r') as file:
    Names = file.read()
    for i in all_students:
        if i in Names:
            Present_student.append(i)

with open('Presents.txt','w') as file:
    for i in Present_student:
        file.write(i+"\n")
print(Color.GREEN+" [!] Your file(Presents.txt) is ready.")

time.sleep(2)
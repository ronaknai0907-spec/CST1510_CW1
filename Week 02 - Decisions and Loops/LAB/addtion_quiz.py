"""
addition quiz 

step 1: Generate two single-digit integers for number1 (e.g., 4) and number 2 (e.g.,5)
step 2: Prompt the student to answer, "what is 4 + 5?" ( user input)
step 3: Check whether the student's answer is correct
"""

import random
while True:
   num_1 = random.randint(1,30)
   num_2 = random.randint(1,30)


   answer = int(input(f"what is {num_1} + {num_2}?"))
   if answer == num_1 + num_2:
    print("correct!,next question")
    
    

   answer = int(input(f"what is {num_1} - {num_2}?"))
   if answer == num_1 - num_2:
    print("correct!, next question")


    answer = int(input(f"what is {num_1} * {num_2}?"))
    if answer == num_1 * num_2:
         print("correct! , next question")
         
    
    answer = int(input(f"what is {num_1} / {num_2}?"))
    if answer == num_1 / num_2:
           print("correct! , nice job you have passed the exam")
           break
    else:
         print("incorrect, you are filed")



     
   


 



    







    
       
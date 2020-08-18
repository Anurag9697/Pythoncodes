#import modules
import sys,random


#initial variables
#loop variable
#list of responses variable
l=["IT IS CERTAIN","YOU MAY RELY ON IT","AS I SEE IT, YES","OUTLOOK LOOKS GOOD","MOST LIKELY","IT IS DECIDELY SO","WITHOUT A DOUBT","YES, DEFINETLY"]


#while loop
while True:
#write the code that will recieve the user input
#return the random response
#and quit the application
    question=input("Ask a question(Press Enter to exit)")
    if(question==""):
        sys.exit()
    else:
        print(random.choice(l))

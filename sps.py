#Stone Paper Scissors
import random
yourscore=0
compscore=0
for i in range(5):
 userchoice=raw_input("choose between stone,paper and scissors")
 l=["stone","paper","scissors"]
 compchoice=random.choice(l)
 print "computer chooses" ,compchoice

 if userchoice==compchoice:
     print "both of you chose the same action"
 elif userchoice=="stone" and compchoice=="scissors":
     yourscore+=1
 elif userchoice=="stone" and compchoice=="paper":
     compscore+=1
 elif userchoice=="scissors" and compchoice=="stone":
     compscore+=1
 elif userchoice=="scissors" and compchoice=="paper":
     yourscore+=1
 elif userchoice=="paper" and compchoice=="stone":
     yourscore+=1
 elif userchoice=="paper" and compchoice=="scissors":
     compscore+=1
print "your score is",yourscore
print "computer's score is",compscore
if yourscore>compscore:
    print "you win"
else:
    print "computer wins"
     

     


                    

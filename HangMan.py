import time
print("Welcome To Guess the Cricketer ")

  
question ={"1.  | Nation =  Pakistan    | Role = Wicket Keeper |" : "farhan" ,
           "2.  | Nation =    India     | Role =     Opener    |" : "gill"   ,
           "3.  | Nation = Afghanistan  | Role =    Spinner    |" : "mujeeb" ,
           "4.  | Nation =  Australia   | Role =  All-Rounder  |" : "green"  ,
           "5.  | Nation =   England    | Role =  All-Rounder  |" : "stokes" ,
           "6.  | Nation =  West Indies | Role =     Opener    |" : "king" ,
           "7.  | Nation = South Africa | Role =  middle order |" : "miller" ,
           "8.  | Nation =   Pakistan   | Role =     Bowler    |" : "naseem" ,
           "9.  | Nation =  New Zealand | Role =     Bowler    |" : "duffy" ,
           "10. | Nation = South Africa | Role =  All-Rounder  |" : "jansen" ,
           "11. | Nation =   Pakistan   | Role =  Fast Bowler  |" : "hasnain" ,
           "12. | Nation = New Zealand  | Role =     Batter    |" : "allen", 
           "13. | Nation = South Africa | Role =  Fast Bowler  |" : "ngidi" ,
           "14. | Nation =     India    | Role =  All-Rounder  |" : "dubey" ,
           "15. | Nation =   Pakistan   | Role =    spinner    |" : "sajid" }

score = 0

for term,ans in question.items():
 print(f"| There are {len(ans)} Letter in His Name | ")
 guess = input(f"{term} : ",  ).lower()
 print("---------------------------------------")
 if guess == ans:
  print("✅ Correct Answer !!")
  print("----------------------------------------")
  score += 1
 else :
  print(f"|❌ Wrong Answer | Correct Answer is {ans}")
  print("------------------------------------------")

print(f"🏆 You Have Guessed {score} out of {len(question)}")


import os
teams= {"Pakistan"    :"| 1.Fakhar | 2.Farhan | 3.Saim | 4.M.Haris (WK) | 5.Hassan Nawaz | 6.Salman (C) | 7.khushdil | 8.Wasim | 9.Haris |10.Sufiyan |11.Hassan Ali |",
       "India"        :"| 1.Gill | 2.Abishak | 3.Jaiswal | 4.Surya (C) | 5. Tilak | 6.Pant (WK) | 7.Hardik | 8.Jadeja | 9.Bumrah | 10.Siraj | 11.Arshdeep |",
       "Australia"    :"| 1.Head | 2.McGark | 3.Marsh | 4.Maxwell | 5.Inglis (WK)| 6. Green | 7.Hardie | 8.Cummins (C)| 9.Starc | 10.hazelwood | 11.Zampa |",
       "New Zealand"  :"| 1.Allen | 2.Conway | 3.Seifert (WK) | 4.Campman | 5. Mitchell | 6. Phillips | 7. Santner (C)| 8.Duffy | 9.Sears | 10.Henry | 11.O`Rourke|",
       "England"      :"| 1.Duckett | 2. Salt | 3.Buttler (C) | 4.Brook | 5.Bethell | 6.Smith (WK)| 7.W.Jacks | 8.Curran | 9.Archer | 10.Wood | 11.A.Rashid|",
       "South africa" :"| 1.Rickelton (WK) | 2.Bavuma (C) | 3.R.Hendrick | 4.Markarm | 5.Stubs| 6.Miller | 7.Mulder | 8.Jansen | 9.Mahraj | 10.Rabada | 11.Maphaka|",
       "West Indies"  :"| 1.Lewis | 2.Myers | 3.Hope (Wk) | 4.Rutherford | 5.Powell (C)| 6.Hetmyer | 7.Russell | 8.Holder | 9.A.Hosein | 10.A.Joseph |11.S.Joseph |",}

sel= ""
sel1=""
sel2="" 
sel3=""
sel4=""
sel5=""
#first
class cricket:
  def main():    
    print("----------------------------------")
    print("   | Welcome To Cricket APP |")
    print("----------------------------------")
#second  
class which:
 global sel
 def select():
     print("------------------------------------")
     print(" Select from Below for Proceeding ")
     print("------------------------------------")
     print("|   Fixture    |    Records    |")
     print("|    Teams     |    Calender   |")
     print("------------------------------------")
     sel =input(" Your Selection :  ").lower()
     return sel
#third
class fixture:
   global sel1
   def fix():
    print("-------------------------------------------")
    print("Select The League From Below For Proceeding")
    print("-------------------------------------------")
    print("|    T20 Leagues    |     International   |")
    print("-------------------------------------------")
    sel1 =input(" Your Selection :  ").lower()
    return sel1
   
   def t20():
    print(" ----------------------------------------------------------------------------------------- ")
    print("|-     T20 Blast   Starting From 29th May      Till 13th September  | Venue :   England   |")
    print("|-        MLC      Starting From 12th June     Till 13th July       | Venue :   America   |")
    print("|-  Global League  Starting From 10th July     Till 18th July       | Venue : West Indies |")
    print("|-   The Hundred   Starting From 05th August   Till 31 August       | Venue :   England   |")
    print("|-        CPL      Starting From 14th August   Till 21st September  | Venue : West Indies |")
    print("|-     Big Bash    Starting From 14th December Till 25th January    | Venue :  Australia  |")
    print(" ----------------------------------------------------------------------------------------- ")
   def nation():
    print(" ---------------------------------------------| JULY |----------------------------------------------------- ")
    print("|                                                                                                          |")
    print("|-   Zimbabave Tri-Series        Starting From 14th July       Till 26th July       | Venue :   Zimbabve   |")
    print("|-  Pakistan    vs  Banglades    Starting From 20th July       Till 24th July       | Venue :  Bangladesh  |")
    print("|-  NewZealand  vs  Zimababve    Starting From 30th July       Till 11th August     | Venue :   Zimbabve   |")
    print("|- West Indies  Vs  Pakistan     Starting From 31th July       Till 12th August     | Venue :  West Indies |")
    print("|                                                                                                          |")
    print(" --------------------------------------------| AUGUST |---------------------------------------------------- ")
    print("|                                                                                                          |")
    print("|- South Africa Vs  Australia    Starting From 10th August     Till 24th August     | Venue :   Australia  |")
    print("|-  Bangladesh  Vs   India       Starting From 17th August     Till 31st August     | Venue :  Bangladesh  |")
    print("|                                                                                                          |")
    print(" ---------------------------------------------| SEPTEMBER |------------------------------------------------ ")
    print("|                                                                                                          |")
    print("|- South Africa Vs  England      Starting From 02nd September  Till 14th September  | Venue :   England    |")
    print("|                                                                                                          |")
    print(" ----------------------------------------------| OCTOBER |------------------------------------------------- ")
    print("|                                                                                                          |")
    print("|-  Australia   Vs  NewZealand   Starting From 01st October    Till 04th October    | Venue :  New Zealand |")
    print("|- West Indies  vs    India      Starting From 02nd October    Till 184h October    | Venue :     India    |")
    print("|-  England     Vs  NewZealand   Starting From 18th October    Till 01st November   | Venue :  New Zealand |")
    print("|-   India      Vs  Australia    Starting From 19th October    Till 08th November   | Venue :   Australia  |")
    print("|                                                                                                          |")
    print("|----------------------------------------------| NOVEMBER |------------------------------------------------|")
    print("|                                                                                                          |")
    print("|- West Indies  Vs  NewZealand   Starting From 05th November   Till 22nd December   | Venue :  New Zealand |")
    print("|- South Africa vs    India      Starting From 14th November   Till 19th December   | Venue :     India    |")
    print("|-          The Ashes            Starting From 21st November   Till 08th January    | Venue :   Australia  |")
    print("|                                                                                                          |")
    print("|----------------------------------------------------------------------------------------------------------|")
#third
class record:
   def rec():
      print("-------------------------------------------")
      print("     Select From Below For Proceeding      ")
      print("-------------------------------------------")
      print("|       Batting       |      Bowling      |")
      print("-------------------------------------------")
      sel2 =input(" Your Selection :  ").lower()
      return sel2 
   def batting():
      print("-------------------------------------------")
      print("     Select From Below For Proceeding      ")
      print("-------------------------------------------")
      print("|     Biletral      |    International    |")
      print("-------------------------------------------")
      sel3 =input(" Your Selection :  ").lower()    
      return sel3
   def bowling():   
      print("-------------------------------------------")
      print("     Select From Below For Proceeding      ")
      print("-------------------------------------------")
      print("|     Biletral       |      World Cup     |")
      print("-------------------------------------------")
      sel3 =input(" Your Selection :  ").lower()    
      return sel3
   def biletral1(): # 1-> bowling
      global sel4
      print("-------------------------------------------")
      print("   Select Format Below For Proceeding      ")
      print("-------------------------------------------")
      print("|     Test    |     Odi     |     T20i    |")
      print("-------------------------------------------")
      sel4 =input(" Your Selection :  ").lower()    
      
      if sel4 == "test":
       print("---------------------------------------------------------------------------------- ")
       print(" |      Most Wickets    in Test Format  : 700 Wickets  |  Record : James Anderson  |")    
       print(" |      Best Figure     in Test Format  :    19/90     |  Record :   Jim Laker     |") 
       print(" | Most 5-Wicket Hauls  in Test Format  :      67      |  Record :  Muttiah Murli  |") 
       print("----------------------------------------------------------------------------------- ")
      elif sel4 == "odi":
       print("----------------------------------------------------------------------- ")
       print(" |      Most Wickets    in Odi Format : 534 Wickets |  Record : Muttiah Murli |")    
       print(" |       Best Figur     in Odi Format :    8/19     |  Record : Chaminda Vaas |") 
       print(" | Most 5-Wicket Hauls  in Odi Format :     13      |   Record : Waqar Younis |") 
       print("-----------------------------------------------------------------------")
      elif sel4 == "t20i":
       print("----------------------------------------------------------------------------------------- ")
       print(" |          Most Wickets         in T20i Format : 107 Wickets |  Record :   Rashid Khan  |")    
       print(" |          Best Figure          in T20i Format :    7/4      |  Record : Deepeak Chahar |") 
       print(" | Best Economy(Min 1000 balls)  in T20i Format :    5.96     |  Record : Daniel Vettori |") 
       print("----------------------------------------------------------------------------------------- ")
   def biletral2(): # 2-> batting
      global sel4
      print("-------------------------------------------")
      print("   Select Format Below For Proceeding      ")
      print("-------------------------------------------")
      print("|     Test    |     Odi     |     T20i    |")
      print("-------------------------------------------")
      sel4 =input(" Your Selection :  ").lower()    
      
      if sel4 == "test":
       print("------------------------------------------------------------------------------ ")
       print(" | Most runs     in Test Format :  |  Record : Sachin Tendulkar (15,921 runs) |")    
       print(" | Higest score  in Test Format :  |  Record :      Brian Lara (400*)         |") 
       print(" | Fastest 100   in Test Format :  |  Record :   Brendon McCullum (54 balls)  |") 
       print(" | Most Four     in Test Format :  |  Record : Sachin Tendulkar (2058 fours)  |")    
       print(" | Most Sixes    in Test Format :  |  Record :     Ben Stokes (128 sixes)     |") 
       print("------------------------------------------------------------------------------ ")

      elif sel4 == "t20i":
       print("----------------------------------------------------------------------------- ")
       print(" | Most runs      in  T20i Format : | Record :     Virat Kohli (4188 runs)   |")    
       print(" | Highest score  in  T20i Format : | Record :       Aaron Finch (172)       |") 
       print(" | Fastest 100    in  T20i Format : | Record :  Multiple Players (35 balls)  |") 
       print(" | Most Fours     in  T20i Format : | Record :     Babar Azam (416 fours)    |")    
       print(" | Most Sixes     in  T20i Format : | Record :    Rohit Sharma (182 sixes)   |") 
       print("----------------------------------------------------------------------------- ")
 
      elif sel4 == "odi":
       print("-------------------------------------------------------------------------------- ")
       print(" | Most runs      in ODI Format  :  |  Record : Sachin Tendulkar (18,426 runs)  |")    
       print(" | Highest score  in ODI Format  :  |  Record :       Rohit Sharma (264)        |") 
       print(" | Fastest 100    in ODI Format  :  |  Record :    AB de Villiers (31 balls)    |") 
       print(" | Most Fours     in ODI Format  :  |  Record :  Sachin Tendulkar (2016 fours)  |")    
       print(" | Most Sixes     in ODI Format  :  |  Record :    Shahid Afridi (351 sixes)    |") 
       print("-------------------------------------------------------------------------------- ")
   def world1(): 
      global sel5
      print("--------------------------------------------")
      print("    Select Format Below For Proceeding      ")
      print("--------------------------------------------")
      print("|   WTC   |  T20 World-cup   |  World Cup  |")
      print("--------------------------------------------")
      sel5 =input(" Your Selection in Format :  ").lower()    
      
      if sel5 == "wtc":
       print("----------------------------------------------------------------------------- ")
       print(" |    Most Wickets      in  WTC :  | Record  :   Pat Cummins (108 wickets)   |")    
       print(" |    Best Figure       in  WTC :  | Record  : Ajaz Patel (10/119 vs India)  |") 
       print(" | Most 5-Wickets Haul  in  WTC :  | Record  : Ravichandran Ashwin (9 times) |") 
       print("----------------------------------------------------------------------------- ")

      elif sel5 == "worldcup" or sel5 == "world cup":
       print("----------------------------------------------------------------------------------------- ")
       print(" |    Most Wickets      in ODI World Cup :  | Record  :   Glenn McGrath (71 wickets)     |")    
       print(" |    Best Figure       in ODI World Cup :  | Record  : Glenn McGrath (7/15 vs Namibia)  |") 
       print(" | Most 5-Wickets Haul  in ODI World Cup :  | Record  :     Mitchell Starc (3 times)     |") 
       print("----------------------------------------------------------------------------------------- ")

      elif sel5 == "t20":
       print("----------------------------------------------------------------------------------------- ")
       print(" |    Most Wickets      in T20 World Cup :  | Record  :  Wanindu Hasaranga (31 wickets)  |")    
       print(" |    Best Figure       in T20 World Cup :  | Record  : Ajantha Mendis (6/8 vs Zimbabwe) |") 
       print(" |    Best Economy      in T20 World Cup :  | Record  :   Sunil Narine (5.17 economy)    |") 
      print("------------------------------------------------------------------------------------------ ")
   def world2():
      global sel5
      print("--------------------------------------------")
      print("    Select Format Below For Proceeding      ")
      print("--------------------------------------------")
      print("|   WTC   |  T20 World-cup   |  World Cup  |")
      print("--------------------------------------------")
      sel5 =input(" Your Selection in Format :  ").lower()    
      
      if sel5 == "wtc":
       print("-------------------------------------------------------------------------- ")
       print(" | Most runs      in WTC :  |  Record :      Joe Root (2,431 runs)        |")    
       print(" | Highest score  in WTC :  |  Record :   Kane Williamson (251 vs WI)     |") 
       print(" | Fastest 100    in WTC :  |  Record : Travis Head (106 off 120 vs Ind)  |") 
       print(" | Most Fours     in WTC :  |  Record :     Joe Root (258 boundaries)     |")    
       print(" | Most Sixes     in WTC :  |  Record :       Ben Stokes (38 sixes)       |") 
       print("-------------------------------------------------------------------------- ")

      elif sel5 == "t20":
       print("------------------------------------------------------------------------------------- ")
       print(" | Most runs      in  T20 World Cup :  |  Record :     Virat Kohli (1,141 runs)      |")    
       print(" | Highest score  in  T20 World Cup :  |  Record :   Brendon McCullum (123 vs BAN)   |") 
       print(" | Fastest 100    in  T20 World Cup :  |  Record : Chris Gayle ( 100 off 48 balls )  |") 
       print(" | Most Fours     in  T20 World Cup :  |  Record :     Virat Kohli (103 fours)       |")    
       print(" | Most Sixes     in  T20 World Cup :  |  Record :     Chris Gayle (63 sixes)        |") 
       print("------------------------------------------------------------------------------------- ")

      elif sel5 == "odi" :
       print("------------------------------------------------------------------------------------ ")
       print(" | Most runs      in  World Cup :  |  Record :    Sachin Tendulkar (2,278 runs)     |")    
       print(" | Highest score  in  World Cup :  |  Record :  Martin Guptill ( 237* vs WI, 2015)  |") 
       print(" | Fastest 100    in  World Cup :  |  Record :   Aiden Markram (100 off 49 balls)   |") 
       print(" | Most Fours     in  World Cup :  |  Record :    Sachin Tendulkar (241 fours)      |")    
       print(" | Most Sixes     in  World Cup :  |  Record :     Glenn Maxwell (43 sixes)         |") 
       print("------------------------------------------------------------------------------------ ")
#third
class calendar:
  def year():
   print("---------------------------------------------")
   print("Select The Year To Get the Stats of that Year")
   print("---------------------------------------------")
   sel7= int(input("Your Selection (2019-2025*) :"))

   if sel7 <2019 or sel7>2025:
     print(f"You Have Selected {sel7} Year !!! Please Select Form (2019-2025)")
   else :
      print(f"You Have Selected {sel7} Year")
      print("-------------------------------------------")
      print("     Select From Below For Proceeding      ")
      print("-------------------------------------------")
      print("|       Batting       |      Bowling      |")
      print("-------------------------------------------")
      sel8 =input(" Your Selection :  ").lower()
    
      if sel8 =="batting":
        if sel7== 2019:
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")
     
        elif sel7== 2020:
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")
     
        elif sel7== 2021:
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")
     
        elif sel7== 2022:
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")
     
        elif sel7== 2023:
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")
     
        elif sel7== 2024:
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")
     
        elif sel7== 2025:      
          print(f"| Most runs    In {sel7} : |Record ")
          print(f"| Highest Run  In {sel7} : |Record ")
          print(f"| Most Hunreds In {sel7} : |Record ")
          print(f"| Most Sixes   In {sel7} : |Record ")   
        else:
           print(f"Invalid Input !! You Have Entered {sel7}")     
      elif sel8=="bowling":
        if sel7== 2019:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")
        
        elif sel7== 2020:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")
        
        elif sel7== 2021:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")
        
        elif sel7== 2022:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")
        
        elif sel7== 2023:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")
        
        elif sel7== 2024:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")
        
        elif sel7== 2025:  
          print(f"| Most Wickets      In {sel7} : |Record ")
          print(f"| Best Figure       In {sel7} : |Record ")
          print(f"| Highest Econmey   In {sel7} : |Record ")
          print(f"| Most 5 Wicke-Haul In {sel7} : |Record ")          
        else:
         print(f"Invalid Input !! You Have Entered {sel7}")
      else:
       print(f"Invalid Input !! You Have Entered {sel8}") 
#third
class Teams:
 def opt():
   print(" ------------------------------------------------------ ")
   print("|    Pakistan    |   West Indies    |    New Zealand   |")
   print("|     India      |      England     |     Australia    |")
   print("|      ---       |   South Africa   |        ---       |")
   print(" ------------------------------------------------------ ")
   sel6 =input(" Your Selection :")


   if sel6 == "pakistan":
     print(f"You have Selected {sel6} :")  
     print(f"{teams['Pakistan']}")   
   
   elif sel6 == "india":
     print(f"You have Selected {sel6} :")  
     print(f"{teams['India']}")   
   
   elif sel6 == "australia":
     print(f"You have Selected{sel6} :")  
     print(f"{teams['Australia']}") 
   
   elif sel6 == "newzealand":
     print(f"You have Selected {sel6} :")  
     print(f"{teams['New Zealand']}") 
   
   elif sel6 == "england":
     print(f"You have Selected {sel6} :")  
     print(f"{teams['England']}") 
   
   elif sel6 == "southafrica":
     print(f"You have Selected {sel6} :")  
     print(f"{teams['South africa']}") 
   
   elif sel6 == "westindies":
     print(f"You have Selected {sel6} :")  
     print(f"{teams['West Indies']}") 
   else:
    if sel6 == "west indies":
     print(f"Invalid Input !! You Have Entered {sel6}")
     print("Please Enter the name with out space")
    elif sel6 == "south africa":
     print(f"Invalid Input !! You Have Entered {sel6}")
     print("Please Enter the name without space !!!!!")

loop = True
while loop:

 cricket.main()
 sel = which.select()

 if sel =="fixture":
    sel1 = fixture.fix()
    if sel1 == "leagues":
        fixture.t20()
    elif sel1 == "international":
        fixture.nation()
    else:
     print(f"Invalid Input !! You Have Entered {sel1}")

 elif sel =="records":
    sel2 =record.rec()
##bowling    
    if sel2 =="bowling":
     sel3 = record.bowling()
    
     if sel3 =="biletral":
       record.biletral1()     
     elif sel3=="world":
        record.world1()
     else:
      print(f"Invalid Input !! You Have Entered {sel3}")
##batting  
    elif sel2=="batting":
     sel3 = record.batting()  
     
     if sel3 =="biletral":
       record.biletral2()     
     elif sel3=="world":
        record.world2()
     else:
      print(f"Invalid Input !! You Have Entered {sel3}") 
    else:
     print(f"Invalid Input !! You Have Entered {sel2}")
 
 elif sel =="teams":
    Teams.opt()

 elif sel =="calender":
   calendar.year()
 
 else :
   print(f"Please Enter from the following You Have selected {sel}")
   print("--------------------------------------------------------")
 
 print()     
 print("Do You Wnat To Continue ........ Press any Key OR To Exit Press (X)")
 sel8=input("Your Selection :")

 if sel8 == "X" or sel8 == "x":
   loop = False 
 else :
    os.system('cls')   

print("-----------------------------------") 
print("   |    Thanks For Coming    |") 
print("-----------------------------------") 
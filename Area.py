import math

print(" Welcome TO AREA Calculator")

while True:
 print(" Enter Which Area YOu want to find")
 print("--------------------------------------------------------")
 print(" Rectangle , Square , Triangle , Circle , Parallelogram ")
 sel = input(" Select  First letter From These :  ")
 print("--------------------------------------------------------")

#Rectangle: Area = length * width.
#Square: Area = side * side (or side squared).
#Triangle: Area = (1/2) * base * height.
#Circle: Area = π * radius * radius (or π * radius squared).
#Parallelogram: Area = base * height

#Rectangle
 if sel == "R" :
   print(f"You Have selected rectagle")
   lenght = float(input (f"Enter Length : ") )
   width = float(input (f"Enter width : ") )
   area1 =width * lenght
   print( f"The Area Of Rectangle Is {round(area1 , 2)}")

#Square
 elif sel == "S" :
  print(f"You Have selected Square")
  side = float(input (f"Enter The Length Of the side : ") )
  area2 =side**2 
  print( f"The Area Of Square Is {round(area2 , 2)}") 
 
 #Triangle
 elif sel == "T" :
  print(f"You Have selected TriAngle")
  base = float(input (f"Enter Base : ") )
  height = float(input (f"Enter Height : ") ) 
  area3 =(1/2)*base*height 
  print( f"The Area Of TriAngle Is {round(area3 , 2)}")

#Circle
 elif sel == "C" :
  print(f"You Have selected Circle")
  radius = float(input (f"Enter radius: ") ) 
  area4 =math.pi*radius**2
  print( f"The Area Of Circle Is {round(area4 , 2)}")
 
 #Parallelogram
 elif sel == "P" :
  print(f"You Have selected Parallelogram")
  lenght = float(input (f"Enter Base : ") )
  width  = float(input (f"Enter Height : ") )
  area6 =width* lenght 
  print( f"The Area Of Parallelogram Is {round(area6 , 2)}")

 else :
  print("Please Enter One of the Following Term First letter")
 opt=input("To COntinue Press Any Key ................TO Exit Press X :")
 if not opt == "X" or opt == "x" :
  print("-------------------------------------------------------")
 else:
  break
print(" Thanks For Coming")
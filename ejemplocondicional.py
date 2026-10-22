while True:
  try:
   nota = float (input("ingrese una nota entre 0 y 100: "))
   if nota < 0 or nota >100:
      print ("nota invalida, ingrese una nota entre 0 y 100")
   elif nota >=90:
       print ("excelente")
   elif nota >=80: 
     print ("bueno")
   elif nota >=70: 
    print ("debe mejorar")
   else: 
      print ("reprobó")
  except ValueError: 
      print ("entrada invalida, ingrese un numero entre 0 y 100")   
    

max_delta = 0.008
min_delta = 0.005

l = 50

base_point = 1337

print("Расчет характерных точек для ландшафта\n")
print("Автор: mgostev.it@gmail.com\n")
print("Обо всех багах пишите на почту - буду фиксить")
print("Git-Hub программки: https://github.com/Butaforsky/arc \n\n")

print("Для выхода введите '0' (ноль)")

while(base_point != 0):
  
  print("Введите высоты точек в метрах, используйте точку, а не запятую!")
  print("По - умолчанию расстояние между точками равно 50 м\n")
  
  base_point = float(input("Первая точка, м: "))
  if(base_point == 0):
    exit()
  xt_point = float(input("Вторая точка, м: "))
  if(xt_point == 0):
    exit()
  try:
     l = float(input("Длина, м: "))
     if(l == 0):
      exit()
  except: 
     l = 50
     pass
  
  delta = (base_point - xt_point)/l

  if delta > max_delta:
      print("Досыпаем")
      xt_point = base_point - max_delta * l
      print("Характерная точка, м: ", round(xt_point, 2))
      delta = (base_point - xt_point)/l
      print("Уклон:", round(delta*1000,2), "промилле \n")

  elif delta < min_delta:
      print("Убираем лишнее")
      xt_point = base_point - min_delta * l
      print("Характерная точка, м: ", round(xt_point, 2))
      delta = (base_point - xt_point)/l
      print("Уклон:", round(delta*1000,2), "промилле \n")

  else:
     print("Уклон в диапазоне 5 - 8 промилле")
     print("Уклон: ", round(delta*1000,2), "промилле\n")

        

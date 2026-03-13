def main():
  # Lista inicial 
  grades = []
  
   # Función para insertar notas
  def add_grade():
    insert_grade = int(input("Ingresa una nota: "))
    grades.append(insert_grade)
    return insert_grade
  
  # Función para calcular promedio
  def calculate_average():
    total = sum(grades)/len(grades)
    return total
  
  # Ingresar notas
  print("Calculadora de Promedios")
  
  # Bucle
  option = 0
  while option != 3:
    
    # Menú
    print("1. Añadir nota\n2. Ver todas las notas\n3. Calcular promedio")
    
    option = int(input("Escoge una opción (1-3): "))
    
    #Casos
    match option:
      
      case 1:
        insert_grade = add_grade()
        print(f"Añadiste la nota {insert_grade}")
        
      case 2:
        for i in grades:
          print(i)
      
      case 3: 
        print(f"El promedio final es {round(calculate_average(), 2)}")
        
      case 4:
        print("No es una opción válida.")
  
main()
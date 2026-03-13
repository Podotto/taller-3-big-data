def main():
  # Lista inicial 
  grades = []
  
   # Función para insertar notas
  def add_grade():
    insert_grade = int(input("Ingresa una nota: "))
    grades.append(insert_grade)
    return insert_grade
  
  # Función para calcular promedio
  def calculate_average(grades):
    total = sum(grades)/len(grades)
    return total
  
main()
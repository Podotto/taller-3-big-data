def main():
  
  # Lista de nombres
  names = ["grethel", "emilio", "león", "maria", "kamila", "mia", "elliot"]
  
  # Función para buscar nombres
  def search_name():
    name_input = input("Name: ").lower()
    if name_input in names:
      print("Student found.")
      
    else:
      print("Student not found.")
      
      
  # Función para añadir nombres
  def add_name():
    new_student = input("Name: ").lower()
    names.append(new_student)
    print(f"Added {new_student} to the database.")
      
  # Menú
  while True:
    
    print("Student Database")
    print("1. Search student\n2. Add student\n3. Exit")
    
    option = int(input("Select an option (1-3): "))
    
    # Casos
    match option:
      
      case 1:
        search_name()
        
      case 2:
        add_name()
        
      case 3:
        print("Exit.")
        break
      
      case 4:
        print("Invalid option")
  
main()
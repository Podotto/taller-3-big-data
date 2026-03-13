def main():
  
  # Lista de nombres
  names = ["León", "Grethel", "Maria", "Emilio", "Kamila", "Mia", "Elliot"]
  
  # Función para buscar nombres
  def search_name():
    name_input = input("Write the name that you want to search: ")
    
    if name_input in names:
      print("Student found.")
    else:
      print("Student not found.")
      
  # Menú
  while True:
    
    print("Student Database")
    print("1. Search name\n2. Exit")
    
    option = int(input("Select an option (1-2): "))
    
    # Casos
    match option:
      
      case 1:
        search_name()
        
      case 2:
        print("Exit.")
        break
      
      case 3:
        print("Invalid option")
  
main()
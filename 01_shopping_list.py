def main():
  
  # Lista
  shopping_list = []
  
  # Agregar elementos
  shopping_list.append("Arroz")
  shopping_list.append("Lentejas")
  shopping_list.append("Leche")
  shopping_list.append("Tomate")
  shopping_list.append("Plátano")
  
    # Bucle
  option = 0
  while option != 5:
    
     # Menú
    print("Lista del súper")
    print("1. Ver la lista actual\n2. Añadir producto\n3. Eliminar producto\n4. Buscar producto\n5. Ir a pagar")
    
    option = int(input("¿Qué quieres hacer?: "))
    
    match option:
      
      # Caso 1 (Ver lista)
      case 1:
        print(shopping_list)
        
      # Caso 2 (Añadir producto)
      case 2:
        add_item = input("Añade un producto: ")
        shopping_list.append(add_item)
        print(f"{add_item} se añadió a la lista.\n")
        
      # Caso 3 (Eliminar producto)
      case 3:
        print(shopping_list)
        remove_item = input("Escribe el producto que quieres eliminar: ")
        shopping_list.remove(remove_item)
        print(f"{remove_item} se eliminó de la lista.\n")
        
               # Caso 4 (Buscar producto) 
      case 4:
        search_item = input("¿Qué producto buscas?: ")
        
        if search_item in shopping_list:
          print(f"{search_item} ya está en la lista.\n")
          
        else:
          print(f"{search_item} no está en la lista.\n")
        
      # Caso 6 (Terminar programa)
      case 5:
        print("Tu lista del súper es: ")
        
        for i in shopping_list:
          print(f"-{i}")
        
        print("Pase a la caja para pagar.")
        
      case 6:
        print("No es una opción válida.")
  
main()
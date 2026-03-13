def main():
  
  #Lista para el inventario
  inventory = []
  
  #Función para agregar items a la lista
  def add_inventory():
    add_item = input("Añade un item al inventario: ")
    inventory.append(add_item)
    print(f"Añadiste el item {add_item}")
  
  #Función para ver inventario
  def show_inventory():
    for i in inventory:
          print(i)
  
  #Función para eliminar items del inventario
  def drop_item():
    print(inventory)
    drop = int(input("¿Qué item quieres eliminar?: "))
    inventory.pop(drop)
  
  #Funció para buscar item
  def search_item():
    look_up = input("¿Qué item buscas?: ")
    
    if look_up in inventory:
      print(f"{look_up} está en tu inventario")
      
    else:
      print("No está en tu inventario.")
    
  #Bucle
  option = 0
  while option != 5:
    
    #Menú del videojuego
    print("Inventario\n1. Ver inventario\n2. Agregar item al inventario\n3. Eliminar item del inventario\n4. Buscar item en el inventario\n5. Salir")    
    
    #Input del usuario
    option = int(input("¿Qué quieres hacer (1-5)?: "))
    
    #Casos
    match option:
      case 1:
        show_inventory()
      
      case 2:
        add_inventory()
        
      case 3:
        drop_item()
        
      case 4:
        search_item()
      
      case 5:
        print("Saliste de tu inventario.")
        
      case 6: 
        print("No es una opción válida.")
        
    
main()
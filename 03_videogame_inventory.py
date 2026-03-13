def main():
  
  #Lista para el inventario
  inventory = []
  
  #Función para agregar items a la lista
  def add_inventory():
    add_item = input("Añade un item al inventario: ")
    inventory.append(add_inventory)
    return add_inventory
  
  #Bucle
  option = 0
  while option != 5:
    
    #Menú del videojuego
    print("Inventario\n1. Ver inventario\n2. Agregar item al inventario\n3. Eliminar item del inventario\n4. Buscar item en el inventario\n5. Salir")    
    
    #Input del usuario
    option = int(input("¿Qué quieres hacer (1-5)?: "))
    
    #Casos
    match option:
      
      case 5:
        print("Saliste de tu inventario.")
    
main()
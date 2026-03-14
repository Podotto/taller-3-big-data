def main():
  
  # Lista general de tareas
  to_do_tasks = []
  
  # Lista de tareas completadas
  completed_tasks = []
  
  #Función para añadir tareas
  def add_task():
    new_task = input("Añade una tarea: ")
    to_do_tasks.append(new_task)
    print(f"Añadiste {new_task} a la lista de tareas.")

  #Función para ver tareas
  def show_tasks():
    for i in to_do_tasks:
      print ("☐", i)
      
    for i in completed_tasks:
      print("[☑]", i)

  #Función para eliminar tareas
  def delete_task():
    
    for i, v in enumerate(to_do_tasks):
      print (i, v)
    
    remove_task = int(input("¿Cuál tarea quieres eliminar?: "))
    to_do_tasks.pop(remove_task)
    print(f"Eliminaste la tarea en la posición {remove_task}")
    
  #Función para completar tarea
  def complete_task():
    
    for i, v in enumerate(to_do_tasks):
      print ("☐", i, v)
      
  #Bucle
  while True:
    
    #Menú
    print("Bienvenido a tu gestor de tareas.")
    print("1. Agregar tarea\n2. Mostrar tareas\n3. Eliminar tarea\n4. Completar tarea\n5. Salir")
    
    option = int(input("¿Qué quieres hacer?: "))
    
    match option:
      
      case 1:
        add_task()
        
      case 2:
        show_tasks()
        
      case 3:
        delete_task()
        
      case 4: 
        complete_task()
        
      case 5:
        print("¡Hasta luego!")
        break
    

main()
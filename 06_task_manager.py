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

main()
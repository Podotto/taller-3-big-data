# taller-3-big-data
# Repositorio para desarrollar los programas del taller 3 de la materia Programación 1 en Python.

## **Preguntas de Desarrollo**

### **PROGRAMA 1 - SHOPPING LIST**

#### *1. ¿Qué estructura de datos usaste?*

R/: Utilicé las listas. Es una estructura de datos que nos permite ordenar elementos y realizar distintas funciones en ellas, como inserción y eliminación de datos, acceso a datos por índices númericos, iteraciones y búsquedas de elementos.

#### *2. ¿Cómo agregaste un nuevo producto?*

R/: Utilicé la función .append() para agregar los productos.

#### *3. ¿Cómo verificaste si un producto existe?*

R/: Utilicé la condición 'if' para que el usuario ingresara el nombre del producto y si hacía match en la lista le devolvía el resultado. De lo contrario, le enviaba un mensaje de que el item no se encontraba actualmente en la lista.

------------

### **PROGRAMA 2 - GRADE AVERAGE CALCULATOR**

#### *1. ¿Cómo recorres la lista?*

R/: La lista la recorro con el bucle 'for'. 

```
for i in grades:
          print(i)
```

Esto me permite visualizar cuáles son las notas almacenadas en la lista actualmente.

#### *2. ¿Cómo calculas el promedio?*

R/: El promedio lo calculo con la función:

```
  def calculate_average():
    total = sum(grades)/len(grades)
    return total
```

Primero defino el nombre de la función, luego la variable 'total', la cual contiene la operación. Esta se calcula utilizando las notas almacenadas en la lista grades. Primero se suman todas las notas, luego se dividen entre la cantidad (lens) y por último se devuelve el total.

#### *3. ¿Qué tipo de dato devuelve la función?*

R/: La función devuelve un dato int (numérico).

------------

### **PROGRAMA 3 - VIDEOGAME INVENTORY**

#### *1. ¿Qué método usaste para eliminar objetos?*

R/: Utilicé el método inventory.pop(), el cual elimina datos de la lista según su posición, no por el nombre. Esto evita eliminar items que tengan el mismo nombre.

#### *2. ¿Cómo verificas si el jugador tiene una poción?*

R/: Se utiliza la función

```
 def search_item():
    look_up = input("¿Qué item buscas?: ")
    
    if look_up in inventory:
      print(f"{look_up} está en tu inventario")
      
    else:
      print("No está en tu inventario.")
```

Esto le permite al usuario escribir lo que busca, y la función lo compara con los items actuales de la lista para ver si se encuentra en ella o no.

#### *3. ¿Qué hace la función showInventory?*

R/: Es una función que muestra (imprime) todo lo que está almacenado en la lista.

----------------

### **PROGRAMA 4 - SHOPPING CART**

#### *1. ¿Cómo sumaste los precios?*

R/: Utilicé la función 

```
  def calculate_total():
    total_price = sum(prices)
    return total_price
```

la cual suma todos los valores almacenados dentro de la lista 'precios' y la guarda en la variable total_price.

#### *2. ¿Qué hace la función calculateTotal?*

R/: Suma los valores almacenados en la lista 'precios' y los guarda en la variable total_price.

#### *3. ¿Qué tipo de dato devuelve?*

R/: Devuelve una variable numérica (int).

--------------

**PROGRAMA 5 - SEARCH NAME**

#### *1. ¿Cómo pediste el nombre al usuario?*

R/: Para pedir el nombre, utilicé:

```
def add_name():
    new_student = input("Name: ").lower()
    names.append(new_student)
    print(f"Added {new_student} to the database.")
```

Esta función permite ingresar un nombre a través de la variable new_student y agregarla a la lista con .appeend.

#### *2. ¿Cómo verificaste si existe en la lista?*

R/: Desarrollé la función:

```
  def search_name():
    name_input = input("Name: ").lower()
    if name_input in names:
      print("Student found.")
      
    else:
      print("Student not found.")
```

El nombre que se ingresa en la variable name_input se compara con los nombres que están en la lista actual. Si hay concidencia muestra un mensaje que lo encontró.

#### *3. ¿Qué ocurre si no existe?*

R/: Si no existe el estudiante, entonces el programa le muestra un mensaje de que no se encontró el estudiante y tiene la opción de añadirlo a la base de datos una vez regresa al menú principal.

.

def main():
  
  #Lista inicial
  prices = [19.99, 11.99, 25.00, 30.00, 45.99]
  
  #Función para calcular total
  def calculate_total():
    total_price = sum(prices)
    return total_price
    
  #Terminal
  print("Bienvenido a tu carrito de compras")
  print(f"Tu lista actual es {prices}")
  print(f"El precio total de su compra es: {calculate_total()}")
  
main()
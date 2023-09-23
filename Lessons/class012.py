# try / except

number = input("Vou dobrar o número que você digitar: ")

try:
  float_number = float(number)
  print(f"O dobro de {number} é {float_number * 2}")
except:
  print("Não foi possivel dobrar o número que você digitou")
# CONSTANTS em python de escreve em letras maiusculas.

velocidade = 61 # velocidade atual
local_carro = 90 # local carro atual

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

eh_velocidade_maior = velocidade >= RADAR_1
menor_range = LOCAL_1 - RADAR_RANGE
maior_range = LOCAL_1 + RADAR_RANGE
carro_multado_radar_1 = local_carro >= menor_range or local_carro >= maior_range

if eh_velocidade_maior:
  print('VELOCIDADE ACIMA DO RADAR')

if eh_velocidade_maior and carro_multado_radar_1:
  print('MULTADO')
# Split e Join 

"""
split - divide uma string através dos espaços.
join - junta uma string
sprip - remove os espaços dos dois lados.
rstrip - remove o espaço do lado direito.
lstrip - remove o espaço do lado esquerdo.
"""

phrase = "Olha só que, coisa interessante."
phrase_list = phrase.split(',')

for i, phrase in enumerate(phrase_list):
  print(phrase_list[i].strip())
  
unit_phrase = ','.join(phrase_list)
print(unit_phrase)
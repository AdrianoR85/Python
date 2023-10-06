# Sets - Conjuntos de dados em Python (tipo set)


# - Conjuntos são ensinados na matemática
# - Representados graficamente pelo diagrama de Venn
# - Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
 
# - Criando um Set ==> set(interável) ou {1,2,3}
s1 = set() # vazio
s1 = {1,2,3} # com dados
print(s1, type(s1))
 
# - Sets são eficientes para remover valores duplicados de iteráveis.
s2 = {1,2,3,4,2,4,3,2,3,2,1,2,5}
print(s2)
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis(for, in, not in)
 
# Métodos úteis:
# add, update, clear, discord 

# - União |
# - Intersecção &
# - Diferença -
# - Diferença Simétrica ^
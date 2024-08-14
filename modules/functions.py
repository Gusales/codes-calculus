from typing import List

def verify_is_function(function: List[List[int]]) -> dict:
  if not isinstance(function, list) or not all(isinstance(linha, list) for linha in function):
    print("O parâmetro fornecido não é uma função")
    return

  domain = []
  image = []

  for line in function:
    if len(line) <= 1 or line[0] == None:
      print("Não é uma função, pois o domínio não possui par na imagem")
      return
    if isinstance(line[1], list) and not all(x == line[1][0] for x in line[1]):
      print(f"Não é uma função, pois o {line[0]} possui dois pares diferentes na imagem {line[1]}")
      return

    domain.append(line[0])
    image.append(line[1])

  dictionary = {
    "dominio": domain,
    "imagem": image
  }

  return dictionary

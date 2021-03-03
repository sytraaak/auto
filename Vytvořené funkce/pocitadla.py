def pocet_znaku(a):
  """
  Sečte znaky a vrátí jejich počet ve slovniku znak : pocet
  """
  pocet = dict()
  for char in a.lower():
    if char not in pocet.keys():
      pocet[char] = 1
    else:
      pocet[char] += 1
  return print(pocet)

def pocet_prvku(a):
  """
  Sečte počet prvků v tuplu , listu nebo slovníku
  U slovníku vrací klíče
  """
  pocet = dict()
  for char in a:
    if char not in pocet.keys():
      pocet[char] = 1
    else:
      pocet[char] += 1
  return print(pocet)


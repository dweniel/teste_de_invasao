import requests

url = "terra.com.br"


file = open('lista.txt')

for line in file:
  line = line.strip()
  
  #Monta url
  sub_to_check = f"https://{line}.{url}"
  try:
      r = requests.get(sub_to_check)
      print("Sucesso")
      print(sub_to_check)
      print("###########")
  except:
    print(f"Não Consegui {sub_to_check}")
    continue

#lista = ["admin", "login", "css", "sport", "css", "mail", "painel"]

#for i in lista:
  #sub_to_check = f"https://{i}.{url}"
  
  #try:
      #r = requests.get(sub_to_check)
      #print("Sucesso")
      #print(sub_to_check)
      #print("###########")
  #except:
    #print(f"Não Consegui {sub_to_check}")
    #continue
  
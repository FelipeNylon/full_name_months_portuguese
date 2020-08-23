import datetime #importando a lib de datas

today = datetime.datetime.now() #instanciando a data atual na variável "today"

mes = today.month  #instanciando o mês atual na variável mês


###### o mes sempre vem como um inteiro, exemplo: 1 = janeiro, 2 = fevereiro. 
###### após a estrutura condicional ele se converterá na string do seu respectivo mês
  if mes == 1:
     mes = str('Janeiro')
  if mes == 2:
      mes = str('Fevereiro')
  if mes == 3:
      mes = str('Março')
  if mes == 4:
      mes = str('Abril')
  if mes == 5:
      mes = str('Maio')
  if mes == 6:
      mes = str('Junho')
  if mes == 7:
      mes = str('Julho')
  if mes == 8:
      mes = str('Agosto')   
  if mes == 9:
      mes = str('Setembro')
  if mes == 10:
      mes = str('Outubro')
  if mes == 11:
      mes = str('Novembro')    
  if mes == 12:
      mes = str('Dezembro')   

print(mes)
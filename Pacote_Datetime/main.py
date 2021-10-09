import datetime

def horario_data_atual():
    agora = datetime.datetime.now() #retorna data e hora atual
    print(agora)
    
    
def hour_construct():
    Time = datetime.time(7, 20, 54) #Constroi a hora, (hora/min/seg)
    print(Time)
    print()
    print(Time.hour) #Mostra somente a hora
    print()
    print(Time.minute) #Mostra somente os minutos
    print()
    print(Time.second) #Mostra somente os segundos
    
    
datetime.time.min #retorna o minuto atual
datetime.date.today() #retorna o dia atual


def Today():
    today = datetime.date.today() #pega o dia e hora atual
    print(today.ctime())#data completa
    print(today.year) #pega o ano atual
    print(today.month) #pega o mes atual
    print(today.day) #pega o dia atual
    

def mudando_data():
    data = datetime.date(2015, 4, 28) # Constroi a data
    print(data)
    data = data.replace(year = 2000) #muda algo, aqui foi o ano
    print(data)
    
    
mudando_data()
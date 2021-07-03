from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
   data_atual = date.today()
   data_atual_sr = data_atual.strftime('%A %B %Y')
   print(data_atual.strftime('%d/%m/%Y'))
   print(data_atual_sr)


def trabalhando_com_time():
    horario = time(hour=10, minute=10, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario.strftime('%H:%M:%S'))
    print(horario_str)


def trabalhando_com_dateTime():
    data_atual = datetime.now()
    #print(data_atual)
    #print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))
    #print(data_atual.strftime('%c'))
    #print(data_atual.weekday())
    data_string = '01/11/2021 11:18:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=365, hours=5)
    print(nova_data)

    dia_da_semana = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo')
    mes_do_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    print(dia_da_semana[data_atual.weekday()], data_atual.day, mes_do_ano[data_atual.month -1], data_atual.year)
    #print(mes_do_ano[data_atual.month -1])

    
    

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_dateTime()
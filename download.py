# from create_contact import collect

# info = collect()
# def writing ():
#     file = 'Phonebook.csv'
#     with open (file, 'a', encoding = 'utf-8') as data:
#         data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def creating_contact ():
    file = 'Phonebook.csv'                                                            # создаем файл с расширение ксв 
    with open (file, 'w', encoding = 'utf-8') as data:                                # открываем файл и записываем в него, стандарт кодирования 
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')
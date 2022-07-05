file = open('C:/Users/anton/Downloads/Чат WhatsApp с Сурок🐉.txt', 'r', encoding='utf-8').read()
file = file.split('\n')
file1 = []
for i in range(len(file)):
    if file[i] != '':
        file1.append(file[i])
b = ' '.join(file)
file = ' '.join(file1).split(' - ')
sleep = ['Спокойн', 'сладк', 'снов', 'ночи', 'сны']
morn = ['Доброе утро', 'утра']

for i in range(len(file)):
    if '.2017,' in file[i] or '.2020,' in file[i] or '.2021,' in file[i] or '.2022,' in file[i]or '.2023,' in file[i] or '.2024,' in file[i]:
        if i == 0:
            file[i] = file[i][18:-18]
        elif i == len(file) - 1:
            pass
        else:
            file[i] = file[i][:-18]
    elif i == len(file) - 1:
        pass
    else:
        file[i + 1] = file[i] + file[i + 1]
dict = {}  # значения - массив со значениями: [Всего сообщений, количество символов, количество пробелов, количество пожеланий спокойной ночи, количество пожеланий доброго утра, количество медиа]
for i in range(len(file)):
    if 'Сообщения и звонки защищены сквозным шифрованием. Третьи лица, включая WhatsApp' not in file[i] and 'Ваш код безопасности с пользователем' not in file[i]:
        # time.sleep(0.2)
        # print(file[i])
        name = file[i].split(': ')[0]
        mes = ': '.join(file[i].split(': ')[1:])
        if mes == '' or name == '':
            continue
        lenght = len(mes)
        spaces = mes.count(' ')
        for j in sleep:
            if j in mes:
                sl = 1
                break
        else:
            sl = 0
        for j in morn:
            if j in mes:
                m = 1
                break
        else:
            m = 0
        med = mes.count('<Без медиафайлов>')
        if name in dict:
            dict[name][0] += 1
            dict[name][1] += lenght
            dict[name][2] += spaces
            dict[name][3] += sl
            dict[name][4] += m
            dict[name][5] += med

        else:
            dict[name] = [0, 0, 0, 0, 0, 0]
            dict[name][0] += 1
            dict[name][1] += lenght
            dict[name][2] += spaces
            dict[name][3] += sl
            dict[name][4] += m
            dict[name][5] += med
print(dict)

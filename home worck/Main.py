books = {
   'Кинг': 'Оно',
   'Лондон': 'Белый клык',
   'Кэрролл': 'Алиса в стране чудес',
   'Линдгрен': 'Карлсон, который живёт на крыше'}


del books['Кинг'] 
books['Дефо'] = 'Приключения Робензона Крузо'
books['Дюма'] = 'Граф Монте-Кристо'
#добавь два наименования
#удали одно наименование

if 'Дефо' in books and 'Дюма' in books:
    print('База обновлена!')
if ('Кинг' in books) == False:
    print('Предпочтения обновлены')
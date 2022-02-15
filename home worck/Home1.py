question = input('Фамилия автора:')
authors = {
    'Пушкин': 'Русский поэт, драматург и прозаик. Один из самых авторитетных литературных деятелей первой трети XIX века',
    'Толстой': 'Один из наиболее известных русских писателей и мыслителей, один из величайших писателей-романистов мира',
    'Бунин': 'Русский писатель, поэт и переводчик, лауреат Нобелевской премии по литературе 1933 года'}
if question in authors:
    print(authors[question])
elif question not in authors:
    answer2 = input('Автор не найлен.Дабавить?')
    if answer2 == 'Да':
        biography = input('Напишите билграфию')
        print('Дабавил!')
        authors[answer2] = biography
        print(authors[answer2])
        if answer2 != 'Нет':
            print('Ответ получен')
print(authors)
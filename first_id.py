def group_count_f_id(n_customers, n_first_id):
    groups_dict = dict() #словарь для хранения кол-ва клиентов по группам
    for id in range(n_first_id, n_first_id + n_customers):
        group = 0
        while id > 0:
            group += id % 10
            id //= 10
        if group in groups_dict.keys():
            groups_dict[group] += 1
        else:
            groups_dict[group] = 1
    return groups_dict


n = int(input('Введите кол-во клиентов: '))
first_id = int(input('Введите первый ID в последовательности: '))

for group in sorted(group_count_f_id(n, first_id).keys()):
    print(f'{group} группа: {group_count_f_id(n, first_id)[group]} клиентов')
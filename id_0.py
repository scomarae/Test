def group_count_0(n_customers):
    groups_dict = dict() #словарь для хранения кол-ва клиентов по группам
    for id in range(n_customers):
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
group_count_0(n)
for group in sorted(group_count_0(n).keys()):
    print(f'{group} группа: {group_count_0(n)[group]} клиентов')

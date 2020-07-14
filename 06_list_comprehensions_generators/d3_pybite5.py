NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    final_list = []
    for name in names:
        if name.title() not in final_list:
            final_list.append(name.title())
    return final_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    desc_names = []
    for name in names:
        f_name, l_name = name.split()
        desc_names.append((f_name, l_name))
    desc_names.sort(key=lambda x: x[1], reverse=True)
    final_list = []
    for name in desc_names:
        final_list.append(f'{name[0]} {name[1]}')
    return final_list


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest_name = (names[0], len(names[0]))
    for name in names:
        if len(name) < shortest_name[1]:
            shortest_name = (name, len(name))
    f_name = shortest_name[0].split()
    return f_name[0]
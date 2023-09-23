import datetime
FORMAT = '%d.%m.%Y'
PREGNANCY_DURATION = datetime.timedelta(weeks = 40)
ECO_DURATION = datetime.timedelta(weeks = 38)
TODAY = datetime.datetime.today().date()

week_names = {
    0: 'недель',
    1: 'неделя',
    2: 'недели',
    3: 'недели',
    4: 'недели',
    5: 'недель',
    6: 'недель',
    7: 'недель',
    8: 'недель',
    9: 'недель',
}
day_names = {
    1: 'день',
    2: 'дня',
    3: 'дня',
    4: 'дня',
    5: 'дней',
    6: 'дней',
}

def get_mode():
    print('[1] По дате последней менструации')
    print('[2] По дате первого УЗИ')
    print('[3] По дате ЭКО')
    mode = input('[1] / [2] / [3]: ')
    if mode != '1' and mode != '2' and mode != '3':
        print('Доступны режимы [1] [2] [3]')
        return get_mode()
    else:
        return int(mode)

def get_mn_date():
    last_mn_input = input('Дата последней менструации (ДД.ММ.ГГГГ): ')
    try:
        last_mn = datetime.datetime.strptime(last_mn_input, FORMAT).date()
        return last_mn
    except:
        print('Неверный формат даты')
        return get_mn_date()
def get_term(mn_day):
    term = datetime.timedelta(days=(TODAY - mn_day).days).days
    return term
def show_term(term_of_pregnant):
    term = f'Срок беременности - '
    weeks = term_of_pregnant // 7
    days = term_of_pregnant % 7
    if weeks != 0:
        week_name = week_names[weeks % 10]
        term += f'{weeks} {week_name}'
    if days != 0:
        day_name = day_names[days % 10]
        if weeks != 0:
            term += f' и {days} {day_name}'
        else:
            term += f'{days} {day_name}'
    print(term)
def get_date(mn_day):
    born_date = (mn_day + PREGNANCY_DURATION)
    return born_date
def show_date(date):
    birth_date = f'Дата родов - {datetime.datetime.strftime(date, FORMAT)}'
    print(birth_date)

def get_uzi_date():
    first_uzi_input = input('Дата УЗИ (ДД.ММ.ГГГГ): ')
    try:
        first_uzi = datetime.datetime.strptime(first_uzi_input, FORMAT).date()
        return first_uzi
    except:
        print('Неверный формат даты')
        return get_uzi_date()
def get_uzi_term():
    uzi_term_input = input('Срок на момент УЗИ (недель дней): ')
    try:
        return [int(i) for i in uzi_term_input.split()]
    except:
        print('Неверный формат')
        return get_uzi_term()
def show_term2(date, term_arr):
    term = f'Срок беременности - '
    time_passed = (TODAY - date).days
    weeks = term_arr[0] + time_passed // 7
    days = term_arr[1] + time_passed % 7
    if weeks != 0:
        week_name = week_names[weeks % 10]
        term += f'{weeks} {week_name}'
    if days != 0:
        day_name = day_names[days % 10]
        if weeks != 0:
            term += f' и {days} {day_name}'
        else:
            term += f'{days} {day_name}'
    print(term)
def get_date2(date, weeks, days):
    total_term = datetime.timedelta(days = days + weeks * 7)
    born_date = (date - total_term + PREGNANCY_DURATION)
    return born_date

def get_eco_date():
    eco_input = input('Дата подсадки (ДД.ММ.ГГГГ): ')
    try:
        date_eco = datetime.datetime.strptime(eco_input, FORMAT).date()
        return date_eco
    except:
        print('Неверный формат даты')
        return get_uzi_date()
def get_embrion_days():
    uzi_term_input = input('Дней эмбриону: ')
    try:
        return int(uzi_term_input)
    except:
        print('Неверный формат')
        return get_uzi_term()
def get_eco_term(date, days):
    term = datetime.timedelta(days = (TODAY - date).days + days).days
    return term
def get_date3(date, days):
    born_date = (date + ECO_DURATION) - datetime.timedelta(days = days)
    return born_date

def do_program():
    mode = get_mode()
    if mode == 1:
        last_mn_day = get_mn_date()
        pregnant_term = get_term(last_mn_day)
        show_term(pregnant_term)
        birth = get_date(last_mn_day)
        show_date(birth)
    elif mode == 2:
        uzi_date = get_uzi_date()
        uzi_term = get_uzi_term()
        show_term2(uzi_date, uzi_term)
        birth = get_date2(uzi_date, uzi_term[0], uzi_term[1])
        show_date(birth)
    elif mode == 3:
        eco_date = get_eco_date()
        days = get_embrion_days()
        term = get_eco_term(eco_date, days)
        birth = get_date3(eco_date, days)
        show_term(term)
        show_date(birth)
do_program()
while True:
    mode = input('[1] Запустить программу ещё раз ')
    if mode == '1':
        do_program()
    else: break
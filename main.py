import datetime

FORMAT = '%d.%m.%Y'
PREGNANCY_DURATION = datetime.timedelta(weeks=40)
IVF_DURATION = datetime.timedelta(weeks=38)
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
    if mode not in ('1', '2', '3'):
        print('Доступны режимы [1] [2] [3]')
        return get_mode()
    else:
        return int(mode)


def get_menstruation_date():
    lm_input = input('Дата последней менструации (ДД.ММ.ГГГГ): ')
    try:
        last_menstruation = datetime.datetime.strptime(lm_input, FORMAT).date()
        return last_menstruation
    except Exception:
        print('Неверный формат даты')
        return get_menstruation_date()


def get_MUS_date():
    first_MUS_input = input('Дата УЗИ (ДД.ММ.ГГГГ): ')
    try:
        first_MUS = datetime.datetime.strptime(first_MUS_input, FORMAT).date()
        return first_MUS
    except Exception:
        print('Неверный формат даты')
        return get_MUS_date()


def get_IVF_date():
    IVF_input = input('Дата подсадки (ДД.ММ.ГГГГ): ')
    try:
        date_IVF = datetime.datetime.strptime(IVF_input, FORMAT).date()
        return date_IVF
    except Exception:
        print('Неверный формат даты')
        return get_MUS_date()


def calculate_term(menstruation_day):
    term = datetime.timedelta(days=(TODAY - menstruation_day).days).days
    return term


def show_term(term_of_pregnant):
    term = 'Срок беременности - '
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


def calculate_date(menstruation_day):
    born_date = (menstruation_day + PREGNANCY_DURATION)
    return born_date


def show_date(date):
    birth_date = f'Дата родов - {datetime.datetime.strftime(date, FORMAT)}'
    print(birth_date)


def get_MUS_term():
    MUS_term_input = input('Срок на момент УЗИ (недель дней): ')
    try:
        return [int(i) for i in MUS_term_input.split()]
    except Exception:
        print('Неверный формат')
        return get_MUS_term()


def show_term_MUS(date, term_arr):
    term = 'Срок беременности - '
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


def calculate_date_MUS(date, weeks, days):
    total_term = datetime.timedelta(days=days + weeks * 7)
    born_date = (date - total_term + PREGNANCY_DURATION)
    return born_date


def get_embrion_days():
    MUS_term_input = input('Дней эмбриону: ')
    try:
        return int(MUS_term_input)
    except Exception:
        print('Неверный формат')
        return get_MUS_term()


def get_IVF_term(date, days):
    term = datetime.timedelta(days=(TODAY - date).days + days).days
    return term


def calculate_date_IVF(date, days):
    born_date = (date + IVF_DURATION) - datetime.timedelta(days=days)
    return born_date


def run_program():
    mode = get_mode()
    if mode == 1:
        last_menstruation_day = get_menstruation_date()
        pregnant_term = calculate_term(last_menstruation_day)
        show_term(pregnant_term)
        birth = calculate_date(last_menstruation_day)
        show_date(birth)
    elif mode == 2:
        MUS_date = get_MUS_date()
        MUS_term = get_MUS_term()
        show_term_MUS(MUS_date, MUS_term)
        birth = calculate_date_MUS(MUS_date, MUS_term[0], MUS_term[1])
        show_date(birth)
    elif mode == 3:
        IVF_date = get_IVF_date()
        days = get_embrion_days()
        term = get_IVF_term(IVF_date, days)
        birth = calculate_date_IVF(IVF_date, days)
        show_term(term)
        show_date(birth)


run_program()

while True:
    mode = input('[1] Запустить программу ещё раз ')
    if mode == '1':
        run_program()
    else:
        break

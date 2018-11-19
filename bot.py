# -*- coding: utf-8 -*-
import config
import telebot
import datetime
from telebot import types
import pytz
import json
import numpy as np
from threading import Thread
import multiprocessing
import time
import psycopg2

bot = telebot.AsyncTeleBot(config.token)


def notify_10_mins(delta):
    database = psycopg2.connect(config.connection_string)
    database_cursor = database.cursor()
    database_cursor.execute('''SELECT id_10,last_notified_10  FROM notifications WHERE id_10 IS NOT NULL''')
    data = database_cursor.fetchall()
    now = int(round(time.time() * 1000))
    print(now)
    id_list = []
    for row in data:
        try:
            print(row)
            user_id = int(row[0])
            bot.send_message(chat_id=user_id, text="До начала урока осталось "+ str(delta) + " минут")
        except Exception as e:
            bot.send_message(chat_id=user_id, text="До начала урока осталось " + str(delta) + " минут")
            pass
    pass


def notify_5_mins(delta):
    database = psycopg2.connect(config.connection_string)
    database_cursor = database.cursor()
    database_cursor.execute('''SELECT id_5,last_notified_5  FROM notifications WHERE id_5 IS NOT NULL''')
    data = database_cursor.fetchall()
    now = int(round(time.time() * 1000))
    print(now)
    id_list = []
    for row in data:
        try:
            print(row)
            user_id = int(row[0])
            bot.send_message(chat_id=user_id, text="До начала урока осталось " + str(delta) + " минут")
        except Exception as e:
            print(e)
            pass
    pass
    pass


def check_deadlines(times):
        msg = "s is running"
        print(msg)
        fmt = '%H:%M:%S'
        while True:
            dt_now = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
            time_moscow = datetime.datetime.strptime(
                str(dt_now.hour) + ":" + str(dt_now.minute) + ":" + str(dt_now.second),
                fmt)

            for some_time in times:
                delta = ((some_time.hour*3600) + (some_time.minute * 60) + some_time.second) - ((time_moscow.hour*3600) +
                                                                                                (time_moscow.minute*60) +
                                                                                                time_moscow.second)
                delta /= 60
                print(delta)
                if 5 < delta <= 10:
                    notify_10_mins(delta)
                    print("sleepin 5 min")
                    time.sleep(300)
                elif 0 < delta <= 5:
                    notify_5_mins(delta)
                    print("sleep for 30 min")

                    time.sleep(1800)
                else:
                    print("nothing")
                    time.sleep(0.2)


def get_data_from_db(user_id, get_exist, get_group, get_hasdeadlines, get_condition_db):
    database_cursor = psycopg2.connect(config.connection_string).cursor()
    if get_exist and not get_hasdeadlines and not get_condition_db:
        try:
            database_cursor.execute('''SELECT * FROM ''' + config.users_table + ''' WHERE id = ''' + str(user_id))
            print(str(database_cursor.fetchone()[0]))
            return True
        except Exception:
            return False
    if get_condition_db:
        database_cursor.execute('''SELECT condition FROM users_table WHERE id = ''' + str(user_id))
        return str(database_cursor.fetchone()[0])

    if get_hasdeadlines and get_condition_db:
        try:
            database_cursor.execute('''SELECT hasDeadlines AND condition WHERE id = ''' + str(user_id))
        except Exception:
            return None
    if get_group:
        try:
            database_cursor.execute('''SELECT user_group FROM users_table WHERE id = ''' + str(user_id))
            return str(database_cursor.fetchone()[0])
        except Exception:
            return -1


def show_deadlines(user_id):
    database_cursor = psycopg2.connect(config.connection_string).cursor()
    try:
        reply = database_cursor.execute('SELECT * FROM DEADLINES_TABLE WHERE id = ' + str(id))
        all_rows = reply.fetchall()
        print('1):', all_rows)
    except Exception as e:
        print(e)
        bot.send_message(user_id, "Не удалось ничего найти")


def throw_deadline_choice(message):
    button1 = types.InlineKeyboardButton(text="Единичное уведомление ⚡", callback_data="deadline_once")
    button2 = types.InlineKeyboardButton(text="Циклическое напоминание 📅", callback_data="deadline_circular")
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(button1, button2)
    bot.send_message(chat_id=message.chat.id, text="Выберите тип уведомления", reply_markup=keyboard)
    pass


def add_deadline(message):
    user_id = message.chat.id
    deadline_string = message.text
    try:
        fmt = '%d/%m/%Y %H:%M:%S'
        deadline_date = datetime.datetime.strptime(deadline_string, fmt)
    except Exception as e:
        print(e)
        try:
            fmt = '%H:%M:%S'
            deadline_date = datetime.datetime.strptime(deadline_string, fmt)
        except Exception as e:
            print(e)
            bot.send_message(chat_id=message.chat.id, text="Введенная дата не соответствует формату")
            return
    database = psycopg2.connect(config.connection_string)
    cursor = database.cursor()
    cursor.execute('''INSERT INTO deadlines_table (id, deadline_string)\n VALUES(''' + str(user_id) + ''', "''' + str(
        deadline_date) + '''");
    ''')
    database.commit()
    change_condition_bd("deadline process", message.chat.id)
    throw_deadline_choice(message)
    pass


def send_formula_image(call):
    global timetable_photo
    user_id = call.message.chat.id
    image_str = call.data
    if image_str == "kpv":
        timetable_photo = open(config.kvp, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "elasticity":
        timetable_photo = open(config.elasticity, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "markets":
        timetable_photo = open(config.markets, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "production_and_costs":
        timetable_photo = open(config.production_and_costs, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "unemployment":
        timetable_photo = open(config.unemployment, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "inflation":
        timetable_photo = open(config.inflation, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "gdp":
        timetable_photo = open(config.GDP, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "gini":
        timetable_photo = open(config.gini, 'rb')
        bot.send_photo(user_id, timetable_photo)
    elif image_str == "economicgrowth":
        timetable_photo = open(config.economicgrowth, 'rb')
        bot.send_photo(user_id, timetable_photo)


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


def send_time_before_break(user_id):
    times = {
        datetime.datetime.strptime("9:00:00", '%H:%M:%S'),
        datetime.datetime.strptime("9:40:00", '%H:%M:%S'),
        datetime.datetime.strptime("9:45:00", '%H:%M:%S'),
        datetime.datetime.strptime("10:25:00", '%H:%M:%S'),
        datetime.datetime.strptime("10:45:00", '%H:%M:%S'),
        datetime.datetime.strptime("11:25:00", '%H:%M:%S'),
        datetime.datetime.strptime("11:30:00", '%H:%M:%S'),
        datetime.datetime.strptime("12:10:00", '%H:%M:%S'),
        datetime.datetime.strptime("12:20:00", '%H:%M:%S'),
        datetime.datetime.strptime("13:00:00", '%H:%M:%S'),
        datetime.datetime.strptime("13:05:00", '%H:%M:%S'),
        datetime.datetime.strptime("13:45:00", '%H:%M:%S'),
        datetime.datetime.strptime("14:45:00", '%H:%M:%S'),
        datetime.datetime.strptime("15:25:00", '%H:%M:%S'),
        datetime.datetime.strptime("15:30:00", '%H:%M:%S'),
        datetime.datetime.strptime("16:10:00", '%H:%M:%S'),
        datetime.datetime.strptime("16:20:00", '%H:%M:%S'),
        datetime.datetime.strptime("17:00:00", '%H:%M:%S'),
        datetime.datetime.strptime("17:05:00", '%H:%M:%S'),
        datetime.datetime.strptime("17:45:00", '%H:%M:%S')
    }
    dt_now = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
    fmt = '%H:%M:%S'
    time_moscow = datetime.datetime.strptime(str(dt_now.hour) + ":" + str(dt_now.minute) + ":" + str(dt_now.second),
                                             fmt)
    max_minus_delta = datetime.timedelta(days=-1, minutes=0, hours=0, seconds=0)
    max_delta = datetime.timedelta(hours=23, minutes=59, seconds=59)
    time_delta = datetime.timedelta(hours=23, minutes=59, seconds=59)
    for tim in times:
        if tim - time_moscow < max_delta and not (tim - time_moscow).days == -1:
            max_delta = tim - time_moscow
        if tim - time_moscow > max_minus_delta and (tim - time_moscow).days == -1:
            max_minus_delta = tim - time_moscow
    max_minus_delta += datetime.timedelta(days=1)
    max_minus_delta = datetime.timedelta(days=1) - max_minus_delta
    if max_delta + max_minus_delta == datetime.timedelta(minutes=40):
        response_message = "До конца урока осталось " + str(max_delta)
    elif max_delta == time_delta:
        answer = datetime.datetime.strptime("9:00:00", '%H:%M:%S') - time_moscow
        response_message = (strfdelta(answer, "До первого урока осталось {hours} часов {minutes} минут "))
    else:
        response_message = "До следующего урока осталось: " + str(max_delta)
    bot.send_message(user_id, response_message)
    pass


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, 'Для начала нужно настроить бота! \n '
                                      '\n Введите вашу группу \n Пример: 10МЭ1',
                     reply_markup=markup)
    change_condition_bd("setting_bot", message.chat.id)


def add_user_to_db(id_):
    db = psycopg2.connect(config.connection_string)
    database_cursor = db.cursor()
    database_cursor.execute('''INSERT INTO users_table (id, condition)\n VALUES(''' + str(id_) +
                            ''', 'get_group');''')
    db.commit()
    pass


def add_user_group_bd(message):
    db = psycopg2.connect(config.connection_string)
    database_cursor = db.cursor()
    database_cursor.execute('''UPDATE users_table SET user_group = \'''' + message.text + '''\' WHERE id = ''' +
                            str(message.chat.id))
    db.commit()
    pass


def change_condition_bd(new_condition, user_id):
    db = psycopg2.connect(config.connection_string)
    database_cursor = db.cursor()
    database_cursor.execute('''UPDATE users_table SET condition = \'''' + new_condition + '''\' WHERE id = ''' +
                            str(user_id))
    db.commit()
    pass


def send_user_group(message):
    user_id = message.chat.id
    seeked_user = message.text
    seeked_group = ""
    json_file = open('students.json', mode='r', encoding='UTF-8')
    json_students = json.load(json_file)
    for group, students in json_students.items():
        for student in students:
            if seeked_user.strip() == student.strip():
                seeked_group = group
    if not seeked_group == "":
        bot.send_message(chat_id=user_id, text="Ученик/ца " + seeked_user + " обучается в группе " + seeked_group)
    else:
        bot.send_message(chat_id=user_id, text="Данные об указанном ученике не найдены")
    pass


def send_marks(message):
    input_string = message.text
    weights = config.marks_weight
    subject = input_string.split(',')[0].strip()
    k_mark_koef = 0.0
    f_mark_koef = 0.0
    t_mark_koef = 0.0
    for key, value in weights.items():
        if subject in key:
            k_mark_koef = value[0]
            f_mark_koef = value[1]
            t_mark_koef = value[2]
    marks_k = []
    for num in input_string.split(",")[1].strip().split(" "):
        marks_k.append(float(num))
    marks_f = []
    for num in input_string.split(',')[2].strip().split(" "):
        marks_f.append(float(num))
    marks_t = []
    for num in input_string.split(',')[3].strip().split(" "):
        marks_t.append(float(num))
    seeked_mark = float(input_string.split(',')[4])
    average = round(np.mean(marks_k) * k_mark_koef + np.mean(marks_f) * f_mark_koef + np.mean(marks_t) * t_mark_koef, 2)
    bot.send_message(chat_id=message.chat.id, text="Ваш средний балл равен " + str(average))
    difference = round(seeked_mark - average, 2)
    print(difference)
    if difference <= 0:
        bot.send_message(chat_id=message.chat.id, text="Ваш средний бал выше или равен желаемому")
    else:
        koeffs = [k_mark_koef, f_mark_koef, t_mark_koef]
        marks = [marks_k, marks_f, marks_t]
        answers = []
        for index, koeff in enumerate(koeffs):
            n = len(marks[index])
            s2 = difference / koeff + np.mean(marks[index])
            s1 = np.mean(marks[index])
            if s2 >= 5:
                answers.append(0.0)
                pass
            else:
                k = (n * (s2 - s1)) / (5 - s2)
                answers.append(round(k + 0.5))
        answer_string = "Для желаемого балла вам нужно получить \n"
        if answers[0] > 0 and answers[1] > 0 and answers[2] > 0:
            answer_string += str(int(answers[0])) + "  Констатирующих '5' или \n"
            answer_string += str(int(answers[1])) + "  Формирующих '5' или \n"
            answer_string += str(int(answers[2])) + "  Творческих '5'"
        elif answers[0] > 0 >= answers[2] and answers[1] > 0:
            answer_string += str(int(answers[0])) + "  Констатирующих '5' или \n"
            answer_string += str(int(answers[1])) + "  Формирующих '5'"
        elif answers[0] <= 0 < answers[1] and answers[2] > 0:
            answer_string += str(int(answers[1])) + "  Формирующих '5' или \n"
            answer_string += str(int(answers[2])) + "  Творческих '5'"
        elif answers[0] > 0 >= answers[1] and answers[2] > 0:
            answer_string += str(int(answers[0])) + "  Констатирующих '5' или \n"
            answer_string += str(int(answers[2])) + "  Творческих '5'"
        elif answers[0] > 0 >= answers[2] and answers[1] <= 0:
            answer_string += str(int(answers[0])) + "  Констатирующих '5'"
        elif answers[0] <= 0 < answers[1] and answers[2] <= 0:
            answer_string += str(int(answers[1])) + "  Формирующих '5'"
        elif answers[0] <= 0 and answers[1] <= 0 < answers[2]:
            answer_string += str(int(answers[2])) + "  Творческих '5'"
        elif answers[0] == 0 and answers[1] == 0 and answers[2] == 0:
            answer_string = "К сожалению, бот не нашел пути достижения желаемого балла"

        bot.send_message(chat_id=message.chat.id, text=answer_string)
    pass


@bot.message_handler(content_types=["text"])
def any_message(message):
    user_condition = " "
    id_exists = get_data_from_db(message.chat.id, True, False, False, False)
    print(id_exists)
    if not id_exists:
        add_user_to_db(message.chat.id)
        if str(message.text) in config.groups:
            add_user_group_bd(message)
            change_condition_bd("empty", message.chat.id)
            bot.send_message(message.chat.id, "Группа добавлена в базу данных!")
        else:
            print(str(message.text))
            print(message.text in config.groups)
            bot.send_message(message.chat.id, "Введите вашу группу \n Например: 10МЭ3")
    else:
        user_condition = get_data_from_db(message.chat.id, get_exist=False, get_group=False, get_hasdeadlines=False,
                                          get_condition_db=True)
    if user_condition == "adding_deadline":
        add_deadline(message)
        change_condition_bd("empty", message.chat.id)
    elif user_condition == "get_group" or not user_has_group(message.chat.id):
        if str(message.text) in config.groups:
            add_user_group_bd(message)
            change_condition_bd("empty", message.chat.id)
            bot.send_message(message.chat.id, "Группа добавлена в базу данных!")
        else:
            print(str(message.text))
            print(message.text in config.groups)
            bot.send_message(message.chat.id, "Введите вашу группу \n Например: 10МЭ3")

    elif user_condition == "group_number_w":
        send_timetable_photo(message)
        change_condition_bd("empty", message.chat.id)
    elif user_condition == "searching_user":
        send_user_group(message)
        change_condition_bd("empty", message.chat.id)

    elif user_condition == "deadline process":
        if message.text == "Циклическое напоминание 📅":
            set_deadline_type(message.chat.id, "circular")
        elif message.text == "Единичное уведомление ⚡":
            set_deadline_type(message.chat.id, "once")

    elif user_condition == "searching_teacher":
        send_teacher_info_photo(message)
        change_condition_bd("empty", message.chat.id)

    elif user_condition == "marks":
        send_marks(message)
        change_condition_bd("empty", message.chat.id)

    else:
        keyboard_start = types.InlineKeyboardMarkup()
        callback_button_start = types.InlineKeyboardButton(text="Начать", callback_data="start")
        keyboard_start.add(callback_button_start)
        bot.send_message(message.chat.id, text="Здравствуй, я твой бот-помощник в лицее", reply_markup=keyboard_start)
    print(user_condition)


def show_start_keyboard(user_id):
    cb_btn_deadline_notif = types.InlineKeyboardButton(text="Оповещение о дедлайнах",
                                                       callback_data="notificationDeadline")
    cb_btn_lessons_notif = types.InlineKeyboardButton(text="Оповещение о начале пар",
                                                      callback_data="notificationLesson")
    cb_btn_useful_links = types.InlineKeyboardButton(text="Выдача полезных ссылок", callback_data="links")
    cb_btn_formulas = types.InlineKeyboardButton(text="Выдача экономических формул", callback_data="formulas")
    cb_btn_marks = types.InlineKeyboardButton(text="Выдача нужных оценок", callback_data="marks")
    cb_btn_timetobell = types.InlineKeyboardButton(text="Выдача оставшегося времени до пары",
                                                   callback_data="time")
    cb_btn_teachers_info = types.InlineKeyboardButton(text="Выдача информации об учителей",
                                                      callback_data="teachersInfo")
    cb_btn_student_info = types.InlineKeyboardButton(text="Выдача информации об учениках",
                                                     callback_data="studentsInfo")
    cb_btn_timetable = types.InlineKeyboardButton(text="Выдача расписания", callback_data="timetable")
    keyboard_functional = types.InlineKeyboardMarkup()
    keyboard_functional.row_width = 1
    keyboard_functional.add(cb_btn_deadline_notif, cb_btn_lessons_notif, cb_btn_useful_links, cb_btn_formulas,
                            cb_btn_marks, cb_btn_timetobell, cb_btn_teachers_info, cb_btn_student_info,
                            cb_btn_timetable)
    bot.send_message(chat_id=user_id, text="Вот тебе мои функции:",
                     reply_markup=keyboard_functional, )
    pass


def send_notification_keyboard(user_id):
    cb_btn_5minute = types.InlineKeyboardButton(text="За 5 минут до урока", callback_data="5minute")
    cb_btn_10minute = types.InlineKeyboardButton(text="За 10 минут до урока", callback_data="10minute")
    cb_btn_delete = types.InlineKeyboardButton(text="Остановить напоминания", callback_data="delete_notifications")

    keyboard_notifications = types.InlineKeyboardMarkup()
    keyboard_notifications.row_width = 1
    keyboard_notifications.add(cb_btn_5minute, cb_btn_10minute, cb_btn_delete)
    bot.send_message(chat_id=user_id, text="Выберите режим", reply_markup=keyboard_notifications)


def add_user_notifications(user_id, minutes):
    db_ = psycopg2.connect(config.connection_string)
    cursor = db_.cursor()
    if minutes == 5:
        cursor.execute('''INSERT INTO ''' + config.notifications_table + ''' (id_5)\n VALUES(''' +
                       str(user_id) + ''');''')
    elif minutes == 10:
        cursor.execute('''INSERT INTO ''' + config.notifications_table + ''' (id_10)\n VALUES(''' +
                       str(user_id) + ''');''')
    db_.commit()
    pass


def delete_user_notifications(user_id):
    db_ = psycopg2.connect(config.connection_string)
    cursor = db_.cursor()
    cursor.execute('''DELETE FROM ''' + config.notifications_table + ''' WHERE id_5 = '''+str(user_id) +
                   ''' or id_10 = '''+str(user_id))
    db_.commit()
    bot.send_message(chat_id=user_id, text="Уведомления приостановлены")


def show_subjects_keyboard(user_id):
    cb_btn_maths = types.InlineKeyboardButton(text="Математика", callback_data="maths")
    cb_btn_russian = types.InlineKeyboardButton(text="Русский язык", callback_data="russian")
    cb_btn_literature = types.InlineKeyboardButton(text="Литература", callback_data="literature")
    cb_btn_english = types.InlineKeyboardButton(text="Английский язык", callback_data="english")
    cb_btn_sociology = types.InlineKeyboardButton(text="Обществознание", callback_data="sociology")
    cb_btn_tok = types.InlineKeyboardButton(text="ТОК", callback_data="TOK")
    cb_btn_physics = types.InlineKeyboardButton(text="Физика", callback_data="physics")
    cb_btn_history = types.InlineKeyboardButton(text="История", callback_data="history")
    cb_btn_economics = types.InlineKeyboardButton(text="Экономика", callback_data="economics")
    cb_btn_historyofeconomics = types.InlineKeyboardButton(text="ИЭиЭМ", callback_data="historyofeconomics")
    cb_btn_psychology = types.InlineKeyboardButton(text="Психология", callback_data="psychology")
    cb_btn_geography = types.InlineKeyboardButton(text="География", callback_data="geography")
    cb_btn_business = types.InlineKeyboardButton(text="Бизнес", callback_data="business")
    cb_btn_it = types.InlineKeyboardButton(text="Информатика", callback_data="IT")
    cb_btn_pe = types.InlineKeyboardButton(text="Физическая культура", callback_data="PE")
    cb_btn_biology = types.InlineKeyboardButton(text="Биология", callback_data="biology")
    cb_btn_chemistry = types.InlineKeyboardButton(text="Химия", callback_data="chemistry")
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")

    keyboard_subjects = types.InlineKeyboardMarkup()
    keyboard_subjects.row_width = 1
    keyboard_subjects.add(cb_btn_maths, cb_btn_russian, cb_btn_literature, cb_btn_english, cb_btn_sociology, cb_btn_tok,
                          cb_btn_physics, cb_btn_history, cb_btn_economics, cb_btn_historyofeconomics,
                          cb_btn_psychology, cb_btn_geography, cb_btn_business, cb_btn_it, cb_btn_biology,
                          cb_btn_chemistry, cb_btn_pe, cb_btn_cancel)
    bot.send_message(chat_id=user_id, text="Выбери нужный предмет",
                     reply_markup=keyboard_subjects)
    pass


def show_formulas_keyboard(user_id):
    cb_btn_f_kpv = types.InlineKeyboardButton(text="КПВ", callback_data="kpv")
    cb_btn_f_gini = types.InlineKeyboardButton(text="Джини", callback_data="gini")
    cb_btn_f_gdp = types.InlineKeyboardButton(text="ВВП", callback_data="gdp")
    cb_btn_f_elasticity = types.InlineKeyboardButton(text="Эластичность", callback_data="elasticity")
    cb_btn_f_proizvodstvo = types.InlineKeyboardButton(text="Производство и издержки",
                                                       callback_data="production_and_costs")
    cb_btn_f_markets = types.InlineKeyboardButton(text="Рыночные струкутуры", callback_data="markets")
    cb_btn_f_unemployment = types.InlineKeyboardButton(text="Безработица", callback_data="unemployment")
    cb_btn_f_inflation = types.InlineKeyboardButton(text="Инфляция", callback_data="inflation")
    cb_btn_f_economicgrowth = types.InlineKeyboardButton(text="Экономический рост", callback_data="economicgrowth")

    keyboard_formulas = types.InlineKeyboardMarkup()
    keyboard_formulas.row_width = 2
    keyboard_formulas.add(cb_btn_f_kpv, cb_btn_f_gini, cb_btn_f_gdp, cb_btn_f_elasticity,
                          cb_btn_f_proizvodstvo, cb_btn_f_markets, cb_btn_f_unemployment,
                          cb_btn_f_economicgrowth, cb_btn_f_inflation)
    bot.send_message(chat_id=user_id, text="Выбери нужную тему", reply_markup=keyboard_formulas)
    pass


def show_deadline_menu(user_id):
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    cb_btn_my_deadlines = types.InlineKeyboardButton(text="Показать мои дэдлайны", callback_data="show_deadlines")
    cb_btn_add_deadline = types.InlineKeyboardButton(text="Добавить дэдлайн", callback_data="add_deadline")

    keyboard_deadline = types.InlineKeyboardMarkup()
    keyboard_deadline.row_width = 1
    keyboard_deadline.add(cb_btn_my_deadlines, cb_btn_add_deadline, cb_btn_cancel)
    bot.send_message(chat_id=user_id, text="Меню установки Дэдлайнов",
                     reply_markup=keyboard_deadline)
    pass


def get_cancel_keyboard():
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(cb_btn_cancel)
    return keyboard


def send_teacher_info_photo(message):
    text = message.text
    user_id = message.chat.id
    photo_path = ''
    try:
        for teacher, path in config.teachers.items():
            if teacher.strip() == text.strip():
                photo_path = path
        photo_file = open(photo_path, 'rb')
        bot.send_photo(user_id, photo_file, "Информация об учителе")
    except Exception as e:
        print(str(e))
        bot.send_message(chat_id=user_id, text="Учитель не найден")


def send_timetable_photo(message):
    group = message.text
    user_id = message.chat.id
    global photo
    try:
        if group == "10МЭ1":
            photo = open(config._10me1, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "10МЭ2":
            photo = open(config._10me2, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "10МЭ3":
            photo = open(config._10me3, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "10МЭ4":
            photo = open(config._10me4, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "10МЭ5":
            photo = open(config._10me5, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "10МЭ6":
            photo = open(config._10me6, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "11МЭ1":
            photo = open(config._11me1, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "11МЭ2":
            photo = open(config._11me2, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "11МЭ3":
            photo = open(config._11me3, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "11МЭ4":
            photo = open(config._11me4, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "11МЭ5":
            photo = open(config._11me5, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        elif group == "11МЭ6":
            photo = open(config._11me6, 'rb')
            bot.send_photo(user_id, photo, "Расписание на неделю")
        else:
            bot.send_message(user_id, "Расписание введенной группы отсутствует")
    except Exception as e:
        print(e)
        bot.send_message(chat_id=user_id, text="Группа введена неверно. Пример: 10МЭ3")
    pass


def get_user_group(user_id):
    try:
        db_ = psycopg2.connect(config.connection_string)
        cursor = db_.cursor()
        cursor.execute('''SELECT user_group FROM users_table WHERE id = ''' + str(user_id))
        group = cursor.fetchone()
        return group[0]
    except Exception as e:
        print(e)
        return "null"
    pass


def get_current_weekday():
    dt = datetime.datetime.weekday(datetime.datetime.now())
    if dt == 0:
        return 'monday'
    elif dt == 1:
        return 'tuesday'
    elif dt == 2:
        return 'wednesday'
    elif dt == 3:
        return 'thursday'
    elif dt == 4:
        return 'friday'
    elif dt == 5:
        return 'saturday'
    elif dt == 6:
        return 'sunday'
    else:
        return 'unexpected error'
    pass


def get_timetable_text(user_id):
    result_string = []
    user_weekday = get_current_weekday()
    user_group = get_user_group(user_id)
    json_file = open('timetable.json', 'r', encoding='UTF-8')
    json_timetable = json.load(json_file)
    today_table = json_timetable.get('timetable').pop(0).get(str(user_group)).pop(0).get(user_weekday)
    try:
        for tt in today_table:
            result_string.append(tt)
            result_string.append('\n')
        message = ''.join(result_string)
    except Exception as e:
        print(e)
        message = "Расписание на данный день отсутствует"
    return message
    pass


def set_deadline_type(user_id, param):
    database = psycopg2.connect(config.connection_string)
    database_cursor = database.cursor()
    if param == "once":
        database_cursor.execute('''UPDATE deadlines_table SET circular = "once" WHERE id = ''' + str(user_id) +
                                ''' AND circular = "empty"''')
    elif param == "circular":
        database_cursor.execute('''UPDATE deadlines_table SET circular = "circular" WHERE id = ''' + str(user_id) +
                                ''' AND circular = "empty"''')
    database.commit()
    pass


def user_has_group(user_id):
    try:
        database = psycopg2.connect(config.connection_string)
        database_cursor = database.cursor()
        database_cursor.execute('''SELECT user_group FROM users_table WHERE id = ''' + str(user_id))
        group = database_cursor.fetchone()[0]
        print("Group is " + str(group))
        if group == "" or group is None:
            return False
        else:
            return True
    except Exception as e:
        print(e)
        return False
    pass


@bot.callback_query_handler(func=lambda call: True)
def functions(call):
    if call.message:
        if user_has_group(call.message.chat.id):
            if call.data == "start":
                show_start_keyboard(call.message.chat.id)

            elif call.data == "maths":
                bot.send_message(call.message.chat.id, config.maths)

            elif call.data == "russian":
                bot.send_message(call.message.chat.id, config.russian)

            elif call.data == "literature":
                bot.send_message(call.message.chat.id, config.literature)

            elif call.data == "english":
                bot.send_message(call.message.chat.id, config.english)

            elif call.data == "sociology":
                bot.send_message(call.message.chat.id, config.sociology)

            elif call.data == "TOK":
                bot.send_message(call.message.chat.id, config.TOK)

            elif call.data == "physics":
                bot.send_message(call.message.chat.id, config.physics)

            elif call.data == "history":
                bot.send_message(call.message.chat.id, config.history)

            elif call.data == "economics":
                bot.send_message(call.message.chat.id, config.economics)

            elif call.data == "historyofeconomics":
                bot.send_message(call.message.chat.id, config.historyofeconomics)

            elif call.data == "psychology":
                bot.send_message(call.message.chat.id, config.psychology)

            elif call.data == "geography":
                bot.send_message(call.message.chat.id, config.geography)

            elif call.data == "business":
                bot.send_message(call.message.chat.id, config.business)

            elif call.data == "IT":
                bot.send_message(call.message.chat.id, config.IT)

            elif call.data == "PE":
                bot.send_message(call.message.chat.id, config.PE)

            elif call.data == "biology":
                bot.send_message(call.message.chat.id, config.biology)

            elif call.data == "chemistry":
                bot.send_message(call.message.chat.id, config.chemistry)

            elif call.data == "notificationLesson":
                send_notification_keyboard(call.message.chat.id)

            elif call.data == "delete_notifications":
                delete_user_notifications(call.message.chat.id)

            elif call.data == "5minute":
                add_user_notifications(call.message.chat.id, 5)

            elif call.data == "10minute":
                add_user_notifications(call.message.chat.id, 10)

            elif call.data == "studentsInfo":
                markup = types.ForceReply(selective=True)
                bot.send_message(call.message.chat.id, "Теперь введите имя ученика",
                                 reply_markup=markup)
                change_condition_bd("searching_user", user_id=call.message.chat.id)
                bot.send_message(chat_id=call.message.chat.id, text="Вернуться в главное меню",
                                 reply_markup=get_cancel_keyboard())

            elif call.data == "teachersInfo":
                change_condition_bd("searching_teacher", call.message.chat.id)
                show_subjects_keyboard(call.message.chat.id)

            elif call.data == "formulas":
                show_formulas_keyboard(call.message.chat.id)

            elif call.data == "notificationDeadline":
                show_deadline_menu(call.message.chat.id)

            elif call.data == "show_deadlines":
                show_deadlines(call.message.chat.id)

            elif call.data == "cancel":
                bot.send_message(chat_id=call.message.chat.id, text="Отмена", reply_markup=types.ReplyKeyboardRemove(),
                                 parse_mode='HTML', disable_web_page_preview=True)
                show_start_keyboard(call.message.chat.id)
                change_condition_bd("empty", call.message.chat.id)

            elif call.data == "add_deadline":
                markup = types.ForceReply(selective=True)
                bot.send_message(call.message.chat.id, "Введите дату и время дэдлайна в формате dd/mm/yyyy hh.mm.ss или"
                                 + " hh.mm.ss для одноразового напоминания",
                                 reply_markup=markup)
                cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(cb_btn_cancel)
                bot.send_message(call.message.chat.id, reply_markup=keyboard, text="Отменить настройку дэдлайна")
                change_condition_bd("adding_deadline", call.message.chat.id)

            elif call.data == "deadline_circular":
                set_deadline_type(call.message.chat.id, "circular")

            elif call.data == "deadline_once":
                set_deadline_type(call.message.chat.id, "once")

            elif call.data == "time":
                send_time_before_break(call.message.chat.id)

            elif call.data == "links":
                bot.send_message(call.message.chat.id, config.links)

            elif call.data == "marks":
                change_condition_bd("marks", call.message.chat.id)
                bot.send_message(chat_id=call.message.chat.id, text="Введите данные в следующем формате: 'Предмет, "
                                                                    "констатирующие. формирующие, творческие оценки,"
                                                                    " желаемый балл ' ",
                                 reply_markup=get_cancel_keyboard())

            elif call.data == "timetable":
                cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
                cb_btn_daylytimetable = types.InlineKeyboardButton(text="На день",
                                                                   callback_data="daylytimetable")
                cb_btn_weeklytimetable = types.InlineKeyboardButton(text="На неделю",
                                                                    callback_data="weeklytimetable")
                keyboard_timetable = types.InlineKeyboardMarkup()
                keyboard_timetable.add(cb_btn_weeklytimetable, cb_btn_daylytimetable, cb_btn_cancel)
                bot.send_message(chat_id=call.message.chat.id, text="Расписание", reply_markup=keyboard_timetable)

            elif call.data == "weeklytimetable":
                markup = types.ForceReply(selective=False)
                bot.send_message(call.message.chat.id, "Введите группу ",
                                 reply_markup=markup)
                change_condition_bd("group_number_w", call.message.chat.id)

            elif call.data == "daylytimetable":
                bot.send_message(chat_id=call.message.chat.id, text=get_timetable_text(call.message.chat.id))

            elif call.data == "economicgrowth" or "inflation" or "unemployment" or "markets" or "production_and_costs" \
                    or "kvp" or "gini" or "gdp" or "elasticity":
                send_formula_image(call)
            else:
                bot.send_message(call.message.chat.id, "Error")

        else:
            if str(call.message.text) in config.groups:
                add_user_group_bd(call.message)
                change_condition_bd("empty", call.message.chat.id)
                bot.send_message(call.message.chat.id, "Группа добавлена в базу данных!")
            else:
                print(str(call.message.text))
                print(call.message.text in config.groups)
                bot.send_message(call.message.chat.id, "Введите вашу группу \n Например: 10МЭ2")


def get_condition(user_id):
    database = psycopg2.connect(config.connection_string)
    database_cursor = database.cursor()
    database_cursor.execute('''SELECT condition FROM users_table WHERE id = ''' + str(user_id))
    return str(database_cursor.fetchone()[0])


def create_db():
    database = psycopg2.connect(config.connection_string)
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ''' + config.users_table + '''
                    (id bigint, user_group TEXT ,has_deadlines BOOLEAN, condition TEXT)
    ''')
    database.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ''' + config.deadlines_table + '''
                    (id bigint, deadline_string TEXT, circular TEXT, frequency TEXT)
    ''')
    database.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ''' + config.notifications_table + '''
                    (id_5 bigint, last_notified_5 TEXT, id_10 bigint, last_notified_10 TEXT)
    ''')
    database.commit()


if __name__ == '__main__':
    create_db()
    bot.polling(none_stop=True, timeout=5)

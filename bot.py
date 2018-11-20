# -*- coding: utf-8 -*-
import config
import telebot
import datetime
from telebot import types
import pytz
import json
import numpy as np
import time
import psycopg2
import keyboards as kb
import db_operations as db

bot = telebot.AsyncTeleBot(config.token)


@bot.message_handler(content_types=["text"])
def any_message(message):
    user_condition = " "
    id_exists = db.get_data_from_db(message.chat.id, True, False, False, False)
    print(id_exists)
    if not id_exists:
        db.add_user_to_db(message.chat.id)
        if str(message.text) in config.groups:
            db.add_user_group_bd(message)
            db.change_condition_bd("empty", message.chat.id)
            bot.send_message(message.chat.id, "Группа добавлена в базу данных!")
        else:
            print(str(message.text))
            print(message.text in config.groups)
            bot.send_message(message.chat.id, "Введите вашу группу \n Например: 10МЭ3")
    else:
        user_condition = db.get_data_from_db(message.chat.id, get_exist=False, get_group=False, get_hasdeadlines=False,
                                             get_condition_from_db=True)
    if user_condition == "adding_deadline":
        add_deadline(message)
        db.change_condition_bd("empty", message.chat.id)
    elif user_condition == "get_group" or not db.user_has_group_db(message.chat.id):
        if str(message.text) in config.groups:
            db.add_user_group_bd(message)
            db.change_condition_bd("empty", message.chat.id)
            bot.send_message(message.chat.id, "Группа добавлена в базу данных!")
        else:
            print(str(message.text))
            print(message.text in config.groups)
            bot.send_message(message.chat.id, "Введите вашу группу \n Например: 10МЭ3")

    elif user_condition == "group_number_w":
        send_timetable_photo(message)
        db.change_condition_bd("empty", message.chat.id)
    elif user_condition == "searching_user":
        send_user_group(message)
        db.change_condition_bd("empty", message.chat.id)

    elif user_condition == "deadline process":
        if message.text == "Циклическое напоминание 📅":
            db.set_deadline_type(message.chat.id, "circular")
        elif message.text == "Единичное уведомление ⚡":
            db.set_deadline_type(message.chat.id, "once")

    elif user_condition == "searching_teacher":
        send_teacher_info_photo(message)
        db.change_condition_bd("empty", message.chat.id)

    elif user_condition == "marks":
        send_marks(message)
        db.change_condition_bd("empty", message.chat.id)

    else:
        keyboard_start = types.InlineKeyboardMarkup()
        callback_button_start = types.InlineKeyboardButton(text="Начать", callback_data="start")
        keyboard_start.add(callback_button_start)
        bot.send_message(message.chat.id, text="Здравствуй, я твой бот-помощник в лицее", reply_markup=keyboard_start)
    print(user_condition)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    markup = types.ForceReply(selective=False)
    if not db.user_has_group_db(user_id):
        bot.send_message(user_id, 'Для начала нужно настроить бота! \n '
                                  '\n Введите вашу группу \n Пример: 10МЭ1',
                         reply_markup=markup)
        db.change_condition_bd("setting_bot", user_id)


@bot.callback_query_handler(func=lambda call: True)
def functions(call):
    user_id = call.message.chat.id
    if call.message:
        if db.user_has_group_db(call.message.chat.id):
            if call.data == "start":
                bot.send_message(chat_id=user_id, text="Вот тебе мои функции:",
                                 reply_markup=kb.get_start_keyboard(), )

            elif call.data == "maths":
                bot.send_message(user_id, config.maths)

            elif call.data == "russian":
                bot.send_message(user_id, config.russian)

            elif call.data == "literature":
                bot.send_message(user_id, config.literature)

            elif call.data == "english":
                bot.send_message(user_id, config.english)

            elif call.data == "sociology":
                bot.send_message(user_id, config.sociology)

            elif call.data == "TOK":
                bot.send_message(user_id, config.TOK)

            elif call.data == "physics":
                bot.send_message(user_id, config.physics)

            elif call.data == "history":
                bot.send_message(user_id, config.history)

            elif call.data == "economics":
                bot.send_message(user_id, config.economics)

            elif call.data == "historyofeconomics":
                bot.send_message(user_id, config.historyofeconomics)

            elif call.data == "psychology":
                bot.send_message(user_id, config.psychology)

            elif call.data == "geography":
                bot.send_message(user_id, config.geography)

            elif call.data == "business":
                bot.send_message(user_id, config.business)

            elif call.data == "IT":
                bot.send_message(user_id, config.IT)

            elif call.data == "PE":
                bot.send_message(user_id, config.PE)

            elif call.data == "biology":
                bot.send_message(user_id, config.biology)

            elif call.data == "chemistry":
                bot.send_message(user_id, config.chemistry)

            elif call.data == "notificationLesson":
                bot.send_message(chat_id=user_id, text="Выберите режим",
                                 reply_markup=kb.get_notification_keyboard())

            elif call.data == "delete_notifications":
                db.delete_user_notifications_db(call.message.chat.id)
                bot.send_message(chat_id=user_id, text="Уведомления приостановлены")

            elif call.data == "5minute":
                kb.add_user_notifications(user_id, 5)

            elif call.data == "10minute":
                kb.add_user_notifications(user_id, 10)

            elif call.data == "studentsInfo":
                markup = types.ForceReply(selective=True)
                bot.send_message(user_id, "Теперь введите имя ученика",
                                 reply_markup=markup)
                db.change_condition_bd("searching_user", user_id=user_id)
                bot.send_message(chat_id=user_id, text="Вернуться в главное меню",
                                 reply_markup=kb.get_cancel_keyboard())

            elif call.data == "teachersInfo":
                db.change_condition_bd("searching_teacher", user_id)
                bot.send_message(chat_id=user_id, text="Выбери нужный предмет",
                                 reply_markup=kb.get_subjects_keyboard())

            elif call.data == "formulas":
                bot.send_message(chat_id=user_id, text="Выбери нужную тему", reply_markup=kb.get_formulas_keyboard())

            elif call.data == "notificationDeadline":
                bot.send_message(chat_id=user_id, text="Меню установки Дэдлайнов",
                                 reply_markup=kb.get_deadline_keyboard())

            elif call.data == "show_deadlines":
                show_deadlines(user_id)

            elif call.data == "cancel":
                bot.send_message(chat_id=user_id, text="Отмена", reply_markup=types.ReplyKeyboardRemove(),
                                 parse_mode='HTML', disable_web_page_preview=True)
                bot.send_message(chat_id=user_id, text="Вот тебе мои функции:",
                                 reply_markup=kb.get_start_keyboard(), )
                db.change_condition_bd("empty", user_id)

            elif call.data == "add_deadline":
                markup = types.ForceReply(selective=True)
                bot.send_message(user_id, "Введите дату и время дэдлайна в формате dd/mm/yyyy hh.mm.ss или"
                                 + " hh.mm.ss для одноразового напоминания",
                                 reply_markup=markup)
                cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(cb_btn_cancel)
                bot.send_message(user_id, reply_markup=keyboard, text="Отменить настройку дэдлайна")
                db.change_condition_bd("adding_deadline", user_id)

            elif call.data == "deadline_circular":
                db.set_deadline_type(user_id, "circular")

            elif call.data == "deadline_once":
                db.set_deadline_type(user_id, "once")

            elif call.data == "time":
                send_time_before_break(user_id)

            elif call.data == "links":
                bot.send_message(user_id, config.links)

            elif call.data == "marks":
                db.change_condition_bd("marks", user_id)
                bot.send_message(chat_id=user_id, text="Введите данные в следующем формате: 'Предмет, "
                                                       "констатирующие. формирующие, творческие оценки,"
                                                       " желаемый балл ' ",
                                 reply_markup=kb.get_cancel_keyboard())

            elif call.data == "timetable":
                bot.send_message(chat_id=user_id, text="Расписание", reply_markup=kb.get_timetable_keyboard())

            elif call.data == "weeklytimetable":
                markup = types.ForceReply(selective=False)
                bot.send_message(call.message.chat.id, "Введите группу ",
                                 reply_markup=markup)
                db.change_condition_bd("group_number_w", user_id)

            elif call.data == "daylytimetable":
                bot.send_message(chat_id=call.message.chat.id, text=get_timetable_text(user_id))

            elif call.data == "economicgrowth" or "inflation" or "unemployment" or "markets" or "production_and_costs" \
                    or "kvp" or "gini" or "gdp" or "elasticity":
                send_formula_image(call)
            else:
                bot.send_message(user_id, "Error")

        else:
            if str(call.message.text) in config.groups:
                db.add_user_group_bd(call.message)
                db.change_condition_bd("empty", user_id)
                bot.send_message(user_id, "Группа добавлена в базу данных!")
            else:
                print(str(call.message.text))
                print(call.message.text in config.groups)
                bot.send_message(user_id, "Введите вашу группу \n Например: 10МЭ2")


def notify_10_mins(delta):
    database = psycopg2.connect(config.connection_string)
    database_cursor = database.cursor()
    database_cursor.execute('''SELECT id_10,last_notified_10  FROM notifications WHERE id_10 IS NOT NULL''')
    data = database_cursor.fetchall()
    now = int(round(time.time() * 1000))
    print(now)
    for row in data:
        try:
            print(row)
            user_id = int(row[0])
            bot.send_message(chat_id=user_id, text="До начала урока осталось " + str(delta) + " минут")
        except Exception as e:
            # bot.send_message(chat_id=user_id, text="До начала урока осталось " + str(delta) + " минут")
            print("что-то пошло не так" + str(e))


def notify_5_mins(delta):
    database = psycopg2.connect(config.connection_string)
    database_cursor = database.cursor()
    database_cursor.execute('''SELECT id_5,last_notified_5  FROM notifications WHERE id_5 IS NOT NULL''')
    data = database_cursor.fetchall()
    now = int(round(time.time() * 1000))
    print(now)
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
            delta = ((some_time.hour * 3600) + (some_time.minute * 60) + some_time.second) - (
                    (time_moscow.hour * 3600) +
                    (time_moscow.minute * 60) +
                    time_moscow.second)
            delta /= 60
            print(delta)
            if 5 < delta <= 10:
                notify_10_mins(delta)
                print("sleeping 5 min")
                time.sleep(300)
            elif 0 < delta <= 5:
                notify_5_mins(delta)
                print("sleeping for 30 min")

                time.sleep(1800)
            else:
                print("nothing")
                time.sleep(0.2)


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
    db.change_condition_bd("deadline process", message.chat.id)
    throw_deadline_choice(message)
    pass


def send_formula_image(call):
    global timetable_photo
    user_id = call.message.chat.id
    image_str = call.data
    if image_str == "kpv":
        timetable_photo = open(config.kpv, 'rb')
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
    user_group = db.get_user_group_db(user_id)
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


if __name__ == '__main__':
    db.create_db()
    bot.remove_webhook()
    bot.polling(none_stop=True, timeout=5)

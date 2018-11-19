import psycopg2
from telebot import types
import config


def get_start_keyboard():
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
    return keyboard_functional
    pass


def get_notification_keyboard():
    cb_btn_5minute = types.InlineKeyboardButton(text="За 5 минут до урока", callback_data="5minute")
    cb_btn_10minute = types.InlineKeyboardButton(text="За 10 минут до урока", callback_data="10minute")
    cb_btn_delete = types.InlineKeyboardButton(text="Остановить напоминания", callback_data="delete_notifications")

    keyboard_notifications = types.InlineKeyboardMarkup()
    keyboard_notifications.row_width = 1
    keyboard_notifications.add(cb_btn_5minute, cb_btn_10minute, cb_btn_delete)
    return keyboard_notifications


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


def get_cancel_keyboard():
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(cb_btn_cancel)
    return keyboard


def get_timetable_keyboard():
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    cb_btn_daylytimetable = types.InlineKeyboardButton(text="На день",
                                                       callback_data="daylytimetable")
    cb_btn_weeklytimetable = types.InlineKeyboardButton(text="На неделю",
                                                        callback_data="weeklytimetable")
    keyboard_timetable = types.InlineKeyboardMarkup()
    keyboard_timetable.add(cb_btn_weeklytimetable, cb_btn_daylytimetable, cb_btn_cancel)
    return keyboard_timetable


def get_deadline_keyboard():
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    cb_btn_my_deadlines = types.InlineKeyboardButton(text="Показать мои дэдлайны", callback_data="show_deadlines")
    cb_btn_add_deadline = types.InlineKeyboardButton(text="Добавить дэдлайн", callback_data="add_deadline")

    keyboard_deadline = types.InlineKeyboardMarkup()
    keyboard_deadline.row_width = 1
    keyboard_deadline.add(cb_btn_my_deadlines, cb_btn_add_deadline, cb_btn_cancel)
    return keyboard_deadline
    pass


def get_formulas_keyboard():
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
    return keyboard_formulas
    pass


def get_subjects_keyboard():
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
    return keyboard_subjects

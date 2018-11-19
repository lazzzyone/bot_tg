import config
import psycopg2


def get_data_from_db(user_id, get_exist, get_group, get_hasdeadlines, get_condition_from_db):
    database_cursor = psycopg2.connect(config.connection_string).cursor()
    if get_exist and not get_hasdeadlines and not get_condition_from_db:
        try:
            database_cursor.execute('''SELECT * FROM ''' + config.users_table + ''' WHERE id = ''' + str(user_id))
            print(str(database_cursor.fetchone()[0]))
            return True
        except Exception as e:
            print(e)
            return False
    if get_condition_from_db:
        database_cursor.execute('''SELECT condition FROM users_table WHERE id = ''' + str(user_id))
        return str(database_cursor.fetchone()[0])

    if get_hasdeadlines and get_condition_from_db:
        try:
            database_cursor.execute('''SELECT hasDeadlines AND condition WHERE id = ''' + str(user_id))
        except Exception as e:
            print(e)
            return None
    if get_group:
        try:
            database_cursor.execute('''SELECT user_group FROM users_table WHERE id = ''' + str(user_id))
            return str(database_cursor.fetchone()[0])
        except Exception as e:
            print(e)
            return -1


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


def delete_user_notifications_db(user_id):
    db_ = psycopg2.connect(config.connection_string)
    cursor = db_.cursor()
    cursor.execute('''DELETE FROM ''' + config.notifications_table + ''' WHERE id_5 = '''+str(user_id) +
                   ''' or id_10 = '''+str(user_id))
    db_.commit()


def get_user_group_db(user_id):
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


def get_condition_db(user_id):
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


def user_has_group_db(user_id):
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

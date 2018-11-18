import datetime

token = '681676837:AAGzwsd5_pQUAC1jchWufv7UdUbjMB5xZVM'

economicgrowth = '\\timetables\economicgrowth.png'
elasticity = '\\timetables\elasticity.png'
markets = '\\timetable\smarkets.png'
production_and_costs = '\\timetables\production_and_costs.png'
unemployment = 'D:\\Bot\\unemployment.png'
inflation = '\\timetables\inflation.png'
GDP = '\\timetables\GDP.png'
gini = 'D:\Bot\gini.png'
kvp = 'timetables\kvp.png'

_10me1 = 'D:\Bot\\timetables\\10МЭ1.jpg'
_10me2 = 'D:\Bot\\timetables\\10МЭ2.jpg'
_10me3 = 'D:\Bot\\timetables\\10МЭ3.jpg'
_10me4 = 'D:\Bot\\timetables\\10МЭ4.jpg'
_10me5 = 'D:\Bot\\timetables\\10МЭ5.jpg'
_10me6 = 'D:\Bot\\timetables\\10МЭ6.jpg'
_11me1 = 'D:\Bot\\timetables\\11МЭ1.jpg'
_11me2 = 'D:\Bot\\timetables\\11МЭ2.jpg'
_11me3 = 'D:\Bot\\timetables\\11МЭ3.jpg'
_11me4 = 'D:\Bot\\timetables\\11МЭ4.jpg'
_11me5 = 'D:\Bot\\timetables\\11МЭ5.jpg'
_11me6 = 'D:\Bot\\timetables\\11МЭ6.jpg'

links = """ссылки вк
https://vk.com/hse_lyceum Лицей НИУ ВШЭ  
https://vk.com/hselyceumhelp помощь абитуриетнам 
https://vk.com/hsemeetingarea хочу в лицей 
https://vk.com/hselyceumquotes цитатник преподователей
https://vk.com/hselyceumevents организация мероприятий 
https://vk.com/mediahselyc медиа-команда 
https://vk.com/ravenpress raven press
https://vk.com/hsemem хайер скул оф мемс
https://vk.com/hselyceumprojects ИВР 
https://vk.com/avhselyceum ассоциация волонтеров 
https://vk.com/perspectivelyc perspective lyceum 
https://vk.com/charitymarkethselyceum сharity market 
https://vk.com/hsegayclub сложные мемы

ссылка на сайт лицея
https://school.hse.ru

ссылки инстаграм 
https://www.instagram.com/hse_lyceum/?hl=ru лицей НИУ ВШЭ
https://www.instagram.com/raven_press_hse/?hl=ru raven press
https://www.instagram.com/om.team_/  организация мероприятий """

connection_string = "host='ec2-79-125-124-30.eu-west-1.compute.amazonaws.com' dbname='d2b2cuvkqcaflp' " \
                    "port='5432' user='ywdmdxihjmmrvv' " \
                    "password='1b2b751c24f0f0c62f6fc29b129d5744ddc3391c55a608d9a84ef966a0833e33' "

db_path = 'D:/_allMyProjects/python_projects/bot/database/bot.db'
users_table = "users_table"
deadlines_table = "deadlines_table"
notifications_table = "notifications"

groups = ["10МЭ1", "10МЭ2", "10МЭ3", "10МЭ4", "10МЭ5", "11МЭ6", "11МЭ1", "11МЭ2", "11МЭ3", "11МЭ4", "11МЭ5", "11МЭ6"]

maths = """Выбери и введи нужного учителя:
Красинец А.В.
Салимова А.Ф.
Деменко В.Н.
Шабат Н.А.
Чистяков Д.С.
Зубков И.В.
Зубов А.Б. 
Быков Ю.В."""

russian = """Выбери и введи нужного учителя:
Арабули Ц.Г.
Задорожная А.С.
Казакова О.В.
Юганова Ф.С.
Фатеева И.М.
Кузнецов А.А."""

literature = """Выбери и введи нужного учителя:
Арабули Ц.Г.
Задорожная А.С.
Казакова О.В.
Юганова Ф.С.
Мирецкая Е.В.
Кузнецов А.А."""

english = """Выбери и введи нужного учителя:
Бабаян Т.М.
Бутина М.В.
Рычкова С.А.
Юрьев А.Е.
Салехова Л.Ю. 
Николаева О.С.
Воронкова А.В.
Шабалин В.В.
Крючкова М.А.
Купцов А.А."""

sociology = """Выбери и введи нужного учителя:
Крикунов К.А.
Антонова К.А. 
Никулин Д.Н.
Цыганков Н.С.
Бешта Н.В.
Томашов И.А."""

TOK = """Выбери и введи нужного учителя:
Бродский В.И.
Беляева А.В."""

physics = """Выбери и введи нужного учителя:
Строганкова Н.И.
Тюгашин В.Н.
Шелаева Н.А."""

history = """Выбери и введи нужного учителя:
Московцева Ж.Ю.
Матвеев С.Р.
Степанов Д.Ю.
Кацнельсон Г.С.
Аристов С.В.
Морозов А.Ю.
Абдулаев Э.Н.
Донской Г.Г.
Новоселова Е.В.
Маслакова Т.П."""

economics = """Выбери и введи нужного учителя:
Андреева В.В.
Михайлов Д.А.
Железнякова Н.А.
Челеховский А.Н.
Дичева О.В.
Маканчиков К.Н.
Калашникова А.Е.
Дьячков Г.В."""

historyofeconomics = """Выбери и введи нужного учителя:
Хаиткулов Р.Г. 
Баженов Г.А.
Чаплыгина И.Г."""

teachers = {
    "Красинец А.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Салимова А.Ф.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Деменко В.Н.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Шабат Н.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Чистяков Д.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Зубков И.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Зубов А.Б. ": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Быков Ю.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Арабули Ц.Г.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Задорожная А.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Казакова О.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Юганова Ф.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Фатеева И.М.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Кузнецов А.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Мирецкая Е.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Бабаян Т.М.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Бутина М.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Рычкова С.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Юрьев А.Е.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Салехова Л.Ю. ": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Николаева О.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Воронкова А.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Шабалин В.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Крючкова М.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Крикунов К.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Антонова К.А. ": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Никулин Д.Н.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Цыганков Н.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Бешта Н.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Томашов И.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Бродский В.И.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Беляева А.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Строганкова Н.И.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Тюгашин В.Н.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Шелаева Н.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Московцева Ж.Ю.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Матвеев С.Р.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Степанов Д.Ю.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Кацнельсон Г.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Аристов С.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Морозов А.Ю.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Абдулаев Э.Н.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Донской Г.Г.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Новоселова Е.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Маслакова Т.П": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Андреева В.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Михайлов Д.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Железнякова Н.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Челеховский А.Н.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Дичева О.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Маканчиков К.Н.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Калашникова А.Е.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Дьячков Г.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Хаиткулов Р.Г. ": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Баженов Г.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Чаплыгина И.Г.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Этко Е.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Батюк Н.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Ясный Е.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Тищенко Н.Ю.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Молокостова А.М.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Байбурин Р.Ф.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Купцов А.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Голубев Е.В.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Сорокина С.С.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Бородулина В.П.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Шопенская Т.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Моручков А.А.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg',
    "Нерето М.О.": 'C:\\Users\\user\\Pictures\\bot\\teachers\\12.jpg'
}

psychology = """Выбери и введи нужного учителя:
Этко Е.А.
Батюк Н.С."""

geography = """Выбери и введи нужного учителя:
Ясный Е.В."""

business = """Выбери и введи нужного учителя:
Тищенко Н.Ю.
Молокостова А.М."""

IT = """Выбери и введи нужного учителя:
Байбурин Р.Ф.
Купцов А.А."""

PE = """Выбери и введи нужного учителя:
Голубев Е.В.
Сорокина С.С."""

biology = """Выбери и введи нужного учителя:
Бородулина В.П.
Шопенская Т.А.
Моручков А.А."""

chemistry = """"Выбери и введи нужного учителя:
Нерето М.О."""

marks_weight = {
    ("Русский язык", "русский язык", "русский", "русс", "Литература", "литература", "литра", "Русский"): (
     0.4, 0.2, 0.4),
    ("математика", "матеша", "Математика", "матан"): (0.6, 0.25, 0.15),
    ("История", "история"): (0.6, 0.3, 0.1),
    ("Иностранный язык", "иностранный", "ИЭиЭМ", "Иностранный", "инстранный язык"): (0.5, 0.3, 0.2),
    ("Гоеография", "география", "гео"): (0.6, 0.15, 0.25),
    ("Биология", "биология", "Физика", "физика", "Астрономия", "астрономия", "Химия", "био"): (0.7, 0.15, 0.15),
    ("Психология", "психология", "общество", "Обществознание", "обществознание", "Общество", "Информатика",
     "информатика",
     "ТОК", "ток"): (0.6, 0.2, 0.2)
}

lessons_starts = {
            datetime.datetime.strptime("9:00:00", '%H:%M:%S'),
            datetime.datetime.strptime("9:45:00", '%H:%M:%S'),
            datetime.datetime.strptime("10:45:00", '%H:%M:%S'),
            datetime.datetime.strptime("11:30:00", '%H:%M:%S'),
            datetime.datetime.strptime("12:20:00", '%H:%M:%S'),
            datetime.datetime.strptime("13:05:00", '%H:%M:%S'),
            datetime.datetime.strptime("14:45:00", '%H:%M:%S'),
            datetime.datetime.strptime("15:30:00", '%H:%M:%S'),
            datetime.datetime.strptime("16:20:00", '%H:%M:%S'),
            datetime.datetime.strptime("17:05:00", '%H:%M:%S'),
            datetime.datetime.strptime("00:14:00", '%H:%M:%S')
        }

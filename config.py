import datetime

token = '681676837:AAGzwsd5_pQUAC1jchWufv7UdUbjMB5xZVM'

economicgrowth = 'formulas/economicgrowth.png'
elasticity = 'formulas/elasticity.png'
markets = 'formulas/markets.png'
production_and_costs = 'formulas/production_and_costs.png'
unemployment = 'formulas/unemployment.png'
inflation = 'formulas/inflation.png'
GDP = 'formulas/GDP.png'
gini = 'formulas/gini.png'
kpv = 'formulas/kpv.png'

_10me1 = 'timetables/10МЭ1.jpg'
_10me2 = 'timetables/10МЭ2.jpg'
_10me3 = 'timetables/10МЭ3.jpg'
_10me4 = 'timetables/10МЭ4.jpg'
_10me5 = 'timetables/10МЭ5.jpg'
_10me6 = 'timetables/10МЭ6.jpg'
_11me1 = 'timetables/11МЭ1.jpg'
_11me2 = 'timetables/11МЭ2.jpg'
_11me3 = 'timetables/11МЭ3.jpg'
_11me4 = 'timetables/11МЭ4.jpg'
_11me5 = 'timetables/11МЭ5.jpg'
_11me6 = 'timetables/11МЭ6.jpg'

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
Макшанчиков К.Н.
Калашникова А.Е.
Дьячков Г.В."""

historyofeconomics = """Выбери и введи нужного учителя:
Хаиткулов Р.Г. 
Баженов Г.А.
Чаплыгина И.Г."""

teachers = {
    "Красинец А.В.": 'teachers/teachers/krasinec.png',
    "Салимова А.Ф.": 'teachers/teachers/salimova.png',
    "Деменко В.Н.": 'teachers/teachers/demenko.png',
    "Шабат Н.А.": 'teachers/teachers/shabat.png',
    "Чистяков Д.С.": 'teachers/teachers/chistyakov.png',
    "Зубков И.В.": 'teachers/teachers/zubkov.png',
    "Зубов А.Б. ": 'teachers/teachers/zubov.png',
    "Быков Ю.В.": 'teachers/teachers/bikov.png',
    "Арабули Ц.Г.": 'teachers/teachers/arabuli.png',
    "Задорожная А.С.": 'teachers/teachers/zadorognaya.png',
    "Казакова О.В.": 'teachers/teachers/kazakova.png',
    "Юганова Ф.С.": 'teachers/teachers/yganova.png',
    "Фатеева И.М.": 'teachers/teachers/fateeva.png',
    "Кузнецов А.А.": 'teachers/teachers/kuznecov.png',
    "Мирецкая Е.В.": 'teachers/teachers/mireckaya.png',
    "Бабаян Т.М.": 'teachers/teachers/babayan.png',
    "Бутина М.В.": 'teachers/teachers/butina.png',
    "Рычкова С.А.": 'teachers/teachers/richkova.png',
    "Юрьев А.Е.": 'teachers/teachers/uriev.png',
    "Салехова Л.Ю. ": 'teachers/teachers/salehova.png',
    "Николаева О.С.": 'teachers/teachers/nikolaeva.png',
    "Воронкова А.В.": 'teachers/teachers/voronka.png',
    "Шабалин В.В.": 'teachers/teachers/shabalin.png',
    "Крючкова М.А.": 'teachers/teachers/kruchkova.png',
    "Крикунов К.А.": 'teachers/teachers/krikunov.png',
    "Антонова К.А. ": 'teachers/teachers/antonova.png',
    "Никулин Д.Н.": 'teachers/teachers/nikulin.png',
    "Цыганков Н.С.": 'teachers/teachers/cigankov.png',
    "Бешта Н.В.": 'teachers/teachers/beshta.png',
    "Томашов И.А.": 'teachers/teachers/tomashov.png',
    "Бродский В.И.": 'teachers/teachers/brodskiy.png',
    "Беляева А.В.": 'teachers/teachers/belyaeva.png',
    "Строганкова Н.И.": 'teachers/teachers/strogankova.png',
    "Тюгашин В.Н.": 'teachers/teachers/tugashin.png',
    "Шелаева Н.А.": 'teachers/teachers/shelaeva.png',
    "Московцева Ж.Ю.": 'teachers/teachers/moscovceva.png',
    "Матвеев С.Р.": 'teachers/teachers/matveev.png',
    "Степанов Д.Ю.": 'teachers/teachers/stepanova.png',
    "Кацнельсон Г.С.": 'teachers/teachers/kacnelson.png',
    "Аристов С.В.": 'teachers/teachers/aristov.png',
    "Морозов А.Ю.": 'teachers/teachers/morozov.png',
    "Абдулаев Э.Н.": 'teachers/teachers/abdulaev.png',
    "Донской Г.Г.": 'teachers/teachers/donskoi.png',
    "Новоселова Е.В.": 'teachers/teachers/novoselova.png',
    "Маслакова Т.П": 'teachers/teachers/maslakova.png',
    "Андреева В.В.": 'teachers/teachers/andreeva.png',
    "Михайлов Д.А.": 'teachers/teachers/mihaylov.png',
    "Железнякова Н.А.": 'teachers/teachers/geleznyakova.png',
    "Челеховский А.Н.": 'teachers/teachers/chelehovskiy.png',
    "Дичева О.В.": 'teachers/teachers/dicheva.png',
    "Макшанчиков К.Н.": 'teachers/teachers/makshanchikov.png',
    "Калашникова А.Е.": 'teachers/teachers/kalashnikova.png',
    "Дьячков Г.В.": 'teachers/teachers/dyachkova.png',
    "Хаиткулов Р.Г. ": 'teachers/teachers/haitkulov.png',
    "Баженов Г.А.": 'teachers/teachers/bagenov.png',
    "Чаплыгина И.Г.": 'teachers/teachers/chapligina.png',
    "Этко Е.А.": 'teachers/teachers/etko.png',
    "Батюк Н.С.": 'teachers/teachers/batuk.png',
    "Ясный Е.В.": 'teachers/teachers/yasniy.png',
    "Тищенко Н.Ю.": 'teachers/teachers/tishenko.png',
    "Молокостова А.М.": 'teachers/teachers/molostova.png',
    "Байбурин Р.Ф.": 'teachers/teachers/baiburin.png',
    "Купцов А.А.": 'teachers/teachers/kuptsov.png',
    "Голубев Е.В.": 'teachers/teachers/golubev.png',
    "Сорокина С.С.": 'teachers/teachers/sorokina.png',
    "Бородулина В.П.": 'teachers/teachers/borodulina.png',
    "Шопенская Т.А.": 'teachers/teachers/shopenskaya.png',
    "Моручков А.А.": 'teachers/teachers/moruchkov.png',
    "Нерето М.О.": 'teachers/teachers/nereto.png'
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

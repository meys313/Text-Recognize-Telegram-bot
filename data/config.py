import os
from pathlib import Path
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent # формирует конрневую директорию проекта



env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
pytesseract_way = os.path.join(BASE_DIR, env.str('pytesseract_way')) # формирует путь к директории pytesseract



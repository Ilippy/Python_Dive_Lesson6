# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

__all__ = []

from datetime import datetime as dt
from collections import defaultdict as dd
from sys import getsizeof as size_of
from random import randint as rnd_int
from decimal import Decimal as Dcml
from re import findall as fa
from typing import Generator as Gen

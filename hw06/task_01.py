def inchCm(int: int) -> int:
    result = int * 2.54
    return result

    """Эта функция конвертирует дюймы в сантиметры
    Parameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def cmInch(int: int) -> int:
    result = int * 0.39
    return result

    """Эта функция конвертирует сантиметры в дюймы
    Parameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def milesKm(int: int) -> int:
    result = int * 1.60
    return result

    """Эта функция мили в километры
    Parameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def kmMiles(int: int) -> int:
    result = int * 0.62
    return result

    """Эта функция конвертирует километры в мили
    Parameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def futKg(int: int) -> int:
    result = int * 2.20
    return result

    """Эта функция конвертирует фунты в килограммы
    Parameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def kgFut(int: int) -> int:
    result = int * 0.45
    return result

    """Эта функция конвертирует километры в фунтыParameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def unGr(int: int) -> int:
    result = int * 28
    return result

    """Эта функция конвертирует унции в граммы
    Parameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def grUn(int: int) -> int:
    result = int * 0.03
    return result

    """Эта функция конвертирует граммы в унцииParameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def galLitr(int: int) -> int:
    result = int * 3.78
    return result

    """Эта функция конвертирует галлоны в литрыParameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def litrGal(int: int) -> int:
    result = int * 0.26
    return result

    """Эта функция конвертирует литры в галлоныParameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def pinLitr(int: int) -> int:
    result = int * 0.47
    return result

    """Эта функция конвертирует пинты в литрыParameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

def litrPin(int: int) -> int:
    result = int * 2.11
    return result

    """Эта функция конвертирует литры в пинтыParameters
    ----------

    int: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

print('Ноль в качестве варианта перевода'
      '\nзавершит работу программы!!!')
while True:
    a = input('Варианты перевода:' '\n1) Дюймы в сантиметры'
    '\n2) Сантиметры в дюймы''\n3) Мили в километры'
    '\n4) Километры в мили' '\n5) Фунты в килограммы'
    '\n6) Килограммы в фунты' '\n7) Унции в граммы' '\n8) Граммы в унции'
    '\n9) Галлон в литры''\n10) Литры в галлоны' '\n11) Пинты в литры'
    '\n12) Литры в пинты'
    '\nВведите вариант перевода:')
    if a == '0':
        break
    if a in '1':
        print(inchCm(float(input())))
    elif a in '2':
        print(cmInch(float(input())))
    elif a in '3':
         print(milesKm(float(input())))
    elif a in '4':
        print(kmMiles(float(input())))
    elif a in '5':
        print(futKg(float(input())))
    elif a in '6':
        print(kgFut(float(input())))
    elif a in '7':
        print(unGr(float(input())))
    elif a in '8':
        print(grUn(float(input())))
    elif a in '9':
        print(galLitr(float(input())))
    elif a in '10':
        print(litrGal(float(input())))
    elif a in '11':
        print(pinLitr(float(input())))
    elif a in '12':
        print(litrPin(float(input())))

def main():
    if __name__ == '__main__':
        inchCm()
def main():
    if __name__ == '__main__':
        cmInch()
def main():
    if __name__ == '__main__':
        milesKm()
def main():
    if __name__ == '__main__':
        kmMiles()
def main():
    if __name__ == '__main__':
        futKg()
def main():
    if __name__ == '__main__':
        kgFut()
def main():
    if __name__ == '__main__':
        unGr()
def main():
    if __name__ == '__main__':
        grUn()
def main():
    if __name__ == '__main__':
        galLitr()
def main():
    if __name__ == '__main__':
        litrGal()
def main():
    if __name__ == '__main__':
        pinLitr()
def main():
    if __name__ == '__main__':
        litrPin()

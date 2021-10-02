# AllCups
Решение задач по треку "Разработка на GO" в проект AllCups | Route 256


# Задание А - 6/60 баллов
В базе данных хранится история значений графика по дням. Каждое значение – это целое число x ≥ 0, либо специальное значение -1.

Требуется вывести значения точек графика по данным из базы. При этом действуют следующие правила:

1. если в данных отсутствует значение для дня X или оно равно -1, то текущим считается значение ближайшего предыдущего дня, для которого есть значение;
2. если до дня X нет никаких значений, то в этот день отдаем специальное значение -1, которое говорит о том, что данных нет;
3. для любого дня в будущем отдаем специальное значение -1;

# Задание B
Есть JSON, состоящий из массива объектов, в каждом объекте которого есть поле data. В поле data лежит объект, в котором гарантируется наличие строкового ключа key`. Длина массива 0 ≤ x ≤ 105.

Требуется посчитать количество уникальных значений среди всех key во всех data.

# Задание C - 30/30 баллов
 Есть массив целых чисел, требуется найти в нём самое большое N-ое число.

Объяснение к примеру:

1. первое самое большое число – это 5, оно встречается один раз;
2. второе самое большое число – это 3, оно встречается два раза;
3. третье самое большое число – это 2, оно встречается один раз и является искомым.

# Задание D
Есть 0 < N ≤ 105 складов. На каждом лежит до 0 < M ≤ 105 товаров. У каждого товара свой уникальный числовой артикул 0 < a ≤ 105. Некоторые товары могут находиться на нескольких складах одновременно. Для каждого склада известна стоимость доставки до получателя.

Нужно определить, какую стоимость товара показать пользователю, учитывая его доступность на складе и стоимость доставки. Разумеется, это должна быть наименьшая из возможных цен.

Объяснение к примеру:

1. Товар с артикулом 123 находится на складах 1 и 2, стоимость доставки с первого склада 321, со второго 101. Стоимость самого товара 9999. Минимальная стоимость товара с учётом доставки 9999 + 101 = 10100.
2. Товар с артикулом 555 находится на складе 1, цена доставки до пользователя 999. Стоимость самого товара 10001. Тогда стоимость с учётом доставки 10001 + 999 = 11000.
3. Товара с артикулом 42 нет ни на одном из складов. Поэтому выводится -1 -1.


# Задание E
Однажды на склад привезли сразу несколько партий товаров и выгрузили их в N разных куч, размер каждый кучи ai. При этом известно, что в первой куче товары имеют номера от 1 до a1, во второй от a1 + 1 до a1 + a2 и так далее.

Но из этих товаров надо собрать заказы. Поэтому надо как можно быстрее по номеру товара определять в какой куче он лежит.

# Задание F
Римская система счисления содержит символы: I, V, X, L, C, D и M.

Следующие цифры римской системы счисления соответствуют символам в десятичной системе: I = 1; V = 5; X = 10; L = 50; C = 100; D = 500; M = 1000.

Числа в римской системе обычно записываются от большего к меньшему, слева направо, например, семь можно записать как V + II = VII, а двадцать семь как XX + V + II = XXVII.

Однако, число 4 записывается не как IIII, а как IV. Т.е. Для получения некоторых цифр в римской системе счисления используется принцип вычитания.

Следующие правила задают условия, при которых следует использовать принцип вычитания:

1. I может предшествовать V (5) и X (10) для получения 4-х и 9-и соответственно;
2. X может предшествовать L (50) и С (100) для получения 40-а и 90-а соответственно;
3. С может предшествовать D (500) и M (1000) для получения 400-а и 900-а соответственно;
Но не всё так просто. Согласно классическим римским правилам, максимальное число, которое может быть представлено в этой системе счисления, это 3999. Однако есть способы, которые позволяют обойти это ограничение. Мы будем использовать модификацию vinculum. В базовой версии это позволяет разделить число на два блока цифр, первый из которых умножается на 1000, т.е. IV|DCXXVII = 4 627, при этом второй блок не больше тысячи, чтобы не было коллизий при записи. Мы же пойдём чуть дальше и введём следующие правила:

1. Может быть сколько угодно много блоков, которые разделены символом |
2. Каждый из блоков, кроме первого, содержит в себе число меньше 1000
3. Первый блок может быть каким угодно римским числом.


# Задание G
Даны три таблицы:

1. Клиенты (client), описывающая клиентов
2. Заказы (order), описывающая заказы
3. Товары (product), описывающая товары, которые есть в заказах
Таблица client
id	email
1	client1@ozon.ru
2	client2@ozon.ru
3	client3@ozon.ru
Таблица order
id	client_id	created_at	updated_at
1	1	2021-09-10 12:30	2021-09-12 12:24
2	1	2021-08-10 12:30	2021-09-12 12:24
3	3	2021-09-01 12:30	2021-09-12 12:24
Таблица product
id	order_id	cnt	price
1	1	1	200
2	2	1	500
3	3	1	600
Требуется вывести средний чек каждого клиента, при условии, что клиент совершил не менее двух заказов на сумму более 1000 рублей каждый.

# Задание H
Ввод информации о себе

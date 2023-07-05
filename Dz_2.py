# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]


text = "Python - это простой в освоении и мощный язык программирования. Он обладает эффективными высокоуровневыми структурами данных и простым, но эффективным подходом к объектно-ориентированному программированию. Элегантный синтаксис Python и динамическая типизация вместе с его интерпретируемым характером делают его идеальным языком для написания сценариев и быстрой разработки приложений во многих областях на большинстве платформ.\
Интерпретатор Python и обширная стандартная библиотека свободно доступны в исходном виде или в двоичном виде для всех основных платформ с веб-сайта Python, https://www.python.org/ и могут свободно распространяться. На этом же сайте также содержатся дистрибутивы и указатели на множество бесплатных модулей, программ и инструментов Python сторонних производителей, а также дополнительная документация.\
Интерпретатор Python легко расширяется за счет новых функций и типов данных, реализованных на C или C ++ (или других языках, вызываемых из C). Python также подходит в качестве языка расширения для настраиваемых приложений.\
Это руководство неофициально знакомит читателя с основными концепциями и функциями языка и системы Python. Для практического использования полезно иметь под рукой интерпретатор Python, но все примеры являются автономными, поэтому руководство также можно прочитать в автономном режиме.\
Описание стандартных объектов и модулей см. в Стандартной библиотеке Python. Справочник по языку Python дает более формальное определение языка. Чтобы написать расширения на C или C ++, ознакомьтесь с расширением и внедрением интерпретатора Python и справочным руководством по Python / C API. Существует также несколько книг, подробно освещающих Python.\
Это руководство не пытается быть всеобъемлющим и охватывать каждую отдельную функцию или даже каждую часто используемую функцию. Вместо этого в нем представлены многие из наиболее примечательных функций Python и оно даст вам хорошее представление об особенностях и стиле языка. Прочитав его, вы сможете читать и писать модули и программы на Python и будете готовы узнать больше о различных библиотечных модулях Python, описанных в Стандартной библиотеке Python."

print(most_frequent(text))
def single_root_words(root_world, *other_words):
    same_words = []
    root_word_lower = root_world.lower()  # переводим слово которое ищем в нижний регист
    for word in other_words:
        word_lower = word.lower()  # переводим слово из списка в нижний регист
        if root_word_lower in word_lower or word_lower in root_word_lower:  # условие что одно из слов должно
            # находиться в другом
            same_words.append(word)
    return same_words


# Подставляем значени и проверяем
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# #
# root_world = 'Able'
# other_words = 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel'
# same_words = single_root_words(root_world, *other_words)
# print(f"Слова, содержащие '{root_world}' : {same_words}")
#
# root_world = 'rich'
# other_words = 'rich', 'richiest', 'orichalcum', 'cheers', 'richies'
# same_words = single_root_words(root_world, *other_words)
# print(f"Слова, содержащие '{root_world}' : {same_words}")

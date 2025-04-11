import random

LETTER_SCORES = {"А": 1, "Б": 3, "В": 1,
                 "Г": 3, "Д": 2, "Е": 1,
                 "Ё": 3, "Ж": 5, "З": 5,
                 "И": 1, "Й": 4, "К": 2,
                 "Л": 2, "М": 2, "Н": 1,
                 "О": 1, "П": 2, "Р": 1,
                 "С": 1, "Т": 1, "У": 2,
                 "Ф": 10, "Х": 5, "Ц": 5,
                 "Ш": 8, "Щ": 10, "Ъ": 10,
                 "Ы": 4, "Ь": 3, "Э": 8,
                 "Ю": 8, "Я": 3}


def get_random_letter():
    dict_keys = LETTER_SCORES.keys()
    converted_dictionary = list(dict_keys)
    while True:
        random_letter = random.choice(converted_dictionary)
        if random_letter not in ["Ь", "Ъ", "Ы"]:
            return random_letter


def get_word_with_letter(letter):
    while True:
        word_player = input(f"введите слово на букву {letter} :")
        if word_player[0].upper() == letter:
            return word_player
        else:
            print(f"Слово должно начинатся на букву *{letter}*. Попробуйте снова.")


def calculate_score(word):
    all_scores = []
    for letter in word.upper():
        all_scores.append(LETTER_SCORES.get(letter, 0))
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    random_letter = (get_random_letter())
    print("Начальная буква: ", random_letter)
    print("Игрок 1")
    word_p1 = get_word_with_letter(random_letter)
    score_p1 = calculate_score(word_p1)
    print("Игрок 2")
    word_p2 = get_word_with_letter(random_letter)
    score_p2 = calculate_score(word_p2)
    print(f"Игрок 1 ввел слово '{word_p1}' инабрал {score_p1} очков.")
    print(f"Игрок 2 ввел слово '{word_p2}' инабрал {score_p2} очков.")
    if score_p1 > score_p2:
        print("игрок 1 победил!!!")
    elif score_p2 > score_p1:
        print("Икрок 2 победил!!!")
    else:
        print("победила дружба")


if __name__ == '__main__':
    main()

def recognize(word: str) -> bool:
    stack = []

    # В строке должны быть ровно три символа a в начале
    if len(word) < 3 or word[:3] != "aaa":
        return False

    # После первых трёх a больше символов a быть не должно
    index = 3

    # Считываем b и помещаем X в магазин
    while index < len(word) and word[index] == "b":
        stack.append("X")
        index += 1

    # Считываем c и извлекаем X из магазина
    while index < len(word) and word[index] == "c":
        if not stack:
            return False

        stack.pop()
        index += 1

    # Строка принимается, если:
    # 1. прочитана полностью;
    # 2. магазин пуст, то есть количество b равно количеству c
    return index == len(word) and len(stack) == 0


def main():
    tests = [
        "aaa",
        "aaabc",
        "aaabbcc",
        "aaabbbccc",
        "aaabbc",
        "aaabcc",
        "aaaa",
        "aaabbbc",
        "aabbcc",
    ]

    for word in tests:
        result = "ACCEPT" if recognize(word) else "REJECT"
        print(f"{word:12} -> {result}")


if __name__ == "__main__":
    main()
__all__ = ['guess_answer']


def guess_answer(question: str, answers: list[str], tries: int) -> int:
    for i in range(tries):
        print(question)
        answer = input("Введите ваш ответ: ")
        if answer in answers:
            return i + 1
        else:
            print("Ответ не верный")
    return 0

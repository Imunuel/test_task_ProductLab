# names_list = ["Ваня", "Лёша", "Катя", "Лена", "Оля", "Петя", "Стёпа", "Настя", "Дима", "Маша"]


def prepare_set(net: tuple, mediator: str, current_set: list):
    for count in range(0, len(net)):
        if mediator in net[count]:
            if mediator == net[count][0]:
                mediator = net[count][1]
            elif mediator == net[count][1]:
                mediator = net[count][0]
            if mediator not in current_set:
                current_set.append(mediator)
                prepare_set(net, mediator, current_set)


def check_relation(net: tuple, first: str, second: str):
    first_set = []
    second_set = []
    prepare_set(net, first, first_set)
    prepare_set(net, second, second_set)

    if first in second_set or second in first_set:
        first_set.clear()
        second_set.clear()
        return True
    first_set.clear()
    second_set.clear()
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True

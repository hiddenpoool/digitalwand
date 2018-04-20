# -----------------
# Реализуйте функцию best_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. У каждой карты есть масть(suit) и
# ранг(rank)
# Масти: трефы(clubs, C), пики(spades, S), червы(hearts, H), бубны(diamonds, D)
# Ранги: 2, 3, 4, 5, 6, 7, 8, 9, 10 (ten, T), валет (jack, J), дама (queen, Q), король (king, K), туз (ace, A)
# Например: AS - туз пик (ace of spades), TH - дестяка черв (ten of hearts), 3C - тройка треф (three of clubs)

# Реализуйте функцию best_wild_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. Кроме прочего в данном варианте "рука"
# может включать джокера. Джокеры могут заменить карту любой
# масти и ранга того же цвета, в колоде два джокерва.
# Черный джокер '?B' может быть использован в качестве треф
# или пик любого ранга, красный джокер '?R' - в качестве черв и бубен
# любого ранга.

# Одна функция уже реализована, сигнатуры и описания других даны.
# Вам наверняка пригодится itertools
# Можно свободно определять свои функции и т.п.
# -----------------
from itertools import repeat, starmap

# Масти
TRUMP = ['C', 'S', 'H', 'D']
# Значения карт
VALUES = [str(x) for x in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
# Массив для поиска стрит-последовательностей
EQUAL_DIFF = list(repeat(1, 4))
# Колода
DECK = [value + trump for value in VALUES for trump in TRUMP]


def hand_rank(hand):
    """Возвращает значение определяющее ранг 'руки'"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, flush(hand)
    elif kind(4, ranks):
        return 7, kind(4, ranks)
    elif kind(3, ranks, 2):
        return 6, kind(3, ranks, 2)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, ranks
    elif kind(3, ranks):
        return 3, kind(3, ranks)
    elif two_pair(ranks):
        return 2, two_pair(ranks)
    elif kind(2, ranks):
        return 1, kind(2, ranks)
    else:
        return 0, ranks


def card_ranks(hand):
    """Возвращает список рангов (его числовой эквивалент),
    отсортированный от большего к меньшему"""
    ranks = [card[:-1] for card in hand]
    return sorted(ranks, key=lambda rank: VALUES.index(rank), reverse=True)


def flush(hand):
    """Возвращает True, если все карты одной масти"""
    trump_check = dict(zip(TRUMP, repeat(0, 4)))
    for card in hand:
        trump_check[card[-1]] += 1
        if trump_check[card[-1]] == 5:
            return card[-1]
    return False


def straight(ranks):
    """Возвращает True, если отсортированные ранги формируют последовательность
    из 5-то карт, где у 5ти карт ранги идут по порядку (стрит)"""
    diffs = list(starmap(lambda x, y: VALUES.index(x) - VALUES.index(y),
                         zip(ranks[:-1], ranks[1:])))
    return diffs[:4] == EQUAL_DIFF or diffs[1:5] == EQUAL_DIFF or diffs[2:] == EQUAL_DIFF


def kind(n, ranks, second_rank=1):
    """Возвращает первый ранг, который n раз встречается в данной руке.
    Возвращает None, если ничего не найдено"""
    rank_check = dict(zip(VALUES, repeat(0, 13)))
    for rank in ranks:
        rank_check[rank] += 1
    best_value, second_best = None, None

    for rank, count in rank_check.items():
        if not best_value and count == n:
            best_value = rank
            break
    if best_value:
        for rank, count in rank_check.items():
            if rank != best_value and count >= second_rank:
                if second_best:
                    second_best = second_best \
                        if VALUES.index(second_best) > VALUES.index(rank) \
                        else rank
                else:
                    second_best = rank

    return (best_value, second_best) if best_value and second_best else None


def two_pair(ranks):
    """Если есть две пары, то возврщает два соответствующих ранга,
    иначе возвращает None"""
    return kind(2, ranks, 2)


def get_straight(hand):
    """из 7 карт возвращает комбинацию из 5 карт"""
    hand_copy = sorted(hand, key=lambda card_: VALUES.index(card_[:-1]),
                       reverse=True)
    if VALUES.index(hand_copy[0][:-1]) - VALUES.index(hand_copy[1][:-1]) == 1 \
            and VALUES.index(hand_copy[1][:-1]) - \
            VALUES.index(hand_copy[2][:-1]) == 1:
        return hand_copy[:5]
    elif VALUES.index(hand_copy[1][:-1]) - \
            VALUES.index(hand_copy[2][:-1]) == 1:
        return hand_copy[1:6]
    else:
        return hand_copy[2:]


def best_hand(hand):
    """Из "руки" в 7 карт возвращает лучшую "руку" в 5 карт """
    rank, card = hand_rank(hand)
    if rank == 8:
        hand_copy = filter(lambda x: x[-1] == card, hand)
        return get_straight(hand_copy)

    elif rank == 7:
        best, second_best = card
        hand_copy = next(filter(lambda x: x[:-1] == second_best, hand))
        return list(map(lambda trump: best + trump, TRUMP)) + [hand_copy]

    elif rank == 6:
        best, second_best = card
        hand_copy = list(filter(lambda x: x[:-1] == second_best
                                or x[:-1] == best, hand))
        return list(sorted(hand_copy, key=lambda x: VALUES.index(x[:-1]),
                           reverse=True))

    elif rank == 5:
        hand_copy = filter(lambda x: x[-1] == card, hand)
        hand_copy = sorted(hand_copy, key=lambda card_:
                           VALUES.index(card_[:-1]), reverse=True)
        return hand_copy[:5]

    elif rank == 4:
        return get_straight(hand)

    elif rank == 3:
        best, _ = card
        hand_copy = filter(lambda x: x[:-1] != best, hand)
        hand_copy = sorted(hand_copy, key=lambda card_:
                           VALUES.index(card_[:-1]), reverse=True)
        return list(hand_copy)[:2] + \
            list(filter(lambda x: x[:-1] == best, hand))

    elif rank == 2:
        best, second_best = card
        hand_copy = filter(lambda x: x[:-1] != best
                           or x[:-1] != second_best, hand)
        hand_copy = sorted(hand_copy, key=lambda card_:
                           VALUES.index(card_[:-1]), reverse=True)
        return list(hand_copy)[:1] + \
            list(filter(lambda x: x[:-1] == best
                        or x[:-1] == second_best, hand))

    elif rank == 1:
        best, _ = card
        hand_copy = filter(lambda x: x[:-1] != best, hand)
        hand_copy = sorted(hand_copy, key=lambda card_:
                           VALUES.index(card_[:-1]), reverse=True)
        return list(hand_copy)[:3] + \
            list(filter(lambda x: x[:-1] == best, hand))

    else:
        return list(sorted(hand, key=lambda card_:
                    VALUES.index(card_[:-1]), reverse=True))[:5]


def update_rank(best_hand_, best_rank, best_sum, hand):
    """Проверяет лучше ли новая рука чем старая"""
    rank, _ = hand_rank(hand)
    sum_ = sum([VALUES.index(card_[:-1]) for card_ in best_hand(hand)])
    if rank > best_rank or rank == best_rank and sum_ > best_sum:
        best_rank = rank
        best_hand_ = hand.copy()
        best_sum = sum_
    return best_hand_, best_rank, best_sum


def best_wild_hand(hand):
    """best_hand но с джокерами"""
    best_hand_ = hand.copy()
    best_rank = 0
    best_sum = 0

    if '?B' in hand:
        hand_copy = hand.copy()
        hand_copy.remove('?B')
        for card_B in DECK:
            if card_B not in hand_copy and (card_B[-1] == 'C'
                                            or card_B[-1] == 'S'):
                hand_copy.append(card_B)
                if '?R' in hand:
                    hand_copy.remove('?R')
                    for card_R in DECK:
                        if card_R not in hand_copy \
                                and (card_R[-1] == 'H' or card_R[-1] == 'D'):
                            hand_copy.append(card_R)
                            best_hand_, best_rank, best_sum = update_rank(
                                best_hand_, best_rank, best_sum, hand_copy)
                            hand_copy.pop()
                    hand_copy.insert(0, '?R')

                else:
                    best_hand_, best_rank, best_sum = update_rank(
                        best_hand_, best_rank, best_sum, hand_copy)
                hand_copy.pop()

    elif '?R' in hand:
        hand_copy = hand.copy()
        for card_R in DECK:
            if card_R not in hand_copy and (card_R[-1] == 'C'
                                            or card_R[-1] == 'D'):
                hand_copy.append(card_R)
                best_hand_, best_rank, best_sum = update_rank(
                    best_hand_, best_rank, best_sum, hand_copy)
                hand_copy.pop()

    return best_hand(best_hand_)


def test_best_hand():
    print("test_best_hand...")
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')


def test_best_wild_hand():
    print("test_best_wild_hand...")
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')

if __name__ == '__main__':
    test_best_hand()
test_best_wild_hand()
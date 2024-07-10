import random

suits = {1: '黑桃', 2: '紅心', 3: '方塊', 4: '梅花'}
ranks = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

deck = [(suit, rank) for suit in suits for rank in range(1, 14)]

random.shuffle(deck)

players = [set() for _ in range(4)]

for i in range(4):
    players[i] = set(deck[i*13:(i+1)*13])

for i, player in enumerate(players):
    print(f'玩家 {i+1} 的手牌:')
    for card in player:
        print(card, end=', ')
    print()

for i, player in enumerate(players):
    if (1, 1) in player:
        print(f'黑桃1 在玩家 {i+1} 的手上')
        break


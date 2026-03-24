class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        suit_names = ['Трефы', 'Бубны', 'Червы', 'Пики']
        rank_names = [None, 'Туз', '2', '3', '4', '5', '6', '7', 
                      '8', '9', '10', 'Валет', 'Дама', 'Король']
        return f"{rank_names[self.rank]} {suit_names[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def shuffle(self):
        """Перемешивает колоду"""
        import random
        random.shuffle(self.cards)
    
    def deal_hands(self, num_players, cards_per_hand):
        """
        Создает и возвращает список рук.
        
        Параметры:
        num_players (int): количество игроков
        cards_per_hand (int): количество карт на руку
        
        Возвращает:
        list: список объектов Hand
        """
        # Проверка, что карт хватит
        total_cards_needed = num_players * cards_per_hand
        if total_cards_needed > len(self.cards):
            raise ValueError(f"Недостаточно карт! Нужно {total_cards_needed}, есть {len(self.cards)}")
        
        # Создаем пустые руки
        hands = [Hand(label=f"Игрок {i+1}") for i in range(num_players)]
        
        # Раздаем карты (по одной каждому игроку, пока не раздадим все)
        for _ in range(cards_per_hand):
            for hand in hands:
                if self.cards:  # если карты еще есть
                    card = self.cards.pop(0)  # берем карту сверху
                    hand.add_card(card)
        
        return hands
    
    def __str__(self):
        return f"Колода: {len(self.cards)} карт"


class Hand:
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
    def add_card(self, card):
        """Добавляет карту в руку"""
        self.cards.append(card)
    
    def __str__(self):
        if not self.cards:
            return f"{self.label}: (пусто)"
        cards_str = ', '.join(str(card) for card in self.cards)
        return f"{self.label}: {cards_str}"


# Демонстрация работы
deck = Deck()
print(f"Создана {deck}")
print()

deck.shuffle()  # перемешиваем
print("Колода перемешана\n")

# Раздаем 3 игрокам по 5 карт
hands = deck.deal_hands(num_players=3, cards_per_hand=5)

# Показываем, что получилось
for i, hand in enumerate(hands):
    print(hand)

print(f"\nВ колоде осталось: {len(deck.cards)} карт")
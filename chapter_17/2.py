class Kangaroo:
    def __init__(self, pouch_contents=None):
        """Создает кенгуру с сумкой."""
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = pouch_contents
    
    def put_in_pouch(self, item):
        """Кладет предмет в сумку."""
        self.pouch_contents.append(item)
    
    def __str__(self):
        """Показывает содержимое сумки."""
        return f"Kangaroo with: {self.pouch_contents}"


# Тестирование
kanga = Kangaroo()
roo = Kangaroo()

print("До добавления:")
print(f"kanga: {kanga}")  # Kangaroo with: []
print(f"roo: {roo}")      # Kangaroo with: []

kanga.put_in_pouch(roo)

print("\nПосле добавления roo в сумку kanga:")
print(f"kanga: {kanga}")  # Kangaroo with: [Kangaroo with: []]
print(f"roo: {roo}")      # Kangaroo with: []  ← пусто, как и должно быть

# Проверка, что сумка roo не изменилась
roo.put_in_pouch("банан")
print(f"\nПосле добавления банана в сумку roo:")
print(f"kanga: {kanga}")
print(f"roo: {roo}")      # Kangaroo with: ['банан']
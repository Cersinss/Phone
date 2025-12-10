from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Phone:
    brand: str
    model: str
    price: float
    color: str
    storage_gb: int
    is_in_stock: bool

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        if discount_percent < 0:
            raise ValueError("Скидка не может быть отрицательной")
        self.price *= 1 - discount_percent / 100

    def check_availability(self) -> str:
        return "В наличии" if self.is_in_stock else "Нет в наличии"

    def __str__(self) -> str:
        availability = self.check_availability()
        return (
            f"{self.get_full_name()} | {self.color}, {self.storage_gb} ГБ | "
            f"{self.price:.2f} ₽ | {availability}"
        )


def demo() -> None:
    phones = [
        Phone("Apple", "iPhone 15", 120_000.0, "чёрный", 256, True),
        Phone("Samsung", "Galaxy S24", 95_000.0, "серебристый", 512, False),
        Phone("Google", "Pixel 9", 88_000.0, "белый", 128, True),
        Phone("Xiaomi", "Mi 14", 42_000.0, "синий", 256, True),
    ]

    print("Каталог телефонов:")
    for phone in phones:
        print(phone)

    print("\nПрименяем скидку 10% к первому телефону:")
    phones[0].apply_discount(10)
    print(phones[0])

    print("\nПроверяем доступность второго телефона:")
    print(phones[1].check_availability())


if __name__ == "__main__":
    demo()


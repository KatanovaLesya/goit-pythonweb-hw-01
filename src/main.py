from vehicles import USVehicleFactory, EUVehicleFactory
from library import Library, LibraryManager

def run_vehicles():
    """Запускає тестування Завдання 1: Фабрика транспортних засобів"""
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    vehicle3 = eu_factory.create_car("BMW", "X5")
    vehicle3.start_engine()

    vehicle4 = eu_factory.create_motorcycle("Ducati", "Panigale V4")
    vehicle4.start_engine()

def run_library():
    """Запускає тестування Завдання 2: Бібліотека книг"""
    library = Library()
    manager = LibraryManager(library)

    manager.add_book("1984", "George Orwell", 1949)
    manager.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

    manager.show_books()

    manager.remove_book("1984")
    manager.show_books()

    manager.remove_book("Невідома книга")

def main():
    """Головне меню: вибір між двома завданнями"""
    while True:
        print("\nВиберіть завдання:")
        print("1 - Фабрика транспортних засобів")
        print("2 - Бібліотека книг")
        print("3 - Вийти")

        choice = input("Введіть 1, 2 або 3: ").strip()

        if choice == "1":
            run_vehicles()
        elif choice == "2":
            run_library()
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("❌ Невірний вибір. Введіть 1, 2 або 3.")

if __name__ == "__main__":
    main()

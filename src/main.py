from vehicles import USVehicleFactory, EUVehicleFactory

def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Створення авто для США
    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    # Створення мотоцикла для США
    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    # Створення авто для Європи
    vehicle3 = eu_factory.create_car("BMW", "X5")
    vehicle3.start_engine()

    # Створення мотоцикла для Європи
    vehicle4 = eu_factory.create_motorcycle("Ducati", "Panigale V4")
    vehicle4.start_engine()

if __name__ == "__main__":
    main()

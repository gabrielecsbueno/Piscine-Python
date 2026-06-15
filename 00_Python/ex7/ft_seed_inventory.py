def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    new_seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{new_seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{new_seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{new_seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

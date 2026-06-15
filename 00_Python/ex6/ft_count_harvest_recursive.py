def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def ft_count(day, count):
        if day >= count:
            print(f"Day {count}")
            count += 1
            ft_count(day, count)
        else:
            print("Harvest time!")

    ft_count(day, 1)

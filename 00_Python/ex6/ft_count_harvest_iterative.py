def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    count = 1
    while day >= count:
        print(f"Day {count}")
        count += 1
    print("Harvest time!")

def ft_count_harvest_iterative():
    days_until_harvest = input("Days until harvest: ")
    days_range = int(days_until_harvest) + 1
    for day in range(1, days_range):
        print("Day", day)
    print("Harvest time!")

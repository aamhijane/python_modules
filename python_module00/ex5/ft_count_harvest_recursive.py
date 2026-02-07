def ft_print_days(days_range, count):
    print("Day", count)
    if int(days_range) > count:
        count += 1
        ft_print_days(days_range, count)
     
def ft_count_harvest_recursive():
    days_range = input("Days until harvest: ")
    count = 1
    ft_print_days(days_range, count)
    print("Harvest time!")

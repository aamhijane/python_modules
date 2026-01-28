# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayamhija <ayamhija@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 18:17:04 by ayamhija          #+#    #+#              #
#    Updated: 2026/01/28 18:27:07 by ayamhija         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

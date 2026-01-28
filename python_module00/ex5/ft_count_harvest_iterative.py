# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayamhija <ayamhija@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 18:04:15 by ayamhija          #+#    #+#              #
#    Updated: 2026/01/28 18:11:04 by ayamhija         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days_until_harvest = input("Days until harvest: ")
    days_range = int(days_until_harvest) + 1
    for day in range(1, days_range):
        print("Day", day)
    print("Harvest time!")

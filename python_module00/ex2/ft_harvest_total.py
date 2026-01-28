# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayamhija <ayamhija@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 16:10:54 by ayamhija          #+#    #+#              #
#    Updated: 2026/01/28 16:13:36 by ayamhija         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day_1 = input("Day 1 harvest: ")
    day_2 = input("Day 2 harvest: ")
    day_3 = input("Day 3 harvest: ")
    result = int(day_1) + int(day_2) + int(day_3)
    print("Total harvest:", result)

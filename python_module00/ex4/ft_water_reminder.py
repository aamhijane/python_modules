# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayamhija <ayamhija@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 17:53:58 by ayamhija          #+#    #+#              #
#    Updated: 2026/01/28 17:59:11 by ayamhija         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    last_watering = input("Days since last watering: ")
    if int(last_watering) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

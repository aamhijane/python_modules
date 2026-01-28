# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayamhija <ayamhija@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 16:16:18 by ayamhija          #+#    #+#              #
#    Updated: 2026/01/28 16:21:15 by ayamhija         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    plant_age = input("Enter plant age in days: ")
    if int(plant_age) < 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")


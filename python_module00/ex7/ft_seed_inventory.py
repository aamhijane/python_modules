# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayamhija <ayamhija@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 18:47:37 by ayamhija          #+#    #+#              #
#    Updated: 2026/01/28 19:08:02 by ayamhija         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit.lower() == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit.lower()} available")
    elif unit.lower() == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit.lower()} total")
    elif unit.lower() == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

import math

def distance_between_gold_producers(delta_x, delta_y):
    d = math.sqrt(((delta_x**2)-5) + ((delta_y**2)-5))
    return d

def civilization_calculator():
    return

def trade_cart_speed(isUpgraded):
    if(isUpgraded):
        speed = 1.5
    else:
        speed = 1
    return speed

def get_map_size(recommended_player_count):
    if(recommended_player_count == 2):
        return 120
    if(recommended_player_count == 3):
        return 144
    if(recommended_player_count == 4):
        return 168
    if(recommended_player_count == 6):
        return 200
    if(recommended_player_count == 8):
        return 220

def calculate_cart_gold():
    map_size = get_map_size(2)
    distance = distance_between_gold_producers(map_size, map_size)
    trade_cart_gold = ((.46/map_size)*(distance**2)) + (.138*distance)
    return trade_cart_gold
    
def gold_per_minute(is_edge):
    if(is_edge):
        speed = get_map_size(2)/2
    else:
        speed = get_map_size(2)


def main():
    print(calculate_cart_gold())
    
    
if __name__ == "__main__":
    main()

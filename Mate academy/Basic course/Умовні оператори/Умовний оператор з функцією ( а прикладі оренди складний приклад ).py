short_term_cost=50 #1-3 days
medium_term_cost=40 #4-7 days
long_term_cost=30 # 8+ days

def get_rental_price(number_of_days:int)->int:
    if number_of_days <= 3:
        return number_of_days*50
    else:
        days_left = number_of_days -3
        if number_of_days<=4:
            return 3*50+days_left*40
        else:
            days_left=number_of_days-7

            return 3*50 + 4*40+days_left*30


print(
    get_rental_price(2),
    get_rental_price(5),
    get_rental_price(10)
)
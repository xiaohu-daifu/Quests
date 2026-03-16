def apply_discount(price, discount):
    if type(price) == int or type(price) == str:
        if price <= 0:
            return "The price should be greater than 0"
    else:
        return "The price should be a number"

    if type(discount) != int and type(discount) != float:
        return "The discount should be a number"

    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discounted = discount / 100 * price
    total = price - discounted
    return total


banana = apply_discount(0, 10)

print(banana)

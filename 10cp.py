import random
def generate_lotto_numbers():
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)
        if number not in lotto_numbers:
            lotto_numbers.append(number)

    lotto_numbers.sort()
    return lotto_numbers

print(generate_lotto_numbers())
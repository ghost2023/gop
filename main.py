import random
from collections import Counter

max_num = 9876
min_num = 1234

def generate_num() -> str:
    num = str(random.randint(min_num, max_num))
    while "0" in num or Counter(num).most_common(1)[0][1] > 1:
        num = str(random.randint(min_num, max_num))
    return num

def num_checker(guess: str, actual: str) -> int:
    count = 0
    
    for c in guess:
        if c in actual:
            count += 1

    return count

def position_checker(guess: str, actual: int) -> int:
    count = 0

    for i in range(4):
        if guess[i] == actual[i]:
            count += 1

    return count

def main():
    num = generate_num()
    status = "p"

    while status == "p":
        guess = input('|')
        nums_count = num_checker(guess, num)
        pos = position_checker(guess, num)
        print("\b\b\t|", nums_count, "|", pos, "|")
        if nums_count == 4 and pos == 4:
            print("******************")
            print("*****YOU WON******")
            print("******************")
            return

if __name__ == "__main__":
    main()

import random


def main():

    """
    Initiating difficulty level and randomly generated
    numbers for addition. For-loop generates 10 problems after
    each answer...
    """
    lev = get_level()
    grade = 0
    for i in range(10):
        numbers = generate_integer(lev)
        x = numbers[0]
        y = numbers[1]
        z = x + y
        answer = input(str(x) + " + " + str(y) + " = ")

        """
        Except for when the answer is wrong. This will check
        for any errors in the summation or for a ValueError
        like a word. This also allows three attempts on an incorrect
        answer. If the user gets it wrong three times, the for-loop
        will stop and display the right answer. If answers are correct,
        it will add points to the grade variable.
        """
        if answer.isalpha() or z != int(answer):
            print("EEE")
            for j in range(2):
                answer = input(str(x) + " + " + str(y) + " = ")
                if answer.isalpha() or z != int(answer):
                    print("EEE")
                    j += 1
                elif int(answer) == z:
                    grade += 1
                    break
            print(str(x) + " + " + str(y) + " = " + str(z))
        elif z == int(answer):
            grade += 1

        i += 1

    print("Score:", grade)

# Allows user to input a difficulty level.
def get_level():
    while True:
        try:
            difficulty = int(input("Level: "))
            if difficulty not in range(1, 4):
                raise ValueError
        except ValueError:
            pass

        else:
            return difficulty

# This will generate a random integer for x and y.
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y

if __name__ == "__main__":
    main()

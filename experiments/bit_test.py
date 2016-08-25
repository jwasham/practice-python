import random


def bit_test():
    keep_going = True
    while keep_going:
        rand_num = random.randint(0, 0xFF)
        bits = bin(rand_num)
        correct = False
        attempts = 1
        while not correct:
            answer = input('What is {} in decimal? '.format(bits.replace('0b', '').rjust(8, '0')))
            attempts += 1
            if int(answer) == rand_num:
                print('*** Correct! ***')
                correct = True
            else:
                if attempts > 3:
                    print('The answer is: {}'.format(rand_num))
                    correct = True
                else:
                    print('Try again.')


def main():
    bit_test()

if __name__ == '__main__':
    main()

__author__ = 'Brian Snyder'

def multiple_of_three(number):
    if type(number) == str:
        return number

    if number % 3 == 0:
        return 'fizz'
    else:
        return number

def multiple_of_five(number):
    if type(number) == str:
        return number

    if number % 5 == 0:
        return 'buzz'
    else:
        return number

def multiple_of_fifteen(number):
    if type(number) == str:
        return number

    if number % 15 == 0:
        return 'fizzbuzz'
    else:
        return number


def fizzbuzz(number):
    result = []
    for fbnumber in range(1, number+1):
        n = multiple_of_fifteen(fbnumber)
        n = multiple_of_three(n)
        n = multiple_of_five(n)
        result.append(n)
    return result


if __name__ == '__main__':
    print(' '.join(map(str, fizzbuzz(100))))



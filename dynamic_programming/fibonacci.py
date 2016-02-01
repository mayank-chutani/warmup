__author__ = 'mayank'

def fib(n):
    """
    Finds the fibonacci value of n
    :return: integer value
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 2
    fibList = [None for i in range(n)]
    fibList[0] = 0
    fibList[1] = fibList[2] = 1

    for i in range(2, n):
        fibList[i] = fibList[i-1] + fibList[i-2]
    return fibList[n-1]

if __name__ == '__main__':
    print fib(10)
import time


def AlgTests(self):
    a, b = 0, 1
    while a < self :
        print(a)
        time.sleep(.174)
        a, b = b, a + b


AlgTests(100000000000000)

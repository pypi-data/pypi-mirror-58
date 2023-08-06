from __future__ import absolute_import
import random
import string
from time import sleep


def is_prime(num):
    if num < 0:
        raise Exception("must be a positive number")
    try:
        if num == 1 or num == 0:
            return "not a prime number or a composite number"
        srnum = int(num ** 0.5 + 1)
        tem = srnum
        for i in range(srnum):
            if (num % tem) == 0:
                break
            tem -= 1
        if tem == 1:
            return True
        else:
            return False
    except TypeError:
        raise Exception("unknown error")


def is_square(num):
    try:
        if abs(num ** 0.5 - int(num ** 0.5)) < 10 ** -10:
            return True
        else:
            return False
    except TypeError:
        return "not an integer"


def fib(num):
    try:
        f_a, f_b = 1, 1
        for i in range(num - 1):
            f_a, f_b = f_b, f_a + f_b
        return a
    except TypeError:
        raise Exception("unknown error")


def random_method1(len1):
    m1_a = ""
    for i in range(int(len1)):
        m1_a = m1_a + random.choice(string.ascii_letters)
    return m1_a


def random_method2(len1):
    m2_a = ""
    for i in range(int(len1)):
        b = string.ascii_letters + string.digits
        m2_a = m2_a + random.choice(b)
    return m2_a


def random_all(len1):
    a_a = ""
    for i in range(int(len1)):
        b = string.printable
        a_a = a_a + random.choice(b)
    return a_a


def level(string1):
    s = list(string1)
    ll = d = t = ul = 0
    list1 = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    length = len(string1)
    for items in s:
        if items in string.ascii_lowercase:
            ll += 1
        if items in string.ascii_uppercase:
            ul += 1
        if items in string.digits:
            d += 1
        if items in list1:
            t += 1
    st = passwd.level_store(ll, ul, d, t, length)
    if st >= 90:
        return "perfect"
    elif st >= 80:
        return " very good"
    elif st >= 70:
        return "very strong"
    elif st >= 60:
        return "strong"
    elif st >= 50:
        return "average"
    elif st >= 25:
        return "low"
    else:
        return "too low"


def level_store(ll, ul, d, t, length):
    store = 0
    if d == 1:
        store += 10
    elif d > 1:
        store += 20
    else:
        pass
    if t == 1:
        store += 10
    elif t > 1:
        store += 25
    else:
        pass
    if ll == 0 and ul == 0:
        pass
    elif ll != 0 and ul != 0:
        store += 20
    else:
        store += 1
    if length < 5:
        store += 5
    elif length < 8:
        store += 10
    else:
        store += 20
    if ((ll and ul) and d) and t:
        store += 5
    elif ((ll or ul) and d) and t:
        store += 3
    else:
        store += 2
    if length > 50:
        store += 50
    elif length > 40:
        store += 40
    elif length > 30:
        store += 30
    elif length > 20:
        store += 20
    else:
        pass
    return store


def encode1(st):
    e1_a, b = random_all(10), random_all(10)
    lst = list(st)
    st1 = ""
    for items in lst:
        ord1 = ord(items) + 1
        st1 = st1 + chr(ord1)
    st = st1
    st = e1_a + st + b
    return st


class Func:
    def __init__(self, func_len):
        self.func_len = func_len
        self.func_coe_list = [0]*func_len
        self.func_power_list = list(range(1, func_len + 1))

    def add_thing(self, coefficient, power):
        self.func_coe_list[power-1] = coefficient

    def printf(self, reverse=False):
        if reverse is False:
            p_a = ""
            for i in range(1, self.func_len + 1):
                if int(self.func_coe_list[-i]) == 0:
                    continue
                else:
                    p_a = p_a + str(self.func_coe_list[-i]) + "x^" + str(self.func_power_list[-i]) + " + "
            print(p_a[:-2])
        elif reverse is True:
            p_a = ""
            for i in range(self.func_len):
                if int(self.func_coe_list[i]) == 0:
                    continue
                else:
                    p_a = p_a + str(self.func_coe_list[i]) + "x^" + str(self.func_power_list[i]) + " + "
            print(p_a[:-2])
        else:
            print("error")


if __name__ == '__main__':
    a = Func(9)
    a.add_thing(7, 9)
    a.add_thing(9, 3)
    a.add_thing(8, 5)
    a.add_thing(2, 1)
    print(a.func_power_list, a.func_coe_list)
    a.printf()

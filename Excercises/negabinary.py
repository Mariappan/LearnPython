#!/usr/bin/env python

lookup_table = {
                0:(0,0,0),
                1:(0,0,1),
                2:(1,1,0),
                3:(1,1,1),
                4:(1,0,0)
               }

def normalise(a, b):
    if not a: a.append(0)
    if not b: b.append(0)

    len_a, len_b = len(a), len(b)
    if len_a == len_b:
        return

    if len_a > len_b:
        b.extend([0]*(len_a - len_b))
    else:
        a.extend([0]*(len_b - len_a))

def calcAddition(a, b):
    add = list()
    carry, carry2, carry2_next = 0, 0, 0

    normalise(a, b)

    for i in range(len(a)):
        addval = a[i] + b[i] + carry + carry2
        carry2 = carry2_next
        carry2_next, carry, bitval = lookup_table[addval]
        #print ("Add is " + str(addval) + "C is " + str(carry2) + " " + str(carry) + " bit is " + str(bitval))
        add.append(bitval)

    #print ("C is " + str(carry2_next) + " " + str(carry2) + " " + str(carry))
    if not(carry == 1 and carry2 == 1 and carry2_next == 1):
        while 1 == carry or 1 == carry2:
            addval = carry + carry2
            carry2 = carry2_next
            carry2_next, carry, bitval = lookup_table[addval]
            add.append(bitval)

    while len(add) > 1 and 0 == add[-1]:
        add.pop()

    return add

def negabinary(i, _print=False):
    if i == 0:
        digits = [0]
    else:
        digits = list()
        while i != 0:
            i, remainder = divmod(i, -2)
            if remainder < 0:
                i, remainder = i + 1, remainder + 2
            digits.append(int(remainder))
    if _print is True:
        print("Exp is " + str(digits))
    return digits

def testCase(a, b):
    print ("======================================================")
    print ("Sum of " + str(a) + " " + str(b) + " is " + str(a+b))
    print ("Sum is " + str(calcAddition(negabinary(a), negabinary(b))))
    negabinary(a+b, True)


testCase(-23, 12)
testCase(9, 4)
testCase(5730, -2396)
testCase(-12, 4)
testCase(2, -2)
testCase(-9, -5)
testCase(-9, -14)

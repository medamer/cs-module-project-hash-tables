"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
for a in range(len(q)):
    for b in range(a+1, len(q)):
        for c in range(b+1, len(q)):
            for d in range(c+1, len(q)):
                print("f({}) + f({}) = f({}) - f({})      {} + {} = {} - {}".format(q[a],q[b],q[c],q[d],f(q[a]), f(q[b]), f(q[c]), f(q[d])))
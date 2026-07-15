a = 85
def fun():
    global a
    a = 25
    print(a)

fun()
print(a)

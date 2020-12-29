# gil-global interpreter lock
import dis
def add(a):
    a = a + 1

x = 1
add(x)
print(x)
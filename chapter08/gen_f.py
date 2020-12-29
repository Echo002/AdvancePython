# 只要存在yield就是生成器
def gen_fun():
    yield 1
    yield 2
# 惰性求值，延迟求值提供了可能
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list
# 问题：当re_list很大的时候，直接返回会非常消耗内存

def gen_fib2(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

def fun():
    return 1

if __name__ == "__main__":
    # 生成器对象，python编译字节码的时候产生
    gen = gen_fun()
    # for value in gen:
    #     print(value)
    # re = fun()
    print(fib(10))
    print(fib2(10))
    for data in gen_fib2(10):
        print(data)
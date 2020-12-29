import inspect
import dis
frame = None
# python中函数的工作原理
def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

# 解释器使用PyEval_EvalFramEx(C函数)去执行foo函数
# 首先会创建一个栈帧(stack_frame)，它是一个字节码对象
# 调用子函数bar时，又会创建一个栈帧
# 所有的栈帧都会分配在堆内存中，决定了栈帧可以独立于调用者存在

# 查看字节码
# import dis
# print(dis.dis(foo))

def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 30
    return "imooc"

gen = gen_func()
# print(dis.dis(gen))

print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

# foo()
# print(frame.f_code.co_name)
# caller_frame = frame.f_back
# print(caller_frame.f_code.co_name)
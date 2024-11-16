import time
配置 = 1

def debug(a):
    时间 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
    if 配置 == 1:
        print(f'{时间},debug:{a}')
    return f'{时间},debug:{a}'
def bug(a):
    时间 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
    print(f'{时间},bug:{a}')
    return f'{时间},bug:{a}'
def problem(a):
    时间 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
    print(f'warning!!! in {时间},a problem:{a}')
    return f'{时间},problem:{a}'
def warning(a):
    时间 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
    print(f'warning!!! in {时间},a warning:{a}')
    exit(1)
    return f'{时间},warning:{a}'
def erron(a):
    时间 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
    print(f'warning!!! in {时间},a erron:{a}')
    exit(1)
    return f'{时间},erron:{a}'

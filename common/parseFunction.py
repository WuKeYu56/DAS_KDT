import time

def do_step(das, steps):
    results = []
    for step in steps:
        key = step["key"]
        obj = step["object"]
        obj = tuple(obj.split('=', 1))
        if hasattr(das, key):
            func = getattr(das, key)
            if len(step) == 2:
                if len(obj) == 1:
                    rlt = func(obj[0])
                else:
                    if key == 'open':
                        obj = obj[0]+'='+obj[1]
                        print(f'函数open链接：{obj}')
                    rlt = func(obj)
            elif len(step) == 3:
                rlt = func(obj, step["param"])
            results.append(rlt)
        else:
            print("传入关键字错误，请检查用例")
            results.append(False)
        if "" not in results and False not in results:
            result = True
        else:
            result = False
        time.sleep(1)
    return results, result
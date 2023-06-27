from common.parseXLS import Parse

def get_data(datafile, module_name='login'):
    tcs = data(datafile)
    tc = []
    for t in tcs:
        if t.module == module_name and int(t.mark) == 1:
            tc.append(t)
    return tc

def data(datafile):
    p = Parse(datafile)
    p.get_sheet("Sheet1")
    # p.get_sheet()
    tcs = p.prepare_tc()
    return tcs

if __name__ == '__main__':
    # print(data('D:\code\DAS_KDT\\testdata\case1.xls'))
    a = get_data('D:\code\DAS_KDT\\testdata\case2.xls', 'projects')
    for b in a:
        print(b.title)
        print(b.mark)
        print(b.module)
        print(b.steps)
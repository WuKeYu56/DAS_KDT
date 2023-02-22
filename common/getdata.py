from common.parseXLS import Parse

def data(datafile):
    p = Parse(datafile)
    p.get_sheet("Sheet1")
    tcs = p.prepare_tc()
    return tcs

if __name__ == '__main__':
    print(data('D:\code\DAS_KDT\\testdata\case1.xls'))
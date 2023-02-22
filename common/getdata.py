from common.parseXLS import Parse

def data():
    p = Parse("D:\code\DAS_KDT\\testdata\case1.xls")
    p.get_sheet("Sheet1")
    tcs = p.prepare_tc()
    return tcs

if __name__ == '__main__':
    print(data())
class solution:
    def isHappy(self):
        value = input('Enter a positive integer:')  # value为一字符串
        set_1 = set(value)
        while True:
            sum_1 = 0
            for each in value:
                sum_1 += int(each)**2
            if sum_1 == 1:
                return True
            else:
                value = str(sum_1)
                if value in set_1:
                    return False
                set_1.add(value)

s = solution()
while True:
    prompt = int(input('Do you want to continue? 1 to continue,others to break:'))
    if prompt == 1:
        flag = s.isHappy()
        if flag:
            print('Yes')
        else:
            print('No')
    else:
        break
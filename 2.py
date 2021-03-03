class solution:
    def prime(self,n):
        if n < 3:
            return 0
        prim = [1]*n  # 下标0~n-1代表数据0~n-1
        prim[0] = prim[1] = 0
        for each in range(2,int(n**0.5)+1):
            if prim[each]:
                t = 1
                while each*(t+1) < n:
                    prim[each*(t+1)] = 0
                    t += 1
        for each in range(0,n):
            if prim[each]:
                print(each,end=' ')
        print('\n')
        return sum(prim)

s = solution()
result = s.prime(200)

# 第一次修改
# 第二次修改(在newdev分支上)
# 第三次修改(为了生成分支图)
# 第四次修改
# 第五次修改
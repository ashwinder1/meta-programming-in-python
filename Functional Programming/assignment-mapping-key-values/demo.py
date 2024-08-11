def f(x): return x * 2
def m(y): return y % 2 == 0

c_list = [1,2,3,4]

flist = list(filter(f, c_list))
print(c_list)
print(flist)

mlist = list(map(m, c_list))
print(c_list)
print(mlist)
from operator import add
def judgeCircle(string):
    list1 = list(string)
    dic = {
        'U': [1, 0],
        'D': [-1, 0],
        'R': [0, 1],
        'L': [0, -1],
    }
    pos = [0, 0]
    for c in list1:
        x = dic.get(c)
        pos = list(map(add, pos, x))

    if pos == [0, 0]:
        return True
    else:
        return False


print(judgeCircle('LLRR'))

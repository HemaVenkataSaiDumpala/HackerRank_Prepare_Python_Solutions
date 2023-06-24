if __name__ == '__main__':
    N = int(input())
    list_1=[]
    str1=""
    str2=""
    str3=""
    for _ in range(N):
        cmd = input()
        if 'insert' in cmd:
            str1,str2,str3=cmd.split(" ")
            pos=int(str2)
            val=int(str3)
            list_1.insert(pos,val)
        elif 'print' in cmd:
            print(list_1)
        elif 'remove' in cmd:
            str1,str2=cmd.split(" ")
            val=int(str2)
            list_1.remove(val)
        elif 'append' in cmd:
            str1,str2=cmd.split(" ")
            val=int(str2)
            list_1.append(val)
        elif 'sort' in cmd:
            list_1.sort()
        elif 'pop' in cmd:
            list_1.pop()
        elif 'reverse' in cmd:
            list_1.reverse()
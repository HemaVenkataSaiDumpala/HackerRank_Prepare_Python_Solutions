if __name__ == '__main__':
    list_1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_1.append([name,score])
    #print(type(list_1))
    list_1.sort(key=lambda list_1:list_1[1])
    first_lowest_val=list_1.pop(0)
    if __name__ == '__main__':
    list_1=[] 
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_1.append([name,score])
    #print(type(list_1))
    list_1.sort(key=lambda list_1:list_1[1])
    
    #for i in list_1:
    #    print(i)
    first_lowest=list_1[0][1]
    #print(first_lowest)
    count=0
    for i in list_1:
        for j in [1]:
            if i[j]==first_lowest:
                count=count+1
   
    
    if count==1:
        first_lowest_val=list_1.pop(0)
    elif count>1:
        for i in range(0,count):
                list_1.pop(0)

    second_lowest=list_1[0][1]
    #print(second_lowest)
    count=0
    for i in list_1:
        for j in [1]:
            if i[j]==second_lowest:
                count=count+1
            
    list_final=[]
    if count==1:
        print(list_1[0][0])
    elif count>1:
        for i in range(0,count):
            for j in [0]:
                list_final.append(list_1[i][j])
                
    list_final.sort(key=lambda list_final:list_final[0])    
    for i in list_final:
        print(i)                    
            
     
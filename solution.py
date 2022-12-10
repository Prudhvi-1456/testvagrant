# Online Python - IDE, Editor, Compiler, Interpreter
input_array=[[3,3,3,3,3,5,6],[2.5, 2.5 ,2.5, 2.5, 2.5, 4, 4],[4,4,4,4,4,4,10],[1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],[2, 2, 2, 2, 2, 4 ,4
]]
n={}
n["TOI"]=sum(input_array[0])
n["Hindu"]=sum(input_array[1])
n["ET"]=sum(input_array[2])
n["BM"]=sum(input_array[3])
n["HT"]=sum(input_array[4])
weekly_budget=int(input())
categories=["TOI","Hindu","ET","BM","HT"]
answer=[]
for i in range(len(categories)):
    for j in range(i+1,len(categories)):
        if n[categories[i]]+n[categories[j]]<weekly_budget:
            tmp=[]
            tmp.append(categories[i])
            tmp.append(categories[j])
            answer.append(tmp)
print(answer)
            


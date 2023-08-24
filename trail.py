def tuples(num1):
    if num1 %2 == 0:
        x=(num1,"none")
    else:
        x=("none",num1)
    
    return x

def partition_list(list):
    ty=[]
    for num in list:
        ty.append(tuples(num))
    return ty

num3=[5,7,8]
print(partition_list(num3))
     

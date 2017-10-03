import sys

# ln function
def ln(x):
    number = 1000000.0
    return number * ((x ** (1/number)) - 1)

#power function
def pow(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

# Num function
def num(A):
    binary = ""
    for i in range(0,len(A)):
        binary+=str(A[i])
    decimal = int(binary, 2)
    return decimal;

#Row addition
def addRows(A,B):
    addition=[0 for _ in range(len(A))]
    for i in range(len(A)):
        addition[i]=A[i] | B[i]
    return addition

# Output C matrix
def output(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(j!=len(matrix)-1):
                print(matrix[i][j], end=',')
            else:
                print(matrix[i][j])

def RowFromBottom(B,number):
    return B[len(B)-number]

# Import array
def import_list(file):
    with open(file) as f:
        list1 = f.readlines()
    list1 = [x.strip() for x in list1]
    return_array = []
    for i in list1:
        split_list = [int(n) for n in i.split(",")]
        return_array.append(split_list)
    return return_array

def four_russians(first_array,second_array,n):
    m= int(ln(n))+1
    # check if n can be divided by m and then add a column in A and a row in B
    size=n
    if(n%m!=0):
        for i in range (0 ,len(first_array)):
            for l in range(0,m-n%m):
                first_array[i].append(0)
        for l in range(0, m-n % m):
            temp = [0 for _ in range(n)]
            second_array.append(temp)
        size=n+n%m
    #cut A in parts
    A=[]
    i=0
    while(i<size):
        atemp = [[] for _ in range(n)]
        for j in range (i,i+m):
            for k in range(0,n):
                atemp[k].append(first_array[k][j])
        A.append(atemp)
        i = i + m

    #cut B in parts
    B=[]
    i=0
    while(i<size):
        Bi=[]
        for j in range (i,i+m):
            Bi.append(second_array[j])
        B.append(Bi)
        i=i+m
    C = [[0 for _ in range(n)] for __ in range(n)]
    ceil = -(-n//m)
    for i in range(0,ceil):
        rs = [[0 for _ in range(n)] for __ in range(pow(2,3))]
        bp = 1
        k = 0
        for j in range(1,pow(2,m)):
            rs[j]=addRows(rs[j-pow(2,k)],RowFromBottom(B[i],k+1))
            if(bp==1):
                bp = j + 1
                k = k + 1
            else:
                bp = bp - 1
        Ctemp = [[0 for _ in range(n)] for __ in range(n)]
        for j in range(0,n):
            Ctemp[j]=rs[num(A[i][j])]
        for row in range(0,n):
            for column in range(0,n):
                C[row][column] = C[row][column] | Ctemp[row][column]
    return C


if(len(sys.argv) > 2):
    first_array=import_list(sys.argv[1])
    second_array=import_list(sys.argv[2])
    n= len(first_array)
    C = four_russians(first_array,second_array,n)
    output(C)
elif(len(sys.argv)>1):
    with open(sys.argv[1]) as f:
        list1 = f.readlines()
    list1 = [x.strip() for x in list1]
    graph = []
    for i in list1:
        split_list = [int(n) for n in i.split(" ")]
        graph.append(split_list)
    max=graph[len(graph)-1][1]+1
    adjacency_matrix = [[0 for _ in range(max)] for __ in range(max)]
    for g in graph:
        adjacency_matrix[g[0]][g[1]]=1
    for i in range(len(adjacency_matrix)):
        adjacency_matrix[i][i]=1
    for i in range(0,max-1):
        adjacency_matrix = four_russians(adjacency_matrix, adjacency_matrix, max)
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if(adjacency_matrix[i][j]==1):
                print(str(i)+" "+str(j))
else:
    print ("Wrong parameters!")

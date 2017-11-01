### PREYANSH RASTOGI {2017176}  
### VAIBHAV SARDA    {2017320}


### IP HW 4

def input_matrix():
    '''
    Takes input from the user in the following form:
    
		first line ----> no. of rows (no. of sub-lists in a matrix)
		next line ----> no. of columns (no. of elements in each list)
		next line ----> space-separated elements of a particular row
    '''
    A=[]
    m=int(input())
    n=int(input())
    for i in range (m):
        x=[]
        k=str(input())
        z=k.split(' ')
        for j in range (n):
            x.append(int(z[j]))
        A.append(x)
    return A

def Row_Transformation(A,x,row1,row2):
    '''
    Performs row transformation on matrix A in the following manner:
	   row2 ----> row2 + x*(row1)
    Preconditions:
    ● A is a matrix containing integers
    ● x is of type double
    ● The possible values for the arguments ​row1 and ​row2 are ​0, ..., nrows - 1, where nrows in number of rows in A 
    '''
    i=0
    for c in A[row2]:
        c+=x*A[row1][i]
        A[row2][i]=c
        i+=1
    

def swapRows(A,row1,row2):
    '''
     Swaps two rows of a given matrix. 
		It takes three arguments:
		1) A ----> represents the matrix
		2) Possible values for parameters row1 and row2 are 0,1,2,...,nrows-1
		Here, nrows is number of rows in A.
    '''
    temp=A[row1]
    A[row1]=A[row2]
    A[row2]=temp
    
def swapColumns(A,col):
    '''
    Swaps a column (col) of matrix A with the last column of matrix A
    '''
    m=len(A)
    n=len(A[0])
    for i in range(m):
        temp      = A[i][col]
        A[i][col] = A[i][n-1]
        A[i][n-1] = temp


def transpose(A):
    '''
    Takes transpose of a matrix A and returns the transposed matrix
    '''
    m=len(A)
    n=len(A[0])
    B=[]
    for i in range(n):
        x=[]
        for j in range(m):
            a=A[j][i]
            x.append(a)
        B.append(x)
    return B
    
def MatrixRank(A):
    '''
    Finds rank of matrix A.
	    Takes a nested list (representing a matrix) as an argument 
	    and returns an integer representing the rank of A.

	    Precondition: A is a matrix containing integer elements.
    '''
    row=0
    m=len(A)
    n=len(A[0])
    
    if n > m:
        B = transpose(A)
        A = B
        
    m=len(A)
    n=len(A[0])
    rank=n
    g=0
    while row <=  rank-1:
        
            y= A[row][row]
            if y != 0:
                for i in range (m):
                    x=A[i][row]   
                    if x != 0 and i!=row:
                        Row_Transformation(A,y-1,i,i)
                        Row_Transformation(A,-x,row,i)
                    
            else:
                if row == m-1:
                    rank=rank-1
                else:
                    flag=0
                    for i in range(row,m):
                        if A[i][row] != 0 and flag ==0 :
                            j = i
                            flag = 1
                    if flag ==  1:
                        swapRows(A,j,row)
                        row=row-1
    
                    else:
                        temp=1
                        for i in range(m):
                            if A[i][row]!=A[i][n-1] :
                                temp=0
                        swapColumns(A,row)
                        if temp == 0:
                            row-=1
                            rank-=1
                        else:
                            g+=1
                        

                            
            row+=1
    rank=rank-g
    return rank
    
if __name__=='__main__':
    A=[]
    A=input_matrix()
    rank=MatrixRank(A)
    print(rank)

from prettytable import PrettyTable

def is_symmetric (A, n):
    for i in range(n):
        for j in range(i-1):
            if A[i][j] != A[j][i]:
                return False
    return True


def LU (A, n):
    for k in range(n):
        for i in range(k+1, n):
            if A[k][k] == 0:
                print("ERROR! One of the leading principal submatrices is not singular.")
                exit()
            A[i][k] /= A[k][k]
            for j in range(k+1, n):
                A[i][j] -= (A[i][k] * A[k][j])


def print_LDLT (A, n):
    if is_symmetric(A, n) == False:
        print("ERROR! The matrix is not symmetric.")
        exit()
    LU(A, n)

    L = PrettyTable()
    for i in range(n):
        l_row = []
        for j in range(n):
            if j == i:
                l_row.append(1)
            elif j > i:
                l_row.append(0)
            else:
                x = A[i][j]
                if x % 1 == 0:
                    l_row.append(int(x))
                else:
                    l_row.append(x)
        L.add_row(l_row)
    print("\nL:")
    L.border, L.header = False, False
    print(L)

    D = PrettyTable()
    for i in range(n):
        d_row = []
        for j in range(n):
            if i != j:
                d_row.append(0)
            else:
                x = A[i][j]
                if x % 1 == 0:
                    d_row.append(int(x))
                else:
                    d_row.append(x)
        D.add_row(d_row)
    print("\nD:")
    D.border, D.header = False, False
    print(D)


n = int(input("Enter the number of columns and rows:"))
print("Enter the matrix (separate columns with tab or space and separate rows with enter):")
A = []
for i in range(n):
    A.append([])
    inp = input().split()
    for j in range(n):
        if len(inp) == 0:
            print("ERROR! The number of columns is less than expected.")
            exit()
        A[i].append(float(inp.pop(0)))
    if len(inp) > 0:
        print("ERROR! The number of columns is greater than expected.")
        exit()

print_LDLT(A, n)
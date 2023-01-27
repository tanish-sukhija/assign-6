def pascaltriangle(n):
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[j - 1] * (i - j + 1) // j)
        print(' '.join(str(x) for x in row))

n = int(input("Enter the number of rows: "))
pascaltriangle(n)
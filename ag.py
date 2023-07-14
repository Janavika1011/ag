A = input("Enter: ")
count = 0
for i in range(len(A) - 1):
    if A[i] == 'A' and A[i + 1] == 'G':
        count += 1

print(count)

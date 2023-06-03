lis = [0,1,2,3,4,5,6,7,8,9]
lis2 = []


def traverse(start, middle, end):
    left = (start+middle)//2
    right = -(-(middle+end)//2)

    if left != middle:
        lis2.append(lis[left])
        traverse(0, left, middle)

    if right != middle:
        lis2.append(lis[right])
        traverse(middle, right, end)

traverse(0, len(lis)//2 , len(lis))
print(lis2)
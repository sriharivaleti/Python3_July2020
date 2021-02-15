def almostIncreasingSequence(sequence):
    count=0;
    i=0;
    while i<len(sequence):
        if (i+1) < len(sequence) and  sequence[i]>=sequence[i+1]:
            count= count +1 
        i= i+1
    print('count :', count)
    if count >1:
        return False
    else:
        return True

print(almostIncreasingSequence([1, 2, 1, 2]))
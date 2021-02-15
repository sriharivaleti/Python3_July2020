def adjacentElementsProduct(inputArray):
    products = []
    i=0
    while i < len(inputArray)-1:
        if inputArray[i+1] != None:
            products.append(inputArray[i+1] * inputArray[i])
        i=i+1
    products.sort()
    print(products)
    return products[len(products)-1]


print(adjacentElementsProduct([5, 1, 2, 3, 1, 4]))


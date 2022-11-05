for i in range(98):
    j = 99 - i
    k = j - 1
    print(j + "bottles of beer on the wall, " + j + " bottles of beer,")
    if(j != 1):
        print("Take one down and pass it around, " + k + " bottles of beer on the wall")
    else:
        print("Take one down and pass it around, no more bottles of beer on the wall")
        print("No more bottles of beer on the wall, no more bottles of beer")
        print("Go to the store and buy some more, 99 bottles of beer on the wall")
        

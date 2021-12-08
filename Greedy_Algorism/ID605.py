def canPlaceFlowers(flowerbed, n):
        num = 0
        l = len(flowerbed)
        if l > 2:
            if (flowerbed[0] == 0) and (flowerbed[1] == 0):
                flowerbed[0] = 1
                num += 1
            for i in range(0,l-2):
                if (flowerbed[i] == 0) and (flowerbed[i+1] == 0) and (flowerbed[i+2] == 0):
                    flowerbed[i+1] = 1
                    num += 1
            if (flowerbed[l-1] == 0) and (flowerbed[l-2] == 0):
                flowerbed[l-1] = 1
                num += 1
        # return (n <= num,num)
        if l==1 and flowerbed[0]==0:
            num = 1
        if l==2 and flowerbed[0]==0 and flowerbed[1]==0:
            num = 1
        return (n <= num)

# print(canPlaceFlowers([1,0,0,0,1],1))#Ture
# print(canPlaceFlowers([1,0,0,0,1],2))#False
# print(canPlaceFlowers([0,0,0,0,1],2))#Ture##
# print(canPlaceFlowers([0,0,0],2))#Ture
# print(canPlaceFlowers([1,0,0,0,1,0,0],2))#Ture##
print(canPlaceFlowers([1,0,0,0,0,1],2))#False##
print(canPlaceFlowers([1,0,0,1],2))#False##
print(canPlaceFlowers([1,0,0,0,0,0,1],2))#Ture##
print(canPlaceFlowers([1,0,0,0,0,0,1],2))
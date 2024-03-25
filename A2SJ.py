import pygame
#PyGame
#Samuel Joseph
#Assignment 2 

#Initialize 
pygame.init()
#sound effects
beep = pygame.mixer.Sound('chime_down.wav')

#Code block for merge sort
def mergeSort(all, start, middle, end):
    leftSize = middle - start + 1
    rightSize = end - middle

    lefty = [0] * leftSize
    
    righty = [0] * rightSize

    for i in range(0, leftSize):
        lefty[i] = all[start+i]

    for j in range(0, rightSize):
        righty[j] = all[middle+1+j]
    i,j,k=0,0,start
    while i<leftSize and j<rightSize:
        if lefty[i]<=righty[j]:
            all[k]=lefty[i]
            i+=1
        else:
            all[k] = righty[j]
            #BEEP FOR SWAP
            beep.play
            j+=1
        k+=1

    while i<leftSize:
        all[k] = lefty[i]
        i+=1
    while j<rightSize:
        all[k] = righty[j]
        #BOOP BEEP
        beep.play
        j+=1
        k+=1
        #Showing where you currently are and using a print function 
        print(f"Currently Here: {all[start:end+1]}")

def breakandputbacktogether(numz, start, end):
    if start<end:
        middle = start+(end-start)//2
        breakandputbacktogether(numz,start,middle)
        breakandputbacktogether(numz,middle + 1,end)
        mergeSort(numz,start,middle,end)

# PRODUCT ID TO SORT
product = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("We have:", product)

# SORT THE PRODUCT ID
breakandputbacktogether(product, 0, len(product)-1)

# ALL SORTED
print("Sorted!!!", product)





# Task 6 : Sum of 2 Numbers

##

## Step-1: Function CountSum(list,target)

### Step-1.A : Iterate through elements of list, choose the first number of pair
    for i = 0 to length(list) -1 :
### Step-1.B : Start another loop to choose the second number 
    for j = j+1 to length (list) - 1

### Step-1.C : Check if sum of pair is equal to target
    if list[i]+list[j] == target :  
        return [i,j]

## Step-2 : Take input from user for list and target
    list[]
    integer target
## Step-3 : Call function CountSum(list,target)
    CountSum(list,target)
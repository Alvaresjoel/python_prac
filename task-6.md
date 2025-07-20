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



# Dry Run

# Example 1

    Input: list = [2,7,11,15], target = 9 
    Output: [0,1]

    for i <- 0 to 3 :
        for j : i+1 => 1 to 3:
            if list[0] + list [1] => 
            2 + 7 =>
             9 == 9 => true:
                return [0,1] 


# Example 2

    Input: nums = [3,2,4], target = 6 
    Output: [1,2] 

    for i<- 0 to 2 :
        i <- 0
        for j <- 1 to 2:
            j <- 1 => list[0] + list[1]
            if 3 + 2 == 6 => false
            j <- 2 => list[0] + list[2]
            if 3 + 4 == 6 => false
        i <- 1
        for j <- 2 to 2:
            j<- 2: list[1]+list[2]
            if  2+4 == 6 => true: 
                return [1,2]



# Example 3

    Input: nums = [3,3], target = 6 
    Output: [0,1]

    for i <- 0 to 1:
    i <- 0
    for j <- 1 to 1:
        j <- 1  => list[0] + list[1]
        if 3 + 3 == 6 => true:
            return [0,1]

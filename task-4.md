# Task 4: Pattern Formation: Diamond

## Step-1: Function StarPattern(number)

### Step-1.A : Divide the diagram into Upper Half and Lower Half
     
  - Upper Half
  
        for i <- 1 to n :
            print spaces (n-i)
            print stars (2*i - 1)
   
  - Lower Half:
  
        for i <- n-1 to 1 :
            print spaces (n-i)
            print stars(2*i - 1) 

## Step-2: Take input from user
    integer n
## Step-3 : Call function StarPattern(n)
    StarPattern(n)



# Dry Run

# Example 1
        Input : 4
        Output :    
            * 
           *** 
          ***** 
         ******* 
          ***** 
           *** 
            *      

    n <- 4

    StarPattern(4)

    Upper Half:
    for i <- 1 to 4:
        i <- 1
        print space (4-1) => space(3)
        print star (2*1 - 1) => star(1)

        "_""_""_"*
    
    for i <- 2 to 4:
        i <- 2
        print space (4-2) => space(2)
        print star (2*2 - 1) => star(3)

        "_""_"***

    for i <- 3 to 4:
        i <- 3
        print space (4-3) => space(1)
        print star (2*3 - 1) => star(5)

        "_"*****
    for i <- 3 to 4:
        i <- 4
        print space (4-4) => space(0)
        print star (2*4 - 1) => star(7)

        *******
    Lower Half:

    for i <- 3 to 1:
        i <- 3
        print spaces (4-3) => space(1)
        print stars(2*3 - 1)  => star(5)
        "_"*****
    for i <- 2 to 1:
        i <- 2
        print space (4-2) => space(2)
        print star (2*2 - 1) => star(3)
        "_""_"***
    for i <- 1 to 1:
        i <- 1
        print space (4-1) => space(3)
        print star (2*1 - 1) => star(1)
        "_""_""_"*


    
    
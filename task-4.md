# Task 4: Pattern Formation: Diamond

## Step-1: Function StarPattern(number)

### Step-1.A : Print above half
     '*'
    '***'
   '*****'
  '*******'
  Upper Half
    for i <- 1 to n
        print spaces n-i
        print stars (2*i - 2)
   *****
    ***
     *
  Lower Half
    for i <- n-1 to 1 
        print spaces n-i
        print stars(2*i - 1) 

## Step-2: Take input from user
    integer n
## Step-3 : Call function StarPattern(n)
    StarPattern(n)
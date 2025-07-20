# Task 3: Area of Rectangle

##

### Step 1 : Define a class Rectangle with width and height attributes
    Class Rectangle 
        private height, width

### Step 1.A: Create a constructor to set width and height
        Method Constructor(w,h)
            width <- w
            height <- h
### Step 1.B: Create a method CalculateArea to calculate area of Rectangle
        Method CalculateArea()
            return width x height
        
### Step 2: Take height and width input from user
    integer h,w


### Step 3: Create an object and call CalculateArea

    object rectangle <- Rectangle(w,h)
    integer area <- rectangle.CalculateArea()
    print area

# Dry Run

# Example 1

## Input (10,12)

## Output 120

    w <- 10     
    h <- 12 

    rectangle <- Rectangle(10,12)

    area <- rectangle.CalculateArea(10,12):
            return 10 x 12

    print 120


# Example 2

## Input (14,15)

## Output 120

    w <- 14     
    h <- 15 

    rectangle <- Rectangle(14,15)

    area <- rectangle.CalculateArea(14,15):
            return 14 x 15

    print 210
    
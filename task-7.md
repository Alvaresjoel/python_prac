# Task 7 : Product Catalog System (Class, Object, List)

## Step 1: Define a class Product with attributes name,price and category and method display_info
    Class Product 

        Attributes : name,price,category

        Method display_info(name)
        Print(name,
            price
            category)

## Step 1.A: Find max price product
    Method max_price(product_list)
        string max_product 
        integer max_price <- 0
        for each product in product_list:
            if product.price > max_price :
                    max_price <- product.price



## Step-2: Create multiple product objects to store 
    string name , category
    integer price
    product_list[]
    flag <- true
    while(flag):
        input(name,price,category)
        new_product <- product(name,price,category)
        product_list.add(new_product)

        if user_input <- no:
            flag <- true 
    
## Step-3: Find product with highest price 
    
    print "highest price " max_price(product_list)


# Dry Run

# Example 1

    Input: 
    Enter product details: Phone, 30000, Electronics 
    Enter product details: Pen, 20, Stationery 
    
    Output: 
    Highest price product is Phone costing ₹30000

    flag <- true
    while(true):

        name <- Phone
        price<- 30000
        category <- Electronics
        product_list = [(Phone,30000,Electronics)]

        name <- Pen
        price<- 20
        category <- Stationery
        product_list = [(Pen,20,Stationery)]

        flag <- false
    maximum_product <- Product.max_price(product_list):
        max_price <- 0
        string max_product 
        for product in product_list :
            product <- Phone
            if product.price => 30000 > 0:
                max_price <- 30000
                max_product <- Phone

            product <- Pen
                if product.price => 20 > 0:
                max_price <- 30000
                max_product <- Phone
        
        return Phone
        
    Product.display_info(maximum_product)
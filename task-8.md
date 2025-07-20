# Task 8 : Unique Words Extractor (Set)

## Step-1: Function UniqueWord(paragraph)

### Step-1.A: Initialise a set to store words
    Set unique_words
### Step-1.B: Iterate through the elements of paragraph
    for each character in paragraph
### Step-1.C: Check if words are formed due to space and push to set
    string new_word
    if character == " ":
        push new_word to unique_word 
        new_word = ""
    if else character == ".":
        push new_word to unique_word 
        exit
    else:
        new_word <- new_word + character
### Step-1.D: Return Set

    return unique_words



## Step-2: Take paragraph from user
    String paragraph
## Step-3: Call function UniqueWord(paragraph)
    set Word = Unique(paragraph)

## Step-4: Print Set
    print 
    


# Dry Run

## Example-1

    Input: 
    Enter a paragraph: Hello world! Hello Python. 
    
    Output: 
    Unique words: ['hello', 'python', 'world']


## Step-2:
    paragraph <- Hello world! Hello Python. 
    Word <- UniqueWord(paragraph)

# 
    UniqueWord(paragraph):
        set unique_words
        for each character in paragraph:
            
            character = 'h'
            new_word = "" + "h" => "h"

            character = 'e'
            new_word = "h" + "e" => "he"

            character = 'l'
            new_word = "he" + "l" => "hel"

            character = 'l'
            new_word = "hel" + "l" => "hell"

            character = 'o'
            new_word = "hell" + "o" => "hello"

            character = " " (space)
            if character == " " => true :
            
                unique_words.push(new_word) => unique_words = {"hello"}

                Reset new_word = ""

            character = 'w'
            new_word = "" + "w" => "w"

            character = 'o'
            new_word = "w" + "o" => "wo"

            character = 'r'
            new_word = "wo" + "r" => "wor"

            character = 'l'
            new_word = "wor" + "l" => "worl"

            character = 'd'
            new_word = "worl" + "d" => "world"

            character = " " (space)
            if character == " " => true :
            
                unique_words.push(new_word) 
                unique_words = {"hello", "world"}
                Reset new_word = ""

            character = 'h'
            new_word = "" + "h" => "h"

            character = 'e'
            new_word = "h" + "e" => "he"

            character = 'l'
            new_word = "he" + "l" => "hel"

            character = 'l'
            new_word = "hel" + "l" => "hell"

            character = 'o'
            new_word = "hell" + "o" => "hello"

            character = " " (space)
            if character == " " => true :
            
                unique_words.push(new_word) => unique_words = {"hello","world"}
                // hello already in set

                Reset new_word = ""

            character = 'p'
            new_word = "p"

            character = 'y'
            new_word = "py"

            character = 't'
            new_word = "pyt"

            character = 'h'
            new_word = "pyth"

            character = 'o'
            new_word = "pytho"

            character = 'n'
            new_word = "python"

            if character == "." :
                unique_word.push(new_word)
                unique_words = {"hello", "world", "python"}

            


            
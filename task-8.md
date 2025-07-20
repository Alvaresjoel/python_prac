# Task 8 : Unique Words Extractor (Set)

## Step-1: Function UniqueWord(paragraph)

### Step-1.A: Initialise a set to store words
    Set unique_words
### Step-1.B: Iterate through the elements of paragraph
    for each character in paragraph
### Step-1.C: Check if words are formed due to space and push to set
    string new_word
    if character == " ":
        push new_word to unique_word set
        new_word = ""
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


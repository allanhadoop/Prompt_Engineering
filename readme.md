# Prompt engineering

1. Give direction, Specify format, Provide examples, Evaluate quality(Run multiple times), Divide labor (multiple supporting prompts) 
2) Template - 
Brainstrom a list of product names for a {product description}, in the style of {famous inventor}
Return the results as a comma separated list, in this format : 
Product description: a shoe that fits any foot size
Product names : [list of 3 product names
##Examples
{Product examples}
3) Use """ .............Text..........""" and then query referencing document in quotes. 
4) Variables 
    a) _ _ _ Mini     = iFit Mini, Omnisneal Mini, Flexform Mini 
    b) Apple _ _ _    = Apple Flexwalk, Apple Unifit, Apple Omnifit 
    c) Specify CFG scale for better image resolution
    d) Retrieval - list related product for reference 
    e) function calls - for example - iFitShoe.com is available on GoDaddy!
    f) Seed words - For example which words you would prefer to start with 
    g) Delimiters - We can mention delimiters in the prompt . For e.g. """.............""" or [.....text.....] or < >.....< >

4) Stop hallcuniation -- " If you dont know an answer simply respond with "I dont know".

#----------------OpenAI Platform------------

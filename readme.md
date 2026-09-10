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
1. Text Generation: Use client.responses.create() with input parameter and control output with temperature and top_p
2. Structured Outputs: Define JSON schemas or use Pydantic models with text.format to get typed, validated responses
3. Image Generation: Use the image_generation tool in the Responses API to generate images with options for quality, size, and transparent backgrounds

4. Multimodal: Vision (image analysis), text-to-speech, and speech-to-text capabilities are all available through the API
5. Function Calling: Define tools with JSON schemas and handle tool calls in an agentic loop
6. Reasoning Models: Use effort and verbosity to control the level of reasoning and output verbosity

7. Embeddings: Generate vector representations of text for semantic search and similarity comparisons
8. Video Generation: Use the Sora API (client.videos.create()) for async text-to-video generation with progress polling
9. Deep Research: Use o3-deep-research or o4-mini-deep-research with background=True for comprehensive, multi-source research reports
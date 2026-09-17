# -----------------Quick recap-----------------------
[] - Get an item - List 
{} - Dictionary - Key value pair
.  - Get an attribute/property
[{...} {....}] - Means multiple dictionaries within the list
{ key1 : value1, key2 :value2} -- This is json object

->     This function is expected to return... For example -- 
def test(query: str, docs: list[str]) -> list[str]:
above function takes query (as a string), and list of documents (as a strings) and returns list of strings.

---------------------------------------------------------------------------------- 
| Python concept | Simple meaning               | Example                   |
| -------------- | ---------------------------- | ------------------------- |
| **Function**   | Does a job                   | `get_weather()`           |
| **Class**      | Blueprint                    | `class Car:`              |
| **Object**     | Actual thing made from class | `car1 = Car()`            |
| **Method**     | Function inside a class      | `car1.drive()`            |
| **List**       | Container                    | `[tool1, tool2]`          |
| **Dictionary** | Key-value information        | `{"name": "get_weather"}` |

1) 
* = multiple positional arguments - E.g. below
def add_numbers(*numbers):
    print(numbers)

add_numbers(10, 20, 30)             <---------------multiple

2) 
** = multiple keyword arguments
def person(**details):              <----------or def create(**kwargs): ---------->
    print(details)

person(name="Anand", age=40, city="Pune")
Python collects them into a dictionary:
details = {
    "name": "Anand",
    "age": 40,
    "city": "Pune"
}

3) 
def test(*args, **kwargs):
  print(test)

4) 
tasks = [make_single_query() for _ in range(num_runs)]         # Create list of tasks
""" above line is a short way of writing below -- if num_runs = 3 then
        tasks = [
        make_single_query(),
        make_single_query(),
        make_single_query()
        ]
we may write below 
    for i in range(3):
but here we don't care about i therefore we write below short form 
    for _ in range(3)
"""
----------------------------------------
Parameters used in Response API 
| Parameter                       | Simple meaning                                              | Example                               
| ------------------------------- | ---------------------------------------------------       - | ------------------------------------- 
| `model`                         | Which AI model to use                                       | `"gpt-5.6-luna"`                 
| `input`                         | The user's actual input/question                            | `"What is Python?"`                           
| `instructions`                  | System-level instructions telling the model how to behave   | `"Answer simply"`                      
| `text`                          | Controls the format/style of the output                     | `{"format": {"type": "json_object"}}`     
| `text.format`                   | Specifies the required output format                        | `"json_object"`                         
| `text.verbosity`                | Controls how detailed the answer should be                  | `"low"` / `"medium"` / `"high"`       
| `max_output_tokens`             | Maximum number of tokens the model can generate             | `500`                                   
| `reasoning`                     | Controls reasoning effort for models that support it        | `{"effort": "low"}`                  
| `reasoning.effort`              | How much reasoning the model should use                     | `"low"`, `"medium"`, `"high"`              
| `tools`                         | Gives the model access to external functions/tools                       | `[weather_tool]`    
| `tool_choice`                   | Controls whether/how the model uses a tool                               | `"auto"`           
| `parallel_tool_calls`           | Allows multiple tool calls at the same time                              | `True`                
| `temperature`                   | Controls randomness/creativity where supported                           | `0.7`                         
| `top_p`                         | Controls how broadly the model chooses possible next tokens              | `0.9`              
| `store`                         | Whether the response is stored for later retrieval/use                   | `True` / `False`  
| `previous_response_id`          | Connects this request to a previous response                             | `"resp_123"`                
| `conversation`                  | Associates the request with a conversation/state                         | `"conv_123"`                          
| `stream`                        | Returns the answer progressively instead of waiting for the whole answer | `True`                        
| `background`                    | Runs the response as a background task                                   | `True`                       
| `include`                       | Requests additional information in the response                          | `["..."]`                          
| `metadata`                      | Adds your own key/value information to the request                       | `{"user":"123"}`                      
| `truncation`                    | Controls what happens if the input/context is too large                  | `"auto"`                              
| `service_tier`                  | Controls the service/latency tier where available                        | `"auto"`                              
| `prompt_cache_key`              | Helps identify requests that can share cached prompt content             | `"my_app_v1"`                         
| `safety_identifier`             | Identifies an end user for safety/rate-limit purposes                    | `"user_123"`                          
| `top_logprobs`                  | Requests probabilities for likely alternative tokens where supported     | `5`                                   
| `logprobs`                      | Requests token probability information where supported                   |`True`                                
| `user` / related end-user identifiers | Associates requests with an end user where supported               | `"user_123"`                 

----------------------------------------
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

#--------------Token count scenarios - 
1. Approaching context limits - Models have fixed context windows (e.g., 128K for GPT-4o). Exceeding causes truncation or errors.
(Count tokens before sending; truncate or summarize if needed)

2. Optimizing costs - API pricing is per-token. Long prompts = higher costs. (Remove redundant text, use concise instructions)
3. Comparing prompt strategies - Different prompts may achieve similar results with fewer tokens (A/B test prompts and measure token efficiency)
4. Batch processing - Processing thousands of requests amplifies small inefficiencies (Optimize prompts before scaling)
5. RAG applications - Retrieved context adds tokens quickly (Set retrieval limits based on token budget)

Rule of thumb: If your prompt + expected response approaches 50% of the context window, start actively managing tokens.

#--------------------Agents and Tool calling ----------------

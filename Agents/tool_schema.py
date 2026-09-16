    
tool_schema_def = [
    {
            "type": "function",
            "name": "get_capital",
            "description": "Get the capital city of a country. Use this tool when the user asks for the weather in the capital of a country.",
            "parameters": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "description": "Name of the country"
                      }
                    },
                "required": ["country"],
                "additionalProperties": False
            },
            "strict": True
        },
    {
            "type": "function",
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"],
                "additionalProperties": False
            },
            "strict": True
    }
]
import openai
openai.api_key = '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'

def get_from_openai(jsondata, day):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "what the format of my daily calendar?"},
            {"role": "assistant", "content": 
             "Here's the format for your daily calendar:\n"
             + "$ [start-time]:[end-time] [event-name] <[short-description-within-25-words]>\n"
             + "$ [start-time]:[end-time] [event-name] <[short-description-within-25-words]>"},
            {"role": "user", "content": "Here's a JSON file of a person:\n" + jsondata},
            {"role": "assistant", "content": "Thank you for the information. What shall I do with it?"},
            {"role": "user", "content": "Write a day calendar for this person on " + day}
        ]
    )
    return response["choices"][0]["message"]["content"]
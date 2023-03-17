import openai

api_response = openai.Completion.create(
    model="{fine-tuned model goes here, without brackets}",
    prompt="toothpaste -->",
    temperature=0,
    max_tokens=1
)
completion_text = api_response['choices'][0]['text']
if completion_text == ' edible':
    label = 'edible'
elif completion_text == ' in':
    label = 'inedible'
else:
    label = 'other'
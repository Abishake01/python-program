import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def generate_content(title, summary):
    prompt = f"{title}\n{summary}\n\nGenerate content:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Adjust the engine based on your preference
        prompt=prompt,
        max_tokens=200  # Adjust max tokens based on desired output length
    )
    return response.choices[0].text.strip()

# Example usage
title = "Title of the content"
summary = "Brief summary or introduction"
generated_content = gene
rate_content(title, summary)
print(generated_content)
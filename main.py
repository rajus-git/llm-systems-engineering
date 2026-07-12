from openai import OpenAI


# https://developers.openai.com/api/docs/quickstart?desktop-os=windows&language=python
def main():
    print("Hello from llm-systems-engineering!")
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4o-mini",
        input="Write a one-sentence bedtime story about a unicorn.",
        
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
from openai import OpenAI
client = OpenAI()

def get_completion(prompt, model="gpt-4o-mini"): # Updated to a modern model
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices.message.content
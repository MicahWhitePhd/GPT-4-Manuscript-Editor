import openai

class GPTAPIHandler:
    def __init__(self, prompt, api_key):
        openai.api_key = api_key
        self.prompt = prompt

    def get_edited_text(self, text):
        response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"{self.prompt}"},
                    {"role": "user", "content": f"{text}"},
                ],
                temperature=1,
                max_tokens=3000
            )

        return response.choices[0].message.content.strip()

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-nano")

def summarize(text, max_tokens=300):
    prompt = f"Sammanfatta följande nyhet på svenska i 2–4 meningar:\n\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"OpenAI-sammanfattning misslyckades: {e}")
        return "Kunde inte sammanfatta nyheten just nu."
# GoToSocial Summarizer Bot 🤖📝

En AI-bot för din GoToSocial-instans som följer RSS-botar och postar korta summeringar som svar på deras inlägg.

## Funktioner

- Läser toots från angivna konton (t.ex. RSS-botar)
- Extraherar länkad artikel
- Summerar innehållet med OpenAI:s GPT-modell
- Publicerar summering som ett svar (reply)

## Kör med Docker Compose

1. Klona detta repo:
```bash
git clone https://github.com/dittkonto/gotosocial-summarizer.git
cd gotosocial-summarizer

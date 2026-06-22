import wikipedia

def search_wikipedia(query: str):
    try:
        wikipedia.set_lang("en")

        result = wikipedia.summary(
            query,
            sentences=3,
            auto_suggest=False
        )

        return result

    except Exception as e:
        return f"Error: {e}"
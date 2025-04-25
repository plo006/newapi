import wikipedia

def search_wikipedia(query):
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=2)
        return f"📘 {summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"❗ Too many results found: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return f"❌ No page found for '{query}'."
    except Exception as e:
        return f"Error: {str(e)}"

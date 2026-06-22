from ddgs import DDGS

def web_search(query):

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=5
            )

            for result in search_results:

                title = result.get(
                    "title",
                    "No Title"
                )

                body = result.get(
                    "body",
                    "No Description"
                )

                results.append(
                    f"""
Title: {title}

Snippet: {body}
"""
                )

        if len(results) == 0:
            return "No search results found."

        return "\n".join(results)

    except Exception as e:
        return f"Search Error: {e}"
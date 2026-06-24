import time
import wikipedia


def load_wikipedia(query, retries=3, delay=2):

    wikipedia.set_user_agent("KnowledgeRAG/1.0 (research project)")

    for attempt in range(retries):

        try:

            search_results = wikipedia.search(query, results=1)

            if not search_results:
                raise ValueError(f"No Wikipedia article found for: '{query}'")

            page = wikipedia.page(search_results[0], auto_suggest=False)

            return page.content

        except wikipedia.exceptions.DisambiguationError as e:

            page = wikipedia.page(e.options[0], auto_suggest=False)
            return page.content

        except ValueError:
            raise

        except Exception as error:

            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise ValueError(f"Wikipedia search failed after {retries} attempts: {error}")

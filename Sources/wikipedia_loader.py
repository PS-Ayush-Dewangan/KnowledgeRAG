import wikipedia


def load_wikipedia(query):

    try:

        search_results = wikipedia.search(
            query,
            results=1
        )

        if not search_results:

            return None

        page = wikipedia.page(
            search_results[0],
            auto_suggest=False
        )

        return page.content

    except Exception as error:

        print(error)

        return None
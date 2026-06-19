import wikipedia


def load_wikipedia(topic):

    try:

        page = wikipedia.page(
            topic,
            auto_suggest=False
        )

        return page.content

    except Exception as error:

        print(error)

        return None
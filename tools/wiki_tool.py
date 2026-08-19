import requests


def search_wikipedia(question):

    try:

        url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + question.replace(" ", "_")
        )

        headers = {
            "User-Agent": "DocumentAssistant/1.0 (student-project)"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        data = response.json()

        if "extract" in data:
            return data["extract"]

        return "No information found."

    except Exception as e:
        return f"Error: {e}"
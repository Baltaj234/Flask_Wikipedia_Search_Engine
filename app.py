from flask import Flask, request, render_template
import requests
import wikipedia

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    context = {
        "search_query": "",
        "summary": None,
        "result_title": None,
        "error": None,
        "suggestions": [],
    }

    if request.method == "POST":
        search_query = request.form.get("search", "").strip()
        context["search_query"] = search_query

        if not search_query:
            context["error"] = "Enter a topic to search."
        else:
            try:
                context["summary"] = wikipedia.summary(search_query, sentences=2)
                context["result_title"] = search_query
            except wikipedia.DisambiguationError as error:
                context["error"] = "That topic could mean a few different things."
                context["suggestions"] = error.options[:5]
            except wikipedia.PageError:
                context["error"] = "We couldn't find a Wikipedia page for that topic."
            except (wikipedia.WikipediaException, requests.RequestException):
                context["error"] = "Wikipedia is temporarily unavailable. Please try again."

    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)

 
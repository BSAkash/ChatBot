from flask import Flask, render_template, request, jsonify
import conversation


app = Flask(__name__)
app.config["DEBUG"] = True
conversation.initBrain()


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/api/', methods=["GET","POST"])
def api():
    try:
        if request.method == "POST":
            data = request.get_json()
            query = data['query']
            reply = conversation.botAnswer(query)
            # dict can also be used as param for jsonify
            return jsonify(
                response="BOT > " + reply,
                mode="reply"
            )
    except Exception as e:
        return jsonify(
            response="Error: " + str(e)
        )


if __name__ == "__main__":
    app.run()
from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def index():
    result = '\n'
    candidates = utils.get_candidates_all()

    for candidate in candidates:
        result += candidate['name'] + '\n'
        result += candidate['position'] + '\n'
        result += candidate['skills'] + '\n'
        result += '\n'

    return f' <pre> {result} </pre>'


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)

    if candidate == 'Not Found':
        return 'Not Found'

    result = '\n'
    result += candidate['name'] + '\n'
    result += candidate['position'] + '\n'
    result += candidate['skills'] + '\n'

    return f"""
        <img scr="{candidate['picture']}">
        f'<pre> {result} </pre>
    """


@app.route("/candidate/<skill>")
def get_candidates_by_skill(skill):
    result = '\n'
    candidates = utils.get_candidates_by_skill(skill)

    for candidate in candidates:
        result += candidate['name'] + '\n'
        result += candidate['position'] + '\n'
        result += candidate['skills'] + '\n'
        result += '\n'

    return f'<pre> {result} </pre>'


app.run(debug=True)

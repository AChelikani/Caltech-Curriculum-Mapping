from flask import Flask, render_template
from flask import url_for
from os import listdir


courses = [file.rstrip(".tsv") for file in filter(lambda x: ".tsv" in x, listdir("static/data"))]

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", courses=courses)


@app.route('/viz/<course>')
def viz(course):
    course_name = " ".join(course.split("_"))
    return render_template("viz.html", data_path=url_for('static', filename='data/%s.tsv' % course), course_name = course_name, courses=courses)

@app.route("/graph")
def graph():
    return render_template("graph.html", courses=courses)

if __name__ == "__main__":
    app.debug = True
    app.run()

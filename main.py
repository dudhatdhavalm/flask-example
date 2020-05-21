from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def templates():
    template_list = ["Template1", "Template2",
                     "Template3", "Template4", "Template5"]
    return render_template("templates.html", template_list=template_list)


@app.route("/examples")
def examples():
    example_list = ["Test", "Test1", "Test2", "Test3"]
    return render_template("examples.html", example_list=example_list)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact-data")
def contact_data():
    print(request.args.get("email"))
    return render_template("thankyou.html")


@app.route("/user/<name>")
def username(name):
    return "user name is " + name


if __name__ == "__main__":
    app.run(debug=True)

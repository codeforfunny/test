from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "HEAD"])
def index():
    if request.method == 'HEAD':
        return '', 200
    return render_template("index.html")

@app.route("/categories/<category>", methods=["GET"])
def category_page(category):
    if category in ["beverage", "food", "perfumes"]:
        return render_template(f"{category}.html")
    else:
        return "Category not found", 404

if __name__ == "__main__":
    app.run(debug=True)

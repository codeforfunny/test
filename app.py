from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

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

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error
    app.logger.error(f"Error: {e}")
    return "An error occurred", 500

if __name__ == "__main__":
    app.run(debug=True)

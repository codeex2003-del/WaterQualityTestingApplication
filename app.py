from flask import Flask, render_template, request

app = Flask(__name__)

class Water:
    def __init__(self, color, smell, clarity):
        self.color = color
        self.smell = smell
        self.clarity = clarity

    @property
    def is_safe(self):
        if self.smell != "low":
            return False
        if self.color == "high":
            return False
        if self.clarity == "low":
            return False
        return True

    @property
    def level(self):
        if not self.is_safe:
            return "Unsafe"
        return "Safe"

    @property
    def suggestion(self):
        if self.is_safe:
            return "Water appears safe. Boiling is still recommended."
        return "Do NOT drink. Boil or use proper filtration."

class WaterAnalyzer(Water):
    pass

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        color = request.form.get("color")
        smell = request.form.get("smell")
        clarity = request.form.get("clarity")

        water = WaterAnalyzer(color, smell, clarity)

        result = {
            "color": color,
            "smell": smell,
            "clarity": clarity,
            "level": water.level,
            "suggestion": water.suggestion
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

class Water:
    def __init__(self, color, smell, clarity):
        self.color = color
        self.smell = smell
        self.clarity = clarity
        self._score = 0
        self._level = None
        self._suggestion = None

    @property
    def level(self):
        return self._level

    @property
    def suggestion(self):
        return self._suggestion

    def calculate_score(self):
        score = 0
        if self.color == 'low': score += 2
        elif self.color == 'medium': score += 1

        if self.smell == 'low': score += 2
        elif self.smell == 'medium': score += 1

        if self.clarity == 'high': score += 2
        elif self.clarity == 'medium': score += 1

        self._score = score
        self._determine_level()

    def _determine_level(self):
        if self._score >= 5:
            self._level = "Safe"
            self._suggestion = "Water appears safe. Boiling is still recommended."
        elif self._score >= 3:
            self._level = "Moderate"
            self._suggestion = "Water may not be fully safe. Consider filtering or boiling."
        else:
            self._level = "Unsafe"
            self._suggestion = "Water is not safe to drink. Do not use."

class TapWater(Water):
    def __init__(self, color, smell, clarity):
        super().__init__(color, smell, clarity)
        self.source = "Tap"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        color = request.form.get('color')
        smell = request.form.get('smell')
        clarity = request.form.get('clarity')

        water = Water(color, smell, clarity)
        water.calculate_score()

        result = {
            "color": color,
            "smell": smell,
            "clarity": clarity,
            "level": water.level,
            "suggestion": water.suggestion
        }

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

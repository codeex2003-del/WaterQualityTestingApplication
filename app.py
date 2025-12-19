from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        color = request.form.get('color')
        smell = request.form.get('smell')
        clarity = request.form.get('clarity')

        score = 0
        if color == 'low': score += 2
        elif color == 'medium': score += 1

        if smell == 'low': score += 2
        elif smell == 'medium': score += 1

        if clarity == 'high': score += 2
        elif clarity == 'medium': score += 1

        if score >= 5:
            level = "Safe"
            suggestion = "Water appears safe. Boiling is still recommended."
        elif score >= 3:
            level = "Moderate"
            suggestion = "Water may not be fully safe. Consider filtering or boiling."
        else:
            level = "Unsafe"
            suggestion = "Water is not safe to drink. Do not use."

        result = {
            "color": color,
            "smell": smell,
            "clarity": clarity,
            "level": level,
            "suggestion": suggestion
        }

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

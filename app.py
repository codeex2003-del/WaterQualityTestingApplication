class WaterSample:
    def __init__(self, color, smell, clarity):
        self._color = color
        self._smell = smell
        self._clarity = clarity

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value not in ['low', 'medium', 'high']:
            raise ValueError("Color must be 'low', 'medium', or 'high'")
        self._color = value

    @property
    def smell(self):
        return self._smell

    @smell.setter
    def smell(self, value):
        if value not in ['low', 'medium', 'high']:
            raise ValueError("Smell must be 'low', 'medium', or 'high'")
        self._smell = value

    @property
    def clarity(self):
        return self._clarity

    @clarity.setter
    def clarity(self, value):
        if value not in ['low', 'medium', 'high']:
            raise ValueError("Clarity must be 'low', 'medium', or 'high'")
        self._clarity = value


class WaterAnalyzer(WaterSample):
    def analyze(self):
        score = 0
        if self.color == 'high':
            score += 1
        if self.smell == 'high':
            score += 1
        if self.clarity == 'low':
            score += 1

        if score == 0:
            return "✅ Water is Safe"
        elif score == 1:
            return "⚠️ Water is Slightly Unsafe"
        else:
            return "🚨 Water is Unsafe"


if __name__ == "__main__":
    sample = WaterAnalyzer(color='medium', smell='low', clarity='high')
    print(sample.analyze())

    sample.color = 'high'
    sample.smell = 'medium'
    print(sample.analyze())
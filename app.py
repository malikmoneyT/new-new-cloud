from flask import Flask, render_template, request, jsonify
from sentiment import ComprehendService

app = Flask(__name__)

AWS_REGION = 'ca-central-1'
sentiment = ComprehendService(AWS_REGION)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = sentiment.analyze_sentiment(text)
    sentiment = result['SentimentScore']
    return jsonify(sentiment)

if __name__ == '__main__':
    app.run(debug=True)

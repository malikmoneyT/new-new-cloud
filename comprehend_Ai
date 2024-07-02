import boto3

class ComprehendService:
    def __init__(self, region_name):
        self.client = boto3.client(
            'comprehend',
            region_name=region_name
        )

    def analyze_sentiment(self, text):
        response = self.client.detect_sentiment(Text=text, LanguageCode='en')
        return response

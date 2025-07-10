import requests

API_TOKEN = "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"  
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

def classify_text(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    if response.status_code == 200:
        result = response.json()
        print("Sentiment analysis results:")
        for item in result[0]:
            label = label_map.get(item['label'], item['label'])
            score = item['score']
            print(f"  {label}: {score:.2%}")
    else:
        print("Error:", response.status_code, response.text)

while True:
    user_input = input("Enter text to classify (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    classify_text(user_input)

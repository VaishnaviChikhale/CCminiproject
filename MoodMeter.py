from textblob import TextBlob

def analyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

# User input interface
def main():
    print("Emotion Recognition from Text")
    print("Type 'exit' to quit the program.")
    
    while True:
        text = input("Enter a sentence to analyze: ")
        if text.lower() == 'exit':
            break
        emotion = analyze_emotion(text)
        print(f"Emotion: {emotion}\n")

if __name__ == "__main__":
    main()

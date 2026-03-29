import os
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file
import openai
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import io

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("OPENAI_API_KEY", "")

def analyze_ticket_with_ai(title, description, api_key):
    openai.api_key = api_key
    prompt = f"""
    Analyze the following support ticket and provide the following details strictly in this format:
    Urgency: [High / Medium / Low]
    Sentiment: [Frustrated / Neutral / Happy]
    Response: [A short 2-3 sentence professional response suggestion]

    Ticket Title: {title}
    Ticket Description: {description}
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert customer support AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=150
        )
        output = response.choices[0].message.content.strip().split('\n')
        
        urgency = "Medium"
        sentiment = "Neutral"
        suggestion = "We are looking into this."
        
        for line in output:
            if line.startswith("Urgency:"):
                urgency = line.replace("Urgency:", "").strip()
            elif line.startswith("Sentiment:"):
                sentiment = line.replace("Sentiment:", "").strip()
            elif line.startswith("Response:"):
                suggestion = line.replace("Response:", "").strip()
                
        return urgency, sentiment, suggestion
    except Exception as e:
        return "Medium", "Neutral", f"Error analyzing ticket: {str(e)}"

def perform_clustering(df, num_clusters=3):
    if len(df) < num_clusters:
        num_clusters = len(df)
    texts = df['Title'] + " " + df['Description']
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    return kmeans.labels_

@app.route('/')
def index():
    return render_template('index.html', default_api_key=API_KEY)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Get file and api key
    api_key = request.form.get('api_key', API_KEY)
    if not api_key:
        return jsonify({"error": "OpenAI API Key is required."}), 400
    
    file = request.files.get('file')
    if file:
        df = pd.read_csv(file)
    else:
        if os.path.exists('tickets.csv'):
            df = pd.read_csv('tickets.csv')
        else:
            return jsonify({"error": "No file uploaded and tickets.csv not found."}), 400
    
    results = []
    for index, row in df.iterrows():
        urgency, sentiment, suggestion = analyze_ticket_with_ai(row.get('Title',''), row.get('Description',''), api_key)
        results.append({
            "Ticket ID": row.get('Ticket ID', f"T-{index}"),
            "Title": row.get('Title',''),
            "Description": row.get('Description',''),
            "Urgency": urgency,
            "Sentiment": sentiment,
            "Suggested Response": suggestion
        })
    
    analyzed_df = pd.DataFrame(results)
    
    try:
        clusters = perform_clustering(df, num_clusters=3)
        analyzed_df['Cluster Group'] = clusters.tolist()
    except Exception as e:
        analyzed_df['Cluster Group'] = 0
        
    # Save to a temporary file internally to allow download later
    analyzed_df.to_csv('analyzed_tickets_output.csv', index=False)
    
    # Calculate stats
    high_urgency = len(analyzed_df[analyzed_df['Urgency'].str.contains('High', case=False, na=False)])
    frustrated = len(analyzed_df[analyzed_df['Sentiment'].str.contains('Frustrated', case=False, na=False)])
    
    return jsonify({
        "status": "success",
        "total": len(analyzed_df),
        "high_urgency": high_urgency,
        "frustrated": frustrated,
        "data": analyzed_df.to_dict(orient='records')
    })

@app.route('/api/download')
def download():
    if os.path.exists('analyzed_tickets_output.csv'):
        return send_file('analyzed_tickets_output.csv', as_attachment=True, download_name='analyzed_tickets_smart_ai.csv')
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

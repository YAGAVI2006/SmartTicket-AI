# SmartTicket AI – Prioritize & Respond

## Overview
Support teams receive hundreds of tickets daily, but urgent issues often get buried under low-priority requests. This leads to delays, frustrated customers, and wasted time.

**SmartTicket AI** is an intelligent agent that:
- Analyzes incoming support tickets for urgency (High / Medium / Low).
- Detects customer sentiment (Frustrated / Neutral / Happy).
- Groups similar issues for better workflow management.
- Suggests quick response templates for critical tickets.

## Tech Stack
- **Python 3.x**
- **OpenAI GPT API**: For urgency, sentiment analysis, and response suggestion.
- **Pandas, Scikit-learn**: For data handling and ML clustering of similar tickets.
- **Streamlit**: For the interactive dashboard.

## Setup Instructions

1. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   - Copy `.env.example` to `.env`.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=sk-...
     ```
   - Alternatively, you can enter the API key directly in the Streamlit Sidebar when running the app.

3. **Run the Dashboard**
   ```bash
   streamlit run app.py
   ```

4. **Testing Data**
   A sample `tickets.csv` is included in this directory to test out the application instantly if you don't upload your own.

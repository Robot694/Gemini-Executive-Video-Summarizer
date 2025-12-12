# -*- coding: utf-8 -*-

import os
from google import genai

try:
    client = genai.Client()
except Exception as e:
    print(f"Error initializing client: {e}")
    print("Please ensure your GEMINI_API_KEY is set correctly in the previous cell.")
    exit()

youtube_url_to_summarize = "https://www.youtube.com/watch?v=9RvWcXVaAng" # Replace with your target URL
target_model = "gemini-2.5-flash"

summary_prompt = (
    "Analyze this video and provide a summary for an executive audience. "
    "Structure your response with the following format:\n\n"
    "1. **Summary:** A single paragraph executive summary (max 3 sentences).\n"
    "2. **Key Takeaways:** A bulleted list of the top 3 critical insights/facts.\n"
    "3. **Actionable Insight:** A single-sentence recommendation based on the content.\n"
)

print("Sending request to Gemini API. This may take a moment...")

response = client.models.generate_content(
    model=target_model,
    contents=[
        {
            "parts": [
                {"text": summary_prompt},
                # Passing the URL as a file_data Part is what enables video understanding
                {"file_data": {"file_uri": youtube_url_to_summarize}},
            ]
        }
    ],
)

print("\n--- GEMINI VIDEO SUMMARY ---")
print(response.text)
print("----------------------------")
print(f"Source Video: {youtube_url_to_summarize}")
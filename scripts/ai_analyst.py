import os
import json
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def analyze_transcript(transcript_text):
    """Uses Gemini API to analyze the transcript and generate metadata."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set in the environment.")
        return None

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    You are an expert YouTube Video Analyst for the "@AICourseforKidsandTeens" channel.
    Analyze the following video transcript/notes and generate:
    1. 3 catchy, high-CTR YouTube titles.
    2. A short engaging YouTube description (include chapters if you can guess timestamps).
    3. 10 highly relevant SEO tags.
    4. Suggested timestamps for the best short clips to extract.
    
    Format the output as JSON with keys: "titles", "description", "tags", "clip_suggestions".
    
    Transcript/Notes:
    {transcript_text}
    """
    
    print("Calling Gemini API to analyze transcript...")
    try:
        response = model.generate_content(prompt)
        # Attempt to parse the response as JSON. In a production app, we'd use Structured Outputs.
        try:
            # Strip markdown if present
            raw_text = response.text.strip()
            if raw_text.startswith("```json"):
                raw_text = raw_text[7:-3]
            elif raw_text.startswith("```"):
                raw_text = raw_text[3:-3]
                
            return json.loads(raw_text)
        except json.JSONDecodeError:
            print("Failed to parse JSON. Raw output:")
            print(response.text)
            return {"raw_output": response.text}
            
    except Exception as e:
        print(f"Error calling API: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="AI Video Analyst")
    parser.add_argument("--notes", help="Path to a text file containing raw notes or transcript")
    args = parser.parse_args()

    if not args.notes or not os.path.exists(args.notes):
        print("Please provide a valid path to a notes/transcript file using --notes.")
        return

    with open(args.notes, 'r') as f:
        content = f.read()
        
    result = analyze_transcript(content)
    
    if result:
        output_file = "../config/ai_analysis.json"
        os.makedirs("../config", exist_ok=True)
        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)
        print(f"Analysis saved to {output_file}")

if __name__ == "__main__":
    main()

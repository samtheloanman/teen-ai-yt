import os
import json
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generate_seo_metadata(topic):
    """Uses Gemini API to generate SEO metadata and thumbnail ideas."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        return None

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    You are an expert YouTube SEO Strategist for the "@AICourseforKidsandTeens" channel.
    Topic: {topic}
    
    Please generate:
    1. 5 highly optimized, click-worthy titles.
    2. A rich, keyword-heavy description template.
    3. 15 tags optimized for search ranking.
    4. 3 detailed text-to-image prompts for generating a YouTube thumbnail (e.g. for fal.ai/Midjourney).
    
    Format the output as JSON with keys: "titles", "description", "tags", "thumbnail_prompts".
    """
    
    print(f"Generating SEO metadata for topic: '{topic}'...")
    try:
        response = model.generate_content(prompt)
        try:
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
    parser = argparse.ArgumentParser(description="AI SEO & Thumbnail Metadata Generator")
    parser.add_argument("--topic", required=True, help="The episode topic or idea")
    args = parser.parse_args()
        
    result = generate_seo_metadata(args.topic)
    
    if result:
        output_file = "../config/episode_metadata.json"
        os.makedirs("../config", exist_ok=True)
        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)
        print(f"SEO Metadata saved to {output_file}")

if __name__ == "__main__":
    main()

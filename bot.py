import os
import json
import requests
import random
from datetime import datetime

OPENAI_KEY = os.getenv('OPENAI_KEY')

HOOKS = [
    "This AI made me $500 yesterday",
    "Stop using ChatGPT. This is free",
    "I automated my income with this",
    "Nobody talks about this AI hack",
    "This replaced my $5K assistant"
]

TOOLS = ["Claude AI", "Midjourney", "AutoGPT", "Copy.ai", "Jasper", "Notion AI", "Canva AI", "Runway ML"]

def write_script(tool):
    hook = random.choice(HOOKS)
    prompt = f"Write 58-second YouTube Short script about {tool}. Hook: {hook}. Format: Problem 10s, Demo 35s, CTA 10s. Energetic, simple words."
    
    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"},
            json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]},
            timeout=30
        )
        return r.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"{hook}. {tool} is amazing. Link in bio. Follow for more. (Error: {str(e)})"

def main():
    print(f"[{datetime.now()}] Starting...")
    
    # Create output directory
    os.makedirs('scripts', exist_ok=True)
    
    generated = []
    for tool in random.sample(TOOLS, 3):
        script = write_script(tool)
        data = {
            "tool": tool,
            "script": script,
            "hook": random.choice(HOOKS),
            "created": datetime.now().isoformat()
        }
        
        # Save to scripts folder
        filename = f"scripts/{tool.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        generated.append(filename)
        print(f"Created: {filename}")
        print(f"Content preview: {script[:100]}...")
    
    # Also create a summary file
    with open('scripts/LATEST_SCRIPTS.txt', 'w') as f:
        f.write(f"Generated on: {datetime.now()}\n\n")
        for g in generated:
            f.write(f"- {g}\n")

if __name__ == "__main__":
    main()

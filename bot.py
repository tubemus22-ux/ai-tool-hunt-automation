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
        print(f"Error calling OpenAI: {e}")
        return f"{hook}. {tool} is amazing. Link in bio. Follow for more."

def main():
    print(f"[{datetime.now()}] Starting...")
    print(f"OPENAI_KEY present: {bool(OPENAI_KEY)}")
    
    # Create output directory in current working directory
    script_dir = os.path.join(os.getcwd(), 'scripts')
    os.makedirs(script_dir, exist_ok=True)
    print(f"Created directory: {script_dir}")
    
    generated = []
    selected_tools = random.sample(TOOLS, 3)
    print(f"Selected tools: {selected_tools}")
    
    for tool in selected_tools:
        print(f"Generating script for: {tool}")
        script = write_script(tool)
        
        data = {
            "tool": tool,
            "script": script,
            "hook": random.choice(HOOKS),
            "created": datetime.now().isoformat()
        }
        
        # Save to scripts folder
        safe_tool_name = tool.replace(' ', '_').replace('/', '_')
        filename = os.path.join(script_dir, f"{safe_tool_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        generated.append(filename)
        print(f"Created: {filename}")
        print(f"Content length: {len(script)} characters")
    
    print(f"Total scripts generated: {len(generated)}")
    
    # List files in scripts directory to verify
    print(f"Files in scripts directory: {os.listdir(script_dir)}")

if __name__ == "__main__":
    main()

import os
import json
import requests
import random
from datetime import datetime

OPENAI_KEY = os.getenv('OPENAI_KEY')

HOOKS = [
    "This AI made me $500 yesterday (proof)",
    "Stop using ChatGPT. This free AI is better",
    "I automated my income with this tool",
    "Nobody talks about this AI hack",
    "This replaced my $5K virtual assistant",
    "ChatGPT is dead. Use this instead",
    "I found an AI that does my job for me"
]

TOOLS = [
    {"name": "Claude AI", "url": "claude.ai", "category": "writing"},
    {"name": "Midjourney", "url": "midjourney.com", "category": "image"},
    {"name": "Copy.ai", "url": "copy.ai", "category": "writing"},
    {"name": "Jasper", "url": "jasper.ai", "category": "writing"},
    {"name": "Notion AI", "url": "notion.so", "category": "productivity"},
    {"name": "Canva AI", "url": "canva.com", "category": "design"},
    {"name": "Runway ML", "url": "runwayml.com", "category": "video"},
    {"name": "Synthesia", "url": "synthesia.io", "category": "video"}
]

def write_script(tool):
    hook = random.choice(HOOKS)
    prompt = f"""Create a viral 58-second YouTube Shorts script about {tool['name']}.

Hook: {hook}

Structure:
- 0-3 sec: Pattern interrupt hook
- 3-10 sec: Problem statement
- 10-45 sec: Show the tool working (step by step)
- 45-55 sec: Results/success
- 55-58 sec: Call to action ("Follow for more")

Make it energetic, simple words, no fluff. Include specific features of {tool['name']}."""

    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"},
            json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]},
            timeout=30
        )
        script = r.json()['choices'][0]['message']['content']
    except:
        script = f"{hook}. {tool['name']} is a game-changing AI tool that saves hours of work. Link in bio. Follow for daily AI tools."

    return {
        "tool": tool['name'],
        "url": tool['url'],
        "category": tool['category'],
        "hook": hook,
        "script": script,
        "title": f"{hook} #{tool['name'].replace(' ', '')} #AI #Shorts",
        "hashtags": f"#Shorts #AI #Tech #{tool['name'].replace(' ', '')} #Automation",
        "created": datetime.now().isoformat()
    }

def main():
    print(f"[{datetime.now()}] Generating scripts...")
    
    os.makedirs('scripts', exist_ok=True)
    
    selected = random.sample(TOOLS, 3)
    
    for tool in selected:
        data = write_script(tool)
        
        # Save as JSON
        filename = f"scripts/{tool['name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        # Also save as readable text
        text_filename = filename.replace('.json', '.txt')
        with open(text_filename, 'w') as f:
            f.write(f"TITLE: {data['title']}\n\n")
            f.write(f"HOOK: {data['hook']}\n\n")
            f.write(f"SCRIPT:\n{data['script']}\n\n")
            f.write(f"HASHTAGS: {data['hashtags']}\n")
            f.write(f"TOOL URL: {data['url']}")
        
        print(f"Created: {tool['name']}")

if __name__ == "__main__":
    main()

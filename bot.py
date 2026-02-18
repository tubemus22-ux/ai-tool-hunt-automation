import os
import json
import requests
import random
from datetime import datetime

OPENAI_KEY = os.getenv('OPENAI_KEY')

HOOKS = [
    "Nobody talks about this AI hack",
    "This AI made me $500 yesterday",
    "Stop using ChatGPT. This is free and better"
]

TOOLS = [
    {"name": "Notion AI", "url": "notion.so", "task": "writing blog posts"},
    {"name": "Midjourney", "url": "midjourney.com", "task": "creating images"},
    {"name": "Canva AI", "url": "canva.com", "task": "designing graphics"}
]

def write_script(tool):
    hook = random.choice(HOOKS)
    
    # Create detailed 58-second script
    script = f"""{hook}.

I used to spend 3 hours {tool['task']}. It was exhausting.

Then I discovered {tool['name']}.

Look at this. I just type what I need.

[Show screen recording of {tool['name']}]

Boom. Done in 30 seconds.

This would have taken me hours before.

{tool['name']} just saved me 10 hours this week.

Link in my bio to try it free.

Follow for daily AI tools that save you time."""
    
    return {
        "tool": tool['name'],
        "url": tool['url'],
        "hook": hook,
        "script": script,
        "title": f"{hook} #{tool['name'].replace(' ', '')} #AI #Shorts",
        "hashtags": "#Shorts #AI #Tech #Automation",
        "created": datetime.now().isoformat()
    }

def main():
    os.makedirs('scripts', exist_ok=True)
    
    for tool in random.sample(TOOLS, 3):
        data = write_script(tool)
        
        # Save as text file
        filename = f"scripts/{tool['name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"TITLE: {data['title']}\n\n")
            f.write(f"HOOK: {data['hook']}\n\n")
            f.write(f"SCRIPT:\n{data['script']}\n\n")
            f.write(f"HASHTAGS: {data['hashtags']}\n")
            f.write(f"TOOL: {data['url']}")
        
        print(f"Created: {tool['name']}")

if __name__ == "__main__":
    main()

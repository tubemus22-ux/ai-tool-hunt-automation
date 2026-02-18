import os
import json
import requests
import random
from datetime import datetime

OPENAI_KEY = os.getenv('OPENAI_KEY')
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
    
    print(f"Total scripts generated: {len(generated)}")

if __name__ == "__main__":
    main()

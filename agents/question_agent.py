import requests
import random
import json

def generate_questions(topic):
    url = "http://localhost:11434/api/generate"
    
    tech_prompt = open('prompts/technical_prompt.txt').read().format(topic=topic)
    behav_prompt = open('prompts/behavioral_prompt.txt').read().format(topic=topic)
    
    tech_response = requests.post(url, json={"model": "llama3", "prompt": tech_prompt, "stream": False})
    behav_response = requests.post(url, json={"model": "llama3", "prompt": behav_prompt, "stream": False})

    # Manual decoding (safe way)
    tech_json = json.loads(tech_response.content.split(b'\n')[0])
    behav_json = json.loads(behav_response.content.split(b'\n')[0])

    tech_questions = tech_json.get('response', '').strip().split('\n')
    behav_questions = behav_json.get('response', '').strip().split('\n')
    
    def assign_difficulty(q):
        return random.choice(['Easy', 'Medium', 'Hard'])
    
    tech_final = [(q, 'Technical', assign_difficulty(q)) for q in tech_questions if q]
    behav_final = [(q, 'Behavioral', assign_difficulty(q)) for q in behav_questions if q]
    
    return tech_final, behav_final

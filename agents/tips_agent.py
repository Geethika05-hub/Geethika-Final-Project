import requests
import json

def generate_tips(job_description):
    url = "http://localhost:11434/api/generate"
    prompt = open('prompts/tips_prompt.txt').read().format(job_description=job_description)
    response = requests.post(url, json={"model": "llama3", "prompt": prompt, "stream": False})
    resp_json = json.loads(response.content.split(b'\n')[0])
    tips = resp_json.get('response', '').strip().split('\n')
    return [t for t in tips if t]

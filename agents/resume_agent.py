import requests
import json

def generate_resume_points(job_description):
    url = "http://localhost:11434/api/generate"
    prompt = open('prompts/resume_prompt.txt').read().format(job_description=job_description)
    response = requests.post(url, json={"model": "llama3", "prompt": prompt, "stream": False})
    resp_json = json.loads(response.content.split(b'\n')[0])
    points = resp_json.get('response', '').strip().split('\n')
    return [p for p in points if p]

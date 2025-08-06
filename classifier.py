from config import llm

def classify_event(prompt: str, case_description: str) -> str:
    filled_prompt = prompt.replace("{case_description}", case_description)
    response = llm.invoke(filled_prompt)
    return response.content.strip()

from config import llm

def generate_prompt():
    system_instruction = (
        "You are a prompt engineer. Your job is to generate a prompt for a legal classification model.\n"
        "The prompt will be used to identify which articles of the European Convention on Human Rights (ECHR) have been violated.\n\n"
        "IMPORTANT:\n"
        "- Include the exact placeholder {case_description} where the case will be inserted.\n"
        "- Do not use any other placeholder or brackets.\n"
        "- Output ONLY the final prompt text. No extra explanation or formatting.\n"
        "- Ask the model to return only article numbers (e.g., 3, 6).\n"
        "- You may include an example in the format instructions.\n\n"
        "Write the prompt below:"
    )

    response = llm.invoke(system_instruction)
    return response.content.strip()

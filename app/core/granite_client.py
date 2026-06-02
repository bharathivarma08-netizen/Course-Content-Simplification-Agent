import os
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

load_dotenv()

def get_granite_model():
    credentials = Credentials(
        url=os.getenv("IBM_URL"),
        api_key=os.getenv("IBM_API_KEY")
    )
    model = ModelInference(
        model_id="ibm/granite-4-h-small",
        credentials=credentials,
        project_id=os.getenv("IBM_PROJECT_ID")
    )
    return model

def ask_granite(prompt: str, system: str = "") -> str:
    model = get_granite_model()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    response = model.chat(messages=messages)
    return response["choices"][0]["message"]["content"]
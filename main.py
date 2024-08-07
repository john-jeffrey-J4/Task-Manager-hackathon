from fastapi import FastAPI
from huggingface_hub import InferenceClient


app = FastAPI()


@app.get("/{title}")
async def root(title: str = None):
    client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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",
    )

    response_content = ""

    for message in client.chat_completion(
        messages=[{"role": "user", "content": f"I am creating a task in task manager for title {title} .Please give me suggestion for task summary within 150 letters. Avoid these  'Here are a few suggestions for a task summary within 150 characters:' letters give only content to use"}],
        max_tokens=500,
        stream=True,
    ):
        response_content += message.choices[0].delta.content

    return {"response": response_content}

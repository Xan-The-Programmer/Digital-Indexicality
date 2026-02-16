import torch
from transformers import AutoTokenizer, AutoModel

model_name = "xlm-roberta-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

text = "This is a multilingual test sentence."

inputs = tokenizer(
    text, 
    return_tensors="pt",
    padding = True,
    truncation = True
)


with torch.no_grad():
    outputs = model(**inputs)

token_embeddings = outputs.last_hidden_state
print(token_embeddings)
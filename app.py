from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
import torch
import json
import glob

app = FastAPI()

tokenizer=AutoTokenizer.from_pretrained('./ashish_trained_biobert/')
model=AutoModelForSequenceClassification.from_pretrained('./ashish_trained_biobert/',num_labels=2,ignore_mismatched_sizes=True)
model.config.id2label = {0: "Cancer", 1: "Non-Cancer"}
model.config.label2id = {"Cancer": 0, "Non-Cancer": 1}
@app.get("/")
def hello_world():
    return {"Hello": "World"}


def llm_classify(input_string):
    tokens = tokenizer(input_string,return_tensors='pt',padding=True,truncation=True,max_length=512)
    output = model(**tokens)
    prob = torch.sigmoid(output.logits)
    pred = prob.argmax().item()
    predicted_label = model.config.id2label[pred]
    scores = {y:x for x,y in zip(prob.tolist()[0],['Cancer','Non-Cancer'])}
    return predicted_label, scores

@app.post("/classify_paper")
def classify_paper(abstract: str):
    label,scores = llm_classify(abstract)
    return {"predicted_labels":label,"confidence_scores":scores}

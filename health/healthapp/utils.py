from transformers import pipeline

text_generate = pipeline('text-generation',model='gpt2')
def generate_text(prompt):
    res = text_generate(prompt,max_length=100,num_return_sequences=1)
    return res[0]['generated_text']
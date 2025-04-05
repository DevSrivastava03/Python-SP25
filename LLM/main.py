from flask import Flask, render_template, request
import torch  
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chat_history_ids = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global chat_history_ids
    bot_reply = ""

    if request.method == 'POST':
        user_input = request.form['user_text'].strip()

        if user_input:
            try:
                new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

                bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

                chat_history_ids = model.generate(
                    bot_input_ids,
                    max_length=1000,
                    pad_token_id=tokenizer.eos_token_id,
                    num_beams=5,
                    no_repeat_ngram_size=3,
                    early_stopping=True
                )

                bot_reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            except Exception as e:
                bot_reply = f"Error during conversation: {str(e)}"

    return render_template('index.html', bot_reply=bot_reply)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

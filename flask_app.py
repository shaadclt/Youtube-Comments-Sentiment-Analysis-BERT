from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
            model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

            data = []
            
            with Chrome(executable_path=r'C:\Program Files\chromedriver.exe') as driver:
                wait = WebDriverWait(driver, 15)
                driver.get(url)

                for item in range(1):
                    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
                    time.sleep(15)

                for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
                    data.append(comment.text)

            df = pd.DataFrame(data, columns=['comment'])
            df.head()

            def sentiment_score(comment):
                tokens = tokenizer.encode(comment, return_tensors='pt')
                result = model(tokens)
                return int(torch.argmax(result.logits)) + 1

            df['sentiment'] = df['comment'].apply(lambda x: sentiment_score(x[:512]))

            avg_sentiment_score = round(df['sentiment'].mean(), 2)

            return render_template('result.html', avg_sentiment_score=avg_sentiment_score)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

# YouTube Comments Sentiment Analysis using BERT

This project provides a sentiment analysis tool for YouTube comments using BERT (Bidirectional Encoder Representations from Transformers). It allows you to analyze the sentiment of comments on a scale of 1 to 5 on YouTube videos using state-of-the-art natural language processing models.

## Table of Contents

- [Introduction](#introduction)
- [How it Works](#how-it-works)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The YouTube Comments Sentiment Analysis project leverages BERT, a powerful transformer-based model, to classify the sentiment of YouTube comments. BERT, with its pre-trained language representations, can effectively understand the sentiment expressed in the text and provide accurate sentiment analysis.

## How it Works

The project follows these steps to analyze the sentiment of YouTube comments:

1. **Data Collection**: Selenium is used to retrieve comments from a specified YouTube video. The comments are extracted and stored for analysis.

2. **Model Loading**: A pre-trained BERT model, fine-tuned for sentiment analysis, is loaded. This model has been trained on labeled sentiment analysis datasets to learn to classify sentiment accurately.

4. **Encoding**: The preprocessed comments are encoded into numerical representations using the BERT tokenizer.

5. **Sentiment Classification**: The encoded comments are fed into the loaded BERT model to classify the sentiment on a scale of 1 to 5.

6. **Output**: The sentiment analysis results are generated, indicating the overall sentiment score of the comments.

## Setup

To use this project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/youtube-comments-sentiment-analysis.git
```

2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `streamlit_app.py` script:

```
streamlit streamlit_app.py
```

2. Paste the desired Youtube video URL.

3. The sentiment score will be displayed on the screen. 

Feel free to customize the sentiment analysis tool according to your specific requirements, such as integrating it into a web application or incorporating additional features.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). You are free to modify and use the code for both personal and commercial purposes.

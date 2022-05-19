# Fake News Detection

1. **Team name:** Team Tons

    1. Aleksander Rolander - cph-al351@cphbusiness.dk

    2. Magnus Granno - cph-mg319@cphbusiness.dk

    3. Oliver Staehr - cph-os85@cphbusiness.dk

2. **Data:** [Fake_News_Data.zip - Google Disk](https://drive.google.com/file/d/1necMgCR28GUzoYhqilDcytfeKIWijCFp/view?usp=sharing)
   The training dataset has 20800 rows and 5 columns

    - ["id"]
    - ["Title"]
    - ["Author"]
    - ["Text"]
    - ["Label"]

      - 1 === Fake
      - 0 === Real

    The test data set has 5200 rows and 4 columns

    - ["id"]
    - ["Title"]
    - ["Author"]
    - ["Text"]

3. **Problems:** (Sorted by priority)

    1. We want to make sure the data is clean by removing unused columns, null values etc and then we clean up the text by removing stopword, urls etc.

    1. We will use stemming and lemmetization and create a wordcloud for real news and a wordcloud for fake news to demonstrate most common words in fake news vs real news.

    1. We will train a model to identify fake news and real news in a given dataset / text and compare the results to a pretrained model made my Facebook.

    1. We will create a web app where you can paste text and check if it is fake news.

    1. We will persist a database with articles marked with fake and display the latest fake news on the web app.

4. **Techonologies:** Pandas, Numpy, Sklearn, Wordcloud, Nltk, Regular expressions, TensorFlow, Flask/FastAPI, Transformers.

5. **Challenges:** The first challenge will be to make the model as accurate as possible and the second challenge will be to create a web app with Flask/FastApi, since we've never worked with it before.

#

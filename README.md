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

4. **Techonologies:** 

    Pandas, Numpy, Sklearn, Wordcloud, Nltk, Regular expressions, TensorFlow, FastAPI, Transformers, Starlette, Jinja2, Spacy, Uvicorn, Python-multipart, sqlalchemy.

5. **Challenges:** 

    The first challenge was to make the model as accurate as possible and the second challenge was creating a web app with FastApi, since we've never worked with the library before.
    FastAPI made it possible for us to create endpoints for our website in an efficient manner. The Endpoints are located under app.py.   


6. **Installation Guide:**
    1. Download all of the following libraries using PIP
        1. fastapi
        2. Tensorflow
        3. sqlalchemy
        4. uvicorn[standard]
        5. Spacy
        6. Nltk
        7. pandas
        8. numpy
        9. jinja2
        10. python-multipart
        11. Wordclouds
        12. starlette
    2. Download the "en_core_web_sm" library by writing the following in console.
        python -m spacy download en_core_web_sm


7. **User Guide**
    1. Run the following command in the rootfolder.
        uvicorn app:app --reload
    2. Go to 127.0.0.1:8000
    3. Copy paste an article into the text field on the website and click "Detect"

8. **Status**

    We finished the project with most of your goals achieved.
    We wanted to test our model against a model created by Facebook called "Bert-Base-Uncased", however the model was estimated to take 19 hours to run. 
    For that reason we decide to skip that part of the project.
    We have created a functional website using python to detect whether an article is fake or true.
#

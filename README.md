to install:

    cd /your/python/env/path
    git clone https://github.com/j3ygithub/nlp
    python -m venv /your/python/env/path/nlp
    cd nlp
    pip install -r requirements.txt


write script here:

    /your/python/env/path/nlp/nlp/nlp/text/views.py

    def handler(input_text):
        return result_text


to run website:

    cd /your/python/env/path/nlp/nlp/
    python manage.py runserver

    text nlp app:
        browser > http://127.0.0.1:8000/text ( or http://127.0.0.1:8000/text )

    hello world test:
        browser > http://127.0.0.1:8000/text/helloworld
# <div align="center">Django Wiki</div>

This is originally a project in Harvard's CS50W course. You can visit my version [here](https://marcos-napolitano-markup-wiki.up.railway.app/)! :rocket:

This app is similar to a wiki but utilizing Django's view model template.Entries can be edited in Markdown language and then saved in the server. Currently the parsing into HTML is made by a library called Markdown2, but it supports standard Markdown syntax. There's also a search bar and a *random page* feature. 

## Tech Stack

* HTML
* CSS
* JavaScript
* Django
* Python Decouple - Stores enviroment variables securely.
* Markdown2 - Parses markdown into HTML

## Quickview

![Screenshot of the site](https://marcosnapolitano.github.io/Assets/thumbnail3.jpg)

## Quickstart

*Make sure both python and virtualenv are installed on your OS.*

1. Fork the project.
2. Clone project using `git clone git@github.com:<YOUR-USERNAME>/markdown_wiki.git`.
3. Run `virtualenv env` then `env\scripts\activate`.
4. Once in your virtual enviroment `(env)`, run `pip install -r "markdown_wiki\requirements.txt"`.
5. You need to generate a SECRET_KEY now, in order to do so you have to:
    ```
    (env)... cd markdown_wiki
    (env)... markdown_wiki\python
    
    >>> from django.core.management.utils import get_random_secret_key
    >>> SECRET_KEY = get_random_secret_key()
    >>> exit()
    ```
6. Create a `.env` file and paste `SECRET_KEY=[NEW_SECRET_KEY]`
7. Run `python manage.py runserver`

## Docs

All logic contained in `Views.py` in the `encyclopedia` folder. The actual code is pretty simple and it's commented enought to fully understand what is going on. 

## Final Notes

This site was deployed using [Railway](https://railway.app/). A workflow provided by Vite is included to build the app correctly.
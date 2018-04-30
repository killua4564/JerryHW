## Member
- killua4564
    - B10509002
- kuma0923
    - B10509010
- a9630121a9630121
    - B10533018
- FormyHarmony
    - B10533012

## 0430
- site url
    - https://immense-escarpment-86478.herokuapp.com/Blog/blog/
- heroku
    - install heroku
    - $ heroku login
        - Email
        - Password
    - $ git clone https://github.com/heroku/python-getting-started.git
        - in folder 0430
    - $ cd python-getting-started
    - $ heroku create
    - $ git push heroku master
    - $ heroku ps:scale web=1
    - $ heroku open

- Add own apps to heroku
    - $ sudo pip install Django --upgrade
    - $ python manage.py migrate
    - $ python manage.py startapp \<appname\>
    - \[move your app file to the app folder\]
    - $ python manage.py makemigrations
    - $ python manage.py migrate
    - $ git add .
    - $ git commit -m '\<commit\>'
    - $ git push heroku master
    - $ heroku run python manage.py createsuperuser
        - admin
        - P@ssword
    - heroku open


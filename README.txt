This web app's function is to enable a user to search for a movie using the search box and obtaining information about a movie through https://www.omdbapi.com/ site's API.

Registered/logged in user could also create a comment on a movie which would then be saved into a database and displayed in the commentary section for it to be visible for other users.

Besides login and register functions, user can also reset password, change profile picture, delete, change or post comments

Creation process:

1. Installing Apios
	https://www.npmjs.com/package/axios
2. https://www.omdbapi.com/
	API
3. Install node.js
	nodejs
	nodejs supports Windows officially. Just download it at http://nodejs.org and run the installer.
	From Nodejs.x86 start menu, click nodejs command prompt
	Try commands
    		node -v
    		npm -v

4. install live-server
	npm install -g live-server
5. Getting user interface and bootstrep theme from: https://bootswatch.com/
	click download and grab a link from url
6. Getting jquery 3x minified from q
7. getting axios client (search axios npm) https://www.npmjs.com/package/axios


8.//Installing and creating virtual environment for python and those first setups
(Look in snippets folder)


9.//Installing Flask and creating first app setups
10.//Making git repository (git needs to be installed)
	-creating master branch


11.//Adding bootstrap from (both JS and CSS)
https://getbootstrap.com/docs/4.2/getting-started/introduction/
-implementing and organizing static folder and JS and CSS linkage with url_for()

12. installing flask-wtf for forms (validation of forms)
	pip install flask-wtf
	create forms.py

13. Generating secret key
	to start Python in git bash, type python -i
	import secrets
	secrets.token_hex(16)

14. Creating login forms and registration forms in app.py and
	linking them to html pages
	adding validation

15.//Installing sql alchemy with pip
	pip install flask-sqlalchemy
	//There is a regular sqlalchemy but flask-sqlalchemy
	// is flask extension and is better for flask application

16. Setting up db and columns

17. Creating db in python (look in snippets)
	Creates file site.db

18. Changing and reorganizing everything to be Package Structure for easier
	Code maintenance and better structure
	Running now with python run.py

19. User autenthication and encrypting
	pip install flask-bcrypt
	adding Bcrypt module in __init__.py
	adding email and username validation to registration form
	installing

	Login with extention flask-login
	pip install flask-login

	creating user loader in models.py

	redirecting user in register and login function if user is authenticated to home route

creating account.html page which is only accessible if user is logged in (login_required function)

19.User Account and Profile Picture
// Adding update account form in both account.html and in routes
// saving pictures from local system to app
//reducing img size of pics
	Installing Pillow
	pip install Pillow
20. Style of application fixed, bugs removed, some templates changed (commentary added) Comment button in movie.html added and other stuff fixed.
	//git add .
	//git commit -m "similar to above"

21. added pagination and style fixed..jumbotron added on posts and account etc.
added template with only a specific user's posts

22. Email and Password Reset
importing Serializer for creating token for email reset
creating email reset routes and logic

	pip install flask-mail (for function that is sending mail after reseting password)

	Making Environment variabels for Flask-mail configuration:
		USER and PASSWORD - for this you have to specify an email account 
		on which you will be getting reset message
		app.config['MAIL_USERNAME'] = os.environ.get('USER')
		app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')

23. Creating custom error pages

24. Creating requirements.txt file (displays all moduels used for this app via 'final_project' virtual environment)
	pip freeze --local > requirements.txt





Running application:
1. Open command window/git bash or similar in directory where run.py file is
2. Type python run.py
3. for_Json.py file will be run only once and saved to db. was is already ran and posts are saved to db, so if you do not want to have double posts you should delete it or comment it (also check 'commentary' function in routes.py)

Testing database:
1. Open Python shell
2. from final_project import db
3. db.drop_all() 
4. db.create_all()
5. from final_project.models import User
	-create Users:
	user_1 = User(username='admin', email='admin@fp.com', password='cs50')
	user_2 = User(username='guest', email='guest@fp.com', password='cs50')
6. db.session.add(user_1)
7. db.session.add(user_2)
8. db.session.commit()
9. User.query.all()

Sources:
https://flask-bcrypt.readthedocs.io/en/latest/
http://flask.pocoo.org/docs/1.0/quickstart/
http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
https://flask-login.readthedocs.io/en/latest/
https://pythonhosted.org/Flask-Mail/
http://flag-icon-css.lip.is/
https://getbootstrap.com/
https://fontawesome.com/
https://www.youtube.com/user/schafer5
https://www.youtube.com/user/TechGuyWeb
https://pythonhosted.org/itsdangerous/
https://flask-wtf.readthedocs.io/en/stable/



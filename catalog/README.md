# Item-Catalog Web-Application...
--By Doredla.Gayathri.


# About Item-Catalog...
--It is a  web-application.
In this Item-catalog project mainly using the Flask framework  application is designed.
By using  SQL database this project access.
In this project watch categories and their watch lists are displayed. 
OAuth2 provides authentication for  CRUD operations.
Mainly crud includes adding watch categories,deleting watch categories,editing watchitems,deleting items respectively.
Currently OAuth2 is implemented for Google Accounts.


# What are the Skills Required for this project...
 Python ,HTML,CSS,OAuth, Flask Framework,DataBaseModels.


# In this Project contains...
--This project has one  Python module named `wsss.py` it runs  Flask-application. 
In this 'wss.py' all the google connections also established here.
A SQL database is created in this `wch_Sp.py` module.
In 'wch_it.py' all the sampledata is placed in this file.
Flask-application contains all HTML templates written in the templates folder.
It is easy for front-end of the application.
ImaGes_outPut folder contains all the screens related to the project are displayed...



# Installation steps for this project...
--There are some dependencies, few instructions on how to run the application.
Seperate instructions are provided to get GConnect working also...

# Dependencies for this project...
-- [Vagrant](https://www.vagrantup.com/)
-- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
-- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)



# How to Install steps for this project...
a). Install Vagrant & VirtualBox
b). Clone the Udacity Vagrantfile
---first for flask-application i have done vagrant init ubuntu/xenial64
c). Next I have taken  Vagrant VM (`vagrant up`)
d).Next  Log into Vagrant VM (`vagrant ssh`)
e). Navigate to `cd /vagrant` as suggested in terminal.
f). If this app imports requests which is not on this vm. Run 
 then pip install requests.

Otherwise for you simply Install the dependency libraries such as (Flask, sqlalchemy, requests,psycopg2 and oauth2client) by running 
`pip install -r requirements.txt`.



---After instaling all these steps::
I have created  DatabaseSetup file named as 'wch_Sp.py' then in this python file I have created 3classes such as User,Watchname,Watchlist.
And their respective tablenames suchas user,watchname,watchlist.


In that respective classes I have written as::
User class I have written id,name,email through which userdetails are written.
Watchname class I have written id,name,user_id is written.
Watchlist class I have written features of the watches such as their modelname,description,price,rating,color,modelweight,modellength,modelwidth,date,watchnameid,user_id.
and a database is created named watches.db.

--Run the application 'wch_Sp.py' then python file will be executed.

In the init file named wch_it.py all the sample data is written in it..
Run the application 'wch_it.py' then all the data is stored in database.

---In the main file named 'wsss.py' I have written all the google connections in it.
In this file I have imported all create_engine classes and all classnames ,and all the libraries which are related for this file.
To acesss or login in google account then I have generated 'client_secrets.json' file.
-- Run the application  using http://localhost:8000 then my watcheshub will be opened.

By clicking the login button gconnect will open.
I have generated client_secrets.json file I have secret key through which we can access the mail and login in it.

By login into the watchesHub  a message will be displayed such as welcome to watchstore.
in this watchstore contains watchnames,wtchlists.
I have written an url for the image when my project opens the picture will be displayed.
I have written in sidenav to display my Watchnames easily.
When I login then myname will be displayed and for logout easily logout option also displayed in nav-bar at the top.
I have used background-colors,css styles are applied for this project.

when I pressed any watchname then their related items are displayed.
with edit and delete options.

when I used edit button then their related items such as modelname,description,price,rating,color,modelweight,modellength,modelwidth these are displayed.
 
 when I used delete option then I may have chance for cancel button or delete button.
 If I used cancel button then it may be canceled.
 when I used delete button it may delete the item.
 
 I have the chance for editing watchname,adding watchname,deleting watchname by using pencil on leftside placed in the sidenav.
 
 I can use add watch category to add watchname easily.
  by adding the watchname I can also add its corresponding details for respective watch.
 

---Optional steps for this project...

#Using Google Login
To get the Google login working there are a few additional steps::

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web-application
6. Enter name 'Watch-Store'
7. Authorized JavaScript origins = 'http://localhost:8000'
8. Authorized redirect URIs = 'http://localhost:8000/login' && 'http://localhost:8000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in watch-store directory that you cloned from here
14. Run application using `python /watch_store/wsss.py`

# JSON Endpoints...
The following are open to the public:

allWatchesJSON: `/watchStore/JSON`
    -- It Displays the whole watches models and their listitems also. 
	

Watch CategoriesJSON: `/watchStore/watchCategories/JSON`
    -- It Displays all Watch categories.
	
itemsJSON: `/watchStore/watches/JSON`
	-- It Displays all items of respective watches. 

categoryItemsJSON: `/watchStore/<path:watch_name>/watches/JSON`
    -- Displays Watch models for a specific Watch category.
	in this <path:watch_name> represents Watchname then we get the watches. 

ItemJSON: `/watchStore/<path:watch_name>/<path:edition_name>/JSON`
    -- Displays a specific Watch category Model.
	in this <path:edition_name> represents the item of a specific watch.

# Miscellaneous...

This project is inspiration from [gmawji](https://github.com/gmawji/item-catalog).

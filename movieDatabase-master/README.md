# movieDatabase

- This project aims to design and implement a movie database application including both a backend database and frontend web user interface.
- The database has the following entities:
--- Crews, Genres, Movies, Reviews, Tags, Users
- This web application is designed to allow a manager add, change, and delete data in a movie database.
- Users will first register and then are able to filter the database with a faceted search.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
### Prerequisites

```
* Python version 2.7, 3.3, 3.4 and 3.5. Python 3+ is recommended.
* Python virtual environment
* Django 1.10+
* MySQL
```

### Installing

* If you’re on Linux or Mac OS X, you probably have Python already installed. Type python at a command prompt (or in Applications/Utilities/Terminal, in OS X).
* Assuming Python is not installed in your system, we first need to get the installer. Go to https://www.python.org/downloads/ and click the big yellow button that says “Download Python 3.x.x”
```
* python -m pip install -U pip 
```
Install virtual environment
```
shell> pip install virtualenv 
shell> virtualenv env_mysite 
shell> env_mysite\scripts\activate 
```
Install MySQL. We are assuming you're using Linux or Mac OS X. If not, check out how to install MySQL on this page: https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html



This assumes MySQL is being used. You can change what database that is being used by altering settings.py
Go to mysite/settings.py and go to lines 93-94 and change the MySQL username/password. 
To install and use a MySQL binary distribution, the command sequence looks like this:
```
shell> groupadd mysql
shell> useradd -r -g mysql -s /bin/false mysql
shell> cd /usr/local
shell> tar zxvf /path/to/mysql-VERSION-OS.tar.gz
shell> ln -s full-path-to-mysql-VERSION-OS mysql
shell> cd mysql
shell> mkdir mysql-files
shell> chmod 750 mysql-files
shell> chown -R mysql .
shell> chgrp -R mysql .
shell> bin/mysql_install_db --user=mysql    # MySQL 5.7.5
shell> bin/mysqld --initialize --user=mysql # MySQL 5.7.6 and up
shell> bin/mysql_ssl_rsa_setup              # MySQL 5.7.6 and up
shell> chown -R root .
shell> chown -R mysql data mysql-files
shell> bin/mysqld_safe --user=mysql &
# Next command is optional
shell> cp support-files/mysql.server /etc/init.d/mysql.server
```
Finally, install Django.
```
shell> pip install django
```

## Built With

* [Python](https://www.python.org/) - The programming language used.
* [Django](https://www.djangoproject.com/) - The web framework used.
* [Virtual Environment](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) - a tool to keep the dependencies required by different projects in separate places
* [Bootstrap](http://getbootstrap.com/) -  HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.
* [MySQL](https://www.mysql.com/) - Open source database used to handle and store our data.
* [HTML](https://en.wikipedia.org/wiki/HTML) - standard markup language for creating web pages and web applications.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - style sheet language used for describing the presentation of a document written in a markup language.




## Authors

* **Daniel Ng** - [mdng223](https://github.com/mdng223)
* **Lucian Hymer** - [lucianhymer](https://github.com/lucianhymer)
* **Tristan Basil** - [Immaculato](https://github.com/Immaculato)
* **Katie Long** - [katrinamo](https://github.com/katrinamo)


## Acknowledgments

* This was a good learning process on the use of a MVC framework. 
* In order to access the manager options, you need to log into the built in admin page and change the first user to be a manager. Following this, that manager can promote any other regular user to be a manager. Every registered account is defaulted to be a regular user at first. 

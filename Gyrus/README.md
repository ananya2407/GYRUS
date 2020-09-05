# Gyrus: An app for Doctors and Patients

### The main feature being prediction of Breast cancer, using the power of Machine Learning. 
## 10 features taken into account for the predictions and uses Logistic Regression for prediction.

Healthcare web-app that provides doctors and patients a platform for appointments, chat and contact their respective doctors.


Clone this repository in a folder and change your directory to that folder

### Contribution

All contributions to this repository are welcome. 
Also contributors must raise an issue before submitting a Pull Request

### Requisites

`pip install -r requirements.txt`

Then we need to create the database for the project. To do that use

`python3 manage.py makemigrations`

`python3 manage.py migrate`

Now the final thing to do is create a superuser

`python3 manage.py createsuperuser`

On doing this you will be prompted through a series of steps
On completion you will get a message 
`Superuser created successfully.`

Now we are done

To run this on your local machine

`python3 manage.py runserver`

On Windows:

replace `python3` with `py -3`

### Team Members
1. -[@soumyadeeptadas](https://github.com/soumyadeeptadas)
2. -[@ananya2407](https://github.com/ananya2407)
3. -[@Sid200026](https://github.com/Sid200026)

# GYRUS
Project by team # Nyx 

# Gyrus: An app for Doctors and Patients

GYRUS is a state of the art breast cancer prediction interface that employs the best machine learning tools available to accurately predict the occurrence of cancer in an individual. Current diagnosis and prediction of a disease by doctors are based on control values used by doctors to assess the condition. Normal ranges used are not always revised to consider the variance of a lot of factors such as age, lifestyle and demographics.

The need of the hour is a technical based prediction system which using historical data can predict the likelihood of cancer in a patient, saving a lot of time and effort diagnosis of the disease. Our website harnesses the power of Machine Learning to predict the status of a tumor, whether it is malignant or benign, based on inputs from a mammogram test of a tumor tissue. This solution simplifies the prediction process for doctors with enhanced accuracy and also eases the work for both patients and doctors.

### The main feature being prediction of Breast cancer, using the power of Machine Learning. 
## 10 features taken into account for the predictions and uses Logistic Regression for prediction.

Healthcare web-app that provides doctors and patients a platform for appointments, chat and contact their respective doctors.

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




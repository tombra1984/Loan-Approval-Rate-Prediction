# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals

The project goal is to combine and practice the topics that have been learned so far. These incude 
Machine learning, Serialization of models, Flask and AWS while trying to model a loan automation process to predict loan approval rate.




## Hypothesis
Males will have a higher loan approval rate. This is because males ususally are the income earners within household and in society in general. This presents them the opportunity to have good credit and income and thus higher borrowing power. 
This would be tested during the EDA process by comparing the features by gender. example male income against female income or comparing the credit score of both genders etc.
    


## EDA 
Major insights from the EDA include:
Low income range for both Applicant and Coapplicants
Males had higher incomes than females
Loan amount is approximately 1% of income
Graduates have higher income and are given higher loan values than non graduates
People with rural properties are given slighter higher loan values
Approximately 70% of all loans are given


## Process

Data Collection:

Identify the data sources and collect the required data.
Download or access the data from the sources.

Data Preprocessing:

Perform data cleaning to handle missing values, outliers, and inconsistencies.
Conduct data transformation, normalization, or scaling as necessary.
Split the data into training and testing sets.

Feature Engineering:

Analyze and select relevant features for the model.
Create new features or derive additional information from existing features.
Encode categorical variables and handle feature scaling.

Model creation:

Select an appropriate machine learning or statistical model for your problem.
Train the model using the training data.
Tune hyperparameters to optimize model performance.
Evaluate the model using the testing data.

Model Deployment:

Save the trained model to a file or serialize it for future use.
Set up a server or hosting environment for deploying the model.
Develop an API or web interface for model interaction.
Deploy the model to the server or hosting platform.

Testing:

Integrate the deployed model with the user interface or application.
Handle user input and preprocess it for model prediction.
Pass the preprocessed data to the deployed model for prediction.
Return the model's prediction to the user or application.



## Results/Demo
The model was created using a linear regressor. The model had an accuracy of approximately 70% and predicted loan approval rates of about 79%.

## Challanges 
There were several challenges associated with this project. However the major challenge was trying to launch the model and working with AWS as both were affected by security set ups.

## Future Goals
There were alot of 'Nans' within the data that was filled out using means and modes this may cause bais within the dataset.If there was more time more EDA would be done throughly to try and aviod such complications. 

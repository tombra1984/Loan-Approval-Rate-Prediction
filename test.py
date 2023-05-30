#test file

import requests as r 

base_url = 'http://127.0.0.1:5000/' #base url local host
#base_url = 'http://ec2-35-173-246-171.compute-1.amazonaws.com:5000/'

json_data = {
    'Gender': 'Male',
    'Married': 'Yes',
    'Dependents': 1,
    'Education': 'Graduate',
    'Self_Employed': 'No',
    'ApplicantIncome': 4583,
    'CoapplicantIncome': 1508,
    'LoanAmount': 128,
    'Loan_Amount_Term': 360,
    'Credit_History': 1,
    'Property_Area': 'Rural',
    'Loan_Status': 'N'
}

#get response
#response = r.get(base_url + 'helloworld')
response = r.post(base_url + "predict", json =json_data)

if response.status_code == 200:

    print ('test 1:success')
    print (response.json ())

else:
    print ('request failed')    

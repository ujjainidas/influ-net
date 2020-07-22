# -*- coding: utf-8 -*-
"""
@author: Ujjaini Das
"""
import pandas as pd

training_data_input = pd.read_csv('flu_data_cleaned.csv')
training_data_input = training_data_input.drop("DROP", axis=1)
training_data_input = training_data_input.drop("% WEIGHTED ILI", axis=1)
training_data_input = training_data_input.drop("%UNWEIGHTED ILI", axis=1)
training_data_input = training_data_input.drop("AGE 0-4", axis=1)
training_data_input = training_data_input.drop("AGE 25-49", axis=1)
training_data_input = training_data_input.drop("AGE 5-24", axis=1)
training_data_input = training_data_input.drop("AGE 50-64", axis=1)
training_data_input = training_data_input.drop("AGE 65", axis=1)
training_data_input = training_data_input.drop("AGE 25-64", axis=1)
training_data_input = training_data_input.drop("ILITOTAL", axis=1)
training_data_input = training_data_input.drop("NUM. OF PROVIDERS", axis=1)
training_data_input = training_data_input.drop("TOTAL PATIENTS", axis=1)

testing_data_input = training_data_input[len(training_data_input)//2:]
#testing_data_input.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\influ-net-linkedin-mentorship\testing_input.csv')
training_data_input = training_data_input[:len(training_data_input)//2]
#training_data_input.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\influ-net-linkedin-mentorship\training_input.csv')

training_data_output = pd.read_csv('flu_data_cleaned.csv')
training_data_output = training_data_output.drop("DROP", axis = 1)
training_data_output = training_data_output.drop("REGION", axis = 1)
training_data_output = training_data_output.drop("YEAR", axis = 1)
training_data_output = training_data_output.drop("WEEK", axis = 1)
training_data_output = training_data_output.drop("NUM. OF PROVIDERS", axis = 1)

testing_data_output = training_data_output[len(training_data_output)//2:]
#testing_data_output.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\influ-net-linkedin-mentorship\testing_output.csv')
training_data_output = training_data_output[:len(training_data_output)//2]
#training_data_output.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\influ-net-linkedin-mentorship\training_output.csv')

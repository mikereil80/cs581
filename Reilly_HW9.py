# Author: Michael Reilly
# I pledge my honor that I have abided by the Stevens Honor System.

# To run in terminal window: python3 Reilly_HW9.py;
# All graphs and charts can be found in the Plots folder after code execution.

# The goal of this program is to see the frequency of respondent's internet usage
# And whether there is a relation between that and 
# their use of social media, the region of the US the respondent lives in, 
# their gender, their age, their marital status, their employment status,
# their education level, and their political affiliation.
# This is to see whether any of these factors affect how much someone uses the internet.

import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Need to read in the Pew_Survey.csv file to use it.
survey_table=pd.read_csv('Pew_Survey.csv')
survey_table.head()

# Creating a directory to store all the created graphs and charts using matplotlib so they can be seen.
# First, check if it exists already, create it if it does not
Plots=os.getcwd()+"/Plots"
Check_Folder=os.path.isdir(Plots)
if not Check_Folder:
    os.mkdir(Plots)

# First check the relation between how often people use the internet and whether they use social media.
# Use different figures to avoid graph overlaps.
# Internet Usage was best shown as a histogram.
plt.figure(0)
plt.hist(survey_table['intfreq'], bins=20)
plt.xlabel("Internet Usage, Most -> Least")
plt.ylabel("Count")
plt.title("Internet Usage")
plt.xlim(0,10)
plt.savefig("Plots/InternetUsage.png")
plt.show()
print("Internet Usage: ")
print(survey_table['intfreq'].value_counts(), "\n")

# Having Social Media or not was best shown as a pie chart.
plt.figure(1)
survey_table['snsint2'].value_counts().plot(kind='pie', labels=["Yes", "No"])
plt.title("Has Social Media")
plt.savefig("Plots/HasSocialMedia.png")
plt.show()
print("Has Social Media: ")
print(survey_table['snsint2'].value_counts(), "\n")

# Now calculate the correlation coefficient and to see the relationship between the two aspects.
print("Internet Usage v. Has Social Media")
print(np.corrcoef(survey_table['intfreq'], survey_table['snsint2']))
print("The correlation coefficient between Internet Usage and Social Media is about 29.5%, which statistically is a weak positive relationship.")
print("This means that the more someone uses the Internet they are slightly more likely to have Social Media.\n")

# Now check the relation between Internet Usage and Region of the US.
# Regions of the US were best shown through a pie chart.
plt.figure(2)
survey_table['cregion'].value_counts().plot(kind='pie', labels=["South", "West", "Midwest", "Northeast"])
plt.title("Regions of the US")
plt.savefig("Plots/Regions.png")
plt.show()
print("Regions of the US:")
print(survey_table['cregion'].value_counts(), "\n")

print("Internet Usage v. Region of the US")
print(np.corrcoef(survey_table['intfreq'], survey_table['cregion']))
print("The correlation coefficient between Internet Usage and Region of the US is about -0.6%, which statistically indicates there is no relationship between them.\n")

# Now check the relation between Internet Usage and Gender.
# The Gender of those surveyed is best shown by pie chart.
plt.figure(3)
survey_table['sex'].value_counts().plot(kind='pie', labels=["Male", "Female"])
plt.title("Distribution of Gender")
plt.savefig("Plots/Gender.png")
plt.show()
print("Gender Distribution:")
print(survey_table['sex'].value_counts(), "\n")

print("Internet Usage v. Gender")
print(np.corrcoef(survey_table['intfreq'], survey_table['sex']))
print("The correlation coefficient between Internet Usage and Gender is 7%, which statistically indicates there is no relationship between them.\n")

# Now check the relation between someone's Internet Usage and their Age.
# This can best be represented by a scatter plot.
plt.figure(4)
plt.scatter(survey_table['age'], survey_table['intfreq'])
plt.title("Internet Usage v. Age")
plt.xlabel("Age")
plt.ylabel("Internet Usage, Golf Scores")
plt.savefig("Plots/Age.png")
plt.show()

print("Internet Usage v. Age")
print(np.corrcoef(survey_table['intfreq'], survey_table['age']))
print("The correlation coefficient between Internet Usage and Age is 33%, which statistically is a weak positive relationship.")
print("This means that the younger someone is they will use the Internet slightly more than those who are older.\n")

# Now check the relation between Internet Usage and Marital Status.
# This can best be represented by a pie chart.
plt.figure(5)
survey_table['marital'].value_counts().plot(kind='pie', labels=["Married", "Never been married", "Divorced", "Widowed", "Living with a partner", "Separated", "Refused", "Don't Know"])
plt.title("Marital Status")
plt.savefig("Plots/MaritalStatus")
plt.show()
print("Marital Status:")
print(survey_table['marital'].value_counts(), "\n")

print("Internet Usage v. Marital Status")
print(np.corrcoef(survey_table['intfreq'], survey_table['marital']))
print("The correlation coefficient between Internet Usage and Marital Status is -0.5%, which statistically indicates there is no relationship between them.\n")

# Now check the relation between Internet Usage and Employment Status.
# This can best be represented by a pie chart.
plt.figure(6)
survey_table['emplnw'].value_counts().plot(kind='pie', labels=["Employed full-time", "Retired", "Not employed for pay", "Employed part-time", "Have own business/self-employed", "Disabled", "Student", "Refused", "Other"])
plt.title("Employment Status")
plt.savefig("Plots/EmploymentStatus.png")
plt.show()
print("Employment Status:")
print(survey_table['emplnw'].value_counts(), "\n")

print("Internet Usage v. Employment Status")
print(np.corrcoef(survey_table['intfreq'], survey_table['emplnw']))
print("The correlation coefficient between Internet Usage and Employment Status is 4%, which statistically indicates there is no relationship between them.\n")

# Now check the relation between Internet Usage and Education Level.
# This can best be represented by a pie chart.
plt.figure(7)
survey_table['educ2'].value_counts().plot(kind='pie', labels=["Four-year college or university degree/Bachelor's degree", "High school graduate", "Some college, no degree", "Some postgraduate or professional schooling, no postgraduate degree", "Two-year associate degree from a college or university", "Postgraduate or professional degree, including master's, doctorate, medical, and law degree", "High school incomplete", "Less than high school", "Refused", "Don't know"])
plt.title("Education Level")
plt.savefig("Plots/EducationLevel.png")
plt.show()
print("Education Level:")
print(survey_table['educ2'].value_counts(), "\n")

print("Internet Usage v. Education Level")
print(np.corrcoef(survey_table['intfreq'], survey_table['educ2']))
print("The correlation coefficient between Internet Usage and Education Level is -3.5%, which statistically indicates there is no relationship between them.\n")

# Now check the relation between Internet Usage and Polticial Affiliation.
# This can best be represented by a pie chart.
plt.figure(8)
survey_table['party'].value_counts().plot(kind='pie', labels=["Independent", "Democrat", "Republican", "No Preference", "Refused", "Don't Know", "Other Party"])
plt.title("Political Affiliation")
plt.savefig("Plots/Poltics.png")
plt.show()
print("Polticial Affiliation:")
print(survey_table['party'].value_counts(), "\n")

print("Internet Usage v. Political Affiliation")
print(np.corrcoef(survey_table['intfreq'], survey_table['party']))
print("The correlation coefficient between Internet Usage and Political Affiliation is 6%, which statisticlly indicates there is no relationship between them.")

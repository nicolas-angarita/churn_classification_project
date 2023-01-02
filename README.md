# To Churn or not to Churn ?

# Project Goals

My goal is to identify key drivers of churn. To see which customers are at risk of churning, and make recommendations for changes, so that we can reduce the monthly churn rate and at the same time increase customer retention.

# Project Description

Anytime a business is struggling, they have to revert to the basic questions of business and answer who is the customer and what makes them stay or leave. In this case why does it seem like so many customers are churning. What are key drivers that are turning our customers away? Could it be the services we are providing, our pricing policy, our target market (age of customer, gender, etc.), or other drivers. We will analyze some of the drivers just mentioned to see if we can come up with a model to see what is causing our customers to chun. Once we have ran our models we will make recommendations on how to better retain our customers from churning in the future. 

# Initial Questions

Do customers with partners and dependents churn more than those with no dependents?
Is there a difference in age on who is churning?
Do number of add-ons affect rate of churn?
Are Senior citizens more or less likely to churn than non Senior Citizens?
Does tenure affect churn?

# The Plan

 - Create README with project goals, project description, initial hypotheses, planning of project, data dictionary, and come up with recommedations/takeaways

### Acquire Data
 - Acquire data from Sequel Ace and create a function to later import the data into a juptyer notebook. (acquire.py)

### Prepare Data
 - Clean and prepare the data creating a function that will give me data that is ready to be explored upon. Within this step we will also write a function to split our data into train, validate, and test. (prepare.py) 
 
 - Establish a baseline accuracy
 
### Explore Data
 - Create at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, document any findings and takeaways that are observed.
 
### Model Data 
 - Create and train three classification models.
 
 - Evaluate models on train and validate datasets.
 
 - Evaluate which model performs the best and on that model use the test data subset.
 
### Delivery  
 - Create CSV file with the customer_id, probability of churn, and prediction of churn for each observation in my test dataset.
 
 - Create a Final Report Notebook to document conclusions, takeaways, and next steps in recommadations for customers churning. Also, inlcude visualizations to help explain why the model that was selected is the best to better help the viewer understand. 


## Data Dictionary

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |




## Steps to Reproduce

Your readme should include useful and adequate instructions for reproducing your analysis and final report.

For example:

You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the titanic_db.passengers table. Store that env file locally in the repository.
clone my repo (including the acquireTitanic.py and prepare.Titanic.py) (confirm .gitignore is hiding your env.py file)
libraries used are pandas, matplotlib, seaborn, numpy, sklearn.
you should be able to run survival_report.

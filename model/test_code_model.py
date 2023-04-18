import joblib
import warnings
warnings.filterwarnings('ignore')

# Load the saved model from file
model = joblib.load('email_spam_checker')

# Prepare new data for prediction
user_input = input("Please copy the email: ")
#new_data = ['Congratulations! Youve been selected to receive a free cruise to the Bahamas! This is a limited time offer, so act now to claim your prize.']

# Use the loaded model to make predictions on the new data
predictions = model.predict([user_input])

# Print the predictions

if predictions == 1:
    print("\n!!!! This is a spam email.")

else:
    print("\n!!!! This is not a spam email.")

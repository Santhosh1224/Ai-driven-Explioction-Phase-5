# Import necessary libraries
from sklearn import tree

# Define a dataset of fruit features (weight in grams and color)
# The label '0' represents 'apple' and '1' represents 'orange'
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

# Create a decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier on the dataset
clf = clf.fit(features, labels)

# Input from the user
weight = int(input("Enter the weight of the fruit (grams): "))
color = int(input("Enter the color (0 for red, 1 for orange): "))

# Make a prediction using the trained model
prediction = clf.predict([[weight, color]])

# Map the prediction back to the fruit name
fruit_name = "apple" if prediction[0] == 0 else "orange"

# Display the prediction
print(f"The fruit is a {fruit_name}")

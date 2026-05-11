from sklearn.neural_network import MLPClassifier
 
# Input Dataset
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
 
# AND Gate Output
y = [0, 0, 0, 1]
 
# Create Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(2,),
    activation='logistic',
    solver='lbfgs',
    max_iter=5000,
    random_state=42
)
 
# Train Model
model.fit(X, y)
 
# Prediction
print("AND Gate Predictions:")
 
for data in X:
    print(data, "->", model.predict([data])[0])

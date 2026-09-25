# 🐍 Snake Game AI

An AI-powered Snake Game project built with Python and Machine Learning.

The project uses a **Random Forest Classifier** to learn from game situations and predict the best action for the Snake.

## 🚀 Features

- 🐍 Classic Snake Game
- 🤖 AI-controlled Snake
- 🌳 Random Forest Classifier
- 📊 Machine Learning model training
- 🎯 Action prediction
- ⚡ Real-time decision making

## 🛠️ Technologies

- Python
- Pygame
- NumPy
- Scikit-learn
- Random Forest

## 🧠 How It Works

The AI observes the current state of the Snake game and uses this information to decide which direction the Snake should move.

### 1. Game State

At each step, the program collects information about the current game state, such as:

- Snake position
- Food position
- Distance to the food
- Possible obstacles
- Current movement direction
- Whether moving in a direction is dangerous

This information is converted into numerical features that can be given to the machine learning model.

### 2. Random Forest Model

The project uses a Random Forest Classifier:

```python
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

# Algerian Forest Fire Prediction

A machine learning web application that predicts the burned area of forest fires in Algeria using meteorological and geographical data.

## Project Overview

This project implements a Ridge Regression model to predict the extent of burned areas in forest fires based on various environmental factors. The model is deployed as a web application using Flask, allowing users to input parameters and receive predictions in real-time.

## Dataset

The model was trained on the Algerian Forest Fire dataset, which contains weather data and fire observations from the Sidi Bel-abbes region and Bejaia region of Algeria from June 2012 to September 2012.

Key Features:
- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rainfall (Rain)
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Initial Spread Index (ISI)
- Classes (numerical encoding of fire danger)
- Region (numerical encoding of geographical region)

Target Variable:
- Burned Area (in hectares)

## Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework
- **Scikit-learn**: Machine learning library
  - Ridge Regression
  - Standard Scaler
- **Pandas & NumPy**: Data manipulation and numerical operations
- **Pickle**: Model serialization
- **HTML/CSS**: Frontend interface

## Project Structure

```
├── app.py                # Flask application
├── config.py             # Configuration settings
├── models/               # Trained model files
│   ├── ridge.pkl         # Ridge regression model
│   ├── scaler.pkl        # StandardScaler preprocessing model
│   └── linear.pkl        # Linear regression model (alternative)
├── templates/            # HTML templates
│   ├── index.html        # Landing page
│   └── home.html         # Results page
├── README.md             # Project documentation
└── requirements.txt      # Dependencies
```

## Installation & Setup

1. Clone the repository:
   ```
   git clone https://github.com/tejask0512/Algerian_ForestFire_ML-project_Cloud.git
   cd Algerian_ForestFire_ML-project_Cloud
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Access the web application at http://127.0.0.1:5000/

## Usage

1. Enter the required meteorological and geographical data in the form.
2. Submit the form to get a prediction of the potential burned area.
3. The application will display the predicted area in hectares.

## Model Information

This project implements multiple regression models, with Ridge Regression being the primary model. The models were trained on historical data and evaluated for accuracy. The Ridge model was chosen for its robustness against multicollinearity in the dataset features.

Key steps in the modeling process:
1. Data preprocessing and feature scaling
2. Model training and hyperparameter tuning
3. Model evaluation and selection
4. Deployment via Flask web framework

## Future Improvements

- Implement additional regression models for comparison
- Add data visualization features
- Enhance the web interface with dynamic charts
- Include more detailed geographical information
- Add real-time weather data integration


## Contact

👨‍💻 Author
Tejas Kamble
🌐 tejaskamble.com
🔗 GitHub

## Acknowledgements

- Dataset source: [UCI Machine Learning Repository - Algerian Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++)
- Contributors and collaborators

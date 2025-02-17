import matplotlib.pyplot as plt

# Data
features = [
    "age_ADULT <= 0.00",
    "30.50 < enrollment <= 56.00",
    "funder_type_INDUSTRY <= 0.00",
    "study_title_385 <= 0.02",
    "-0.26 < study_title_284 <= 0.06",
    "-0.14 < conditions_262 <= -0.04",
    "secondary_outcome_measures_632 <= -0.05",
    "secondary_outcome_measures_244 <= -0.05",
    "-0.20 < interventions_284 <= 0.03",
    "0.01 < secondary_outcome_measures_7 <= 0.12"
]

weights = [
    0.04759088657908404,
    -0.035661975117007666,
    0.02196459196217836,
    -0.002205494801272586,
    -0.001889128958661916,
    -0.0015373130185348674,
    0.0012037810103344788,
    -0.0006367428569417232,
    0.000521972082833042,
    -0.00014078655483393566
]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.barh(features, weights, color='skyblue')
plt.xlabel('Weight')
plt.title('Feature Weights for LIME Explanation')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add data labels
for i, weight in enumerate(weights):
    plt.text(weight, i, f"{weight:.6f}", va='center', ha='left' if weight > 0 else 'right', color='black')

# Show the plot
plt.tight_layout()
plt.show()
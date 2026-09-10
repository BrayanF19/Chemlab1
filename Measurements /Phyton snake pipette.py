#this is density graph using pipette
import matplotlib.pyplot as plt

# Measurement numbers
measurements = [1, 2, 3, 4, 5]

# Density measurements using volumetric pipettes (g/mL)
densities = [0.926, 1.009, 1.003, 1.005, 0.9992]

# Average and sample standard deviation
average = 0.98844
standard_deviation = 0.03508

# Reference density of water (g/mL)
water_density = 0.997

# Create graph
plt.figure(figsize=(8, 6))

# Create bars with error bars
plt.bar(
    measurements,
    densities,
    width=0.5,
    yerr=standard_deviation,
    capsize=6,
    label="Measured Density"
)

# Average density reference line
plt.axhline(
    y=average,
    linestyle="--",
    linewidth=2,
    label="Average Density = 0.98844 g/mL"
)

# Water density reference line
plt.axhline(
    y=water_density,
    linestyle=":",
    linewidth=2,
    label="Water Density = 0.997 g/mL"
)

# X-axis
plt.xlabel("Measurement")
plt.xticks([1, 2, 3, 4, 5])

# Y-axis
plt.ylabel("Density (g/mL)")
plt.ylim(0, 1.5)
plt.yticks([0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50])

# Graph title
plt.title("Density Measurements Using Volumetric Pipettes")

# Add density value above each error bar
for measurement, density in zip(measurements, densities):
    plt.text(
        measurement,
        density + standard_deviation + 0.02,
        f"{density:.4f}",
        ha="center"
    )

# Display standard deviation
plt.text(
    0.02,
    0.95,
    "Error Bars = ±1 SD (0.03508 g/mL)",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

# Show legend
plt.legend()

# Adjust spacing
plt.tight_layout()

# Display graph
plt.show()
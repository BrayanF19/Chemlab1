#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Measurement numbers
measurements = [1, 2, 3, 4, 5]

# Density measurements (g/mL)
densities = [0.920, 0.984, 0.970, 0.981, 0.978]

# Average and sample standard deviation
average = 0.9666
standard_deviation = 0.0263

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

# Average density line
plt.axhline(
    y=average,
    linestyle="--",
    linewidth=2,
    label="Average Density = 0.9666 g/mL"
)

# Water density reference line
plt.axhline(
    y=water_density,
    linestyle=":",
    linewidth=2,
    label="Water Density = 0.997 g/mL"
)

# Axis labels
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")

# X-axis values
plt.xticks([1, 2, 3, 4, 5])

# Y-axis range
plt.ylim(0, 1.5)
plt.yticks([0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50])

# Graph title
plt.title("Density Measurements with Error Bars")

# Add density value above each error bar
for measurement, density in zip(measurements, densities):
    plt.text(
        measurement,
        density + standard_deviation + 0.02,
        f"{density:.3f}",
        ha="center"
    )

# Show standard deviation
plt.text(
    0.02,
    0.95,
    "Error bars = ±1 SD (0.0263 g/mL)",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

# Legend
plt.legend()

plt.tight_layout()
plt.show()
#this is second
import matplotlib.pyplot as plt

# Measurement numbers
measurements = [1, 2, 3, 4, 5]

# Density measurements (g/mL)
densities = [0.920, 0.984, 0.970, 0.981, 0.978]

# Average and sample standard deviation
average = 0.9666
standard_deviation = 0.0263

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

# Average density line
plt.axhline(
    y=average,
    linestyle="--",
    linewidth=2,
    label="Average Density = 0.9666 g/mL"
)

# Water density reference line
plt.axhline(
    y=water_density,
    linestyle=":",
    linewidth=2,
    label="Water Density = 0.997 g/mL"
)

# Axis labels
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")

# X-axis values
plt.xticks([1, 2, 3, 4, 5])

# Y-axis range
plt.ylim(0, 1.5)
plt.yticks([0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50])

# Graph title
plt.title("Density Measurements with Error Bars")

# Add density value above each error bar
for measurement, density in zip(measurements, densities):
    plt.text(
        measurement,
        density + standard_deviation + 0.02,
        f"{density:.3f}",
        ha="center"
    )

# Show standard deviation
plt.text(
    0.02,
    0.95,
    "Error bars = ±1 SD (0.0263 g/mL)",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

# Legend
plt.legend()

plt.tight_layout()
plt.show()
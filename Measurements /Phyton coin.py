#this is the penny graph
import matplotlib.pyplot as plt

# Measurement numbers
measurements = [1, 2, 3, 4]

# Calculated density for each measurement (g/cm^3)
densities = [9.59, 9.59, 9.59, 9.59]

# Average experimental density
average_density = 9.59

# Standard deviation
standard_deviation = 0.00

# Reference density for a modern penny (approximately g/cm^3)
reference_density = 7.20

# Create graph
plt.figure(figsize=(8, 6))

# Create bars
plt.bar(
    measurements,
    densities,
    width=0.5,
    label="Measured Density"
)

# Experimental average density line
plt.axhline(
    y=average_density,
    linestyle="--",
    linewidth=2,
    label="Average Density = 9.59 g/cm³"
)

# Reference density line
plt.axhline(
    y=reference_density,
    linestyle=":",
    linewidth=2,
    label="Reference Penny Density = 7.20 g/cm³"
)

# X-axis
plt.xlabel("Measurement")
plt.xticks([1, 2, 3, 4])

# Y-axis
plt.ylabel("Density (g/cm³)")
plt.ylim(0, 12)
plt.yticks([0, 2, 4, 6, 8, 10, 12])

# Graph title
plt.title("Density Measurements of a Penny")

# Add density values above bars
for measurement, density in zip(measurements, densities):
    plt.text(
        measurement,
        density + 0.2,
        f"{density:.2f}",
        ha="center"
    )

# Display standard deviation
plt.text(
    0.02,
    0.95,
    "Standard Deviation = 0.00 g/cm³",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

# Legend
plt.legend()

# Adjust graph spacing
plt.tight_layout()

# Display graph
plt.show()
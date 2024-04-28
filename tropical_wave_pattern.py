import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.ndimage import gaussian_filter

# Image sizing, creating a grid of coordinates
width, height = 400, 400
x = np.linspace(0, 2 * np.pi, width)
y = np.linspace(0, 2 * np.pi, height)
X, Y = np.meshgrid(x, y)

# Define colors (tropical color palette)
color1 = np.array([0.0, 0.5, 0.8])  # Dark Blue
color2 = np.array([0.0, 0.8, 1.0])  # Cyan
color3 = np.array([0.0, 0.3, 0.4])  # Dark Cyan
color4 = np.array([0.0, 0.2, 0.3])  # Very Dark Cyan

# Create a tropical wave-like pattern
fabric = np.sin(15 * np.pi * X + Y) + np.cos(15 * np.pi * Y + X)

# Generate Perlin noise
noise = np.random.normal(size=(height, width))
perlin_noise = ndimage.gaussian_filter(noise, sigma=5)

# Combine pattern and noise
fabric = np.sin(20 * np.pi * perlin_noise)

# Create the final color image by interpolating between colors
color_image = np.zeros((height, width, 3))
for i in range(3):
    color_image[:, :, i] = np.interp(fabric, [fabric.min(), fabric.max()], [color1[i], color2[i]])

# Display Image
plt.imshow(color_image)
plt.axis('off')
plt.savefig('images/results/tropical_wave_pattern.png')  # Save the color image
plt.show()

# Convert the color image to grayscale
gray_image = np.mean(color_image, axis=2)

# Calculate the mean and standard deviation of the grayscale image
mean_value = np.mean(gray_image)
std_deviation = np.std(gray_image)

print("Mean of the image:", mean_value)
print("Standard deviation of the image:", std_deviation)

# Flatten the grayscale image to a 1D array
gray_flat = gray_image.flatten()

# Create a figure with subplots
fig, axs = plt.subplots(1, 4, figsize=(15, 4))

# Plot the histogram of the grayscale image
axs[0].hist(gray_flat, bins=250, color='gray', alpha=0.7)
axs[0].set_title('Grayscale Image')
axs[0].set_xlabel('Pixel Intensity')
axs[0].set_ylabel('Frequency')
axs[0].grid(True)

# Specify colors for RGB histograms
channel_colors = ['red', 'green', 'blue']

# Plot standalone histograms for each RGB channel with specified colors
for i in range(3):
    axs[i+1].hist(color_image[:, :, i].flatten(), bins=250, color=channel_colors[i], alpha=0.7)
    axs[i+1].set_title(f'Channel {["Red", "Green", "Blue"][i]}')
    axs[i+1].set_xlabel('Pixel Intensity')
    axs[i+1].set_ylabel('Frequency')
    axs[i+1].grid(True)

plt.tight_layout()
plt.savefig('images/results/histograms.png')  # Save the histograms image
plt.show()

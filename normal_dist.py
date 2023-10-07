import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm  # Import the normal distribution module

# Dictionary with keys as labels and values as the data values
mice_dict = {"key":[10.2,12.5,15.1,11.0]}

# Loop through key value pairs and create normal distribution
for key, values in mice_dict.items():
    # Mean and standard deviation for current key's data
    mean = np.mean(values)
    std_dev = np.std(values)
    
    # Data points for normal distribution (perfect normal distribution)
    num_samples = 1000  # Number of data points to generate
    generated_data = np.random.normal(mean, std_dev, num_samples)
    
    # Histogram for the generated data
    # Create a range of x values for the normal distribution curve
    x_range = np.linspace(min(generated_data), max(generated_data), 100)

    # Calculate the PDF values for the normal distribution
    pdf_values = norm.pdf(x_range, mean, std_dev)

    # Plot the normal distribution curve as a line
    plt.plot(x_range, pdf_values, 'r-', label='Normal Distribution')

    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.hist(generated_data, bins=65, density=True, alpha=0.6, label='Generated Data')
    plt.title(f'Normal Distribution Plot for {key}')
    plt.legend()
    plt.show()
    
    
# Separability --> P1(mean1,std1) and P2(mean2,std2) --> separability is (mean2-mean1)/(std1*std2)
# Separability is between 0 and infinity 



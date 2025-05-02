import matplotlib.pyplot as plt
import numpy as np

with open('train_loss_hist.txt', 'r') as f:
    data = f.read()
    loss_values = [float(val.strip()) for val in data.split(',') if val.strip()]

with open('val_loss_hist.txt', 'r') as f:
    data = f.read()
    val_loss_values = [float(val.strip()) for val in data.split(',') if val.strip()]

# mean val_loss 
mean_val_loss = np.mean(val_loss_values)


# We will reduce the number of points to plot for better visualization
# by taking mean of every 100 value

loss_values = loss_values[0:len(loss_values)//250*250]  # Ensure we have a multiple of 500
reduced_loss_values = [sum(loss_values[i:i+250])/250 for i in range(0, len(loss_values), 250)]

plt.figure(figsize=(12, 6))
plt.axhline(y=mean_val_loss, color='green', linestyle='--', label='Mean Validation Loss')
plt.plot(reduced_loss_values, marker='o', color='blue', label='Loss')
plt.title('Training Loss Over Time')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
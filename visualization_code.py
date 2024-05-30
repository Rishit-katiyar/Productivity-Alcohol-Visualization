import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
time = np.linspace(0, 240, 1000)  # time in minutes (0 to 240 minutes or 4 hours)

# Blood Thinning Effect: Gaussian-like distribution peaking at 60 minutes
blood_thinning_effect = np.exp(-0.005 * (time - 60) ** 2)

# Productivity Boost Effect: Directly related to blood thinning effect
productivity_boost = blood_thinning_effect / 2  # scaling for visualization purposes

# Alcohol Metabolism: Exponential decay representing declining BAC over time
initial_bac = 0.08  # Initial BAC
half_life = 40  # Half-life of alcohol metabolism in minutes
alcohol_metabolism = initial_bac * np.exp(-time / half_life)

# Different rates of alcohol metabolism
fast_metabolism = initial_bac * np.exp(-time / 30)
slow_metabolism = initial_bac * np.exp(-time / 60)

# Peak values
peak_blood_thinning = max(blood_thinning_effect)
peak_productivity = max(productivity_boost)

# Creating subplots
fig, axs = plt.subplots(4, 2, figsize=(18, 24), sharex=True)

# Blood Thinning Effect
color = 'tab:red'
axs[0, 0].plot(time, blood_thinning_effect, color=color, label='Blood Thinning Effect', linewidth=2)
axs[0, 0].fill_between(time, blood_thinning_effect, color=color, alpha=0.1)
axs[0, 0].scatter(60, peak_blood_thinning, color=color, edgecolor='black', zorder=5)
axs[0, 0].text(60, peak_blood_thinning + 0.1, f'Peak: {peak_blood_thinning:.2f}', ha='center', color=color,
               fontsize=12, fontweight='bold')
axs[0, 0].set_ylabel('Blood Thinning Effect', color=color, fontsize=14)
axs[0, 0].tick_params(axis='y', labelcolor=color)
axs[0, 0].legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
axs[0, 0].set_title('Blood Thinning Effect Over Time', fontsize=16, fontweight='bold')
axs[0, 0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[0, 0].annotate('Peak Blood Thinning Effect', xy=(60, peak_blood_thinning), xytext=(100, 1.5),
                  arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='red', fontweight='bold')

# Productivity Boost Effect
color = 'tab:blue'
axs[0, 1].plot(time, productivity_boost, color=color, linestyle='--', label='Productivity Boost', linewidth=2)
axs[0, 1].fill_between(time, productivity_boost, color=color, alpha=0.1)
axs[0, 1].scatter(60, peak_productivity, color=color, edgecolor='black', zorder=5)
axs[0, 1].text(60, peak_productivity + 0.05, f'Peak: {peak_productivity:.2f}', ha='center', color=color,
               fontsize=12, fontweight='bold')
axs[0, 1].set_ylabel('Productivity Boost', color=color, fontsize=14)
axs[0, 1].tick_params(axis='y', labelcolor=color)
axs[0, 1].legend(loc='upper left', fontsize=12, frameon=True, shadow=True)
axs[0, 1].set_title('Productivity Boost Over Time', fontsize=16, fontweight='bold')
axs[0, 1].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[0, 1].annotate('Peak Productivity Boost', xy=(60, peak_productivity), xytext=(100, 0.8),
                  arrowprops=dict(facecolor='blue', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='blue', fontweight='bold')

# Alcohol Metabolism
color = 'tab:green'
axs[1, 0].plot(time, alcohol_metabolism, color=color, label='Normal Metabolism (Half-life: 40 min)', linewidth=2)
axs[1, 0].plot(time, fast_metabolism, color='tab:orange', linestyle='-', label='Fast Metabolism (Half-life: 30 min)',
               linewidth=2)
axs[1, 0].plot(time, slow_metabolism, color='tab:purple', linestyle='-', label='Slow Metabolism (Half-life: 60 min)',
               linewidth=2)
axs[1, 0].fill_between(time, alcohol_metabolism, color=color, alpha=0.1)
axs[1, 0].axhline(y=0.08, color='grey', linestyle='--', linewidth=1, label='Legal Driving Limit (0.08%)')
axs[1, 0].set_ylabel('Blood Alcohol Concentration (BAC)', color=color, fontsize=14)
axs[1, 0].set_xlabel('Time (minutes)', fontsize=14)
axs[1, 0].tick_params(axis='y', labelcolor=color)
axs[1, 0].legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
axs[1, 0].set_title('Alcohol Metabolism Over Time', fontsize=16, fontweight='bold')
axs[1, 0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[1, 0].annotate('Declining Alcohol Levels', xy=(150, alcohol_metabolism[500]), xytext=(200, 0.1),
                  arrowprops=dict(facecolor='green', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='green', fontweight='bold')

# Combined Effects
color1 = 'tab:red'
color2 = 'tab:blue'
axs[1, 1].plot(time, blood_thinning_effect, color=color1, label='Blood Thinning Effect', linewidth=2)
axs[1, 1].plot(time, productivity_boost, color=color2, linestyle='--', label='Productivity Boost', linewidth=2)
axs[1, 1].fill_between(time, blood_thinning_effect, color=color1, alpha=0.1)
axs[1, 1].fill_between(time, productivity_boost, color=color2, alpha=0.1)
axs[1, 1].set_ylabel('Effect Intensity', fontsize=14)
axs[1, 1].set_xlabel('Time (minutes)', fontsize=14)
axs[1, 1].legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
axs[1, 1].set_title('Combined Effects of Alcohol Consumption Over Time', fontsize=16, fontweight='bold')
axs[1, 1].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[1, 1].annotate('Peak Blood Thinning', xy=(60, peak_blood_thinning), xytext=(100, 1.5),
                  arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='red', fontweight='bold')
axs[1, 1].annotate('Peak Productivity', xy=(60, peak_productivity), xytext=(100, 0.8),
                  arrowprops=dict(facecolor='blue', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='blue', fontweight='bold')

# Additional Effects (Heart Rate and Cognitive Function)
# Heart Rate Increase: Gaussian-like distribution peaking at 45 minutes
heart_rate_increase = np.exp(-0.007 * (time - 45) ** 2)

# Cognitive Function: Gaussian-like distribution peaking at 30 minutes
cognitive_function = np.exp(-0.01 * (time - 30) ** 2)

# Heart Rate Increase Effect
color = 'tab:orange'
axs[2, 0].plot(time, heart_rate_increase, color=color, label='Heart Rate Increase', linewidth=2)
axs[2, 0].fill_between(time, heart_rate_increase, color=color, alpha=0.1)
axs[2, 0].scatter(45, max(heart_rate_increase), color=color, edgecolor='black', zorder=5)
axs[2, 0].text(45, max(heart_rate_increase) + 0.1, f'Peak: {max(heart_rate_increase):.2f}', ha='center',
               color=color, fontsize=12, fontweight='bold')
axs[2, 0].set_ylabel('Heart Rate Increase', color=color, fontsize=14)
axs[2, 0].tick_params(axis='y', labelcolor=color)
axs[2, 0].legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
axs[2, 0].set_title('Heart Rate Increase Over Time', fontsize=16, fontweight='bold')
axs[2, 0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[2, 0].annotate('Peak Heart Rate Increase', xy=(45, max(heart_rate_increase)), xytext=(80, 1.5),
                  arrowprops=dict(facecolor='orange', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='orange', fontweight='bold')

# Cognitive Function Effect
color = 'tab:purple'
axs[2, 1].plot(time, cognitive_function, color=color, label='Cognitive Function', linewidth=2)
axs[2, 1].fill_between(time, cognitive_function, color=color, alpha=0.1)
axs[2, 1].scatter(30, max(cognitive_function), color=color, edgecolor='black', zorder=5)
axs[2, 1].text(30, max(cognitive_function) + 0.1, f'Peak: {max(cognitive_function):.2f}', ha='center', color=color,
               fontsize=12, fontweight='bold')
axs[2, 1].set_ylabel('Cognitive Function', color=color, fontsize=14)
axs[2, 1].tick_params(axis='y', labelcolor=color)
axs[2, 1].legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
axs[2, 1].set_title('Cognitive Function Over Time', fontsize=16, fontweight='bold')
axs[2, 1].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[2, 1].annotate('Peak Cognitive Function', xy=(30, max(cognitive_function)), xytext=(70, 1.5),
                  arrowprops=dict(facecolor='purple', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='purple', fontweight='bold')

# Alcohol Effects on Heart Rate and Cognitive Function Combined
color1 = 'tab:orange'
color2 = 'tab:purple'
axs[3, 0].plot(time, heart_rate_increase, color=color1, label='Heart Rate Increase', linewidth=2)
axs[3, 0].plot(time, cognitive_function, color=color2, linestyle='--', label='Cognitive Function', linewidth=2)
axs[3, 0].fill_between(time, heart_rate_increase, color=color1, alpha=0.1)
axs[3, 0].fill_between(time, cognitive_function, color=color2, alpha=0.1)
axs[3, 0].set_ylabel('Effect Intensity', fontsize=14)
axs[3, 0].set_xlabel('Time (minutes)', fontsize=14)
axs[3, 0].legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
axs[3, 0].set_title('Combined Effects on Heart Rate and Cognitive Function', fontsize=16, fontweight='bold')
axs[3, 0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[3, 0].annotate('Peak Heart Rate Increase', xy=(45, max(heart_rate_increase)), xytext=(80, 1.5),
                  arrowprops=dict(facecolor='orange', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='orange', fontweight='bold')
axs[3, 0].annotate('Peak Cognitive Function', xy=(30, max(cognitive_function)), xytext=(70, 1.5),
                  arrowprops=dict(facecolor='purple', shrink=0.05, width=2, headwidth=8),
                  fontsize=12, color='purple', fontweight='bold')

# Overall Title and Layout
fig.suptitle('Visualization of Alcohol Consumption Effects Over Time', fontsize=24, fontweight='bold')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for the overall title

# Show Plot
plt.show()

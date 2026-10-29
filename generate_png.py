import matplotlib
matplotlib.use("Agg")  # Works without a GUI

import matplotlib.pyplot as plt

# Create a simple 
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot([1, 2, 3, 4, 5], [2, 4, 3, 6, 5], marker="o")
ax.set_title("My Generated PNG")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

# Save PNG
plt.savefig("output.png", dpi=150, bbox_inches="tight")
plt.close()

print("PNG generated: output.png")

import os
import pandas as pd

# Directory containing the generated images
# image_dir = "generated_faces" #"fine_tuned_faces"
image_dir = "fine_tuned_faces"

# Collect all PNG files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith(".png")]

# Create full paths
img_paths = [os.path.join(image_dir, fname) for fname in sorted(image_files)]

# Save to CSV
df = pd.DataFrame({"img_path": img_paths})
df.to_csv("image_paths_fine_tuned.csv", index=False)

print("image_paths_fine_tuned.csv has been created.")

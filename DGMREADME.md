Once you download the 70 images from Colab, you can put them in fine_tuned_faces.

Then, you can use create_image_paths.py to generate the csv

You can use this command:
python3 predict.py --csv image_paths_fine_tuned.csv


Then, you can pass image_paths_fine_tuned.csv to visualize.py to generate the visualizations. You can adjust the labels and titles as needed.


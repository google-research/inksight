import os
import random
import argparse
import matplotlib.pyplot as plt
from utils.io import inkml_to_ink, parse_inkml_annotations, load_and_pad_img_dir
from utils.visualize import plot_ink


def visualize_samples(dataset, num_samples, model, data_dir="./data"):
    """Visualize samples from the dataset with different inference modes.

    Args:
        dataset (str): Dataset name ("IMGUR5K", "IAM", "HierText")
        num_samples (int): Number of samples to visualize
        model (str): Model name ("Small-i", "Large-i", "Small-p")
        data_dir (str): Base directory containing the data
    """
    # Set up paths
    inkml_path = os.path.join(data_dir, f"{model.lower()}_{dataset.lower()}_inkml")
    image_path = os.path.join(data_dir, dataset, "images_sample")

    # Validation
    if not os.path.exists(image_path):
        raise ValueError(f"Dataset path not found: {image_path}")
    if not os.path.exists(inkml_path):
        raise ValueError(f"Model outputs not found: {inkml_path}")

    # Get samples
    samples = os.listdir(image_path)
    picked_samples = random.sample(samples, min(num_samples, len(samples)))

    # Plot settings
    plot_title = {"r+d": "Recognized: ", "d+t": "OCR Input: ", "vanilla": "Vanilla"}
    query_modes = ["d+t", "r+d", "vanilla"]

    # Visualize each sample
    for name in picked_samples:
        fig, ax = plt.subplots(1, 1 + len(query_modes), figsize=(6 * len(query_modes), 4))

        # Plot input image
        img = load_and_pad_img_dir(os.path.join(image_path, name))
        ax[0].set_xticks([])
        ax[0].set_yticks([])
        ax[0].imshow(img)
        ax[0].set_title("Input")

        # Plot each inference mode
        for i, mode in enumerate(query_modes):
            example_id = name.strip(".png")
            inkml_file = os.path.join(inkml_path, mode, f"{example_id}.inkml")

            try:
                ink = inkml_to_ink(inkml_file)
                text_field = parse_inkml_annotations(inkml_file)["textField"]

                plot_ink(ink, ax[1 + i], input_image=img, lw=1.8)
                ax[1 + i].set_xticks([])
                ax[1 + i].set_yticks([])
                ax[1 + i].set_title(f"{plot_title[mode]}{text_field}")
            except Exception as e:
                print(f"Error processing {inkml_file}: {str(e)}")

        plt.tight_layout()
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="Visualize InkSight dataset samples")
    parser.add_argument(
        "--dataset", type=str, choices=["IMGUR5K", "IAM", "HierText"], default="HierText", help="Dataset to visualize"
    )
    parser.add_argument("--num_samples", type=int, default=3, help="Number of samples to visualize")
    parser.add_argument(
        "--model", type=str, choices=["Small-i", "Large-i", "Small-p"], default="Small-i", help="Model to use"
    )
    parser.add_argument(
        "--data_dir", type=str, default="./InkSight-Derenderings", help="Base directory containing the data"
    )

    args = parser.parse_args()
    visualize_samples(args.dataset, args.num_samples, args.model, args.data_dir)


if __name__ == "__main__":
    main()

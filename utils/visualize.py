import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.colors as mcolors
import copy
import numpy as np
import colorsys
from PIL import ImageEnhance
from matplotlib.patheffects import withStroke
import matplotlib.animation as animation


def plot_ink(ink, ax, lw=1.8, input_image=None, with_path=True, path_color="white", N=224):
    """Plot ink strokes with rainbow coloring.

    Args:
        ink (Ink): Ink object to visualize
        ax: Matplotlib axis
        lw (float): Line width
        input_image: Optional background image
        with_path (bool): Whether to show path effects
        path_color (str): Color of path outline
    """
    if input_image is not None:
        img = copy.deepcopy(input_image)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.45)
        ax.imshow(img)

    base_colors = plt.cm.get_cmap("rainbow", len(ink.strokes))

    for i, stroke in enumerate(ink.strokes):
        x, y = np.array(stroke.x), np.array(stroke.y)
        base_color = base_colors(len(ink.strokes) - 1 - i)
        hsv_color = colorsys.rgb_to_hsv(*base_color[:3])
        darker_color = colorsys.hsv_to_rgb(hsv_color[0], hsv_color[1], max(0, hsv_color[2] * 0.65))
        colors = [mcolors.to_rgba(darker_color, alpha=1 - (0.5 * j / len(x))) for j in range(len(x))]

        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        lc = LineCollection(segments, colors=colors, linewidth=lw)
        if with_path:
            lc.set_path_effects([withStroke(linewidth=lw * 1.25, foreground=path_color)])
        ax.add_collection(lc)

    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.invert_yaxis()


def plot_ink_to_gif(ink, output_filename, lw=1.8, input_image=None, path_color="white", fps=30, N=224):
    """Create animated GIF of ink strokes.

    Args:
        ink (Ink): Ink object to animate
        output_filename (str): Output path
        lw (float): Line width
        input_image: Optional background image
        path_color (str): Color of path outline
        fps (int): Frames per second
        N (int): max value for x and y axes
    """
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)

    if input_image is not None:
        img = copy.deepcopy(input_image)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.45)
        ax.imshow(img)

    base_colors = plt.cm.get_cmap("rainbow", len(ink.strokes))

    def get_segments(stroke):
        x, y = np.array(stroke.x), np.array(stroke.y)
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        return np.concatenate([points[:-1], points[1:]], axis=1)

    all_segments = [get_segments(stroke) for stroke in ink.strokes]
    max_frames = sum(len(segments) for segments in all_segments)

    def update(frame):
        current_frame = 0
        for i, segments in enumerate(all_segments):
            if current_frame + len(segments) > frame:
                segment_index = frame - current_frame
                base_color = base_colors(len(ink.strokes) - 1 - i)
                hsv_color = colorsys.rgb_to_hsv(*base_color[:3])
                darker_color = colorsys.hsv_to_rgb(hsv_color[0], hsv_color[1], max(0, hsv_color[2] * 0.65))
                colors = [
                    mcolors.to_rgba(darker_color, alpha=1 - (0.5 * j / len(segments))) for j in range(len(segments))
                ]

                lc = LineCollection(segments[: segment_index + 1], colors=colors[: segment_index + 1], linewidth=lw)
                if path_color:
                    lc.set_path_effects([withStroke(linewidth=lw * 1.25, foreground=path_color)])
                ax.add_collection(lc)
                break
            current_frame += len(segments)
        return ax.collections

    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.invert_yaxis()
    plt.tight_layout()
    ax.axis("off")
    ani = animation.FuncAnimation(fig, update, frames=max_frames, blit=True)
    ani.save(output_filename, writer="imagemagick", fps=fps)
    plt.close(fig)

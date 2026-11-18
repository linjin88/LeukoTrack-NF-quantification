# -*- coding: utf-8 -*-
"""Draw the pipeline-overview figure for the B manuscript (CMPB version).

The canvas is sized to the actual text width of the elsarticle `review`
layout (344 pt = 4.78 in), so the labels print at their nominal size instead
of being scaled down.  Left column: two photographs carried over from the
original combined-manuscript figure (the nailfold capillaroscopy device and
an example imaged finger; the rectangle marks the imaged nailfold region).
Right: the four-tier flowchart -- input/enhancement+detection, pass 1 and
the ST branch, then pass 2 and the velocity output.

Photographs live in ./photos/ and are cropped from the pre-split
Figure 1 source image (no content modification; overlay arrows and baked-in
captions were excluded by cropping, captions are re-set as vector text).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from PIL import Image

BLUE_F, BLUE_E = "#DEEBF7", "#2E75B6"
GREEN_F, GREEN_E = "#E2EFDA", "#548235"
CREAM_F, CREAM_E = "#FFF2CC", "#BF9000"
GREY_F, GREY_E = "#EDEDED", "#7F7F7F"
ARROW = "#2E75B6"
TXT = "#1A1A1A"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 6.3,
    "pdf.fonttype": 42,
    "mathtext.fontset": "dejavusans",
})

# canvas geometry
W_IN, H_IN = 4.78, 3.30          # figure size in inches
UX = 100.0 / W_IN                # x-units per inch
UY = 100.0 / H_IN                # y-units per inch


def box(ax, x, y, w, h, title, body="", fc=BLUE_F, ec=BLUE_E, tsize=7.1,
        bsize=6.0):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.0,rounding_size=0.7",
        linewidth=0.8, facecolor=fc, edgecolor=ec, zorder=2))
    ty = y + h - 1.6 if body else y + h / 2
    ax.text(x + w / 2, ty, title, ha="center",
            va="top" if body else "center", fontsize=tsize, fontweight="bold",
            color=TXT, zorder=3, linespacing=1.3)
    if body:
        ax.text(x + w / 2, y + h - 4.6, body, ha="center", va="top",
                fontsize=bsize, color=TXT, zorder=3, linespacing=1.45)


def arrow(ax, p0, p1):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle="-|>", mutation_scale=6, linewidth=1.0,
        color=ARROW, zorder=1, connectionstyle="arc3,rad=0",
        shrinkA=1.2, shrinkB=1.2))


def photo(ax, img_path, x0, y_top, w_units):
    """Place a photograph preserving its aspect ratio; returns (x1, y_bottom)."""
    img = Image.open(img_path)
    w_in = w_units / UX
    h_in = w_in * img.height / img.width
    h_units = h_in * UY
    y0 = y_top - h_units
    ax.imshow(img, extent=[x0, x0 + w_units, y0, y_top], aspect="auto",
              interpolation="antialiased", zorder=2)
    ax.add_patch(Rectangle((x0, y0), w_units, h_units, facecolor="none",
                           edgecolor="#9C9C9C", linewidth=0.5, zorder=3))
    return x0 + w_units, y0, h_units


def main():
    here = Path(__file__).resolve().parent
    fig, ax = plt.subplots(figsize=(W_IN, H_IN))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # ---- left photo column (from the pre-split Figure 1) ----
    x1, yb, _ = photo(ax, here / "photos" / "device_capillaroscopy.png",
                      2.5, 93, 15.5)
    ax.text((2.5 + x1) / 2, yb - 1.2, "Nailfold\ncapillaroscopy",
            ha="center", va="top", fontsize=6.0, color=TXT,
            linespacing=1.25, zorder=3)
    x1n, ybn, _ = photo(ax, here / "photos" / "nailfold_finger.png",
                        4.0, 44, 12.5)
    ax.text((4.0 + x1n) / 2, ybn - 1.2, "Nailfold",
            ha="center", va="top", fontsize=6.0, color=TXT, zorder=3)

    # ---- tier 1 - input and stabilisation ----
    box(ax, 24, 84, 74, 15, "Nailfold video (raw frames)",
        "520 frames per video at 30 frames/s, stabilised by SIFT\n"
        "keypoints and a RANSAC homography per frame",
        fc=GREY_F, ec=GREY_E)

    # ---- tier 2 - MD2 and frame-level detection ----
    box(ax, 24, 62, 36, 16, "MD2 enhancement",
        "AngioMD map $\\oplus$ per-frame IFM\nresponse $\\rightarrow$ frame $E_t$")
    box(ax, 62, 62, 36, 16, "Frame detection",
        "DPA-Refine: boxes $\\mathbf{b}_i^{(t)}$, scores\n"
        "$c_i^{(t)}$, centres $\\mathbf{z}_i^{(t)}$", fc=GREEN_F, ec=GREEN_E)

    # ---- tier 3 - ST branch and pass 1 ----
    box(ax, 24, 38, 36, 18, "ST branch",
        "along-vessel sampling $ST_v(k,t)$;\nstreak slope $a_{v,w}$ per window")
    box(ax, 62, 38, 36, 18, "Pass 1 \u00b7 vessel ROI",
        "detections with $c_i\\geq\\tau_{\\mathrm{roi}}=0.2$;\n"
        "activity heatmap and shape\nscreening $\\rightarrow$ vessel map $L(x,y)$",
        fc=CREAM_F, ec=CREAM_E)

    # ---- tier 4 - outputs ----
    box(ax, 24, 10, 36, 22, "Velocity $\\widehat u_v$",
        "$\\widehat u_{v,w}=|a_{v,w}|\\,\\delta_v\\rho_v f_{\\mathrm{cam}}$\n"
        "median over accepted windows")
    box(ax, 62, 10, 36, 22, "Pass 2 \u00b7 counting",
        "Norfair association with\n"
        "$c_i\\geq\\tau_{\\mathrm{count}}=0.45$; confirmed\n"
        "tracks per vessel $\\rightarrow$ count $N_v$",
        fc=CREAM_F, ec=CREAM_E)

    # ---- connections ----
    arrow(ax, (18.5, 76), (23.5, 87))     # device photo -> video box
    arrow(ax, (17.0, 38), (23.5, 85.5))   # nailfold ROI -> video box
    arrow(ax, (42, 84), (42, 78))         # input -> MD2
    arrow(ax, (60, 70), (62, 70))         # MD2 -> detection
    arrow(ax, (42, 62), (42, 56))         # MD2 -> ST branch
    arrow(ax, (80, 62), (80, 56))         # detection -> pass 1
    arrow(ax, (42, 38), (42, 32))         # ST -> velocity
    arrow(ax, (80, 38), (80, 32))         # pass 1 -> pass 2

    fig.subplots_adjust(0, 0, 1, 1)
    out = Path(__file__).resolve().parent
    fig.savefig(out / "Figure_1_pipeline_overview.pdf", dpi=600)
    fig.savefig(out / "Figure_1_pipeline_overview.png", dpi=600)
    print("written", out)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Draw the pipeline-overview figure for the B manuscript (CMPB version).

The canvas is sized to the actual text width of the elsarticle `review`
layout (344 pt = 4.78 in), so the 7 pt labels print at 7 pt instead of being
scaled down.  Four tiers: input/enhancement+detection, pass 1 and the ST
branch, then pass 2 and the velocity output.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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


def box(ax, x, y, w, h, title, body="", fc=BLUE_F, ec=BLUE_E, tsize=7.1,
        bsize=6.2):
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


def main():
    fig, ax = plt.subplots(figsize=(4.78, 3.30))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # tier 1 - input and stabilisation
    box(ax, 2, 84, 96, 15, "Nailfold video (raw frames)",
        "520 frames per video at 30 frames/s, stabilised by SIFT\n"
        "keypoints and a RANSAC homography per frame",
        fc=GREY_F, ec=GREY_E)

    # tier 2 - MD2 and frame-level detection
    box(ax, 2, 62, 46, 16, "MD2 enhancement",
        "AngioMD map $\\oplus$ per-frame IFM\nresponse $\\rightarrow$ frame $E_t$")
    box(ax, 52, 62, 46, 16, "Frame detection",
        "DPA-Refine: boxes $\\mathbf{b}_i^{(t)}$, scores\n"
        "$c_i^{(t)}$, centres $\\mathbf{z}_i^{(t)}$", fc=GREEN_F, ec=GREEN_E)

    # tier 3 - ST branch and pass 1
    box(ax, 2, 38, 46, 18, "ST branch",
        "along-vessel sampling $ST_v(k,t)$;\nstreak slope $a_{v,w}$ per window")
    box(ax, 52, 38, 46, 18, "Pass 1 \u00b7 vessel ROI",
        "detections with $c_i\\geq\\tau_{\\mathrm{roi}}=0.2$;\n"
        "activity heatmap and shape screening\n$\\rightarrow$ vessel map $L(x,y)$",
        fc=CREAM_F, ec=CREAM_E)

    # tier 4 - outputs
    box(ax, 2, 10, 46, 22, "Velocity $\\widehat u_v$",
        "$\\widehat u_{v,w}=|a_{v,w}|\\,\\delta_v\\rho_v f_{\\mathrm{cam}}$\n"
        "median over accepted windows")
    box(ax, 52, 10, 46, 22, "Pass 2 \u00b7 counting",
        "Norfair association with\n"
        "$c_i\\geq\\tau_{\\mathrm{count}}=0.45$; confirmed\n"
        "tracks per vessel $\\rightarrow$ count $N_v$",
        fc=CREAM_F, ec=CREAM_E)

    # connections
    arrow(ax, (25, 84), (25, 78))    # input -> MD2
    arrow(ax, (48, 70), (52, 70))    # MD2 -> detection
    arrow(ax, (25, 62), (25, 56))    # MD2 -> ST branch
    arrow(ax, (75, 62), (75, 56))    # detection -> pass 1
    arrow(ax, (25, 38), (25, 32))    # ST -> velocity
    arrow(ax, (75, 38), (75, 32))    # pass 1 -> pass 2

    fig.subplots_adjust(0, 0, 1, 1)
    out = Path(__file__).resolve().parent
    fig.savefig(out / "Figure_1_pipeline_overview.pdf", dpi=600)
    fig.savefig(out / "Figure_1_pipeline_overview.png", dpi=600)
    print("written", out)


if __name__ == "__main__":
    main()

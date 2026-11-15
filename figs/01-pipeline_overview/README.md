# Figure 1: Quantification pipeline overview

Manuscript figure: **Fig. 1** (`fig:pipeline`).

`code/make_pipeline_overview.py` draws the four-tier overview with matplotlib and writes `fig/pipeline_overview.pdf` and `.png` at 600 dpi. The script is self-contained and reads no external data.

The figure summarises the two-pass quantification pipeline: pass 1 accumulates frame-level detections into a vessel label map, pass 2 associates detections into trajectories and counts confirmed identifiers per vessel, and a separate branch samples spatiotemporal maps for apparent-velocity estimation. The frame-level detector itself is reported separately and is not described in this archive.

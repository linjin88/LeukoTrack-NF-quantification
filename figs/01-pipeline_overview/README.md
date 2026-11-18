# Figure 1: Quantification pipeline overview

Manuscript figure: **Fig. 1** (`fig:pipeline`).

`fig/pipeline_overview.pdf` and `.png` reproduce the original composite overview figure carried over from the pre-split system figure. It shows, from left to right: the nailfold capillaroscopy device and an imaged finger with the imaged nailfold region marked; the raw nailfold video and its MD2-enhanced counterpart; the dual-path attention mechanism inherited from the companion detection study; the adaptive ROI stage with vessel masks and LeukoTrack-NF counting; and the leukocyte-count / apparent-velocity outputs.

Frame-level detection and MD2 enhancement are reported in the companion detection paper. This manuscript covers the vessel-level quantification and its measurement error; the figure caption states the reference comparisons (five-rater consensus for counts, repeated manual spatiotemporal measurements for velocity).

`code/make_pipeline_overview.py` is retained as an earlier redraw of this overview and is not the source of the figure distributed here.

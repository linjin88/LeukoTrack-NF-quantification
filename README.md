# LeukoTrack-NF — figure archive for the quantification study

Rendered figures and figure-rendering code for a study of **vessel-level
leukocyte event counting and apparent-velocity estimation** in nailfold
capillaroscopy (NFC) videos:

> **A reproducible video pipeline for vessel-level leukocyte event counting
> and apparent-velocity estimation in nailfold capillaroscopy**

This archive contains the six figures of that quantification study and the
scripts that produced them. The frame-level detector and its evaluation are
reported separately; this archive contains no detector-architecture,
enhancement, UIS, training-dynamics, feature-response or detection-comparison
materials, no participant-level recordings, and no annotation, prediction or
evaluation data.

## Figure ↔ package mapping

The `NN-` directory indices are historical package identifiers and are **not**
manuscript figure numbers. Manuscript numbering follows order of first
appearance.

| Manuscript figure | Label in the source | Package directory | Content |
|---|---|---|---|
| Fig. 1 | `fig:pipeline` | `figs/01-pipeline_overview` | Quantification pipeline overview |
| Fig. 2 | `fig:roi_generation` | `figs/04-adaptive_ROI` | Detection-guided vessel ROI construction |
| Fig. 3 | `fig:st_map` | `figs/05-ST_map_workflow` | ST-map analysis of apparent along-vessel velocity |
| Fig. 4 | `fig:dpa_normalized_profile` | `figs/09-DPA_performance_profile` | Descriptive normalized performance profiles |
| Fig. 5 | `fig:dpa_refine_counting_consistency` | `figs/08-counting_consistency` | Counts against the mean manual reference |
| Fig. 6 | `fig:st_velocity_agreement` | `figs/10-ST_manual_agreement` | Automated versus manual ST velocity agreement |

Each package contains:

- `fig/` — the rendered figure used by the manuscript (PDF; a PNG render is
  kept alongside it where one exists);
- `code/` — the plotting/processing code that renders or supports the figure;
- `README.md` — package-specific notes.

All six figures are main-text figures of the quantification study; this archive
contains no supplementary figure.

## Method summary

The figures accompany a two-pass pipeline that converts frame-level detections
into vessel-level event counts and apparent-velocity estimates, together with
an explicit error budget. Pass 1 accumulates detections over the whole
recording into a detection-guided vessel label map; pass 2 associates
detections into trajectories and counts confirmed identifiers per vessel. A
separate branch samples spatiotemporal (ST) maps along vessel centerlines to
estimate apparent velocity, with acceptance criteria for analysis windows.
Measurement error is characterized against a five-rater manual reference and
an independent manual ST-based velocity reference.

This archive documents the figures only. The novelty of the frame-level
detector, its architecture and its frame-level evaluation belong to the
separate detection study and are not claimed here.

## Regenerating the figures

The rendered PDFs are the figures of record; the scripts are published as the
code that produced them. Some plotting scripts read inputs from a controlled
`data/` directory that is not redistributed here; those commands therefore
document how each figure was made and do not run against this archive alone.
`figs/01-pipeline_overview/code/make_pipeline_overview.py` is self-contained and
can be run directly from its package directory.

No frame-selection tokens or links to the original dataset filenames are
included in this public archive.

## Scope and data boundary

This public archive contains **only rendered figures and figure-rendering
code**. It does not contain:

- original human-subject videos or raw image collections;
- annotation files, prediction files, evaluation outputs, per-ROI counts or
  other analysis inputs;
- frame identifiers, participant codes, batch-to-video mappings, consent
  records, real names, hospital identifiers or identity-linkage keys;
- detector-architecture, enhancement, UIS or frame-level detection materials;
- model checkpoints or superseded figure variants.

The displayed imagery is de-identified and was derived from the 2026
acquisition batches under approval no. GUET-EC-2026-001 (Guilin University of
Electronic Technology) and no. 2026041601 (People's Hospital of Nanhai
Economic Development Zone).

## Data and code availability

The executable training code, model checkpoints and the privacy-compatible
derived materials are withheld from public release because the underlying
recordings were acquired from human participants under institutional ethics
approvals and written informed consent. They are deposited in the project
repository upon acceptance of the manuscript. De-identified participant-level
videos are available from the first author upon reasonable request, subject to
approval by the relevant ethics committees; consent records and batch-to-video
mappings remain under institutional control and are never released.

## Interpretation boundary

Having a rendered figure and a plotting script does not by itself establish
end-to-end reproducibility. A figure is complete only when the exact input
data, processing parameters, source code, and, where applicable, model
checkpoint can be identified and retained.

## Licensing

Two licences apply, split by material type:

- **Code** — every script, configuration and diagram source in this archive is
  released under the [MIT License](LICENSE).
- **Figures** — every rendered file under `figs/**/fig/` (`.pdf`, `.png`) is
  released under [CC BY 4.0](LICENSE-figures); reuse should credit the
  manuscript named above.

Neither licence extends to the underlying human-subject recordings or the
de-identified derived data, which remain governed by the ethics approval and
informed-consent terms described in the manuscript.

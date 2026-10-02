# Mental Health Prediction

This repository currently contains one notebook, `Mental Health Prediction.ipynb`. It demonstrates preprocessing survey fields and fitting several classifiers for the notebook's `treatment` target.

## Data prerequisite

The notebook reads `data.csv` from the current working directory. **That file is not included in this repository**, so the notebook cannot be run end to end from a fresh clone and its reported results cannot be independently reproduced from the repository alone. Obtain and review the data source and its license yourself; place a compatible `data.csv` beside the notebook, and do not commit private or sensitive respondent data. The notebook expects fields such as `Age`, `Country`, `state`, `Timestamp`, `comments`, `Gender`, `self_employed`, `work_interfere`, and `treatment`; verify the full schema against the notebook before running it.

## Run locally

Use Python with Jupyter and the libraries imported by the notebook (`numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, and `xgboost`). Install those packages in an isolated environment using versions appropriate for your Python platform. From the repository root, open `Mental Health Prediction.ipynb` in Jupyter and run cells in order after supplying the data file. The repository does not currently pin dependency versions.

Run the repository's data-independent notebook checks with:

```sh
python -m unittest discover -s tests
```

These checks validate notebook structure, cached-output hygiene, and Python syntax only. They do **not** train or validate a model.

## Limitations and privacy

The notebook's target is the survey's `treatment` field, not a clinical diagnosis. Its predictions must not be used to diagnose, screen, or make decisions about individuals. The input dataset is absent, and no model-performance claim is made here. Notebook execution outputs are intentionally cleared to avoid distributing cached respondent-level data, predictions, plots, or stale metrics; rerunning it may recreate sensitive outputs locally.

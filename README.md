# Disclaimer
This is a repository containing the materials for the talk given at PyData Paris, Oct. 1st 2025, by Alix TIRAN-CAPPELLO

The goal is to present the open-souce package `pelage`:  https://alixtc.github.io/pelage/ 

This live coding presentation is based on the dataset `2023_Cars_Raw.csv` available here:
https://sdi.eea.europa.eu/data/ad652e2b-c4a1-4344-a536-dee5a9fae52d

The dataset must be placed in the path `data/2023_Cars_Raw.csv` from the root of this repository, and has not been included because of its size (1.5GB)

More detailed information about the dataset can be found at the following links:
- [General information and context](https://climate.ec.europa.eu/news-your-voice/news/collecting-real-world-data-co2-emissions-and-fuel-consumption-new-cars-and-vans-2021-03-05_en)
- [Metadata](https://sdi.eea.europa.eu/catalogue/datahub/api/records/ad652e2b-c4a1-4344-a536-dee5a9fae52d/formatters/xsl-view?output=pdf&language=eng&approved=true)

# Installation

Once the data has been downloaded, the project can be installed with:

```bash
uv sync --all-groups
```

# Content
There are 4 main components to this repository:
- The notebooks which contains the core of the live coding logic (one should be completely filled, and the other contains only the skeleton of the presentation).
- The folder `tests` which contains performance benchmarks between the different implementations presented in the notebooks. It can be run with:
  ```bash
  pytest --benchmark-min-rounds=10 --benchmark-time-unit=s
  ```
- The `load_data.py` which contains basic preprocessing and types definition for `data/2023_Cars_Raw.csv`
- The combination of `notifier.py` and `vscode-extension`, which are used to trigger notifications in VS Code. It has been hacked together for the sole purpose of this presentation. It is egregious, should be drenched in gasoline and set on fire:

  **This code should never be run anywhere, you have been warned!**

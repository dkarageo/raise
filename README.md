# RAISE
Tools for downloading the RAISE dataset.

## Install Dependencies
```
python -m venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```python download.py --dataset_csv <path_to_dataset_csv> --output_dir <path_to_output_dir>```

where:
- `dataset_csv`: A csv of RAISE dataset obtained from its [official website](http://loki.disi.unitn.it/RAISE/download.html).
- `output_dir`: Path to an output directory.

## License

The project is licensed under GNU GPLv3.
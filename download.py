"""Script for downloading the RAISE dataset."""

from pathlib import Path
from typing import Any
import urllib.request

import click
from tqdm import tqdm

import utils


@click.command()
@click.option("--dataset_csv", required=True,
              type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--output_dir", required=True,
              type=click.Path(file_okay=False, path_type=Path))
@click.option("--url_column", type=str, default="TIFF")
@click.option("--file_column", type=str, default="File")
@click.option("--csv_delimiter", type=str, default=",")
def main(
    dataset_csv: Path,
    output_dir: Path,
    url_column: str,
    file_column: str,
    csv_delimiter: str,
) -> None:
    entries: list[dict[str, Any]] = utils.read_csv_file(dataset_csv, delimiter=csv_delimiter)
    output_dir.mkdir(exist_ok=True, parents=True)
    if url_column == "TIFF":
        suffix: str = ".tif"
    elif url_column == "NEF":
        suffix = ".nef"
    else:
        raise RuntimeError(f"Unsupported url_column: {url_column}")
    for e in tqdm(entries, desc="Downloading RAISE dataset", unit="image"):
        url: str = e[url_column]
        output_file: Path = output_dir / f"{e[file_column]}{suffix}"
        with urllib.request.urlopen(url) as response, open(output_file, "wb") as out_file:
            data = response.read()
            out_file.write(data)

if __name__ == "__main__":
    main()

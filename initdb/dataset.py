from zipfile import ZipFile
import os
import requests

from utils import eprint


DATASET_URL="https://codechallengestracc.blob.core.windows.net/code-challenge/dublin-dataset.zip"
DATASET_DIR='/dataset'
TMP_DIR='/tmp'


def _download_dataset(url):
    filename = url.split('/')[-1]
    tmp_filepath = os.path.join(TMP_DIR, filename)
    with requests.get(url, stream=True) as r:
        with open(tmp_filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    return tmp_filepath


def _decompress_dataset(filepath, dest_dir):
    compressed_file = ZipFile(filepath)
    compressed_file.extractall(dest_dir)
    os.remove(filepath)


def ensure():
    dataset_present = bool(os.listdir(DATASET_DIR))
    print(os.listdir(DATASET_DIR))

    if dataset_present:
        return

    eprint('no dataset found. downloading dataset...')
    zip_filepath = _download_dataset(DATASET_URL)
    eprint('decompressing dataset...')
    _decompress_dataset(zip_filepath, DATASET_DIR)

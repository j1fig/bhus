import csv
import os
import subprocess

from models import VehicleState
from utils import eprint
import db
import dataset


SAMPLE_FILENAME = 'siri.20121106.csv'

CSV_INDEX = {
    0: 'timestamp',
    6: 'operator',
    8: 'longitude',
    9: 'latitude',
    12: 'vehicle_id',
    14: 'at_stop',
}
_CSV_CHUNK_SIZE = 10000


def one():
    filepath = os.path.join(dataset.DATASET_DIR, SAMPLE_FILENAME)
    from_csv(filepath)


def all():
    files = os.listdir(DATASET_DIR)
    for f in files:
    	filepath = os.path.join(dataset.DATASET_DIR, f) 
    	from_csv(filepath)


def from_csv(filepath):
    if _is_loaded(filepath):
        return

    eprint(f'dataset {filepath} not loaded. loading dataset...')
    # deleting if counts don't match is inefficient but makes this idempotent.
    session = db.make_session()
    session.query(VehicleState).filter_by(source=filepath).delete()
    session.commit()

    file_lines = _wc_l(filepath)
    total_chunks = file_lines // _CSV_CHUNK_SIZE
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for chunk, rows in enumerate(_csv_chunk(reader, chunk_size=_CSV_CHUNK_SIZE)):
            eprint(f'loading chunk [{chunk: >4} / {total_chunks}]')
            states = []
            for row in rows:
                vehicle_state = {
                    CSV_INDEX[index]: v
                    for index, v in enumerate(row)
                    if index in CSV_INDEX
                }
                vehicle_state['at_stop'] = _coerce_at_stop(vehicle_state['at_stop'])
                vehicle_state['source'] = filepath
                states.append(vehicle_state)
            session.bulk_insert_mappings(VehicleState, states)
            session.commit()


def _coerce_at_stop(at_stop):
    return True if at_stop == '1' else False


def _csv_chunk(reader, chunk_size):
    """
    A generator to stream rows from large CSV files.
    """
    rows = []
    for row in reader:
        rows.append(row)
        if len(rows) >= chunk_size:
            yield rows
            rows = []
    if rows:
        yield rows


def _wc_l(f):
    """
    Counts the number of lines in the file.

    For large files, Unix's wc has superior performance.
    """
    r = subprocess.run(['wc', '-l', f], capture_output=True)
    return int(r.stdout.split()[0])


def _is_loaded(filename):
    expected_rows = _wc_l(filename)
    session = db.make_session()
    rows = session.query(VehicleState).filter_by(source=filename).count()
    return rows == expected_rows

from pathlib import Path
import pytest
import spudtr.epf as epf
import spudtr.fake_epochs_data as fake_data
import numpy as np

import pdb

TEST_DATA_DIR = Path(__file__).parent / "data"


@pytest.mark.parametrize(
    "_f,h5_group",
    [
        ["sub000p3.epochs.h5", "p3"],
        ["sub000p5.epochs.h5", "p5"],
        ["sub000wr.epochs.h5", "wr"],
    ],
)
def test_hdf_read_epochs(_f, h5_group):
    epochs_df = epf._hdf_read_epochs(TEST_DATA_DIR / _f, h5_group)


# test one file
def test_epochs_QC():
    _f1, h5_group1 = "sub000wr.epochs.h5", "wr"
    epochs_df = epf._hdf_read_epochs(TEST_DATA_DIR / _f1, h5_group1)
    eeg_streams = ["MiPf", "MiCe", "MiPa", "MiOc"]
    epf._epochs_QC(epochs_df, eeg_streams)


def test_center_on():
    _f1, h5_group1 = "sub000wr.epochs.h5", "wr"
    epochs_df = epf._hdf_read_epochs(TEST_DATA_DIR / _f1, h5_group1)
    eeg_streams = ["MiPf", "MiCe", "MiPa", "MiOc"]
    start, stop = -50, 300
    epochs_df_centeron = epf.center_eeg(epochs_df, eeg_streams, start, stop)

    # after center on, the mean inside interval should be zero
    qstr = f"{start} <= Time and Time < {stop}"
    after_mean = epochs_df_centeron.groupby(["Epoch_idx"]).apply(
        lambda x: x.query(qstr)[eeg_streams].mean(axis=0)
    )

    # a is afer_mean numpy array, and b is zero array same size as a

    a = after_mean.values
    b = np.zeros(after_mean.shape)

    # np.isclose(a,b)   #all false
    # np.isclose(a,b,atol=1e-05)  #most true, but some false

    # The absolute tolerance parameter: atol=1e-04
    TorF = np.isclose(a, b, atol=1e-04)
    assert sum(sum(TorF)) == TorF.shape[0] * TorF.shape[1]


"""
    # fake some data
    # check center_on function with fake data
    import numpy as np
    import warnings
    randval = np.random.random()
    if randval > 0.5:
        pdb.set_trace()
        raise ValueError(f'randval > 0.5 {randval}')
    else:
        warnings.warn(f'randval <= 0.5 {randval}')
"""

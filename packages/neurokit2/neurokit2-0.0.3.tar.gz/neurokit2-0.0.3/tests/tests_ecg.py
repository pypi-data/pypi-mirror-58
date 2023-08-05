import numpy as np
import pandas as pd
import neurokit2 as nk

import scipy.stats

# =============================================================================
# ECG
# =============================================================================


def test_ecg_simulate():

    ecg1 = nk.ecg_simulate(duration=20, length=5000)
    assert len(ecg1) == 5000

    ecg2 = nk.ecg_simulate(duration=20, length=5000, heart_rate=500)
#    pd.DataFrame({"ECG1":ecg1, "ECG2": ecg2}).plot()
#    pd.DataFrame({"ECG1":ecg1, "ECG2": ecg2}).hist()
    assert len(nk.signal_findpeaks(ecg1)[0]) < len(nk.signal_findpeaks(ecg2)[0])

"""Scientific checks for the committed multi-sector robustness analysis."""

from pathlib import Path
import hashlib

import numpy as np
import analyze_multisector as multi

EXPECTED_SHA256 = {
    "tess2021232031932-s0042-0000000301289516-0213-s_lc.fits": "9708ef48f7e7d41fe4c56fbe7c82c5b44d816fd64a1ea1d55e772981202597d6",
    "tess2023263165758-s0070-0000000301289516-0265-s_lc.fits": "fdb998982d3094d58400ffb7c26665bba38ae4c4078f5c5643905d42fc405fa0",
    "tess2025127075000-s0092-0000000301289516-0289-s_lc.fits": "9753d4e867c9311112ad962beb1934c186fe8e247e1689bd52557956ffc10efa",
}


def test_all_committed_spoc_files_are_accounted_for():
    expected = list(multi.base.DATA_DIR.glob("tess*_lc.fits"))
    summary = multi.main()
    assert len(summary["sectors"]) + len(summary["skipped"]) == len(expected) == 3
    assert [item["sector"] for item in summary["sectors"]] == [42, 70, 92]
    if summary["supported"]:
        assert np.isfinite(summary["combined_depth_ppm"])
        assert summary["combined_error_ppm"] > 0
    else:
        assert np.isnan(summary["combined_depth_ppm"])
    for item in summary["sectors"]:
        assert item["result"]["n_in_transit"] >= 5
        assert item["result"]["n_out_of_transit"] >= 20
        assert item["beta"] >= 1
        assert item["robust_error_ppm"] >= item["result"]["depth_error_ppm"] - 1e-9
    assert len(summary["supported"]) == 3
    assert summary["q_dof"] == 2
    assert summary["q_p"] > 0.05


def test_spoc_source_files_match_manifested_checksums():
    for filename, expected in EXPECTED_SHA256.items():
        observed = hashlib.sha256((multi.base.DATA_DIR / filename).read_bytes()).hexdigest()
        assert observed == expected


def test_reproducible_outputs_are_nonempty():
    multi.main()
    for path in (multi.STATS_FILE, multi.TRANSITS_FIGURE,
                 multi.CONSISTENCY_FIGURE, multi.NOISE_FIGURE):
        assert Path(path).is_file()
        assert Path(path).stat().st_size > 100

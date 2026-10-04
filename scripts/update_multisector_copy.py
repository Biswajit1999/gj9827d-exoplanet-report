"""Synchronize the marked website multi-sector section from generated results."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "index.html"
text = path.read_text(encoding="utf-8")
start_marker = "<!-- MULTISECTOR-UPGRADE-START -->"
end_marker = "<!-- MULTISECTOR-UPGRADE-END -->"
section = """<section class="reveal"><h2>Multi-sector robustness and noise</h2><div class="grid"><div class="card"><span>Supported combined depth</span><strong>536.5 ± 69.4 ppm</strong></div><div class="card"><span>Supported / fitted sectors</span><strong>3 / 3</strong></div><div class="card"><span>Depth consistency</span><strong>Q = 1.92; p = 0.384</strong></div><div class="card"><span>Residual beta range</span><strong>1.01–3.16</strong></div></div><p>The archive prediction was timing-adjusted independently in Sectors 42, 70, and 92; all three meet ΔBIC ≥ 10. Formal errors were inflated by sqrt(max(reduced χ², 1)) and the residual time-averaging beta factor. The inverse-variance depth is 536.5 ± 69.4 ppm. Cochran's Q does not detect excess depth dispersion after that inflation (Q = 1.92 for 2 dof; p = 0.384), but three sectors provide limited power and Sector 70's beta = 3.16 flags substantial correlated residual noise. This is a robustness diagnostic, not a global physical transit retrieval.</p><figure class="figure reveal"><img src="figures/gj9827d_multisector_transits.png" alt="Independent sector transit fits for GJ 9827 d"><figcaption>Independent fixed-protocol fits to all three committed public TESS SPOC 2-minute light curves.</figcaption></figure><figure class="figure reveal"><img src="figures/gj9827d_depth_consistency.png" alt="Sector depth consistency for GJ 9827 d"><figcaption>Depth comparison after per-sector scatter and time-correlation inflation.</figcaption></figure><figure class="figure reveal"><img src="figures/gj9827d_noise_diagnostics.png" alt="Residual RMS time-averaging diagnostic for GJ 9827 d"><figcaption>Residual time-averaging curves used to estimate the beta inflation factors.</figcaption></figure></section>"""
prefix, remainder = text.split(start_marker, 1)
_, suffix = remainder.split(end_marker, 1)
path.write_text(prefix + start_marker + section + end_marker + suffix, encoding="utf-8")
text = path.read_text(encoding="utf-8")
text = text.replace(
    "The observed photometry is the public MAST file <code>tess2021232031932-s0042-0000000301289516-0213-s_lc.fits</code>, TESS Sector 42,",
    "The observed photometry comprises three public MAST SPOC 2-minute files from TESS Sectors 42, 70, and 92,",
).replace("It is stored unmodified.", "They are stored unmodified.").replace(
    "; Sector 42 used here.</li>", "; Sectors 42, 70, and 92 used here.</li>"
)
path.write_text(text, encoding="utf-8")

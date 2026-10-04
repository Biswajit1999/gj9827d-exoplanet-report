# Data sources

## TESS light curve

- File: `tess2021232031932-s0042-0000000301289516-0213-s_lc.fits`
- Archive: Mikulski Archive for Space Telescopes (MAST), TESS SPOC light-curve product
- TESS sector: 42
- TIC target ID: 301289516
- MAST observation ID: 63406497
- MAST data URI: `mast:TESS/product/tess2021232031932-s0042-0000000301289516-0213-s_lc.fits`
- Exact download URL: <https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:TESS%2Fproduct%2Ftess2021232031932-s0042-0000000301289516-0213-s_lc.fits>
- Collection DOI: [10.17909/t9-nmc8-f686](https://doi.org/10.17909/t9-nmc8-f686) (TESS 2-minute light curves, all sectors; Sectors 42, 70, and 92 used here)
- Retrieved: 2026-08-15
- SHA-256: `9708ef48f7e7d41fe4c56fbe7c82c5b44d816fd64a1ea1d55e772981202597d6`

The FITS file is stored unmodified. The analysis reads `TIME`, `PDCSAP_FLUX`,
`PDCSAP_FLUX_ERR`, and `QUALITY`. PDCSAP flux is the SPOC light curve with common
instrumental trends removed and aperture/crowding corrections applied; this does
not make it free of residual stellar or instrumental systematics.

## System parameters

- File: `system_parameters.csv`
- Service: NASA Exoplanet Archive TAP, `pscomppars` table
- Exact query: <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name%2Chostname%2Cra%2Cdec%2Cpl_orbper%2Cpl_tranmid%2Cpl_trandur%2Cpl_rade%2Cpl_bmasse%2Cpl_eqt%2Cpl_orbsmax%2Csy_dist%2Csy_tmag%2Cst_teff%2Cst_rad%2Cst_mass%2Cdisc_year%2Cdiscoverymethod%2Cdisc_refname%2Cdisc_pubdate%2Cdisc_facility+from+pscomppars+where+pl_name%3D%27GJ+9827+d%27&format=csv>
- Retrieved: 2026-08-15

The saved row is the input actually used by `scripts/analyze_transit.py`; the
analysis does not query a changing live service at run time.


## Additional TESS sectors for robustness analysis

All are unmodified standard-cadence SPOC light curves from the same [MAST TESS collection](https://doi.org/10.17909/t9-nmc8-f686).
Sector 42 was retrieved 2026-08-15; Sectors 70 and 92 were retrieved 2026-10-04 after a complete target-cone product query.

- Sector 42: `tess2021232031932-s0042-0000000301289516-0213-s_lc.fits` (1,863,360 bytes)
  - MAST URI: `mast:TESS/product/tess2021232031932-s0042-0000000301289516-0213-s_lc.fits`
  - SHA-256: `9708ef48f7e7d41fe4c56fbe7c82c5b44d816fd64a1ea1d55e772981202597d6`
- Sector 70: `tess2023263165758-s0070-0000000301289516-0265-s_lc.fits` (1,863,360 bytes)
  - MAST URI: `mast:TESS/product/tess2023263165758-s0070-0000000301289516-0265-s_lc.fits`
  - SHA-256: `fdb998982d3094d58400ffb7c26665bba38ae4c4078f5c5643905d42fc405fa0`
- Sector 92: `tess2025127075000-s0092-0000000301289516-0289-s_lc.fits` (1,949,760 bytes)
  - MAST URI: `mast:TESS/product/tess2025127075000-s0092-0000000301289516-0289-s_lc.fits`
  - SHA-256: `9753d4e867c9311112ad962beb1934c186fe8e247e1689bd52557956ffc10efa`

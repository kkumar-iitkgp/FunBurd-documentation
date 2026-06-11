# FunBurd documentation

This repository contains the public documentation site and lightweight tutorial for **FunBurd**: a functional burden framework for studying gene-dosage sensitivity across human traits.

This documentation accompanies our study:

> **Kazem S.\*, Kumar K.\*, et al. _Determinants of functional burden pleiotropy and gene dosage responses across human traits._**  
> \* Equal contribution.

The site provides:

- a conceptual overview of the FunBurd framework;
- explanations of the core model, assumptions, and interpretation;
- summaries of robustness checks, replication, and biological insights;
- advanced-method explanations for P-Jaccard, normative constraint modeling, CNV-burden correlations, variance explained, and BMI mediation;
- a lightweight tutorial using toy data and the shared FunBurd notebook style.

## Rendered documentation

The hosted documentation is intended to be available at:

- https://funburd.readthedocs.io/

## Primary analysis code

Our manuscript-analysis and figure-generation workflows are available from the primary FunBurd repository:

- https://github.com/SayehKazem/FunBurd

## Local build

Place the approved image assets in:

```text
docs/_static/figures/
```

Then build locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r docs/requirements.txt
python -m sphinx -b html docs docs/_build/html
```

Open:

```text
docs/_build/html/index.html
```

For a stricter check:

```bash
python -m sphinx -b html -W --keep-going docs docs/_build/html
python -m sphinx -b linkcheck docs docs/_build/linkcheck
```

## License notice

See [`LICENSE_NOTICE.md`](LICENSE_NOTICE.md). The final repository-level license should be added after approval by the relevant copyright holders and institutional office.

# Can I apply FunBurd to my own data?

FunBurd can be adapted to a new cohort when the required inputs are available and the analyst is prepared to validate cohort-specific choices. We provide a tested implementation and a lightweight notebook example, not a universal plug-and-play package.

## Minimum inputs

| Input | Minimum content | Why it is needed |
|---|---|---|
| Participant-level CNV calls | Participant ID, chromosome, start, stop, deletion or duplication status, and QC status | Defines the structural variants to aggregate |
| CNV-to-gene mapping | Gene identifiers linked to each CNV and a rule for overlap | Determines which genes contribute to burden |
| Functional gene sets | Gene identifiers for each tissue, cell type, or other predefined function | Defines the biological unit of analysis |
| Phenotypes | Trait value and participant ID | Outcome of the association model |
| Covariates | Age, sex, ancestry principal components, and any cohort-specific covariates | Reduces confounding |

## Publication-aligned default choices

Our primary analysis used:

- deletions and duplications analyzed separately;
- CNVs of at least 50 kb;
- full-gene encompassment for at least one protein-coding gene;
- expression-defined tissue and cell-type gene sets;
- inverse-rank normal transformation for continuous traits;
- age, sex, and ten ancestry principal components as covariates;
- an inside-set burden term ($x_1$) and an outside-set burden term ($x_2$).

These defaults are a defensible starting point because they match our validated primary analysis.

## What can be changed?

You can extend FunBurd, but each change alters the estimand or its reliability.

| Extension | Feasible in principle? | What requires validation? |
|---|---|---|
| WGS-based CNV calls | Yes | QC, CNV-size distribution, recurrence, gene-overlap rules, and compatibility with the published burden definition |
| Partial-gene overlaps | Yes | Threshold choice and interpretation; we focused on fully encompassed genes |
| Different CNV-size thresholds | Yes | Sensitivity of burden distributions and association profiles |
| Alternative gene-set resources | Yes | Set sizes, overlap structure, biological interpretation, and multiple-testing burden |
| Pathway or GO sets | Possible but not directly comparable | Highly variable set sizes and power differences |
| Different ancestry groups | Yes | Transportability, CNV frequency, calling performance, and covariate structure |
| Clinical cohorts | Yes | Ascertainment, phenotype harmonization, CNV burden distribution, and model calibration |

```{admonition} Important boundary
:class: warning
We do not claim that a model validated on our call set is automatically calibrated for every CNV-calling platform, cohort, ancestry group, or gene-set collection. Re-run descriptive and sensitivity analyses when the inputs change.
```

## Recommended adoption workflow

1. Inspect CNV size, gene-content, and recurrence distributions.
2. Define a transparent CNV-to-gene overlap rule.
3. Inspect gene-set sizes and pairwise overlap.
4. Calculate $x_1$ and $x_2$ distributions for representative sets.
5. Fit deletion and duplication models separately.
6. Validate carrier-count balance and sensitivity to large or recurrent CNVs.
7. Apply appropriate multiple-testing correction.
8. Use overlap-aware procedures for downstream profile correlations.
9. Report deviations from our study-aligned defaults explicitly.

## What the current toy example covers

The [lightweight notebook walkthrough](../tutorial/lightweight_notebook.md) demonstrates the core association workflow on toy files. It is intentionally small and does not reproduce our full-scale analyses.

## Related resources

- [Data inputs and processing](../concepts/data_inputs.md)
- [Input and output reference](../tutorial/input_output_reference.md)
- [Current code state](code_status.md)
- [Assumptions and limitations](../reference/assumptions_limitations.md)

## Next

Continue to [Try the lightweight notebook](../tutorial/lightweight_notebook.md).

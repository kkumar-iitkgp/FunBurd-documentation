# What is new in this work?

We combine established statistical tools with several framework-level contributions. This page distinguishes our core additions from supporting analyses.

## Core contributions

| Contribution | What it adds | Where to read more |
|---|---|---|
| **FunBurd association model** | Aggregates genome-wide coding CNVs by biological function while adjusting for disrupted genes outside the target set | [FunBurd model](../concepts/funburd_model.md) |
| **Functional burden pleiotropy** | Extends pleiotropy from the gene or variant level to the number of traits associated with burden in a functional gene set | [Pleiotropy and constraint](../evidence/pleiotropy_constraint.md) |
| **P-Jaccard null maps** | Tests selected gene-set-profile correlations against overlap-aware null maps rather than treating gene sets as independent | [P-Jaccard](../advanced_methods/p_jaccard.md) |
| **Normative constraint modeling** | Asks whether a gene set is more pleiotropic than expected for its level of genetic constraint | [Normative constraint modeling](../advanced_methods/normative_constraint_modeling.md) |
| **CNV-burden correlations** | Extends cross-trait burden-correlation logic to deletion and duplication profiles across functional gene sets | [CNV-burden correlations](../advanced_methods/cnv_burden_correlations.md) |
| **Gene-dosage response classification** | Separates deletion-specific, duplication-specific, monotonic, and non-monotonic patterns across traits and functions | [Gene-dosage responses](../evidence/gene_dosage_responses.md) |

## Supporting extensions

We also use established or adapted analyses to strengthen interpretation:

- replication in the All of Us cohort;
- comparison with aggregated predicted loss-of-function burden;
- comparison with common-variant S-LDSC enrichments;
- sex-stratified analyses;
- BMI mediation decomposition for selected correlated trait pairs;
- extensive sensitivity analyses.

## Why the distinctions matter

Not every analysis should be described as a new method. Our primary novelty lies in the framework: how coding CNVs are aggregated, how functional associations are interpreted, how overlap-aware inference is handled, and how the resulting profiles are used to study pleiotropy and dosage responses.

```{admonition} Citation principle
:class: tip
When reusing a specific extension, cite our accompanying publication and the relevant prior method where appropriate. For example, S-LDSC and mediation analysis are established approaches applied here within the FunBurd framework.
```

## Next

Continue to [Why functional burden?](../concepts/why_functional_burden.md) for the biological and statistical motivation.

# FunBurd

```{image} _static/figures/funburd_logo.png
:alt: FunBurd logo
:width: 360px
:align: center
```

**Functional Burden analysis for studying gene-dosage sensitivity across human traits**

FunBurd is a genome-wide framework for studying how rare coding copy-number variants (CNVs) influence complex traits. Instead of limiting analysis to a small number of recurrent loci, FunBurd aggregates deletions and duplications according to the biological functions of the genes they disrupt.

We applied FunBurd to 43 traits in approximately 500,000 UK Biobank participants using 172 tissue- or cell-type gene sets. We examined replication in All of Us, concordance with predicted loss-of-function variants, comparisons with common variants, functional burden pleiotropy, genetic constraint, cross-trait CNV-burden correlations, BMI-mediated effects, and gene-dosage response patterns.

## Executive summary

We developed FunBurd to move beyond locus-specific CNV analyses. It provides a functional view of gene-dosage sensitivity across the genome by estimating the average trait association of disrupting one additional gene within a predefined functional gene set, while adjusting for genes disrupted outside that set.

We use FunBurd to address three broad questions:

1. **Which biological functions are sensitive to altered gene dosage?**
2. **How do deletions and duplications differ in their associations with complex traits?**
3. **How do functional burden, genetic constraint, pleiotropy, and shared architecture across traits relate to one another?**

```{admonition} Scope of this documentation
:class: note
This site is a **methodological companion and adoption guide**. We explain the logic of FunBurd, the evidence supporting the framework, its assumptions and limitations, and a lightweight notebook example. It is not a full study-reproduction archive and it is not yet documentation for an installable software package.
```

## FunBurd framework

The diagram below shows how the main components fit together: inputs, the core FunBurd model, overlap-aware inference, functional burden pleiotropy, normative constraint modeling, gene-dosage response classification, CNV-burden correlations, variance explained, and BMI mediation analysis.

```{image} _static/figures/method_dependency_map.png
:alt: Dependency map showing how the FunBurd methods fit together
:width: 100%
:align: center
```

Read the guided explanation: [How the FunBurd methods fit together](overview/how_pieces_fit_together.md).

## Publication and code

- [Accepted-manuscript preprint](https://www.medrxiv.org/content/10.1101/2025.02.25.25322833v3)
- [Primary FunBurd analysis-code repository](https://github.com/SayehKazem/FunBurd)
- [Documentation source repository](https://github.com/kkumar-iitkgp/FunBurd-documentation)
- [How to cite FunBurd](reference/citation.md)
- [Current state of the code](using_funburd/code_status.md)

The final *Nature Communications* DOI and versioned archive DOI will be added after the article is published.

## License

We intend to permit **non-commercial research and educational use**. Scholarly use of the framework, code, documentation, or derived workflows should cite our accompanying publication. Commercial use requires separate written permission from the copyright holders.

The approved repository-level license will govern permitted use after final review. See the [License and permitted use](reference/license.md) page for the intended terms and citation requirement.

## Contents

| Section | What it covers | Start here |
|---|---|---|
| **Overview** | How the components fit together, what is new, and the key terminology | [How the pieces fit together](overview/how_pieces_fit_together.md) |
| **Concepts** | Why functional burden is needed, the core model, gene-set construction, data inputs, and interpretation | [Why functional burden?](concepts/why_functional_burden.md) |
| **Using FunBurd** | Applying the framework to a new dataset, the lightweight notebook, toy input/output files, and code state | [Can I apply FunBurd to my own data?](using_funburd/apply_to_your_data.md) |
| **Inference foundation** | Why overlapping gene sets require overlap-aware inference | [P-Jaccard null maps](advanced_methods/p_jaccard.md) |
| **Validation** | Robustness checks, All of Us replication, and comparison across variant classes | [Why trust the framework?](evidence/robustness_checks.md) |
| **Biological insights** | Functional burden pleiotropy, genetic constraint, and gene-dosage responses | [Functional burden pleiotropy and genetic constraint](evidence/pleiotropy_constraint.md) |
| **Advanced extensions** | Normative constraint modeling, CNV-burden correlations, variance explained, BMI mediation, sex-stratified analyses, and sensitivity analyses | [Normative constraint modeling](advanced_methods/normative_constraint_modeling.md) |
| **Reference** | Assumptions, limitations, supplementary tables, figures, citation, licensing, and contributors | [Assumptions and limitations](reference/assumptions_limitations.md) |

## Suggested reading paths

| Reader | Recommended path |
|---|---|
| New to FunBurd | [Why functional burden?](concepts/why_functional_burden.md) → [Core model](concepts/funburd_model.md) → [Interpreting associations](concepts/interpreting_associations.md) |
| Planning to apply the framework | [Apply FunBurd to your data](using_funburd/apply_to_your_data.md) → [Lightweight notebook](tutorial/lightweight_notebook.md) → [Assumptions and limitations](reference/assumptions_limitations.md) |
| Interested in inference | [How the pieces fit together](overview/how_pieces_fit_together.md) → [P-Jaccard](advanced_methods/p_jaccard.md) → [CNV-burden correlations](advanced_methods/cnv_burden_correlations.md) |
| Interested in the biological findings | [Pleiotropy and constraint](evidence/pleiotropy_constraint.md) → [Gene-dosage responses](evidence/gene_dosage_responses.md) |

```{toctree}
:hidden:
:maxdepth: 2
:caption: Overview

overview/how_pieces_fit_together
overview/methodological_contributions
reference/glossary
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Concepts

concepts/why_functional_burden
concepts/funburd_model
concepts/functional_gene_sets
concepts/data_inputs
concepts/interpreting_associations
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Using FunBurd

using_funburd/apply_to_your_data
tutorial/lightweight_notebook
tutorial/input_output_reference
using_funburd/code_status
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Inference foundation

advanced_methods/p_jaccard
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Validation

evidence/robustness_checks
evidence/replication_variant_classes
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Biological insights

evidence/pleiotropy_constraint
evidence/gene_dosage_responses
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Advanced extensions

advanced_methods/normative_constraint_modeling
advanced_methods/cnv_burden_correlations
advanced_methods/bmi_mediation
advanced_methods/sex_stratified
advanced_methods/sensitivity_index
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Reference

reference/assumptions_limitations
reference/supplementary_table_guide
reference/figures
reference/citation
reference/license
reference/contributors
```

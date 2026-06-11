# Try FunBurd with a lightweight notebook

## Purpose

The toy notebook demonstrates the core FunBurd association workflow using small synthetic files. It is intended as a readable walkthrough and a starting point for adaptation, not as a full study-reproduction pipeline.

## Before running the notebook

Read:

1. [How does the FunBurd model work?](../concepts/funburd_model.md)
2. [Applying FunBurd to a new dataset](../using_funburd/apply_to_your_data.md)
3. [Input and output reference](input_output_reference.md)

## Files included with the example

```text
examples/FunBurd_toy/
├── FunBurd_Multitrait_EffectSizes_Computation_Script_On_ToyDatasets.ipynb
├── FunBurd_Multitrait_EffectSizes_Computation_Script_On_ToyDatasets.py
├── Args_File_FunBurd.txt
├── Gene_Sets/
├── Genotypic_info_Toy/
├── Phenotypic_info_Toy/
└── Outcome_Toy/
```

## Walkthrough

### 1. Load genotype, phenotype, and gene-set files

The example reads:

- participant-level CNV information;
- CNV-to-gene annotations;
- cleaned participant covariates;
- one toy phenotype;
- one functional gene-set directory.

### 2. Label genes inside and outside the target set

The function `annotate_gene_set_status()` labels each CNV-overlapped gene according to whether it belongs to the current target set.

### 3. Aggregate participant-level burden variables

The function `aggregate_cnv_counts()` calculates:

- `inside_DEL`;
- `outside_DEL`;
- `inside_DUP`;
- `outside_DUP`.

These correspond to the inside-set and outside-set burden variables used by the FunBurd models.

### 4. Fit deletion and duplication models separately

The function `fit_model_and_extract_results()` fits the relevant continuous or binary outcome model and extracts the association estimate for the inside-set burden variable.

### 5. Iterate across gene sets

The function `analyze_gene_set_data()` applies the workflow across toy gene-set files and writes a compact output table.

## Run one command-line example

From `examples/FunBurd_toy/`:

```bash
python3 FunBurd_Multitrait_EffectSizes_Computation_Script_On_ToyDatasets.py \
  Phenotypic_info_Toy/phenotype1_toy.tsv \
  phenotype1 \
  phenotype1 \
  Gene_Sets/GeneSet_HPA_tissue_fantom_TDEP_nTPM \
  HPA_tissue_fantom_nTPM
```

## Run the supplied argument list

`Args_File_FunBurd.txt` contains example commands spanning four toy phenotypes and three gene-set collections.

## What this example does not cover

The toy example does not reproduce our manuscript figures, perform cross-cohort replication, run S-LDSC, generate P-Jaccard null maps, estimate normative constraint models, compute CNV-burden correlations, or implement the full high-performance-computing workflow used in our study.

For the complete analysis scripts and archived releases, use the public GitHub repository and Zenodo release.

## Next

Continue to [Input and output reference](input_output_reference.md) or [Current code state](../using_funburd/code_status.md).

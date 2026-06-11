# What is the current state of the code?

## Current public interface

The current FunBurd release is **not** an installable Python package with a stable application programming interface. The public materials include:

- analysis and figure-generation workflows from our study in the GitHub repository;
- a lightweight Python script and notebook using toy inputs;
- toy gene-set files, phenotype files, and sample outputs;
- this conceptual and methodological documentation site.

## What is supported by this documentation?

We provide:

- understanding the FunBurd model and its assumptions;
- inspecting the expected input structure;
- running or adapting the toy notebook;
- interpreting the toy outputs;
- locating our analysis scripts and supplementary tables.

## What is outside the scope of this site?

We do not provide:

- a one-command installation of a packaged library;
- a stable public API guarantee;
- an end-to-end CNV-calling pipeline;
- figure-reproduction instructions for every analysis;
- participant-level UK Biobank or All of Us data.

```{admonition} Versioning principle
:class: note
Use tagged GitHub and Zenodo releases for study-matched snapshots. The Read the Docs `latest` version can evolve, while a tagged stable version should remain fixed.
```

## Where to report issues

Use the GitHub repository issue tracker for reproducible problems with the public toy workflow or documentation. Questions requiring restricted cohort data cannot be resolved from the public repository alone.

## Related resources

- [Applying FunBurd to a new dataset](apply_to_your_data.md)
- [Lightweight notebook walkthrough](../tutorial/lightweight_notebook.md)
- [Citation](../reference/citation.md)

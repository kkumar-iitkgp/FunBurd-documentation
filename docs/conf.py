project = "FunBurd"
author = "Sayeh Kazem, Kuldeep Kumar, and collaborators"
copyright = "FunBurd contributors"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "FunBurd documentation"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
]

exclude_patterns = ["_build"]

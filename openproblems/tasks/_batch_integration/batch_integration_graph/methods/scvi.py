# from ....tools.normalize import log_cpm
from .....tools.decorators import method
from .....tools.utils import check_version


@method(
    method_name="Scvi",
    paper_name="Deep generative modeling for single-cell transcriptomics",
    paper_url="https://www.nature.com/articles/s41592-018-0229-2",
    paper_year=2018,
    code_url="https://github.com/YosefLab/scvi-tools",
    code_version=check_version("scvi"),
    image="openproblems-python-batch-integration",  # only if required
)
def scvi_full_unscaled(adata):
    from scIB.integration import runScvi
    from scIB.preprocessing import reduce_data

    adata.obs.rename(
        columns={"labels": "lab"}, inplace=True
    )  # ugly fix for scvi conversion error
    adata = runScvi(adata, "batch")
    reduce_data(adata, umap=False, use_rep="X_emb")
    adata.obs.rename(
        columns={"lab": "labels"}, inplace=True
    )  # ugly fix for scvi conversion error
    # Complete the result in-place
    return adata


@method(
    method_name="Scvi (hvg/unscaled)",
    paper_name="Deep generative modeling for single-cell transcriptomics",
    paper_url="https://www.nature.com/articles/s41592-018-0229-2",
    paper_year=2018,
    code_url="https://github.com/YosefLab/scvi-tools",
    code_version=check_version("scvi"),
    image="openproblems-python-batch-integration",  # only if required
)
def scvi_hvg_unscaled(adata):
    from ._hvg import hvg_batch
    from scIB.integration import runScvi
    from scIB.preprocessing import reduce_data

    adata.obs.rename(
        columns={"labels": "lab"}, inplace=True
    )  # ugly fix for scvi conversion error
    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = runScvi(adata, "batch")
    reduce_data(adata, umap=False, use_rep="X_emb")
    adata.obs.rename(
        columns={"lab": "labels"}, inplace=True
    )  # ugly fix for scvi conversion error
    return adata


@method(
    method_name="Scvi (hvg/scaled)",
    paper_name="Deep generative modeling for single-cell transcriptomics",
    paper_url="https://www.nature.com/articles/s41592-018-0229-2",
    paper_year=2018,
    code_url="https://github.com/YosefLab/scvi-tools",
    code_version=check_version("scvi"),
    image="openproblems-python-batch-integration",  # only if required
)
def scvi_hvg_scaled(adata):
    from ._hvg import hvg_batch
    from ._hvg import scale_batch
    from scIB.integration import runScvi
    from scIB.preprocessing import reduce_data

    adata.obs.rename(
        columns={"labels": "lab"}, inplace=True
    )  # ugly fix for scvi conversion error
    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)
    adata = scale_batch(adata, "batch")
    adata = runScvi(adata, "batch")
    reduce_data(adata, umap=False, use_rep="X_emb")
    adata.obs.rename(
        columns={"lab": "labels"}, inplace=True
    )  # ugly fix for scvi conversion error
    return adata


@method(
    method_name="Scvi (full/scaled)",
    paper_name="Deep generative modeling for single-cell transcriptomics",
    paper_url="https://www.nature.com/articles/s41592-018-0229-2",
    paper_year=2018,
    code_url="https://github.com/YosefLab/scvi-tools",
    code_version=check_version("scvi"),
    image="openproblems-python-batch-integration",  # only if required
)
def scvi_full_scaled(adata):
    from ._hvg import scale_batch
    from scIB.integration import runScvi
    from scIB.preprocessing import reduce_data

    adata.obs.rename(
        columns={"labels": "lab"}, inplace=True
    )  # ugly fix for scvi conversion error
    adata = scale_batch(adata, "batch")
    adata = runScvi(adata, "batch")
    reduce_data(adata, umap=False, use_rep="X_emb")
    adata.obs.rename(
        columns={"lab": "labels"}, inplace=True
    )  # ugly fix for scvi conversion error
    return adata

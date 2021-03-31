from ....tools.decorators import method
from ....tools.utils import check_version
from anndata import AnnData
from scipy.sparse import issparse
from sklearn.decomposition import NMF

import numpy as np


def obs_means(adata: AnnData, cluster_key: str) -> AnnData:
    """Return means over observation key."""

    labels = adata.obs[cluster_key].cat.categories
    means = np.empty((labels.shape[0], adata.shape[1]))
    for i, lab in enumerate(labels):
        means[i, :] = adata[adata.obs[cluster_key] == lab].X.mean(axis=0).flatten()
    adata_means = AnnData(means)
    adata_means.obs_names = labels
    adata_means.var_names = adata.var_names

    return adata_means


@method(
    method_name="Non-Negative Matrix Factorization (NMF).",
    paper_name="Fast local algorithms for large scale nonnegative matrix and tensor factorizations",  # noqa: E501
    paper_url="https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.214.6398&rep=rep1&type=pdf",  # noqa: E501
    paper_year=2009,
    code_url="https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html",  # noqa: E501
    code_version=check_version("scikit-learn"),
)
def nmf(adata):
    """NMF for spatial deconvolution."""

    adata_sc = adata.uns["sc_reference"].copy()
    n_types = adata_sc.obs["label"].cat.categories.shape[0]

    vanila_nmf_model = NMF(
        n_components=n_types,
        beta_loss="kullback-leibler",
        solver="mu",
        max_iter=4000,
        alpha=0.1,
        init="custom",
        random_state=17,  # TODO(handle random_state)
    )

    # Make profiles from single-cell expression dataset
    adata_means = obs_means(adata_sc, "label")

    if issparse(adata.X):
        X = adata.X.toarray()
    else:
        X = adata.X

    Wa = vanila_nmf_model.fit_transform(
        X, H=adata_means.X, W=np.ones((adata.shape[0], n_types), dtype=np.float32)
    )

    prop = Wa / Wa.sum(1)[:, np.newaxis]
    adata.obsm["proportions_pred"] = prop

    return adata
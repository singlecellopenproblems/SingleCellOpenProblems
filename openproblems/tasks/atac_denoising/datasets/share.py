from ....data.multimodal import share
from ....tools.decorators import dataset

def _do_dropout(adata, seed, dropout_rate=.3, cell_fraction=.8):
    '''
    Substract `dropout_rate` many atac reads from the positive
    peak counts.
    '''
    np.random.seed(seed)

    n_cells = int(cell_fraction * adata.n_obs)
    affected_cells = np.random.choice(adata.n_obs, n_cells)
    X = adata.obsm['mode2'].copy()
    atac_subset = X[affected_cells, :]

    positive = atac_subset.data > 0
    values = np.asarray(atac_subset.data[positive].data, dtype=int)
    n_effects = int(dropout_rate * np.sum(values))
    choices = np.repeat(range(len(values)), values)
    affected_peaks = np.random.choice(choices, n_effects)
    idx, diff = np.unique(affected_peaks, return_counts=True)

    atac_subset.data[idx] -= diff
    X[affected_cells, :] = atac_subset
    adata.obsm['mode2_noisy'] = X
    return adata


@dataset(
    "SHARE-seq mouse skin data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_mouse_skin_dropout(
        test = False,
        seed = 234978,
        dropout_rate = .3,
        cell_fraction = .8):
    adata = share.load_share_mouse_skin(test=test)

    adata.uns["species"] = "mus_musculus"
    adata.uns["version"] = "GRCm38"
    adata.uns["release"] = "100"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata


@dataset(
    "SHARE-seq mouse brain data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_mouse_brain_dropout(
        test = False,
        seed = 98712,
        dropout_rate = .3,
        cell_fraction = .8
):
    adata = share.load_share_mouse_brain(test=test)

    adata.uns["species"] = "mus_musculus"
    adata.uns["version"] = "GRCm38"
    adata.uns["release"] = "100"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata


@dataset(
    "SHARE-seq mouse brain data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_mouse_brain(
        test = False,
        seed = 98712,
        dropout_rate = .3,
        cell_fraction = .8
):
    adata = share.load_share_mouse_brain(test=test)

    adata.uns["species"] = "mus_musculus"
    adata.uns["version"] = "GRCm38"
    adata.uns["release"] = "100"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata


@dataset(
    "SHARE-seq mouse lung data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_mouse_lung(
        test = False,
        seed = 98712,
        dropout_rate = .3,
        cell_fraction = .8
):
    adata = share.load_share_mouse_lung(test=test)

    adata.uns["species"] = "mus_musculus"
    adata.uns["version"] = "GRCm38"
    adata.uns["release"] = "100"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata


@dataset(
    "SHARE-seq GM12878 rep1 data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_gm12878_rep1(
        test = False,
        seed = 98712,
        dropout_rate = .3,
        cell_fraction = .8
):
    adata = share.load_share_gm12878_rep1(test=test)

    adata.uns["species"] = "homo_sapiens"
    adata.uns["version"] = "GRCh38"
    adata.uns["release"] = "97"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata


@dataset(
    "SHARE-seq GM12878 rep2 data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_gm12878_rep2(
        test = False,
        seed = 98712,
        dropout_rate = .3,
        cell_fraction = .8
):
    adata = share.load_share_gm12878_rep2(test=test)

    adata.uns["species"] = "homo_sapiens"
    adata.uns["version"] = "GRCh38"
    adata.uns["release"] = "97"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata


@dataset(
    "SHARE-seq GM12878 rep3 data with evenly distributed dropout in\
    the postive peak counts",
    image="openproblems-python-extras"
)
def share_gm12878_rep3(
        test = False,
        seed = 98712,
        dropout_rate = .3,
        cell_fraction = .8
):
    adata = share.load_share_gm12878_rep3(test=test)

    adata.uns["species"] = "homo_sapiens"
    adata.uns["version"] = "GRCh38"
    adata.uns["release"] = "97"
    adata = _do_dropout(
        adata,
        seed,
        dropout_rate = dropout_rate,
        cell_fraction = cell_fraction
    )
    return adata

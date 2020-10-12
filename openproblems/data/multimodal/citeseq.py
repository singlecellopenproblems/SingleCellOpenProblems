import os
import tempfile

import numpy as np
import pandas as pd
import scanpy as sc
import scprep
import anndata

from ..utils import loader
from .utils import filter_joint_data_empty_cells, create_joint_adata, subset_joint_data

ADT_URL = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE100866&format=file&file=GSE100866%5FCBMC%5F8K%5F13AB%5F10X%2DADT%5Fumi%2Ecsv%2Egz"
RNA_URL = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE100866&format=file&file=GSE100866%5FCBMC%5F8K%5F13AB%5F10X%2DRNA%5Fumi%2Ecsv%2Egz"


@loader
def load_citeseq_cbmc(test=False):
    if test:
        adata = load_citeseq_cbmc(test=False)
        adata = subset_joint_data(adata)
        return adata

    rna_data = scprep.io.load_csv(
        RNA_URL, cell_axis="col", compression="gzip", sparse=True
    )
    adt_data = scprep.io.load_csv(
        ADT_URL, cell_axis="col", compression="gzip", sparse=True
    )

    adata = create_joint_adata(rna_data, adt_data)
    adata = filter_joint_data_empty_cells(adata)
    return adata
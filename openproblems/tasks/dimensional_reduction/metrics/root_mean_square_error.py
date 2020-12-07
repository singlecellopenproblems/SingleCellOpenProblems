import numpy as np
import scipy as sp
import pandas as pd

from ....tools.decorators import metric


def calculate_squareform_pairwise_distance(data):
    """Calculate pairwise distances.

    Compute pairwise distance between points in a matrix / vector and then format this
    into a squareform vector.
    """
    df = pd.DataFrame(sp.spatial.distance.squareform(sp.spatial.distance.pdist(data)))
    return df


def calculate_rmse(adata):
    """Calculate dimensional reduction stress via root mean square error."""
    high_dimensional_distance_matrix = calculate_squareform_pairwise_distance(
        pd.DataFrame(adata.X)
    )

    low_dimensional_distance_matrix = calculate_squareform_pairwise_distance(
        pd.DataFrame(adata.obsm["X_emb"])
    )

    diff = high_dimensional_distance_matrix - low_dimensional_distance_matrix

    kruskel_matrix = np.sqrt(diff ** 2 / sum(low_dimensional_distance_matrix ** 2))

    kruskel_score = np.sqrt(sum(diff ** 2) / sum(low_dimensional_distance_matrix ** 2))

    y_actual = high_dimensional_distance_matrix
    y_predic = low_dimensional_distance_matrix

    from sklearn.metrics import mean_squared_error
    from math import sqrt

    rms = sqrt(mean_squared_error(y_actual, y_predic))

    return kruskel_matrix, kruskel_score, rms


@metric(metric_name="root mean squared error", maximize=True)
def rmse(adata):
    """Calculate the root mean squared error.

    Computes  (RMSE) between the full (or processed) data matrix and a list of
    dimensionally-reduced matrices.
    """
    (
        adata.obsp["kruskel_matrix"],
        adata.uns["kruskel_score"],
        adata.uns["rmse_score"],
    ) = calculate_rmse(adata)

    return float(adata.uns["rmse_score"])
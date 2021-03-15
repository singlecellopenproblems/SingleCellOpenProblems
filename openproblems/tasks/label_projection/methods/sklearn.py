import sklearn.preprocessing
from .utils import pca_op
import numpy as np


def classifier(adata, estimator, n_pca=100, **kwargs):
    """Run a generic scikit-learn classifier."""
    adata_train = adata[adata.obs["is_train"]]
    adata_test = adata[~adata.obs["is_train"]].copy()

    classifier = sklearn.pipeline.Pipeline(
        [
            ("pca", pca_op(adata_train, adata_test, n_components=n_pca)),
            ("scaler", sklearn.preprocessing.StandardScaler(with_mean=True)),
            ("regression", estimator(**kwargs)),
        ]
    )

    # Fit to train data
    classifier.fit(adata_train.X, adata_train.obs["labels"].astype(str))

    # Predict on test data
    adata_test.obs["labels_pred"] = classifier.predict(adata_test.X)

    adata.obs["labels_pred"] = [
        adata_test.obs["labels_pred"][idx] if idx in adata_test.obs_names else np.nan
        for idx in adata.obs_names
    ]
    return adata
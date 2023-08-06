import re
import pandas as pd
import numpy as np
import sklearn
import scipy.sparse as sp
from sklearn.base import clone

def get_numeric_cols(X, cat_cols):
    if cat_cols is None:
        return "all"
    elif len(cat_cols) < X.shape[1]:
        if (isinstance(X, pd.DataFrame)) and (isinstance(cat_cols[0], str)):
            return list((set(X.columns)).difference(cat_cols))
        else:
            return np.array(list(set(range(X.shape[1])).difference(cat_cols)))
    else:
        return None

def safe_column_indexing(X, columns):
    if columns is None:
        return
    if isinstance(columns, str) and (columns == "all"):
        return X
    columns = np.array(columns)
    columns_type = "string" if isinstance(columns[0], str) else "int"

    if isinstance(X, pd.DataFrame):
        if columns_type == "string":
            return X.loc[:, columns]
        else:
            return X.iloc[:, columns]
    else:
        return X[:, columns]

def _get_params(trial, params):
    param_dict = {}
    for (key, value) in params.items():
        if "optuna.distributions" in str(type(value)):
            param_dict[key] = trial._suggest(key, value)
        else:
            param_dict[key] = params[key]
    return param_dict

def _init_pipeline(pipeline, pipe_params, trial):
    if pipeline is not None:
        final_pipeline = clone(pipeline)
        if pipe_params is not None:
            pipe_params = _get_params(trial, pipe_params)
            final_pipeline.set_params(**pipe_params)
        return final_pipeline
    return None

def contains_nan(X):
    if isinstance(X, pd.DataFrame):
        return pd.isnull(X).values.any()
    elif sp.issparse(X):
        return pd.isnull(X.data).any()
    else:
        return pd.isnull(X).any() #numpy

def get_scorer_type(scoring):
    if isinstance(scoring, str):
        scorer = sklearn.metrics.get_scorer(scoring)
        # https://github.com/scikit-learn/scikit-learn/blob/1495f6924/sklearn/metrics/scorer.py
    elif "sklearn.metrics.scorer" in str(type(scoring)):
        scorer = scoring
    else:  # TODO: error
        print("invalid scoring function. please see: "
              "https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter or "
              "use the 'make_scorer' function in sklearn")
        return

    if "_Threshold" in str(type(scorer)):
        scorer_type = "threshold"
    elif "_Predict" in str(type(scorer)):
        scorer_type = "predict"
    else:
        scorer_type = "proba"

    greater_is_better = False if ("greater_is_better=False" in str(scorer)) else True

    return scorer, scorer_type, greater_is_better

def ge_version(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return normalize(version1) >= normalize(version2)
import xgboost as xgb
from xgboost import XGBRegressor
import numpy as np
from ..xgboost import XGBModelHypster

class XGBTreeRegressorHypster(XGBModelHypster):
    def get_tags(self):
        self.tags = {'name' : "XGBoost Tree-Based Regressor",
                    'model type': "tree",
                    'supports regression': True,
                    'supports ranking': False,
                    'supports classification': False,
                    'supports multiclass': False,
                    'supports multilabel': False,
                    'handles categorical' : False,
                    'handles categorical nan': False,
                    'handles sparse': True,
                    'handles numeric nan': True,
                    'nan value when sparse': 0,
                    'sensitive to feature scaling': False,
                    'has predict_proba' : False,
                    'has model embeddings': False,
                    'adjustable model complexity' : True,
                    }
        return self.tags

    def choose_and_set_params(self, trial, y_mean, missing):
        self.trial = trial
        model_params = {'seed': self.random_state,
                        'verbosity': 0,
                        'nthread': self.n_jobs,
                        'missing' : missing,
                        'objective' : 'reg:squarederror',
                        'base_score' : y_mean,
                        'eta': self.sample_hp('eta', "log-uniform", [1e-3, 1.0]),
                        'booster': self.sample_hp('booster', "categorical", ["gbtree", "dart"]),
                        'lambda': self.sample_hp('lambda', "log-uniform", [1e-10, 1.0]),
                        'alpha': self.sample_hp('alpha', "log-uniform", [1e-10, 1.0]),
                        'max_depth': self.sample_hp('max_depth', "int", [2, 20]), #TODO: maybe change to higher range?
                        'min_child_weight': self.sample_hp('min_child_weight', "int", [1, 20]),
                        'gamma': self.sample_hp('gamma', "log-uniform", [1e-10, 5.0]),
                        'grow_policy': self.sample_hp('grow_policy', "categorical", ['depthwise', 'lossguide']),
                        'subsample': self.sample_hp('subsample', "uniform", [0.5, 1.0]),
                        'colsample_bytree': self.sample_hp('colsample_bytree', "uniform", [0.1, 1.0]),
                        'colsample_bynode': self.sample_hp('colsample_bynode', "uniform", [0.1, 1.0]),
                        }

        forest_boosting = self.sample_hp('forest_boosting', "categorical", [True, False])
        if forest_boosting:
            model_params['num_parallel_tree'] = self.sample_hp('num_parallel_tree', "int", [2, 10])
        else:
            model_params['num_parallel_tree'] = 1

        #model_params['feature_selector'] = self.sample_hp('shotgun_feature_selector', "categorical",
        #                                                      ['cyclic', 'shuffle'])

        if model_params['booster'] == 'dart':
            dart_dict = {'sample_type': self.sample_hp('sample_type', "categorical", ['uniform', 'weighted'])
                , 'normalize_type': self.sample_hp('normalize_type', "categroical", ['tree', 'forest'])
                , 'rate_drop': self.sample_hp('rate_drop', "log-uniform", [1e-8, 1.0])
                , 'skip_drop': self.sample_hp('skip_drop', "log-uniform", [1e-8, 1.0])
                }

            model_params.update(dart_dict)

        self.model_params = model_params

    def predict(self):
        if self.model_params["booster"] == "dart":
            preds = self.current_model.predict(self.dtest, output_margin=False, ntree_limit=0)
        else:
            preds= self.current_model.predict(self.dtest, output_margin=False)

        return preds

    def create_model(self):
        # TODO: if learning rates are identical throughout - create a regular Classifier

        self.model_params['n_estimators'] = self.best_n_iterations
        self.model_params['learning_rate'] = self.learning_rates[0]

        self.model_params['n_jobs'] = self.model_params.pop('nthread')
        self.model_params['random_state'] = self.model_params.pop('seed')
        self.model_params['reg_lambda'] = self.model_params.pop('lambda')
        self.model_params['reg_alpha'] = self.model_params.pop('alpha')

        final_model = XGBRegressor(**self.model_params)
        #final_model = XGBRegressorLR(learning_rates=self.learning_rates, **self.model_params)
        return final_model

class XGBLinearRegressorHypster(XGBModelHypster):
    def get_tags(self):
        self.tags = {'name' : "XGBoost Linear Regressor",
                    'model type': "linear",
                    'supports regression': True,
                    'supports ranking': False,
                    'supports classification': False,
                    'supports multiclass': False,
                    'supports multilabel': False,
                    'handles categorical' : False,
                    'handles categorical nan': False,
                    'handles sparse': True,
                    'handles numeric nan': True,
                    'nan value when sparse': 0,
                    'sensitive to feature scaling': False,
                    'has predict_proba' : False,
                    'has model embeddings': False,
                    'adjustable model complexity' : True,
                    }
        return self.tags

    def choose_and_set_params(self, trial, y_mean, missing):
        self.trial = trial
        model_params = {'seed': self.random_state,
                        'verbosity': 0,
                        'nthread': self.n_jobs,
                        'missing' : missing,
                        'objective' : 'reg:squarederror',
                        'base_score' : y_mean,
                        'eta': self.sample_hp('eta', "log-uniform", [1e-3, 1.0]),
                        'booster': "gblinear",
                        'lambda': self.sample_hp('lambda', "log-uniform", [1e-10, 1.0]),
                        'alpha': self.sample_hp('alpha', "log-uniform", [1e-10, 1.0]),
                        'feature_selector' : self.sample_hp('shotgun_feature_selector', "categorical",
                                                            ['cyclic', 'shuffle'])
                        }

        self.model_params = model_params

    def predict(self):
        preds= self.current_model.predict(self.dtest, output_margin=False)
        return preds

    def create_model(self):
        # TODO: if learning rates are identical throughout - create a regular Classifier
        self.model_params['n_estimators'] = self.best_n_iterations
        self.model_params['learning_rate'] = self.learning_rates[0]

        self.model_params['n_jobs'] = self.model_params.pop('nthread')
        self.model_params['random_state'] = self.model_params.pop('seed')
        self.model_params['reg_lambda'] = self.model_params.pop('lambda')
        self.model_params['reg_alpha'] = self.model_params.pop('alpha')

        final_model = XGBRegressor(**self.model_params)
        #final_model = XGBRegressorLR(learning_rates=self.learning_rates, **self.model_params)
        return final_model

class XGBRegressorLR(XGBRegressor):
    def __init__(self, learning_rates = None,
                 max_depth=3, learning_rate=1, n_estimators=100,
                 verbosity=1,
                 objective="reg:squarederror", booster="gbtree", n_jobs=1, nthread=None, gamma=0,
                 min_child_weight=1, max_delta_step=0, subsample=0.8, colsample_bytree=1,
                 colsample_bylevel=1, colsample_bynode=0.8, reg_alpha=0, reg_lambda=1,
                 scale_pos_weight=1, base_score=0.5, random_state=0, seed=None,
                 missing=None, **kwargs):

        if 'learning_rates' in kwargs:
            self.learning_rates = kwargs.pop('learning_rates')
        else:
            self.learning_rates = learning_rates

        super(XGBRegressorLR, self).__init__(
            max_depth=max_depth, learning_rate=learning_rate, n_estimators=n_estimators,
            verbosity=verbosity, objective=objective, booster=booster,
            n_jobs=n_jobs, nthread=nthread, gamma=gamma,
            min_child_weight=min_child_weight, max_delta_step=max_delta_step,
            subsample=subsample, colsample_bytree=colsample_bytree,
            colsample_bylevel=colsample_bylevel, colsample_bynode=colsample_bynode,
            reg_alpha=reg_alpha, reg_lambda=reg_lambda, scale_pos_weight=scale_pos_weight,
            base_score=base_score, random_state=random_state, seed=seed, missing=missing,
            **kwargs)


    def fit(self, X, y, sample_weight=None, eval_set=None, eval_metric=None,
            early_stopping_rounds=None, verbose=True, xgb_model=None,
            sample_weight_eval_set=None, callbacks=None):

        y = np.array(y)

        if self.learning_rates is not None:
            lr_callback = [xgb.callback.reset_learning_rate(self.learning_rates)]
        else:
            lr_callback = None

        if callbacks is not None:
            callbacks = [callback for callback in callbacks if 'reset_learning_rate' not in str(callback)]
            callbacks = callbacks + lr_callback
        else:
            callbacks = lr_callback

        return super(XGBRegressorLR, self).fit(X, y, callbacks = callbacks)
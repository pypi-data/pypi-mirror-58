import pickle
import unittest

import numpy as np
import scipy.sparse as sp

from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_almost_equal
from sklearn.utils.testing import assert_array_almost_equal
from sklearn.utils.testing import assert_greater
from sklearn.utils.testing import assert_greater_equal
from sklearn.utils.testing import assert_less
from sklearn.utils.testing import raises
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import assert_false, assert_true
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_not_equal
from sklearn.utils.testing import assert_raises_regexp
from sklearn.utils.testing import ignore_warnings

from sklearn import linear_model, datasets, metrics
from sklearn.base import clone
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import LabelEncoder, scale, MinMaxScaler

from sklearn.linear_model import sgd_fast
from sklearn.utils.multiclass import unique_labels


class SparseSGDClassifier(SGDClassifier):

    def fit(self, X, y, *args, **kw):
        X = sp.csr_matrix(X)
        return super(SparseSGDClassifier, self).fit(X, y, *args, **kw)

    def partial_fit(self, X, y, *args, **kw):
        X = sp.csr_matrix(X)
        return super(SparseSGDClassifier, self).partial_fit(X, y, *args, **kw)

    def decision_function(self, X):
        X = sp.csr_matrix(X)
        return super(SparseSGDClassifier, self).decision_function(X)

    def predict_proba(self, X):
        X = sp.csr_matrix(X)
        return super(SparseSGDClassifier, self).predict_proba(X)

# Test Data

# test sample 1
X = np.array([[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1]])
Y = [1, 1, 1, 2, 2, 2]
T = np.array([[-1, -1], [2, 2], [3, 2]])
true_result = [1, 2, 2]

# test sample 2; string class labels
X2 = np.array([[-1, 1], [-0.75, 0.5], [-1.5, 1.5],
               [1, 1], [0.75, 0.5], [1.5, 1.5],
               [-1, -1], [0, -0.5], [1, -1]])
Y2 = ["one"] * 3 + ["two"] * 3 + ["three"] * 3
T2 = np.array([[-1.5, 0.5], [1, 2], [0, -2]])
true_result2 = ["one", "two", "three"]

# test sample 3
X3 = np.array([[1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1],
               [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]])
Y3 = np.array([1, 1, 1, 1, 2, 2, 2, 2])

# test sample 4 - two more or less redundant feature groups
X4 = np.array([[1, 0.9, 0.8, 0, 0, 0], [1, .84, .98, 0, 0, 0],
               [1, .96, .88, 0, 0, 0], [1, .91, .99, 0, 0, 0],
               [0, 0, 0, .89, .91, 1], [0, 0, 0, .79, .84, 1],
               [0, 0, 0, .91, .95, 1], [0, 0, 0, .93, 1, 1]])
Y4 = np.array([1, 1, 1, 1, 2, 2, 2, 2])

iris = datasets.load_iris()

# test sample 5 - test sample 1 as binary classification problem
X5 = np.array([[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1]])
Y5 = [1, 1, 1, 2, 2, 2]
true_result5 = [0, 1, 1]


# Classification Test Case

class CommonTest(object):

    def factory(self, **kwargs):
        if "random_state" not in kwargs:
            kwargs["random_state"] = 42
        return self.factory_class(**kwargs)

    # a simple implementation of ASGD to use for testing
    # uses squared loss to find the gradient
    def asgd(self, X, y, eta, alpha, weight_init=None, intercept_init=0.0):
        num_classes = len(unique_labels(y))
        if weight_init is None:
            weights = np.zeros((num_classes, X.shape[1]))
        else:
            weights = weight_init

        average_weights = np.zeros((num_classes, X.shape[1]))
        intercept = intercept_init
        average_intercept = np.zeros(num_classes)
        decay = 1.0

        # sparse data has a fixed decay of .01
        if (isinstance(self, SparseSGDClassifierTestCase)):
            decay = .01

        print("weights", weights)
        for i, entry in enumerate(X):
            p = np.dot(entry, weights)
            p += intercept
            gradient = p - y[i]
            weights *= 1.0 - (eta * alpha)
            weights += -(eta * gradient * entry)
            intercept += -(eta * gradient) * decay

            average_weights *= i
            average_weights += weights
            average_weights /= i + 1.0

            average_intercept *= i
            average_intercept += intercept
            average_intercept /= i + 1.0

        print("average_weights", average_weights)
        return average_weights, average_intercept

    def _test_warm_start(self, X, Y, lr):
        # Test that explicit warm restart...
        clf = self.factory(alpha=0.01, eta0=0.01, n_iter=5, shuffle=False,
                           learning_rate=lr)
        clf.fit(X, Y)

        clf2 = self.factory(alpha=0.001, eta0=0.01, n_iter=5, shuffle=False,
                            learning_rate=lr)
        clf2.fit(X, Y,
                 coef_init=clf.coef_.copy(),
                 intercept_init=clf.intercept_.copy())

        # ... and implicit warm restart are equivalent.
        clf3 = self.factory(alpha=0.01, eta0=0.01, n_iter=5, shuffle=False,
                            warm_start=True, learning_rate=lr)
        clf3.fit(X, Y)

        assert_equal(clf3.t_, clf.t_)
        assert_array_almost_equal(clf3.coef_, clf.coef_)

        clf3.set_params(alpha=0.001)
        clf3.fit(X, Y)

        assert_equal(clf3.t_, clf2.t_)
        assert_array_almost_equal(clf3.coef_, clf2.coef_)

    def test_warm_start_constant(self):
        self._test_warm_start(X, Y, "constant")

    def test_warm_start_invscaling(self):
        self._test_warm_start(X, Y, "invscaling")

    def test_warm_start_optimal(self):
        self._test_warm_start(X, Y, "optimal")

    def test_input_format(self):
        # Input format tests.
        clf = self.factory(alpha=0.01, n_iter=5,
                           shuffle=False)
        clf.fit(X, Y)
        Y_ = np.array(Y)[:, np.newaxis]

        Y_ = np.c_[Y_, Y_]
        assert_raises(ValueError, clf.fit, X, Y_)

    def test_clone(self):
        # Test whether clone works ok.
        clf = self.factory(alpha=0.01, n_iter=5, penalty='l1')
        clf = clone(clf)
        clf.set_params(penalty='l2')
        clf.fit(X, Y)

        clf2 = self.factory(alpha=0.01, n_iter=5, penalty='l2')
        clf2.fit(X, Y)

        assert_array_equal(clf.coef_, clf2.coef_)

    def test_plain_has_no_average_attr(self):
        clf = self.factory(average=True, eta0=.01)
        clf.fit(X, Y)

        assert_true(hasattr(clf, 'average_coef_'))
        assert_true(hasattr(clf, 'average_intercept_'))
        assert_true(hasattr(clf, 'standard_intercept_'))
        assert_true(hasattr(clf, 'standard_coef_'))

        clf = self.factory()
        clf.fit(X, Y)

        assert_false(hasattr(clf, 'average_coef_'))
        assert_false(hasattr(clf, 'average_intercept_'))
        assert_false(hasattr(clf, 'standard_intercept_'))
        assert_false(hasattr(clf, 'standard_coef_'))

    def test_late_onset_averaging_not_reached(self):
        clf1 = self.factory(average=600)
        clf2 = self.factory()
        for _ in range(100):
            if isinstance(clf1, SGDClassifier):
                clf1.partial_fit(X, Y)
                clf2.partial_fit(X, Y)
            else:
                clf1.partial_fit(X, Y)
                clf2.partial_fit(X, Y)

        assert_array_almost_equal(clf1.coef_, clf2.coef_, decimal=16)
        assert_almost_equal(clf1.intercept_, clf2.intercept_, decimal=16)

    # This test does not work right now because now we have separate averaging
    # schedules for each class and so the results with asgd do not match.
    #
    # def test_late_onset_averaging_reached(self):
    #     eta0 = .001
    #     alpha = .0001
    #     Y_encode = np.array(Y)
    #     Y_encode[Y_encode == 1] = -1.0
    #     Y_encode[Y_encode == 2] = 1.0

    #     clf1 = self.factory(average=7, learning_rate="constant",
    #                         loss='squared_loss', eta0=eta0,
    #                         alpha=alpha, n_iter=2, shuffle=False)
    #     clf2 = self.factory(average=0, learning_rate="constant",
    #                         loss='squared_loss', eta0=eta0,
    #                         alpha=alpha, n_iter=1, shuffle=False)

    #     clf1.fit(X, Y_encode)
    #     clf2.fit(X, Y_encode)


    #     average_weights, average_intercept = \
    #         self.asgd(X, Y_encode, eta0, alpha,
    #                   weight_init=clf2.coef_,
    #                   intercept_init=clf2.intercept_)

    #     assert_array_almost_equal(clf1.coef_.ravel(),
    #                               average_weights.ravel(),
    #                               decimal=16)
    #     assert_almost_equal(clf1.intercept_, average_intercept, decimal=16)

    @raises(ValueError)
    def test_sgd_bad_alpha_for_optimal_learning_rate(self):
        # Check whether expected ValueError on bad alpha, i.e. 0
        # since alpha is used to compute the optimal learning rate
        self.factory(alpha=0, learning_rate="optimal")


class DenseSGDClassifierTestCase(unittest.TestCase, CommonTest):
    """Test suite for the dense representation variant of SGD"""
    factory_class = SGDClassifier

    def test_sgd(self):
        # Check that SGD gives any results :-)

        for loss in ("hinge", "squared_hinge", "log", "modified_huber"):
            clf = self.factory(penalty='l2', alpha=0.01, fit_intercept=True,
                               loss=loss, n_iter=10, shuffle=True)
            clf.fit(X, Y)
            # assert_almost_equal(clf.coef_[0], clf.coef_[1], decimal=7)
            assert_array_equal(clf.predict(T), true_result)

    @raises(ValueError)
    def test_sgd_bad_l1_ratio(self):
        # Check whether expected ValueError on bad l1_ratio
        self.factory(l1_ratio=1.1)

    @raises(ValueError)
    def test_sgd_bad_learning_rate_schedule(self):
        # Check whether expected ValueError on bad learning_rate
        self.factory(learning_rate="<unknown>")

    @raises(ValueError)
    def test_sgd_bad_eta0(self):
        # Check whether expected ValueError on bad eta0
        self.factory(eta0=0, learning_rate="constant")

    @raises(ValueError)
    def test_sgd_bad_alpha(self):
        # Check whether expected ValueError on bad alpha
        self.factory(alpha=-.1)

    @raises(ValueError)
    def test_sgd_bad_penalty(self):
        # Check whether expected ValueError on bad penalty
        self.factory(penalty='foobar', l1_ratio=0.85)

    @raises(ValueError)
    def test_sgd_bad_loss(self):
        # Check whether expected ValueError on bad loss
        self.factory(loss="foobar")

    @raises(ValueError)
    def test_sgd_n_iter_param(self):
        # Test parameter validity check
        self.factory(n_iter=-10000)

    @raises(ValueError)
    def test_sgd_shuffle_param(self):
        # Test parameter validity check
        self.factory(shuffle="false")

    @raises(TypeError)
    def test_argument_coef(self):
        # Checks coef_init not allowed as model argument (only fit)
        # Provided coef_ does not match dataset.
        self.factory(coef_init=np.zeros((3,))).fit(X, Y)

    @raises(ValueError)
    def test_provide_coef(self):
        # Checks coef_init shape for the warm starts
        # Provided coef_ does not match dataset.
        self.factory().fit(X, Y, coef_init=np.zeros((3,)))

    @raises(ValueError)
    def test_set_intercept(self):
        # Checks intercept_ shape for the warm starts
        # Provided intercept_ does not match dataset.
        self.factory().fit(X, Y, intercept_init=np.zeros((3,)))

    # def test_set_intercept_binary(self):
    #     # Checks intercept_ shape for the warm starts in binary case
    #     self.factory().fit(X5, Y5, intercept_init=0)

    # def test_average_binary_computed_correctly(self):
    #     # Checks the SGDClassifier correctly computes the average weights
    #     eta = .1
    #     alpha = 2.
    #     n_samples = 20
    #     n_features = 10
    #     rng = np.random.RandomState(0)
    #     X = rng.normal(size=(n_samples, n_features))
    #     w = rng.normal(size=n_features)

    #     clf = self.factory(loss='squared_loss',
    #                        learning_rate='constant',
    #                        eta0=eta, alpha=alpha,
    #                        fit_intercept=True,
    #                        n_iter=1, average=True, shuffle=False)

    #     # simple linear function without noise
    #     y = np.dot(X, w)
    #     y = np.sign(y)

    #     clf.fit(X, y)

    #     average_weights, average_intercept = self.asgd(X, y, eta, alpha)
    #     average_weights = average_weights.reshape(1, -1)
    #     assert_array_almost_equal(clf.coef_,
    #                               average_weights,
    #                               decimal=14)
    #     assert_almost_equal(clf.intercept_, average_intercept, decimal=14)

    def test_set_intercept_to_intercept(self):
        # Checks intercept_ shape consistency for the warm starts
        # Inconsistent intercept_ shape.
        clf = self.factory().fit(X5, Y5)
        self.factory().fit(X5, Y5, intercept_init=clf.intercept_)
        clf = self.factory().fit(X, Y)
        self.factory().fit(X, Y, intercept_init=clf.intercept_)

    # @raises(ValueError)
    # def test_sgd_at_least_two_labels(self):
    #     # Target must have at least two labels
    #     self.factory(alpha=0.01, n_iter=20).fit(X2, np.ones(9))

    def test_partial_fit_weight_class_balanced(self):
        # partial_fit with class_weight='balanced' not supported"""
        assert_raises_regexp(ValueError,
                             "class_weight 'balanced' is not supported for "
                             "partial_fit. In order to use 'balanced' weights, "
                             "use compute_class_weight\('balanced', classes, y\). "
                             "In place of y you can us a large enough sample "
                             "of the full training set target to properly "
                             "estimate the class frequency distributions. "
                             "Pass the resulting weights as the class_weight "
                             "parameter.",
                             self.factory(class_weight='balanced').partial_fit,
                             X, Y)

    def test_sgd_multiclass(self):
        # Multi-class test case
        clf = self.factory(alpha=0.01, n_iter=20).fit(X2, Y2)
        assert_equal(clf.coef_.shape, (3, 2))
        assert_equal(clf.intercept_.shape, (3,))
        assert_equal(clf.decision_function([[0, 0]]).shape, (1, 3))
        pred = clf.predict(T2)
        assert_array_equal(pred, true_result2)

    def test_sgd_multiclass_average(self):
        eta = .001
        alpha = .01
        # Multi-class average test case
        clf = self.factory(loss='squared_loss',
                           learning_rate='constant',
                           eta0=eta, alpha=alpha,
                           fit_intercept=True,
                           n_iter=1, average=True, shuffle=False)

        np_Y2 = np.array(Y2)
        clf.fit(X2, np_Y2)
        classes = np.unique(np_Y2)

        for i, cl in enumerate(classes):
            y_i = np.ones(np_Y2.shape[0])
            y_i[np_Y2 != cl] = -1
            average_coef, average_intercept = self.asgd(X2, y_i, eta, alpha)
            assert_array_almost_equal(average_coef,
                                      np.array([clf.average_coef_[i],
                                                clf.average_coef_[i]]),
                                      decimal=3)
            assert_almost_equal(average_intercept,
                                np.array([clf.intercept_[i],
                                          clf.intercept_[i]]),
                                decimal=3)

    def test_sgd_multiclass_with_init_coef(self):
        # Multi-class test case
        clf = self.factory(alpha=0.01, n_iter=20)
        clf.fit(X2, Y2, coef_init=np.zeros((3, 2)),
                intercept_init=np.zeros(3))
        assert_equal(clf.coef_.shape, (3, 2))
        assert_true(clf.intercept_.shape, (3,))
        pred = clf.predict(T2)
        assert_array_equal(pred, true_result2)

    def test_sgd_multiclass_njobs(self):
        # Multi-class test case with multi-core support
        clf = self.factory(alpha=0.01, n_iter=20, n_jobs=2).fit(X2, Y2)
        assert_equal(clf.coef_.shape, (3, 2))
        assert_equal(clf.intercept_.shape, (3,))
        assert_equal(clf.decision_function([[0, 0]]).shape, (1, 3))
        pred = clf.predict(T2)
        assert_array_equal(pred, true_result2)

    def test_set_coef_multiclass(self):
        # Checks coef_init and intercept_init shape for multi-class
        # problems
        # Provided coef_ does not match dataset
        clf = self.factory()
        assert_raises(ValueError, clf.fit, X2, Y2, coef_init=np.zeros((2, 2)))

        # Provided coef_ does match dataset
        clf = self.factory().fit(X2, Y2, coef_init=np.zeros((3, 2)))

        # Provided intercept_ does not match dataset
        clf = self.factory()
        assert_raises(ValueError, clf.fit, X2, Y2,
                      intercept_init=np.zeros((1,)))

        # Provided intercept_ does match dataset.
        clf = self.factory().fit(X2, Y2, intercept_init=np.zeros((3,)))

    def test_sgd_proba(self):
        # Check SGD.predict_proba

        # Hinge loss does not allow for conditional prob estimate.
        # We cannot use the factory here, because it defines predict_proba
        # anyway.
        clf = SGDClassifier(loss="hinge", alpha=0.01, n_iter=10).fit(X, Y)
        assert_false(hasattr(clf, "predict_proba"))
        assert_false(hasattr(clf, "predict_log_proba"))

        # log and modified_huber losses can output probability estimates
        # binary case
        for loss in ["log", "modified_huber"]:
            clf = self.factory(loss=loss, alpha=0.01, n_iter=10)
            clf.fit(X, Y)
            p = clf.predict_proba([[3, 2]])
            assert_true(p[0, 1] > 0.5)
            p = clf.predict_proba([[-1, -1]])
            assert_true(p[0, 1] < 0.5)

            p = clf.predict_log_proba([[3, 2]])
            assert_true(p[0, 1] > p[0, 0])
            p = clf.predict_log_proba([[-1, -1]])
            assert_true(p[0, 1] < p[0, 0])

        # log loss multiclass probability estimates
        clf = self.factory(loss="log", alpha=0.01, n_iter=10).fit(X2, Y2)

        d = clf.decision_function([[.1, -.1], [.3, .2]])
        p = clf.predict_proba([[.1, -.1], [.3, .2]])
        assert_array_equal(np.argmax(p, axis=1), np.argmax(d, axis=1))
        assert_almost_equal(p[0].sum(), 1)
        assert_true(np.all(p[0] >= 0))

        p = clf.predict_proba([[-1, -1]])
        d = clf.decision_function([[-1, -1]])
        assert_array_equal(np.argsort(p[0]), np.argsort(d[0]))

        l = clf.predict_log_proba([[3, 2]])
        p = clf.predict_proba([[3, 2]])
        assert_array_almost_equal(np.log(p), l)

        l = clf.predict_log_proba([[-1, -1]])
        p = clf.predict_proba([[-1, -1]])
        assert_array_almost_equal(np.log(p), l)

        # Modified Huber multiclass probability estimates; requires a separate
        # test because the hard zero/one probabilities may destroy the
        # ordering present in decision_function output.
        clf = self.factory(loss="modified_huber", alpha=0.01, n_iter=10)
        clf.fit(X2, Y2)
        d = clf.decision_function([[3, 2]])
        p = clf.predict_proba([[3, 2]])
        if not isinstance(self, SparseSGDClassifierTestCase):
            assert_equal(np.argmax(d, axis=1), np.argmax(p, axis=1))
        else:   # XXX the sparse test gets a different X2 (?)
            assert_equal(np.argmin(d, axis=1), np.argmin(p, axis=1))

        # the following sample produces decision_function values < -1,
        # which would cause naive normalization to fail (see comment
        # in SGDClassifier.predict_proba)
        x = X.mean(axis=0)
        d = clf.decision_function([x])
        if np.all(d < -1):  # XXX not true in sparse test case (why?)
            p = clf.predict_proba([x])
            assert_array_almost_equal(p[0], [1 / 3.] * 3)

    def test_sgd_l1(self):
        # Test L1 regularization
        n = len(X4)
        rng = np.random.RandomState(13)
        idx = np.arange(n)
        rng.shuffle(idx)

        X = X4[idx, :]
        Y = Y4[idx]

        clf = self.factory(penalty='l1', alpha=.2, fit_intercept=False,
                           n_iter=2000, shuffle=False)
        clf.fit(X, Y)
        assert_array_equal(clf.coef_[0, 1:-1], np.zeros((4,)))
        pred = clf.predict(X)
        assert_array_equal(pred, Y)

        # test sparsify with dense inputs
        clf.sparsify()
        assert_true(sp.issparse(clf.coef_))
        pred = clf.predict(X)
        assert_array_equal(pred, Y)

        # pickle and unpickle with sparse coef_
        clf = pickle.loads(pickle.dumps(clf))
        assert_true(sp.issparse(clf.coef_))
        pred = clf.predict(X)
        assert_array_equal(pred, Y)

    # def test_class_weights(self):
    #     # Test class weights.
    #     X = np.array([[-1.0, -1.0], [-1.0, 0], [-.8, -1.0],
    #                   [1.0, 1.0], [1.0, 0.0]])
    #     y = [1, 1, 1, -1, -1]

    #     clf = self.factory(alpha=0.1, n_iter=1000, fit_intercept=False,
    #                        class_weight=None)
    #     clf.fit(X, y)
    #     assert_array_equal(clf.predict([[0.2, -1.0]]), np.array([1]))

    #     # we give a small weights to class 1
    #     clf = self.factory(alpha=0.1, n_iter=1000, fit_intercept=False,
    #                        class_weight={1: 0.001})
    #     clf.fit(X, y)

    #     # now the hyperplane should rotate clock-wise and
    #     # the prediction on this point should shift
    #     assert_array_equal(clf.predict([[0.2, -1.0]]), np.array([-1]))

    # def test_equal_class_weight(self):
    #     # Test if equal class weights approx. equals no class weights.
    #     X = [[1, 0], [1, 0], [0, 1], [0, 1]]
    #     y = [0, 0, 1, 1]
    #     clf = self.factory(alpha=0.1, n_iter=1000, class_weight=None)
    #     clf.fit(X, y)

    #     X = [[1, 0], [0, 1]]
    #     y = [0, 1]
    #     clf_weighted = self.factory(alpha=0.1, n_iter=1000,
    #                                 class_weight={0: 0.5, 1: 0.5})
    #     clf_weighted.fit(X, y)

    #     # should be similar up to some epsilon due to learning rate schedule
    #     assert_almost_equal(clf.coef_, clf_weighted.coef_, decimal=2)

    # @raises(ValueError)
    # def test_wrong_class_weight_label(self):
    #     # ValueError due to not existing class label.
    #     clf = self.factory(alpha=0.1, n_iter=1000, class_weight={0: 0.5})
    #     clf.fit(X, Y)

    # @raises(ValueError)
    # def test_wrong_class_weight_format(self):
    #     # ValueError due to wrong class_weight argument type.
    #     clf = self.factory(alpha=0.1, n_iter=1000, class_weight=[0.5])
    #     clf.fit(X, Y)

    # def test_weights_multiplied(self):
    #     # Tests that class_weight and sample_weight are multiplicative
    #     class_weights = {1: .6, 2: .3}
    #     rng = np.random.RandomState(0)
    #     sample_weights = rng.random_sample(Y4.shape[0])
    #     multiplied_together = np.copy(sample_weights)
    #     multiplied_together[Y4 == 1] *= class_weights[1]
    #     multiplied_together[Y4 == 2] *= class_weights[2]

    #     clf1 = self.factory(alpha=0.1, n_iter=20, class_weight=class_weights)
    #     clf2 = self.factory(alpha=0.1, n_iter=20)

    #     clf1.fit(X4, Y4, sample_weight=sample_weights)
    #     clf2.fit(X4, Y4, sample_weight=multiplied_together)

    #     assert_almost_equal(clf1.coef_, clf2.coef_)

    # def test_balanced_weight(self):
    #     # Test class weights for imbalanced data"""
    #     # compute reference metrics on iris dataset that is quite balanced by
    #     # default
    #     X, y = iris.data, iris.target
    #     X = scale(X)
    #     idx = np.arange(X.shape[0])
    #     rng = np.random.RandomState(6)
    #     rng.shuffle(idx)
    #     X = X[idx]
    #     y = y[idx]
    #     clf = self.factory(alpha=0.0001, n_iter=1000,
    #                        class_weight=None, shuffle=False).fit(X, y)
    #     assert_almost_equal(metrics.f1_score(y, clf.predict(X), average='weighted'), 0.96,
    #                         decimal=1)

    #     # make the same prediction using balanced class_weight
    #     clf_balanced = self.factory(alpha=0.0001, n_iter=1000,
    #                                 class_weight="balanced",
    #                                 shuffle=False).fit(X, y)
    #     assert_almost_equal(metrics.f1_score(y, clf_balanced.predict(X), average='weighted'), 0.96,
    #                         decimal=1)

    #     # Make sure that in the balanced case it does not change anything
    #     # to use "balanced"
    #     assert_array_almost_equal(clf.coef_, clf_balanced.coef_, 6)

    #     # build an very very imbalanced dataset out of iris data
    #     X_0 = X[y == 0, :]
    #     y_0 = y[y == 0]

    #     X_imbalanced = np.vstack([X] + [X_0] * 10)
    #     y_imbalanced = np.concatenate([y] + [y_0] * 10)

    #     # fit a model on the imbalanced data without class weight info
    #     clf = self.factory(n_iter=1000, class_weight=None, shuffle=False)
    #     clf.fit(X_imbalanced, y_imbalanced)
    #     y_pred = clf.predict(X)
    #     assert_less(metrics.f1_score(y, y_pred, average='weighted'), 0.96)

    #     # fit a model with balanced class_weight enabled
    #     clf = self.factory(n_iter=1000, class_weight="balanced", shuffle=False)
    #     clf.fit(X_imbalanced, y_imbalanced)
    #     y_pred = clf.predict(X)
    #     assert_greater(metrics.f1_score(y, y_pred, average='weighted'), 0.96)

    #     # fit another using a fit parameter override
    #     clf = self.factory(n_iter=1000, class_weight="balanced", shuffle=False)
    #     clf.fit(X_imbalanced, y_imbalanced)
    #     y_pred = clf.predict(X)
    #     assert_greater(metrics.f1_score(y, y_pred, average='weighted'), 0.96)

    def test_sample_weights(self):
        # Test weights on individual samples
        X = np.array([[-1.0, -1.0], [-1.0, 0], [-.8, -1.0],
                      [1.0, 1.0], [1.0, 0.0]])
        y = [1, 1, 1, -1, -1]

        clf = self.factory(alpha=0.1, n_iter=1000, fit_intercept=False)
        clf.fit(X, y)
        assert_array_equal(clf.predict([[0.2, -1.0]]), np.array([1]))

        # we give a small weights to class 1
        clf.fit(X, y, sample_weight=[0.001] * 3 + [1] * 2)

        # now the hyperplane should rotate clock-wise and
        # the prediction on this point should shift
        assert_array_equal(clf.predict([[0.2, -1.0]]), np.array([-1]))

    @raises(ValueError)
    def test_wrong_sample_weights(self):
        # Test if ValueError is raised if sample_weight has wrong shape
        clf = self.factory(alpha=0.1, n_iter=1000, fit_intercept=False)
        # provided sample_weight too long
        clf.fit(X, Y, sample_weight=np.arange(7))

    # No longer an error as we allow new classes.
    # @raises(ValueError)
    # def test_partial_fit_exception(self):
    #     clf = self.factory(alpha=0.01)
    #     # classes was not specified
    #     clf.partial_fit(X3, Y3)

    def test_partial_fit_binary(self):
        third = X.shape[0] // 3
        clf = self.factory(alpha=0.01)
        classes = np.unique(Y)

        clf.partial_fit(X[:third], Y[:third])
        assert_equal(clf.coef_.shape, (1, X.shape[1]))
        assert_equal(clf.intercept_.shape, (1,))
        assert_equal(clf.decision_function([[0, 0]]).shape, (1, ))
        id1 = id(clf.coef_.data)

        clf.partial_fit(X[third:], Y[third:])
        id2 = id(clf.coef_.data)
        # check that coef_ haven't been re-allocated
        assert_true(id1, id2)

        y_pred = clf.predict(T)
        assert_array_equal(y_pred, true_result)

    def test_partial_fit_multiclass(self):
        third = X2.shape[0] // 3
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2[:third], Y2[:third])
        assert_equal(clf.coef_.shape, (1, X2.shape[1]))
        assert_equal(clf.intercept_.shape, (1,))
        assert_equal(clf.decision_function([[0, 0]]).shape, (1,))
        id1 = id(clf.coef_.data)

        sixth = 2*third
        clf.partial_fit(X2[third:sixth], Y2[third:sixth])
        assert_equal(clf.coef_.shape, (2, X2.shape[1]))
        assert_equal(clf.intercept_.shape, (2,))
        assert_equal(clf.decision_function([[0, 0]]).shape, (1,2))
        id2 = id(clf.coef_.data)
        # check that coef_ haven't been re-allocated
        assert_true(id1, id2)

        clf.partial_fit(X2[sixth:], Y2[sixth:])
        assert_equal(clf.coef_.shape, (3, X2.shape[1]))
        assert_equal(clf.intercept_.shape, (3,))
        assert_equal(clf.decision_function([[0, 0]]).shape, (1,3))
        id3 = id(clf.coef_.data)
        # check that coef_ haven't been re-allocated
        assert_true(id1, id3)

    def test_partial_fit_multiclass_delete_new_class(self):
        # Train with training data containing only 2 classes(d1), then add
        # training data with the third class.
        # Check that for an example in d1 the label before the third class was
        # added is the same as the label after the third class is removed.
        sixth = 2*(X2.shape[0] // 3)
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2[:sixth], Y2[:sixth])
        label1, score1 = clf.predict_and_score(X2[0])
        clf.partial_fit(X2[sixth:], Y2[sixth:])
        assert_equal(clf.delete_class(Y2[sixth]), True)
        label2, score2 = clf.predict_and_score(X2[0])
        assert_equal(label1, label2)

    def test_partial_fit_multiclass_delete_old_class(self):
        # Train with training data containing only 2 classes(d1), then deletes
        # the second class. Check that the prediction for an example for the
        # second class is now the first class.
        third = X2.shape[0] // 3
        sixth = 2 * third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2[:sixth], Y2[:sixth])
        label1, score1 = clf.predict_and_score(X2[third])
        assert_equal(clf.delete_class(Y2[third]), True)
        label2, score2 = clf.predict_and_score(X2[third])
        assert_not_equal(label1, label2)

    def test_partial_fit_multiclass_delete_one_class(self):
        # Train with training data containing only one classes, and test
        # deleting that class.
        third = X2.shape[0] // 3
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2[:third], Y2[:third])
        assert_equal(clf.delete_class(Y2[0]), True)

    def test_partial_fit_multiclass_delete_wrong_class(self):
        # Test that deleting a class for empty model returns False. Also test
        # that when trained on two class, and when delete is called with the
        # third class, it returns false.
        # deleting that class.
        sixth = 2 * (X2.shape[0] // 3)
        clf = self.factory(alpha=0.01)
        assert_equal(clf.delete_class(Y2[0]), False)

        clf.partial_fit(X2[:sixth], Y2[:sixth])
        assert_equal(clf.delete_class(Y2[sixth]), False)

    def test_partial_fit_multiclass_predict_correct(self):
        third = X2.shape[0] // 3
        sixth = 2*third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2[:third], Y2[:third])

        predicted_label = clf.predict_and_score(X2[0])[0]
        assert_equal(predicted_label, Y2[0])

        clf.partial_fit(X2[third:sixth], Y2[third:sixth])
        predicted_label = clf.predict_and_score(X2[third])[0]
        assert_equal(predicted_label, Y2[third])

        clf.partial_fit(X2[sixth:], Y2[sixth:])
        predicted_label = clf.predict_and_score(X2[third])[0]
        assert_equal(predicted_label, Y2[third])

        predicted_label = clf.predict_and_score(X2[sixth])[0]
        assert_equal(predicted_label, Y2[sixth])

    def test_partial_fit_multiclass_predict_multiple(self):
        third = X2.shape[0] // 3
        sixth = 2*third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2, Y2)
        (classes, scores) = clf.predict_and_score_multiple(X2[0], 3)
        assert_equal(classes.size, 3)
        assert_equal(scores.size, 3)
        assert_greater_equal(scores[0], scores[1])
        assert_greater_equal(scores[1], scores[2])

    def test_partial_fit_multiclass_predict_multiple_less_classes(self):
        third = X2.shape[0] // 3
        sixth = 2*third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2, Y2)
        (classes, scores) = clf.predict_and_score_multiple(X2[0], 2)
        assert_equal(classes.size, 2)
        assert_equal(scores.size, 2)
        assert_greater_equal(scores[0], scores[1])
        assert_array_equal(classes[0], Y2[0])

    def test_partial_fit_multiclass_predict_multiple_too_many_classes(self):
        third = X2.shape[0] // 3
        sixth = 2*third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2, Y2)
        (classes, scores) = clf.predict_and_score_multiple(X2[0], 4)
        assert_equal(classes.size, 3)
        assert_equal(scores.size, 3)
        assert_greater_equal(scores[0], scores[1])
        assert_greater_equal(scores[1], scores[2])

    def test_partial_fit_multiclass_predict_multiple_zero_classes(self):
        third = X2.shape[0] // 3
        sixth = 2*third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2, Y2)
        (classes, scores) = clf.predict_and_score_multiple(X2[0], 0)
        assert_equal(classes, None)
        assert_equal(scores, None)

    def test_partial_fit_multiclass_predict_multiple_one_classes(self):
        third = X2.shape[0] // 3
        sixth = 2*third
        clf = self.factory(alpha=0.01)

        clf.partial_fit(X2, Y2)
        (classes, scores) = clf.predict_and_score_multiple(X2[0], 1)
        print(classes)
        assert_equal(classes, Y2[1])

    def test_partial_fit_multiclass_average(self):
        third = X2.shape[0] // 3
        clf = self.factory(alpha=0.01, average=X2.shape[0])
        classes = np.unique(Y2)

        clf.partial_fit(X2[:third], Y2[:third])
        assert_equal(clf.coef_.shape, (1, X2.shape[1]))
        assert_equal(clf.intercept_.shape, (1,))

        clf.partial_fit(X2[third:], Y2[third:])
        assert_equal(clf.coef_.shape, (3, X2.shape[1]))
        assert_equal(clf.intercept_.shape, (3,))

    def test_fit_then_partial_fit(self):
        # Partial_fit should work after initial fit in the multiclass case.
        # Non-regression test for #2496; fit would previously produce a
        # Fortran-ordered coef_ that subsequent partial_fit couldn't handle.
        clf = self.factory()
        clf.fit(X2, Y2)
        clf.partial_fit(X2, Y2)     # no exception here

    def _test_partial_fit_equal_fit(self, lr):
        for X_, Y_, T_ in ((X, Y, T), (X2, Y2, T2)):
            clf = self.factory(alpha=0.01, eta0=0.01, n_iter=2,
                               learning_rate=lr, shuffle=False)
            clf.fit(X_, Y_)
            y_pred = clf.decision_function(T_)
            t = clf.t_

            classes = np.unique(Y_)
            clf = self.factory(alpha=0.01, eta0=0.01, learning_rate=lr,
                               shuffle=False)
            for i in range(2):
                clf.partial_fit(X_, Y_)
            y_pred2 = clf.decision_function(T_)

            assert_equal(clf.t_, t)
            assert_array_almost_equal(y_pred, y_pred2, decimal=2)

    def test_partial_fit_equal_fit_constant(self):
        self._test_partial_fit_equal_fit("constant")

    def test_partial_fit_equal_fit_optimal(self):
        self._test_partial_fit_equal_fit("optimal")

    def test_partial_fit_equal_fit_invscaling(self):
        self._test_partial_fit_equal_fit("invscaling")

    def test_regression_losses(self):
        clf = self.factory(alpha=0.01, learning_rate="constant",
                           eta0=0.1, loss="epsilon_insensitive")
        clf.fit(X, Y)
        assert_equal(1.0, np.mean(clf.predict(X) == Y))

        clf = self.factory(alpha=0.01, learning_rate="constant",
                           eta0=0.1, loss="squared_epsilon_insensitive")
        clf.fit(X, Y)
        assert_equal(1.0, np.mean(clf.predict(X) == Y))

        clf = self.factory(alpha=0.01, loss="huber")
        clf.fit(X, Y)
        assert_equal(1.0, np.mean(clf.predict(X) == Y))

        clf = self.factory(alpha=0.01, learning_rate="constant", eta0=0.01,
                           loss="squared_loss")
        clf.fit(X, Y)
        assert_equal(1.0, np.mean(clf.predict(X) == Y))

    def test_warm_start_multiclass(self):
        self._test_warm_start(X2, Y2, "optimal")

    def test_multiple_fit(self):
        # Test multiple calls of fit w/ different shaped inputs.
        clf = self.factory(alpha=0.01, n_iter=5,
                           shuffle=False)
        clf.fit(X, Y)
        assert_true(hasattr(clf, "coef_"))

        # Non-regression test: try fitting with a different label set.
        y = [["ham", "spam"][i] for i in LabelEncoder().fit_transform(Y)]
        clf.fit(X[:, :-1], y)


class SparseSGDClassifierTestCase(DenseSGDClassifierTestCase):
    """Run exactly the same tests using the sparse representation variant"""

    factory_class = SparseSGDClassifier



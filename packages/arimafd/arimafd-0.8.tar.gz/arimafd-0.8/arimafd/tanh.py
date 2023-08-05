 """
 This module describe methods which allow use ch
 """
import numpy as np
from numpy import linalg
import pandas as pd
from sympy import diff, symbols, sympify, Symbol, poly
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from time import time




#=============================================================
def projection(w,circle=1.01):
    """
    Function for projection weights  
    """
    w=w[::-1] # due to using in function body
    # find coeff of poly if we have roots 
    def c_find(roots):
        x = Symbol('x')
        whole =1
        for root in roots:
            whole *=(x-root)
    #     print('f(x) =',whole.expand())
        p = poly(whole, x)
        return np.array(p.all_coeffs()).astype(float)
    
    roots = np.roots(w)
    l1 = linalg.norm(roots)
    #print(l1)

    if l1 < circle:
        print('Projection')
        scale = circle/l1
        new_roots = roots*scale
        new_w=c_find(new_roots)[::-1]
        return new_w
    else:
        return w[::-1]
 #================================================================

          
class online_tanh:
    """
    
    
    Logistic Regression (aka logit, MaxEnt) classifier.

    In the multiclass case, the training algorithm uses the one-vs-rest (OvR)
    scheme if the 'multi_class' option is set to 'ovr', and uses the
    cross-entropy loss if the 'multi_class' option is set to 'multinomial'.
    (Currently the 'multinomial' option is supported only by the 'lbfgs',
    'sag', 'saga' and 'newton-cg' solvers.)

    This class implements regularized logistic regression using the
    'liblinear' library, 'newton-cg', 'sag', 'saga' and 'lbfgs' solvers. **Note
    that regularization is applied by default**. It can handle both dense
    and sparse input. Use C-ordered arrays or CSR matrices containing 64-bit
    floats for optimal performance; any other input format will be converted
    (and copied).

    The 'newton-cg', 'sag', and 'lbfgs' solvers support only L2 regularization
    with primal formulation, or no regularization. The 'liblinear' solver
    supports both L1 and L2 regularization, with a dual formulation only for
    the L2 penalty. The Elastic-Net regularization is only supported by the
    'saga' solver.

    Read more in the :ref:`User Guide <logistic_regression>`.

    Parameters
    ----------
    penalty : str, 'l1', 'l2', 'elasticnet' or 'none', optional (default='l2')
        Used to specify the norm used in the penalization. The 'newton-cg',
        'sag' and 'lbfgs' solvers support only l2 penalties. 'elasticnet' is
        only supported by the 'saga' solver. If 'none' (not supported by the
        liblinear solver), no regularization is applied.

        .. versionadded:: 0.19
           l1 penalty with SAGA solver (allowing 'multinomial' + L1)

    dual : bool, optional (default=False)
        Dual or primal formulation. Dual formulation is only implemented for
        l2 penalty with liblinear solver. Prefer dual=False when
        n_samples > n_features.

    tol : float, optional (default=1e-4)
        Tolerance for stopping criteria.

    C : float, optional (default=1.0)
        Inverse of regularization strength; must be a positive float.
        Like in support vector machines, smaller values specify stronger
        regularization.

    fit_intercept : bool, optional (default=True)
        Specifies if a constant (a.k.a. bias or intercept) should be
        added to the decision function.

    intercept_scaling : float, optional (default=1)
        Useful only when the solver 'liblinear' is used
        and self.fit_intercept is set to True. In this case, x becomes
        [x, self.intercept_scaling],
        i.e. a "synthetic" feature with constant value equal to
        intercept_scaling is appended to the instance vector.
        The intercept becomes ``intercept_scaling * synthetic_feature_weight``.

        Note! the synthetic feature weight is subject to l1/l2 regularization
        as all other features.
        To lessen the effect of regularization on synthetic feature weight
        (and therefore on the intercept) intercept_scaling has to be increased.

    class_weight : dict or 'balanced', optional (default=None)
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``.

        Note that these weights will be multiplied with sample_weight (passed
        through the fit method) if sample_weight is specified.

        .. versionadded:: 0.17
           *class_weight='balanced'*

    random_state : int, RandomState instance or None, optional (default=None)
        The seed of the pseudo random number generator to use when shuffling
        the data.  If int, random_state is the seed used by the random number
        generator; If RandomState instance, random_state is the random number
        generator; If None, the random number generator is the RandomState
        instance used by `np.random`. Used when ``solver`` == 'sag' or
        'liblinear'.

    solver : str, {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'},              optional (default='liblinear').

        Algorithm to use in the optimization problem.

        - For small datasets, 'liblinear' is a good choice, whereas 'sag' and
          'saga' are faster for large ones.
        - For multiclass problems, only 'newton-cg', 'sag', 'saga' and 'lbfgs'
          handle multinomial loss; 'liblinear' is limited to one-versus-rest
          schemes.
        - 'newton-cg', 'lbfgs', 'sag' and 'saga' handle L2 or no penalty
        - 'liblinear' and 'saga' also handle L1 penalty
        - 'saga' also supports 'elasticnet' penalty
        - 'liblinear' does not handle no penalty

        Note that 'sag' and 'saga' fast convergence is only guaranteed on
        features with approximately the same scale. You can
        preprocess the data with a scaler from sklearn.preprocessing.

        .. versionadded:: 0.17
           Stochastic Average Gradient descent solver.
        .. versionadded:: 0.19
           SAGA solver.
        .. versionchanged:: 0.20
            Default will change from 'liblinear' to 'lbfgs' in 0.22.

    max_iter : int, optional (default=100)
        Maximum number of iterations taken for the solvers to converge.

    multi_class : str, {'ovr', 'multinomial', 'auto'}, optional (default='ovr')
        If the option chosen is 'ovr', then a binary problem is fit for each
        label. For 'multinomial' the loss minimised is the multinomial loss fit
        across the entire probability distribution, *even when the data is
        binary*. 'multinomial' is unavailable when solver='liblinear'.
        'auto' selects 'ovr' if the data is binary, or if solver='liblinear',
        and otherwise selects 'multinomial'.

        .. versionadded:: 0.18
           Stochastic Average Gradient descent solver for 'multinomial' case.
        .. versionchanged:: 0.20
            Default will change from 'ovr' to 'auto' in 0.22.

    verbose : int, optional (default=0)
        For the liblinear and lbfgs solvers set verbose to any positive
        number for verbosity.

    warm_start : bool, optional (default=False)
        When set to True, reuse the solution of the previous call to fit as
        initialization, otherwise, just erase the previous solution.
        Useless for liblinear solver. See :term:`the Glossary <warm_start>`.

        .. versionadded:: 0.17
           *warm_start* to support *lbfgs*, *newton-cg*, *sag*, *saga* solvers.

    n_jobs : int or None, optional (default=None)
        Number of CPU cores used when parallelizing over classes if
        multi_class='ovr'". This parameter is ignored when the ``solver`` is
        set to 'liblinear' regardless of whether 'multi_class' is specified or
        not. ``None`` means 1 unless in a :obj:`joblib.parallel_backend`
        context. ``-1`` means using all processors.
        See :term:`Glossary <n_jobs>` for more details.

    l1_ratio : float or None, optional (default=None)
        The Elastic-Net mixing parameter, with ``0 <= l1_ratio <= 1``. Only
        used if ``penalty='elasticnet'`. Setting ``l1_ratio=0`` is equivalent
        to using ``penalty='l2'``, while setting ``l1_ratio=1`` is equivalent
        to using ``penalty='l1'``. For ``0 < l1_ratio <1``, the penalty is a
        combination of L1 and L2.

    Attributes
    ----------

    classes_ : array, shape (n_classes, )
        A list of class labels known to the classifier.

    coef_ : array, shape (1, n_features) or (n_classes, n_features)
        Coefficient of the features in the decision function.

        `coef_` is of shape (1, n_features) when the given problem is binary.
        In particular, when `multi_class='multinomial'`, `coef_` corresponds
        to outcome 1 (True) and `-coef_` corresponds to outcome 0 (False).

    intercept_ : array, shape (1,) or (n_classes,)
        Intercept (a.k.a. bias) added to the decision function.

        If `fit_intercept` is set to False, the intercept is set to zero.
        `intercept_` is of shape (1,) when the given problem is binary.
        In particular, when `multi_class='multinomial'`, `intercept_`
        corresponds to outcome 1 (True) and `-intercept_` corresponds to
        outcome 0 (False).

    n_iter_ : array, shape (n_classes,) or (1, )
        Actual number of iterations for all classes. If binary or multinomial,
        it returns only 1 element. For liblinear solver, only the maximum
        number of iteration across all classes is given.

        .. versionchanged:: 0.20

            In SciPy <= 1.0.0 the number of lbfgs iterations may exceed
            ``max_iter``. ``n_iter_`` will now report at most ``max_iter``.

    Examples
    --------
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.linear_model import LogisticRegression
    >>> X, y = load_iris(return_X_y=True)
    >>> clf = LogisticRegression(random_state=0, solver='lbfgs',
    ...                          multi_class='multinomial').fit(X, y)
    >>> clf.predict(X[:2, :])
    array([0, 0])
    >>> clf.predict_proba(X[:2, :]) # doctest: +ELLIPSIS
    array([[9.8...e-01, 1.8...e-02, 1.4...e-08],
           [9.7...e-01, 2.8...e-02, ...e-08]])
    >>> clf.score(X, y)
    0.97...

    See also
    --------
    SGDClassifier : incrementally trained logistic regression (when given
        the parameter ``loss="log"``).
    LogisticRegressionCV : Logistic regression with built-in cross validation

    Notes
    -----
    The underlying C implementation uses a random number generator to
    select features when fitting the model. It is thus not uncommon,
    to have slightly different results for the same input data. If
    that happens, try with a smaller tol parameter.

    Predict output may not match that of standalone liblinear in certain
    cases. See :ref:`differences from liblinear <liblinear_differences>`
    in the narrative documentation.

    References
    ----------

    LIBLINEAR -- A Library for Large Linear Classification
        https://www.csie.ntu.edu.tw/~cjlin/liblinear/

    SAG -- Mark Schmidt, Nicolas Le Roux, and Francis Bach
        Minimizing Finite Sums with the Stochastic Average Gradient
        https://hal.inria.fr/hal-00860051/document

    SAGA -- Defazio, A., Bach F. & Lacoste-Julien S. (2014).
        SAGA: A Fast Incremental Gradient Method With Support
        for Non-Strongly Convex Composite Objectives
        https://arxiv.org/abs/1407.0202

    Hsiang-Fu Yu, Fang-Lan Huang, Chih-Jen Lin (2011). Dual csoordinate descent
        methods for logistic regression and maximum entropy models.
        Machine Learning 85(1-2):41-75.
        https://www.csie.ntu.edu.tw/~cjlin/papers/maxent_dual.pdf
       При каждом предикте точки в self.data и self.predict записываеются
    """
    def __init__(self, order=4, lrate=0.001, random_state=42, soft_grad=False,project=True):
        self.soft_grad = soft_grad
        self.order=order
        self.lrate=lrate
        self.random_state=random_state
        self.project = project
        
        if soft_grad:
            def fun_w(i):
                return 1/ np.sqrt(i+1)  #намерено опустил  член -order, из-за небольшой погрешности допущения
        else:
            def fun_w(i):
                return 1
        self.fun_w = fun_w
    
    def fit(self, data, init_w=None):
        data=np.array(data)
        self.data=data
        np.random.seed(self.random_state)
        self.pred = np.zeros(data.shape[0] + 1)*np.nan
        self.w = np.random.rand(self.order+1)*0.01 if init_w is None else init_w.copy()
        self.ww=pd.DataFrame([self.w])
        self.diff=np.zeros(len(self.w))
        # create pandas diffrent of w 
        self.dif_w = pd.DataFrame([self.w])
        for i in range(self.order, data.shape[0]):
            self.pred[i] = self.w[:-1] @ data[i-self.order:i] + self.w[-1]          
            self.diff[:-1]= np.tanh(self.pred[i] - data[i])*data[i-self.order:i]
            self.diff[-1] = np.tanh(self.pred[i] - data[i])# свободный член
            self.w -= self.lrate * self.diff * self.fun_w(i)
            
            if self.project:
                self.w = projection(self.w)
            self.ww=self.ww.append([self.w], ignore_index=True)
            self.dif_w = self.dif_w.append([self.diff], ignore_index=True)
        self.iii=i
        # реальные предсказания 
        # это нужно для дальнейшей работы алгоритма: 1 точка
        self.pred[-1]=self.w[:-1] @ data[-self.order:] + self.w[-1]                
    
    def predict(self, point_get=None, predict_size=1,return_predict=True):
        """
        пожалуйста в point get только одну точечк запишите 
        """
        # часть отвечающая за онлайн
        if point_get is not None:
            self.data=np.append(self.data,point_get)            
            self.diff[:-1]= np.tanh(self.pred[-1] - self.data[-1])*self.data[-self.order-1:-1]
            self.diff[-1] = np.tanh(self.pred[-1] - self.data[-1])# свободный член
            self.w -= self.lrate * self.diff * self.fun_w(self.iii)
            
            
            self.ww=self.ww.append([self.w], ignore_index=True)
            
            self.pred=np.append(self.pred,np.nan)
            self.dif_w = self.dif_w.append([self.diff], ignore_index=True)
            self.pred[-1]=self.w[:-1] @ self.data[-self.order:] + self.w[-1]

            
                    
        if predict_size > 1:
            data_p=np.append(self.data[-self.order:],np.zeros(predict_size)*np.nan)
            
            for i in range(self.order,self.order+predict_size):
                data_p[i]=self.w[:-1] @ data_p[i-self.order:i] + self.w[-1]
            if return_predict:
                return data_p[self.order:]
        elif predict_size==1 and return_predict:
            return self.pred[-1]



def auto(data1,ar_order=None,return_tensor='norm'):
    if ar_order is None:
        ar_order=int(len(data1)/3)
    
    ss = StandardScaler()
    mms = MinMaxScaler()
    
    data1=ss.fit_transform(data1.copy())
    
    tensor = np.zeros((data1.shape[0]-ar_order,data1.shape[1],ar_order+1))
    tensor_scale = np.zeros((data1.shape[0]-ar_order,data1.shape[1],ar_order+1))
    # tensor1 = np.zeros((data1.shape[0]-ar_order,data1.shape[1],ar_order+1))
    j=0
    for i in range(data1.shape[1]):
        t1=time()
        kkk=0

        diffr=diff_integ([1])
        dif = diffr.fit_transform(data1[:,i])

        model=online_tanh(ar_order)
        model.fit(dif)
        t2=time()
        print('Time seconds:', t2-t1)

        tensor[:,i,:] = model.dif_w.values
        tensor_scale[:,i,:] = mms.fit_transform(np.abs(model.dif_w.values.ravel()).reshape(-1,1)).reshape(tensor_scale[:,i,:].shape)
    if return_tensor=='both':
        return tensor,tensor_scale
    elif return_tensor=='scale':
        return tensor_scale
    elif return_tensor=='norm':
        return tensor


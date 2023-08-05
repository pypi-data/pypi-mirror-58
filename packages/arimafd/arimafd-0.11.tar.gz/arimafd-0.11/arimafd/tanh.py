import numpy as np
from numpy import linalg
import pandas as pd
from sympy import diff, symbols, sympify, Symbol, poly
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from time import time
from diff_integ import diff_integ
from find_best_model import find_best_model

#=============================================================
def projection(w,circle=1.01):
    """
    Function for projection weights
    
    Parameters
    ----------
    w : array-like, shape (n_weights,)
        List of initial weights, where n_weights is the number of weights 

    Returns
    -------
    new_w : array-like, shape (n_weights,)
        List of weights resolved solution area,
        where n_weights is the number of weights.

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
    def __init__(self, order=4, lrate=0.001, random_state=42, soft_grad=False,project=True):
        """
                A class for detecting outliers based on tracking changes
        in the weights of an autoregressive model with stochastic gradient
        descent and log-cosh loss function

        Parameters
        ----------
        order : array-like, shape (default=4)
            Order of autoregression
            
        lrate : float
            Value of gradint descent rate
        
        random_state : int, (default=42)
            Random_state is the random number generator

        soft_grad, optional (default=False)
            Rate of gradient descent is redused with every iteration
            
        project, optional (default=True)
            If True, make projection on resolved solution

        Returns
        -------
        self : object

        Examples
        --------
        >>> import arimafd as oa
        >>> pr = oa.online_tanh()
        >>> my_array=[1,2,3,4,5]
        >>> pr.fit(my_array)
        >>> pr.predict(predict_size=4)
        array([0.13778082, 0.11579774, 0.08165416, 0.0298824 ])
        """
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
        """
        Fit the AR model according to the given historical data. 
        It will be better if data represent normal operation mode
        
        
        Parameters
        ----------
        data : array-like, shape (n_samples,)
            Training data, where n_samples is the number of samples

        init_w : array-like, shape (n_weight,), (default=None)
            Initial array of weights, where n_weight is the number of weights
            If None the weights are initialized randomly

        Returns
        -------
        self : object
        """
        
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
        Make forecasting series from data to predict_size points
       
        Parameters
        ----------
        point_get : float (default=None)
            Add new for next iteration of stochastic gradiend descent
        
        predict_size: float
            The number of out of sample forecasts from the end of the sample
            
        return_predict, optional (default=True)
            Returns array of forecasting values

        Returns
        -------
        If return_diff = True: data_new : array-like, shape (n_samples - sum_seasons,) 
            where sum_seasons is sum of all lags
        
        self : object           
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
    """
    Generation tensor of weights for outlier detection
    
    Parameters
    ----------
    ar_order : float (default=None)
        Order of auoregression
    return_tensor : str; 'norm', 'scale', 'both'
        If 'norm' return single tensor of weight 
        If 'scale' return min_max scaled tensor of weight
        If 'both' return both of tensors of weight

    Returns
    -------
    tensor : array-like, shape (n_samples,n_features,ar_order)
        Tensor of weights (see higher for scale) where 
        n_samples - number of samples
        n_features - number of features
        ar_order - number of weights
    """
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


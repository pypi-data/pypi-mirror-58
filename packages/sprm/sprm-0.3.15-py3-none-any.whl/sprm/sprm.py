#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:56:12 2018

Module containing:
    
    Estimators
    ----------
    Sparse Partial Robust M Regression (SPRM)
    
    0.2: Ancillary functions moved to ._m_support_functions
         Plotting functions moved to .sprm_plot
    0.3: Sparse NIPALS (SNIPLS) estimator moved to .snipls.

Depends on robcent class for robustly centering and scaling data and on snipls 
class

@author: Sven Serneels, Ponalytics
"""

from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals
from sklearn.base import RegressorMixin,BaseEstimator,TransformerMixin
from sklearn.utils.metaestimators import _BaseComposition
from scipy.stats import norm, chi2
import copy
import numpy as np
import pandas as ps
import warnings
from .robcent import robcent
from .snipls import snipls
from ._m_support_functions import *

class sprm(_BaseComposition,BaseEstimator,TransformerMixin,RegressorMixin):
    
    """
    SPRM Sparse Partial Robust M Regression 
    
    Algorithm first outlined in: 
        Sparse partial robust M regression, 
        Irene Hoffmann, Sven Serneels, Peter Filzmoser, Christophe Croux, 
        Chemometrics and Intelligent Laboratory Systems, 149 (2015), 50-59. 
    
    Parameters:
    -----------
    eta: float. Sparsity parameter in [0,1)
    n_components: int, min 1. Note that if applied on data, n_components shall 
        take a value <= min(x_data.shape)
    fun: str, downweighting function. 'Hampel' (recommended), 'Fair' or 
                'Huber'
    probp1: float, probability cutoff for start of downweighting 
                 (e.g. 0.95)
    probp2: float, probability cutoff for start of steep downweighting 
                 (e.g. 0.975, only relevant if fun='Hampel')
    probp3: float, probability cutoff for start of outlier omission 
                 (e.g. 0.999, only relevant if fun='Hampel')
    centre: str, type of centring ('mean' or 'median' [recommended])
    scale: str, type of scaling ('std','mad' [recommended] or 'None')
    verbose: boolean, specifying verbose mode
    maxit: int, maximal number of iterations in M algorithm
    tol: float, tolerance for convergence in M algorithm 
    start_cutoff_mode: str, values:
        'specific' will set starting value cutoffs specific to X and y (preferred); 
        any other value will set X and y stating cutoffs identically. 
        The latter yields identical results to the SPRM R implementation available from
        CRAN.
    start_X_init: str, values:
        'pcapp' will include a PCA/broken stick projection to 
                calculate the staring weights, else just based on X;
        any other value will calculate the X starting values based on the X
                matrix itself. This is less stable for very flat data (p >> n), 
                yet yields identical results to the SPRM R implementation 
                available from CRAN.   
    colums (def false): Either boolean or list
        if False, no column names supplied 
        if a list (will only take length x_data.shape[1]), the column names of 
            the x_data supplied in this list, will be printed in verbose mode
    copy (def True): boolean, whether to copy data
        Note: copy not yet aligned with sklearn def  
    
    """
    
    def __init__(self,n_components=1,eta=.5,fun='Hampel',probp1=0.95
                 ,probp2=0.975,probp3=0.999,centre='median',scale='mad'
                 ,verbose=True,maxit=100,tol=0.01,start_cutoff_mode='specific'
                 ,start_X_init='pcapp',columns=False,copy=True):
        self.n_components = int(n_components) 
        self.eta = float(eta)
        self.fun = fun
        self.probp1 = probp1
        self.probp2 = probp2
        self.probp3 = probp3
        self.centre = centre
        self.scale = scale
        self.verbose = verbose
        self.maxit = maxit
        self.tol = tol
        self.start_cutoff_mode = start_cutoff_mode
        self.start_X_init = start_X_init
        self.columns = columns
        self.copy = copy
        self.probctx_ = 'irrelevant'
        self.probcty_ = 'irrelevant'
        self.hampelbx_ = 'irrelevant'
        self.hampelby__ = 'irrelevant'
        self.hampelrx_ = 'irrelevant'
        self.hampelry_ = 'irrelevant'
        self.non_zero_scale_vars_ = None
    

    def fit(self,X,y):
        if self.copy:
            self.X = copy.deepcopy(X)
            self.y = copy.deepcopy(y)
        (n,p) = X.shape
        if not(type(self.n_components)==int) | (self.n_components<=0):
            raise MyException("Number of components has to be a positive integer")
        if ((self.n_components > n) | (self.n_components > p)):
            raise MyException("The number of components is too large.")
        if (self.n_components <= 0):
            raise MyException("The number of components has to be positive.")
        if not(type(self.eta)==float):
            raise MyException("Sparsity parameter eta has to be a floating point number")
        if ((self.eta < 0) | (self.eta >= 1)):
            raise MyException("eta has to come from the interval [0,1)")
        if (not(self.fun in ("Hampel", "Huber", "Fair"))):
            raise MyException("Invalid weighting function. Choose Hampel, Huber or Fair for parameter fun.")
        if ((self.probp1 > 1) | (self.probp1 <= 0)):
            raise MyException("probp1 is a probability. Choose a value between 0 and 1")
        if (self.fun == "Hampel"):
            if (not((self.probp1 < self.probp2) & (self.probp2 < self.probp3) & (self.probp3 <= 1))):
                raise MyException("Wrong choise of parameters for Hampel function. Use 0<probp1<hampelp2<hampelp3<=1")
        ny = y.shape[0]
        if ny != n:
            raise MyException("Number of cases in y and X must be identical.")
        if len(y.shape) >1:
            y = np.array(y).reshape(-1).astype('float64')
            
        if type(X) == ps.core.frame.DataFrame:
            X = X.to_numpy()
        if type(y) in [ps.core.frame.DataFrame,ps.core.series.Series]:
            y = y.to_numpy().T.astype('float64')

        scaling = robcent(center=self.centre, scale=self.scale)
        Xs = scaling.fit(X).astype('float64')
        mX = scaling.col_loc_
        sX = scaling.col_sca_
        ys = scaling.fit(y).astype('float64')
        my = scaling.col_loc_
        sy = scaling.col_sca_
        setattr(self,"x_loc_",mX)
        setattr(self,"y_loc_",my)
        setattr(self,"x_sca_",sX)
        setattr(self,"y_sca_",sy)
        
        zero_scale = np.where(sX < 1e-5)[0]
        vars_to_keep = np.arange(0,p)
        if len(zero_scale) > 0:
            if type(self.columns) != bool:
                warntext = 'Zero scale variables with indices ' + str(self.columns[zero_scale]) + ' detected and removed'
            else:
                warntext = 'Zero scale variables with indices ' + str(zero_scale) + ' detected and removed'

            warnings.warn(warntext)
            vars_to_keep = np.setdiff1d(np.arange(0,p),zero_scale)
            Xs = Xs[:,vars_to_keep]
            X = X[:,vars_to_keep]
            sX = sX[vars_to_keep]
            if type(self.columns) != bool:
                self.columns = self.columns[vars_to_keep]
            p = len(vars_to_keep)
        
        self.non_zero_scale_vars_ = vars_to_keep


        if (self.start_X_init=='pcapp'):
            U, S, V = np.linalg.svd(Xs)
            spc = np.square(S)
            spc /= np.sum(spc)
            relcomp = max(np.where(spc - brokenstick(min(p,n))[:,0] <=0)[0][0],1)
            Urc = np.array(U[:,0:relcomp])
            Us = scaling.fit(Urc)
        else: 
            Us = Xs
        wx = np.sqrt(np.array(np.sum(np.square(Us),1),dtype=np.float64))
        wx = wx/np.median(wx)
        if [self.centre,self.scale]==['median','mad']:
            wy = np.array(abs(ys),dtype=np.float64)
        else:
            wy = (y - np.median(y))/(1.4826*np.median(abs(y-np.median(y))))
        self.probcty_ = norm.ppf(self.probp1)
        if self.start_cutoff_mode == 'specific':
            self.probctx_ = chi2.ppf(self.probp1,relcomp)
        else: 
            self.probctx_ = self.probcty_
        if (self.fun == "Fair"):
            wx = Fair(wx,self.probctx_)
            wy = Fair(wy,self.probcty_)
        if (self.fun == "Huber"):
            wx = Huber(wx,self.probctx_)
            wy = Huber(wy,self.probcty_)
        if (self.fun == "Hampel"):
            self.hampelby_ = norm.ppf(self.probp2)
            self.hampelry_ = norm.ppf(self.probp3)
            if self.start_cutoff_mode == 'specific':
                self.hampelbx_ = chi2.ppf(self.probp2,relcomp)
                self.hampelrx_ = chi2.ppf(self.probp3,relcomp)
            else: 
                self.hampelbx_ = self.hampelby_
                self.hampelrx_ = self.hampelry_
            wx = Hampel(wx,self.probctx_,self.hampelbx_,self.hampelrx_)
            wy = Hampel(wy,self.probcty_,self.hampelby_,self.hampelry_)
        wx = np.array(wx).reshape(-1)
        w = (wx*wy).astype("float64")
        if (w < 1e-06).any():
            w0 = np.where(w < 1e-06)[0]
            w[w0] = 1e-06
            we = np.array(w,dtype=np.float64)
        else:
            we = np.array(w,dtype=np.float64)
        wte = wx
        wye = wy
        WEmat = np.array([np.sqrt(we) for i in range(1,p+1)],ndmin=1).T    
        Xw = np.multiply(Xs,WEmat).astype("float64")
        yw = ys*np.sqrt(we)
        loops = 1
        rold = 1E-5
        difference = 1
        # Begin at iteration
        res_snipls = snipls(self.eta,self.n_components,
                            self.verbose,self.columns,'mean','None',
                            self.copy)
        while ((difference > self.tol) & (loops < self.maxit)):
            res_snipls.fit(Xw,yw)
            T = np.divide(res_snipls.x_scores_,WEmat[:,0:(self.n_components)])
            b = res_snipls.coef_
            yp = res_snipls.fitted_
            r = ys - yp
            if (len(r)/2 > np.sum(r == 0)):
                r = abs(r)/(1.4826 * np.median(abs(r)))
            else:
                r = abs(r)/(1.4826 * np.median(abs(r[r != 0])))
            scalet = self.scale
            if (scalet == "None"):
                scaling.set_params(scale = "mad") 
            dt = scaling.fit(T)
            wtn = np.sqrt(np.array(np.sum(np.square(dt),1),dtype=np.float64))
            wtn = wtn/np.median(wtn)
            wtn = wtn.reshape(-1)
            wye = r
            wte = wtn
            if (self.fun == "Fair"):
                wte = Fair(wtn,self.probctx_)
                wye = Fair(wye,self.probcty_)
            if (self.fun == "Huber"):
                wte = Huber(wtn,self.probctx_)
                wye = Huber(wye,self.probcty_)
            if (self.fun == "Hampel"):
                self.probctx_ = chi2.ppf(self.probp1,self.n_components)
                self.hampelbx_ = chi2.ppf(self.probp2,self.n_components)
                self.hampelrx_ = chi2.ppf(self.probp3,self.n_components)
                wte = Hampel(wtn,self.probctx_,self.hampelbx_,self.hampelrx_)
                wye = Hampel(wye,self.probcty_,self.hampelby_,self.hampelry_)
            b2sum = np.sum(np.power(b,2))    
            difference = abs(b2sum - rold)/rold
            rold = b2sum
            wte = np.array(wte).reshape(-1)
            we = (wye * wte).astype("float64")
            w0=[]
            if (any(we < 1e-06)):
                w0 = np.where(we < 1e-06)[0]
                we[w0] = 1e-06
                we = np.array(we,dtype=np.float64)
            if (len(w0) >= (n/2)):
                break
            WEmat = np.array([np.sqrt(we) for i in range(1,p+1)],ndmin=1).T    
            Xw = np.multiply(Xs,WEmat).astype("float64")
            yw = ys*np.sqrt(we)
            loops += 1
        if (difference > self.maxit):
            print("Warning: Method did not converge. The scaled difference between norms of the coefficient vectors is " + 
                  str(round(difference,4)))
        plotprec = False
        if plotprec:
            print(str(loops - 1))
        w = we
        w[w0] = 0
        wt = wte
        wt[w0] = 0
        wy = wye
        wy[w0] = 0
        P = res_snipls.x_loadings_
        W = res_snipls.x_weights_
        R = res_snipls.x_Rweights_
        Xrw = np.array(np.multiply(Xs,np.sqrt(WEmat)).astype("float64"))
        scaling.set_params(scale='None')
        Xrw = scaling.fit(Xrw) 
        T = Xs * R
        if self.verbose:
            print("Final Model: Variables retained for " + str(self.n_components) + " latent variables: \n" 
                 + str(res_snipls.colret_) + "\n")
        b_rescaled = np.multiply(np.reshape(sy/sX,(p,1)),b)
        yp_rescaled = np.array(X*b_rescaled).reshape(-1)
        if(self.centre == "mean"):
            intercept = np.mean(y - yp_rescaled)
        else:
            intercept = np.median(y - yp_rescaled)
        # This median calculation produces slightly different result in R and Py
        yfit = yp_rescaled + intercept    
        if (self.scale!="None"):
            if (self.centre == "mean"):
                b0 = np.mean(ys.astype("float64") - np.matmul(Xs.astype("float64"),b))
            else:
                b0 = np.median(np.array(ys.astype("float64") - np.matmul(Xs.astype("float64"),b)))
            # yfit2 = (np.matmul(Xrc.Xs.astype("float64"),b) + b0)*yrc.col_sca + yrc.col_loc
            # already more generally included
        else:
            if (self.centring == "mean"):
                intercept = np.mean(y - np.matmul(X,b))
            else:
                intercept = np.median(np.array(y - np.matmul(X,b)))
            # yfit = np.matmul(X,b) + intercept
        yfit = yfit.reshape(-1)    
        r = y - yfit
        setattr(self,"x_weights_",W)
        setattr(self,"x_loadings_",P)
        setattr(self,"C_",res_snipls.C_)
        setattr(self,"x_scores_",T)
        setattr(self,"coef_",b_rescaled)
        setattr(self,"intercept_",intercept)
        setattr(self,"coef_scaled_",b)
        setattr(self,"intercept_scaled_",b0)
        setattr(self,"residuals_",r)
        setattr(self,"x_ev_",res_snipls.x_ev_)
        setattr(self,"y_ev_",res_snipls.y_ev_)
        setattr(self,"fitted_",yfit)
        setattr(self,"x_Rweights_",R)
        setattr(self,"x_caseweights_",wte)
        setattr(self,"y_caseweights_",wye)
        setattr(self,"caseweights_",we)
        setattr(self,"colret_",res_snipls.colret_)
        setattr(self,'scaling',scaling)
        return(self)
        pass
    
        
    def predict(self,Xn):
        if type(Xn) == ps.core.frame.DataFrame:
            Xn = Xn.to_numpy()
        (n,p) = Xn.shape
        if p!= self.X.shape[1]:
            raise(ValueError('New data must have seame number of columns as the ones the model has been trained with'))
        Xn = Xn[:,self.non_zero_scale_vars_]
        return(np.matmul(Xn,self.coef_) + self.intercept_)
        
    def transform(self,Xn):
        if type(Xn) == ps.core.frame.DataFrame:
            Xn = Xn.to_numpy()
        (n,p) = Xn.shape
        if p!= self.X.shape[1]:
            raise(ValueError('New data must have seame number of columns as the ones the model has been trained with'))
        Xn = Xn[:,self.non_zero_scale_vars_]
        Xnc = self.scaling.scale_data(Xn,self.x_loc_[self.non_zero_scale_vars_],self.x_sca_[self.non_zero_scale_vars_])
        return(Xnc*self.x_Rweights_)
        
    def weightnewx(self,Xn):
        if type(Xn) == ps.core.frame.DataFrame:
            Xn = Xn.to_numpy()
        (n,p) = Xn.shape
        if p!= self.X.shape[1]:
            raise(ValueError('New data must have seame number of columns as the ones the model has been trained with'))
        Tn = self.transform(Xn)
        scaling = self.scaling
        scalet = self.scale
        if (scalet == "None"):
            scaling.set_params(scale = "mad")
        if isinstance(Tn,np.matrix):
            Tn = np.array(Tn)
        dtn = scaling.fit(Tn)
        wtn = np.sqrt(np.array(np.sum(np.square(dtn),1),dtype=np.float64))
        wtn = wtn/np.median(wtn)
        wtn = wtn.reshape(-1)
        if (self.fun == "Fair"):
            wtn = Fair(wtn,self.probctx_)
        if (self.fun == "Huber"):
            wtn = Huber(wtn,self.probctx_)
        if (self.fun == "Hampel"):
            wtn = Hampel(wtn,self.probctx_,self.hampelbx_,self.hampelrx_)
        return(wtn)
        
    def valscore(self,Xn,yn,scoring):
        if type(Xn) == ps.core.frame.DataFrame:
            Xn = Xn.to_numpy()
        if type(yn) in [ps.core.frame.DataFrame,ps.core.series.Series]:
            yn = yn.to_numpy().T.astype('float64')
        (n,p) = Xn.shape
        if p!= self.X.shape[1]:
            raise(ValueError('New data must have seame number of columns as the ones the model has been trained with'))
        if scoring=='weighted':
            return(RegressorMixin.score(self,Xn,yn,sample_weight=self.caseweights_))
        elif scoring=='normal':
            return(RegressorMixin.score(self,Xn,yn))
        else:
            raise(ValueError('Scoring flag must be set to "weighted" or "normal".'))

        
        
    

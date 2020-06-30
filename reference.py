#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:41:01 2020

@author: daniuher
"""



def getLV(unipol, getHV = 'no'):
        """
        returns the channels with a below average variability
        getHV = 'yes' returns also the above average channels
        """
        import numpy as np
        
        v = list()
        for i in range(unipol.shape[1]):
            v.append(np.var(unipol[:,i]));
    
        vAverage = np.mean(v)  
        v.append(vAverage)      
        v.sort()
    
        vList = list()
        HV = list()
        for i in range(unipol.shape[1]):
            if np.var(unipol[:,i])<vAverage:
                vList.append(i)
            else:
                HV.append(i)
    
        below_average = unipol[:,vList]
        above_average = unipol[:,HV]     
    #    below_average = np.transpose(below_average[:,0:-2])
        
        if getHV == 'no':
            return below_average
        else:
            return below_average, above_average
        


def grs(unipol, **kwargs):
        """
        Parameters
        ----------
        unipol     : set of unipolar signals
        
        unipoltype : 'd' | 'pymef'  (default 'd')
        method     : 'avg' | 'ica'  (default 'avg')
        dataset    : 'full' | 'lv'  (default 'lv')
        analysis   : (NOT YET IMPLEMENTED) generate information about the ref 
                     signal and the calculation process 
        
        grs...GetReferenceSignal
        
        Get the reference signal from a set of unipolar data. Ref signal can
        be obtained with either an average-based method or an ICA-based
        method. The signal can be obtained either from the full dataset
        (settype='full') or only from the channels with below average 
        variance (settype='lv')
        
        P.S. Don't forget to use the set of iEEG data only with removed
        utility channels (ECG, EOG, etc.). I forgot that many times :D


        Returns 
        -------
        ref : the reference signal
        analysis gets saved alongside the dataset (not yet implemented)

        """
        
        try:
            from refsig import getref
            import numpy as np
            from sklearn.decomposition import FastICA
        except ImportError as e:
            print(e)
            print("Please (probably) use:  pip install "+e.name)
            return "Function not executed. Missing dependency"
        
        try:
            kwargs["unipoltype"]
        except:    
            kwargs["unipoltype"]='d'
           
            
        try:
            kwargs["method"]
        except:    
            kwargs["method"]='avg'
        
        
        try:
            kwargs["dataset"]
        except:    
            kwargs["dataset"]='lv'
        
         
        try:
            kwargs["analysis"]
        except:    
            kwargs["analysis"]='no'
        
        
        
        if kwargs["dataset"] == 'lv':
            originial_data = unipol
            unipol = getLV(unipol)
            
        
        if kwargs["method"] == 'avg':
            ref = getref.avg(np.transpose(unipol))
        else:
            ref = getref.calc(np.transpose(unipol))
        
        
        return ref
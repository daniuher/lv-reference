Reference signal toolbox
------------------------

Import:

	import reference

Usage:
	
	ref_signal = reference.grs(unipol, **kwargs)
	
	
Help:

	reference.grs()
	Parameters
        ------
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

Publications:

[D. Uher, P. Klimes, et al., "Stereo-electroencephalography (SEEG) reference based on low-variance signals," 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Montreal, QC, Canada, 2020](https://ieeexplore.ieee.org/abstract/document/9175734/citations#citations)

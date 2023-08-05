# Copyright 2018 Regents of the University of Colorado. All Rights Reserved.
# Released under the MIT license.
# This software was developed at the University of Colorado's Laboratory for Atmospheric and Space Physics.
# Verify current version before use at: https://github.com/MAVENSDC/Pytplot

import pytplot
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d

                              
def resample(tvar,times,new_tvar=None):
    """
    Linearly interpolates data to user-specified values.  To interpolate one tplot variable to another, use tinterp.

    .. note::
        This analysis routine assumes the data is no more than 2 dimensions.  If there are more, they may become flattened!

    Parameters:
        tvar : str
            Name of tvar whose data will be interpolated to specified times.
        times : int/list
            Desired times for interpolation.
        new_tvar : str
            Name of new tvar in which to store interpolated data.  If none is specified, a name will be created.

    Returns:
        None

    Examples:
        >>> # Interpolate data for 'd' to values [3,4,5,6,7,18].
        >>> pytplot.store_data('d', data={'x':[2,5,8,11,14,17,21], 'y':[[1,1],[2,2],[100,100],[4,4],[5,5],[6,6],[7,7]]})
        >>> pytplot.tplot_resample('d',[3,4,5,6,7,18],'d_resampled')
    """

    if new_tvar is None:
        new_tvar=tvar+'_resampled'

    resample_spec_bins = False
    if ('spec_bins' in pytplot.data_quants[tvar].coords) and (pytplot.data_quants[tvar]['spec_bins'].shape > 1):
        resample_spec_bins = True

    if 'spec_bins' in pytplot.data_quants[tvar].coords:
        d, s = pytplot.tplot_utilities.convert_tplotxarray_to_pandas_dataframe(tvar)
    else:
        d = pytplot.tplot_utilities.convert_tplotxarray_to_pandas_dataframe(tvar)

    #create dummy dataframe for times to interpolate to
    df_index = d.columns.copy()
    new_df = []
    spec_df = []
    tvar_orig = d.copy()

    if resample_spec_bins:
        spec_orig = s.copy()
         
    #for each column of dataframe
    for i in df_index:
        tv2_col = [item[i] for item in tvar_orig.values]
        if resample_spec_bins:
            spec_col = [item[i] for item in spec_orig.values]
        #linear interpolation
        f = interp1d(tvar_orig.index,tv2_col,fill_value="extrapolate")
        new_df = new_df + [f(times)]
         
        if resample_spec_bins:
            g = interp1d(tvar_orig.index,spec_col,fill_value="extrapolate")
            spec_df = spec_df + [g(times)]
    new_df = np.transpose((list(new_df)))
     
    if resample_spec_bins:
        spec_df = np.transpose((list(spec_df)))

    #store interpolated tvar
    if resample_spec_bins:
        pytplot.store_data(new_tvar, data={'x':times,'y':new_df,'v':spec_df})
    elif 'spec_bins' in pytplot.data_quants[tvar].coords:
        pytplot.store_data(new_tvar, data={'x': times, 'y': new_df, 'v': s})
    else:
        pytplot.store_data(new_tvar, data={'x':times,'y':new_df})
    return

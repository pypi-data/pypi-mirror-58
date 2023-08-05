# Copyright 2018 Regents of the University of Colorado. All Rights Reserved.
# Released under the MIT license.
# This software was developed at the University of Colorado's Laboratory for Atmospheric and Space Physics.
# Verify current version before use at: https://github.com/MAVENSDC/Pytplot

import pytplot
import copy

                              
def deflag(tvar1,flag,new_tvar=None):
    """
    Change specified 'flagged' data to NaN.

    Parameters:
        tvar1 : str
            Name of tplot variable to use for data clipping.
        flag : int,list
            Flagged data will be converted to NaNs.
        newtvar : str
            Name of new tvar for deflagged data storage.  If not specified, then the data in tvar1 will be replaced.

    Returns:
        None

    Examples:
        >>> # Remove any instances of [100,90,7,2,57] from 'd', store in 'e'.
        >>> pytplot.store_data('d', data={'x':[2,5,8,11,14,17,21], 'y':[[1,1],[2,2],[100,4],[4,90],[5,5],[6,6],[7,7]]})
        >>> pytplot.deflag('d',[100,90,7,2,57],'e')
    """

    a = copy.deepcopy(pytplot.data_quants[tvar1].where(pytplot.data_quants[tvar1]!=flag))
    if new_tvar is None:
        a.name = tvar1
        pytplot.data_quants[tvar1] = a
    else:
        if 'spec_bins' in a.coords:
            pytplot.store_data(new_tvar, data={'x': a.coords['time'], 'y': a.values, 'v': a.coords['spec_bins']})
        else:
            pytplot.store_data(new_tvar, data={'x': a.coords['time'], 'y': a.values})

'''
    if newtvar == 'tvar_deflag':
        new_tvar = tvar1 + "_deflag"


    #if int input, make list
    if not isinstance(flags,list):
        flags = [flags]
    #grab column indices
    df_index = pytplot.data_quants[tvar1].data.columns
    new_df = []
    tvar_orig = pytplot.data_quants[tvar1].data.copy()
    #for each column of dataframe
    for i in df_index:
        tv2_col = [item[i] for item in tvar_orig.values]
        for j,valj in enumerate(tv2_col):
            #if one of flagged values, convert to NaN
            if valj in flags:
                tv2_col[j] = np.NaN
        new_df = new_df + [tv2_col]
    new_df = np.transpose((list(new_df)))
    #store deflagged tvar
    if (pytplot.data_quants[tvar1].spec_bins is not None):
        pytplot.store_data(newtvar, data={'x':tvar_orig.index,'y':new_df,'v':pytplot.data_quants[tvar1].spec_bins})
    else:
        pytplot.store_data(newtvar, data={'x':tvar_orig.index,'y':new_df})
    return
'''
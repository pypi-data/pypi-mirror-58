import pytplot
import numpy as np


def avg_res_data(tvar1,res,new_tvar=None):
    """
    Averages the variable over a specified period of time.

    Parameters:
        tvar1 : str
            Name of tplot variable.
        res : int/float
            The new data resolution
        new_tvar : str
            Name of new tvar for averaged data.  If not set, then the data in tvar1 is replaced.

    Returns:
        None

    Examples:
        >>> #Average the data over every two seconds
        >>> pytplot.store_data('d', data={'x':[2,5,8,11,14,17,21], 'y':[[1,1,50],[2,2,3],[100,4,47],[4,90,5],[5,5,99],[6,6,25],[7,7,-5]]})
        >>> pytplot.avg_res_data('d',2,'d2res')
        >>> print(pytplot.data_quants['d'].values)
    """

    tvar = pytplot.data_quants[tvar1].coarsen(time=res, boundary='trim').mean()
    tvar.name = pytplot.data_quants[tvar1].name
    if new_tvar is None:
        pytplot.data_quants[tvar1] = tvar
    else:
        if 'spec_bins' in pytplot.data_quants[tvar1].coords:
            pytplot.store_data(new_tvar, data={'x': tvar.coords['time'].values, 'y': tvar.values,
                                               'v': tvar.coords['spec_bins'].values})
        else:
            pytplot.store_data(new_tvar, data={'x': tvar.coords['time'].values, 'y': tvar.values})
'''
    time_varying = pytplot.data_quants[tvar1].spec_bins_time_varying
    #grab info from tvar
    df = pytplot.data_quants[tvar1].data.copy()
    if (pytplot.data_quants[tvar1].spec_bins is not None) and (time_varying == True):
        dfspec = pytplot.data_quants[tvar1].spec_bins.copy()
    time = df.index
    start_t = df.index[0]
    end_t = df.index[-1]
    df_index = list(df.columns)
    #create list of times spanning tvar range @ specified res
    res_time = np.arange(start_t,end_t+1,res)
    new_res_time = np.array([])
    #find closest time to new resolution times
    for t in res_time:
        if t not in time:
            tdiff = abs(time-t)
            new_res_time = np.append(new_res_time,time[tdiff.argmin()])
        else:
            new_res_time = np.append(new_res_time,t)
    #make sure no duplicate times from resolution time rounding
    new_res_time = np.unique(new_res_time)
    #shift start time array
    start_t = np.roll(new_res_time,1)
    end_t = new_res_time
    start_t = np.delete(start_t,0)
    end_t = np.delete(end_t,0)
    #initialize arrays
    avg_bin_data = []
    avg_bin_spec = []
    avg_bin_time = np.array([])
    #for each time bin
    for it,t in enumerate(start_t):
        #for each data column
        data_avg_bin = np.array([])
        spec_avg_bin = np.array([])
        for i in df_index:
            #append localized bin average to data_avg_bin
            data_avg_bin = np.append(data_avg_bin,[(df.loc[start_t[it]:end_t[it]])[i].mean()])
            if (pytplot.data_quants[tvar1].spec_bins is not None) and (time_varying == True):
                spec_avg_bin = np.append(spec_avg_bin,[(dfspec.loc[start_t[it]:end_t[it]])[i].mean()])
        #append whole array of bin averages (over n columns) to avg_bin_data
        avg_bin_data = avg_bin_data + [data_avg_bin.tolist()]
        if (pytplot.data_quants[tvar1].spec_bins is not None) and (time_varying == True):
            avg_bin_spec = avg_bin_spec + [spec_avg_bin.tolist()]
        avg_bin_time = np.append(avg_bin_time,t)
    #store data in new_tvar
    if (pytplot.data_quants[tvar1].spec_bins is not None) and (time_varying == True):
        pytplot.store_data(new_tvar, data={'x':avg_bin_time,'y':avg_bin_data,'v':avg_bin_spec})
    elif pytplot.data_quants[tvar1].spec_bins is not None:
        pytplot.store_data(new_tvar, data={'x':avg_bin_time,'y':avg_bin_data,'v':pytplot.data_quants[tvar1].spec_bins})
    else:
        pytplot.store_data(new_tvar, data={'x':avg_bin_time,'y':avg_bin_data})
    return new_tvar
'''
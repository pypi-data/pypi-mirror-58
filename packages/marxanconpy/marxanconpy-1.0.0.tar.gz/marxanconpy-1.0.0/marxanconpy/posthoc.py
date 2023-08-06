import numpy
import os
import pandas
import geopandas as gpd
import marxanconpy

def calc_postHoc(pu,filename,format,IDs,selectionIDs):
    """ Calculate PostHoc Metrics

    Calculate PostHoc Metrics for a given Marxan solution

    :param filename: filename of the connectivity data
    :param format: The format of the connectivity file (i.e. "Matrix", "Edge List", "Edge List with Type", "Edge List with Time"). See http://marxanconnect.ca/glossary.html#data_formats for a detailed description of formats
    :param IDs: Planning unit IDs
    :param selectionIDs: Planning unit IDs for those included in the Marxan solution
    :return:
    """
    area_proj = marxanconpy.spatial.get_appropriate_projection(pu, 'area')
    dist_proj = marxanconpy.spatial.get_appropriate_projection(pu, 'distance')
    
    select_pu_area = pu[pandas.Series(IDs).isin(selectionIDs)].to_crs(area_proj)
    select_pu_dist = pu[pandas.Series(IDs).isin(selectionIDs)].to_crs(dist_proj)
    
    solutions_dist = gpd.GeoDataFrame(geometry=list(select_pu_dist.geometry.unary_union))
    
    min_dist = numpy.empty((solutions_dist.shape[0],solutions_dist.shape[0]))
    for i, unit1 in solutions_dist.iterrows():
        for j, unit2 in solutions_dist.iterrows():
            min_dist[i,j] = numpy.min([unit1.geometry.distance(unit2.geometry) ])
            
    min_dist[min_dist==0]=min_dist.max()
        
    postHoc = pandas.DataFrame()
    if os.path.isfile(filename):
        if format==None:
            connectivity = None
        elif format == "Matrix":
            connectivity = pandas.read_csv(filename, index_col=0)
        elif format == "Edge List with Time":
            connectivity = pandas.read_csv(filename,
                            dtype = {'id1': str, 'id2': str})[['id1', 'id2', 'value']].groupby(['id1', 'id2']).mean()
        else:
            connectivity = pandas.read_csv(filename,
                            dtype = {'id1': str, 'id2': str})

        if connectivity.shape[1]==3 or format == "Matrix" or format==None:
            all_type=['default_type_replace']
        else:
            all_type=numpy.unique(connectivity.drop(['id1', 'id2', 'value'], axis=1))

        postHoc = postHoc.append(pandas.DataFrame({"Metric": ("Planning Units",
                                                                  "Mean Size (km^2)",
                                                                  "Mean Min Spacing (km)",
                                                                  "ProtConn (10 km)",
                                                                  "ProtConn (50 km)",
                                                                  "ProtConn (150 km)"),
                                                       "Type": ("All", "All", "All", "All", "All", "All"),
                                                       "Planning Area": (len(IDs),
                                                                         0,
                                                                         0,
                                                                         0,
                                                                         0,
                                                                         0),
                                                       "Solution": (
                                                           len(selectionIDs),
                                                           round(gpd.GeoDataFrame(geometry=list(select_pu_area.geometry.unary_union)).area.mean()/1000000,1),
                                                           round(min_dist.min(axis=1).mean()/1000,1),
                                                           (min_dist<10000).any(axis=1).mean(),
                                                           (min_dist<50000).any(axis=1).mean(),
                                                           (min_dist<150000).any(axis=1).mean())}), ignore_index=True)
        
        for type in all_type:
            if type=="default_type_replace":
                graph = marxanconpy.manipulation.connectivity2graph(connectivity,format,IDs)
            else:
                graph = marxanconpy.manipulation.connectivity2graph(connectivity[(connectivity.drop(['id1', 'id2', 'value'], axis=1)==type).values], format, IDs)

            sub = graph.subgraph([str(i) for i in selectionIDs])

            postHoc = postHoc.append(pandas.DataFrame({"Metric": ("Connections",
                                                                  "Graph Density",
                                                                  "Eigenvalue"),
                                                       "Type": (type, type, type),
                                                       "Planning Area": (graph.ecount(),
                                                                         graph.density(),
                                                                         graph.evcent(weights=graph.es["weight"],
                                                                                      return_eigenvalue=True)[1]),
                                                       "Solution": (
                                                           sub.ecount(),
                                                           sub.density(),
                                                           sub.evcent(weights=sub.es["weight"],
                                                                      return_eigenvalue=True)[1])}), ignore_index=True)
        postHoc["Percent"] = postHoc["Solution"]/postHoc["Planning Area"]*100
        postHoc = postHoc[['Metric','Type','Planning Area','Solution','Percent']]
        if "default_type_replace" in postHoc["Type"].unique():
            del(postHoc["Type"])
    else:
        if format==None:
            all_type=['default_type_replace']
            
        postHoc = pandas.DataFrame()
        for type in all_type:
            
            postHoc = postHoc.append(pandas.DataFrame({"Metric": ("Planning Units",
                                                                    "Mean Size (km^2)",
                                                                    "Mean Min Spacing (km)",
                                                                    "ProtConn (10 km)",
                                                                    "ProtConn (50 km)",
                                                                    "ProtConn (150 km)"),
                                                        "Type": (type, type, type, type, type, type),
                                                        "Planning Area": (len(IDs),
                                                                            0,
                                                                            0,
                                                                            0,
                                                                            0,
                                                                            0),
                                                        "Solution": (
                                                            len(selectionIDs),
                                                            round(gpd.GeoDataFrame(geometry=list(select_pu_area.geometry.unary_union)).area.mean()/1000000,1),
                                                            round(min_dist.min(axis=1).mean()/1000,1),
                                                            (min_dist<10000).any(axis=1).mean(),
                                                            (min_dist<50000).any(axis=1).mean(),
                                                            (min_dist<150000).any(axis=1).mean())}), ignore_index=True)
            
        
        postHoc["Percent"] = postHoc["Solution"]/postHoc["Planning Area"]*100
        postHoc = postHoc[['Metric','Type','Planning Area','Solution','Percent']]
        if "default_type_replace" in postHoc["Type"].unique():
            del(postHoc["Type"])
    return postHoc
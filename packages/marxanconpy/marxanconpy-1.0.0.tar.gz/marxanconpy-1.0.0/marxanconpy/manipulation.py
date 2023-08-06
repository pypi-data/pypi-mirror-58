import numpy
import os
import pandas
import geopandas as gpd
import igraph
import wx
import marxanconpy

def convert_matrix_type(current,desired,matrix,localProd):
    """ Convert Matrix Types

    Converts connectivity data in matrix format to/from various types (e.g. "Probability", "Migration", "Flow"). See
    http://marxanconnect.ca/glossary.html#data_types for detailed description

    :param current: Current connectivity data type (e.g. "Probability", "Migration", "Flow")
    :param desired: Current connectivity data type (e.g. "Probability", "Migration", "Flow")
    :param matrix: Connectivity Matrix
    :param localProd: Local Production at each site in the connectivity matrix
    :return:
    """

    print("converting ",current," to ",desired)
    if current == desired:
        return matrix
    elif current == "Probability":
        if desired == "Migration":
            matrix = matrix * localProd['production'].values[:, numpy.newaxis]
            matrix = matrix / matrix.sum(axis=0)
        elif desired == "Flow":
            matrix = matrix * localProd['production'].values[:, numpy.newaxis]
        else:
            print("Warning: " + desired + " not a recognized matrix type.")
    elif current == "Migration":
        print("Warning: Migration Matrices cannot be converted without knowing local recruitment")
    elif current == "Flow":
        if desired == "Migration":
            matrix = matrix / matrix.sum(axis=0)
        elif desired == "Probability":
            matrix = matrix.divide(matrix.sum(axis=1).values,axis="rows")
        else:
            print("Warning: " + desired + " not a recognized matrix type.")
    else:
        print("Warning: " + current + " not a recognized matrix type.")
    return matrix.fillna(0)

def convert_graph_type(current,desired,graph,localProd):
    """ Convert Graph Types

    Converts connectivity data in graph (igraph) format to/from various types (e.g. "Probability", "Migration", "Flow"). See
    http://marxanconnect.ca/glossary.html#data_types for detailed description

    :param current: Current connectivity data type (e.g. "Probability", "Migration", "Flow")
    :param desired: Current connectivity data type (e.g. "Probability", "Migration", "Flow")
    :param graph: Connectivity Graph
    :param localProd: Local Production at each site in the connectivity matrix
    :return:
    """
    print("converting ",current," to ",desired)
    if current == desired:
        return graph
    elif current == "Probability":
        g = graph.copy()
        from_list = numpy.array([x[0] for x in g.get_edgelist()])
        to_list = numpy.array([x[1] for x in g.get_edgelist()])
        new = numpy.array(g.es["weight"])
        IDs = numpy.unique(numpy.concatenate((numpy.unique(from_list), numpy.unique(to_list))))
        if desired == "Migration":
            for i in range(len(IDs)):
                new[from_list == i] = new[from_list == i] * localProd["production"][i]
            for i in range(len(IDs)):
                new[to_list == i] = new[to_list == i] / numpy.sum(new[to_list == i])
        elif desired == "Flow":
            for i in range(len(IDs)):
                new[from_list == i] = new[from_list == i] * localProd["production"][i]
        else:
            print("Warning: " + desired + " not a recognized matrix type.")
    elif current == "Migration":
        print("Warning: Migration Matrices cannot be converted without knowing local recruitment")
    elif current == "Flow":
        g = graph.copy()
        from_list = numpy.array([x[0] for x in g.get_edgelist()])
        to_list = numpy.array([x[1] for x in g.get_edgelist()])
        new = numpy.array(g.es["weight"])
        IDs = numpy.unique(numpy.concatenate((numpy.unique(from_list), numpy.unique(to_list))))

        if desired == "Migration":
            for i in range(len(IDs)):
                new[to_list == i] = new[to_list == i] / numpy.sum(new[to_list == i])
        elif desired == "Probability":
            for i in range(len(IDs)):
                new[from_list == i] = new[from_list == i] / numpy.sum(new[from_list == i])
        else:
            print("Warning: " + desired + " not a recognized matrix type.")
    else:
        print("Warning: " + current + " not a recognized matrix type.")
    g.es["weight"] = new
    return g

def calc_metrics(project,progressbar,calc_metrics_pu=True,calc_metrics_cu=False):
    """ Calculate connectivity metrics

    Calculates connectivity metrics to be used as conservation features and prepares the connectivity to be used as
    spatial dependencies

    :param project: Project dictionary created by'marxanconpy.marcon.new_project()' or 'marxanconpy.marcon.load_file()'. The later reads the .MarCon JSON project file
    :param progressbar: Logical. True if you want to see a progressbar
    :param calc_metrics_pu: Logical. True if you want to calculate metrics for planning units.
    :param calc_metrics_cu: Logical. True if you want to calculate metrics for connectivity units if such data is supplied. For exploration purposes only as these will not be used in any Marxan analyses.
    :return:
    """
    try:
        # create dict entry for connectivityMetrics
        project['connectivityMetrics'] = {}
        temp = {}

        all_types = []
        if calc_metrics_pu and calc_metrics_cu:
            if os.path.isfile(project['filepaths']['demo_pu_cm_filepath']):
                all_types += ['demo_pu', 'demo_cu']
            if os.path.isfile(project['filepaths']['land_pu_cm_filepath']):
                all_types += ['land_pu']
        elif calc_metrics_pu:
            if os.path.isfile(project['filepaths']['demo_pu_cm_filepath']):
                all_types += ['demo_pu']
            if os.path.isfile(project['filepaths']['land_pu_cm_filepath']):
                all_types += ['land_pu']
        elif calc_metrics_cu:
            if os.path.isfile(project['filepaths']['demo_cu_cm_filepath']):
                all_types += ['demo_cu']

        # create dict entries for boundary
        project['connectivityMetrics']['boundary'] = {}
        bd_demo_conn_boundary_done = False
        bd_land_conn_boundary_done = False

        # load local production
        if os.path.isfile(project['filepaths']['lp_filepath']):
            localProd = pandas.read_csv(project['filepaths']['lp_filepath'], index_col=0)
        else:
            localProd = 1
            if progressbar:
                # start progressbar
                max = 100 * len(all_types)
                dlg = wx.ProgressDialog("Calculating Connectivity Metrics",
                                        "Please wait while the connectivity metrics are being calculated.",
                                        maximum=max,
                                        parent=None,
                                        style=wx.PD_APP_MODAL
                                              | wx.PD_CAN_ABORT
                                              | wx.PD_AUTO_HIDE
                                              | wx.PD_ELAPSED_TIME
                                              | wx.PD_ESTIMATED_TIME
                                              | wx.PD_REMAINING_TIME
                                        )
                count = 0
            keepGoing = True
            for type in all_types:
                if not keepGoing: break

                # check format
                if type[-2:] == 'pu':
                    if type == 'demo_pu':
                        temp['format'] = project["options"]["demo_conmat_format"]
                    if type == 'land_pu':
                        temp['format'] = "Edge List with Habitat"

                # load correct matrix and transform if necessary
                print("loading matrix")
                print(project['filepaths'][type + '_cm_filepath'])
                if os.path.isfile(project['filepaths'][type + '_cm_filepath']):
                    if temp['format'] == "Matrix":
                        temp[type + '_connectivity'] = {}
                        temp[type + '_connectivity']['default_type_replace'] = pandas.read_csv(
                            project['filepaths'][type + '_cm_filepath'], index_col=0)
                    elif temp['format'] == "Edge List":
                        temp[type + '_connectivity'] = {}
                        temp[type + '_connectivity']['default_type_replace'] = pandas.read_csv(
                            project['filepaths'][type + '_cm_filepath'],
                            dtype = {'id1': str, 'id2': str})
                    elif temp['format'] == "Edge List with Time":
                        temp[type + '_conmat_time'] = pandas.read_csv(
                            project['filepaths'][type + '_cm_filepath'],
                            dtype = {'id1': str, 'id2': str})
                        temp[type + '_connectivity'] = {}
                        temp[type + '_connectivity']['default_type_replace'] = temp[type + '_conmat_time'][
                            ['id1', 'id2', 'value']].groupby(['id1', 'id2']).mean()

                        marxanconpy.warn_dialog(
                            message="A connectivity 'Edge List with Time' was provided; however, all metrics except "
                                    "'Temporal Connectivity Correlation' will be calculated from the temporal"
                                    "mean of connectivity")
                    elif temp['format'] == "Edge List with Type":
                        temp[type + '_conmat'] = pandas.read_csv(
                            project['filepaths'][type + '_cm_filepath'],
                            dtype = {'type': str, 'id1': str, 'id2': str})

                        temp[type + '_connectivity'] = {}
                        for t in temp[type + '_conmat']['type'].unique():
                            temp[type + '_connectivity'][t] = temp[type + '_conmat'][
                                temp[type + '_conmat']['type'] == t]
                            if not temp[type + '_connectivity'][t].value.sum() > 0:
                                del temp[type + '_connectivity'][t]
                                marxanconpy.warn_dialog("All connectivity values for type '" + str(
                                    t) + "' are below or equal to zero, excluding from further analyses")

                    elif temp['format'] == "Edge List with Habitat":
                        temp[type + '_conmat'] = pandas.read_csv(
                            project['filepaths'][type + '_cm_filepath'],
                            dtype = {'id1': str, 'id2': str})
                        temp[type + '_conmat'].loc[temp[type + '_conmat']['value'] < float(
                            project['options']['land_hab_thresh']), 'value'] = 0

                        temp[type + '_connectivity'] = {}
                        for h in temp[type + '_conmat']['habitat'].unique():
                            temp[type + '_connectivity'][h] = temp[type + '_conmat'][
                                temp[type + '_conmat']['habitat'] == h]
                            if not temp[type + '_connectivity'][h].value.sum() > 0:
                                del temp[type + '_connectivity'][h]
                                marxanconpy.warn_dialog("All connectivity values for type '" + str(
                                    h) + "' are below or equal to zero, excluding from further analyses")

                else:
                    marxanconpy.warn_dialog(message="File not found: " + project['filepaths'][type + '_cm_filepath'])

                # load correct shapefile path
                print("loading shapefile")
                if type[-2:] == 'pu':
                    temp['shp_filepath'] = project['filepaths']['pu_filepath']
                    temp['shp_file_pu_id'] = project['filepaths']['pu_file_pu_id']
                else:
                    temp['shp_filepath'] = project['filepaths'][type + '_filepath']
                    temp['shp_file_pu_id'] = project['filepaths'][type + '_file_pu_id']

                temp['shp'] = gpd.GeoDataFrame.from_file(temp['shp_filepath'])
                try:
                    temp['shp'][temp['shp_file_pu_id']] = temp['shp'][temp['shp_file_pu_id']].astype('int').astype('str')
                except:
                    temp['shp'][temp['shp_file_pu_id']] = temp['shp'][temp['shp_file_pu_id']].astype('str')


                # create dict entries for spec
                project['connectivityMetrics']['spec_' + type] = {}

                # warn if files not the same length
                # if temp['format'] == "Edge List with Habitat" or "Edge List with Type":
                #     temp['conmat_len'] = str(len(next(iter(temp[type + '_connectivity'].values()))))
                # else:
                #     temp['conmat_len'] = str(len(temp[type + '_connectivity']))
                # temp['conmat_len'] = str(len(next(iter(temp[type + '_connectivity'].values()))))
                # temp['shp_len'] = str(gpd.GeoDataFrame.from_file(temp['shp_filepath']).shape[0])
                # if temp['conmat_len'] != temp['shp_len']:
                #     warn_dialog(
                #         message="The selected shapefile and connectivity matrix do not have the expected number of rows. "
                #                 "There are " + temp['conmat_len'] + " rows in the selected connectivity matrix and " +
                #                 temp['shp_len'] + " rows in the shapefile")

                # warn and end if pu_id not in shapefile
                # temp['shp_file_pu_id']
                # temp['shp_filepath']

                # calculate demographic metrics
                if type[:4] == 'demo':
                    for t in temp[type + '_connectivity'].keys():
                        if t == 'default_type_replace':
                            print('calculating demographic connectivity metrics')
                        else:
                            print("calculating demographic connectivity metrics for "+t)

                        if not keepGoing: break

                        if t == 'default_type_replace':
                            typesuffix = ''
                        else:
                            typesuffix = '_' + t

                        graph = connectivity2graph(connectivity=temp[type + '_connectivity'][t],
                                                   format=temp['format'],
                                                   IDs=temp['shp'][temp['shp_file_pu_id']].values)

                        n = round(100 / 15 / len(temp[type + '_connectivity'].keys()))
                        # if not os.path.isfile(project['filepaths']['lp_filepath']):
                        # warn_dialog("No Local Production input. Marxan Connect will assume equal production in each planning unit.")

                        if project["options"]["demo_metrics"]["in_degree"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'in_degree_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2vertexdegree(graph, mode='IN')
                        marxanconpy.progress_bar_update(count,dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["out_degree"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'out_degree_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2vertexdegree(graph, mode='OUT')
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["between_cent"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'between_cent_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2betweencent(graph)
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["eig_vect_cent"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'eig_vect_cent_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2eigvectcent(
                                    marxanconpy.manipulation.convert_graph_type(
                                        project['options']['demo_conmat_type'],
                                        'Migration',
                                        graph,
                                        localProd))
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["google"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type]['google_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2google(graph)
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)


                        if project["options"]["demo_metrics"]["self_recruit"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'self_recruit_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2diagonal(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Migration',
                                    graph,
                                    localProd))
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["local_retention"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'local_retention_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2diagonal(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Probability',
                                    graph,
                                    localProd))
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["outflow"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type]['outflow_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2outflow(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Flow',
                                    graph,
                                    localProd))
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)


                        if project["options"]["demo_metrics"]["inflow"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type]['inflow_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2inflow(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Flow',
                                    graph,
                                    localProd))
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["fa_recipients"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'fa_recipients_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2recipients(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Flow',
                                    graph,
                                    localProd),
                                                                      project['filepaths']['fa_filepath'],
                                                                      temp['shp_filepath'],
                                                                      temp['shp_file_pu_id']
                                                                      )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["fa_donors"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'fa_donors_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2donors(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Flow',
                                    graph,
                                    localProd),
                                                          project['filepaths']['fa_filepath'],
                                                          temp['shp_filepath'],
                                                          temp['shp_file_pu_id']
                                                          )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["aa_recipients"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'aa_recipients_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2recipients(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Flow',
                                    graph,
                                    localProd),
                                                                      project['filepaths']['aa_filepath'],
                                                                      temp['shp_filepath'],
                                                                      temp['shp_file_pu_id'],
                                                                      True
                                                                      )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["aa_donors"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'aa_donors_' + type + typesuffix] = \
                                marxanconpy.metrics.graph2donors(marxanconpy.manipulation.convert_graph_type(
                                    project['options']['demo_conmat_type'],
                                    'Flow',
                                    graph,
                                    localProd),
                                                                  project['filepaths']['aa_filepath'],
                                                                  temp['shp_filepath'],
                                                                  temp['shp_file_pu_id'],
                                                                  True
                                                                  )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["stochasticity"] and keepGoing:
                            if 'fa_filepath' in project['filepaths']:
                                project['connectivityMetrics']['spec_' + type][
                                    'temp_conn_cov_' + type + typesuffix] = \
                                    marxanconpy.metrics.graphtime2temp_conn_cov(temp[type + '_conmat_time'],
                                                                                 project['filepaths']['fa_filepath'],
                                                                                 temp['shp_filepath']
                                                                                 )
                            else:
                                marxanconpy.warn_dialog(
                                    message="No 'Focus Area' has been specified. Please load a focus area file in "
                                            "the Spatial Input tab")
                                return
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["demo_metrics"]["conn_boundary"] and keepGoing:
                            if bd_demo_conn_boundary_done == False:
                                if t == 'default_type_replace':
                                    project['connectivityMetrics']['boundary']['conn_boundary_' + type] = \
                                        marxanconpy.metrics.graph2connboundary(graph)
                                else:
                                    project['connectivityMetrics']['boundary']['conn_boundary_' + type] = \
                                        temp[type + '_conmat'][['id1', 'id2', 'value']].groupby(
                                            ['id1', 'id2']).mean().reset_index().to_json(orient='split')

                                    marxanconpy.warn_dialog(
                                        message="A connectivity " + temp['format'] + " was provided. The Ecological "
                                                                                          "Distance to be used as the Boundary Definitions will be calculated from the "
                                                                                          "mean of connectivity matrices supplied")
                                bd_demo_conn_boundary_done = True
                                marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                # calculate landscape metrics ############################################################################
                if type[-7:] == 'land_pu':
                    for h in temp[type + '_connectivity'].keys():
                        if h == 'default_type_replace':
                            print('calculating landscape connectivity metrics')
                        else:
                            print("calculating landscape connectivity metrics for "+h)

                        graph = connectivity2graph(connectivity=temp[type + '_connectivity'][h],
                                                   format=temp['format'],
                                                   IDs=temp['shp'][temp['shp_file_pu_id']].values)

                        if not keepGoing: break
                        n = 100 / 10 / len(temp[type + '_conmat'].keys())
                        if project["options"]["land_metrics"]["in_degree"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'in_degree_' + type + "_" + str(h)] = marxanconpy.metrics.graph2vertexdegree(
                                graph, mode='IN')
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)


                        if project["options"]["land_metrics"]["out_degree"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'out_degree_' + type + "_" + str(h)] = marxanconpy.metrics.graph2vertexdegree(
                                graph, mode='OUT')
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["between_cent"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'between_cent_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2betweencent(graph)
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["eig_vect_cent"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'eig_vect_cent_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2eigvectcent(graph)

                        if project["options"]["land_metrics"]["google"]:
                            project['connectivityMetrics']['spec_' + type]['google_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2google(graph)
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["fa_recipients"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'fa_recipients_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2recipients(graph,
                                                                      project['filepaths']['fa_filepath'],
                                                                      temp['shp_filepath'],
                                                                      temp['shp_file_pu_id']
                                                                      )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["fa_donors"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'fa_donors_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2donors(graph,
                                                                  project['filepaths']['fa_filepath'],
                                                                  temp['shp_filepath'],
                                                                  temp['shp_file_pu_id']
                                                                  )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["aa_recipients"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'aa_recipients_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2recipients(graph,
                                                                      project['filepaths']['aa_filepath'],
                                                                      temp['shp_filepath'],
                                                                      temp['shp_file_pu_id'],
                                                                      True
                                                                      )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["aa_donors"] and keepGoing:
                            project['connectivityMetrics']['spec_' + type][
                                'aa_donors_' + type + "_" + str(h)] = \
                                marxanconpy.metrics.graph2donors(graph,
                                                                  project['filepaths']['aa_filepath'],
                                                                  temp['shp_filepath'],
                                                                  temp['shp_file_pu_id'],
                                                                  True
                                                                  )
                        marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)

                        if project["options"]["land_metrics"]["conn_boundary"] and keepGoing:
                            if bd_land_conn_boundary_done == False:
                                if h == 'default_type_replace':
                                    project['connectivityMetrics']['boundary']['conn_boundary_' + type] = \
                                        marxanconpy.metrics.graph2connboundary(graph)
                                else:
                                    project['connectivityMetrics']['boundary']['conn_boundary_' + type] = \
                                        temp[type + '_conmat'][
                                            ['id1', 'id2', 'value']].groupby(
                                            ['id1', 'id2']).mean().reset_index().to_json(orient='split')

                                    marxanconpy.warn_dialog(
                                        message="A connectivity " + temp['format'] + " was provided. The Ecological "
                                                                                          "Distance to be used as the Boundary Definitions will be calculated from the "
                                                                                          "mean of connectivity matrices supplied")
                                bd_land_conn_boundary_done = True
                                marxanconpy.progress_bar_update(count, dlg, keepGoing, n, progressbar)
        if progressbar:
            dlg.Destroy()
    except:
        if progressbar:
            dlg.Destroy()
        raise

def check_matrix_list_format(format, filepath):
    """ Check format

    Quality control function to assure that the file format is 'as advertised'

    :param format: The expected format of the connectivity file (i.e. "Matrix", "Edge List", "Edge List with Type", "Edge List with Time"). See http://marxanconnect.ca/glossary.html#data_formats for a detailed description of formats
    :param filepath: The filepath to the connectivity data
    :return:
    """
    # warn if matrix is wrong format
    warn = False
    message = "See the Glossary for 'Data Formats' under 'Connectivity'."
    if format == "Matrix":
        conmat = pandas.read_csv(filepath, index_col=0)
        if not conmat.shape[1]==conmat.shape[2]:
            message = message + "See the Glossary for 'Data Formats' under 'Connectivity'. Matrices should have an " \
                                "equal number of rows and columns"
            warn-True
    else:
        if format == "Edge List":
            ncol = 3
            expected = numpy.array(['id1', 'id2', 'value'])
        elif format == "Edge List with Type":
            ncol = 4
            expected = numpy.array(['type', 'id1', 'id2', 'value'])
        elif format == "Edge List with Time":
            ncol = 4
            expected = numpy.array(['time', 'id1', 'id2', 'value'])

        conmat = pandas.read_csv(filepath)


        if not conmat.shape[1] == ncol:
            message = message + " The " + format + " Data Format expects exactly " + ncol + " columns, not " + \
                           str(conmat.shape[1]) + " in the file."
            warn = True

        missing = [c not in conmat.columns for c in expected]
        if any(missing):
            message = message + " The " + format + " Data Format expects column header(s) '" + \
                           str(expected[missing]) + \
                           "' which may be missing in the file."
            warn = True
    if warn:
        print(message)
        return message
    else:
        return

def connectivity2graph(connectivity,format,IDs):
    """ Convert Connectivity data to graph format

    :param connectivity: The connectivity data as a pandas data frame (in any format)
    :param format: The format of the connectivity file (i.e. "Matrix", "Edge List", "Edge List with Type", "Edge List with Time"). See http://marxanconnect.ca/glossary.html#data_formats for a detailed description of formats
    :param IDs: Planning unit IDs
    :return:
    """
    print("Converting connectivity data to graph")
    if format == "Matrix":
        g = igraph.Graph.Weighted_Adjacency(connectivity.values.tolist())
        g.vs["name"] = IDs
    else:
        g = igraph.Graph(directed=True)
        g.add_vertices([str(i) for i in IDs])
        g.add_edges(list(zip(connectivity['id1'].astype(str), connectivity['id2'].astype(str))))
        g.es['weight'] = connectivity['value'].values
    return g

def get_marxan_output(input_file,type='Best Solution'):
    """ Get Marxan Output

    Extract Marxan output from a file

    :param input_file: filename of Marxan file to read
    :param type: Marxan file type (i.e. 'Best Solution', 'Selection Frequency',
    :return:
    """
    for line in open(input_file):
        if line.startswith('SCENNAME'):
            SCENNAME = line.replace('SCENNAME ', '').replace('\n', '')
        elif line.startswith('NUMREPS'):
            NUMREPS = int(line.replace('NUMREPS ', '').replace('\n', ''))
        elif line.startswith('OUTPUTDIR'):
            OUTPUTDIR = line.replace('OUTPUTDIR ', '').replace('\n', '')

    if not os.path.isdir(OUTPUTDIR):
        OUTPUTDIR = os.path.join(os.path.dirname(input_file),OUTPUTDIR)

    if type == 'Best Solution':
        fn = os.path.join(OUTPUTDIR, SCENNAME + "_best")
    elif type == 'Selection Frequency':
        fn = os.path.join(OUTPUTDIR, SCENNAME + "_ssoln")
    else:
        fn = os.path.join(OUTPUTDIR, SCENNAME + "_" + type)
        
    if os.path.isfile(fn + '.csv'):
        file = marxanconpy.read_csv_tsv(fn + '.csv')
    elif os.path.isfile(fn + '.txt'):
        file = marxanconpy.read_csv_tsv(fn + '.txt')
    else:
        print('WARNING: ' + fn + ' not found')
    
    if 'planning_unit' in list(file.columns.values):
        try:
            file["planning_unit"] = file["planning_unit"].values.astype('int').astype('str')
        except:
            file["planning_unit"] = file["planning_unit"].values.astype('str')
    elif 'PUID' in list(file.columns.values):
        try:
            file["PUID"] = file["PUID"].values.astype('int').astype('str')
        except:
            file["PUID"] = file["PUID"].values.astype('str')

    return file

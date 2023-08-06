# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:36:11 2019

@author: MichaelEK
"""
import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import cKDTree
import copy

try:
    import overpass
    import osm2geojson
except:
    print('Install overpass and osm2geojson for osm module functions')

#############################################
### Functions


def get_nearest_waterways(gdf_from, id_col, max_distance=500, waterway_type='natural'):
    """
    Function to get the nearest waterways and associated nodes at some max distance from the OSM overpass server. Can specify the waterway type as either 'natural' or 'all'. The higher the max distance the slower the server query.

    Parameters
    ----------
    gdf_from : GeoDataFrame
        Locations of the sites where you want to find the nearest waterway nodes.
    id_col : str
        The column name of the site ID for gdf_from.
    max_distance : int
        The maximum search distance.
    waterway_type : str
        Either 'nautral' or 'all'

    Returns
    -------
    GeoDataFrame
        of the sites and associated waterys and nodes.
    """
    if waterway_type == 'all':
        q_base = """(way['waterway'](around:{dis}, {lat}, {lon});
    node(around:{dis}, {lat}, {lon})(w);)"""
    elif waterway_type == 'natural':
        q_base = "(way['waterway'~'(river|stream|tidal_channel)'](around:{dis}, {lat}, {lon}); node(around:{dis}, {lat}, {lon})(w);)"
    else:
        raise ValueError('waterway_type must be either natural or all.')

    from1 = gdf_from[[id_col, 'geometry']].copy()

    pts1 = from1.to_crs(4326)

    from1['x'] = from1.geometry.x
    from1['y'] = from1.geometry.y
    from1['lon'] = pts1.geometry.x
    from1['lat'] = pts1.geometry.y

    api = overpass.API()

    res_list = []
    for index, p in from1.iterrows():
        q1 = q_base.format(dis=max_distance, lat=p.lat, lon=p.lon)

        response = api.get(q1, responseformat='json')

        nodes1 = [n for n in response['elements'] if n['type'] == 'node']
        pd_nodes = pd.DataFrame.from_records(nodes1)
        gpd_nodes1 = gpd.GeoDataFrame(pd_nodes, geometry=gpd.points_from_xy(pd_nodes['lon'], pd_nodes['lat']), crs=4326)
        gpd_nodes2 = gpd_nodes1.to_crs(from1.crs)

        nodes2 = list(zip(gpd_nodes2.geometry.x, gpd_nodes2.geometry.y))

        btree = cKDTree(nodes2)
        dist, idx = btree.query([p.x, p.y], k=1, distance_upper_bound=max_distance)

        best1 = gpd_nodes2.iloc[[idx]].copy()
        best1['distance'] = int(dist)
        best1[id_col] = p[id_col]

        ways1 = [n for n in response['elements'] if n['type'] == 'way']
        this_way = [{'waterway_id': w['id'], 'waterway_name': w['tags']['name']} for w in ways1 if best1['id'].iloc[0] in w['nodes'][:-1]][0]
        best1['waterway_id'] = this_way['waterway_id']
        best1['waterway_name'] = this_way['waterway_name']

        res_list.append(best1)

    res1 = pd.concat(res_list)
    return res1


def get_waterways(osm_nodes_from, waterway_type='natural'):
    """
    Function to get all the waterways connected by the node IDs derived from the get_nearest_waterways function from the OSM overpass server. Can specify the waterway type as either 'natural' or 'all'.

    Parameters
    ----------
    osm_nodes_from : GeoDataFrame
        Output GeoDataFrame from the get_nearest_waterways function with waterway nodes.
    waterway_type : str
        Either 'nautral' or 'all'.

    Returns
    -------
    Two Dicts
        of waterways and nodes.
    """
    q_node_base = "node({node});"

    if waterway_type == 'all':
        q_other_base = """complete {(way['waterway'](<); >;);};"""
    elif waterway_type == 'natural':
        q_other_base = """complete {(way['waterway'~'(river|stream|tidal_channel)'](<); >;);};"""
    else:
        raise ValueError('waterway_type must be either natural or all.')

    api = overpass.API()

    waterways = {}
    nodes = {}

    for index, p in osm_nodes_from.iterrows():
        if p.waterway_id in waterways:
            continue
#        print(p)
        q_node = q_node_base.format(node=p.id)
        q1 = q_node + q_other_base

        response = api.get(q1, responseformat='json')
        ww1 = {ww['id']: ww for ww in response['elements'] if (ww['type'] == 'way') and (ww['nodes'][0] != ww['nodes'][-1])}
        waterways.update(ww1)
        n1 = {n['id']: n for n in response['elements'] if n['type'] == 'node'}
        nodes.update(n1)

    return waterways, nodes


def waterway_delineation(osm_nodes_from, waterways, site_delineate='all'):
    """
    Function to delineate the waterways above each of the sites/nodes originally derived by the get_nearest_waterways function. Optional to delineate all the way up the waterway network or between the sites.

    Parameters
    ----------
    osm_nodes_from : GeoDataFrame
        Output GeoDataFrame from the get_nearest_waterways function with waterway nodes.
    waterways : dict
        First output dict from the get_waterways function.
    site_delineate : 'all' or 'between'
        Whether the waterway network should be dileated all the way to the top or only in between the sites.

    Returns
    -------
    Dict
        of each site/node each continaing the associated waterways and nodes.
    """
    site_delin = {}
    for index, p in osm_nodes_from.iterrows():
        new_wws = copy.deepcopy(waterways)

        if site_delineate == 'between':
            other_from = osm_nodes_from[osm_nodes_from.index != index]
            other_nodes = other_from.set_index('id')['waterway_id'].to_dict()

        site_ww = {p.waterway_id: waterways[p.waterway_id].copy()}
        site_ww_nodes1 = site_ww[p.waterway_id]['nodes']
        site_node_index = site_ww_nodes1.index(p.id)+1
        site_ww_nodes = site_ww_nodes1[:site_node_index]

        if site_delineate == 'between':
            other_ww = set(other_nodes.values())
            if site_ww[p.waterway_id]['id'] in other_ww:
                for o in list(other_nodes.keys()):
                    if o in site_ww_nodes:
                        site_ww_nodes = site_ww_nodes[(site_ww_nodes.index(o)+1):]
                    other_nodes.pop(o)

        site_ww[p.waterway_id]['nodes'] = site_ww_nodes

        ww_last = {ww[0]: ww[1]['nodes'][-1] for ww in new_wws.items()}

        if len(site_ww_nodes1) == site_node_index:
            big_set = set(site_ww_nodes[:-1])
        else:
            big_set = set(site_ww_nodes)

        set_len = len(big_set)

        while set_len > 0:
            index1 = [ww[0] for ww in ww_last.items() if ww[1] in big_set]
            new_ww = {i: new_wws[i] for i in index1}
            if site_delineate == 'between':
                if other_nodes:
                    other_ww = set(other_nodes.values())
                    for n1 in other_ww:
                        ww_nodes = new_ww[n1]['nodes']
                        for id1 in other_nodes:
                            if id1 in ww_nodes:
                                new_ww[n1]['nodes'] = ww_nodes[(ww_nodes.index(id1)+1):]
                            other_nodes.pop(id1)

            site_ww.update({i: new_ww[i] for i in index1})
            big_set = set()
            [big_set.update(set(new_ww[i]['nodes'][:-1])) for i in index1]
            set_len = len(big_set)

        site_delin.update({p.id: site_ww})

    return site_delin


def to_osm(site_delin, nodes):
    """
    Function to convert the output of the waterway_delineation function to a dict of dict in the OSM dict structure (for futher processing).

    Parameters
    ----------
    site_delin : dict
        Output of the waterway_delineation function.
    nodes : dict
        Second output of the get_waterways function.

    Returns
    -------
    Dict
        dict of dict in the OSM dict structure.
    """
    time1 = pd.Timestamp.now().isoformat()

    osm_delin = {}

    for id1, ww in site_delin.items():
        big_set = set()
        [big_set.update(set(v['nodes'])) for v in ww.values()]
        lotsanodes = [n for i, n in nodes.items() if i in big_set]
        lotsaways = [l for i, l in ww.items()]

        lots = []
        lots.extend(lotsanodes)
        lots.extend(lotsaways)

        dict1 = {'timestamp': time1, 'elements': lots}
        osm_delin.update({id1: dict1})

    return osm_delin


def to_gdf(osm_delin):
    """
    Function to convert the output of the to_osm function to a GeoDataFrame of the waterways associated with the sites/nodes.

    Parameters
    ----------
    osm_delin : dict
        Output of the to_osm function.

    Returns
    -------
    GeoDataFrame
    """
    shape1 = []

    for id1, osm1 in osm_delin.items():
        s1 = osm2geojson.json2shapes(osm1)
        l1 = [[id1, s['properties']['id'], s['properties']['tags']['name'], s['properties']['tags']['waterway'], s['shape']] for s in s1]
        shape1.extend(l1)

    df1 = pd.DataFrame(shape1, columns=['start_node', 'way_id', 'name', 'waterway', 'geometry'])
    gdf1 = gpd.GeoDataFrame(df1, crs=4326, geometry='geometry')

    return gdf1


def to_nx():
    """
    To be completed...convert to networkx. Look at osmnx...
    """


def pts_to_waterway_delineation(gdf_from, id_col, max_distance=500, waterway_type='natural', site_delineate='all'):
    """
    Function to fully perform the OSM waterway delineation process.

    Parameters
    ----------
    Parameters
    ----------
    gdf_from : GeoDataFrame
        Locations of the sites where you want to find the nearest waterway nodes.
    id_col : str
        The column name of the site ID for gdf_from.
    max_distance : int
        The maximum search distance.
    waterway_type : str
        Either 'nautral' or 'all'
    site_delineate : 'all' or 'between'
        Whether the waterway network should be dileated all the way to the top or only in between the sites.

    Returns
    -------
    Two GeoDataFrames
        The first is the GeoDataFrame of the nearest OSM waterway and node associated with the sites and the other is the one that contains the upstream delineated waterways.
    """
    pts1 = get_nearest_waterways(gdf_from, id_col, max_distance, waterway_type)
    waterways, nodes = get_waterways(pts1, waterway_type)
    site_delin = waterway_delineation(pts1, waterways, site_delineate)
    osm_delin = to_osm(site_delin, nodes)
    gdf1 = to_gdf(osm_delin)

    return pts1, gdf1








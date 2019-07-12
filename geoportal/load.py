import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}


# kyrgyz_mapping = {
#     'name_eng' : 'name_eng',
#     'lon' : 'lon',
#     'lat' : 'lat',
#     'geom' : 'MULTIPOLYGON',,
# }
    #
    # 'settlement' : 'settlement',
    # 'year_built' : 'year_built',
    # 'est_capaci' : 'est_capaci',
    # 'num_studen' : 'num_studen',
    # 'build_id' : 'build_id',
    # 'bdg_type' : 'bdg_type',
    # 'bdg_type_a' : 'bdg_type_a',


world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)
# worldshp = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), 'shape', 'kyrgyz_schools_utm43_v01.shp'),
# )

def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

# def running(verbose=True):
#     lm = LayerMapping(KyrgyzBorder, worldshp, kyrgyz_mapping, transform=False)
#     lm.save(strict=True, verbose=verbose)

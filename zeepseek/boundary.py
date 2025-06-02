import geopandas as gpd

# 1. Shapefile 불러오기 (.shp 파일 포함 전체 세트가 필요함)
data = gpd.read_file("seoul_boundary.shp")

# 2. GeoJSON으로 저장
data.to_file("seoul_boundary.geojson", driver='GeoJSON')

#!/bin/python
import argparse
from zipfile import ZipFile

import geopandas as gpd
from geopandas import GeoDataFrame


def statistik_for_period(year_greater_than: int, last_x_years: int):
    print("---")
    print(f"Statistik om senaste {last_x_years} årens inlagda växlar")
    mounted = gdf[gdf['Inlaggningsar_vaxel'] > year_greater_than]
    if type(mounted) != GeoDataFrame:
        print(type(mounted))
        print(mounted)
        raise TypeError("not a dataframe")
    print(f"Totalt inlagda i perioden: {len(mounted)}")
    counts = mounted['Inlaggningsar_vaxel'].value_counts().sort_index()
    print(f"Medelantal inlagd per år: {round(counts.mean())}")
    print(counts)
    # print(mounted.info())
    any_power_gdf = mounted[mounted['Varmeeffekt_kw_totalt'] > 0]
    # print(any_power_gdf.info())
    mean_value_above_zero = any_power_gdf['Varmeeffekt_kw_totalt'].mean()
    total_power_mounted = any_power_gdf['Varmeeffekt_kw_totalt'].sum()
    print(f"Medeleffekt: {round(mean_value_above_zero)} kW\n"
          f"Totaleffekt: {round(total_power_mounted)} kW\n")
    # power = mounted['Varmeeffekt_kw_totalt'].value_counts()
    # print(power)

# Create the argument parser
parser = argparse.ArgumentParser(description="Convert GeoPackage coordinates from SWEREF99TM to WGS84 and export to GeoJSON")

# Add the input and output file arguments
parser.add_argument("-i", "--input", help="Path to the input Zip file")
parser.add_argument("-o", "--output", help="Path to the output GeoJSON file")

# Parse the command-line arguments
args = parser.parse_args()

# Input and output file paths
input_zip = args.input
output_geojson = args.output

with ZipFile(input_zip) as myzip:
    print("Reading zip")
    with myzip.open(input_zip.split("/")[-1].replace("zip", "gpkg")) as mygpkg:
        print("Reading gpkg")
        #print(fiona.listlayers(mygpkg))
        #exit()
        layer_name = 'BIS_DK_O_3300_Sparvaxel'

        # Read the GeoPackage into a GeoDataFrame
        gdf = gpd.read_file(mygpkg, layer=layer_name)
        #print(gdf.info())

        # poster med okänd inkopplingsdatum före 2019
        datum = gdf[gdf['Inkopplingsdatum'] == "<20190405"]
        print(f"Totalt antal växlar i databasen: {len(gdf)}")
        percentage = round(len(datum)*100/len(gdf))
        print(f"Poster med okänd inkopplingsdatum före april 2019: {len(datum)} ({percentage}%)\n"
              f"OBS: Det här tyder på att Trafikverket i "
              f"dagsläget inte har bra koll på sina växlar alls. "
              f"Det här är mycket allvarligt eftersom växlarna ofta "
              f"orsakar stopp i tågtrafiken på vintern vid snöfall, frost, etc.\n\n"
              f"Dessa stopp orsakar problem för både resenärer och tågbolag, såhär skriver "
              f"SJ i sin årsredovisning från 2022: \n"
              f"'Kraftigt ökad tågtrafik har medfört att "
              f"kapacitetstaket på svensk järnvägsinfrastruktur överskridits. Tillsammans med "
              f"eftersatt underhåll medför det återkommande trafikstörningar. Den nationella planen "
              f"innebär att den redan höga underhållsskulden kommer att öka markant. Det riskerar att "
              f"medföra ännu fler trafikstörningar och att SJ inte kan leverera på sina kundlöften, "
              f"där en punktlig resa är prioriterad.'")


        # värmeeffekt
        any_power_gdf = gdf[gdf['Varmeeffekt_kw_totalt'] > 0]
        # print(any_power_gdf.info())
        mean_value_above_zero = any_power_gdf['Varmeeffekt_kw_totalt'].mean()
        print(f"Medeleffekt: {round(mean_value_above_zero)} kW\n"
              f"OBS: eftersom så många poster är inkompletta och Trafikverket "
              f"inte förklarat offentligt varför det är så är det inte en pålitlig siffra.")
        #power = gdf['Varmeeffekt_kw_totalt'].value_counts()
        #print(power)

        # inlagd
        year_mounted_gdf = gdf[gdf['Inlaggningsar_vaxel'] > 0]
        mean_value_above_zero = year_mounted_gdf['Inlaggningsar_vaxel'].mean()
        print(f"Medelår inlagd: {round(mean_value_above_zero)}. "
              f"OBS eftersom >18k poster saknar inläggningsår så är det här nog inte rätt alls")
        #year_mount = gdf['Inlaggningsar_vaxel'].value_counts()
        #print(year_mount)

        # inlagd senaste 20 åren
        statistik_for_period(year_greater_than=2002, last_x_years=20)
        # inlagd senaste 10 åren
        statistik_for_period(year_greater_than=2012, last_x_years=10)
        # inlagd senaste 5 åren
        statistik_for_period(year_greater_than=2017, last_x_years=5)

        # year_created = gdf['Tillverkningsar_vaxel'].value_counts()
        # print(year_created)

        #exit()
        # # Print the transformed GeoDataFrame
        # print(transformed_gdf)
        #
        # # Save the filtered features to a new GeoJSON file
        # print("Writing geojson")
        # transformed_gdf.to_file(output_geojson, driver="GeoJSON")


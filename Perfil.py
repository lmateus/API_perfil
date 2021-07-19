import argparse
import sys
from pyproj import CRS, Transformer
from osgeo import gdal
import numpy as np
import json

class Perfil():

    def __init__(self,Punto_inicial,Punto_final):
        self.Punto_inicial = Punto_inicial
        self.lat_1 = self.Punto_inicial[1]
        self.lon_1 = self.Punto_inicial[0]

        self.Punto_final = Punto_final
        self.lat_2 = self.Punto_final[1]
        self.lon_2 = self.Punto_final[0]
        

    def datos_perfil(self):

        dist = 1
        src= "DEM_05_wgs.tif"
        tif = ""

        ds = gdal.Open(src)

        if not ds:
            print("Could not open dataset.")
            sys.exit(1)
        
        # Set up coordinate transform
        proj_str = "+proj=tpeqd +lon_1={} +lat_1={} +lon_2={} +lat_2={}".format(self.lon_1, self.lat_1, self.lon_2, self.lat_2)
        tpeqd = CRS.from_proj4(proj_str)
        transformer = Transformer.from_crs(CRS.from_proj4("+proj=latlon"), tpeqd)

        # Transfor to tpeqd coordinates
        point_1 = transformer.transform(self.lon_1, self.lat_1)
        point_2 = transformer.transform(self.lon_2, self.lat_2)

        # Create an bounding box (minx, miny, maxx, maxy) in tpeqd coordinates
        width = 1
        bbox = (point_1[0], -(width*0.5), point_2[0], (width*0.5))

        # Calculate the number of samples in our profile.
        num_samples = int((point_2[0] - point_1[0]) / dist)
        
        # Warp it into dataset in tpeqd projection. If args.tif is empty GDAL will
        # interpret it as an in-memory dataset.
        format = 'GTiff' if tif else 'VRT'

        profile = gdal.Warp("", ds, dstSRS=proj_str, outputBounds=bbox, 
                            height=1, width=num_samples, resampleAlg="near", 
                            format=format)
        # Extract the pixel values and write to an output file
        data = profile.GetRasterBand(1).ReadAsArray()
        
        print("Created {}m profile with {} samples.".format(dist*num_samples, num_samples))

        elevation = data[0]
        distance = np.arange(len(elevation)) * dist
        
        profile_points = {
            'distancia_x': list(distance.astype('float')),
            'elevacion': list(elevation.astype('float'))
        } 
        # Todo lo de abajo es una prueba

        


        self.profile_json = profile_points
        
                

        
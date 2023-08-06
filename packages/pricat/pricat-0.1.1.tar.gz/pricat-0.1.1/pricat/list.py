#!/usr/bin/env python
# coding: utf-8

import json,sys, csv
import pandas as pd
import numpy as np
import io,os.path
import re
from datetime import datetime
import pkgutil

##import numpy as np



class List:
    ONLY_LIST_COLS = ["EAN", "BRAND_TEXT", "SUPPLIER_CODE", "TAX_ID", "TAX", "SUGGESTED_PRICE", "GROSS_PRICE", "GP_VALID_FROM", "NET_VALUE", "NV_VALID_FROM", "RECYCLING_FEE", "HEADER_CURRENCY"]

    COMMON_COLS = ["HEADER_COUNTRY","HEADER_DATE", "MDM_FILENAME", "MDM_TS_IMPORTED"]
    
    def __init__(self, pricat):
        self.list = pricat["list"]
        self.add_header_columns(pricat["header"])
        self.add_mdm_columns()

    def __load_db(self, sep=";"):
        dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/../csv"
        self.VEHICLE_TYPE  = pd.read_csv(os.path.join(dir, "VEHICLE_TYPE.csv"),  sep=sep)
        self.PRODUCT_TYPE1 = pd.read_csv(os.path.join(dir, "PRODUCT_TYPE1.csv"), sep=sep)
        self.PRODUCT_TYPE2 = pd.read_csv(os.path.join(dir, "PRODUCT_TYPE2.csv"), sep=sep)
        self.PRODUCT_TYPE2["PRODUCT_TYPE2"] = self.PRODUCT_TYPE2["PRODUCT_TYPE2"].astype(str)
        self.PRODUCT_TYPE3 = pd.read_csv(os.path.join(dir, "PRODUCT_TYPE3.csv"), sep=sep)

    def add_header_columns(self, header):
        self.list["HEADER_COUNTRY"] = header["COUNTRY"]
        self.list["HEADER_CURRENCY"] = header["CURRENCY"]
        self.list["HEADER_DATE"] = header["DATE"]
        self.list["MDM_FILENAME"] = header["MDM_FILENAME"]
        self.list["MDM_TS_IMPORTED"] = header["MDM_TS_IMPORTED"]
        
    def add_mdm_columns(self):
        self.list["MDM_SOURCE"] = "PRICAT"
        self.list["MDM_LOG"] = ""
        self.list["MDM_VALID_ROW"] = True
        
    def parser_required_fields(self, cols=["ASPECT_RATIO", "BRAND_TEXT", "DESIGN_1", "EAN", "GROSS_PRICE", "GP_VALID_FROM", "RIM_INCH", "SUPPLIER_CODE", "WIDTH_MM"]):
        result = 0
        tot_records = self.list.shape[0]
        for col in cols:
            if col not in self.list.columns:
                self.list["MDM_VALID_ROW"] = False
                self.list["MDM_LOG"] = self.list["MDM_LOG"] + "Missing column: %s\n" % col
            else:
                mask = self.list["MDM_VALID_ROW"] & pd.isnull(self.list[col])
                self.list["MDM_VALID_ROW"] = np.where(mask, False, self.list["MDM_VALID_ROW"])
                self.list["MDM_LOG"] = np.where(mask, self.list["MDM_LOG"] + "Missing value for column: %s\n" % col, self.list["MDM_LOG"])

    def parser_product_type(self):
        self.list["PRODUCT_TYPE"] = self.list["PRODUCT_TYPE"].astype(str)
        self.list["PRODUCT_TYPE1"] =  self.list["PRODUCT_TYPE"].apply(lambda x: str(x[0]) if x is not None and len(x) > 0 else "0")
        self.list["PRODUCT_TYPE2"] =  self.list["PRODUCT_TYPE"].apply(lambda x: str(x[1]) if x is not None and len(x) > 1 else "0")
        self.list["PRODUCT_TYPE3"] =  self.list["PRODUCT_TYPE"].apply(lambda x: str(x[2]) if x is not None and len(x) > 2 else "0")
        self.list = self.list.join(self.PRODUCT_TYPE1.set_index('PRODUCT_TYPE1'), on='PRODUCT_TYPE1')
        self.list = self.list.join(self.PRODUCT_TYPE2.set_index('PRODUCT_TYPE2'), on='PRODUCT_TYPE2')
        self.list = self.list.join(self.PRODUCT_TYPE3.set_index('PRODUCT_TYPE3'), on='PRODUCT_TYPE3')

    def parser_vehicle_type(self):
        self.list = self.list.join(self.VEHICLE_TYPE.set_index('VEHICLE_TYPE'), on='VEHICLE_TYPE')

    def parser(self):
        self.__load_db()
        self.parser_required_fields()
        self.parser_product_type()
        self.parser_vehicle_type()
        
    def parse(self, target_file=None, sep=";"):
        df = self.list
        ## drop  columns
        df = df.drop(columns=["POS", "POH"])

        list_cols = self.LIST_COLS + self.COMMMON.COLS
        product_cols = list(set(df.columns()) - set(self.LIST_COLS))
        list_df = df.select([list_cols])
        product_df = df.select([product_cols])
        
        ## Selezionare dalla colonna “Brand” i second brand ed eliminarne tutte le righe ( ex: Bridgestone = Firestone).  
       # filter_brands = df["BRAND"].isin(['BS', 'FS'])

    ## df["GROSS_PRICE"] =  df["GROSS_PRICE"].str.replace(',','.',regex=False)  
        ## Dalla colonna “Vehicle Type” cancellare quello che non è C0, L0, L4 e L5
        ##filter_vehicle_type = df["VEHICLE_TYPE"].isin(['C0', 'L0', 'L4', 'L5'])

        ##df[filter_brands & filter_vehicle_type]
    
        ## TODO
        ## Dalla Colonna Product Type cancella I valori superiori a 400. 
        ## '320', 'K', '200', '100', '300', '00f', '201', '00g'
    
        ## Cambia formato colonna “Ean” in formato numero senza decimali.  
        ##df["EAN"] = pd.to_numeric(df["EAN"])
        ##df["RIM_INCH"] = df["RIM_INCH"].astype(float)
        ## Da colonna “Supply Code”, solo per Continental,  creare una nuova colonna alla destra. Per i codici che iniziano con 15, fai un left a 7 cifre, mentre per gli altri left 6
     
        ## Da colonna “Product Info”, a destra creare tre colonne: “Oe Marking”, “Oe carmaker”, “Marking Brand Class”. Per compilare la prima e la seconda, fai una vlookup da file precedenti dalla colonna “Product Info”. Per compilare la colonna Marking Brand Class, utilizza la colonna Oe Carmaker. Incolla i valori e fai le seguenti modifiche:
        ## * a (*) 
        ## * MO a (*) (M0)*
        ## #N/A e 0 a " " 
    
        ## Creare colonna “Rim Band” a destra di colonna Rim (<=16, 17, >=18)
        ##df['RIM_BAND'] = df.apply(lambda row: None if type(row["RIM_INCH"]) == float and   np.isnan(row["RIM_INCH"]) else "<=16" if int(row["RIM_INCH"]) <= 16 else "17" if int(row["RIM_INCH"]) == 17 else ">=18" if int(row["RIM_INCH"]) >= 18 else "UNKNOWN",  axis=1)
        ## Da colonna SP1, trasformare tutto quello che è (Y) o ZR in Y. 
        
        ## Creare colonna “XL/std” a destra della colonna “RFD”. Compilarla in base alla colonna RFD. In particolare “Rfd” e “XL” à “XL” ,mentre ” “à “std” 
    
        ## Creare colonna “tech” e “r-f” a destra della colonna “Run_Flat”.
        ## Per determinare il contenuto delle colonne, è bene seguire  il seguente schema dei vari competitors, essendo le tecnologie chiamate in modo differente.  

        ## Seasonality:
     
        ## All Terrain:  fai vlookup da battistrada (colonna Design 1). Se viene N/a è il ruotino (solo Conti e Pirelli di solito, verificare perche non è una regola assoluta, nel caso cancella le righe). Incolla i valori e sostituisci gli 0 con “ “. 


        ## vehicle type : TODO: da mappare E0 M0, ...
        ##df['VEHICLE'] = df.apply(lambda row: "CAR" if row["VEHICLE_TYPE"] == "C0" else "SUV" if row["VEHICLE_TYPE"] in ["L4", "LS"] else "VAN" if row["VEHICLE_TYPE"] == "L0" else row["VEHICLE_TYPE"],  axis=1)

        self.list = df
        if target_file:
            self.save_to_csv(df, target_file, sep=sep)

    def save_to_csv(self, df, target_file, sep=";"):
        df.to_csv(target_file, sep=sep, index=False)


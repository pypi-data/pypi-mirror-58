#!/usr/bin/env python
# coding: utf-8

import json,sys, csv
import pandas as pd
import io,os.path
import re
from datetime import datetime

##import numpy as np



def convert_header(header):
    MAPPINGS = [ ["SPECIAL_COMPOUNT", "SPECIAL_COMPOUND"],
                 ["W_REFERENZE_CODE", "X_REFERENCE_CODE"],
                 ["COUNTRY_ID", "COUNTRY_CODE"],
                 ["NV_VALID_FROM", "NV_VALID"]
    ]
    
    ## removing blank spaces at the beginning/end. and converto to uppercase
    new_row = header.strip().upper()
    
    ## converting one or more consecutive spaces (tabs, spaces,) with one _
    new_row = re.sub("\s+", "_", new_row)
    
    ## removing "strange" and not printable and characters
    new_row = re.sub("[^A-Z0-9\(\);_\+/]+","", new_row)
    
    ## removing extra empty columns (;)
    new_row = re.sub(";+$","", new_row)
    
    ## renaming columns if...
    for  mapping in MAPPINGS:
        new_row = new_row.replace(mapping[0], mapping[1])

    return new_row

class File:
    TEMPLATES = [
            {"name": "B2",
             "rows": [convert_header("HDH;DOCUMENT_ID;DATE;CURRENCY;SUPPLIER_ILN;RECEIVER_ID;COUNTRY_ID;Ediwheel Version;C"),
                                    "HDS;0000000001;20190909;EUR;0000001303;113095;DE;B2;",
                                    convert_header("POH;POS;EAN;PROD_GRP_1;SUPPLIER_CODE;DESCRIPTION_1;DESCRIPTION_2;PROD_INFO;WDK_ANUB;WDK_BRAND;WDK_BRAND_TEXT;BRAND;BRAND_TEXT;PROD_GRP_2;GROUP_DESCRIPTION;WEIGHT;RIM_INCH;PROD_CYCLE;THIRD_PARTY;PL;TEL;EDI;ADHOC;PL_ID;URL_1;URL_2;URL_3;URL_4;URL_5;WIDTH_MM;WIDTH_INCH;ASPECT_RATIO;OVL_DIAMETER;CONSTRUCTION_1;CONSTRUCTION_2;USAGE;DEPTH;LI1;LI2;LI3(DWB);LI4(DWB);SP1;SP2;TL/TT;FLANK;PR;RFD;SIZE_PREFIX;COMM_MARK;RIM_MM;RUN_FLAT;SIDEWALL;DESIGN_1;DESIGN_2;PRODUCT_TYPE;VEHICLE_TYPE;COND_GRP;TAX_ID;TAX;SUGGESTED_PRICE;GROSS_PRICE;GP_VALID_FROM;NET_VALUE;NV_VALID;RECYCLING_FEE;NOISE_PERFORMANCE;NOISE_CLASS_TYPE;ROLLING_RESISTANCE;WET_GRIP;EC_VEHICLE_CLASS;EU_DIRECTIVE_NUMBER")
             ]
            },
            {"name": "B4",
             "rows": [convert_header("HDH;DOCUMENT_ID;DATE;CURRENCY;SUPPLIER_ILN;RECEIVER_ID;COUNTRY_CODE;EDIWHEEL_VERSION;C"),
                      "HDS;EW01A2;20190120;EUR;4019238000009;7201650;DE;B4.0;",
                      convert_header("POH;POS;EAN;PROD_GRP_1;SUPPLIER_CODE;DESCRIPTION_1;DESCRIPTION_2;PROD_INFO;RESERVED;M+S_MARK;3PMSF_MARK;BRAND;BRAND_TEXT;PROD_GRP_2;GROUP_DESCRIPTION;WEIGHT;RIM_INCH;PROD_CYCLE;THIRD_PARTY;PL;TEL;EDI;ADHOC;PL_ID;URL_1;URL_2;URL_3;URL_4;URL_5;WIDTH_MM;WIDTH_INCH;ASPECT_RATIO;OVL_DIAMETER;CONSTRUCTION_1;CONSTRUCTION_2;USAGE;DEPTH;LI1;LI2;LI3(DWB);LI4(DWB);SP1;SP2;TL/TT;FLANK;PR;RFD;SIZE_PREFIX;COMM_MARK;RIM_MM;RUN_FLAT;SIDEWALL;DESIGN_1;DESIGN_2;PRODUCT_TYPE;VEHICLE_TYPE;COND_GRP;TAX_ID;TAX;SUGGESTED_PRICE;GROSS_PRICE;GP_VALID_FROM;NET_VALUE;NV_VALID_FROM;RECYCLING_FEE;NOISE_PERFORMANCE;NOISE_CLASS_TYPE;ROLLING_RESISTANCE;WET_GRIP;EC_VEHICLE_CLASS;EU_DIRECTIVE_NUMBER;TRA_CODE;SEAL;SPECIAL_COMPOUND;DIRECTIONAL;ASYMETRIC;X_REFERENCE_CODE;MARKET_COMPLIANCE;WHEEL_POSITION;PRICE_REFERENCE_MATERIAL;RECOMMENDED_REPLACEMENT_ARTICLE;NON_GRADING_ELIGIBILITY;RFID;DESIGN_VARIANT")
             ]
            }
    ]
    def __init__(self, encoding="ISO-8859-1"):
        self.encoding = encoding
  
    def load_headers(self, filename, stream=None):
        if stream is None:
            stream_new =  open(filename, "r", encoding=self.encoding)
        else:
            stream_new = stream
        line1 = stream_new.readline()
        line2 = stream_new.readline()
        line3 = stream_new.readline()
        if stream is None:
            stream_new.close()
            
        return [convert_header(line1), line2, convert_header(line3)]

    def __compare_lines(self, line1, line3, expected_line1, expected_line3):
        result = {"status": "ko"}
    
        line1          = line1
        line3          = line3
        expected_line1 = expected_line1
        expected_line3 = expected_line3
    
        if expected_line1 in line1:
            result["status"] = "matching_header"
            if expected_line3 == line3:
                result["status"] = "ok"
            else:
                ## line3 not matching
                columns = line3.strip("\n").split(";")
                if '' in columns:
                    columns.remove('')
                expected_columns = expected_line3.strip("\n").split(";")
                result["line3_unexpected_columns"] = list(set(columns) - set(expected_columns))
                result["line3_missing_columns"] = list(set(expected_columns) - set(columns))
        else:
            ## line1 not matching
            columns = line1.strip("\n").split(";")
            expected_columns = expected_line1.strip("\n").split(";")
            result["line1_unexpected_columns"] = list(set(columns) - set(expected_columns))
            result["line1_missing_columns"] = list(set(expected_columns) - set(columns))
        return result

    def validate_files(self, dir):
        for filename in os.listdir(dir):
            if filename.lower().endswith("csv"):
                result = self.validate_file(os.path.join(dir,filename))
                print(filename)
                print(result)

    def validate_file(self, filename):
        lines = self.load_headers(filename)
        return self.validate_headers(lines)

    def validate_headers(self, lines):
        results = []
        for template in self.TEMPLATES:
            result = self.__compare_lines(lines[0], lines[2], template["rows"][0], template["rows"][2])
            if result['status'] == 'ok':
                result['version'] = template["name"]
                header_info = self.__extract_info_from_header(lines)
                result.update(header_info)
                return result
            else:
                results.append(result)

        return {"status": "ko", "results": results}

    def __extract_field_from_headers(self, fieldname, headers):
        cols = headers[0].split(";")
        vals = headers[1].split(";")
        try:
            index = cols.index(fieldname)
            result = vals[index]
        except:
            result = "NOT_FOUND"
        return result

    def __extract_info_from_header(self, lines):
        country = self.__extract_field_from_headers("COUNTRY_CODE", lines)
        currency = self.__extract_field_from_headers("CURRENCY", lines)
        head_version = self.__extract_field_from_headers("EDIWHEEL_VERSION", lines)
        date = self.__extract_field_from_headers("DATE", lines)
        return {"COUNTRY": country, "CURRENCY": currency, "EDIWHEEL_VERSION": head_version, "DATE": date}

    def split_file(self, filename, target_path):
        headers = self.load_headers(filename)
        info = self.__extract_info_from_header(headers)

        basename = os.path.basename(filename).replace(".csv","")
        header_filename = os.path.join(target_path, basename + "-head.csv")
        list_filename = os.path.join(target_path, basename + "-full-list.csv")
        with open(header_filename, "w") as header_writer:
                header_writer.write(headers[0])
                header_writer.write(headers[1])
        with open(filename, encoding=self.encoding) as reader:
            reader.readline()
            reader.readline()
            reader.readline()
            with open(list_filename, "w") as list_writer:
                list_writer.write(headers[2])
                for line in reader:
                    list_writer.write(line)
                    return [header_filename, list_filename]

    def load_file(self, filename, sep=";", stream=None):
        if stream is None:
            stream =  open(filename, "r", encoding=self.encoding)
        headers =  self.load_headers(filename, stream=stream)
        info =  self.__extract_info_from_header(headers)
        info["MDM_FILENAME"] = os.path.basename(filename)
        info["MDM_TS_IMPORTED"] = datetime.now()
        lines = [headers[2]] + stream.readlines()
        new_stream=io.StringIO("\n".join(lines))
        alist = self.__load_csv(new_stream, sep=sep)
        return {"header": info, "list": alist}

    def __load_csv(self, filename, sep=";"):
        return pd.read_csv(filename, sep=sep)

def save_to_csv(self, df, target_file, sep=";"):
    df.to_csv(target_file, sep=sep, index=False)

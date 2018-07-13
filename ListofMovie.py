# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import movieReview

def get_movie_list() :
    list12 = pd.read_excel("2012BO.xlsx")
    list13 = pd.read_excel("2013BO.xlsx")
    list14 = pd.read_excel("2014BO.xlsx")
    list15 = pd.read_excel("2015BO.xlsx")
    list16 = pd.read_excel("2016BO.xlsx")
    list17 = pd.read_excel("2017BO.xlsx")
    list18 = pd.read_excel("2018BO.xlsx")
    
    movie_name_list = list(list12['영화명']) + list(list13['영화명']) + list(list14['영화명']) + list(list15['영화명']) + list(list16['영화명']) + list(list17['영화명']) + list(list18['영화명'])
    movie_name_list = [str(i) if type(i)==int else i for i in movie_name_list]

    movie_year_list = list(list12['개봉일']) + list(list13['개봉일']) + list(list14['개봉일']) + list(list15['개봉일']) + list(list16['개봉일']) + list(list17['개봉일']) + list(list18['개봉일'])
    
    movie_year_list = [str(i)[:4] for i in movie_year_list]
    
    movie_list = list(zip(movie_name_list, movie_year_list))

    len(movie_list) # 700
    movie_list = list(set(movie_list))
    len(movie_list) # 675
    
    movie_list.sort()

    return movie_list




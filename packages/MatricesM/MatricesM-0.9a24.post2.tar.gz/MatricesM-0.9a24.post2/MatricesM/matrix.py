# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

from .validations import *
from .errors import *
from .constructors import *
from .customs import *

import re
from typing import Union,Tuple,List,Any,Dict,Optional

from random import random,randint,uniform,triangular,\
                   gauss,gammavariate,betavariate,   \
                   expovariate,lognormvariate,seed


class Vector:
    """
    Column vector

    data: list|list of lists|str; column data
    """
    def __init__(self,data):
        self._cMat = 0
        self._dfMat = 0
        self._fMat = 1
        self.__data = []

        #Data check
        if isinstance(data,(list,tuple)):
            self.__data = [[d] if not isinstance(d,list) else d for d in data]

        elif isinstance(data,str):
            from .setup.listify import _listify
            self.__data = _listify(self,data,True)

        else:
            raise TypeError(f"Can't use type {type(data).__name__} for 'data' parameter")

    @property
    def norm(self):
        return sum([i[0]**2 for i in self.__data])**(0.5) if self.d1==1 else None

    @property
    def dim(self):
        return [self.d0,1]
    @property
    def d0(self):
        return len(self.__data)
    @property
    def d1(self):
        return 1
    
    def __getitem__(self,ind):
        return self.__data[ind][0]

    def __setitem__(self,ind,val):
        self.__data[ind][0] = val

    def __repr__(self):
        return "\n"+"\n".join([str(val[0]) for val in self.__data])+f"\n\nsize: [{self.d0}x1]"

class Matrix(Vector):
    """
    dim: int OR list|tuple of 2 integers; dimensions of the matrix. Giving an integer creates assumes square matrix
    
    data: str|list of lists of values|list of values; Elements of the matrix.

    fill: Any; Fills the matrix with chosen distribution or the value, default is uniform distribution
          Available distributions:
            ->uniform,gauss,lognormvariate,triangular,gammavariate,betavariate,expovariate
          
    ranged: list|tuple of numbers OR dict{column names:list|tuple of numbers}; 
        Usage:
           ->To apply all the elements give a list | tuple
           ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
           ->Arguments should follow one of the following rules:
                1)If 'fill' is uniform --> [minimum,maximum]; 
                2)If 'fill' is gauss or lognormvariate --> [mean,standard_deviation];
                3)If 'fill' is triangular --> [minimum,maximum,mode];
                4)If 'fill' is gammavariate or betavariate --> [alpha,beta]
                5)If 'fill' is expovariate --> [lambda]

    features: list of strings|Label; column names
    
    seed: int; seed to use while generating random numbers, not useful when fill isn't a special distribution
    
    decimal: int; Digits to round to and print

    dtype: int|float|complex|dataframe; type of values the matrix will hold

    coldtypes: tuple|list of objects; data types for each column individually.

    index: Label|Matrix|list|tuple of objects; indices to use for rows. Only works if dtype is set to dataframe
    
    implicit: bool; Skip matrix setting operations if dimensions and elements are given

    NOTE:      
        --> Options: ROW_LIMIT:int,
                     PRECISION:int,
                     QR_ITERS:int,
                     EIGENVEC_ITERS:int,
                     NOTES:str,
                     DEFAULT_NULL:object,
                     DISPLAY_OPTIONS:dict,
                     DEFAULT_BOOL:dict

        --> Check https://github.com/MathStuff/MatricesM  for further explanation and examples
    

        --> Example look of a dataframe with multi-level column names and row labels

            *Default options
            *Arrows are just for indicating levels of labels


            
            +-Lvl1 row label 
            I   +-Lvl2 row label
            V   I
                V

            A_group|  A1      A2         <--Lvl 1 column name
            B_group|  B1  B2  B1      <--Lvl 2 column name
               M, N+------------
              M1,N1| 130  30  10
                 N2| 125  36  11
              M3,N2| 135  34  10
              M4,N1| 133  30   9
                 N2| 129  38  12
        
    """
    def __init__(self,
                 dim:Union[int,List[int],Tuple[int],None]=None,
                 data:Union[List[List[Any]],List[Any],Any]=[],
                 fill:Any=None,
                 ranged:Union[List[Any],Tuple[Any],Dict[str,Union[List[Any],Tuple[Any]]],None]=[0,1],
                 seed:int=None,
                 decimal:int=4,
                 dtype:Union[int,float,complex,dataframe]=float,
                 features:Union[List[str],Label]=Label(),
                 coldtypes:List[type]=[],
                 index:Union[List[Any],Tuple[Any],Label]=Label(),
                 implicit:bool=False,
                 **kwargs):

        #Constants to use for printing,rounding etc.
        self.ROW_LIMIT = 30                         #Upper limit for amount of rows to be printed with __repr__
        self.PRECISION = 6                          #Decimals to round
        self.QR_ITERS = 50                          #QR algorithm iterations for eigenvalues
        self.EIGENVEC_ITERS = 10                    #Shifted inverse iteration method iterations for eigenvectors
        self.NOTES = ""                             #Extra info to add to the end of the string used in __repr__
        self.DEFAULT_NULL = null                    #Object to use as invalid value indicator
        self.DIRECTORY = ""                         #Path of the Matrix in disk
        self.DEFAULT_BOOL = {                       #Values to use as boolean values
                            True:1,
                            False:0,
                            }
        self.BOOL_MAT = False                       #Wheter or not to treat matrix values as default boolean values provided
        self.DISPLAY_OPTIONS = {                    #Options and symbols used while displaying
                                "allow_label_dupes":False,
                                "dupe_place_holder":"//",
                                "label_seperator":",",
                                "left_top_corner":"+",
                                "left_seperator":"|",
                                "top_seperator":"-",
                                "col_place_holder":"...",
                                "row_place_holder":"...",
                               }

        
        #Basic attributes
        self.__features = features                  #Column names
        self.__coldtypes = coldtypes                #Column dtypes 
        self.__dim = dim                            #Dimensions
        self._matrix = data                         #Values
        self.__fill = fill                          #Filling method for the matrix
        self.__initRange = ranged                   #Given range for 'fill'
        self.__seed = seed                          #Seed to pick values from 
        self.__decimal = decimal                    #How many digits to display in decimal places
        self.__dtype = dtype                        #Type of the matrix
        self.__index = index                        #Column to use as index column
        self.__implicit = implicit                  #Implicity value
        self._cMat,self._fMat,self._dfMat = 0,0,0   #Types

        ######Overwrite attributes######
        if kwargs != {}:
            overwrite_attributes(self,kwargs)
        ################################
        self.defaults = {                           #Save default arguments for __call__
                         "dim":dim,
                         "data":data,
                         "fill":fill,
                         "ranged":ranged,
                         "seed":seed,
                         "decimal":decimal,
                         "dtype":dtype,
                         "features":features,
                         "coldtypes":coldtypes,
                         "index":index,
                         "ROW_LIMIT":self.ROW_LIMIT,
                         "PRECISION":self.PRECISION,
                         "QR_ITERS":self.QR_ITERS,
                         "EIGENVEC_ITERS":self.EIGENVEC_ITERS,
                         "NOTES":self.NOTES,
                         "DEFAULT_NULL":self.DEFAULT_NULL,
                         "DISPLAY_OPTIONS":self.DISPLAY_OPTIONS,
                         "DEFAULT_BOOL":self.DEFAULT_BOOL
                        }

        #Set/fix attributes
        self._setDim(self.__dim)           #Fix dimensions
        self.setInstance(self.__dtype)     #Store what type of values matrix can hold

        #For the favor of better results, increase iterations for odd numbered dimensions
        # if self.QR_ITERS < 250:
        #     self.QR_ITERS += 400*(self.__dim[0]%2)  
        
        #Setup the matrix and column names,types
        self.setup(True,self.__implicit)
        
# =============================================================================
    """Attribute formatting and setting methods"""
# =============================================================================    
    def __getattr__(self,attr:str):
        """
        Column names can be treated as attribute names

        Example:

            >>> df
                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
            this_group_2,that_class_3|      0        1        1       -1
            this_group_3,that_class_2|     -1       -2        0        2
            this_group_1,that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
            this_group_2,that_class_3|      1        1       -2        1
            this_group_3,that_class_2|      0        2        0       -1
            this_group_1,that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2
            this_group_2,that_class_3|      0       -1       -1        2

            >>> df.groups.group_3    #Short way of using df.colname["groups"].name["group_3"]

                               groups|group_3
                              classes|class_2
                    this,        that+-------
            this_group_1,that_class_1|     -1
            this_group_2,that_class_3|      1
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|      1
            this_group_2,that_class_3|     -2
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|     -2
            this_group_2,that_class_3|     -1

            n:10,type:int,invalid:0
            
        """
        try:
            #Ignore some of the weird ipython methods 
            if attr in ["_ipython_canary_method_should_not_exist_",
                        "_repr_mimebundle_",]:
                return None
            return object.__getattribute__(self,attr)
        except:
            try:
                if attr == "_Matrix__use_value_based_comparison":
                    return False
                
                #Try as column label name
                if attr in self.features.names:
                    return self.level[self.features.names.index(attr)+1].name

                #Try as a level-1 column name
                return self.level[1].name[attr]

            except MatrixError:#Nothing worked ¯\_(ツ)_/¯
                raise AttributeError(f"'{attr}' is not a column name nor an attribute or a method of Matrix")

    def setup(self,first:bool,implicit:bool=False):
        """
        Process and validate object's initial attributes, shouldn't be manually called 
        unless something went wrong while using the object

        first:bool, wheter or not it's the first time running the setup for the object
        implicit:bool, implicity of the given attributes
        """
        from .setup.argpro import _setup
        _setup(self,first,implicit,Label,Matrix,validlist)

    def setInstance(self,dt:Union[int,float,complex,dataframe]):
        """
        Set the type
        """
        self._fMat = 1 if (dt in [complex,float]) else 0
        self._cMat = 1 if (dt == complex) else 0
        self._dfMat = 1 if (dt == dataframe) else 0 
               
    def _setDim(self,d:Union[int,list,tuple]):
        """
        Set the dimension to be a list if it's an integer
        """
        valid = 0
        if isinstance(d,int):
            if d>=1:
                self.__dim=[d,d]
                valid = 1
        elif isinstance(d,(list,tuple)):
            if len(d)==2:
                if isinstance(d[0],int) and isinstance(d[1],int):
                    if d[0]>0 and d[1]>0:
                        self.__dim=list(d)
                        valid = 1
        if not valid:
            self.__dim = [0,0]
        
    def setMatrix(self,
                  dim:Union[int,list,tuple,None]=None,
                  ranged:Union[List[Any],Tuple[Any],Dict[str,Union[List[Any],Tuple[Any]]],None]=None,
                  lis:Union[List[List[Any]], List[Any]]=[],
                  fill:Any=uniform,
                  cmat:bool=False,
                  fmat:bool=True):
        """
        Set the matrix based on the arguments given
        """
        from .setup.matfill import _setMatrix
        _setMatrix(self,dim,ranged,lis,fill,cmat,fmat,uniform=uniform,seed=seed,null=self.DEFAULT_NULL)

    def fix_coldtypes(self,column:Union[Tuple[str],List[Any],str,None]=None,return_dtype=False):
        """
        Returns a type object or a list of type objects
        Guesses the dtype for the given column, or all columns

        column:column indices,str,None; Name of the column to guess dtype of, None to guess all
        return_dtype:bool; False to apply new dtypes, True to return dtype guesses without applying
        """
        from .setup.declare import declareColdtypes
        from .matrixops.getsetdel import getitem

        column = slice(None) if column == None \
                 else list(column) if isinstance(column,range) \
                 else column

        colinds = list(getitem(self,(slice(None),column),Matrix,returninds=True)[1]) #Get integer indices
        colds = declareColdtypes([[row[j] for j in colinds] for row in self.matrix]) #Get guesses
        if return_dtype:
            return colds if len(colds)>1 else colds[0]
        
        #Apply new guesses
        for i,j in enumerate(colinds):
            self.__coldtypes[j] = colds[i]

# =============================================================================
    """Attribute recalculation methods"""
# =============================================================================    
    def _declareDim(self):
        """
        Set new dimension 
        """
        from .setup.declare import declareDim
        return declareDim(self)
    
    def _declareRange(self,lis:Union[List[List[Any]], List[Any] ]):
        """
        Finds and returns the range of the elements in a given list
        """
        from .setup.declare import declareRange
        return declareRange(self,lis,dataframe)

# =============================================================================
    """Element setting methods"""
# =============================================================================
    def _listify(self,stringold:str):
        """
        Finds all the numbers in the given string
        """
        from .setup.listify import _listify
        return _listify(self,stringold,False)
            
    def _stringfy(self,coldtypes:Union[List[Any],None]=None,returnbounds:bool=False,grid:bool=False):
        """
        Turns a list into a grid-like form that is printable
        Returns a string
        """
        from .setup.stringfy import _stringfy
        return _stringfy(self,coldtypes,returnbounds,grid)

# =============================================================================
    """Row labels used as indices"""
# =============================================================================
    @property
    class level:
        def __init__(self,mat):
            if not mat._dfMat:
                raise TypeError("Can't use label indexing with non-dataframe matrices") 
            self.mat = mat

        def __getitem__(self,pos):
            if not isinstance(pos,int):
                raise TypeError("Level can't be non-int")
            if pos <=0:
                raise ValueError("Level can't be lower than 1")
            
            self.level = pos
            return self

        @property
        class name:
            def __init__(self,parent):
                self.mat = parent.mat
                self.level = parent.level
                self.df = parent.mat._dfMat

            def __getattr__(self,attr:str):
                try:
                    return object.__getattribute__(self,attr)
                except:
                    try:
                        return self[attr]
                    except:
                        raise AttributeError(f"{attr} is not a column name nor an attribute of 'name' class")

            def __getitem__(self,pos):
                """
                Using row indices/labels:
                    --> Use it after sorting the dataframe for the best results for slices
                    
                    >>> df = dataframe()    #Constructor

                    >>> df.level[1].name['core_a']   #Returns all the rows where the level 1 column name is 'core_a'

                    >>> df.level[3].name['layer_1','layer_5','none']   #Returns all the rows where 
                                                                        level 3 row label's are
                                                                        one of ['layer_1','layer_5','none'] 

                    >>> df.level[2].name["sub2":"sub5"]    #Return all the rows with first 'sub2' column name appearance
                                                            until 'sub5' s first appearance on level 2 column names
                    
                """
                from .matrixops.getsetdel import getitem
                return getitem(mat=self.mat,
                               pos=pos,
                               obj=Matrix,
                               usename=True,
                               namelevel=self.level)

            def __setitem__(self,pos,val):
                from .matrixops.getsetdel import setitem
                setitem(mat=self.mat,
                        pos=pos,
                        item=val,
                        obj=Matrix,
                        usename=True,
                        namelevel=self.level)

            def __delitem__(self,val:object):
                """
                Works 'similar' to __getitem__ , but can only be used to delete columns 
                Example:
                    >>> del Matrix.level[2].name["core_a","core_c"]   #Delete all rows with level 1 row labeled "core_a" and "core_c"
                """
                from .matrixops.getsetdel import delitem
                delitem(mat=self.mat,
                        pos=val,
                        obj=Matrix,
                        usename=True,
                        namelevel=self.level)  

        @property
        class ind:
            def __init__(self,level_class):
                self.mat = level_class.mat
                self.level = level_class.level
                self.df = level_class.mat._dfMat

            def __getitem__(self,pos):
                """
                Using row indices/labels:
                    --> Use it after sorting the dataframe for the best results for slices
                    
                    >>> df = dataframe()    #Constructor

                    >>> df.level[1].ind["pending"]   #Returns all the rows where the row label at level 1 is 'pending'

                    >>> df.level[3].ind[1990,"Score"]   #Returns the 'Score' column of all the rows where level 3 row label is 1990

                    >>> df.level[2].ind[50:150]    #Return the rows with index higher than 50 and less than 150 in level 2 row labels
                                                   #starts and stops with limits' first appearances
                                                            
                    >>> df.level[1].ind["Average":,"Final_Score"]   #Return the rows' 'Final_Score' columns from where the level 1 
                                                                    #labels start from 'Average'
                    
                """
                from .matrixops.getsetdel import getitem
                return getitem(mat=self.mat,
                               pos=pos,
                               obj=Matrix,
                               uselabel=1,
                               rowlevel=self.level)

            def __setitem__(self,pos,val):
                from .matrixops.getsetdel import setitem
                setitem(mat=self.mat,
                        pos=pos,
                        item=val,
                        obj=Matrix,
                        uselabel=1,
                        rowlevel=self.level)

            def __delitem__(self,val:object):
                """
                Works 'similar' to __getitem__ , but can only be used to delete rows
                Example:
                    >>> del Matrix.level[1].ind["parrot"]     #Delete all rows with level 1 row labeled "parrot"
                """
                from .matrixops.getsetdel import delitem
                delitem(mat=self.mat,
                        pos=val,
                        obj=Matrix,
                        uselabel=1,
                        rowlevel=self.level)  

    @property
    class rowname:
        """
        Use Label object's column names for indexing to get filter matrix's rows

        Example:

            >>> df
                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
            this_group_2,that_class_3|      0        1        1       -1
            this_group_3,that_class_2|     -1       -2        0        2
            this_group_1,that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
            this_group_2,that_class_3|      1        1       -2        1
            this_group_3,that_class_2|      0        2        0       -1
            this_group_1,that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2
            this_group_2,that_class_3|      0       -1       -1        2

            >>> df.rowname["this"].ind["this_group_1"] #Same as df.level[1].ind["this_group_1"]

                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
                      // that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
                      // that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2


        NOTE:

        -> Since '__getitem__' is returning a Matrix.level object, following calls will return the same results

                >>> df.level[1].name["group_3"]

                >>> df.rowname["this"].name["group_3"]

                #Because 'this' is the level-1 of the row label names

        """
        def __init__(self,mat):
            if not mat._dfMat:
                raise TypeError("Can't use row name indexing with non-dataframe matrices") 
            self.mat = mat

        def __getitem__(self,pos):
            if not isinstance(pos,str):
                raise TypeError("Row label column name can't be non-str")

            if not pos in self.mat.index.names:
                raise TypeError(f"{pos} is not a row label column name")

            lvl = self.mat.index.names.index(pos) + 1
            return self.mat.level[lvl]

    @property
    class colname:
        """
        Use Label object's column names for indexing to get filter matrix's columns
        
        Example:

            >>> df
                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
            this_group_2,that_class_3|      0        1        1       -1
            this_group_3,that_class_2|     -1       -2        0        2
            this_group_1,that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
            this_group_2,that_class_3|      1        1       -2        1
            this_group_3,that_class_2|      0        2        0       -1
            this_group_1,that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2
            this_group_2,that_class_3|      0       -1       -1        2

            >>> df.colname["groups"].name["group_3"]

                               groups|group_3
                              classes|class_2
                    this,        that+-------
            this_group_1,that_class_1|     -1
            this_group_2,that_class_3|      1
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|      1
            this_group_2,that_class_3|     -2
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|     -2
            this_group_2,that_class_3|     -1

            n:10,type:int,invalid:0

        """
        def __init__(self,mat):
            if not mat._dfMat:
                raise TypeError("Can't use column name indexing with non-dataframe matrices") 
            self.mat = mat

        def __getitem__(self,pos):
            if not isinstance(pos,str):
                raise TypeError("Column names can't be non-str")

            if not pos in self.mat.features.names:
                raise TypeError(f"{pos} is not a name for column name rows")

            lvl = self.mat.features.names.index(pos) + 1
            return self.mat.level[lvl]

# =============================================================================
    """Row/Column methods"""
# =============================================================================
    
    def head(self,rows:int=5):
        """
        First 'rows' amount of rows of the matrix
        Returns a matrix
        rows : integer>0 | How many rows to return
        """
        if not isinstance(rows,int):
            raise InvalidIndex(rows,"Rows should be a positive integer number")
        if rows<=0:
            raise InvalidIndex(rows,"rows can't be less than or equal to 0")
        if self.d0>=rows:
            return self[:rows]
        return self[:,:]

    def tail(self,rows:int=5):
        """
        Last 'rows' amount of rows of the matrix
        Returns a matrix
        rows : integer>0 | How many rows to return
        """
        if not isinstance(rows,int):
            raise InvalidIndex(rows,"Rows should be a positive integer number")
        if rows<=0:
            raise InvalidIndex(rows,"rows can't be less than or equal to 0")
        if self.d0>=rows:
            return self[self.d0-rows:]
        return self[:,:]

    def col(self,column:Union[List[Union[int,str]],int,str],
            as_matrix:bool=True,
            namelevel:int=1):
        """
        Get a specific column of the matrix
        Returns a Matrix or a list

        column:integer>=1 and <=column_amount | column name | list of column names/indices(starting from 0)/names in tuples
        as_matrix:False to get the column as a list, True to get a column matrix (default) 
        namelevel:int>=1, Level of the labels to search the given column names 

        NOTE:
            >>> Matrix.col(1) == Matrix.col([0]) == Matrix.col((0,))
        """

        #Column number given
        if isinstance(column,int):
            if not (column<=self.d1 and column>0):
                raise InvalidColumn(column,"Column index out of range")
            
            #Return matrix
            if as_matrix:
                return self[:,column-1]

        #Column name given
        elif isinstance(column,str):
            if not column in self.features.get_level(namelevel):
                raise InvalidColumn(column,f"'{column}' is not in level-{namelevel} column names")

            #Return matrix
            if as_matrix:
                return self[:,column]

            column = self.features.index(column)+1

        #List of column names and column numbers given
        elif isinstance(column,(tuple,list)):
            d0,d1 = self.dim
            feats = self.features.labels
            feats_specific_lvl = self.features.get_level(namelevel)

            #Single tuple given
            if isinstance(column,tuple):
                colinds = [j for j,label in enumerate(feats) if label==column]
            #Combination of column names, numbers and tuple names given
            else:
                if not all([1 if isinstance(num,(int,str)) else 0 for num in column]):
                    raise TypeError("Given list should only contain integers>0 or strings or tuples")
                colinds = [i if isinstance(i,int) \
                           else feats.index(i) if isinstance(i,tuple)\
                           else feats_specific_lvl.index(i) \
                           for i in column]
            if as_matrix:
                return self[:,colinds]

            mm = self._matrix
            temp = []
            for i in range(d0):
                row = mm[i]
                temp.append([row[j] for j in colinds])
                
            return temp
        
        #Invalid type
        else:
            raise InvalidColumn(column)

        #Return list
        mm = self._matrix
        return [mm[r][column-1] for r in range(self.d0)]
    
    def row(self,row:Union[List[int],int]=None,as_matrix:bool=True):
        """
        Get a specific row of the matrix
        Returns a Matrix or a list

        row:int>=1 and <=row_amount | list of integers; row number(s) 
        as_matrix:False to get the row as a list, True to get a row matrix (default) 
        """
        if isinstance(row,int):
            if not (row<=self.d0 and row>0):
                raise InvalidIndex(row,"Row index out of range")
            row -= 1

        elif isinstance(row,(tuple,list)):
            if not all([1 if isinstance(num,int) else 0 for num in row]):
                raise  TypeError("Given list should only contain integers")
            
        else:
            raise InvalidIndex(row)

        if as_matrix:
            return self[row]
        return self._matrix[row][:]
                    
    def add(self,lis:List[Any],
            row:Union[int,None]=None,
            col:Union[int,None]=None,
            feature:Union[str,None]=None,
            dtype:Any=None,
            index:Any="",
            returnmat:bool=False,
            fillnull=True):
        """
        Add a row or a column of numbers

        lis: list; list of objects desired to be added to the matrix
        row: int>=1; row index
        col: int>=1; column index
        feature:str; new column's name
        dtype: type; type of data the new column will hold, doesn't work if a row is inserted
        returnmat:bool; wheter or not to return self
        fillnull:bool; wheter or not to use null object to fill values in missing indices

        To append a row, use row=self.d0
        To append a column, use col=self.d1
        """
        from .matrixops.add import add
        add(self,lis,row,col,feature,dtype,index,fillnull)
        if returnmat:
            return self

    def remove(self,row:int=None,col:int=None,returnmat:bool=False):
        """
        Deletes the given row and/or column

        row:int>=1
        col:int>=1
        returnmat:bool; wheter or not to return self
        """
        from .matrixops.remove import remove
        remove(self,self.d0,self.d1,row,col)
        if returnmat:
            return self  

    def concat(self,matrix:object,axis:[0,1]=1,returnmat:bool=False,fillnull=True):
        """
        Concatenate matrices row or columns vice

        matrix:Matrix; matrix to concatenate to self
        axis:0|1; 0 to add 'matrix' as rows, 1 to add 'matrix' as columns
        returnmat:bool; wheter or not to return self
        fillnull:bool; wheter or not to use null object to fill values in missing indices
        """
        from .matrixops.concat import concat
        concat(self,matrix,axis,fillnull,Matrix)
        if returnmat:
            return self
            
    def delDim(self,num:int):
        """
        Removes desired number of rows and columns from bottom right corner
        """        
        from .matrixops.matdelDim import delDim
        delDim(self,num)

    def swap(self,swap:Union[int,str,Tuple[str]],to:Union[int,str,Tuple[str]],axis:[0,1]=1,returnmat:bool=False):
        """
        Swap two rows or columns

        swap: int>0|str; row/column number or column name
        to: int>0|str; row/column number or column name
        axis: 0|1; 0 for row swap, 1 for column swap
        returnmat: bool; wheter or not to return self after evaluation

        Example:

            #Swap col_1 and col_3 columns
            >>> Matrix.swap(swap="col_1",to="col_3")

            #Swap 4th row with 1552nd row
            >>> Matrix.swap(swap=4,to=1552,axis=0)

        NOTE:
            -> Swapping columns also swap their names and dtypes
            -> Swapping rows also swap their row labels

        """
        def indexer(value,feats,limit):
            if isinstance(value,int):
                assert ((value>0) and (value<=limit)), f"0<index_value<={limit}"
                return value-1
            return feats.index(value) if isinstance(value,str) else\
                   feats.labels.index(value) if isinstance(value,tuple) else\
                   None

        feats = self.features[:]
        rowlabels = self.index
        swap = indexer(swap,feats,self.d1)
        to = indexer(to,feats,self.d1)

        assert None not in [swap,to], "Indices can only be one of (int,str,tuple) types"
        assert axis in [0,1], "axis should be 0 for row swap, 1 for column swap"

        if axis==0:#Row swap
            self._matrix[swap],self._matrix[to] = self._matrix[to][:],self._matrix[swap][:]
            if self._dfMat:
                self.__index[swap],self.__index[to] = self.__index[to],self.__index[swap]
        else:
            self[:,swap],self[:,to] = self[:,to],self[:,swap]
            self.__coldtypes[swap],self.__coldtypes[to] = self.__coldtypes[to],self.__coldtypes[swap]
            self.__features[swap],self.__features[to] = self.__features[to],self.__features[swap]

        if returnmat:
            return self

    def setdiag(self,val:Union[Tuple[Any],List[Any],object],returnmat:bool=False):
        """
        Set new diagonal elements

        val:Any; object to set as new diagonals. 
            -> If a Matrix is given, new diagonals are picked as given matrix's diagonals
            -> If a list/tuple is passed, it should have the length of the smaller dimension of the matrix
            -> Any different value types are treated as single values, all diagonal values get replaced with given object
        
        returnmat:bool ; wheter to return self after evaluations
        """
        expected_length = min(self.dim)
        if isinstance(val,Matrix):
            if min(val.dim)!=expected_length:
                raise DimensionError(f"Expected {expected_length} diagonal elements, got {min(val.dim)}.")

            for i in range(expected_length):
                self._matrix[i][i] = val.matrix[i][i]

        elif isinstance(val,(list,tuple)):
            if len(val) != expected_length:
                raise DimensionError(f"Expected {expected_length} elements, got {len(val)}.")

            for i in range(expected_length):
                self._matrix[i][i] = val[i]

        else:
            for i in range(expected_length):
                self._matrix[i][i] = val
        
        if returnmat:
            return self
    
    def drop_null(self,axis=0,returnmat=False):
        """
        Remove rows or columns with default null values

        axis: 0|1; 0 to drop rows, 1 to drop columns with null values
        returnmat: bool; wheter to return self after evaluations
        """
        if not self._dfMat:
            raise TypeError("Can't drop null values from non-dataframe matrices")
        
        assert axis in [0,1] , "'axis' should be 0 for rows, 1 for columns"

        def_null = self.DEFAULT_NULL
        null_indices = self.find(def_null,0,False)

        #Drop rows
        if axis == 0:
            row_inds = list(set([i for i,j in null_indices]))
            for leap,i in enumerate(row_inds):
                del self._matrix[i-leap]
                del self.__index[i-leap]

            self.__dim[0] -= len(row_inds)
    
        #Drop columns
        else:
            col_inds = list(set([j for i,j in null_indices]))
            for row in range(self.d0):
                for leap,j in enumerate(col_inds):
                    del self._matrix[row][j-leap]
            
            for leap,j in enumerate(col_inds):
                del self.__features[j-leap]
            
            self.__dim[1] -= len(col_inds)

        if returnmat:
            return self

    def fill_null(self,item,returnmat=False):
        """
        Replace null values with the given object

        item: Any; Value to replace null values with
        """
        return self.replace(self.DEFAULT_NULL,item,returnmat=returnmat)
        
# =============================================================================
    """Methods for special matrices and properties"""
# =============================================================================     
    def _determinantByLUForm(self):
        """
        Determinant calculation from LU decomposition
        """
        return self._LU()[1]

    def _transpose(self,hermitian:bool=False):
        """
        Returns the transposed matrix
        hermitian : True|False ; Wheter or not to use hermitian transpose method
        """
        from .linalg.transpose import transpose
        return transpose(self,hermitian,obj=Matrix,labelobj=Label)

    def minor(self,row:int,col:int,returndet:bool=True):
        """
        Returns the minor of the element in the desired position
        row,col : row and column indices of the element, 1<=row and col
        returndet : True if the determinant is wanted, False to return the matrix the determinant is calculated from 
        """
        from .linalg.minor import minor
        return minor(self,row,col,returndet)

    def _adjoint(self):
        """
        Returns the adjoint matrix
        """
        from .linalg.adjoint import adjoint
        dt = complex if self.dtype==complex else float
        return Matrix(self.dim,adjoint(self),dtype=dt,implicit=True)
    
    def _inverse(self):
        """
        Returns the inversed matrix
        """
        from .linalg.inverse import inverse
        return inverse(self,Identity(self.d0))

    def _Rank(self):
        """
        Returns the rank of the matrix
        """
        return self._rrechelon()[1]
    
    def nilpotency(self,limit:int=50):
        """
        Value of k for (A@A@A@...@A) == 0 where the matrix is multipled by itself k times, k in (0,inf) interval
        limit : integer | upper bound to stop iterations
        """
        from .linalg.nilpotency import nilpotency
        return nilpotency(self,limit)
    
    def _eigenvals(self):
        """
        Returns the eigenvalues using QR algorithm
        """
        from .linalg.eigen import _eigenvals
        return _eigenvals(self,roundto)

    def _eigenvecs(self,iters,alpha=1+1e-5):
        """
        Returns the eigenvectors, eigenvector matrix and diagonal matrix
        """
        from .linalg.eigen import _eigenvecs
        return _eigenvecs(self,iters,alpha,Identity,Matrix)

# =============================================================================
    """Decomposition methods"""
# ============================================================================= 
    def _rrechelon(self,rr:bool=True):
        """
        Returns reduced row echelon form of the matrix
        """
        from .linalg.rrechelon import rrechelon
        return rrechelon(self,[a[:] for a in self._matrix],Matrix,rr)
                    
    def _symDecomp(self):
        """
        Decompose the matrix into a symmetrical and an antisymmetrical matrix
        """
        from .linalg.symmetry import symDecomp
        return symDecomp(self,Matrix(self.dim,fill=0))
    
    def _LU(self):
        """
        Returns L and U matrices from LU decomposition
        """
        from .linalg.LU import LU
        return LU(self,Identity(self.d0).matrix,[a[:] for a in self.matrix],Matrix)

    def _QR(self):
        """
        Returns Q and R matrices from QR decomposition
        """
        from .linalg.QR import QR
        return QR(self,Matrix)
    
    def _EIGENDEC(self):
        """
        Returns eigenvecmat, diagmat and the inverse eigenvecmat from eigenvalue decomposition
        """
        results = self._eigenvecs(self.EIGENVEC_ITERS)
        if results in [None,[]]:
            return (None,None,None)
        return (results[1],results[2],results[1].inv)

    def _SVD(self):
        """
        Singular value decomposition, Matrix = U@E@V.ht
        """
        from .linalg.SVD import _SVD
        return _SVD(self)

    def _hessenberg(self):
        pass
    
# =============================================================================
    """Basic properties"""
# =============================================================================  
    @property
    def p(self):
        print(self)
   
    @property
    def grid(self):
        print(self.string)
    
    @property
    def copy(self):
        return Matrix(**self.kwargs)

    @property
    def string(self):
        return self._stringfy(coldtypes=self.coldtypes[:],grid=True)

    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self,li:Union[List[str],Tuple[str]]):
        if isinstance(li,Label):
            assert len(li) == self.d1 , f"Expected {self.d1} labels, got {len(li)} instead."
            
            str_labels = [tuple([str(lbl) for lbl in row]) for row in li.labels]    
            temp = Label(str_labels,li.names)

        elif not isinstance(li,(list,tuple)):
            raise NotListOrTuple(li)
        
        else:
            if len(li) != self.d1:
                raise InvalidList(li,self.d1,"column names")

            temp = []
            for i in range(len(li)):
                name = li[i]
                while name in temp:
                    name = "_"+name
                temp.append(name)

            temp = Label(temp)

        self.__features=temp
                
    @property
    def dim(self):
        return self.__dim
    @dim.setter
    def dim(self,val:Union[int,List[int],Tuple[int]]):
        amount = self.__dim[0]*self.__dim[1]
        if isinstance(val,int):
            assert val>0 , "Dimensions can't be <=0"
            val=[val,val]
        elif isinstance(val,list) or isinstance(val,tuple):
            assert len(val)==2 , f"Matrices accept 2 dimensions, {len(val)} length {type(val)} type can't be used."
        else:
            raise TypeError("dim setter only accepts int>0 or list/tuple with length of 2")

        assert val[0]*val[1]==amount , f"{amount} elements can't fill a matrix with {val} dimensions"

        m = self.matrix
        els=[m[i][j] for i in range(self.d0) for j in range(self.d1)]
        temp=[[els[c+val[1]*r] for c in range(val[1])] for r in range(val[0])]
        self.__init__(dim=list(val),data=temp,dtype=self.dtype,implicit=True)
    
    @property
    def d0(self):
        return self.__dim[0]
    @property
    def d1(self):
        return self.__dim[1]

    @property
    def fill(self):
        return self.__fill
    @fill.setter
    def fill(self,value:[object]):
        try:
            spec_names = ["method","function","builtin_function_or_method",self.DEFAULT_NULL.__name__]
            assert (type(value).__name__ in spec_names) \
                or (type(value) in [int,str,float,complex,range,list]) \
                or  value==None
        except AssertionError:
            raise FillError(value)
        else:
            self.__fill=value
            self.setMatrix(self.__dim,self.__initRange,[],value,self._cMat,self._fMat)

    @property
    def initRange(self):
        return self.__initRange
    @initRange.setter
    def initRange(self,value:Union[ List[Union[float,int]], Tuple[Union[float,int]], Dict[str,Union[Tuple,List]] ]):

        #Check given lists compatability with matrix's 'fill' attribute
        def list_checker(value,fill):
            if ( fill in [uniform,gauss,gammavariate,betavariate,lognormvariate] ) \
            or ( isinstance(fill,(int,float,complex)) ):
                if len(value)!=2:
                    raise IndexError("""initRange|ranged should be in the following formats:
                                        fill is gauss|lognormvariate --> [mean,standard_deviation]
                                        fill is (gamma|beta)variate --> [alpha,beta]
                                        fill is uniform --> [minimum,maximum]""")
                if not (isinstance(value[0],(float,int))) and not (isinstance(value[1],(float,int))):
                    raise ValueError("list contains non integer and non float numbers")
            
            elif fill in [triangular]:
                if len(value)!=3:
                    raise IndexError("initRange|ranged should be in the form of [minimum,maximum,mode]")
                if not (isinstance(value[0],(float,int))) and not (isinstance(value[1],(float,int))) \
                and not (isinstance(value[2],(float,int))):
                    raise ValueError("list contains non integer and non float numbers")
            
            elif fill in [expovariate]:
                if len(value)!=1:
                    raise IndexError("initRange|ranged should be in the form of [lambda]")
                
            else:
                pass

        if isinstance(value,dict):
            names,ranges = list(value.keys()),list(value.values())
            fill = self.fill

            if len(names) != self.d1:
                raise IndexError(f"Expected {self.d1} items in dictionary, got {len(names)} instead.")
            if not all([1 if name in self.features else 0 for name in names]):
                raise NameError("Dictionary keys should match column names")
            
            for lis in ranges:
                if not isinstance(lis,(tuple,list)):
                    raise TypeError(f"Values in dictionary should be lists or tuples")
                list_checker(lis,fill)

            self.__initRange = value

        elif isinstance(value,(list,tuple)):
            list_checker(value,self.fill)
            self.__initRange = list(value)

        else:
            raise TypeError(f"Can't use type '{type(value)} as a list,tuple or a dictionary")

        self.setMatrix(self.__dim,self.__initRange,[],self.__fill,self._cMat,self._fMat)

    @property
    def rank(self):
        """
        Rank of the matrix
        """
        return self._Rank() 
    
    @property
    def perma(self):
        """
        Permanent of the matrix
        """
        from .linalg.perma import perma
        return perma(self,self._matrix)
            
    @property
    def trace(self):
        """
        Trace of the matrix
        """
        if not self.isSquare:
            return None
        return sum(self.diags)
    
    @property
    def matrix(self):
       return self._matrix
   
    @property
    def data(self):
        return self._matrix

    @property
    def det(self):
        """
        Determinant of the matrix
        """
        if not self.isSquare:
            return None
        return self._determinantByLUForm()
    
    @property
    def diags(self):
        m = self._matrix
        return [m[i][i] for i in range(min(self.dim))]
    
    @property
    def eigenvalues(self):
        return self._eigenvals()

    @property
    def eigenvectors(self):
        res = self._eigenvecs(self.EIGENVEC_ITERS,1+1e-4)
        return [vec[2] for vec in res[0]] if not res in [None,[]] else []

    @property
    def eigenvecmat(self):
        res = self._eigenvecs(self.EIGENVEC_ITERS,1+1e-4)
        return res[1] if not res in [None,[]] else None
    
    @property
    def diagmat(self):
        res = self._eigenvecs(self.EIGENVEC_ITERS,1+1e-4)
        return res[2] if not res in [None,[]] else None

    @property
    def obj(self):
        """
        Object call as a string to recreate the matrix
        """
        f,cd = self.fill,str([i.__name__ for i in self.coldtypes]).replace("'","")
        if type(self.fill).__name__ == "method":
            f=self.fill.__name__
            
        dm,m,r,d = self.dim,self.matrix,self.initRange,self.decimal
        s,dt = self.seed,self.dtype.__name__
        i = "Label("+str(self.index.labels)+","+str(self.index.names)+")"
        fs = "Label("+str(self.features.labels)+","+str(self.features.names)+")"
        return f"Matrix(dim={dm},data={m},ranged={r},fill={f},features={fs},decimal={d},seed={s},dtype={dt},coldtypes={cd},index={i})"
 
    @property
    def seed(self):
        return self.__seed
    @seed.setter
    def seed(self,value:int):
        if not isinstance(value,int):
            raise TypeError("Seed must be an integer")
        self.__seed = value
        self.setMatrix(self.dim,self.initRange,[],"",self.fill,self._cMat,self._fMat)

    @property
    def decimal(self):
        return self.__decimal
    @decimal.setter
    def decimal(self,val:int):
        try:
            assert isinstance(val,int)
            assert val>=1
        except:
            raise ValueError("Seed should be an integer higher or equal to 1")
        else:
            self.__decimal=val     
        
    @property
    def dtype(self):
        return self.__dtype
    @dtype.setter
    def dtype(self,val:Union[int,float,complex,dataframe]):
        if not val in [int,float,complex,dataframe]:
            return DtypeError(val.__name__)
        else:
            self.__dtype = val
            self.__init__(dim=self.dim,
                          data=self._matrix,
                          ranged=self.initRange,
                          fill=self.fill,
                          features=self.features,
                          decimal=self.decimal,
                          seed=self.seed,
                          dtype=self.dtype,
                          coldtypes=self.__coldtypes,
                          index=self.index,
                          )

    @property
    def coldtypes(self):
        return self.__coldtypes
    @coldtypes.setter
    def coldtypes(self,val:Union[List[str],Tuple[str]]):
        if not isinstance(val,(list,tuple)):
            raise NotListOrTuple(val)
        if len(val) != self.d1:
            raise InvalidList(val,self.d1,"column dtypes")

        for i in val:
            if type(i)!=type:
                raise ColdtypeError(i)
        self.__coldtypes=val
        self.setup(True)
    
    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self,val:Union[object,list,tuple]):
        if isinstance(val,Matrix):
            if val.d0 != self.d0:
                raise ValueError(f"Given matrix can't be used as indices; expected {self.d0} rows, got {val.d0}")
            new_label = Label(val)
            self.__index = new_label

        elif isinstance(val,(list,tuple)):
            if len(val) != self.d0:
                raise ValueError(f"Given list can't be used as indices; expected {self.d0} values, got {len(val)}")
            self.__index = Label(list(val),self.index.names)

        elif val == None:
            self.__index = Label()

        elif isinstance(val,Label):
            if len(val) != self.d0:
                raise ValueError(f"Given Label can't be used as indices; expected {self.d0} labels, got {len(val)}")
            self.__index = val
        else:
            raise TypeError(f"Type {type(val).__name__} can't be used as indices")     

# =============================================================================
    """Check special cases"""
# =============================================================================    
    @property
    def isSquare(self):
        """
        Matrix.dim == [i,j] where i == j
        """
        return self.d0 == self.d1
    
    @property
    def isIdentity(self):
        """
        Matrix[i,j] == 1 where i==j and Matrix[i,j] == 0 where i!=j 
        """
        if not self.isSquare:
            return False
        return round(self,self.PRECISION).matrix == Identity(self.d0).matrix
    
    @property
    def isSingular(self):
        """
        Matrix.det == 0
        """
        if not self.isSquare:
            return False
        return roundto(self.det,self.PRECISION) == 0
    
    @property
    def isSymmetric(self):
        """
        Matrix[i,j] == Matrix[j,i]
        """        
        if not self.isSquare:
            return False
        dig = self.PRECISION
        return self.t.roundForm(dig).matrix == self.roundForm(dig).matrix
        
    @property  
    def isAntiSymmetric(self):
        """
        Matrix[i,j] == -Matrix[j,i]
        """
        if not self.isSquare:
            return False
        dig = self.PRECISION
        return (self.t*-1).roundForm(dig).matrix == self.roundForm(dig).matrix
    
    @property
    def isPerSymmetric(self):
        """
        Matrix[i,j] == Matrix[n+1-j,n+1-i] , for nxn Matrix 
        """
        if not self.isSquare:
            return False

        m = self.matrix
        dig = self.PRECISION
        d = self.d0
        for i in range(d):
            for j in range(d):
                if roundto(m[i][j],dig) != roundto(m[d-1-j][d-1-i],dig):
                    return False
        return True
    
    @property
    def isHermitian(self):
        """
        Matrix.ht == Matrix
        """
        return (self.ht).matrix == self.matrix
        
    @property
    def isTriangular(self):
        """
        Matrix[i,j] == 0 where i < j XOR i > j
        """
        if not (self.isSquare and (self.isUpperTri or self.isLowerTri)):
            return False
        return True

    @property
    def isUpperTri(self):
        """
        Matrix[i,j] == 0 where i > j
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(1,self.d0):
            for j in range(i):
                if roundto(m[i][j],dig)!=0: #Check elements below diagonal to be 0
                    return False
        return True
    
    @property
    def isLowerTri(self):
        """
        Matrix[i,j] == 0 where i < j
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(1,self.d0):
            for j in range(i):
                if roundto(m[j][i],dig)!=0: #Check elements above diagonal to be 0
                    return False
        return True
    
    @property
    def isDiagonal(self):
        """
        Matrix[i,j] == 0 where i != j
        """
        from functools import reduce
        if not self.isSquare:
            return False
        return self.isUpperTri and self.isLowerTri and (roundto(self.det,self.PRECISION) == reduce((lambda a,b: a*b),self.diags))

    @property
    def isBidiagonal(self):
        """
        Matrix[i,j] == 0 where ( i != j OR i != j+1 ) XOR ( i != j OR i != j-1 )
        """
        return self.isUpperBidiagonal or self.isLowerBidiagonal
    
    @property
    def isUpperBidiagonal(self):
        """
        Matrix[i,j] == 0 where i != j OR i != j+1
        """
        #Assure the matrix is upper triangular
        if not self.isSquare:
            return False
        
        dig = self.PRECISION
        m=self.matrix
        #Assure diagonal and superdiagonal have non-zero elements 
        if 0 in [roundto(m[i][i],dig) for i in range(self.d0)] + [roundto(m[i][i+1],dig) for i in range(self.d0-1)]:
            return False
        
        #Assure the elements above first superdiagonal are zero
        for i in range(self.d0-2):
            if [0]*(self.d0-2-i) != roundto(m[i][i+2:],dig):
                return False
            
        return True

    @property
    def isLowerBidiagonal(self):
        """
        Matrix[i,j] == 0 where i != j OR i != j-1
        """
        #Assure the matrix is upper triangular
        if not self.isSquare:
            return False

        m=self.matrix
        dig = self.PRECISION
        #Assure diagonal and subdiagonal have non-zero elements 
        if 0 in [roundto(m[i][i],dig) for i in range(self.d0)] + [roundto(m[i+1][i],dig) for i in range(self.d0-1)]:
            return False
        
        #Assure the elements above first subdiagonal are zero
        for i in range(self.d0-2):
            if [0]*(self.d0-2-i) != roundto(m[i][i+2:],dig):
                return False
            
        return True
        
    @property
    def isUpperHessenberg(self):
        """
        Matrix[i,j] == 0 where i<j-1
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(2,self.d0):
            for j in range(i):
                if roundto(m[i][j],dig)!=0: #Check elements below subdiagonal to be 0
                    return False
        return True
    
    @property
    def isLowerHessenberg(self):
        """
        Matrix[i,j] == 0 where i>j+1
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(2,self.d0):
            for j in range(i):
                if roundto(m[j][i],dig)!=0: #Check elements above superdiagonal to be 0
                    return False
        return True
    
    @property
    def isHessenberg(self):
        """
        Matrix[i,j] == 0 where i>j+1 XOR i<j-1
        """
        return self.isUpperHessenberg or self.isLowerHessenberg
    
    @property
    def isTridiagonal(self):
        """
        Matrix[i,j] == 0 where abs(i-j) > 1 AND Matrix[i,j] != 0 where 0 <= abs(i-j) <= 1
        """
        if not self.isSquare or self.d0<=2:
            return False
        m = self.matrix
        dig = self.PRECISION
        #Check diagonal and first subdiagonal and first superdiagonal
        if 0 in [roundto(m[i][i],dig) for i in range(self.d0)] \
              + [roundto(m[i][i+1],dig) for i in range(self.d0-1)] \
              + [roundto(m[i+1][i],dig) for i in range(self.d0-1)]:
            return False
        
        #Assure rest of the elements are zeros
        for i in range(self.d0-2):
            #Non-zero check above first superdiagonal
            if [0]*(self.d0-2-i) != roundto(m[i][i+2:],dig):
                return False
            
            #Non-zero check below first subdiagonal
            if [0]*(self.d0-2-i) != roundto(m[self.d0-i-1][:self.d0-i-2],dig):
                return False
        return True

    @property
    def isToeplitz(self):
        """
        Matrix[i,j] == Matrix[i+1,j+1] for every i and j
        """
        m = self.matrix
        dig = self.PRECISION
        for i in range(self.d0-1):
            for j in range(self.d1-1):
                if roundto(m[i][j],dig) != roundto(m[i+1][j+1],dig):
                    return False
        return True
    
    @property
    def isIdempotent(self):
        """
        Matrix@Matrix == Matrix
        """
        if not self.isSquare:
            return False
        dig = self.PRECISION            
        return self.roundForm(dig).matrix == (self@self).roundForm(dig).matrix
    
    @property
    def isOrthogonal(self):
        """
        Matrix.t == Matrix.inv
        """
        if not self.isSquare or self.isSingular:
            return False
        dig = self.PRECISION
        return self.inv.roundForm(dig).matrix == self.t.roundForm(dig).matrix
    
    @property
    def isUnitary(self):
        """
        Matrix.ht == Matrix.inv
        """
        if not self.isSquare or self.isSingular:
            return False
        dig = self.PRECISION
        return self.ht.roundForm(dig).matrix == self.inv.roundForm(dig).matrix
    
    @property
    def isNormal(self):
        """
        Matrix@Matrix.ht == Matrix.ht@Matrix OR Matrix@Matrix.t == Matrix.t@Matrix
        """
        if not self.isSquare:
            return False
        dig = self.PRECISION
        return (self@self.ht).roundForm(dig).matrix == (self.ht@self).roundForm(dig).matrix
    
    @property
    def isCircular(self):
        """
        Matrix.inv == Matrix.conj
        """
        if not self.isSquare or self.isSingular:
            return False
        dig = self.PRECISION
        return self.inv.roundForm(dig).matrix == self.roundForm(dig).matrix
    
    @property
    def isPositive(self):
        """
        Matrix[i,j] > 0 for every i and j 
        """
        if self._cMat:
            return False
        return bool(self>0)
    
    @property
    def isNonNegative(self):
        """
        Matrix[i,j] >= 0 for every i and j 
        """
        if self._cMat:
            return False
        return bool(self>=0)
    
    @property
    def isProjection(self):
        """
        Matrix.ht == Matrix@Matrix == Matrix 
        """
        if not self.isSquare:
            return False
        return self.isHermitian and self.isIdempotent

    @property
    def isInvolutory(self):
        """
        Matrix@Matrix == Identity
        """
        if not self.isSquare:
            return False
        return (self@self).roundForm(4).matrix == Identity(self.d0).matrix
    
    @property
    def isIncidence(self):
        """
        Matrix[i,j] == 0 | 1 for every i and j
        """
        for i in range(self.d0):
            for j in range(self.d1):
                if not self._matrix[i][j] in [0,1]:
                    return False
        return True
    
    @property
    def isZero(self):
        """
        Matrix[i,j] == 0 for every i and j
        """
        m = self.matrix
        for i in range(self.d0):
            for j in range(self.d1):
                if m[i][j] != 0:
                    return False
        return True

    @property
    def isDefective(self):
        """
        len(set(roundto(Matrix.eigenvalues,3))) != len(Matrix.eigenvalues)
        """
        eigs = self.eigenvalues
        return len(set(roundto(eigs,3))) != len(eigs) if not eigs in [None,[]] else False

# =============================================================================
    """Get special formats"""
# =============================================================================    
    @property
    def realsigns(self):
        """
        Determine the signs of the elements' real parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        mm = self._matrix
        signs=[[1 if mm[i][j].real>=0 else -1 for j in range(self.d1)] for i in range(self.d0)]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def imagsigns(self):
        """
        Determine the signs of the elements' imaginary parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        mm = self._matrix
        signs=[[1 if mm[i][j].imag>=0 else -1 for j in range(self.d1)] for i in range(self.d0)]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def signs(self):
        """
        Determine the signs of the elements
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        mm = self._matrix
        if self._cMat:
            return {"Real":self.realsigns,"Imag":self.imagsigns}
        signs=[[1 if mm[i][j]>=0 else -1 for j in range(self.d1)] for i in range(self.d0)]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def echelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._rrechelon(rr=False)[0]

    @property
    def rrechelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._rrechelon(rr=True)[0]
    
    @property
    def conj(self):
        """
        Conjugated matrix
        """
        temp=self.copy
        mm = temp.matrix
        temp._matrix=[[mm[i][j].conjugate() if isinstance(mm[i][j],complex) else mm[i][j] for j in range(self.d1)] for i in range(self.d0)]
        return temp
    
    @property
    def t(self):
        """
        Transposed matrix
        """
        return self._transpose()
    
    @property
    def ht(self):
        """
        Hermitian-transposed matrix
        """
        return self._transpose(hermitian=True)    
    
    @property
    def adj(self):
        """
        Adjoint matrix
        """
        return self._adjoint()
    
    @property
    def inv(self):
        """
        Inversed matrix
        """
        return self._inverse()  
    
    @property
    def pseudoinv(self):
        """
        Pseudo-inversed matrix
        """
        if self.isSquare:
            return self.inv
        if self.d0>self.d1:
            return ((self.t@self).inv)@(self.t)
        return None
    
    @property
    def EIGENDEC(self):
        """
        X, lambda and X.inv matrices from eigenvalue decomposition
        """
        return self._EIGENDEC()

    @property
    def SVD(self):
        """
        U,sigma and V.ht matrices from singular value decomposition
        """
        return self._SVD()

    @property
    def LU(self):
        """
        L and U matrices from LU decomposition
        """
        lu = self._LU()
        return (lu[2],lu[0])
        
    @property
    def U(self):
        """
        Upper triangular part of the matrix
        """
        return self._LU()[0]
    
    @property
    def L(self):
        """
        Lower triangular part of the matrix
        """
        return self._LU()[2]
    
    @property
    def symdec(self):
        ant_sym = self._symDecomp()
        return (ant_sym[0],ant_sym[1])

    @property
    def sym(self):
        """
        Symmetrical part of the matrix
        """
        if self.isSquare:
            return self._symDecomp()[0]
        return []
    
    @property
    def anti(self):
        """
        Anti-symmetrical part of the matrix
        """
        if self.isSquare:
            return self._symDecomp()[1]
        return []    
    
    @property
    def QR(self):
        """
        Q and R matrices from QR decomposition
        """
        qr = self._QR()
        return (qr[0],qr[1])

    @property
    def Q(self):
        """
        Q matrix from QR decomposition
        """
        return self._QR()[0]
    
    @property
    def R(self):
        """
        R matrix from QR decomposition
        """
        return self._QR()[1]    
    
    @property
    def floorForm(self):
        """
        Returns a matrix with all possible values' floor values
        """
        return self.__floor__()
    
    @property
    def ceilForm(self):
        """
        Returns a matrix with all possible values' ceiling values
        """
        return self.__ceil__()
    
    @property   
    def intForm(self):
        """
        Returns a matrix with all possible values as integers
        """
        return self.__floor__()
    
    @property   
    def floatForm(self):
        """
        Returns a matrix with all possible values as floats
        """
        if self._cMat:
            return self
        if self._dfMat:
            return Matrix(self.dim,data=[a[:] for a in self.matrix],features=self.features,
                          coldtypes=[float if i in [int,float] else i for i in self.coldtypes],
                          decimal=self.decimal,seed=self.seed,dtype=dataframe,index=self.index,
                          implicit=True)

        mm = self.matrix
        t=[[float(mm[a][b]) for b in range(self.d1)] for a in range(self.d0)]

        return Matrix(self.dim,t,features=self.features,decimal=self.decimal,seed=self.seed,implicit=True)

    
    def roundForm(self,decimal:int=1,printing_decimal:Union[int,None]=None):
        """
        Elements rounded to the desired decimal after dot

        decimal: int; digits to round to
        printing_decimal: int; returned matrix's 'decimal' parameter
        """
        return self.__round__(decimal,printing_decimal)
        
# =============================================================================
    """Filtering methods"""
# =============================================================================     
    def select(self,columns:Union[List[str],Tuple[str],str]):
        """
        Returns a matrix with chosen columns
        
        columns: tuple|list of strings; Desired column names as strings in a tuple or list
        """
        if columns == None:
            return None
        if isinstance(columns,str):
            columns = (columns,)
        temp = self.col(self.features.index(columns[0])+1)
        for col in columns[1:]:
            temp.concat(self.col(self.features.index(col)+1))
        return temp

    def find(self,value:Any,
             start:[0,1]=1,
             onlyrow:bool=False):
        """
        value: object
        start: 0 or 1. Index to start from
        onlyrow: bool; Wheter or not to return only the row indices of value's appearances
        Returns the indices of the given value in a list
        """
        from .filter.find import find
        return find(self.matrix,self.dim,value,start,onlyrow)

    def join(self,
             SELECT:Union[Tuple[object],List[object]],
             METHOD:['INNER','LEFT','LEFT-EX','RIGHT','RIGHT-EX','FULL','FULL-EX','CROSS'],
             JOIN:object,
             ON:Union[str,None]=None):
        """
        Joins two matrices with given methods and conditions

        SELECT: list or tuple of column matrices|None; columns to return, '*' to use all columns
        METHOD: 'INNER'|'LEFT'|'LEFT-EX'|'RIGHT'|'RIGHT-EX'|'FULL'|'FULL-EX'|'CROSS'; joining method
        JOIN: Matrix object|None; matrix to use as the 2nd table
        ON: str|None; conditions to verify

        SQL:

            SELECT Table1.T_ID, Table2.Name, Table1.T_Date
            FROM Table1 
            INNER JOIN Table2 ON Table1.STD_ID=Table2.ID;

        Corresponding call:

            >>> Table1.join(SELECT=(Table1.T_ID, Table2.Name, Table1.T_Date),
                            METHOD='INNER',
                            JOIN=Table2,
                            ON='Table1.STD_ID == Table2.ID')

            # Notice that 'FROM' is always the dataframe that the join method is called from


        Example representation of methods:
            -> 1's represent the values which will be kept, 0's won't be used.
            -> Each number represents a row
            -> Left most 3 elements represent rows in self, right most are compared matrix's rows
            -> Middle 3 elements represent rows that are in both self and compared matrix

            --- Method ----------- Visually ---

                                    0  1  0
                INNER               0  1  0
                                    0  1  0
                
                                    1  1  0
                LEFT                1  1  0
                                    1  1  0

                                    1  0  0
               LEFT-EX              1  0  0
                                    1  0  0

                                    0  1  1
                RIGHT               0  1  1
                                    0  1  1
        
                                    0  0  1
               RIGHT-EX             0  0  1
                                    0  0  1

                                    1  1  1
                FULL                1  1  1
                                    1  1  1

                                    1  0  1
               FULL-EX              1  0  1
                                    1  0  1                   

        Example usage:
            ->Join Matrix and otherMatrix where Matrix.usr_id==otherMatrix.id,
            using left join, return usr_id and department columns

                >>> Matrix.join(SELECT=(Matrix.usr_id,otherMatrix.department),
                                FROM=otherMatrix,
                                JOIN='left',
                                ON='Matrix.usr_id == otherMatrix.id'
                                )
        
        NOTE:
            -> '-EX' methods guarantees a matrix with null values or an empty matrix
            -> If method is 'CROSS', 'ON' doesn't get used; If 'ON' is None, method is forced to 'CROSS'
        """
        from .matrixops.joins import joins
        return joins(self,SELECT,METHOD,JOIN,ON,null,Matrix)

    def where(self,conditions:Union[List[str],Tuple[str]],
              inplace:bool=True,
              namelevel:Union[Dict[str,int],int]=1):
        """
        Returns a matrix where the conditions are True for the desired columns.
        
        conditions:tuple/list of strings; Desired conditions to apply as a filter
        inplace:bool; True to compare values in place, False to search the values of self in 
                      given matrix with 'find' method and return matching rows as a Group object

        Syntax:
            Matrix.where((" ('Column_Name' (<|>|==|...) obj (and|or|...) 'Column_Name' ...") and ("'Other_column' (<|...) ..."), ...)
        
        Example:
            #Get the rows with Score in range [0,10) or Hours is higher than mean, where the DateOfBirth is higher than 1985
            
                >>> data.where( f" ( ( (Score>=0) and (Score<10) ) or ( Hours>={data.mean('Hours',0)} ) ) 
                                  and ( DateOfBirth>1985 ) ")
                #Same as
                    >>> data[(((data["Score"]>=0) & (data["Score"]<10)) | (data["Hours"]>=data.mean("Hours",0))) 
                            & (data["DateOfBirth"]>1985) ]

            #Return groups where ID of self matches EMP_ID in the given matrix

                >>> data.where("data.ID == table.EMP_ID",inplace=False)

        NOTE:
            -> Every statement HAVE TO BE enclosed in parentheses as shown in the examples above
            -> If a dictionary passed to 'namelevel', given conditions should only have the names
               from the keys of the 'namelevel' 
        """
        from .filter.where import wheres
        if inplace:
            results,indices = wheres(self,conditions,self.features[:],True,namelevel),self.index[:]
            temp,found_inds = results
            lastinds = indices[found_inds] if self._dfMat else []

            return Matrix(data=temp,
                          features=self.features[:],
                          dtype=self.dtype,
                          coldtypes=self.coldtypes[:],
                          index=lastinds)
        else:
            return wheres(self,contiditions,self.features[:],False)
        
    def apply(self,expressions:Union[str,List[str],Tuple[str]],
              columns:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=(None,),
              conditions:Union[str,object,None]=None,
              namelevel:int=1,
              returnmat:bool=False):
        """
        Apply arithmetic, logical, indexing etc. operations to values in desired columns individually inplace

        expressions: str(1 column only)|tuple|list of strings; Operations to do for each column given.
            ->Multiple operations can be applied if given in a single string. 
            ->One white space required between each operation and no space should 
            be given between operator and operand
        
        columns: str(1 column only)|tuple|list|None; Column names to apply the given expression
        
        conditions: str|boolean column Matrix|None; Conditions of rows to apply changes to

        returnmat: bool; True to return self after evaluation, False to return None

        Given operation is applied as:
            >>> exec("values[row][col] = eval('values[row][col]'+operation)")

        Example:

            #Multiply all columns with 3 and then add 10
                >>> Matrix.apply( ("*3 +10") ) 

            #Multiply Prices with 0.9 and subtract 5 also add 10 to Discounts where Price>100 and Discount<5
                >>> Matrix.apply( ("*0.9 -5","+10"), ("Price","Discount"), "(Price>100) and (Discount<5)" )

                #Same as the following process
                >>> filtered = market_base[(market_base.Price>100) & (market_base.Discount<5)]
                >>> filtered['Price'] *= 0.9
                >>> filtered['Price'] -= 5
                >>> filtered['Discount'] += 10
                >>> market_base[(market_base.Price>100) & (market_base.Discount<5)] = filtered

            #Turn strings in "Name" column into their lengths
                >>> Matrix.apply(".__len__()","Name")

        """
        from .filter.apply import applyop
        if returnmat:
            return applyop(self,expressions,columns,conditions,self.features[:],True,Matrix,namelevel)
        applyop(self,expressions,columns,conditions,self.features[:],True,Matrix,namelevel)

    def transform(self,function:object,
                  columns:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=(None,),
                  conditions:Union[str,object,None]=None,
                  namelevel:int=1,
                  returnmat:bool=False):
        """
        Pass values in the matrix to functions and replace them with the outputs

        function: function; A function to pass values to

        columns: str(1 column only)|tuple|list|None; Column names to use

        conditions: str|boolean column Matrix|None; Conditions of rows to apply changes to
        
        namelevel: int>0; column name level to search for
        
        returnmat: bool; True to return self after evaluation, False to return None

        Examples:

            #Apply 'sum' function to 'Scores_list' column
                >>> Matrix.transform(function=sum,
                                     columns='Scores_list')

                Visually:

                  Rank  Scores_list            Rank  Scores_list
                 +------------------           +----------------
                0|   9       [3, 4]   --->   0|   9            7
                1|   3    [2, 4, 6]          1|   3           12


            #Apply a custom function called 'calculate' to 'Bonus' column where 'extra_time_spent' >= 3
                >>> Matrix.transform(function=calculate,
                                     columns="Bonus",
                                     conditions=Matrix.extra_time_spent >= 3)
        
        NOTE:
            Some tweaks to 'coldtypes' may be needed after transformations
            
        """
        from .filter.apply import applyop
        if returnmat:
            return applyop(self,function,columns,conditions,self.features[:],False,Matrix,namelevel)
        applyop(self,function,columns,conditions,self.features[:],False,Matrix,namelevel)

    def combine(self,columns:Union[Tuple[str],Tuple[Tuple[str]]],
                function:object,
                feature:str,
                dtype:type,
                inplace:bool=False,
                namelevel:int=1,
                returnmat:bool=False):
        """
        Combine values in given columns with by passing them into the given function and use the output
        to create a single column matrix

        columns: tuple or list of strings; column names to use
        function: function; function to pass values in the desired columns
        feature: str;new column's name
        dtype: type; column's new dtype
        inplace: bool; True to concatenate the column matrix, False to return the column matrix
        namelevel: int; label level to use for the names given in 'columns' parameter
        returnmat: bool; wheter to return self

        Example:
            #Use Year, Month and Day level-1 columns to create a new column named 'DATE' with dtype str, concatenate the result
                >>> Matrix.combine(columns=('Year','Month','Day'),
                                   function=lambda y,m,d:str(y)+"/"+str(m)+"/"+str(d),
                                   feature="DATE",
                                   dtype=str,
                                   inplace=True)
        
        NOTE:
            ->Values which returned an error when passed to the given function will be replaced with the default null object
            ->If multiple columns have the same name in given 'namelevel', first one found is used.
            ->If 'inplace' is False, column matrix will be returned regardless the 'returnmat' value

        """
        from .filter.combine import _combine
        if returnmat or not inplace:
            return _combine(self,columns,function,feature,dtype,inplace,namelevel,dataframe)
        _combine(self,columns,function,feature,dtype,inplace,namelevel,dataframe)

    def split(self,column):
        pass

    def replace(self,old:Any,
                new:Any,
                column:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=None,
                condition:Optional[object]=None,
                namelevel:int=1,
                returnmat:bool=False):
        """
        Replace single values,rows and/or columns

        old: all available types|boolean *column* matrix; value(s) to be replaced

        new: all available types; value(s) to replace old ones with

        column: str|tuple or list of strings|None;  which column(s) to apply replacements, None for all columns

        condition: boolean *column* matrix|None; row(s) to apply replacements, None for all rows
        
        namelevel: int; Level of the column name labels to use 

        returnmat: bool; True to return self after evaluation, False to return None
        
        Example:
                #Replace all 0's in all columns with 1's
                >>> data.replace(old=0,new=1)

                #Replace all "Pending" values to "Done" in "Order1" and "Order2" columns
                >>> data.replace(old="Pending",
                                 new="Done",
                                 column=("Order1","Order2"))

                #Replace all '' values in the level-2 column "Length" with the mean of the "Length" column
                >>> data.replace=(old='',
                                  new=data.mean("Length",get=0),
                                  column="Length"
                                  namelevel=2)

                #Replace all "FF" values in "Grade" column with "AA" in the column "Grade" where "Year"<=2019
                >>> data.replace(old="FF",
                                 new="AA",
                                 column="Grade",
                                 condition=data["Year"]<=2019)

                #Replace all numbers below 0 in with 0's in column named "F5" where "Score1" is less than "Score2"
                >>> data.replace(old=data["F5"]<0,
                                 new=0,
                                 column="F5",
                                 condition=data["Score1"]<data["Score2"])

        """
        from .filter.replace import _replace
        _replace(self,old,new,column,condition,Matrix,namelevel)
        if returnmat:
            return self
        
    def sortBy(self,column:Union[str,int,None]=None,key=lambda a:a[1],reverse:bool=False,returnmat:bool=False,level:int=1):
        """
        Sort the rows by the desired column

        column:str|int|None; column name as string, column number, None to sort by label column level 'level'
        key:function; function to use while sorting
        reverse:bool; wheter or not to sort the matrix in reversed order
        returnmat:bool; wheter or not to return self
        level:int; level of labels to sort by if no column given
        """
        if column == None:

            if self._dfMat:
                label_mat = self.index.as_df
                temp_mat = self.copy
                real_names = temp_mat.features[:]

                label_mat.concat(temp_mat,returnmat=True). \
                          sortBy(column=label_mat.features.get_level(level),key=key,reverse=reverse)

                self.__index = Label(label_mat[:,:self.index.level])
                self._matrix = label_mat[:,self.index.level:].matrix
                self.__features = real_names

            else:
                raise TypeError("Indexing by index column is not allowed on non-dataframe matrices")
        else:
            if isinstance(column,int):
                assert (column>0) and (column<=self.d1) , f"'column' can't be {column}"
    
            temp=sorted([(i,row) for i,row in enumerate(self.col(column,0))],key=key,reverse=reverse)
            if self._dfMat:
                inds = self.index.labels
                newinds = [r[0] for r in temp]
                self.__index = Label([inds[i] for i in newinds],self.index.names)

            mm = self.matrix
            self._matrix = [mm[r[0]] for r in temp]

        if returnmat:
            return self

    def shuffle(self,returnmat:bool=False):
        """
        Shuffle the rows of the matrix

        returnmat:bool; wheter or not to return self        
        """
        from random import shuffle

        inds = list(range(self.d0))
        unshuffled = inds[:]

        mm = self.matrix
        oldind = self.index.labels
        
        while inds == unshuffled:
            shuffle(inds)

        if self._dfMat:
            self.__index = Label([oldind[i] for i in inds],self.index.names)
        self._matrix = [mm[i][:] for i in inds]

        if returnmat:
            return self

    def sample(self,size:int=10,condition:str=None):
        """
        Get a sample of the matrix

        size:int. How many samples to take
        condition:str. Conditions to set as a base for sampling, uses 'where' method to filter 
        """
        from .filter.sample import samples
        return samples(self,size,condition,Matrix)

    def match(self,expression:str,
              columns:Union[str,int,List[Union[str,None]],Tuple[Union[str,None]],None]=None,
              as_row:bool=True):
        """
        Return the values or rows that match the given expression

        expression: str; regular expression, uses re.findall
        columns: str|tuple or list of strings|int(starts from 1)|None; Column names/numbers
        as_row: bool; True to return rows with the matching values, False to return:
            1)A dictionary if 'columns' == None|tuple or list as {'column_name':[(row_index,matching_value), ...], ...}
            2)A list if 'columns' == str [(row_index,matching_values), ...]

        Example:
            #Return the rows of all email adresses using gmail.com domain in the column 'mail'
                >>> Matrix.match(expression=r"\w+@gmail.com",
                                columns="mail",
                                as_row=True)
        NOTE:
            #This method is CURRENTLY faster in most cases than using boolean matrices as indices:
                >>> Matrix[Matrix[column]==value] --> Using boolean matrices as indices
                >>> Matrix.match(value,column)    --> Corresponding method call for the same result as previous one

        """
        if not self._dfMat:
            raise MatrixError("'match' method only works with dataframes.")
        from .filter.match import _match
        return _match(self,expression,columns,as_row,Matrix)

# =============================================================================
    """Statistical methods"""
# =============================================================================      
    
    def normalize(self,col:Union[int,str,tuple,None]=None,
                       inplace:bool=True,
                       declare:bool=True,
                       returnmat:bool=False):
        """
        Normalizes the data to be valued between 0 and 1

        col:integer>=1 | column name as string | None
        inplace: bool ; True to apply changes to matrix, False to return a new matrix
        declare: bool ; True to guess new dtype and store it in coldtypes, False to keep old dtype
        returnmat: bool ; True to return self after inplace changes applied, False to return None

        NOTE:
            -> 'returnmat' value only applies when 'inplace' is True, otherwise a new Matrix is returned
        """
        from .stats.normalize import normalize
        return normalize(self,col,inplace,self.PRECISION,declare,returnmat)

    def stdize(self,col:Union[int,str,tuple,None]=None,
                    inplace:bool=True,
                    declare:bool=True,
                    returnmat:bool=False):
        """
        Standardization to get mean of 0 and standard deviation of 1

        col:integer>=1 | column name as string
        inplace: bool ; True to apply changes to matrix, False to return a new matrix
        declare: bool ; True to guess new dtype and store it in coldtypes, False to keep old dtype
        returnmat: bool ; True to return self after inplace changes applied, False to return None

        NOTE:
            -> 'returnmat' value only applies when 'inplace' is True, otherwise a new Matrix is returned
        """ 
        from .stats.stdize import stdize
        return stdize(self,col,inplace,self.PRECISION,declare,returnmat)

    def ranged(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Range of the columns

        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """    
        from .stats.ranged import ranged
        return ranged(self,col,get,Matrix,dataframe)

    def max(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Highest value(s) in the desired column(s)

        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.minmax import _minmax
        return _minmax(self,col,get,1,Matrix,dataframe)

    def min(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Lowest value(s) in the desired column(s)

        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.minmax import _minmax
        return _minmax(self,col,get,0,Matrix,dataframe)

    def mean(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Mean of the columns

        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """  
        from .stats.mean import mean
        return mean(self,col,get,Matrix,dataframe)
    
    def mode(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Returns the columns' most repeated elements in a dictionary

        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a tuple of Matrices for every column individually
        """
        from .stats.mode import mode
        return mode(self,col,get,Matrix,dataframe)
    
    def median(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Returns the median of the columns

        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """ 
        from .stats.median import median
        return median(self,col,get,Matrix,dataframe)
    
    def sdev(self,col:Union[int,str,tuple,None]=None,population:[0,1]=1,get:[0,1,2]=1):
        """
        Standard deviation of the columns

        col:integer>=1 | column name as string
        population: 1 for σ, 0 for s value (default 1)
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.sdev import sdev
        return sdev(self,col,population,get,Matrix,dataframe)    
    
    def var(self,col:Union[int,str,tuple,None]=None,population:[0,1]=1,get:[0,1,2]=1):
        """
        Variance in the columns

        col:integer>=1 |None|column name as string ; Index/name of the column, None to get all columns 
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """   
        from .stats.var import var
        return var(self,col,population,get,Matrix,dataframe)     
    
    def ranked(self,col:Union[int,str,tuple,None]=None,reverse:bool=False,key=lambda a:a[1],get:[-1,0,1,2]=1,start:int=0):
        """
        Ranks of the values in the columns when they are sorted

        col:int|str|None; column number/name, None for all columns
        reverse:bool; wheter or not to use reversed sorting
        key:function; function to use while sorting
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.ranked import _rank
        return _rank(self,col,reverse,key,get,start)

    def z(self,col:Union[int,str,tuple,None]=None,population:[0,1]=1):
        """
        z-scores of the elements

        column:integer>=1 |None|column name as string ; z-scores of the desired column
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample

        Give no arguments to get all the scores in a matrix
        """
        from .stats.z import z
        return z(self,col,population,dataframe)        
    
    def iqr(self,col:Union[int,str,tuple,None]=None,as_quartiles:bool=False,get:[0,1,2]=1):
        """
        Returns the interquartile range(IQR)

        col:integer>=1 and <=column amount | column name
        
        as_quartiles:
            True to return dictionary as:
                {Column1=[First_Quartile,Median,Third_Quartile],Column2=[First_Quartile,Median,Third_Quartile],...}
            False to get iqr values(default):
                {Column1=IQR_1,Column2=IQR_2,...}
                
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
                
        Usage:
            #Returns a dictionary with iqr's as values
            >>> self.iqr()

            #Returns a dictionary where the values are quartile medians in lists
            >>> self.iqr(None,True)

            #Returns a list of quartile medians in lists
            >>> self.iqr(None,True,0)

            #Returns a matrix of iqr's
            >>> self.iqr(None,False,2)

        NOTE:
            Replace "None" with any column number to get a specific column's iqr
        """ 
        from .stats.iqr import iqr
        return iqr(self,col,as_quartiles,get,Matrix,dataframe)   
     
    def freq(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Returns the frequency of every element on desired column(s)
        col:column index>=1 or column name
        get: 0|1|2 ; 0 to return a dictionary (uniques as keys, freq as values),
                     1 to return a dictionary (column names as keys, option 0 as values),
                     2 to return a list of Matrices for every column individually
        """
        from .stats.freq import freq
        return freq(self,col,get,Matrix,dataframe)   

    def sum(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1,inf_limit=2**512):
        """
        Return the sum of the desired column, give no arguments to get all columns'.

        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.prodsum import _prodsum
        return _prodsum(self,col,get,Matrix,dataframe,1,inf_limit)

    def prod(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1,inf_limit=2**512):
        """
        Return the product of the desired column, give no arguments to get all columns'.

        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.prodsum import _prodsum
        return _prodsum(self,col,get,Matrix,dataframe,0,inf_limit)

    def count(self,col:Union[int,str,tuple,None]=None,get:[0,1,2]=1):
        """
        Return the count of the valid values in column(s), give no arguments to get all columns'.

        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from .stats.freq import _count
        return _count(self,col,get,Matrix,dataframe)

    def cov(self,col1:Union[int,str,tuple,None]=None,col2:Union[int,str,None]=None,population:[0,1]=1):
        """
        Covariance of two columns

        col1,col2: integers>=1 |str|None; column numbers/names. For covariance matrix give None to both
        population: 0 or 1 ; 0 for samples, 1 for population
        """
        from .stats.cov import cov
        return cov(self,col1,col2,population,Matrix,dataframe)
        
    def corr(self,col1:Union[int,str,tuple,None]=None,
                  col2:Union[int,str,tuple,None]=None,
                  population:[0,1]=1,
                  method:["pearson","kendall","spearman"]="pearson"):
        """
        Correlation of 2 columns

        col1,col2: integers>=1 |str|None; column numbers/names. For correlation matrix give None to both
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        """
        from .stats.corr import _corr
        temp = Identity(self.d1,features=self.features[:],dtype=dataframe,coldtypes=[float for _ in range(self.d1)])
        return _corr(self,col1,col2,population,temp,method,Label)
    
    @property   
    def describe(self):
        """
        Returns a matrix describing the matrix with features: Column, dtype, count,mean, sdev, min, 25%, 50%, 75%, max
        """
        from .stats.describe import describe
        return describe(self,Matrix,dataframe,Label)

    @property
    def info(self):
        """
        Returns a dataframe with column information
        """
        feats,cdtyps = self.features[:],self.coldtypes[:]
        counts = self.count(get=0) if self.d1>1 else [self.count(get=0)]
        uniques = self.freq(get=0) if self.d1>1 else [self.freq(get=0)]
        invalids = [self.d0-j for j in counts]
        return dataframe(dim=(self.d1,4),
                         data=[[cdtyps[i],counts[i],invalids[i],len(uniques[i].keys())] for i in range(self.d1)],
                         coldtypes=[type,int,int,int],
                         features=["dtype","Valid_data","Invalid_data","Unique_data"],
                         implicit=True,
                         index=feats,
                         NOTES=f"Size: {self.dim}")

    def uniques(self,column:Union[str,None]=None):
        """
        Returns a list of unique values in a column

        column: str|None; column name, None to return a list of lists
        """
        if column == None:
            return [list(col.keys()) for col in self.freq(get=0)]
        return list(self.freq(column)[column].keys())

    def groupBy(self,column:Union[str,List[str],None]=None,namelevel:int=1):
        """
        Group values in 'column' of a dataframe by row indices/labels

        column: str|list of strings|None; column name(s), None to use index column
        namelevel: int>0; column name level to use

        Returns a dataframe or a Group object

        NOTE:
            If there are list type indices passed to 'groups', method will try to find matching indices with the values INSIDE the list
            In such case, pass the argument in a list to use the list itself as a row index
        
        """
        from .filter.grouping import grouping
        return grouping(self,column,dataframe,namelevel)

    def oneHotEncode(self,column:str,level:int=1,concat:bool=True,removecol:bool=False,returnmat:bool=True):
        """
        One-hot encode a given column 

        column: str; column name to encode
        concat: bool; wheter or not to concatanate the encoded matrix
        removecol: bool; wheter or not to remove the used column after encoding, doesn't apply if 'concat' is False
        returnmat: bool; wheter or not to return self after encoding, doesn't apply if 'concat' is False
        """
        if not column in self.features.get_level(level):
            raise NameError(f"{column} is not a column name")

        uniq = self.uniques(column)
        temp = Matrix([self.d0,len(uniq)],fill=0,dtype=dataframe).matrix
        
        for i,value in enumerate(self.col(column,0)):
            temp[i][uniq.index(value)] = 1
        encoded_matrix = Matrix(data=temp,features=uniq,dtype=int)

        if concat:
            if removecol:
                del self[column]
            return self.concat(encoded_matrix,returnmat=returnmat)
        else:
            return encoded_matrix

# =============================================================================
    """Logical-bitwise magic methods """
# =============================================================================
    def __bool__(self):
        """
        Returns True if all the elements are equal to 1, otherwise returns False
        """
        if not self.BOOL_MAT:
            return False
            
        m = self.matrix
        true = self.DEFAULT_BOOL[True]
        for i in range(self.d0):
            row = m[i]
            for j in range(self.d1):
                if row[j] != true:
                    return False
        return True

    def __invert__(self):
        """
        Returns a matrix filled with inverted elements, that is the 'not' bitwise operator
        """
        from .matrixops.bitwise import _invert
        return _invert(self,self.intForm)
    
    def __and__(self,other:Union[object,list,int,float,complex]):
        """
        Can only be used with '&' operator not with 'and'
        """        
        from .matrixops.bitwise import _and
        return _and(self,other,Matrix,self.matrix)
    
    def __or__(self,other:Union[object,list,int,float,complex]):
        """
        Can only be used with '|' operator not with 'or'
        """
        from .matrixops.bitwise import _or
        return _or(self,other,Matrix,self.matrix)
        
    def __xor__(self,other:Union[object,list,int,float,complex]):
        """
        Can only be used with '^' operator 
        """
        from .matrixops.bitwise import _xor
        return _xor(self,other,Matrix,self.matrix)
     
# =============================================================================
    """Other magic methods """
# =============================================================================
    def __contains__(self,val:object):
        """
        val: object; value to search for in the whole matrix
        Returns True or False
        syntax: "value" in Matrix
        """
        inds=self.find(val)
        return bool(inds)

    def __getitem__(self,pos:Union[object,int,str,slice,list,Tuple[Union[str,int,slice,list,Tuple[str]]]]):
        """
        Using list indices:

            Indices for full rows:
                Matrix[int]     --> Return a row
                Matrix[slice]   --> Return 0 or more rows
                Matrix[Matrix]  --> Return filtered rows
                Matrix[list]    --> Return rows using indices in the list

            Indices for full columns:
                Matrix[str]                  --> Return all rows of a column
                Matrix[:,slice]              --> Return 0 or more columns
                Matrix[:,(str,...)]          --> Return all rows of the desired columns passed as a tuple of strings (Can include duplicates)
                Matrix[:,[int,str,...]]      --> Return all rows of the desired columns passed as a tuple of strings (Can include duplicates)
                Matrix[str,str,...,str]      --> Return all rows of many columns (Can include duplicates) (Same as the previous one)

            Filtered rows and columns:
                Matrix[slice,(str,str,...,str)]   --> Return 0 or more rows of the desired columns
                Matrix[Matrix,(str,str,...,str)]  --> Return filtered rows of the desired columns 

            Indices for single values:
                Matrix[int,int]     --> Return the value in the matrix using row and column indices
                Matrix[int,str]     --> Return the value in the matrix using row index and column name
                Matrix[int,(str,)]  --> Return a single value as a 1x1 matrix

        NOTE:
            -> Level 1 column names and row labels are used as default, use 'level' property for better indexing options
        """

        from .matrixops.getsetdel import getitem
        return getitem(self,pos,Matrix,0)

    def __setitem__(self,pos:Union[object,int,str,slice,Tuple[Union[str,int,slice,Tuple[str]]]],item:Any):
        """
        Set new values to desired parts of the matrix.
        Uses same logic __getitem__ method uses.

        If a single value is given on the right-hand-side, value replaces all other values where left-hand-side represents
        Example:
            #Every row with even index numbers gets their 'Col 3' column changed to value 99
                >>> Matrix[::2,"col_3"] = 99                        
                
            #Rows where their 'Score1' is lower than 50 gets their 'Pass1' and 'Pass2' columns replaced with value 0   
                >>> Matrix[Matrix["Score1"]<50,('Pass1','Pass2')] = 0
            
                #Following method does the same changes, slightly faster on most cases
                >>> Matrix.replace(Matrix["Score1"]<50,0,('Pass1','Pass2'))
            
            Check README.md and exampleMatrices.py for more examples
        """
        from .matrixops.getsetdel import setitem
        setitem(self,pos,item,Matrix,0)

    def __delitem__(self,val:object):
        """
        Works 'similar' to __getitem__ , but can only be used to delete entire columns and/or rows
        Example:
            >>> del Matrix['col_2']     #Delete 2nd column of the matrix
        """
        from .matrixops.getsetdel import delitem
        delitem(self,val,Matrix,0)

    def __repr__(self):
        """
        Returns the matrix's string form using its row and column limits
        """
        from .matrixops.repr import _repr
        return _repr(self,self.NOTES,dataframe)
    
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        self.__dim=self._declareDim()
        s=self._stringfy(coldtypes=self.coldtypes[:])
        notes = self.NOTES
        if not isinstance(notes,str):
            raise TypeError(f"NOTES option can only be used with strings, not {type(notes).__name__}")
        if not self.isSquare:
            print("\nDimension: {0}x{1}".format(self.d0,self.d1))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}".format(self.d0))
        return s+"\n\n" + notes 
    
    @property
    def kwargs(self):
        rang = self.initRange
        rang = rang[:] if isinstance(rang,(list,tuple)) else rang
        return {"dim":self.dim[:],
                "data":[a[:] for a in self._matrix],
                "fill":self.fill,
                "ranged":rang,
                "seed":self.seed,
                "features":self.features[:],
                "decimal":self.decimal,
                "dtype":self.dtype,
                "coldtypes":self.coldtypes[:],
                "index":self.index[:],
                "implicit":True,
                "ROW_LIMIT":self.ROW_LIMIT,
                "PRECISION":self.PRECISION,
                "QR_ITERS":self.QR_ITERS,
                "EIGENVEC_ITERS":self.EIGENVEC_ITERS,
                "NOTES":self.NOTES[:],
                "DIRECTORY":self.DIRECTORY[:],
                "DEFAULT_NULL":self.DEFAULT_NULL,
                "DISPLAY_OPTIONS":self.DISPLAY_OPTIONS,
                "DEFAULT_BOOL":self.DEFAULT_BOOL,
                "BOOL_MAT":self.BOOL_MAT,
               }

    @property
    def options(self):
        return {
                "ROW_LIMIT":self.ROW_LIMIT,
                "PRECISION":self.PRECISION,
                "QR_ITERS":self.QR_ITERS,
                "EIGENVEC_ITERS":self.EIGENVEC_ITERS,
                "NOTES":self.NOTES,
                "DIRECTORY":self.DIRECTORY,
                "DEFAULT_NULL":self.DEFAULT_NULL,
                "DISPLAY_OPTIONS":self.DISPLAY_OPTIONS,
                "DEFAULT_BOOL":self.DEFAULT_BOOL,
                "BOOL_MAT":self.BOOL_MAT,
               }

    def __len__(self):
        return self.__dim[0]*self.__dim[1]

    def __call__(self,*args,**kwargs):
        r"""
        Use custom constructors.

        EXAMPLE USAGE:

        >>> from MatricesM import *

        >>> In[2]: df = dataframe(decimal=2,PRECISION=8)

        >>> In[3]: data = df([[0.525624, 0.902228, 0.655355, 0.852382],
                             [0.077884, 0.896945, 0.622809, 0.401988],
                             [0.175817, 0.051629, 0.742711, 0.492171],
                             [0.939892, 0.500976, 0.630512, 0.728549]])

        >>> In[4]: data
        >>> Out[4]:

              col_1  col_2  col_3  col_4
             +--------------------------
            0| 0.53   0.90   0.66   0.85
            1| 0.08   0.90   0.62   0.40
            2| 0.18   0.05   0.74   0.49
            3| 0.94   0.50   0.63   0.73
        

        >>> In[5]: mat = Matrix(decimal=5,PRECISION=9,
                         NOTES="9 decimal places are used in calculations\nDisplaying 5 decimals")

        >>> In[6]: matrix_1 = mat(6)

        >>> In[7]: matrix_1
        >>> Out[7]:
            
            0.29136 0.04569 0.62581 0.56670 0.56908 0.98096
            0.30619 0.69436 0.79888 0.09577 0.62117 0.55394
            0.45677 0.46080 0.36360 0.25382 0.25730 0.31367
            0.17618 0.29789 0.89245 0.46773 0.45167 0.51045
            0.38179 0.88610 0.73467 0.45546 0.94040 0.70342
            0.78188 0.88076 0.77035 0.47594 0.93677 0.21937

            9 decimal places are used in calculations
            Displaying 5 decimals

        NOTE:
            -> Positional arguments OVERWRITE keyword arguments. In the given example:
             -> mat(6,dim=100) will create a 6x6 matrix, because the first positional argument gets
                used as 'dim' instead.

            -> mat(6) is the same as mat(dim=6)    

        """
        kwargs = {**self.defaults, **kwargs} #Overwrite defaults with new values if any given
        keys = list(kwargs.keys())

        for i in range(len(args)): #Use positional arguments over keyword ones
            kwargs[keys[i]] = args[i]
                
        return Matrix(**kwargs)

    @property
    def __name__(self):
        return "Matrix"
        
# =============================================================================
    """Arithmetic methods"""        
# =============================================================================
    def __matmul__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import matmul
        return matmul(self,other,Matrix,self.matrix,dataframe)
    
    def __add__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import add
        return add(self,other,Matrix,self.matrix,dataframe)
            
    def __sub__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import sub
        return sub(self,other,Matrix,self.matrix,dataframe)
     
    def __mul__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import mul
        return mul(self,other,Matrix,self.matrix,dataframe)

    def __floordiv__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import fdiv
        return fdiv(self,other,Matrix,self.matrix,dataframe)
            
    def __truediv__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import tdiv
        return tdiv(self,other,Matrix,self.matrix,dataframe)

    def __mod__(self, other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import mod
        return mod(self,other,Matrix,self.matrix,dataframe)
         
    def __pow__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.arithmetic import pwr
        return pwr(self,other,Matrix,self.matrix,dataframe)

# =============================================================================
    """ Comparison operators """                    
# =============================================================================
    def __le__(self,other:Union[object,list,int,float]):
        from .matrixops.comparison import le
        from_wheres = self.__use_value_based_comparison or False
        return le(self,other,dataframe,self.matrix,from_wheres,Matrix)
        
    def __lt__(self,other:Union[object,list,int,float]):
        from .matrixops.comparison import lt
        from_wheres = self.__use_value_based_comparison or False
        return lt(self,other,dataframe,self.matrix,from_wheres,Matrix)
        
    def __eq__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.comparison import eq
        from_wheres = self.__use_value_based_comparison or False
        return eq(self,other,dataframe,self.matrix,from_wheres,Matrix)
        
    def __ne__(self,other:Union[object,list,int,float,complex]):
        from .matrixops.comparison import ne
        from_wheres = self.__use_value_based_comparison or False
        return ne(self,other,dataframe,self.matrix,from_wheres,Matrix)
                
    def __ge__(self,other:Union[object,list,int,float]):
        from .matrixops.comparison import ge
        from_wheres = self.__use_value_based_comparison or False
        return ge(self,other,dataframe,self.matrix,from_wheres,Matrix)
        
    def __gt__(self,other:Union[object,list,int,float]):
        from .matrixops.comparison import gt
        from_wheres = self.__use_value_based_comparison or False
        return gt(self,other,dataframe,self.matrix,from_wheres,Matrix)
        
# =============================================================================
    """ Rounding etc. """                    
# =============================================================================   
    def __round__(self,n:int=-1,dec:Union[int,None]=None):
        from .matrixops.rounding import rnd
        return rnd(self,n,dec,Matrix,self.matrix,dataframe)
    
    def __floor__(self):
        from .matrixops.rounding import flr
        return flr(self,Matrix,self.matrix,dataframe)     
    
    def __ceil__(self):
        from .matrixops.rounding import ceil
        return ceil(self,Matrix,self.matrix,dataframe)
    
    def __abs__(self):
        from .matrixops.rounding import _abs
        return _abs(self,Matrix,self.matrix,dataframe)

###############################################################################

class dataframe(Matrix):
    def __init__(self,
                 data:Union[List[Any],List[List[Any]],Any]=[],
                 features:Union[Label,List[str]]=[],
                 coldtypes:List[type]=[],
                 **kwargs):
        
        kwargs = {**{"data":data,"dtype":dataframe,
                     "decimal":3,"features":features,
                     "coldtypes":coldtypes},
                  **kwargs}

        super().__init__(**kwargs)

    def __call__(self,*args,**kwargs):
        kwargs = {**self.defaults, **kwargs} #Overwrite defaults with new values if any given
        keys = list(kwargs.keys())

        for i in range(len(args)): #Use positional arguments over keyword ones
            kwargs[keys[i+1]] = args[i] # i+1 to skip first
        
        return dataframe(**kwargs)

###############################################################################

class Identity(Matrix):
    def __init__(self,dim,**kwargs):
        super().__init__(dim=dim,data=eye(dim),**kwargs)

###############################################################################

class Symmetrical(Matrix):
    def __init__(self,dim,**kwargs):
        super().__init__(dim=dim,data=sym(dim),**kwargs)

###############################################################################

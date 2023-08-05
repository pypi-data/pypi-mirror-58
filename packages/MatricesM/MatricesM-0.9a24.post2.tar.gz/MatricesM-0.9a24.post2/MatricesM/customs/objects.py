from typing import List

#Forward declaration
class dataframe:
    pass

class null:
    def __init__(self):
        self.real = 0
        self.imag = 0
        self.denominator = 1
        self.numerator = 0

    def __call__(self,*args):
        return null
    def __hash__(self):
        return hash(type(self))
    def __len__(self):
        return 4
    def __round__(self,*args):
        return null

    @property
    def __name__(self):
        return 'null'
    def __str__(self):
        return 'null'
    def __repr__(self):
        return 'null'
    def __format__(self,*args):
        return 'null'
    
    def __le__(self,other):
        return True
    def __lt__(self,other):
        return True
    def __ge__(self,other):
        return False
    def __gt__(self,other):
        return False
    def __eq__(self,other):
        return True if type(other).__name__ == 'null' else False
    def __ne__(self,other):
        return True if type(other).__name__ != 'null' else False

null = null()

class date:
    """
    Date object, define patterns for the date and time data
    data: str; string format of the data
    pattern: str; string to format the data with. 
    delimiters: list of strings; delimiters to use
    
    Usage:
        day "d"
        month "m"
        year "y"

        hour "h"
        minute "n"
        second "s"
 
        milli "3"
        micro "6"
        nano "9"

        timezone "t"

        Create a pattern using the terms above. Example:

            Example pattern             Expected input pattern                     Expected input sample

             yyyy/mm/dd             -->  Year/Month/Day                        -->  2019/10/25
             dd hh:nn:ss            -->  Day Hours:Minutes:Seconds             -->  25 16:32:55
             yyyymmdd,ttttt,hh:nn   -->  YearMonthDay,timezone,Hours:Minutes   -->  19980409,UTC+3,21:45

    """
    def __init__(self,date:str,pattern:str,delimiters:List[str],config:str="default"):
        self.date = date
        self.delimiters = delimiters
        self.pattern = self.fixpattern(pattern)
    
    @staticmethod
    def fixpattern(pattern,cfg):
        if cfg == "default":
            day,month,year = "d","m","y"
            hour,minute,second = "h","n","s"
            milli,micro,nano = "3","6","9"
            tzone = "t"
            terms = [day,month,year,hour,minute,second,milli,micro,nano,tzone]
            delims = self.delimiters[:]

            #Assert given delimiters are valid
            for delimiter in delims:
                if delimiter in terms:
                    raise ValueError(f"Character {delimiter} can't be used as a delimiter")

            input_pattern_term_indices = {"d":0,"m":0,"y":0,"h":0,"n":0,"s":0,"3":0,"6":0,"9":0}
            delimiter_indices = {i:[] for i in delims}
            #Check for terms' every appearance
            for term in terms:
                #Regex pattern for repeated characters
                term_pattern = term + "+"
                
                #Find out what repeated characters patterns are
                partition = {i:[] for i in sorted(re.findall(term_pattern,pattern),reverse=True)}
                
                #Store starting and the ending points of the found patterns
                for part in list(partition.keys()):
                    pattern_copy = pattern[:]
                    while True:
                        lap = 0
                        try:
                            #Start getting all indices of the pattern
                            while part in pattern_copy:
                                l = len(part)
                                ind = pattern_copy.index(part)
                                #Replace the used part with question marks
                                pattern_copy = pattern_copy[:ind] + pattern_copy[ind+l:]
                        except:
                            #Store them
                            input_pattern_term_indices[term][part].append((ind+l*lap,ind+l*(lap+1)))
                            lap += 1
                        else:
                            #All indices stored, get to the next pattern
                            break
                #Should have input_pattern_term_indices -> {"d":{"ddd":[(1,4),(5,8)],"d":[(15,16)]},"m":...}
                
                #Create a regex pattern for the entire pattern using collected indices
                pass

    def __repr__(self):
        return "".join(re.findall(self.date,self.pattern))

class Group:
    def __init__(self,matrix_list,names):
        self.grouped_by = tuple(names)
        self.level = len(names)
        self.groups = []
        self.tables = []
        
        for val in matrix_list:
            if isinstance(val[0],list):
                self.groups.append(tuple(val[0]))
            else:
                self.groups.append(val[0])
            self.tables.append(val[1])

    def __getitem__(self,pos):
        """
        Integer indexing through group tables

        Examples:

            >>> df = dataframe(fill=uniform)
            >>> data = df(dim=(15,3),ranged={"c1":(0,5),"c2":(0,2),"c3":(-5,-1)}) 
            >>> data

                  |c1  c2  c3
                  +----------
                 0| 2   1  -3
                 1| 2   2  -3
                 2| 3   2  -5
                 3| 2   1  -1
                 4| 1   2  -1
                 5| 3   3  -2
                 6| 5   1  -5
                 7| 3   0  -3
                 8| 4   1  -1
                 9| 2   3  -4
                10| 4   2  -1
                11| 3   0  -1
                12| 3   1  -2
                13| 2   1  -3
                14| 1   0  -1
            
            >>> group_1 = data.groupBy("c1")
            >>> group_1.tables

                [
                  |c1  c2  c3
                  +----------
                 0| 2   1  -3
                 1| 2   2  -3
                 3| 2   1  -1
                 9| 2   3  -4
                13| 2   1  -3
                ,
                  |c1  c2  c3
                  +----------
                 2| 3   2  -5
                 5| 3   3  -2
                 7| 3   0  -3
                11| 3   0  -1
                12| 3   1  -2
                ,
                  |c1  c2  c3
                  +----------
                 4| 1   2  -1
                14| 1   0  -1
                ,
                 |c1  c2  c3
                 +----------
                6| 5   1  -5
                ,
                  |c1  c2  c3
                  +----------
                 8| 4   1  -1
                10| 4   2  -1
                ]

            >>> group_1.groups

                [2, 3, 1, 5, 4]
            
            >>> group_1.grouped_by
            
                ('c1',)

            >>> group_1[3]
            
                  |c1  c2  c3
                  +----------
                 2| 3   2  -5
                 5| 3   3  -2
                 7| 3   0  -3
                11| 3   0  -1
                12| 3   1  -2

        """

        if pos not in self.groups:
            raise KeyError(f"{pos} is not a value in grouped values")

        return self.tables[self.groups.index(pos)]


class Label:
    """
    Enables single and multi-level indexing for dataframe's row labels or column names

    labels: [Any,...] | [Tuple(Any,...),...] ; Labels in a list.

    Example:

        >>> labels = [('group_1','class_1'),
                      ('group_2','class_3'),
                      ('group_3','class_2'),
                      ('group_1','class_3')] 
        
        >>> names = ('groups','classes')

        >>> rowlabels = Label(labels,names)

        >>> rowlabels
        
        Label(
              names:  ['groups', 'classes']
              labels: ('group_1', 'class_1')
                      ('group_2', 'class_3')
                      ('group_3', 'class_2')
                      ('group_1', 'class_3')
            
              size:   (4,2)
             )

        >>> dataframe(dim=(4,3),
                      index=rowlabels
                      )
        
                        col_1  col_2  col_3
         groups,classes+-------------------
        group_1,class_1| null   null   null
        group_2,class_3| null   null   null
        group_3,class_2| null   null   null
        group_1,class_3| null   null   null

    """
    def __init__(self,labels:[(...,),...]=[],names:(str,...)=("",),implicit:bool=False):
        self.__labels = labels
        self.__names = names
        self.__level = 1
        if not implicit:
            self.setup(labels,names)
        
    def setup(self,lbls:[(...,),...],nms=[str,...]):
        ####### Label check #######
        type_names = ["Matrix","dataframe","Identity","Symmetrical"]

        if type(lbls).__name__ in type_names:
            nms = lbls.features.get_level(1)
            lvl = lbls.d1
            lbls = [tuple(row) for row in lbls.matrix]
            self.__names = nms
            self.__labels = lbls
            self.__level = lvl
            return None

        elif isinstance(lbls,str):
            lbls = [lbls]
        
        elif isinstance(lbls,tuple):
            lbls = list(lbls)

        elif not isinstance(lbls,list):
            raise TypeError(f"Expected list/Matrix/str/tuple type for 'labels' parameter, got {type(lbls)} instead")
        
        lvl = 1
        lbls_len = len(lbls)
        
        #Multi-leveled, all tuples
        if all([1 if isinstance(val,tuple) else 0 for val in lbls]) and lbls_len>0:
            #Check tuple lengths
            lengths = [len(label) for label in lbls]
            maxlvl = max(lengths)
            for i in range(len(lbls)):
                lbls[i] += tuple(["" for _ in range(maxlvl-lengths[i])]) 
        else:
            lbls = [(label,) for label in lbls]

        #Recalculate dimensions
        maxlvl = max([len(label) for label in lbls]) if len(lbls)>=1 else 1
        diff = maxlvl - lvl

        #Refill labels if lvl is changed
        if diff:
            for i in range(len(lbls)):
                lbls[i] += tuple(["" for _ in range(maxlvl-len(lbls[i]))])

        lvl = maxlvl

        ####### Name check #######
        if isinstance(nms,str):
            if lvl != 1:
                raise IndexError(f"Can't set level-{lvl} index column names to a single string")
            nms = (nms,)
        elif isinstance(nms,(tuple,list)):
            nms = list(nms)
            if len(nms) != lvl:
                nms = ["level_"+str(i+1) for i in range(lvl)]
        else:
            raise TypeError(f"Can't use type {type(nms)} to set index column names")
        
        if not all([1 if isinstance(name,str) else 0 for name in nms]):
            raise TypeError(f"Can't use non-str types for index column names")
        
        from collections import Counter
        if len(Counter(nms).keys()) != len(nms):
            #Non-unique names appear
            temp = []
            for i in range(len(nms)):
                name = nms[i]
                while name in temp:
                    name = "_"+name
                temp.append(name)
            nms = temp[:]
            
        self.__names = nms[:]
        self.__labels = [row[:] for row in lbls]
        self.__level = lvl
 
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,level:int):
        if not isinstance(level,int):
            raise TypeError("Level can't be non-int")
        if level<=0:
            raise ValueError("Level can't be less or equal to zero")

        self.__level = level

    @property
    def labels(self):
        return self.__labels
    @labels.setter
    def labels(self,labels:[(...,),...]):
        self.setup(labels,self.names)

    @property
    def names(self):
        return self.__names
    @names.setter
    def names(self,names:[str,...]):
        self.setup(self.labels,names)

    @property
    def size(self):
        return (len(self.labels),self.level)

    def get_name(self,name:[str,...]):
        """
        Return given index columns named given name(s)
        """
        if isinstance(name,str):
            name = [name]
        
        if not isinstance(name,list):
            raise TypeError("'name' parameter only accepts str or list types")

        all_names = self.names
        labels = self.labels

        #Get inner indices
        try:
            level_inds = [all_names.index(val) for val in name]
        except:
            raise ValueError("Given name(s) not in the column names")
            
        if level_inds == []:
            return Label()
        return Label([tuple([labels[i][name_ind] for name_ind in level_inds]) for i in range(len(labels))],name)

    def get_label(self,label:[...,],level:int=1,return_inds:bool=False):
        """
        Label indexing over the labels list, returns the labels or the integer
        indices of the found labels in the list
        
        Multiple labels can be passed in a list
                
            >>> labels = [('group_1','class_1'),
                         ('group_2','class_3'),
                         ('group_3','class_2'),
                         ('group_1','class_3')]
            
            >>> names = ("groups","classes")

            >>> Label(labels,names).get_label(label='group_1',level=1)

            Label(
                  names:  ('groups', 'classes')
                  labels: ('group_1', 'class_1')
                          ('group_2', 'class_3')
                          ('group_3', 'class_2')
                          ('group_1', 'class_3')
                 )

        """
        label_list = self.labels
        if isinstance(label,str):
            label = [label]
        rowinds = [i for i in range(len(label_list)) if label_list[i][level-1] in label]

        if rowinds == []:
            raise ValueError("No label found")

        if return_inds:
            return rowinds
        return Label([label_list[i] for i in rowinds],self.names)
    
    def get_level(self,level:int):
        """
        Return labels of the desired level in a list
        """
        name_len = len(self.names)
        if name_len == 0:
            raise IndexError("No names in Label")
        if not isinstance(level,int):
            raise TypeError("Level can't be non-int")
        if level<=0 or level>name_len:
            raise ValueError(f"Level should be an int between 1 and {name_len}")
        
        return [label[0] for label in self.get_name(self.names[level-1]).labels]

    def add_level(self,labels,names=None):
        """
        Add a new level for each label
        """
        type_names = ["Matrix","dataframe","Identity","Symmetrical"]
        name_skip = False

        labels = [row if isinstance(row,tuple) else (row,) for row in labels] if isinstance(labels,list) \
                 else labels.labels if isinstance(labels,Label) \
                 else labels if type(labels).__name__ in type_names \
                 else None
        
        if labels == None:
            raise TypeError("'labels' only accepts list and Label")
        
        elif len(labels) != len(self):
            raise IndexError(f"Expected {len(self)} labels, got {len(labels)} instead")

        elif type(labels).__name__ in type_names:
            if labels.d0 != len(self):
                raise IndexError(f"Expected {len(self)} labels, got {labels.d0} instead")

            names = labels.features if names == None else names
            name_skip = True

            labels = [tuple(row) for row in labels.matrix]
            
        if not name_skip:
            if names == None:
                names = [""]

            elif isinstance(names,str):
                names = [names]
            
            elif isinstance(names,tuple):
                names = list(names)
            
            elif not isinstance(names,(list,tuple)):
                raise TypeError("Names should be given in a list as strings")

        self.setup([old+labels[i] for i,old in enumerate(self.labels)],self.names+names)

    def sort_by(self,level:int=1,key:object=lambda a:a[1],reverse:bool=False,ret:bool=False):
        """
        Sort the labels in the given level with the given function

        level: int=1; label level to sort by
        key: function; key function to use for sorting
        reverse: bool=False; wheter or not to use reverse sorting
        ret: bool=False; wheter or not to return the label after sorting
        """
        pass
    
    @property
    def as_df(self):
        from ..matrix import dataframe
        return dataframe(data=[list(row[:]) for row in self.labels],features=self.names[:])

    @property
    def copy(self):
        return Label(labels=[tuple(lbl) for lbl in self.labels],
                     names=tuple([str(name) for name in self.names]))

    def reset(self,start:int=0,name:str=""):
        """
        Reset back to a level 1 Label, use integer labels starting from 'start'
        """
        self.setup(list(range(start,len(self)+start)),name)

    def label_update(self,level:int,prefix:str="",suffix:str="",changechar:(str,str)=None):
        """
        Update string type row labels
        
        level: int; level of the labels to update
        prefix: str; string to add to the begining of the row label
        suffix: str; string to add to the end of the row label
        changechar: list or tuple of strings| None; character to change into other given character

        Example:
            #Add 'pos_' prefix to the labels, then change ' ' characters into '_' character
                >>> Label.label_update(level=1,
                                       prefix='pos_',
                                       changechar=(' ','_')) 
        """
        ch_char = False
        if not isinstance(changechar,(tuple,list)) and changechar != None:
            raise TypeError("'changechar' should be a tuple/list with 2 strings or None")
        else:
            if changechar != None:
                assert len(changechar)==2 , "Given list/tuple should have 2 strings"
                assert isinstance(changechar[0],str) and isinstance(changechar[1],str) , "tuple/list have to have strings"
                ch_char = True
        assert isinstance(prefix,str) and isinstance(suffix,str) , "Prefix and suffix should be strings"

        labels = self.labels

        #Update string labels
        for i,row in enumerate(labels):
            val = row[level-1]
            if isinstance(val,str):
                val = prefix+val+suffix
                if ch_char:
                   val = val.replace(changechar[0],changechar[1])  
            temp = list(row)
            temp[level-1] = val
            labels[i] = tuple(temp)

    def insert(self,pos,item):
        item = item if isinstance(item,tuple) else (item,)

        len_item = len(item)
        lvl = self.level

        if len_item != lvl:
            if len_item == 1 and lvl != 1:
                item = item*lvl
            else:
                raise IndexError(f"Expected {lvl} or 1 labels, got {len_item}")

        self.labels.insert(pos,item)

    def append(self,obj):
        self.__add__(obj)

    def index(self,obj,level=1):
        return self.get_level(level).index(obj)

    def __add__(self,obj):
        """
        Append labels to the labels list
        """
        type_names = ["Matrix","dataframe","Identity","Symmetrical"]
        obj = [obj] if isinstance(obj,tuple) \
              else obj if isinstance(obj,list) \
              else obj.labels if isinstance(obj,Label) \
              else [tuple(row) for row in obj.matrix] if type(obj).__name__ in type_names \
              else [(obj,)]

        self.labels += obj
        return self

    def __len__(self):
        return len(self.labels)

    def __repr__(self):
        ROW_LIMIT = 25
        lbls = self.labels
        if len(self)>ROW_LIMIT:
            str_labels = "\n              ".join([str(row) for row in lbls[:ROW_LIMIT//2]+["..."]+lbls[-ROW_LIMIT//2:]])
        else:
            str_labels = "\n              ".join([str(row) for row in self.labels])
        return "\nLabel(\n      names:  "+ str(self.names) +"\n      labels: "+ str_labels + f"\n\n      size:   ({len(self)},{self.level})" + "\n     )"

    def __getattr__(self,attr:str):
        try:
            return object.__getattribute__(self,attr)
        except:
            try:
                return self.get_name(attr)
            except:
                raise ValueError(f'{attr} is neither a level-1 label nor an attribute' )

    def __getitem__(self,pos):
        """
        Integer indexing over labels list
        
        """
        labels = self.labels
        items = labels[pos] if isinstance(pos,slice) \
                            else [labels[pos]] if isinstance(pos,int) \
                            else [labels[i] for i in pos] if isinstance(pos,list) \
                            else None

        return Label(items,self.names)
    
    def __setitem__(self,pos,val):
        """
        Set new labels
        """
        #Label given
        if isinstance(val,Label):
            val = val.labels
            if len(val) == 0:
                raise IndexError("No labels found")
            
            #Single label update
            if isinstance(pos,int):
                self.labels[pos] = val[0]
            
            #Slices for multiple label update
            elif isinstance(pos,slice):
                from ..matrixops.getsetdel import betterslice
                pos = betterslice(pos,len(self))
                if abs(pos.stop-pos.start) != len(val):
                    raise IndexError(f"Expected {abs(pos.stop-pos.start)} items, got {len(val)} instead")
                self.labels[pos] = val

            #List of indices for multiple label update
            elif isinstance(pos,list):
                if len(pos) != len(val):
                    raise IndexError(f"Expected {len(pos)} items, got {len(val)} instead")
                for i,j in enumerate(pos):
                    self.labels[j] = val[i]
            
            #Wrong type
            else:
                raise TypeError(f"{pos} can't be used as indices")
        
        else:
            self.labels[pos] = val

        #Recalculate dimensions
        labels = self.labels
        current = self.level
        lvl = max([len(label) for label in labels])
        diff = lvl - current

        self.__names += tuple(["level_"+str(current+i+1) for i in range(lvl-len(self.names))])

        #Refill labels if lvl is changed
        if diff:
            for i in range(len(self)):
                self.__labels[i] += tuple(["" for _ in range(lvl-len(labels[i]))])

        self.__level = lvl

    def __delitem__(self,pos):
        del self.labels[pos]
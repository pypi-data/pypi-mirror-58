def _rank(mat,col,rev,key,get,start):
    
    if not mat._dfMat:
        raise TypeError("'ranked' method only works with dataframes")
    
    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    if isinstance(col,(tuple,str)):
        col=feats.index(col)+1

    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        col -= 1
        
    if not isinstance(start,int):
        raise TypeError("'start' only accepts integers")

    ranks={}
    feats = mat.features[:].labels if col == None else mat.features[col].labels

    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    for i,name in enumerate(feats):
        #Get the column and store copy to return
        column = mat[:,i].copy
        copy = column.copy
        #Reset indices and sort
        column.index.reset()
        column.sortBy(1,reverse=rev,key=key)
        inds = column.index.get_level(1)
        #Updated indices
        temp = ["" for _ in range(column.d0)]
        for i,ind in enumerate(inds):
            temp[ind] = i+start
        #Add ranks then set values as indices
        copy.add(temp,col=2,feature="Rank",dtype=int)
        copy.index = copy[:,0]
        #Add to dictionary
        ranks[name] = copy[:,1]

    #Return ranks in-place of the values
    if get == -1:
        temp = mat.copy

        for col,rankmat in enumerate(ranks.values()):
            temp[:,col] = rankmat["Rank"]

        temp._Matrix__coldtypes = [int for _ in range(temp.d1)]
        return temp
    #Return matrices in a tuple
    elif get == 2:
        items = tuple([val for val in ranks.values()])
        if len(items)==1:
            return items[0]
        return items
    #Return a dictionary
    elif get == 1:
        return {feat:lis.col("Rank",0) for feat,lis in ranks.items()}
    #Return a list
    else:
        items=[lis.col("Rank",0) for lis in ranks.values()]
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[0]

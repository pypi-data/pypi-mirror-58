# This source code file is a part of SigProfilerTopography
# SigProfilerTopography is a tool included as part of the SigProfiler
# computational framework for comprehensive analysis of mutational
# signatures from next-generation sequencing of cancer genomes.
# SigProfilerTopography provides the downstream data analysis of
# mutations and extracted mutational signatures w.r.t.
# nucleosome occupancy, replication time and strand bias.
# Copyright (C) 2018 Burcak Otlu

###################################################################################
################ This python code read the nucleosome occupancy filename ##########
######################## Remove the outliers or not ###############################
###### Write the chromosome based average nucleosome occupancy signal arrays ######
###################################################################################

#TODO This code will be updated for histone occupancy analysis.
#Unnecessary code will be removed.
#This code must be working for bed or wig files.
#Converting bed and wig files into chr based dataframes and then chr based arrays

#unnesting requires too much memory because of that jobs sleep and then become zombie
import os
import matplotlib
import sys
from sys import getsizeof

BACKEND = 'Agg'
if matplotlib.get_backend().lower() != BACKEND.lower():
    # If backend is not set properly a call to describe will hang
    matplotlib.use(BACKEND)

from matplotlib import pyplot as plt
#To plot for bi range of x axis such as 250M
plt.rcParams['agg.path.chunksize'] = 10000

#############################################################
current_abs_path = os.path.dirname(os.path.realpath(__file__))
#############################################################

commonsPath = os.path.join(current_abs_path, '..','commons')
sys.path.append(commonsPath)

from TopographyCommons import *

#########################################################################
def unnesting(df, explode):
    idx=df.index.repeat(df[explode[0]].str.len())
    df1=pd.concat([pd.DataFrame({x:np.concatenate(df[x].values)} )for x in explode],axis=1)
    df1.index=idx
    return df1.join(df.drop(explode,1),how='left')
#########################################################################



######################################################################
# Requires too much memory results in first sleeping and then zombie jobs
def computeSignalArrayAndCountArray(chromSize,chrBased_nucleosome_df):

    print('for debug in computeSignalArrayAndCountArrayForEachChr starts')
    print('before key column added')
    print('getsizeof(chrBased_nucleosome_df): %d in MB' %int(getsizeof(chrBased_nucleosome_df)/1000000))

    chrBased_nucleosome_df['key'] = [list(range(x, y)) for x, y in zip(chrBased_nucleosome_df.start, chrBased_nucleosome_df.end)]
    print('after key column added')
    print('getsizeof(chrBased_nucleosome_df): %d in MB' %int(getsizeof(chrBased_nucleosome_df)/1000000))

    chrBased_nucleosome_df.drop(['start','end'], axis=1, inplace=True)
    print('after drop column')
    print('getsizeof(chrBased_nucleosome_df): %d in MB' %int(getsizeof(chrBased_nucleosome_df)/1000000))

    # Unnest and  generate signalArray and countArray
    chrBasedNucleosomeDFSignalArray = unnesting(chrBased_nucleosome_df,['key']).groupby('key').signal.sum().reindex(list(range(chromSize))).fillna(0).values
    chrBasedNucleosomeDFCountArray = unnesting(chrBased_nucleosome_df,['key']).groupby('key').signal.count().reindex(list(range(chromSize))).fillna(0).values

    print('getsizeof(chrBasedNucleosomeDFSignalArray): %d MB' %int(getsizeof(chrBasedNucleosomeDFSignalArray)/1000000))
    print('getsizeof(chrBasedNucleosomeDFCountArray): %d MB' %int(getsizeof(chrBasedNucleosomeDFCountArray)/1000000))
    print('np.sum(chrBasedNucleosomeDFSignalArray)')
    print(np.sum(chrBasedNucleosomeDFSignalArray, dtype=np.float64))
    print('np.sum(chrBasedNucleosomeDFCountArray)')
    print(np.sum(chrBasedNucleosomeDFCountArray, dtype=np.float64))
    print('for debug in computeSignalArrayAndCountArrayForEachChr ends')
    return chrBasedNucleosomeDFSignalArray, chrBasedNucleosomeDFCountArray
######################################################################



######################################################################
def updateSignalArrays(row,signalArray):
    signalArray[row[start]:row[end]] += row[signal]
######################################################################

######################################################################
def updateSignalArraysForListComprehension(row,signalArray):
    #row [chrom start end signal]
    signalArray[row[1]:row[2]] += row[3]
######################################################################

######################################################################
# This is used right now.
def writeChrBasedOccupancySignalArraysAtOnceInParallel(inputList):
    chrLong = inputList[0]
    chromSize = inputList[1]
    chrBasedFileDF = inputList[2]
    filename = inputList[3]
    occupancy_type= inputList[4]
    max_signal=inputList[5]
    min_signal = inputList[6]

    if (occupancy_type==EPIGENOMICSOCCUPANCY):
        os.makedirs(os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,EPIGENOMICS,CHRBASED), exist_ok=True)
    elif (occupancy_type==NUCLEOSOMEOCCUPANCY):
        os.makedirs(os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,NUCLEOSOME,CHRBASED), exist_ok=True)

    filenameWoExtension = os.path.splitext(os.path.basename(filename))[0]

    if (np.finfo(np.float16).min<=min_signal) and (max_signal<=np.finfo(np.float16).max):
        signalArray = np.zeros(chromSize, dtype=np.float16)
    else:
        signalArray = np.zeros(chromSize,dtype=np.float32)

    # Using apply
    # chrBasedFileDF.apply(updateSignalArrays, signalArray=signalArray, axis=1)

    # Use list comprehension
    [updateSignalArraysForListComprehension(row,signalArray) for row in chrBasedFileDF.values]

    #############################  Save as npy starts ################################
    signalArrayFilename = '%s_signal_%s' %(chrLong,filenameWoExtension)
    # signalArrayFilenameText = '%s_signal_%s.txt' %(chrLong,filenameWoExtension)
    if occupancy_type==EPIGENOMICSOCCUPANCY:
        # chrBasedSignalFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,EPIGENOMICS,CHRBASED,signalArrayFilenameText)
        # np.savetxt(chrBasedSignalFile, chrBasedFileDF.values,fmt='%s %d %d %f')
        chrBasedSignalFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,EPIGENOMICS,CHRBASED,signalArrayFilename)
        np.save(chrBasedSignalFile, signalArray)

    if occupancy_type==NUCLEOSOMEOCCUPANCY:
        chrBasedSignalFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,NUCLEOSOME,CHRBASED,signalArrayFilename)
        np.save(chrBasedSignalFile, signalArray)
    #############################  Save as npy ends ##################################

######################################################################




######################################################################
def readChromBasedNucleosomeDF(chrLong,nucleosomeFilename):
    chrBasedNucleosmeFilename = '%s_%s' %(chrLong,nucleosomeFilename)
    chrBasedNucleosmeFilePath = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB, NUCLEOSOME, CHRBASED, chrBasedNucleosmeFilename)

    if (os.path.exists(chrBasedNucleosmeFilePath)):
        column_names = [chrom, start, end, signal]
        # chrbased_nucleosome_df = pd.read_table(chrBasedNucleosmeFilePath, sep="\t", header=None, comment='#', names=column_names,dtype={'chrom': str, 'start': np.int32, 'end': np.int32, 'signal': np.float16})
        chrbased_nucleosome_df = pd.read_table(chrBasedNucleosmeFilePath, sep="\t", header=None, comment='#',names=column_names, dtype={chrom: str, start: np.int32, end: np.int32, signal: np.float32})
        return chrbased_nucleosome_df
    else:
        return None
######################################################################

######################################################################
#main function parallel
# parallel it does not end for big chromosomes
def plotChrBasedNucleosomeOccupancyFigures(genome,nucleosomeFilename):
    #read chromnames for this nucleosome data

    nucleosomeFilenameWoExtension = nucleosomeFilename[0:-4]

    chromSizesDict = getChromSizesDict(genome)
    chromNamesList = list(chromSizesDict.keys())

    #Start the pool
    numofProcesses = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(numofProcesses)

    poolInputList = []
    for chrLong in chromNamesList:
        chromBasedNucleosomeDF = readChromBasedNucleosomeDF(chrLong,nucleosomeFilename)
        if chromBasedNucleosomeDF is not None:
            inputList = []
            inputList.append(chrLong)
            inputList.append(nucleosomeFilenameWoExtension)
            poolInputList.append(inputList)

    pool.map(plotNucleosomeOccupancySignalCountFiguresInParallel,poolInputList)

    ################################
    pool.close()
    pool.join()
    ################################

######################################################################

######################################################################
#main function sequential
def plotChrBasedNucleosomeOccupancyFiguresSequential(genome,nucleosomeFilename):
    #read chromnames for this nucleosome data
    nucleosomeFilenameWoExtension = nucleosomeFilename[0:-4]

    chromSizesDict = getChromSizesDict(genome)
    chromNamesList = list(chromSizesDict.keys())

    for chrLong in chromNamesList:
        #Actually no need for such a check
        chromBasedNucleosomeDF = readChromBasedNucleosomeDF(chrLong,nucleosomeFilename)
        if chromBasedNucleosomeDF is not None:
            inputList = []
            inputList.append(chrLong)
            inputList.append(nucleosomeFilenameWoExtension)
            plotNucleosomeOccupancySignalCountFiguresInParallel(inputList)
######################################################################



######################################################################
#main function
def plotChrBasedNucleosomeOccupancyFiguresFromText(genome,nucleosomeFilename):
    #read chromnames for this nucleosome data

    nucleosomeFilenameWoExtension = nucleosomeFilename[0:-4]

    chromSizesDict = getChromSizesDict(genome)
    chromNamesList = list(chromSizesDict.keys())

    #Start the pool
    numofProcesses = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(numofProcesses)

    poolInputList = []
    for chrLong in chromNamesList:
        chromBasedNucleosomeDF = readChromBasedNucleosomeDF(chrLong,nucleosomeFilename)
        if chromBasedNucleosomeDF is not None:
            inputList = []
            inputList.append(chrLong)
            inputList.append(nucleosomeFilenameWoExtension)
            poolInputList.append(inputList)

    pool.map(plotNucleosomeOccupancySignalCountFiguresInParallelFromTextFiles,poolInputList)

    ################################
    pool.close()
    pool.join()
    ################################

######################################################################


######################################################################
def  readNucleosomeOccupancyData(quantileValue,nucleosomeFilename):

    column_names = [chrom, start, end, signal]
    nucleosome_df = pd.read_table(nucleosomeFilename, sep="\t", header=None, comment='#', names=column_names, dtype={chrom: str, start: np.int32, end: np.int32, signal: np.float32})

    print('After nucleosome occupancy is loaded into memory')
    memory_usage()

    #########################################################
    if (quantileValue < 1.0):
        # remove the outliers
        q = nucleosome_df[SIGNAL].quantile(quantileValue)
        print('q:%f' % q)
        print('before %d' % (nucleosome_df.shape[0]))
        nucleosome_df = nucleosome_df[nucleosome_df[SIGNAL] < q]

        print('After nucleosome_df is subset')
        memory_usage()
    #########################################################

    nucleosome_df_grouped = nucleosome_df.groupby(chrom)

    print('After nucleosome occupancy grouped by')
    memory_usage()

    return nucleosome_df_grouped
######################################################################


######################################################################
def readAllNucleosomeOccupancyDataAndWriteChrBasedSignalCountArraysSequentially(genome, quantileValue, nucleosomeFilename):
    chromSizesDict = getChromSizesDict(genome)

    print('Before nucleosome occupancy is loaded into memory')
    memory_usage()

    # column_names = [chrom, start, end, signal]
    if os.path.exists(nucleosomeFilename):

        nucleosome_df_grouped = readNucleosomeOccupancyData(quantileValue,nucleosomeFilename)

        # nucleosome_df = pd.read_table(nucleosomeFilename, sep="\t", header=None, comment='#', names=column_names, dtype={chrom: str, start: np.int32, end: np.int32, signal: np.float32})
        #
        # print('After nucleosome occupancy is loaded into memory')
        # memory_usage()
        #
        # if (quantileValue<1.0):
        #     #remove the outliers
        #     q = nucleosome_df[SIGNAL].quantile(quantileValue)
        #     print('q:%f' % q)
        #     print('before %d' % (nucleosome_df.shape[0]))
        #     nucleosome_df = nucleosome_df[nucleosome_df[SIGNAL] < q]
        #
        #     print('After nucleosome_df is subset')
        #     memory_usage()
        #
        #     nucleosome_df_grouped = nucleosome_df.groupby(chrom)

        print('After nucleosome occupancy grouped by')
        memory_usage()

        for chrLong, chromBasedNucleosomeDF in nucleosome_df_grouped:
            print('Debug June 13, 2019 For %s write nucleosome signal and count array' %(chrLong))
            chromSize = chromSizesDict[chrLong]
            inputList = []
            inputList.append(chrLong)
            inputList.append(chromSize)
            inputList.append(chromBasedNucleosomeDF)
            inputList.append(nucleosomeFilename)
            writeChrBasedOccupancySignalArraysAtOnceInParallel(inputList)

        print('After all chr based files are written')
        memory_usage()
######################################################################


#######################################################
def deleteChrBasedNpyFiles(chrBasedNpyFilesPath):
    #############################################
    # Delete the chrBasedNpyFilesPath if exists

    ################################################
    if (os.path.exists(chrBasedNpyFilesPath)):
        try:
            shutil.rmtree(chrBasedNpyFilesPath,ignore_errors=True)
        except OSError as e:
            print('Error: %s - %s.' % (e.filename, e.strerror))
    ################################################
#######################################################



######################################################################
#Dec 2, 2019
def readBEDandWriteChromBasedSignalArrays(genome,BEDFileWithPath,occupancy_type):
    chromSizesDict = getChromSizesDict(genome)
    numofProcesses = multiprocessing.cpu_count()

    #To reduce memory footprint
    # Delete old chr based epigenomics files
    if occupancy_type==EPIGENOMICSOCCUPANCY:
        chrBasedNpyFilesPath=os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB, EPIGENOMICS, CHRBASED)
        deleteChrBasedNpyFiles(chrBasedNpyFilesPath)

    if os.path.exists(BEDFileWithPath):
        bedFile=os.path.basename(BEDFileWithPath)

        bedfilename, bedfile_extention= os.path.splitext(bedFile)

        if (bedfile_extention.lower()=='.bed' or bedfile_extention.lower()=='.np' or bedfile_extention.lower()=='.narrowpeak'):
            file_df, max_signal, min_signal=readFileInBEDFormat(BEDFileWithPath)
            file_df_grouped = file_df.groupby(chrom)
            pool = multiprocessing.Pool(numofProcesses)

            poolInputList = []

            for chrLong, chromBasedFileDF in file_df_grouped:
                chromSize = chromSizesDict[chrLong]
                inputList = []
                inputList.append(chrLong)
                inputList.append(chromSize)
                inputList.append(chromBasedFileDF)
                inputList.append(bedfilename)
                inputList.append(occupancy_type)
                inputList.append(max_signal)
                inputList.append(min_signal)
                poolInputList.append(inputList)

            pool.map(writeChrBasedOccupancySignalArraysAtOnceInParallel, poolInputList)

            ################################
            pool.close()
            pool.join()
            ################################

######################################################################



######################################################################
def readAllNucleosomeOccupancyDataAndWriteChrBasedSignalCountArrays(genome, quantileValue, nucleosomeFilename):
    chromSizesDict = getChromSizesDict(genome)

    # Start the pool
    numofProcesses = multiprocessing.cpu_count()
    print('Number of processors:%d' %(numofProcesses))

    print('Before nucleosome occupancy is loaded into memory')
    memory_usage()

    column_names = [chrom, start, end, signal]
    if os.path.exists(nucleosomeFilename):
        nucleosome_df = pd.read_table(nucleosomeFilename, sep="\t", header=None, comment='#', names=column_names, dtype={chrom: str, start: np.int32, end: np.int32, signal: np.float32})

        print('After nucleosome occupancy is loaded into memory')
        memory_usage()

        if (quantileValue<1.0):
            #remove the outliers
            q = nucleosome_df[SIGNAL].quantile(quantileValue)
            print('q:%f' % q)
            print('before %d' % (nucleosome_df.shape[0]))
            nucleosome_df = nucleosome_df[nucleosome_df[SIGNAL] < q]

            print('After nucleosome_df is subset')
            memory_usage()

            nucleosome_df_grouped = nucleosome_df.groupby(chrom)

            pool = multiprocessing.Pool(numofProcesses)

            print('After pool is initialized')
            memory_usage()

            poolInputList = []

            for chrLong, chromBasedNucleosomeDF in nucleosome_df_grouped:
                print('for %s write nucleosome signal and count array' %(chrLong))
                chromSize = chromSizesDict[chrLong]
                inputList = []
                inputList.append(chrLong)
                inputList.append(chromSize)
                inputList.append(chromBasedNucleosomeDF)
                inputList.append(nucleosomeFilename)
                poolInputList.append(inputList)

            pool.map(writeChrBasedOccupancySignalArraysAtOnceInParallel, poolInputList)

            ################################
            pool.close()
            pool.join()
            ################################

            print('After pool is closed and joined')
            memory_usage()

######################################################################



#####################################################################
def plotNucleosomeOccupancySignalCountFiguresInParallelFromTextFiles(inputList):
    chrLong = inputList[0]
    nucleosomeFilenameWoExtension = inputList[1]

    ##############################################################
    signalArrayFilename = '%s_signal_%s.txt' %(chrLong,nucleosomeFilenameWoExtension)
    countArrayFilename = '%s_count_%s.txt' % (chrLong, nucleosomeFilenameWoExtension)

    chrBasedSignalNucleosmeFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,NUCLEOSOME,CHRBASED,signalArrayFilename)
    chrBasedCountNucleosmeFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,NUCLEOSOME,CHRBASED,countArrayFilename)

    #################################################################################################################
    if (os.path.exists(chrBasedSignalNucleosmeFile) and os.path.exists(chrBasedCountNucleosmeFile)):

        signal_array_txt = np.loadtxt(chrBasedSignalNucleosmeFile)
        count_array_txt = np.loadtxt(chrBasedCountNucleosmeFile)

        fig = plt.figure(figsize=(30, 10), facecolor=None)
        plt.style.use('ggplot')

        figureFilename = '%s_NucleosomeOccupancy_Signal_Count_from_text.png' %(chrLong)
        figureFilepath = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB,NUCLEOSOME,CHRBASED,figureFilename)

        # This code makes the background white.
        ax = plt.gca()
        ax.set_facecolor('white')

        # This code puts the edge line
        for edge_i in ['left', 'bottom', 'right', 'top']:
            ax.spines[edge_i].set_edgecolor("black")
            ax.spines[edge_i].set_linewidth(3)


        #All Chrom
        chromSize = signal_array_txt.size
        x = np.arange(0, chromSize, 1)
        signalPlot = plt.plot(x, signal_array_txt, 'black', label='Signal Array', marker='.', zorder=1)
        countPlot = plt.plot(x, count_array_txt, 'red', label='Count Array', marker='.',zorder=1)

        # # Small Portion of Chrom
        # if chrLong == 'chrM':
        #     chromSize = signal_array_txt.size
        #     x = np.arange(0, chromSize, 1)
        #     signalPlot = plt.plot(x, signal_array_txt, 'black', label='Signal Array', linewidth=1,zorder=1)
        #     countPlot = plt.plot(x, count_array_txt, 'red', label='Count Array', linewidth=1,zorder=1)
        # else:
        #     x=np.arange(41100000,41200000,1)
        #     signalPlot = plt.plot(x, signal_array_txt[41100000:41200000], 'black', label='Signal Array', linewidth=1,zorder=1)
        #     countPlot = plt.plot(x, count_array_txt[41100000:41200000], 'red', label='Count Array', linewidth=1,zorder=1)

        print('chr %s' %chrLong)
        print('signal array shape and size')
        print(signal_array_txt.size)
        print(signal_array_txt.shape)
        print('count array shape and size')
        print(count_array_txt.size)
        print(count_array_txt.shape)

        listofLegends = []
        listofLegends.append(signalPlot[0])
        listofLegends.append(countPlot[0])
        plt.legend(loc='upper left', handles=listofLegends, prop={'size': 24}, shadow=False, edgecolor='white',facecolor='white')

        # Put vertical line at x=0
        # plt.axvline(x=0, color='gray', linestyle='--')

        #Put ylim
        plt.ylim((0,10))

        plt.title('For %s' %(chrLong), fontsize=40, fontweight='bold')
        # plt.show()
        fig.savefig(figureFilepath)
        plt.close(fig)
#####################################################################


#####################################################################
def plotNucleosomeOccupancySignalCountFiguresInParallel(inputList):
    chrLong = inputList[0]
    nucleosomeFilenameWoExtension = inputList[1]

    ##############################################################
    signalArrayFilename = '%s_signal_%s.npy' %(chrLong,nucleosomeFilenameWoExtension)
    countArrayFilename = '%s_count_%s.npy' % (chrLong, nucleosomeFilenameWoExtension)

    chrBasedSignalNucleosmeFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,NUCLEOSOME,CHRBASED,signalArrayFilename)
    chrBasedCountNucleosmeFile = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,NUCLEOSOME,CHRBASED,countArrayFilename)

    #################################################################################################################
    if (os.path.exists(chrBasedSignalNucleosmeFile) and os.path.exists(chrBasedCountNucleosmeFile)):

        signal_array_npy = np.load(chrBasedSignalNucleosmeFile)
        count_array_npy = np.load(chrBasedCountNucleosmeFile)

        fig = plt.figure(figsize=(30, 10), facecolor=None)
        plt.style.use('ggplot')

        figureFilename = '%s_NucleosomeOccupancy_Signal_Count_from_npy_scatter_allChr.png' %(chrLong)
        figureFilepath = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB,NUCLEOSOME,CHRBASED,figureFilename)

        # This code makes the background white.
        ax = plt.gca()
        ax.set_facecolor('white')

        # This code puts the edge line
        for edge_i in ['left', 'bottom', 'right', 'top']:
            ax.spines[edge_i].set_edgecolor("black")
            ax.spines[edge_i].set_linewidth(3)

        #All Chrom
        chromSize = signal_array_npy.size
        x = np.arange(0, chromSize, 1)
        plt.scatter(x, signal_array_npy, color='black', label='Signal Array', zorder=1)
        plt.scatter(x, count_array_npy, color='red', label='Count Array',zorder=1)

        # #Small Portion of Chrom
        # if chrLong == 'chrM':
        #     chromSize = signal_array_npy.size
        #     x = np.arange(0, chromSize, 1)
        #     # signalPlot = plt.plot(x, signal_array_npy, 'black', label='Signal Array', linewidth=1,zorder=1)
        #     # countPlot = plt.plot(x, count_array_npy, 'red', label='Count Array', linewidth=1,zorder=1)
        #     signalPlot = plt.scatter(x, signal_array_npy, color='black', label='Signal Array',zorder=1)
        #     countPlot = plt.scatter(x, count_array_npy, color ='red', label='Count Array',zorder=1)
        # else:
        #     x=np.arange(41100000,41200000,1)
        #     # signalPlot = plt.plot(x, signal_array_npy[41100000:41200000], 'black', label='Signal Array', linewidth=1,zorder=1)
        #     # countPlot = plt.plot(x, count_array_npy[41100000:41200000], 'red', label='Count Array', linewidth=1,zorder=1)
        #     signalPlot = plt.scatter(x, signal_array_npy[41100000:41200000], color='black', label='Signal Array',zorder=1)
        #     countPlot = plt.scatter(x, count_array_npy[41100000:41200000], color='red', label='Count Array',zorder=1)

        print('chr %s' %chrLong)
        print('x shape and size')
        print(x.size)
        print(x.shape)

        print('signal array shape and size')
        print(signal_array_npy.size)
        print(signal_array_npy.shape)

        print('count array shape and size')
        print(count_array_npy.size)
        print(count_array_npy.shape)

        # listofLegends = []
        # listofLegends.append(signalPlot[0])
        # listofLegends.append(countPlot[0])
        # plt.legend(loc='upper left', handles=listofLegends, prop={'size': 24}, shadow=False, edgecolor='white',facecolor='white')

        # Put vertical line at x=0
        # plt.axvline(x=0, color='gray', linestyle='--')

        #Put ylim
        plt.ylim((0,10))

        plt.title('For %s' %(chrLong), fontsize=40, fontweight='bold')
        # plt.show()
        fig.savefig(figureFilepath)
        plt.close(fig)
    #################################################################################################################



#####################################################################

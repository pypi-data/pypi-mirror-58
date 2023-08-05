# This source code file is a part of SigProfilerTopography
# SigProfilerTopography is a tool included as part of the SigProfiler
# computational framework for comprehensive analysis of mutational
# signatures from next-generation sequencing of cancer genomes.
# SigProfilerTopography provides the downstream data analysis of
# mutations and extracted mutational signatures w.r.t.
# nucleosome occupancy, replication time, strand bias and processivity.
# Copyright (C) 2018 Burcak Otlu

#############################################################
# This python code generates normalized mutation density data for different analyses types which are
# Using all mutations (all chromosomes, all samples, signatures) which leads to Aggregated Substitutions
# Using all mutations but in signature based manner leads to Signature Based
# Using all mutations in signature based and sample based manner leads to Signature based and Sample Based
# Using all indels (all chromosomes, all samples) which leads to Aggregated Indels
# Using all indels (diving indels of length >=3 as microhomology-mediated indels and indels of length <3 as repeat-mediated  indels)

## In this python code
## I read the wavelet-transformed signal wig across whole genome
## Sort the signal in descending order
## Divide the data into 10 equal deciles
## Return 10 deciles as data frames
## Read the mutation file
## Group by mutation file by chromosome
## Group by decile file by chromosome
## For each chromosome (Done in the loop sequentially)
## Make a list of input
## chromosome based mutation file mutation file
## chromosome based decile files coming from 10 different deciles (Done in parallel for all of the 10 deciles)
## In the function I will generate interval tree from decile file
## Overlap the mutations with the interval tree
## Return the total number of mutations that overlap between mutation file and decile file
## Get chromosome based mutation file
## Get chromosome based decile file
## Accumulate the total number of mutations that overlap for each decile file
#############################################################

#############################################################
# Constraints, Thresholds
# Please note that for sample based and signature based replication time analysis
# We consider samples with at least 3000 mutations at total in all deciles.
#############################################################

import multiprocessing
import sys
import twobitreader
import os
import math
import numpy as np
import pandas as pd

from SigProfilerTopography.source.commons.TopographyCommons import current_abs_path
from SigProfilerTopography.source.commons.TopographyCommons import ONE_DIRECTORY_UP
from SigProfilerTopography.source.commons.TopographyCommons import LIB
from SigProfilerTopography.source.commons.TopographyCommons import REPLICATION
from SigProfilerTopography.source.commons.TopographyCommons import UCSCGENOME

from SigProfilerTopography.source.commons.TopographyCommons import DATA
from SigProfilerTopography.source.commons.TopographyCommons import REPLICATIONTIME
from SigProfilerTopography.source.commons.TopographyCommons import SAMPLES
from SigProfilerTopography.source.commons.TopographyCommons import SIGNATUREBASED

from SigProfilerTopography.source.commons.TopographyCommons import NUMOFBASES

from SigProfilerTopography.source.commons.TopographyCommons import CHROM
from SigProfilerTopography.source.commons.TopographyCommons import START
from SigProfilerTopography.source.commons.TopographyCommons import END
from SigProfilerTopography.source.commons.TopographyCommons import SIGNAL

from SigProfilerTopography.source.commons.TopographyCommons import SAMPLE
from SigProfilerTopography.source.commons.TopographyCommons import LENGTH
from SigProfilerTopography.source.commons.TopographyCommons import SIMULATION_NUMBER

from SigProfilerTopography.source.commons.TopographyCommons import SUBS
from SigProfilerTopography.source.commons.TopographyCommons import INDELS
from SigProfilerTopography.source.commons.TopographyCommons import DINUCS

from SigProfilerTopography.source.commons.TopographyCommons import AGGREGATEDSUBSTITUTIONS
from SigProfilerTopography.source.commons.TopographyCommons import AGGREGATEDINDELS
from SigProfilerTopography.source.commons.TopographyCommons import AGGREGATEDDINUCS

from SigProfilerTopography.source.commons.TopographyCommons import MICROHOMOLOGY
from SigProfilerTopography.source.commons.TopographyCommons import REPEAT

from SigProfilerTopography.source.commons.TopographyCommons import readWaveletSmoothedSignalReplicationTime
from SigProfilerTopography.source.commons.TopographyCommons import memory_usage
from SigProfilerTopography.source.commons.TopographyCommons import readChrBasedMutationsDF
from SigProfilerTopography.source.commons.TopographyCommons import getCombinedChrBasedDF

from SigProfilerTopography.source.commons.TopographyCommons import COMPUTATION_ALL_CHROMOSOMES_PARALLEL
from SigProfilerTopography.source.commons.TopographyCommons import COMPUTATION_CHROMOSOMES_SEQUENTIAL_ALL_SIMULATIONS_PARALLEL
from SigProfilerTopography.source.commons.TopographyCommons import COMPUTATION_CHROMOSOMES_SEQUENTIAL_SIMULATIONS_SEQUENTIAL
from SigProfilerTopography.source.commons.TopographyCommons import COMPUTATION_CHROMOSOMES_SEQUENTIAL_CHROMOSOME_SPLITS_PARALLEL
from SigProfilerTopography.source.commons.TopographyCommons import USING_APPLY_ASYNC
from SigProfilerTopography.source.commons.TopographyCommons import USING_IMAP_UNORDERED

from SigProfilerTopography.source.commons.TopographyCommons import GRCh37
from SigProfilerTopography.source.commons.TopographyCommons import GRCh38
from SigProfilerTopography.source.commons.TopographyCommons import HG19_2BIT
from SigProfilerTopography.source.commons.TopographyCommons import HG38_2BIT


from SigProfilerTopography.source.commons.TopographyCommons import Sample2NumberofDinucsDictFilename
from SigProfilerTopography.source.commons.TopographyCommons import Sample2DinucsSignature2NumberofMutationsDictFilename

from SigProfilerTopography.source.commons.TopographyCommons import getDictionary
from SigProfilerTopography.source.commons.TopographyCommons import getSample2NumberofSubsDict
from SigProfilerTopography.source.commons.TopographyCommons import getSample2NumberofIndelsDict

from SigProfilerTopography.source.commons.TopographyCommons import getSample2SubsSignature2NumberofMutationsDict
from SigProfilerTopography.source.commons.TopographyCommons import getSample2IndelsSignature2NumberofMutationsDict


##################################################################
def fillReplicationTimeNPArrays(inputList):
    chrLong = inputList[0]
    chromSize = inputList[1]
    decile_df_list = inputList[2]
    replicationTimeFilename_wo_extension = inputList[3]

    chrBasedReplicationTimeDataNPArray = fillChrBasedReplicationTimeNPArrayNewVersion(chrLong, chromSize,decile_df_list)
    replicationTimeArrayFilename = '%s_%s' % (chrLong, replicationTimeFilename_wo_extension)
    chrBasedReplicationTimeFile = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB, REPLICATION,replicationTimeFilename_wo_extension, replicationTimeArrayFilename)
    np.save(chrBasedReplicationTimeFile, chrBasedReplicationTimeDataNPArray)
##################################################################


# ##################################################################
# def writeNumberofAttributableBases(decile_df_list,replicationTimeFilename_wo_extension):
#     decileIndex2NumberofAttributableBasesDict = {}
#     for i,decile_df in enumerate(decile_df_list,1):
#         numofAttBases = decile_df[NUMOFBASES].sum()
#         decileIndex2NumberofAttributableBasesDict[i] = numofAttBases
#
#     filepath = os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,REPLICATION,replicationTimeFilename_wo_extension,DecileIndex2NumfAttributableBasesDictFilename)
#     writeDictionaryUsingPickle(decileIndex2NumberofAttributableBasesDict,filepath)
# ##################################################################


##################################################################
def generateIntervalVersion(replication_time_wavelet_signal_unprocessed_df):
    #Read the file and generate chr start end signal wavelet_smoothed_signal
    columns = [CHROM,START,END,SIGNAL]

    #Create an empty dataframe
    replication_time_wavelet_signal_interval_version_df = pd.DataFrame(columns=columns)

    #dummy initialization
    i = 0
    chrom = 'chr1'
    start = 0
    step = 1000

    rows_list = []

    # e.g. rows
    # fixedStep chrom=chr1 start=24500 step=1000 span=1000
    # 57.4679
    # 57.467
    # 57.4651
    # 57.4623
    # 57.4586
    # 57.454
    # 57.4484
    # 57.442
    # 57.4347
    # 57.4266
    # 57.4176

    for row in replication_time_wavelet_signal_unprocessed_df.itertuples(index=True, name='Pandas'):
        # row's type is <class 'pandas.core.frame.Pandas'>
        # row[0] is the index
        # row[1] is fixedStep chrom=chr1 start=24500 step=1000 span=1000 or 57.4679
        if (row[1].startswith('fixedStep')):
            #This is the information line
            chrom = row[1].split()[1].split('=')[1]
            start = int(row[1].split()[2].split('=')[1])
            step = int(row[1].split()[3].split('=')[1])
        else:
            signal = float(row[1])
            chr = chrom
            start = start
            end = start + step-1
            dict = {CHROM:chr, START:start, END:end, SIGNAL:signal}
            rows_list.append(dict)
            start += step

    # print('Number of intervals to be inserted in wavelet_processed_df: %d' %len(rows_list))
    #rows_list contain the list of row where each row is a dictionary

    replication_time_wavelet_signal_interval_version_df = pd.DataFrame(rows_list, columns=[CHROM,START,END,SIGNAL])

    # print('replication_time_wavelet_signal_interval_version_df.dtypes')
    # print(replication_time_wavelet_signal_interval_version_df.dtypes)

    replication_time_wavelet_signal_interval_version_df[CHROM] = replication_time_wavelet_signal_interval_version_df[CHROM].astype(str)
    replication_time_wavelet_signal_interval_version_df[START] = replication_time_wavelet_signal_interval_version_df[START].astype(np.int32)
    replication_time_wavelet_signal_interval_version_df[END] = replication_time_wavelet_signal_interval_version_df[END].astype(np.int32)
    replication_time_wavelet_signal_interval_version_df[SIGNAL] = replication_time_wavelet_signal_interval_version_df[SIGNAL].astype(np.float32)

    # print('replication_time_wavelet_signal_interval_version_df.dtypes')
    # print(replication_time_wavelet_signal_interval_version_df.dtypes)

    return replication_time_wavelet_signal_interval_version_df
##################################################################


##################################################################
def readRepliSeqTimeData(genome,repliseqDataFilename):

    ###################################################################
    ############### Read RepliSeq Time data starts ####################
    ###################################################################

    ################################
    numofProcesses = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(numofProcesses)
    ################################

    #Read the wavelet signal
    replication_time_wavelet_signal_unprocessed_df = readWaveletSmoothedSignalReplicationTime(repliseqDataFilename)

    #Process the wavelet signal, convert into interval version
    # here column names are added
    replication_time_interval_version_df = generateIntervalVersion(replication_time_wavelet_signal_unprocessed_df)

    chrNamesInReplicationTimeDataArray = replication_time_interval_version_df[CHROM].unique()
    print('Chromosome names in replication time signal data: %s' %(chrNamesInReplicationTimeDataArray))

    #Augment wavelet_processed_df with numberofAttributableBases
    wavelet_processed_augmented_df = augment(genome,pool,replication_time_interval_version_df)

    #Return 10 deciles: the first decile is the earliest one and the tenth decile is the latest one

    #Sort in descending order
    #Higher the replication time signal earlier the replication is
    wavelet_processed_augmented_df.sort_values(SIGNAL, ascending=False, inplace=True)

    # print('############ after sort wavelet_processed_augmented_df ###################')
    # print(wavelet_processed_augmented_df.head())
    # print('############ after sort wavelet_processed_augmented_df ###################')

    #Split wavelet_processed_augmented_df into 10 deciles
    deciles_df_list = np.array_split(wavelet_processed_augmented_df,10)
    # print('Number of decile:%d' %len(deciles))
    #deciles is a list and each decile is a dataframe <class 'pandas.core.frame.DataFrame'>
    #The first decile is the earliest one
    #The last decile is the latest one
    # print('type(deciles_df_list):%s' %type(deciles_df_list))
    # type(deciles_df_list) --> <class 'list'>

    # ############################################################
    # #For information
    # totalNumberofIntervals = 0
    # for decileIndex, decile_df in enumerate(deciles_df_list,1):
    #     # print('decileIndex: %d' %decileIndex)
    #     # print('type(decile_df)')
    #     # print(type(decile_df))
    #     # type(decile_df) --> <class 'pandas.core.frame.DataFrame'>
    #     totalNumberofIntervals += len(decile_df)
    # print('totalNumberofIntervals in all deciles : %d' %totalNumberofIntervals)
    # ############################################################

    ################################
    pool.close()
    pool.join()
    ################################

    return chrNamesInReplicationTimeDataArray, deciles_df_list
    ###################################################################
    ############### Read RepliSeq Time data ends ######################
    ###################################################################

##################################################################



##################################################################
def getNumberofAttributableBases(wavelet_row, chrBasedGenome):
    start =wavelet_row[1]
    end = wavelet_row[2]
    #In my code ends are inclusive
    #twobitreader uses ends exlusive
    seq = chrBasedGenome.get_slice(start, end+1)
    numofAttributableBases = seq.count('A') + seq.count('T') + seq.count('G') + seq.count('C') + seq.count('a') + seq.count('t') + seq.count('g') + seq.count('c')
    # print('######### debug starts ##############')
    # print(wavelet_row)
    # print('len(seq):%d' %len(seq))
    # print('numofAttributableBases:%d' %numofAttributableBases)
    # print('##########  debug ends #############')
    return numofAttributableBases
##################################################################

##################################################################
def addNumofAttributableBasesColumn(inputList):
    chrLong = inputList[0]
    chrBased_wavelet_processed_df_group =inputList[1]
    wholeGenome = inputList[2]
    resulting_df = chrBased_wavelet_processed_df_group.apply(getNumberofAttributableBases, chrBasedGenome = wholeGenome[chrLong], axis= 1)

    # print('######## debug numberofAttributableBases starts ########')
    # print('for %s starts' %chrLong)
    # print('len(chrBased_wavelet_processed_df_group): %d ' %len(chrBased_wavelet_processed_df_group))
    # print('len(resulting_df): %d' %len(resulting_df))
    # print('type(chrBased_wavelet_processed_df_group): %s' % type(chrBased_wavelet_processed_df_group))
    # print('type(resulting_df): %s' %type(resulting_df))

    if (len(chrBased_wavelet_processed_df_group)!=len(resulting_df)):
        print('There is a situation: len(chrBased_wavelet_processed_df_group) is not equal  to len(resulting_df)')

    # print('debug starts')
    # print(resulting_df)
    # print(chrBased_wavelet_processed_df_group.columns.values.tolist())
    # print('debug ends')

    #Add the resulting_df as a new column to chrBased_wavelet_processed_df_group
    chrBased_wavelet_processed_df_group[NUMOFBASES] = resulting_df

    # print('debug starts')
    # print(chrBased_wavelet_processed_df_group.columns.values.tolist())
    # print('debug ends')

    # print('for %s ends' % chrLong)
    # print('######## debug numberofAttributableBases ends ########')

    return (chrLong,chrBased_wavelet_processed_df_group)
##################################################################

##################################################################
#DEC 8, 2019
def searchMutation_simulations_integrated_using_list_comprehension(mutation_row,
                                                   sample2NumberofMutationsDict,
                                                   sample2Signature2NumberofMutationsDict,
                                                   chrBasedReplicationTimeDataArrayWithDecileIndex,
                                                   type2DecileIndex2NumberofMutationsDict,
                                                   sample2Type2DecileIndex2NumberofMutationsDict,
                                                   signature2PropertiesListDict,
                                                   type,
                                                   sample_based,
                                                   df_columns):

    # For single point mutations start and end are the same, therefore we need to add 1 to mutation_row[END]
    indexofSample = df_columns.index(SAMPLE)
    sample = mutation_row[indexofSample]

    indexofStart = df_columns.index(START)
    start=mutation_row[indexofStart]

    if (type==AGGREGATEDINDELS):
        indexofLength = df_columns.index(LENGTH)
        length=mutation_row[indexofLength]

    #end is exclusive for subs, indels and dincuc provided by readChrBased methods
    # start= mutation_row[START]

    if (type==AGGREGATEDINDELS):
        # end = start + mutation_row[LENGTH]
        end = start + length
    elif (type==AGGREGATEDSUBSTITUTIONS):
        end = start + 1
    elif (type==AGGREGATEDDINUCS):
        end = start + 2

    slicedArray = chrBasedReplicationTimeDataArrayWithDecileIndex[start:end]

    # np.nonzero returns the indices of the elements that are non-zero.
    # np.unique finds the unique elements of an array returns ndarray the sorted unique values.
    # np.nditer efficient multi-dimensional iterator object to iterate over arrays.
    uniqueIndexesArray = np.unique(slicedArray[np.nonzero(slicedArray)])

    if (uniqueIndexesArray.size>0):
        for decileIndex in np.nditer(uniqueIndexesArray):
            # type(decileIndex) is numpy.ndarray
            decileIndexNum = int(decileIndex)

            ################### AGGREGATED starts #####################
            if type in type2DecileIndex2NumberofMutationsDict:
                if decileIndexNum in type2DecileIndex2NumberofMutationsDict[type]:
                    type2DecileIndex2NumberofMutationsDict[type][decileIndexNum] += 1
                else:
                    type2DecileIndex2NumberofMutationsDict[type][decileIndexNum] = 1
            else:
                type2DecileIndex2NumberofMutationsDict[type]={}
                type2DecileIndex2NumberofMutationsDict[type][decileIndexNum] = 1

            if (type==AGGREGATEDINDELS):
                if length >= 3:
                    if MICROHOMOLOGY in type2DecileIndex2NumberofMutationsDict:
                        if decileIndexNum in type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY]:
                            type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY][decileIndexNum] += 1
                        else:
                            type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY][decileIndexNum] = 1
                    else:
                        type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY] = {}
                        type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY][decileIndexNum] = 1

                else:
                    if REPEAT in type2DecileIndex2NumberofMutationsDict:
                        if decileIndexNum in type2DecileIndex2NumberofMutationsDict[REPEAT]:
                            type2DecileIndex2NumberofMutationsDict[REPEAT][decileIndexNum] += 1
                        else:
                            type2DecileIndex2NumberofMutationsDict[REPEAT][decileIndexNum] = 1
                    else:
                        type2DecileIndex2NumberofMutationsDict[REPEAT] = {}
                        type2DecileIndex2NumberofMutationsDict[REPEAT][decileIndexNum] = 1
            ################### AGGREGATED ends #######################

            ########################### Signatures start ###########################
            for signature in signature2PropertiesListDict:
                indexofSignature=df_columns.index(signature)
                if mutation_row[indexofSignature] >= float(signature2PropertiesListDict[signature][0]):
                    if signature in type2DecileIndex2NumberofMutationsDict:
                        if decileIndexNum in type2DecileIndex2NumberofMutationsDict[signature]:
                            type2DecileIndex2NumberofMutationsDict[signature][decileIndexNum] += 1
                        else:
                            type2DecileIndex2NumberofMutationsDict[signature][decileIndexNum] = 1
                    else:
                        type2DecileIndex2NumberofMutationsDict[signature] = {}
                        type2DecileIndex2NumberofMutationsDict[signature][decileIndexNum] = 1
            ########################### Signatures end #############################

            ############################# Sample Based starts ###########################
            if sample_based:

                if sample in sample2NumberofMutationsDict:
                    ############## Sample Based Aggregated Substitutions starts ############
                    if sample in sample2Type2DecileIndex2NumberofMutationsDict:
                        if type in sample2Type2DecileIndex2NumberofMutationsDict[sample]:

                            if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][type]:
                                sample2Type2DecileIndex2NumberofMutationsDict[sample][type][decileIndexNum] += 1
                            else:
                                sample2Type2DecileIndex2NumberofMutationsDict[sample][type][decileIndexNum] = 1

                            if (type==AGGREGATEDINDELS):
                                if length >= 3:
                                    if MICROHOMOLOGY in sample2Type2DecileIndex2NumberofMutationsDict[sample]:
                                        if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY]:
                                            sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] += 1
                                        else:
                                            sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] = 1
                                    else:
                                        sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY] = {}
                                        sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] = 1


                                else:
                                    if REPEAT in sample2Type2DecileIndex2NumberofMutationsDict[sample]:
                                        if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT]:
                                            sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] += 1
                                        else:
                                            sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] = 1
                                    else:
                                        sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT] = {}
                                        sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] = 1

                        else:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][type] = {}
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][type][decileIndexNum] = 1
                            if type == AGGREGATEDINDELS:
                                if length >= 3:
                                    sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY] = {}
                                    sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] = 1
                                else:
                                    sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT] = {}
                                    sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] = 1

                    else:
                        sample2Type2DecileIndex2NumberofMutationsDict[sample]={}
                        sample2Type2DecileIndex2NumberofMutationsDict[sample][type]={}
                        sample2Type2DecileIndex2NumberofMutationsDict[sample][type][decileIndexNum] = 1
                        if type==AGGREGATEDINDELS:
                            if length >= 3:
                                sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY] = {}
                                sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] = 1
                            else:
                                sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT] = {}
                                sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] = 1

                ############## Sample Based Aggregated Substitutions ends ##############

            if sample in sample2Signature2NumberofMutationsDict:
                for signature in sample2Signature2NumberofMutationsDict[sample]:
                    indexofSignature = df_columns.index(signature)
                    if mutation_row[indexofSignature] >= float(signature2PropertiesListDict[signature][0]):
                        if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][signature]:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][signature][decileIndexNum] += 1
                        else:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][signature][decileIndexNum] = 1
                ############## Sample Based Signatures ends ############################

            ############################# Sample Based ends ############################

##################################################################


##################################################################
#Simulations
def searchMutation_simulations_integrated(mutation_row,
    sample2NumberofMutationsDict,
    sample2Signature2NumberofMutationsDict,
    chrBasedReplicationTimeDataArrayWithDecileIndex,
    simNum2Type2DecileIndex2NumberofMutationsDict,
    simNum2Sample2Type2DecileIndex2NumberofMutationsDict,
    signature2PropertiesListDict,
    type):

    # For single point mutations start and end are the same, therefore we need to add 1 to mutation_row[END]

    #end is exclusive for subs, indels and dincuc provided by readChrBased methods
    start= mutation_row[START]

    if (type==AGGREGATEDINDELS):
        end = start + mutation_row[LENGTH]
    elif (type==AGGREGATEDSUBSTITUTIONS):
        end = start + 1
    elif (type==AGGREGATEDDINUCS):
        end = start + 2

    slicedArray = chrBasedReplicationTimeDataArrayWithDecileIndex[start:end]

    #get the samplename
    sample = mutation_row[SAMPLE]
    simNum = mutation_row[SIMULATION_NUMBER]

    # np.nonzero returns the indices of the elements that are non-zero.
    # np.unique finds the unique elements of an array returns ndarray the sorted unique values.
    # np.nditer efficient multi-dimensional iterator object to iterate over arrays.
    uniqueIndexesArray = np.unique(slicedArray[np.nonzero(slicedArray)])

    if (uniqueIndexesArray.size>0):
        for decileIndex in np.nditer(uniqueIndexesArray):
            # type(decileIndex) is numpy.ndarray
            decileIndexNum = int(decileIndex)

            ##############################################################
            type2DecileIndex2NumberofMutationsDict = simNum2Type2DecileIndex2NumberofMutationsDict[simNum]
            sample2Type2DecileIndex2NumberofMutationsDict = simNum2Sample2Type2DecileIndex2NumberofMutationsDict[simNum]
            ##############################################################

            ################### AGGREGATED starts #####################
            if decileIndexNum in type2DecileIndex2NumberofMutationsDict[type]:
                type2DecileIndex2NumberofMutationsDict[type][decileIndexNum] += 1
            else:
                type2DecileIndex2NumberofMutationsDict[type][decileIndexNum] = 1

            if (type==AGGREGATEDINDELS):
                if mutation_row[LENGTH] >= 3:
                    if decileIndexNum in type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY]:
                        type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY][decileIndexNum] += 1
                    else:
                        type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY][decileIndexNum] = 1
                else:
                    if decileIndexNum in type2DecileIndex2NumberofMutationsDict[REPEAT]:
                        type2DecileIndex2NumberofMutationsDict[REPEAT][decileIndexNum] += 1
                    else:
                        type2DecileIndex2NumberofMutationsDict[REPEAT][decileIndexNum] = 1
            ################### AGGREGATED ends #######################

            ########################### Signatures start ###########################
            for signature in signature2PropertiesListDict:
                if mutation_row[signature] >= float(signature2PropertiesListDict[signature][0]):
                    if decileIndexNum in type2DecileIndex2NumberofMutationsDict[signature]:
                        type2DecileIndex2NumberofMutationsDict[signature][decileIndexNum] += 1
                    else:
                        type2DecileIndex2NumberofMutationsDict[signature][decileIndexNum] = 1
            ########################### Signatures end #############################

            ############################# Sample Based starts ###########################
            if sample in sample2NumberofMutationsDict:
                ############## Sample Based Aggregated Substitutions starts ############
                if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][type]:
                    sample2Type2DecileIndex2NumberofMutationsDict[sample][type][decileIndexNum] += 1
                else:
                    sample2Type2DecileIndex2NumberofMutationsDict[sample][type][decileIndexNum] = 1

                if (type==AGGREGATEDINDELS):
                    if mutation_row[LENGTH] >= 3:
                        if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY]:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] += 1
                        else:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY][decileIndexNum] = 1

                    else:
                        if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT]:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] += 1
                        else:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT][decileIndexNum] = 1
                ############## Sample Based Aggregated Substitutions ends ##############

            if sample in sample2Signature2NumberofMutationsDict:
                for signature in sample2Signature2NumberofMutationsDict[sample]:
                    if mutation_row[signature] >= float(signature2PropertiesListDict[signature][0]):
                        if decileIndexNum in sample2Type2DecileIndex2NumberofMutationsDict[sample][signature]:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][signature][decileIndexNum] += 1
                        else:
                            sample2Type2DecileIndex2NumberofMutationsDict[sample][signature][decileIndexNum] = 1
                ############## Sample Based Signatures ends ############################

            ############################# Sample Based ends ############################

##################################################################


##################################################################
#Dec 8, 2019
#There is a new version to be used by imap_unordered and apply_sync
#Where there is no need for initialization
#This will be called by fillDictionaries
def searchforMutations_NoInitialization(sample2NumberofMutationsDict,
        sample2Signature2NumberofMutationsDict,
        chrBased_simBased_mutations_df,
        chrBasedReplicationTimeDataArrayWithDecileIndex,
        signature2PropertiesListDict,
        type,
        sample_based):

    ######################################################################
    type2DecileIndex2NumberofMutationsDict = {}
    sample2Type2DecileIndex2NumberofMutationsDict = {}

    size_in_mbs = sys.getsizeof(chrBased_simBased_mutations_df) / 1048576
    max_size_in_mbs = 50
    if (size_in_mbs > max_size_in_mbs):
        numberofSplits = math.ceil(size_in_mbs / max_size_in_mbs)

        list_of_dfs = np.array_split(chrBased_simBased_mutations_df, numberofSplits)
        if list_of_dfs is not None:
            for part_index, part_df in enumerate(list_of_dfs, 1):
                df_columns = list(part_df.columns.values)
                [searchMutation_simulations_integrated_using_list_comprehension(mutation_row,
                                                       sample2NumberofMutationsDict,
                                                       sample2Signature2NumberofMutationsDict,
                                                       chrBasedReplicationTimeDataArrayWithDecileIndex,
                                                       type2DecileIndex2NumberofMutationsDict,
                                                       sample2Type2DecileIndex2NumberofMutationsDict,
                                                       signature2PropertiesListDict,
                                                       type,
                                                       sample_based,
                                                       df_columns) for mutation_row in part_df.values]
    else:
        df_columns=list(chrBased_simBased_mutations_df.columns.values)
        [searchMutation_simulations_integrated_using_list_comprehension(mutation_row,
                                                                        sample2NumberofMutationsDict,
                                                                        sample2Signature2NumberofMutationsDict,
                                                                        chrBasedReplicationTimeDataArrayWithDecileIndex,
                                                                        type2DecileIndex2NumberofMutationsDict,
                                                                        sample2Type2DecileIndex2NumberofMutationsDict,
                                                                        signature2PropertiesListDict,
                                                                        type,
                                                                        sample_based,
                                                                        df_columns) for mutation_row in chrBased_simBased_mutations_df.values]


    return type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict

##################################################################


##################################################################
def searchforMutations(sample2NumberofMutationsDict,
        sample2Signature2NumberofMutationsDict,
        chrBased_simBased_mutations_df,
        chrBasedReplicationTimeDataArrayWithDecileIndex,
        signature2PropertiesListDict,
        type,
        numofSimulations):

    ######################################################################
    simNum2Type2DecileIndex2NumberofMutationsDict = {}
    simNum2Sample2Type2DecileIndex2NumberofMutationsDict = {}

    for simNum in range(0,numofSimulations+1):
        simNum2Type2DecileIndex2NumberofMutationsDict[simNum]={}
        simNum2Sample2Type2DecileIndex2NumberofMutationsDict[simNum]={}

        ############################################################
        # We will fill type2DecileIndex2NumberofMutationsDict for AGGREGATEDSUBSTITUTIONS and for each signature and return it
        type2DecileIndex2NumberofMutationsDict= simNum2Type2DecileIndex2NumberofMutationsDict[simNum]

        # Initialize for AGGREGATEDSUBSTITUTIONS and subs signatures
        # type2DecileIndex2NumberofMutationsDict[AGGREGATEDSUBSTITUTIONS] = {}
        type2DecileIndex2NumberofMutationsDict[type] = {}
        if (type==AGGREGATEDINDELS):
            type2DecileIndex2NumberofMutationsDict[MICROHOMOLOGY] = {}
            type2DecileIndex2NumberofMutationsDict[REPEAT] = {}

        for signature in signature2PropertiesListDict:
            type2DecileIndex2NumberofMutationsDict[signature] = {}
        ############################################################

        ############################################################
        #Initialize sample2Type2DecileIndex2NumberofMutationsDict
        sample2Type2DecileIndex2NumberofMutationsDict = simNum2Sample2Type2DecileIndex2NumberofMutationsDict[simNum]

        for sample in  sample2NumberofMutationsDict:
            sample2Type2DecileIndex2NumberofMutationsDict[sample] = {}
            sample2Type2DecileIndex2NumberofMutationsDict[sample][type] = {}
            if (type == AGGREGATEDINDELS):
                sample2Type2DecileIndex2NumberofMutationsDict[sample][MICROHOMOLOGY] = {}
                sample2Type2DecileIndex2NumberofMutationsDict[sample][REPEAT] = {}

        for sample in sample2Signature2NumberofMutationsDict:
            for signature in sample2Signature2NumberofMutationsDict[sample]:
                sample2Type2DecileIndex2NumberofMutationsDict[sample][signature] = {}
        ############################################################
    ######################################################################

    size_in_mbs = sys.getsizeof(chrBased_simBased_mutations_df) / 1048576
    max_size_in_mbs = 50
    if (size_in_mbs > max_size_in_mbs):
        numberofSplits = math.ceil(size_in_mbs / max_size_in_mbs)

        list_of_dfs = np.array_split(chrBased_simBased_mutations_df, numberofSplits)

        if list_of_dfs is not None:
            for part_index, part_df in enumerate(list_of_dfs, 1):
                part_df.apply(searchMutation_simulations_integrated,
                                            sample2NumberofMutationsDict = sample2NumberofMutationsDict,
                                            sample2Signature2NumberofMutationsDict= sample2Signature2NumberofMutationsDict,
                                            chrBasedReplicationTimeDataArrayWithDecileIndex= chrBasedReplicationTimeDataArrayWithDecileIndex,
                                            simNum2Type2DecileIndex2NumberofMutationsDict=simNum2Type2DecileIndex2NumberofMutationsDict,
                                            simNum2Sample2Type2DecileIndex2NumberofMutationsDict=simNum2Sample2Type2DecileIndex2NumberofMutationsDict,
                                            signature2PropertiesListDict = signature2PropertiesListDict,
                                            type= type,
                                            axis=1)
    else:
        chrBased_simBased_mutations_df.apply(searchMutation_simulations_integrated,
                      sample2NumberofMutationsDict=sample2NumberofMutationsDict,
                      sample2Signature2NumberofMutationsDict=sample2Signature2NumberofMutationsDict,
                      chrBasedReplicationTimeDataArrayWithDecileIndex=chrBasedReplicationTimeDataArrayWithDecileIndex,
                      simNum2Type2DecileIndex2NumberofMutationsDict=simNum2Type2DecileIndex2NumberofMutationsDict,
                      simNum2Sample2Type2DecileIndex2NumberofMutationsDict=simNum2Sample2Type2DecileIndex2NumberofMutationsDict,
                      signature2PropertiesListDict=signature2PropertiesListDict,
                      type=type,
                      axis=1)

    return simNum2Type2DecileIndex2NumberofMutationsDict, simNum2Sample2Type2DecileIndex2NumberofMutationsDict
##################################################################

##################################################################
#Please notice that replication time data are not overlappig data therefore only setting one decileIndex will be correct.
# e.g.:
# start end
#   10 1009
# 1010 2009
def fillArray(chrBased_replicationtimedata_row,chrBasedDecileIndexArray,decileIndex):
    start= chrBased_replicationtimedata_row[START]
    end = chrBased_replicationtimedata_row[END] + 1
    chrBasedDecileIndexArray[start:end] = decileIndex
##################################################################


##################################################################
def  fillChrBasedReplicationTimeNPArrayNewVersion(chrLong,chromSize,decile_df_list):
    # int8	Byte (-128 to 127)
    chrBasedReplicationTimeDataArrayWithDecileIndex = np.zeros(chromSize, dtype=np.int8)

    #First decileIndex is 1, last decile index is 10.
    for decileIndex, decile_df in enumerate(decile_df_list,1):
        chrBased_grouped_decile_df = decile_df.groupby(CHROM)
        # print('debug: len(chrBased_grouped_decile_df): %d' %len(chrBased_grouped_decile_df))
        if chrLong in chrBased_grouped_decile_df.groups.keys():
            chrBased_replicationtimedata_df = chrBased_grouped_decile_df.get_group(chrLong)
            #what is chrBased_decile's type? DataFrame
            if ((chrBased_replicationtimedata_df is not None) and (not chrBased_replicationtimedata_df.empty)):
                chrBased_replicationtimedata_df.apply(fillArray,chrBasedDecileIndexArray=chrBasedReplicationTimeDataArrayWithDecileIndex,decileIndex=decileIndex, axis=1)

    return chrBasedReplicationTimeDataArrayWithDecileIndex
##################################################################


##################################################################
#What am i doing in this function?
#This function is called for each chromosome
#For each chromosome, a numpy array is filled.
#If there is a chromosome locus with a decile index 8 let's say, in the array that locus is filled with 8.
#Decile index can be 1-10.
#In this function, each available interval with an index is filled in the corresponding numpy array
def  fillChrBasedReplicationTimeNPArray(chrLong,chromSize,chrBased_grouped_decile_df_list):
    #We can set the starting index as 1 in builtin function enumerate
    #First chrBased_grouped_decile has index of 1
    #Last chrBased_grouped_decile has index of 10

    # int8	Byte (-128 to 127)
    chrBasedReplicationTimeDataArrayWithDecileIndex = np.zeros(chromSize, dtype=np.int8)

    #First decileIndex is 1, last decile index is 10.
    for decileIndex, chrBased_grouped_decile_df in enumerate(chrBased_grouped_decile_df_list,1):
        if chrLong in chrBased_grouped_decile_df.groups.keys():
            chrBased_replicationtimedata_df = chrBased_grouped_decile_df.get_group(chrLong)
            #what is chrBased_decile's type? DataFrame
            if ((chrBased_replicationtimedata_df is not None) and (not chrBased_replicationtimedata_df.empty)):
                chrBased_replicationtimedata_df.apply(fillArray,chrBasedDecileIndexArray=chrBasedReplicationTimeDataArrayWithDecileIndex,decileIndex=decileIndex, axis=1)

    return chrBasedReplicationTimeDataArrayWithDecileIndex
##################################################################


##################################################################
#Dec 8, 2019
#For pool.apply_sync and pool.imap_unordered
def fillDictionaries_chromBased_simBased(sample2NumberofSubsDict,
                    sample2NumberofIndelsDict,
                    sample2NumberofDinucsDict,
                    sample2SubsSignature2NumberofMutationsDict,
                    sample2IndelsSignature2NumberofMutationsDict,
                    sample2DinucsSignature2NumberofMutationsDict,
                    chrBasedReplicationTimeDataArrayWithDecileIndex,
                    chrBased_simBased_subs_df,
                    chrBased_simBased_indels_df,
                    chrBased_simBased_dinucs_df,
                    sample_based,
                    simNum,
                    chrLong,
                    subsSignature2PropertiesListDict,
                    indelsSignature2PropertiesListDict,
                    dinucsSignature2PropertiesListDict,
                    verbose):

    type2DecileIndex2AccumulatedNumberofMutationsDict = {}
    sample2Type2DecileIndex2AccumulatedNumberofMutationsDict = {}

    ##################################################################################################################
    if ((chrBased_simBased_subs_df is not None) and (not chrBased_simBased_subs_df.empty)):
        if verbose: print('Worker %s STEP2.1 Search for Mutations SUBS STARTS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))
        subsType2DecileIndex2NumberofMutationsDict, sample2SubsType2DecileIndex2NumberofMutationsDict = searchforMutations_NoInitialization(
            sample2NumberofSubsDict,
            sample2SubsSignature2NumberofMutationsDict,
            chrBased_simBased_subs_df,
            chrBasedReplicationTimeDataArrayWithDecileIndex,
            subsSignature2PropertiesListDict,
            AGGREGATEDSUBSTITUTIONS,
            sample_based)
        if verbose: print('Worker %s STEP2.1 Search for Mutations SUBS ENDS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))

        accumulate_for_same_simulation(subsType2DecileIndex2NumberofMutationsDict,sample2SubsType2DecileIndex2NumberofMutationsDict,type2DecileIndex2AccumulatedNumberofMutationsDict,sample2Type2DecileIndex2AccumulatedNumberofMutationsDict)
    ##################################################################################################################

    ##################################################################################################################
    if ((chrBased_simBased_indels_df is not None) and (not chrBased_simBased_indels_df.empty)):
        if verbose: print('Worker %s STEP2.2 Search for Mutations INDELS STARTS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))
        indelType2DecileIndex2NumberofMutationsDict, sample2IndelsType2DecileIndex2NumberofMutationsDict = searchforMutations_NoInitialization(
            sample2NumberofIndelsDict,
            sample2IndelsSignature2NumberofMutationsDict,
            chrBased_simBased_indels_df,
            chrBasedReplicationTimeDataArrayWithDecileIndex,
            indelsSignature2PropertiesListDict,
            AGGREGATEDINDELS,
            sample_based)
        if verbose: print('Worker %s STEP2.2 Search for Mutations INDELS ENDS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))

        accumulate_for_same_simulation(indelType2DecileIndex2NumberofMutationsDict,sample2IndelsType2DecileIndex2NumberofMutationsDict,type2DecileIndex2AccumulatedNumberofMutationsDict,sample2Type2DecileIndex2AccumulatedNumberofMutationsDict)
    ##################################################################################################################

    ##################################################################################################################
    if ((chrBased_simBased_dinucs_df is not None) and (not chrBased_simBased_dinucs_df.empty)):
        if verbose: print('Worker %s STEP2.3 Search for Mutations DINUCS STARTS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))
        dinucType2DecileIndex2NumberofMutationsDict, sample2DinucsType2DecileIndex2NumberofMutationsDict = searchforMutations_NoInitialization(
            sample2NumberofDinucsDict,
            sample2DinucsSignature2NumberofMutationsDict,
            chrBased_simBased_dinucs_df,
            chrBasedReplicationTimeDataArrayWithDecileIndex,
            dinucsSignature2PropertiesListDict,
            AGGREGATEDDINUCS,
            sample_based)
        if verbose: print('Worker %s STEP2.3 Search for Mutations DINUCS ENDS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))

        accumulate_for_same_simulation(dinucType2DecileIndex2NumberofMutationsDict,sample2DinucsType2DecileIndex2NumberofMutationsDict,type2DecileIndex2AccumulatedNumberofMutationsDict,sample2Type2DecileIndex2AccumulatedNumberofMutationsDict)
    ##################################################################################################################

    return  type2DecileIndex2AccumulatedNumberofMutationsDict, sample2Type2DecileIndex2AccumulatedNumberofMutationsDict

##################################################################


##################################################################
#Used up to now
def fillDictionaries(sample2NumberofSubsDict,
                    sample2NumberofIndelsDict,
                    sample2NumberofDinucsDict,
                    sample2SubsSignature2NumberofMutationsDict,
                    sample2IndelsSignature2NumberofMutationsDict,
                    sample2DinucsSignature2NumberofMutationsDict,
                    chrBasedReplicationTimeDataArrayWithDecileIndex,
                    chrBased_simBased_subs_df,
                    chrBased_simBased_indels_df,
                    chrBased_simBased_dinucs_df,
                    numofSimulations,
                    simNum,
                    chrLong,
                    subsSignature2PropertiesListDict,
                    indelsSignature2PropertiesListDict,
                    dinucsSignature2PropertiesListDict,
                    verbose):

    simNum2Type2DecileIndex2NumberofMutationsDict = {}
    simNum2Sample2Type2DecileIndex2NumberofMutationsDict = {}

    ##################################################################################################################
    if ((chrBased_simBased_subs_df is not None) and (not chrBased_simBased_subs_df.empty)):
        if verbose: print('Worker %s STEP2.1 Search for Mutations SUBS STARTS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))
        simNum2SubsType2DecileIndex2NumberofMutationsDict, simNum2Sample2SubsType2DecileIndex2NumberofMutationsDict = searchforMutations(
            sample2NumberofSubsDict,
            sample2SubsSignature2NumberofMutationsDict,
            chrBased_simBased_subs_df,
            chrBasedReplicationTimeDataArrayWithDecileIndex,
            subsSignature2PropertiesListDict,
            AGGREGATEDSUBSTITUTIONS,
            numofSimulations)
        if verbose: print('Worker %s STEP2.1 Search for Mutations SUBS ENDS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))

        accumulate(simNum2SubsType2DecileIndex2NumberofMutationsDict,simNum2Sample2SubsType2DecileIndex2NumberofMutationsDict,simNum2Type2DecileIndex2NumberofMutationsDict,simNum2Sample2Type2DecileIndex2NumberofMutationsDict)
    ##################################################################################################################

    ##################################################################################################################
    if ((chrBased_simBased_indels_df is not None) and (not chrBased_simBased_indels_df.empty)):
        if verbose: print('Worker %s STEP2.2 Search for Mutations INDELS STARTS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))
        simNum2IndelType2DecileIndex2NumberofMutationsDict, simNum2Sample2IndelsType2DecileIndex2NumberofMutationsDict = searchforMutations(
            sample2NumberofIndelsDict,
            sample2IndelsSignature2NumberofMutationsDict,
            chrBased_simBased_indels_df,
            chrBasedReplicationTimeDataArrayWithDecileIndex,
            indelsSignature2PropertiesListDict,
            AGGREGATEDINDELS,
            numofSimulations)
        if verbose: print('Worker %s STEP2.2 Search for Mutations INDELS ENDS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))

        accumulate(simNum2IndelType2DecileIndex2NumberofMutationsDict,simNum2Sample2IndelsType2DecileIndex2NumberofMutationsDict,simNum2Type2DecileIndex2NumberofMutationsDict,simNum2Sample2Type2DecileIndex2NumberofMutationsDict)
    ##################################################################################################################

    ##################################################################################################################
    if ((chrBased_simBased_dinucs_df is not None) and (not chrBased_simBased_dinucs_df.empty)):
        if verbose: print('Worker %s STEP2.3 Search for Mutations DINUCS STARTS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))
        simNum2DinucType2DecileIndex2NumberofMutationsDict, simNum2Sample2DinucsType2DecileIndex2NumberofMutationsDict = searchforMutations(
            sample2NumberofDinucsDict,
            sample2DinucsSignature2NumberofMutationsDict,
            chrBased_simBased_dinucs_df,
            chrBasedReplicationTimeDataArrayWithDecileIndex,
            dinucsSignature2PropertiesListDict,
            AGGREGATEDDINUCS,
            numofSimulations)
        if verbose: print('Worker %s STEP2.3 Search for Mutations DINUCS ENDS %s simNum:%d %s MB' % (str(os.getpid()), chrLong, simNum, memory_usage()))

        accumulate(simNum2DinucType2DecileIndex2NumberofMutationsDict,simNum2Sample2DinucsType2DecileIndex2NumberofMutationsDict,simNum2Type2DecileIndex2NumberofMutationsDict,simNum2Sample2Type2DecileIndex2NumberofMutationsDict)
    ##################################################################################################################

    return  simNum2Type2DecileIndex2NumberofMutationsDict, simNum2Sample2Type2DecileIndex2NumberofMutationsDict
##################################################################

##################################################################
#DEC 9, 2019
# for pool.apply_sync
def combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray_for_apply_sync(outputDir,jobname,simNum,chrLong,
                    sample2NumberofSubsDict,sample2NumberofIndelsDict,sample2NumberofDinucsDict,
                    sample2SubsSignature2NumberofMutationsDict,sample2IndelsSignature2NumberofMutationsDict,sample2DinucsSignature2NumberofMutationsDict,
                    sample_based,subsSignature2PropertiesListDict,indelsSignature2PropertiesListDict,dinucsSignature2PropertiesListDict,verbose,chrBasedReplicationTimeDataArrayWithDecileIndex):

    if verbose: print('Worker %s STEP1 GENERATE %s simNum:%d STARTS %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))

    chrBased_simBased_subs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, SUBS, simNum)
    chrBased_simBased_indels_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, INDELS, simNum)
    chrBased_simBased_dinucs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, DINUCS, simNum)

    # #Read already created npy file
    # chrBasedReplicationTimeFile = '%s_replication_time.npy' % (chrLong)
    # chrBasedReplicationTimeFilePath = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB,REPLICATION, CHRBASED, chrBasedReplicationTimeFile)
    # chrBasedReplicationTimeDataArrayWithDecileIndex=np.load(chrBasedReplicationTimeFilePath,mmap_mode='r')

    if verbose: print('Worker %s STEP2 FILL DICTIONARIES STARTS %s simNum:%d %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))
    type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict = fillDictionaries_chromBased_simBased(
        sample2NumberofSubsDict,
        sample2NumberofIndelsDict,
        sample2NumberofDinucsDict,
        sample2SubsSignature2NumberofMutationsDict,
        sample2IndelsSignature2NumberofMutationsDict,
        sample2DinucsSignature2NumberofMutationsDict,
        chrBasedReplicationTimeDataArrayWithDecileIndex,
        chrBased_simBased_subs_df,
        chrBased_simBased_indels_df,
        chrBased_simBased_dinucs_df,
        sample_based,
        simNum,
        chrLong,
        subsSignature2PropertiesListDict,
        indelsSignature2PropertiesListDict,
        dinucsSignature2PropertiesListDict,
        verbose)
    if verbose: print('Worker %s STEP3 FILL DICTIONARIES ENDS %s simNum:%d %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))

    if verbose: print('Worker %s STEP4 GENERATE %s simNum:%d ENDS %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))
    return (simNum,chrLong,type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict)

##################################################################


##################################################################
#Nov 12, 2019
#Subs, Indels, Dinucs
def combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray(inputList):
    outputDir=inputList[0]
    jobname=inputList[1]
    simNum = inputList[2]
    chrLong = inputList[3]
    sample2NumberofSubsDict = inputList[4]
    sample2NumberofIndelsDict = inputList[5]
    sample2NumberofDinucsDict = inputList[6]
    sample2SubsSignature2NumberofMutationsDict = inputList[7]
    sample2IndelsSignature2NumberofMutationsDict = inputList[8]
    sample2DinucsSignature2NumberofMutationsDict = inputList[9]
    sample_based = inputList[10]
    subsSignature2PropertiesListDict=inputList[11]
    indelsSignature2PropertiesListDict=inputList[12]
    dinucsSignature2PropertiesListDict=inputList[13]
    verbose=inputList[14]
    chrBasedReplicationTimeDataArrayWithDecileIndex= inputList[15]

    if verbose: print('Worker %s STEP1 GENERATE %s simNum:%d STARTS %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))

    chrBased_simBased_subs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, SUBS, simNum)
    chrBased_simBased_indels_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, INDELS, simNum)
    chrBased_simBased_dinucs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, DINUCS, simNum)

    # #Read already created npy file
    # chrBasedReplicationTimeFile = '%s_replication_time.npy' % (chrLong)
    # chrBasedReplicationTimeFilePath = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB,REPLICATION, CHRBASED, chrBasedReplicationTimeFile)
    # chrBasedReplicationTimeDataArrayWithDecileIndex=np.load(chrBasedReplicationTimeFilePath,mmap_mode='r')

    if verbose: print('Worker %s STEP2 FILL DICTIONARIES STARTS %s simNum:%d %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))
    type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict = fillDictionaries_chromBased_simBased(
        sample2NumberofSubsDict,
        sample2NumberofIndelsDict,
        sample2NumberofDinucsDict,
        sample2SubsSignature2NumberofMutationsDict,
        sample2IndelsSignature2NumberofMutationsDict,
        sample2DinucsSignature2NumberofMutationsDict,
        chrBasedReplicationTimeDataArrayWithDecileIndex,
        chrBased_simBased_subs_df,
        chrBased_simBased_indels_df,
        chrBased_simBased_dinucs_df,
        sample_based,
        simNum,
        chrLong,
        subsSignature2PropertiesListDict,
        indelsSignature2PropertiesListDict,
        dinucsSignature2PropertiesListDict,
        verbose)
    if verbose: print('Worker %s STEP3 FILL DICTIONARIES ENDS %s simNum:%d %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))

    if verbose: print('Worker %s STEP4 GENERATE %s simNum:%d ENDS %s MB' %(str(os.getpid()),chrLong,simNum,memory_usage()))
    return simNum, type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict

##################################################################



##################################################################
#Subs, Indels, Dinucs
def generateReplicationTimeNPArrayAndSearchMutationsOnNPArray(inputList):
    chrLong = inputList[0]
    chromSize = inputList[1]
    sample2NumberofSubsDict = inputList[2]
    sample2NumberofIndelsDict = inputList[3]
    sample2NumberofDinucsDict = inputList[4]
    sample2SubsSignature2NumberofMutationsDict = inputList[5]
    sample2IndelsSignature2NumberofMutationsDict = inputList[6]
    sample2DinucsSignature2NumberofMutationsDict = inputList[7]
    chrBased_subs_df_split = inputList[8]
    chrBased_indels_df_split = inputList[9]
    chrBased_dinucs_df_split = inputList[10]
    chrBased_grouped_decile_df_list = inputList[11]
    numofSimulations = inputList[12]
    subsSignature2PropertiesListDict=inputList[13]
    indelsSignature2PropertiesListDict=inputList[14]
    dinucsSignature2PropertiesListDict=inputList[15]

    #fill nparray slices with decileIndex and return it in the function fillChrBasedDecileIndexArray
    chrBasedReplicationTimeDataArrayWithDecileIndex = fillChrBasedReplicationTimeNPArray(chrLong,chromSize,chrBased_grouped_decile_df_list)

    simNum2Type2DecileIndex2NumberofMutationsDict, simNum2Sample2Type2DecileIndex2NumberofMutationsDict = fillDictionaries(
        sample2NumberofSubsDict,
        sample2NumberofIndelsDict,
        sample2NumberofDinucsDict,
        sample2SubsSignature2NumberofMutationsDict,
        sample2IndelsSignature2NumberofMutationsDict,
        sample2DinucsSignature2NumberofMutationsDict,
        chrBasedReplicationTimeDataArrayWithDecileIndex,
        chrBased_subs_df_split,
        chrBased_indels_df_split,
        chrBased_dinucs_df_split,
        numofSimulations,
        subsSignature2PropertiesListDict,
        indelsSignature2PropertiesListDict,
        dinucsSignature2PropertiesListDict)

    return simNum2Type2DecileIndex2NumberofMutationsDict, simNum2Sample2Type2DecileIndex2NumberofMutationsDict
##################################################################

##################################################################
#DEC 8, 2019
#Accumulate for the same simulation
def accumulate_for_same_simulation(type2DecileIndex2CountDict,sample2Type2DecileIndex2CountDict,
               type2DecileIndex2AccumulatedCountDict,sample2Type2DecileIndex2AccumulatedCountDict):

    ######################## Type Based starts #######################################
    for type, decileIndex2CountDict in type2DecileIndex2CountDict.items():

        if type not in type2DecileIndex2AccumulatedCountDict:
            type2DecileIndex2AccumulatedCountDict[type] = {}

        for decileIndex, decileCount in decileIndex2CountDict.items():
            # if key in dictionary
            if decileIndex in type2DecileIndex2AccumulatedCountDict[type]:
                type2DecileIndex2AccumulatedCountDict[type][decileIndex] += decileCount
            else:
                type2DecileIndex2AccumulatedCountDict[type][decileIndex] = decileCount
    ######################## Type Based starts #######################################


    ######################## Sample Based starts #######################################
    for sample in sample2Type2DecileIndex2CountDict:
        if sample not in sample2Type2DecileIndex2AccumulatedCountDict:
            sample2Type2DecileIndex2AccumulatedCountDict[sample] = {}

        for type, decileIndex2CountDict in sample2Type2DecileIndex2CountDict[sample].items():
            if type not in sample2Type2DecileIndex2AccumulatedCountDict[sample]:
                sample2Type2DecileIndex2AccumulatedCountDict[sample][type] = {}

            for decileIndex, decileCount in decileIndex2CountDict.items():
                # if key in dictionary
                if decileIndex in sample2Type2DecileIndex2AccumulatedCountDict[sample][type]:
                    sample2Type2DecileIndex2AccumulatedCountDict[sample][type][decileIndex] += decileCount
                else:
                    sample2Type2DecileIndex2AccumulatedCountDict[sample][type][decileIndex] = decileCount
    ######################## Sample Based ends #########################################

##################################################################

##################################################################
#DEC 8, 2019
def accumulate_each_sim_result(simNum,
                       type2DecileIndex2CountDict,
                       sample2Type2DecileIndex2CountDict,
                       simNum2Type2DecileIndex2AccumulatedCountDict,
                       simNum2Sample2Type2DecileIndex2AccumulatedCountDict):

    ###########################################################################
    if simNum not in simNum2Type2DecileIndex2AccumulatedCountDict:
        simNum2Type2DecileIndex2AccumulatedCountDict[simNum] = {}

    type2DecileBasedAllChrAccumulatedCountDict = simNum2Type2DecileIndex2AccumulatedCountDict[simNum]

    for type, decileIndex2CountDict in type2DecileIndex2CountDict.items():

        if type not in type2DecileBasedAllChrAccumulatedCountDict:
            type2DecileBasedAllChrAccumulatedCountDict[type] = {}

        for decileIndex, decileCount in decileIndex2CountDict.items():
            # if key in dictionary
            if decileIndex in type2DecileBasedAllChrAccumulatedCountDict[type]:
                type2DecileBasedAllChrAccumulatedCountDict[type][decileIndex] += decileCount
            else:
                type2DecileBasedAllChrAccumulatedCountDict[type][decileIndex] = decileCount
    ###########################################################################

    ######################## Sample Based starts #######################################
    if simNum not in simNum2Sample2Type2DecileIndex2AccumulatedCountDict:
        simNum2Sample2Type2DecileIndex2AccumulatedCountDict[simNum] = {}

    sample2Type2DecileIndex2AccumulatedCountDict = simNum2Sample2Type2DecileIndex2AccumulatedCountDict[simNum]

    for sample in sample2Type2DecileIndex2CountDict:
        if sample not in sample2Type2DecileIndex2AccumulatedCountDict:
            sample2Type2DecileIndex2AccumulatedCountDict[sample] = {}

        for type, decileIndex2CountDict in sample2Type2DecileIndex2CountDict[sample].items():
            if type not in sample2Type2DecileIndex2AccumulatedCountDict[sample]:
                sample2Type2DecileIndex2AccumulatedCountDict[sample][type] = {}

            for decileIndex, decileCount in decileIndex2CountDict.items():
                # if key in dictionary
                if decileIndex in sample2Type2DecileIndex2AccumulatedCountDict[sample][type]:
                    sample2Type2DecileIndex2AccumulatedCountDict[sample][type][decileIndex] += decileCount
                else:
                    sample2Type2DecileIndex2AccumulatedCountDict[sample][type][decileIndex] = decileCount
    ######################## Sample Based ends #########################################


##################################################################



##################################################################
#simulations integrated
def accumulate(simNum2Type2DecileIndex2CountDict,simNum2Sample2Type2DecileIndex2CountDict,simNum2Type2DecileIndex2AccumulatedCountDict,simNum2Sample2Type2DecileIndex2AccumulatedCountDict):

    ###########################################################################
    for simNum, type2DecileIndex2CountDict in simNum2Type2DecileIndex2CountDict.items():

        if simNum not in simNum2Type2DecileIndex2AccumulatedCountDict:
            simNum2Type2DecileIndex2AccumulatedCountDict[simNum] = {}

        type2DecileBasedAllChrAccumulatedCountDict = simNum2Type2DecileIndex2AccumulatedCountDict[simNum]

        for type, decileIndex2CountDict in type2DecileIndex2CountDict.items():

            if type not in type2DecileBasedAllChrAccumulatedCountDict:
                type2DecileBasedAllChrAccumulatedCountDict[type] = {}

            for decileIndex, decileCount in decileIndex2CountDict.items():
                # if key in dictionary
                if decileIndex in type2DecileBasedAllChrAccumulatedCountDict[type]:
                    type2DecileBasedAllChrAccumulatedCountDict[type][decileIndex] += decileCount
                else:
                    type2DecileBasedAllChrAccumulatedCountDict[type][decileIndex] = decileCount
    ###########################################################################

    ######################## Sample Based starts #######################################
    for simNum, sample2Type2DecileIndex2CountDict in simNum2Sample2Type2DecileIndex2CountDict.items():

        if simNum not in simNum2Sample2Type2DecileIndex2AccumulatedCountDict:
            simNum2Sample2Type2DecileIndex2AccumulatedCountDict[simNum] = {}

        sample2Type2DecileIndex2AccumulatedCountDict = simNum2Sample2Type2DecileIndex2AccumulatedCountDict[simNum]

        for sample in sample2Type2DecileIndex2CountDict:
            if sample not in sample2Type2DecileIndex2AccumulatedCountDict:
                sample2Type2DecileIndex2AccumulatedCountDict[sample] = {}

            for type, decileIndex2CountDict in sample2Type2DecileIndex2CountDict[sample].items():
                if type not in sample2Type2DecileIndex2AccumulatedCountDict[sample]:
                    sample2Type2DecileIndex2AccumulatedCountDict[sample][type] = {}

                for decileIndex, decileCount in decileIndex2CountDict.items():
                    # if key in dictionary
                    if decileIndex in sample2Type2DecileIndex2AccumulatedCountDict[sample][type]:
                        sample2Type2DecileIndex2AccumulatedCountDict[sample][type][decileIndex] += decileCount
                    else:
                        sample2Type2DecileIndex2AccumulatedCountDict[sample][type][decileIndex] = decileCount
    ######################## Sample Based ends #########################################

##################################################################


##################################################################
#simulations integrated
def accumulateTypeBasedDictionaries_simulations_integrated(listofDictionaries,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict):
    for dictList in listofDictionaries:
        #comes from each chromosome
        simNum2Type2DecileIndex2CountBasedDict = dictList[0]
        simNum2Sample2Type2DecileIndex2CountDict = dictList[1]

        accumulate(simNum2Type2DecileIndex2CountBasedDict,simNum2Sample2Type2DecileIndex2CountDict,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
##################################################################


##################################################################
def getNormalizedMutationDensityList(mutationDensityDict):
    densities = mutationDensityDict.values()
    maxDensity = max(densities)
    if maxDensity>0:
        normalizedMutationDensities = [x/maxDensity for x in densities]

    else:
        normalizedMutationDensities = densities

    return normalizedMutationDensities
##################################################################



##################################################################
#March 22, 2019 starts
def getMutationDensityDictNewVersion(decileIndex2NumberofAttributableBasesDict,decileBasedAllChrAccumulatedCountDict):
    decileBasedMutationDensityDict = {}
    numberofMutations = 0

    numberofMutationsList = []
    numberofAttributableBasesList = []

    for decileIndex in decileIndex2NumberofAttributableBasesDict:
        if (decileIndex in decileBasedAllChrAccumulatedCountDict):
            count = decileBasedAllChrAccumulatedCountDict[decileIndex]
            numberofMutations += count
            numofAttBases = decileIndex2NumberofAttributableBasesDict[decileIndex]
            mutationDensity = float(count) / numofAttBases
            decileBasedMutationDensityDict[decileIndex] = mutationDensity
            numberofMutationsList.append(count)
            numberofAttributableBasesList.append(numofAttBases)

        else:
            decileBasedMutationDensityDict[decileIndex] = 0
            numberofMutationsList.append(0)
            numberofAttributableBasesList.append(0)


    return numberofMutations, decileBasedMutationDensityDict, numberofMutationsList, numberofAttributableBasesList
#March 22, 2019 starts
##################################################################

##################################################################
def getMutationDensityDict(decile_df_list,decileBasedAllChrAccumulatedCountDict):
    decileBasedMutationDensityDict = {}
    numberofMutations = 0

    numberofMutationsList = []
    numberofAttributableBasesList = []

    #Modifiled as enumerate(deciles,1) formerly it was enumerate(deciles,0)
    for i,decile_df in enumerate(decile_df_list,1):
        if (i in decileBasedAllChrAccumulatedCountDict):
            count = decileBasedAllChrAccumulatedCountDict[i]
            numberofMutations += count
            numofAttBases = decile_df[NUMOFBASES].sum()
            mutationDensity=float(count)/numofAttBases
            decileBasedMutationDensityDict[i] = mutationDensity
            numberofMutationsList.append(count)
            numberofAttributableBasesList.append(numofAttBases)
        else:
            decileBasedMutationDensityDict[i] = 0
            numberofMutationsList.append(0)
            numberofAttributableBasesList.append(0)

        # print('decile: %d numofAttBases: %d' %(i,numofAttBases))

    return numberofMutations, decileBasedMutationDensityDict, numberofMutationsList, numberofAttributableBasesList
##################################################################


##################################################################
def fillInputList(outputDir,jobname,simNum,chrLong,
                  sample2NumberofSubsDict,sample2NumberofIndelsDict,sample2NumberofDinucsDict,
                 sample2SubsSignature2NumberofMutationsDict,sample2IndelsSignature2NumberofMutationsDict,sample2DinucsSignature2NumberofMutationsDict,
                 sample_based,subsSignature2PropertiesListDict,indelsSignature2PropertiesListDict,dinucsSignature2PropertiesListDict,verbose,chrBasedReplicationTimeDataArrayWithDecileIndex):

    if verbose: print('Worker %s FillInputList %s simNum:%d starts' %(str(os.getpid()),chrLong,simNum))
    inputList=[]
    inputList.append(outputDir)
    inputList.append(jobname)
    inputList.append(simNum)
    inputList.append(chrLong)
    inputList.append(sample2NumberofSubsDict)
    inputList.append(sample2NumberofIndelsDict)
    inputList.append(sample2NumberofDinucsDict)
    inputList.append(sample2SubsSignature2NumberofMutationsDict)
    inputList.append(sample2IndelsSignature2NumberofMutationsDict)
    inputList.append(sample2DinucsSignature2NumberofMutationsDict)
    inputList.append(sample_based)
    inputList.append(subsSignature2PropertiesListDict)
    inputList.append(indelsSignature2PropertiesListDict)
    inputList.append(dinucsSignature2PropertiesListDict)
    inputList.append(verbose)
    inputList.append(chrBasedReplicationTimeDataArrayWithDecileIndex)

    return inputList
##################################################################

##################################################################
def calculateCountsForMutationsFillingReplicationTimeNPArrayRuntime(computationType,
                                    outputDir,
                                    jobname,
                                    numofSimulations,
                                    sample2NumberofSubsDict,sample2NumberofIndelsDict,sample2NumberofDinucsDict,
                                    sample2SubsSignature2NumberofMutationsDict,sample2IndelsSignature2NumberofMutationsDict,sample2DinucsSignature2NumberofMutationsDict,
                                    chromSizesDict,
                                    chrNamesList,
                                    chrBased_grouped_decile_df_list,
                                    subsSignature2PropertiesListDict,
                                    indelsSignature2PropertiesListDict,
                                    dinucsSignature2PropertiesListDict,
                                    sample_based,
                                    verbose):

    numofProcesses = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(numofProcesses)

    simNum2Type2DecileBasedAllChrAccumulatedCountDict = {}
    simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict ={}

    ########################################################################################################################################################
    if (computationType == COMPUTATION_ALL_CHROMOSOMES_PARALLEL):
        # It seems that chrNames in replicationTimeData are long chr names such as chr1, chrX
        poolInputList = []
        for chrLong in chrNamesList:
            chromSize = chromSizesDict[chrLong]

            original_chrBased_subs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, SUBS,0)
            original_chrBased_indels_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, INDELS,0)
            original_chrBased_dinucs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong,DINUCS,0)

            #original data combined with simulations dara
            combined_chrBased_subs_df= getCombinedChrBasedDF(outputDir, jobname, chrLong,original_chrBased_subs_df,SUBS,numofSimulations)
            combined_chrBased_indels_df = getCombinedChrBasedDF(outputDir, jobname, chrLong,original_chrBased_indels_df,INDELS,numofSimulations)
            combined_chrBased_dinucs_df= getCombinedChrBasedDF(outputDir, jobname, chrLong,original_chrBased_dinucs_df,DINUCS,numofSimulations)

            ###################################################################################################################################################
            inputList = []
            inputList.append(chrLong)
            inputList.append(chromSize)
            inputList.append(sample2NumberofSubsDict)
            inputList.append(sample2NumberofIndelsDict)
            inputList.append(sample2NumberofDinucsDict)
            inputList.append(sample2SubsSignature2NumberofMutationsDict)
            inputList.append(sample2IndelsSignature2NumberofMutationsDict)
            inputList.append(sample2DinucsSignature2NumberofMutationsDict)
            inputList.append(combined_chrBased_subs_df)  # Different
            inputList.append(combined_chrBased_indels_df)  # Different
            inputList.append(combined_chrBased_dinucs_df)  # Different
            inputList.append(chrBased_grouped_decile_df_list)  # Same
            inputList.append(numofSimulations)
            inputList.append(subsSignature2PropertiesListDict)
            inputList.append(indelsSignature2PropertiesListDict)
            inputList.append(dinucsSignature2PropertiesListDict)
            poolInputList.append(inputList)

        # Call the parallel code for poolInputList
        # It returns a list of whatever generateNPArrayAndSearchMutationsOnNPArray will return
        # It must return list of tuples
        # Since generateNPArrayAndSearchMutationsOnNPArray return tuple
        # Fill np.array with 0 if there is no signal, otherwise fill with the decileIndex if there is a signal
        listofDictionaries = pool.map(generateReplicationTimeNPArrayAndSearchMutationsOnNPArray, poolInputList)
        accumulateTypeBasedDictionaries_simulations_integrated(listofDictionaries,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
        ###################################################################################################################################################

    ########################################################################################################################################################

    elif (computationType == COMPUTATION_CHROMOSOMES_SEQUENTIAL_SIMULATIONS_SEQUENTIAL):
        # It seems that chrNames in replicationTimeData are long chr names such as chr1, chrX
        for chrLong in chrNamesList:
            chromSize = chromSizesDict[chrLong]

            for simNum in range(0,numofSimulations+1):
                subs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, SUBS,simNum)
                indels_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, INDELS,simNum)
                dinucs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong,DINUCS,simNum)

                ###################################################################################################################################################
                inputList = []
                inputList.append(chrLong)
                inputList.append(chromSize)
                inputList.append(sample2NumberofSubsDict)
                inputList.append(sample2NumberofIndelsDict)
                inputList.append(sample2NumberofDinucsDict)
                inputList.append(sample2SubsSignature2NumberofMutationsDict)
                inputList.append(sample2IndelsSignature2NumberofMutationsDict)
                inputList.append(sample2DinucsSignature2NumberofMutationsDict)
                inputList.append(subs_df)  # Different
                inputList.append(indels_df)  # Different
                inputList.append(dinucs_df)  # Different
                inputList.append(chrBased_grouped_decile_df_list)  # Same
                inputList.append(numofSimulations)
                inputList.append(subsSignature2PropertiesListDict)
                inputList.append(indelsSignature2PropertiesListDict)
                inputList.append(dinucsSignature2PropertiesListDict)

                simNum2Type2DecileIndex2NumberofMutationsDict, simNum2Sample2Type2DecileIndex2NumberofMutationsDict = generateReplicationTimeNPArrayAndSearchMutationsOnNPArray(inputList)
                accumulate(simNum2Type2DecileIndex2NumberofMutationsDict,simNum2Sample2Type2DecileIndex2NumberofMutationsDict,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
        ###################################################################################################################################################

    elif (computationType==USING_APPLY_ASYNC):
        sim_nums = range(0, numofSimulations + 1)

        #########################################################################################
        def accumulate_apply_async_result(result_tuple):
            simNum = result_tuple[0]
            chrLong=result_tuple[1]
            type2DecileIndex2NumberofMutationsDict = result_tuple[2]
            sample2Type2DecileIndex2NumberofMutationsDict = result_tuple[3]

            if verbose: print('Worker pid %s memory_usage %.2f MB ACCUMULATE simNum:%s %s' % (str(os.getpid()), memory_usage(), simNum, chrLong))

            accumulate_each_sim_result(simNum,
                                       type2DecileIndex2NumberofMutationsDict,
                                       sample2Type2DecileIndex2NumberofMutationsDict,
                                       simNum2Type2DecileBasedAllChrAccumulatedCountDict,
                                       simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
        #########################################################################################


        #######################################################################################################################
        for chrLong in chrNamesList:
            chromSize = chromSizesDict[chrLong]
            if verbose: print('Worker pid %s maximum memory usage in FILL CHROM BASED NP ARRAY %.2f MB for %s STARTS' % (str(os.getpid()), memory_usage(),chrLong))
            chrBasedReplicationTimeDataArrayWithDecileIndex = fillChrBasedReplicationTimeNPArray(chrLong, chromSize,chrBased_grouped_decile_df_list)
            if verbose: print('Worker pid %s maximum memory usage in FILL CHROM BASED NP ARRAY %.2f MB for %s ENDS' % (str(os.getpid()), memory_usage(),chrLong))

            for simNum in sim_nums:
                pool.apply_async(combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray_for_apply_sync, (outputDir,jobname,simNum,chrLong,
                    sample2NumberofSubsDict,sample2NumberofIndelsDict,sample2NumberofDinucsDict,
                    sample2SubsSignature2NumberofMutationsDict,sample2IndelsSignature2NumberofMutationsDict,sample2DinucsSignature2NumberofMutationsDict,
                    sample_based,subsSignature2PropertiesListDict,indelsSignature2PropertiesListDict,dinucsSignature2PropertiesListDict,verbose,chrBasedReplicationTimeDataArrayWithDecileIndex), callback=accumulate_apply_async_result)
        #######################################################################################################################


    elif (computationType == USING_IMAP_UNORDERED):
        sim_nums = range(0, numofSimulations + 1)
        sim_num_chr_tuples = ((sim_num, chrLong) for sim_num in sim_nums for chrLong in chrNamesList)

        #######################################################################################################################
        #Creating chr based replication time array file only once.
        #imap_unordered
        for chrLong in chrNamesList:
            chromSize = chromSizesDict[chrLong]
            if verbose: print('Worker pid %s maximum memory usage in FILL CHROM BASED NP ARRAY %.2f MB for %s STARTS' % (str(os.getpid()), memory_usage(),chrLong))
            chrBasedReplicationTimeDataArrayWithDecileIndex = fillChrBasedReplicationTimeNPArray(chrLong, chromSize,chrBased_grouped_decile_df_list)
            if verbose: print('Worker pid %s maximum memory usage in FILL CHROM BASED NP ARRAY %.2f MB for %s ENDS' % (str(os.getpid()), memory_usage(),chrLong))

            for simNum, type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict in pool.imap_unordered(
                    combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray, (
                    fillInputList(outputDir,jobname,simNum,chrLong,
                    sample2NumberofSubsDict,sample2NumberofIndelsDict,sample2NumberofDinucsDict,
                    sample2SubsSignature2NumberofMutationsDict,sample2IndelsSignature2NumberofMutationsDict,sample2DinucsSignature2NumberofMutationsDict,
                    sample_based,subsSignature2PropertiesListDict,indelsSignature2PropertiesListDict,dinucsSignature2PropertiesListDict,verbose,chrBasedReplicationTimeDataArrayWithDecileIndex) for simNum in sim_nums), chunksize=1):

                if verbose: print('Worker pid %s maximum memory usage in ACCUMULATE %.2f (mb) for %s' % (str(os.getpid()), memory_usage(),chrLong))
                accumulate_each_sim_result(simNum,
                                           type2DecileIndex2NumberofMutationsDict,
                                           sample2Type2DecileIndex2NumberofMutationsDict,
                                           simNum2Type2DecileBasedAllChrAccumulatedCountDict,
                                           simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
        #######################################################################################################################

        #######################################################################################################################
        #Creating and writing npy files and loading npy files is faster.
        #Requires 4 GB memory space
        #In order to return to this solution:
        # Remove chrBasedReplicationTimeDataArrayWithDecileIndex from combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray
        # Remove chrBasedReplicationTimeDataArrayWithDecileIndex from fillInputList
        # Uncomment Read already created npy file part in  combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray
        # Create and save npy files Create and save npy files part in replicationTimeAnalysis main function

        # #Using already created and written npy files
        # imap_unordered
        # for simNum, type2DecileIndex2NumberofMutationsDict, sample2Type2DecileIndex2NumberofMutationsDict in pool.imap_unordered(
        #         combined_generateReplicationTimeNPArrayAndSearchMutationsOnNPArray, (
        #         fillInputList(outputDir,jobname,simNum,chrLong,
        #         sample2NumberofSubsDict,sample2NumberofIndelsDict,sample2NumberofDinucsDict,
        #         sample2SubsSignature2NumberofMutationsDict,sample2IndelsSignature2NumberofMutationsDict,sample2DinucsSignature2NumberofMutationsDict,
        #         sample_based,subsSignature2PropertiesListDict,indelsSignature2PropertiesListDict,dinucsSignature2PropertiesListDict,verbose) for simNum, chrLong in sim_num_chr_tuples), chunksize=1):
        #
        #     if verbose: print('\tWorker pid %s maximum memory usage in accumulate %.2f (mb)' % (str(os.getpid()), memory_usage()))
        #     accumulate_each_sim_result(simNum,
        #                type2DecileIndex2NumberofMutationsDict,
        #                sample2Type2DecileIndex2NumberofMutationsDict,
        #                simNum2Type2DecileBasedAllChrAccumulatedCountDict,
        #                simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
        #######################################################################################################################


    elif (computationType == COMPUTATION_CHROMOSOMES_SEQUENTIAL_ALL_SIMULATIONS_PARALLEL):
        # It seems that chrNames in replicationTimeData are long chr names such as chr1, chrX
        for chrLong in chrNamesList:
            poolInputList = []
            chromSize = chromSizesDict[chrLong]

            for simNum in range(0,numofSimulations+1):
                chrBased_simBased_subs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, SUBS,simNum)
                chrBased_simBased_indels_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, INDELS,simNum)
                chrBased_simBased_dinucs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong,DINUCS,simNum)

                ###################################################################################################################################################
                inputList = []
                inputList.append(chrLong)
                inputList.append(chromSize)
                inputList.append(sample2NumberofSubsDict)
                inputList.append(sample2NumberofIndelsDict)
                inputList.append(sample2NumberofDinucsDict)
                inputList.append(sample2SubsSignature2NumberofMutationsDict)
                inputList.append(sample2IndelsSignature2NumberofMutationsDict)
                inputList.append(sample2DinucsSignature2NumberofMutationsDict)
                inputList.append(chrBased_simBased_subs_df)  # Different
                inputList.append(chrBased_simBased_indels_df)  # Different
                inputList.append(chrBased_simBased_dinucs_df)  # Different
                inputList.append(chrBased_grouped_decile_df_list)  # Same
                inputList.append(numofSimulations)
                inputList.append(subsSignature2PropertiesListDict)
                inputList.append(indelsSignature2PropertiesListDict)
                inputList.append(dinucsSignature2PropertiesListDict)
                poolInputList.append(inputList)

            # Call the parallel code for poolInputList
            # It returns a list of whatever generateNPArrayAndSearchMutationsOnNPArray will return
            # It must return list of tuples
            # Since generateNPArrayAndSearchMutationsOnNPArray return tuple
            # Fill np.array with 0 if there is no signal, otherwise fill with the decileIndex if there is a signal
            listofDictionaries = pool.map(generateReplicationTimeNPArrayAndSearchMutationsOnNPArray, poolInputList)
            accumulateTypeBasedDictionaries_simulations_integrated(listofDictionaries,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
        ###################################################################################################################################################

    elif (computationType == COMPUTATION_CHROMOSOMES_SEQUENTIAL_CHROMOSOME_SPLITS_PARALLEL):
        #It seems that chrNames in replicationTimeData are long chr names such as chr1, chrX
        for chrLong in chrNamesList:
            # chrLong = 'chr%s' %(chr)
            chromSize = chromSizesDict[chrLong]

            original_chrBased_subs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, SUBS,0)
            original_chrBased_indels_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, INDELS,0)
            original_chrBased_dinucs_df = readChrBasedMutationsDF(outputDir, jobname, chrLong, DINUCS,0)

            #original data combined with simulations dara
            combined_chrBased_subs_df= getCombinedChrBasedDF(outputDir, jobname, chrLong,original_chrBased_subs_df,SUBS,numofSimulations)
            combined_chrBased_indels_df = getCombinedChrBasedDF(outputDir, jobname, chrLong,original_chrBased_indels_df,INDELS,numofSimulations)
            combined_chrBased_dinucs_df= getCombinedChrBasedDF(outputDir, jobname, chrLong,original_chrBased_dinucs_df,DINUCS,numofSimulations)

            chrBased_combined_subs_df_splits_list = []
            chrBased_combined_indels_df_splits_list = []
            chrBased_combined_dinucs_df_splits_list = []

            if ((combined_chrBased_subs_df is not None) and (not combined_chrBased_subs_df.empty)):
                chrBased_combined_subs_df_splits_list = np.array_split(combined_chrBased_subs_df, numofProcesses)

            if ((combined_chrBased_indels_df is not None) and (not combined_chrBased_indels_df.empty)):
                chrBased_combined_indels_df_splits_list = np.array_split(combined_chrBased_indels_df, numofProcesses)

            if ((combined_chrBased_dinucs_df is not None) and (not combined_chrBased_dinucs_df.empty)):
                chrBased_combined_dinucs_df_splits_list = np.array_split(combined_chrBased_dinucs_df, numofProcesses)

            ###################################################################################################################################################
            poolInputList = []
            for split_index in range(numofProcesses):
                if (len(chrBased_combined_subs_df_splits_list)):
                    chrBased_combined_subs_df_split_array = chrBased_combined_subs_df_splits_list[split_index]
                else:
                    chrBased_combined_subs_df_split_array = None

                if (len(chrBased_combined_indels_df_splits_list)):
                    chrBased_combined_indels_df_split_array = chrBased_combined_indels_df_splits_list[split_index]
                else:
                    chrBased_combined_indels_df_split_array = None

                if (len(chrBased_combined_dinucs_df_splits_list)):
                    chrBased_combined_dinucs_df_split_array = chrBased_combined_dinucs_df_splits_list[split_index]
                else:
                    chrBased_combined_dinucs_df_split_array = None

                inputList = []
                inputList.append(chrLong) #Same
                inputList.append(chromSize)
                inputList.append(sample2NumberofSubsDict)
                inputList.append(sample2NumberofIndelsDict)
                inputList.append(sample2NumberofDinucsDict)
                inputList.append(sample2SubsSignature2NumberofMutationsDict)
                inputList.append(sample2IndelsSignature2NumberofMutationsDict)
                inputList.append(sample2DinucsSignature2NumberofMutationsDict)
                inputList.append(chrBased_combined_subs_df_split_array) #Different
                inputList.append(chrBased_combined_indels_df_split_array) #Different
                inputList.append(chrBased_combined_dinucs_df_split_array)  # Different
                inputList.append(chrBased_grouped_decile_df_list)  #Same
                inputList.append(numofSimulations)
                inputList.append(subsSignature2PropertiesListDict)
                inputList.append(indelsSignature2PropertiesListDict)
                inputList.append(dinucsSignature2PropertiesListDict)

                poolInputList.append(inputList)

            # Call the parallel code for poolInputList
            # It returns a list of whatever generateNPArrayAndSearchMutationsOnNPArray will return
            # It must return list of tuples
            # Since generateNPArrayAndSearchMutationsOnNPArray return tuple
            # Fill np.array with 0 if there is no signal, otherwise fill with the decileIndex if there is a signal
            listofDictionaries = pool.map(generateReplicationTimeNPArrayAndSearchMutationsOnNPArray,poolInputList)
            accumulateTypeBasedDictionaries_simulations_integrated(listofDictionaries,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
            ###################################################################################################################################################

        ###################################################################################################################################################

    # print('Replication Time Results %s starts' %(computationType))
    # print('simNum2Type2DecileBasedAllChrAccumulatedCountDict[0]')
    # print(simNum2Type2DecileBasedAllChrAccumulatedCountDict[0])
    # print('simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict[0]')
    # print(simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict[0])
    # print('Replication Time Results %s ends' %(computationType))

    ################################
    pool.close()
    pool.join()
    ################################

    return simNum2Type2DecileBasedAllChrAccumulatedCountDict, simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict
##################################################################



##################################################################
def augment(genome,pool,wavelet_processed_df):
    if (genome==GRCh37):
        wholeGenome = twobitreader.TwoBitFile(os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,UCSCGENOME,HG19_2BIT))
    elif (genome==GRCh38):
        wholeGenome = twobitreader.TwoBitFile(os.path.join(current_abs_path,ONE_DIRECTORY_UP,ONE_DIRECTORY_UP,LIB,UCSCGENOME,HG38_2BIT))

    #Augment in parallel for each chromosome
    poolInputList = []
    chrBased_wavelet_processed_df_groups = wavelet_processed_df.groupby(CHROM)
    for chr, chrBased_wavelet_processed_df_group in chrBased_wavelet_processed_df_groups:
        inputList = []
        inputList.append(chr)
        inputList.append(chrBased_wavelet_processed_df_group)
        #Please note that when you provide the chr based hg19_genome it gives error
        inputList.append(wholeGenome)
        poolInputList.append(inputList)

    # print('Augmentation starts')
    #Each tuple contains chrLong and the dataframe with augmented column with number of attributable bases
    listofTuples = pool.map(addNumofAttributableBasesColumn,poolInputList)
    # print('len(poolInputList): %d' %len(poolInputList))
    # print('len(listofDFs): %d' %len(listofTuples))

    #Define frames which will be a list of dataframes
    frames = []

    for tuple in listofTuples:
        #chrLong = tuple[0]
        chrBased_augmented_df = tuple[1]
        frames.append(chrBased_augmented_df)

    augment_df = pd.concat(frames,ignore_index=True)

    return augment_df
##################################################################


##################################################################
def writeReplicationTimeData(outputDir,jobname,sample_based,decile_df_list,decileIndex2NumberofAttributableBasesDict,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict):
    os.makedirs(os.path.join(outputDir, jobname, DATA, REPLICATIONTIME), exist_ok=True)

    ##############################################################
    for simNum in simNum2Type2DecileBasedAllChrAccumulatedCountDict:
        type2DecileBasedAllChrAccumulatedCountDict = simNum2Type2DecileBasedAllChrAccumulatedCountDict[simNum]
        for type in type2DecileBasedAllChrAccumulatedCountDict:
            decileBasedAllChrAccumulatedCountDict = type2DecileBasedAllChrAccumulatedCountDict[type]

            if (simNum==0):
                normalizedMutationDensityFilename = '%s_NormalizedMutationDensity.txt' %(type)
                numberofMutationsFilename = '%s_NumberofMutations.txt' %(type)
                numberofAttributabelBasesFilename = '%s_NumberofAttributableBases.txt' %(type)
            else:
                normalizedMutationDensityFilename = '%s_sim%d_NormalizedMutationDensity.txt' %(type,simNum)
                numberofMutationsFilename = '%s_sim%d_NumberofMutations.txt' %(type,simNum)
                numberofAttributabelBasesFilename = '%s_sim%d_NumberofAttributableBases.txt' %(type,simNum)

            if (type==AGGREGATEDSUBSTITUTIONS) or (type==AGGREGATEDINDELS) or (type==AGGREGATEDDINUCS) or (type==MICROHOMOLOGY) or (type==REPEAT):
                os.makedirs(os.path.join(outputDir, jobname, DATA, REPLICATIONTIME,type), exist_ok=True)
                normalizedMutationDensityFilePath = os.path.join(outputDir,jobname, DATA, REPLICATIONTIME,type,normalizedMutationDensityFilename)
                numberofMutationsFilePath = os.path.join(outputDir, jobname, DATA, REPLICATIONTIME,type,numberofMutationsFilename)
                numberofAttributabelBasesFilePath = os.path.join(outputDir, jobname, DATA, REPLICATIONTIME,type,numberofAttributabelBasesFilename)
            else:
                os.makedirs(os.path.join(outputDir, jobname, DATA, REPLICATIONTIME, SIGNATUREBASED), exist_ok=True)
                normalizedMutationDensityFilePath = os.path.join(outputDir, jobname, DATA, REPLICATIONTIME, SIGNATUREBASED,normalizedMutationDensityFilename)
                numberofMutationsFilePath = os.path.join(outputDir, jobname, DATA, REPLICATIONTIME, SIGNATUREBASED,numberofMutationsFilename)
                numberofAttributabelBasesFilePath = os.path.join(outputDir, jobname, DATA, REPLICATIONTIME, SIGNATUREBASED,numberofAttributabelBasesFilename)

            # If decileBasedAllChrAccumulatedCountDict is not empty
            if (decileBasedAllChrAccumulatedCountDict):

                if (decile_df_list is not None):
                    numberofMutations, mutationDensityDict,numberofMutationsList, numberofAttributableBasesList = getMutationDensityDict(decile_df_list,decileBasedAllChrAccumulatedCountDict)
                elif (decileIndex2NumberofAttributableBasesDict is not None):
                    numberofMutations, mutationDensityDict,numberofMutationsList, numberofAttributableBasesList = getMutationDensityDictNewVersion(decileIndex2NumberofAttributableBasesDict, decileBasedAllChrAccumulatedCountDict)

                normalizedMutationDensityList = getNormalizedMutationDensityList(mutationDensityDict)

                #Normalized Mutation Density
                with open(normalizedMutationDensityFilePath, 'w') as file:
                    for normalizedMutationDensity in normalizedMutationDensityList:
                        file.write(str(normalizedMutationDensity) + ' ')
                    file.write('\n')

                #Number of Mutations
                with open(numberofMutationsFilePath, 'w') as file:
                    for numberofMutations in numberofMutationsList:
                        file.write(str(numberofMutations) + ' ')
                    file.write('\n')

                #Number of Attributable Bases
                with open(numberofAttributabelBasesFilePath, 'w') as file:
                    for numberofAttributabelBases in numberofAttributableBasesList:
                        file.write(str(numberofAttributabelBases) + ' ')
                    file.write('\n')
    ##############################################################


    ######################### Sample Based starts #####################
    if sample_based:
        for simNum in simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict:
            sample2Type2DecileBasedAllChrAccumulatedCountDict= simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict[simNum]
            for sample in sample2Type2DecileBasedAllChrAccumulatedCountDict:
                os.makedirs(os.path.join(outputDir, jobname, DATA, SAMPLES, sample, REPLICATIONTIME), exist_ok=True)

                for type in sample2Type2DecileBasedAllChrAccumulatedCountDict[sample]:
                    decileBasedAllChrAccumulatedCountDict = sample2Type2DecileBasedAllChrAccumulatedCountDict[sample][type]

                    if (simNum==0):
                        normalizedMutationDensityFilename = '%s_%s_NormalizedMutationDensity.txt' %(sample,type)
                    else:
                        normalizedMutationDensityFilename = '%s_%s_sim%d_NormalizedMutationDensity.txt' %(sample,type,simNum)

                    if (type == AGGREGATEDSUBSTITUTIONS) or (type == AGGREGATEDINDELS) or (type == AGGREGATEDDINUCS) or (type == MICROHOMOLOGY) or (type == REPEAT):
                        os.makedirs(os.path.join(outputDir, jobname, DATA,SAMPLES,sample, REPLICATIONTIME, type), exist_ok=True)
                        normalizedMutationDensityFilePath = os.path.join(outputDir, jobname, DATA, SAMPLES, sample,REPLICATIONTIME,type, normalizedMutationDensityFilename)
                    else:
                        os.makedirs(os.path.join(outputDir, jobname, DATA,SAMPLES,sample, REPLICATIONTIME, SIGNATUREBASED), exist_ok=True)
                        normalizedMutationDensityFilePath = os.path.join(outputDir, jobname, DATA, SAMPLES, sample,REPLICATIONTIME,SIGNATUREBASED, normalizedMutationDensityFilename)

                    #If decileBasedAllChrAccumulatedCountDict is not empty
                    if (decileBasedAllChrAccumulatedCountDict):
                        if (decile_df_list is not None):
                            numberofMutations, mutationDensityDict, numberofMutationsList, numberofAttributableBasesList = getMutationDensityDict(decile_df_list, decileBasedAllChrAccumulatedCountDict)
                        elif (decileIndex2NumberofAttributableBasesDict is not None):
                            numberofMutations, mutationDensityDict, numberofMutationsList, numberofAttributableBasesList = getMutationDensityDictNewVersion(decileIndex2NumberofAttributableBasesDict, decileBasedAllChrAccumulatedCountDict)
                        normalizedMutationDensityList = getNormalizedMutationDensityList(mutationDensityDict)

                        with open(normalizedMutationDensityFilePath, 'w') as file:
                            for normalizedMutationDensity in normalizedMutationDensityList:
                                file.write(str(normalizedMutationDensity) + ' ')
                            file.write('\n')
    ######################### Sample Based ends #######################

##################################################################


##################################################################
#main function
def replicationTimeAnalysis(computationType,sample_based,genome,chromSizesDict,chromNamesList,outputDir,jobname,numofSimulations,repliseqDataFilename,subsSignature2PropertiesListDict,indelsSignature2PropertiesListDict,dinucsSignature2PropertiesListDict,verbose):
    print('\n#################################################################################')
    print('--- ReplicationTimeAnalysis starts')
    print('--- Replication Time Analyis Computation Type:%s' % (computationType))

    #########################################################################
    # Analysis Type can be
    # AggregatedSubstitutions: All in one
    # AggregatedIndels : All in one
    # AggregatedDinucs : All in one
    # IndelsBased : Microhomology, Repeat
    # SignatureBased: Subs Signatures Sig1, Sig2, ... and Indels Signatures  ID1, ID2, ..., ... and Dinucs Signatures  DBS1, DBS2, ...

    # We know the indels type we are interested in.
    # Microhomology indels --- len(indels) >= 3
    # Repeat indels --- len(indels) < 3
    #########################################################################

    ##########################################################################################
    if (sample_based):
        sample2NumberofSubsDict = getSample2NumberofSubsDict(outputDir,jobname)
        sample2NumberofIndelsDict = getSample2NumberofIndelsDict(outputDir,jobname)
        sample2NumberofDinucsDict = getDictionary(outputDir,jobname,Sample2NumberofDinucsDictFilename)

        sample2SubsSignature2NumberofMutationsDict = getSample2SubsSignature2NumberofMutationsDict(outputDir,jobname)
        sample2IndelsSignature2NumberofMutationsDict = getSample2IndelsSignature2NumberofMutationsDict(outputDir,jobname)
        sample2DinucsSignature2NumberofMutationsDict = getDictionary(outputDir,jobname,Sample2DinucsSignature2NumberofMutationsDictFilename)
    else:
        sample2NumberofSubsDict = {}
        sample2NumberofIndelsDict = {}
        sample2NumberofDinucsDict = {}

        sample2SubsSignature2NumberofMutationsDict = {}
        sample2IndelsSignature2NumberofMutationsDict = {}
        sample2DinucsSignature2NumberofMutationsDict = {}
    ##########################################################################################

    # Fill replication np arrays during runtime

    ###################################################################
    ############### Read MCF-7 RepliSeq Time data starts ##############
    ###################################################################
    # Fist decile_df in decile_df_list contains the intervals that are replicated the earliest.
    # Last decile_df in decile_df_list contains the intervals that are replicated the latest.
    # Please note that each decile_df contains intervals from all chroms (mixed chroms)
    #What is the type of deciles? Deciles is a list of dataframes.
    if verbose: print('Worker pid %s READ Repliseq DATA STARTS  %s MB' % (str(os.getpid()), memory_usage()))
    chrNamesInReplicationTimeDataArray, decile_df_list = readRepliSeqTimeData(genome,repliseqDataFilename)
    if verbose: print('Worker pid %s READ Repliseq DATA ENDS  %s MB' % (str(os.getpid()), memory_usage()))

    #Get chrBased grouped deciles
    chrBased_grouped_decile_df_list = []
    #Get this chrLong of each decile
    #The first decile is the earliest one with index 1
    #The last decile is the latest one with index 10
    #We provide these indexes later in the fillChrBasedDecileIndexArray function by enumerate
    for decile_df in decile_df_list:
        chrBased_grouped_decile_df = decile_df.groupby(CHROM)
        chrBased_grouped_decile_df_list.append(chrBased_grouped_decile_df)

    # #Create and save npy files
    # os.makedirs(os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB, REPLICATION,CHRBASED),exist_ok=True)
    # chrBasedNpyFilesPath = os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB, REPLICATION,CHRBASED)
    # for chrLong in chromNamesList:
    #     chromSize=chromSizesDict[chrLong]
    #     #fill nparray slices with decileIndex and return it in the function fillChrBasedDecileIndexArray
    #     if verbose: print('Worker %s FILL AND SAVE CHR BASED REPLICATION TIME NPY ARRAY STARTS %s %s MB' %(str(os.getpid()),chrLong,memory_usage()))
    #     chrBasedReplicationTimeDataArrayWithDecileIndex = fillChrBasedReplicationTimeNPArray(chrLong,chromSize,chrBased_grouped_decile_df_list)
    #     chrBasedReplicationTimeFile='%s_replication_time.npy' %(chrLong)
    #     chrBasedReplicationTimeFilePath=os.path.join(current_abs_path, ONE_DIRECTORY_UP, ONE_DIRECTORY_UP, LIB, REPLICATION,CHRBASED,chrBasedReplicationTimeFile)
    #     np.save(chrBasedReplicationTimeFilePath, chrBasedReplicationTimeDataArrayWithDecileIndex)
    #     if verbose: print('Worker %s FILL AND SAVE CHR BASED REPLICATION TIME NPY ARRAY ENDS %s %s MB' %(str(os.getpid()),chrLong,memory_usage()))

    simNum2Type2DecileBasedAllChrAccumulatedCountDict, simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict = calculateCountsForMutationsFillingReplicationTimeNPArrayRuntime(
                                                                                                                            computationType,
                                                                                                                            outputDir,
                                                                                                                            jobname,
                                                                                                                            numofSimulations,
                                                                                                                            sample2NumberofSubsDict,
                                                                                                                            sample2NumberofIndelsDict,
                                                                                                                            sample2NumberofDinucsDict,
                                                                                                                            sample2SubsSignature2NumberofMutationsDict,
                                                                                                                            sample2IndelsSignature2NumberofMutationsDict,
                                                                                                                            sample2DinucsSignature2NumberofMutationsDict,
                                                                                                                            chromSizesDict,
                                                                                                                            chromNamesList,
                                                                                                                            chrBased_grouped_decile_df_list,
                                                                                                                            subsSignature2PropertiesListDict,
                                                                                                                            indelsSignature2PropertiesListDict,
                                                                                                                            dinucsSignature2PropertiesListDict,
                                                                                                                            sample_based,
                                                                                                                            verbose)

    writeReplicationTimeData(outputDir,jobname,sample_based,decile_df_list,None,simNum2Type2DecileBasedAllChrAccumulatedCountDict,simNum2Sample2Type2DecileBasedAllChrAccumulatedCountDict)
    ###################################################################
    ############### Read MCF-7 RepliSeq Time data ends ################
    ###################################################################

    #######################################################################################################
    ############### Carry out Replication Time Data Analysis for each analysis type starts ################
    #######################################################################################################

    print('--- ReplicationTimeAnalysis ends')
    print('#################################################################################\n')

##################################################################
[![Docs](https://img.shields.io/badge/docs-latest-blue.svg)](https://osf.io/t6j7u/wiki/home/) 
[![License](https://img.shields.io/badge/License-BSD\%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build Status](https://travis-ci.com/AlexandrovLab/SigProfilerExtractor.svg?branch=master)](https://travis-ci.com/AlexandrovLab/SigProfilerExtractor)

# SigProfilerExtractor
SigProfilerExtractor allows de novo extraction of mutational signatures from data generated in a matrix format. 
The tool identifies the number of operative mutational signatures, their activities in each sample, and the probability 
for each signature to cause a specific mutation type in a cancer sample. The tool makes use of SigProfilerMatrixGenerator 
and SigProfilerPlotting. 

## INSTALLATION
In the commandline, please type the following line:
```
$pip install sigproextractor
```
Install your desired reference genome from the command line/terminal as follows (available reference genomes are: GRCh37, GRCh38, mm9, and mm10):
```
$ python
>> from SigProfilerMatrixGenerator import install as genInstall
>> genInstall.install('GRCh37')
```
This will install the human 37 assembly as a reference genome. You may install as many genomes as you wish.

open a python interpreter and import the SigProfilerExtractor module. Please see the examples of the functions. 

## FUNCTIONS

### importdata 
    
    
    Imports the path of example data.
    
    importdata(datatype="matobj")

    Example: 
    -------
    >>> from sigproextractor import sigpro as sig
    >>> path_to_example_table = sig.importdata("table")
    >>> data = path_to_example_table 
    This "data" variable can be used as a parameter of the "project" argument of the sigProfilerExtractor function.
    
    To get help on the parameters and outputs of the "importdata" function, please write down the following line:
    
    >>> help(sig.importdata)
        

### sigProfilerExtractor 
    
    
    Extracts mutational signatures from an array of samples.
    
    sigProfilerExtractor(input_type, out_put, project, refgen="GRCh37", genome_build = "GRCh37", startProcess=1, endProcess=10, totalIterations=8, 
    cpu=-1, hierarchy = False, mtype = ["default"],exome = False)
    
    
    Parameters
    ----------
    
    input_type: A string. Type of input. The type of input should be one of the following:
            - "vcf": used for vcf format inputs.
            - "table": used for table format inputs using a tab seperated file.
             
        
    out_put: A string. The name of the output folder. The output folder will be generated in 
    the current working directory. 
            
    input_data: A string. Name of the input folder (in case of "vcf" type input) or the 
    input file (in case of "table"  type input). The project file or folder should be inside the 
    current working directory. For the "vcf" type input,the project has to be a folder which will 
    contain the vcf files in vcf format or text formats. The "text"type projects have to be a file.   
            
    refgen: A string, optional. The name of the reference genome. The default reference genome is "GRCh37". 
    This parameter is applicable only if the input_type is "vcf".
    
    genome_build: A string, optional. The build or version of the reference signatures for the refgen. 
    The default genome build is GRCh37. If the input_type is "vcf", the genome_build automatically 
    matches the input refgen value.        
    
    startProcess: A positive integer, optional. The minimum number of signatures to be extracted. 
    The default value is 1. 
    
    endProcess: A positive integer, optional. The maximum number of signatures to be extracted. 
    The default value is 10.
    
    totalIterations: A positive integer, optional. The number of iteration to be performed to extract 
    each number signature. The default value is 8. However, we STRONGLY RECOMMEND TO USE 1000 
    iterations to get valid results. 
            
    cpu: An integer, optional. The number of processors to be used to extract the signatures. 
    The default value is -1 which will use all available processors. 
    
    hierarchy: Boolean, optional. Defines if the signature will be extracted in a hierarchical fashion. 
    The default value is "False".
    
    par_h = Float, optional. Ranges from 0 t0 1. Default is 0.90. Active only if the "hierarchy" is True. 
    Sets the cutoff to select the unexplained samples in a hierarchical layer based on the cosine similarity 
    between the original and reconstructed samples.  
    
    mtype: A list of strings, optional. The items in the list defines the mutational contexts to be considered 
    to extract the signatures. The default value is ["96", "DINUC" , "ID"], where "96" is the SBS96 context, "DINUC"
    is the DINULEOTIDE context and ID is INDEL context. Other options are: '6144', '384', '1536', '6', '24' .
            
    exome: Boolean, optional. Defines if the exomes will be extracted. The default value is "False".
    
    penalty: Float, optional. Takes any positive float. Default is 0.05. Defines the thresh-hold cutoff 
    to asaign signatures to a sample.    
    
    resample: Boolean, optional. Default is True. If True, add poisson noise to samples by resampling.  
    
```    
    Examples
    --------

    >>> from sigproextractor import sigpro as sig
    
    # to get input from vcf files
    >>> path_to_example_folder_containing_vcf_files = sig.importdata("vcf")
    >>> data = path_to_example_folder_containing_vcf_files # you can put the path to your folder containing the vcf samples
    >>> sig.sigProfilerExtractor("vcf", "example_output", data, startProcess=1, endProcess=3)
    
    Wait untill the excecution is finished. The process may a couple of hours based on the size of the data.
    Check the current working directory for the "example_output" folder.
    
    # to get input from table format (mutation catalog matrix)
    >>> path_to_example_table = sig.importdata("table")
    >>> data = path_to_example_table # you can put the path to your tab delimited file containing the mutational catalog matrix/table
    >>> sig.sigProfilerExtractor("table", "example_output", data, genome_build="GRCh38", startProcess=1, endProcess=3)
    
    To get help on the parameters and outputs of the "sigProfilerExtractor" function, please write down the following line:
    
    >>> help(sig.sigProfilerExtractor)
```
    
### GPU support

Sigprofilerextractor is GPU-enabled and can run on single or multi-GPU systems for significantly increased performance in most circumstances.

To use this feature set the GPU flag to True:
```
    sigProfilerExtractor(input_type, out_put, project, refgen="GRCh37", genome_build = "GRCh37", startProcess=1, endProcess=10, totalIterations=8, 
    cpu=-1, hierarchy = False, mtype = ["default"],exome = False, gpu=True)
```
If CUDA out of memory exceptions occur, it will be necessary to reduce the number of CPU processes used (the `cpu` parameter).

## For more information, help and examples, please visit: https://osf.io/t6j7u/wiki/home/

## COPYRIGHT
This software and its documentation are copyright 2018 as a part of the sigProfiler project. The SigProfilerExtractor framework is free software and is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## CONTACT INFORMATION
Please address any queries or bug reports to S M Ashiqul Islam (Mishu) at m0islam.ucsd.edu

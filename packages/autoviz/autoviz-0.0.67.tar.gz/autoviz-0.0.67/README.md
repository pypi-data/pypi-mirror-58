# AutoViz
Automatically Visualize any dataset, any size with a single line of code

        ##############################################################################
        #############       This is not an Officially Supported Google Product! ######
        ##############################################################################
        #Copyright 2019 Google LLC                                              ######
        #                                                                       ######
        #Licensed under the Apache License, Version 2.0 (the "License");        ######
        #you may not use this file except in compliance with the License.       ######
        #You may obtain a copy of the License at                                ######
        #                                                                       ######
        #    https://www.apache.org/licenses/LICENSE-2.0                        ######
        #                                                                       ######
        #Unless required by applicable law or agreed to in writing, software    ######
        #distributed under the License is distributed on an "AS IS" BASIS,      ######
        #WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#####
        #See the License for the specific language governing permissions and    ######
        #limitations under the License.                                         ######
        ##############################################################################
        ###########             AutoViz Class                                   ######
        ###########             by Ram Seshadri                                 ######
        ###########      AUTOMATICALLY VISUALIZE ANY DATA SET                   ######
        ###########            Version 0.0.67       date: 12/27/19              ######
        ##############################################################################
        ##### AUTOVIZ PERFORMS AUTOMATIC VISUALIZATION OF ANY DATA SET WITH ONE CLICK.
        #####    Give it any input file (CSV, txt or json) and AV will visualize it.##
        ##### INPUTS:                                                            #####
        #####    A FILE NAME OR A DATA FRAME AS INPUT.                           #####
        ##### AutoViz will visualize any sized file using a statistically valid sample.
        #####  - max_rows_analyzed = 150000 ### this limits the max number of rows ###
        #####           that is used to display charts                             ###
        #####  - max_cols_analyzed = 30  ### This limits the number of continuous  ###
        #####           vars that can be analyzed                                 ####
        #####  - COMMA is assumed as default separator in file. But u can change it.##
        #####  - Assumes first row as header in file but you can change it.      #####
        #####  - First instantiate an AutoViz class to  hold output of charts, plots.#
        #####  - Then call the Autoviz program with inputs as defined below.       ###
        ##############################################################################
        ##### This is the main calling program in AV. It will call all the load, #####
        ####  display and save rograms that are currently outside AV. This program ###
        ####  will draw scatter and other plots for the input data set and then   ####
        ####  call the correct variable name with add_plots function and send in  ####
        ####  the chart created by that plotting program, for example, scatter   #####
        ####  You have to make sure that add_plots function has the exact name of ####
        ####  the variable defined in the Class AV. If not, this will give an error.##
        ####  If verbose=0: it does not print any messages and goes into silent mode##
        ####  This is the default.                                               #####
        ####  If verbose=1, it will print messages on the terminal and also display###
        ####  charts on terminal                                                 #####
        ####  If verbose=2, it will print messages but will not display charts,  #####
        ####  it will simply save them.                                          #####
        ##############################################################################
 
## Installation
_Prerequsites_:
* [Anaconda](https://docs.anaconda.com/anaconda/install/)

To clone the AutoViz, it's better to create a new environment, and install the required dependencies:

To install from PyPi:

```bash
conda create -n <your_env_name> python=3.7 anaconda
conda activate <your_env_name> # ON WINDOWS: `source activate <your_env_name>` 
pip install autoviz
```

To install from source:

```bash
cd <AutoViz_Destination>
git clone git@github.com:AutoViML/AutoViz.git 
# or download and unzip https://github.com/AutoViML/AutoViz/archive/master.zip
conda create -n <your_env_name> python=3.7 anaconda
conda activate <your_env_name> # ON WINDOWS: `source activate <your_env_name>` 
cd AutoViz
pip install -r requirements.txt
```

## RUN AutoViz

* In the AutoViz directory, open a Jupyter Notebook and use this line to import the .py file:

```python
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
```

* Load a data set (any CSV or text file) into a Pandas dataframe or give the name of the path and filename you want to visualize. If you don't have a filename, you can simply assign the filename variable below to '' (empty string):

* Finally, call AutoViz using the filename (or dataframe) along with the separator (if any in file) and the name of the target variable in file or data frame. That's all. AutoViz will do the rest. You will see charts and plots on your screen.

```python
filename = ''
sep = ','
dft = AV.AutoViz(filename, sep, target, df, header=0, verbose=0, lowess=False, chart_format='svg', max_rows_analyzed=150000, max_cols_analyzed=30)
```

## DISCLAIMER

_**This is not an official Google product.**_

## LICENSE

Licensed under the Apache License, Version 2.0 (the “License”).

Powered by [Gitiles](https://gerrit.googlesource.com/gitiles/)| [Privacy](https://policies.google.com/privacy)

## SAMPLE TUTORIALS
Plot your dataset in a single line of code by [DataKnight](twitter.com/emeka_boris)

https://youtu.be/gtzouIxebd8

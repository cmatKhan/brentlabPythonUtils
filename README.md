# Installation

I would suggest building this "from source", which is an unclear way of saying, git clone this directory into whatever directory that you collect source code in (I use a directory called $HOME/code, something suggested to me and which I've found very useful), and then 'build' it from there (which, remember, means that python will place it in the PYTHONPATH).

```
cd /to/your/source_code_directory
git clone <the url to this repo>
```

Next, create the environment. Do this however you like, but I have found it easiest to store the environment in the actual package directory (actually, suggested in the conda docs, but very buried). To build the environment in the current directory, do this:

```
cd brentlab_utils # assuming your one directory up from this
conda create -p ./envs --file requirements.txt
```
Next, activate the environment:
```
conda activate ./envs # assuming your still in the same directory where you made the environment
```
Finally, install the package into the python library of this new environment
```
pip install -e . # the -e flag installs the 'build package' as a symlink, so your edits in the source code are immediately available in the built code. I typically re-build after making changes, though
```
Now you can launch a python session and do something like this:
```
from brentlab_utils import gene_conversion
gene_conversion.translateGeneIdentifiers('scerevisiae', 'ENTREZGENE_ACC', ["YDR189W", "YER105C", "YGR005C", "YKL062W", "YPR181C", "YPL218W", "YHR046C"])
  converted                                        description incoming  n_converted  n_incoming    name namespaces    query
0    851770  Hydrophilic protein involved in ER/Golgi vesic...  YDR189W            1           1    SLY1  ENSG,ENSP  query_1
1    856842  Subunit of the inner ring of the nuclear pore ...  YER105C            1           2  NUP157  ENSG,ENSP  query_1
2    852888  TFIIF (Transcription Factor II) middle subunit...  YGR005C            1           3    TFG2  ENSG,ENSP  query_1
3    853803  Stress-responsive transcriptional activator; a...  YKL062W            1           4    MSN4  ENSG,ENSP  query_1
4    856311  GTPase-activating protein, stimulates the GTPa...  YPR181C            1           5   SEC23  ENSG,ENSP  query_1
5    855883  ARF family GTPase; component of the COPII vesi...  YPL218W            1           6    SAR1  ENSG,ENSP  query_1
6    856442  Inositol monophosphatase; involved in biosynth...  YHR046C            1           7    INM1  ENSG,ENSP  query_1
```
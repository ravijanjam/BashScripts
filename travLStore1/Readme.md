### Counting files in any directory

To loop through all the directories on the LServer and get the file count for a specific set of filters based on extensions type, date range and excluded directory list. The script also writes the output to *fileInfo.dat*, which can be scraped for any further information. 

**Filters** :
```excluded directories, startDate, endDate, starting path```

The inputs to the file are the following and given as key-value pairs:

| **Variable** | **Explanation** | **Example** |
|--- |--- |---|
|iPath | Starting path to look up for files recursively | ```"~/your/path/to/images/```"|
|rExt | List of file extensions to look for per directory | ```"jpg tex iso"``` |
|sDate | Starting date | ```2012-01-01```|
|eDate | Ending date | ```2019-12-01```|
|dExcl | Key words to exclude in the directory search path | ```logs videos``` |

The results look as shown below.

```
Path: /a1/b1/c1/d1
sh:1, size:0.00155735 MB        C:3, size:0.00381374 MB

Path: /a2/b2/c2/d2
sh:1, size:0.00155735 MB        C:3, size:0.00381374 MB
png:9, size:0.117346 MB

Path: /home/bokadia/CMS/CMSHIResearch/pPbWithAndWithoutCuts
```

For a list of examples, scroll to the end of the [script](https://github.com/ravijanjam/BashScripts/blob/master/travLStore1/fileExtPerDir1.sh)

**Note**: The order of the key-value pairs should be in the same sequence as given in the script. 
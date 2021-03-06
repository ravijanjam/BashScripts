### LStoreFileCount.sh

To loop through all the directories on the LServer and get the file count for a specific set of filters based on extensions type, date range and excluded directory list. The script also writes the output to *fileInfo.dat*, which can be scraped for any further information. 

**Filters** :
```file-extension list, excluded directories, startDate, endDate, starting path```

The inputs to the file are the following and given as key-value pairs:

| **Variable** | **Explanation** | **Example** |
|--- |--- |---|
|iPath | Starting path to look up for files recursively | ```"~/your/path/to/images/```"|
|rExt | List of file extensions to look for per directory | ```"jpg tex iso"``` |
|sDate | Starting date | ```2012-01-01```|
|eDate | Ending date | ```2019-12-01```|
|dExcl | Key words to exclude in the directory search path | ```logs videos``` |

For a list of examples, scroll to the end of the [LStoreFileCount.sh](https://github.com/ravijanjam/BashScripts/blob/master/travLStore/LStoreFileCount.sh)

**Note**: The order of the key-value pairs should be in the same sequence as given in the script. 

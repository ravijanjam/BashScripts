### LStoreFileCount.sh

To loop through all the directories on the LServer and get the file count for a specific set of extensions and the total number of files per extension in between a given range of dates. The script also writes the output to *fileInfo.dat*, which can be scraped for any further information. 

**Output**
Eg: ```file-extension list, excluded directories, startDate, endDate, starting path```

The inputs to the file are the following and they have to be in the same order, and given as key-value pairs:

| **Variable** | **Explanation** | **Example** |
|--- |--- |---|
|iPath | Starting path to look up for files recursively | ```"~/your/path/to/images/```"|
|rExt | List of file extensions to look for per directory | ```"jpg tex iso"``` |
|sDate | Starting date | ```2012-01-01```|
|eDate | Ending date | ```2019-12-01```|
|dExcl | Key words to exclude in the directory search path | ```logs videos``` |

For a list of examples, scroll to the end of the [LStoreFileCount.sh](https://github.com/ravijanjam/BashScripts/blob/master/travLStore/LStoreFileCount.sh)

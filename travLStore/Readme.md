### LStoreFileCount.sh

To loop through all the directories on the LServer and get the file count for a specific set of extensions and the total number of files per extention. The script also writes the output to *fileInfo.dat*, which can be scraped for any further information. 

**Output**
Eg: ```file-extension list, excluded directories, startDate, endDate, starting path```

The inputs to the file are the following and they have to be in the same order, and given as key-value pairs:

| **Variable** | **Explanation** |
|-- |-- |
|iPath | Starting path to look up for files recursively |


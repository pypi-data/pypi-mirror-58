# mergecat

Automatic voice line clip extractor

## How to use

1. Install the package via `pip install mergecat`
2. Create a timing file in a format like this (using seconds)  
   Example:
   ```
   2 24
   60 75
   92 103
   128 135
   ```
3. Run mergecat via `mergecat video_file timing_file`  
   Example: `mergecat something.mp4 timing.txt`
   
## Goals

- Automate the process instead of requiring timing files
- Allow batch processing
- Handle temporary file cleanup better
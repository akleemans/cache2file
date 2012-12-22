cache2file
==========

Converts a HTML cache file from chrome into the original file.
Access your cache with `chrome://cache/` and save the file you want to convert with right click -> save as.
Currently default target file format is mp3.

For more information, see [this blog post](http://www.kleemans.ch/if-you-can-stream-it-you-can-download-it)

## Use

    python cache2file.py filename.html

## Note
Should also work with other format where a separate header is shown on the cache page. For other files you would have to decide where the _real_ data starts, as this is currently done with a simple HTML tag search.

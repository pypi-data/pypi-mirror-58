<a href="https://cognite.com/">
    <img src="https://raw.githubusercontent.com/cognitedata/cognite-python-docs/master/img/cognite_logo.png" alt="Cognite logo" title="Cognite" align="right" height="80" />
</a>

# CDF IFS file extractor
[![build](https://webhooks.dev.cognite.ai/build/buildStatus/icon?job=github-builds/cdf-ifs-file-extractor/master)](https://jenkins.cognite.ai/job/github-builds/job/cdf-ifs-file-extractor/job/master/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

**In progress**

## General
The cdf-ifs-file-extractor allows continuous uploading, changing and deletion of files stored in a local directory
and connect those files to the corresponding assets with some metadata.
Running on a continuous schedule the extractor moves old mapping_files into an Archive and uploads new files if it is
fed with a new mapping file. Feedback of unsuccessful upload attempts is given via the two files unknown_files.csv and
unknown_assets.csv.

## Structure of the Mapping file
The extractor expects the mapping file to have a specific format. This requires the following columns:
- FILE_NAME
- DOC_NO
- DOC_REV
- DOC_SHEET
- DOC_CLASS
- DOC_CLASS_NAME
- DOC_FORMAT
- DOC_FORMAT_NAME
- DOC_TITLE
- DOC_RESP_SIGN
- LETTER_DATE
- LAST_UPDATED: to be checked if this column is really included
- DOC_REFERENCE_OBJECT
- OPERATION: allows one of the three values N, C, D to upload a new file or change or delete an existing one

## Requirements local directory
The local directory needs to contain
- the desired files to operate on
- a folder with the name Archive
- the mapping file

## Parameters
The parameters for the function are
- project:
- api_key_name: name of the environment variable storing the api key
- base_url
- client_name
- client_timeout
- log_path
- log_level
- path: path of the local directory
- mapping_file: file name

## Feedback of the extractor
For non developing users the extractor provides feedback to the user for unsuccessful file operation attempts in two
cases
- The asset_id specified in the mapping file does not exist: these ids are stored together with the corresponding file
name in unknown_assets.csv
- The specified file does not exist: unknown_files.csv

Both files will be created in the end of a run of the extractor and archived as soon as the extractor is running the
next time.



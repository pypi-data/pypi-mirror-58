[![Build Status](https://travis-ci.org/Cloudzero/dynotool.svg?branch=master)](https://travis-ci.org/Cloudzero/dynotool)

# Dyn-O-Tool

Tools for easier living with AWS DynamoDB


Features
--------

* Get a quick informational summary of any table
* Quickly grab 10 records from any table
* Export all or a subset of any DynamoDB table to CSV

Install
-------

    pip install dyn-o-tool
    
Usage
-----

    CloudZero Dyn-O-Tool!
    
    Tools for making life with DynamoDB easier
    
    Usage:
        dynotool list [--profile <name>]
        dynotool info <TABLE> [--profile <name>]
        dynotool head <TABLE> [--profile <name>]
        dynotool copy <SRC_TABLE> <DEST_TABLE> [--profile <name>]
        dynotool export <TABLE> [--format <format> --file <file> --profile <name>]
        dynotool import <TABLE> --file <file> [--profile <name>]
        dynotool wipe <TABLE> [--profile <name>]
        dynotool truncate <TABLE> [--filter <filter>] [--profile <name>]
    
    
    Options:
        -? --help               Usage help.
        list                    List all DyanmoDB tables currently provisioned.
        info                    Get info on the specified table.
        head                    Get the first 20 records from the table.
        copy                    Copy the data from SRC TABLE to DEST TABLE
        export                  Export TABLE to JSON
        import                  Import file into TABLE
        wipe                    Wipe an existing table by recreating it (delete and create)
        truncate                Wipe an existing table by deleting all records
        --format <format>       JSON or CSV [default: json]
        --file <file>           File to import or export data to, defaults to table name.
        --profile <profile>     AWS Profile to use (optional) [default: default].
        --filter <filter>       A filter to apply to the operation. The syntax depends on the operation.


Copyright &copy; 2020 CloudZero, Inc.
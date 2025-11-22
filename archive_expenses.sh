#!/bin/bash

echo " ===ARCHIVE EXPENSES SCRIPT==="

#check if archives directory exists
if [ ! -d "archives" ]; then
echo "Archives folder not found. Creating it now!"
mkdir archives
echo " Archives folder created."
fi  

# Ask user for the date
echo "Enter the date of the expense file you want to archive (YYYY-MM-DD): "
read file_date

#create the filename
filename="expenses_${file_date}.txt"

#check if the file exists
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' does not exist."
    exit 1
fi

#moves the file to archives 
mv "$filename" archives/
echo "File '$filename' moved to archives/"

#log the operation 
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
echo "$timestamp - Archived file: $filename" >> archive_log.txt
echo "Action logged in archive_log.txt"


echo ""
echo "Do you want to search for an archived file? (y/n)"
read search_choice

if [ "$search_choice" = "y" ]; then
    echo "Enter the date to search (YYYY-MM-DD): "
    read search_date

    search_filename="archives/expenses_${search_date}.txt"

    if [ -f "$search_filename" ]; then
        echo ""
        echo "=== Archived File Found ==="
        cat "$search_filename"
    else
        echo "No archived file found for that date."
    fi
fi

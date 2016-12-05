echo "Running on directory: $1"

echo "Files in the directory:"
for file in $1/*.py
do
   wc -l $file
done

#!/bin/bash
source ../config/env.sh

# output
target=../exe
[ -d $target ] && rm -r $target
mkdir -p $target

# create setup.py
echo "from distutils.core import setup" >> setup.py
echo "from Cython.Build import cythonize" >> setup.py
echo "setup( name = 'pjct', " >> setup.py
echo "    ext_modules = cythonize([ " >> setup.py
files=$(ls *.py)
for file in $files; do
   if [ "$file" != "real.py" -a "$file" != "setup.py" ]; then
      echo "    '"$file"'," >> setup.py
   fi
done
echo "     ])," >> setup.py
echo "     )" >> setup.py

# cython
python setup.py build_ext 
mv build/lib.linux-x86_64-3.6/*.so $target

# clean
rm -r ./build 2>/dev/null 
rm -r ./*.c   2>/dev/null
rm setup.py 2>/dev/null

# main() 
cp real.py load* $target

# rename
cd $target
rename .cpython-36m-x86_64-linux-gnu. . * 



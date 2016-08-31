rm -rf release
cp -r src release
cd release

export PYTHONPATH=$PYTHONPATH:data
python server_main.py

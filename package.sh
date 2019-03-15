rm -rf target *.zip
# rm -rf dependencies target *.zip

mkdir target
# mkdir dependencies target

# pip install -r requirements-aws.txt -t dependencies

# cp -r dependencies/* target
cp volunteer_tracking/*.py target
mkdir target/psycopg2
cp -r psycopg2-3.6/* target/psycopg2

python -m zipfile -c volunteer_tracking_code.zip target/*

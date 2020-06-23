cd Desktop/iodata

head -n 1 iodata.csv >> attribute_name.txt

attribute_name=$(cat attribute_name.txt)

sudo -u postgres psql << EOF
drop table if exists io table;
create table iotable  (
  $attribute_name
)
EOF

-- so y= axij + xi1j1 +  xi2j2 ... xinjn in relational terms given the model has two basic cases
-- axij is select a(i) from iotable where name='j' so the amount of i that goes into j 
-- direct is just select select a(i) where name=i; e.g. :
select farms from iotable where name='Farms';
--indirect is just select (i) where name=j; e.g. : 
select Forestry_fishing_related_activities from iotable where name='Farms';

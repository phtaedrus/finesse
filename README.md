# FINESSE

## RUN

I. Run the following commands in your terminal:

`$ pip install requirements.txt`

`$ python ddl.py`


Now a new sqlite3 db file called *finesse_db* will be created in local 
directory.

II. Next
 
`$ python main.py`

The local database (or db wherever the connection target is) should now 
be loaded with relevant datatypes and values.


#### Assumptions, Findings, and Architecture Thesis
- This data engineering project intends build an interesting framework that 
doesn't narrow the scope of the future dev and allows for ad-hoc analysis
with super fast turnaround times. However, leaving functional pipelines
 in place is also is also the central thesis here. 
##### Architecture

![Diagram](img/Finesse_POC_Architecture.png)


1. With the release of 
[Spark3.0](https://spark.apache.org/releases/spark-release-3-0-0.html)
and additional support and distributed pandas dataframes, versatility continues
 to reign paramount in data utilities. So SQL and Pandas
may not both be needed in this context, however, together they provide a 
duo support system and modular framework that removes the bulk of 
processing from the (presumed lightweight database) relational store.

2. The scalability of this architecture is a major factor in why 
    a declarative and object oriented structure has been used. 
    
    Attributes may be added to the class after its construction, and they will be added to the underlying Table and mapper() definitions as appropriate:
    ```
    SomeClass.data = Column('data', Unicode)
    SomeClass.related = relationship(RelatedInfo)
   ```
Because of this flexibility, data can be modified at the pre-processing (pandas)  
level or with SQL dialect after the load.



##### There is some new and very cool tech called [Datasette](https://datasette.readthedocs.io/en/stable/index.html) 
 It is  a lightweight tool that sits (alongside) flat files 
that allows for quick data 
interaction and analysis. Depending on the volume, velocity, and variety
of our data sources. This may get us insights significantly faster 
while allowing us time to build towards a production environment. 

Example with our data:

- https://glitch.com/~husky-thundering-yorki

![ExampleScreenshot](img/screenshot.png)

##### Future Pull Requests
- ~~move main to a separate main.py~~  
- Single Responsibility-
- consider process_data.py --> to custom_data_frame.py
- consider moving load_to_sql --> to seperate load_to_sql.py 

1. get service class for (get) building dataframe input:source(csv), output:pd.Dataframe()

2. load service class for process dataframe. input:pd.Dataframe(), output:pd.Dataframe()

3. ~~normalize_data service~~

4. Unit tests

5. `$ python etl.py`



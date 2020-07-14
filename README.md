# FINESSE

## RUN
I. Run the following commands in your terminal:

`$ python ddl.py`


Now a new sqlite3 db file called *finesse_db* will be created in local 
directory.

II. Next
 
`$ python process_data.py`

The local database (or db wherever the connection target is) should now 
be loaded with relevant datatypes and values.

III. 


#### Assumptions, Findings, and Architecture Thesis

##### Architecture

1. With the release of 
[spark3.0]("https://spark.apache.org/releases/spark-release-3-0-0.html")
and additional support and distributed pandas dataframes, I wanted to 
build something 
I think it's especially important to build a maleable structure. SQL and Pandas
may not actually be needed in this context, however, together they provide

2. The scalability of this architecture is a major factor in why 
    a declarative and object oriented structure has been used. 
    
    Attributes may be added to the class after its construction, and they will be added to the underlying Table and mapper() definitions as appropriate:
    ```
    SomeClass.data = Column('data', Unicode)
    SomeClass.related = relationship(RelatedInfo)
   ```
3.  

3. There is some new and very cool tech called 
[Datasette](https://datasette.readthedocs.io/en/stable/index.html) 
, it's a lightweight
tool that sits (alongside) flat files that allows for quick data 
interaction and analysis. Depending on the volume, velocity, and variety
of our data sources. This may get us insights significantly faster 
while allowing us time to build towards a production environment. 

Example with our data:

- https://glitch.com/~husky-thundering-yorki

![ExampleScreenshot](img/screenshot.png)






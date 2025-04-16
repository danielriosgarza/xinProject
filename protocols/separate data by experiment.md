## **separate data by experiment**
1. run 《scp pioreactor@100.117.2.9:/home/pioreactor/.pioreactor/storage/pioreactor.sqlite mCPU_db_day.sqlite》 replace the date.
2. Connect to the reactor and run 《sqlite3 mCPU_db_14_04_25.sqlite》 to enter the database; 
3.《.tables》 to see if there are any data names in the database that are needed; 
4. 《SELECT *
    FROM od_readings 
    WHERE experiment = 'experiment name' 
    LIMIT 10;》 display data, used to confirm that the data is correct.
5. 《.headers on》
   《.mode csv》
   《.output file name.csv》
   《SELECT * FROM od_readings WHERE experiment = 'Culture_OD0.05_workers0456 10-04-25';》
   《.output stdout》 Create a new csv file and copy the experimental data associated with the selected experiment name into this new csv file.
6. run 《scp pioreactor@100.117.2.9:/home/pioreactor/file name.csv Culture_day.csv》 Download this csv file to the desired location.

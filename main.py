import psycopg2

#Conecting to Database
con = psycopg2.connect(
database = "movies",
user = "postgres",
password="1234",
host = "localhost",
port = "5432"

)

print('Sucess')


cur = con.cursor()
cur.execute("select * from public.func_csv fc")
rows = cur.fetchall()



print(rows)
#cur.close()
#con.close()


#------------------------------------------------------------------------------------------------------------------------------------------------#



with open("sample.csv", 'w', encoding='UTF-8') as fd:
     cur.copy_expert("COPY public.func_csv TO STDOUT WITH (FORMAT CSV,  HEADER TRUE)", fd)


# copy_sql = """
#            COPY table_name FROM stdin WITH CSV HEADER
#            DELIMITER as ','
#            """
# with open(path, 'r') as f:
#     cur.copy_expert(sql=copy_sql, file=f)
#     conn.commit()
#     cur.close()
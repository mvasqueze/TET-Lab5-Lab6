# TET-Lab5-Lab6

#Lab5
![image](./Imágenes/1.png)
Creación del bucket

![image](./Imágenes/2.png)
Creación de las carpetas

![image](./Imágenes/3.png)
Creación de la key

![image](./Imágenes/4.png)
Cluster creado

![image](./Imágenes/5.png)
Creación del perfil y verificación de clreación del S3

![image](./Imágenes/6.png)
Creación y subida del .txt

![image](./Imágenes/7.png)
Segundo directorio creado desde la consola

![image](./Imágenes/8.png)
Constancia de la creación del directorio

![image](./Imágenes/9.png)
Segundo archivo ya existente en la consola

![image](./Imágenes/10.png)
Constancia de creación desde la interfaz web

#Laboratorio 6

#Reto 1

![image](./Imágenes/11.png)
Instalación del CLI en el local

![image](./Imágenes/12.png)
Cambio el config.txt t credentials.txt en la carpeta de AWS por los datos del CLI

![image](./Imágenes/13.png)
Creación del cluster (Development Cluster)

#Reto 2

![image](./Imágenes/14.png)
Abro otra terminal, conecto con el nodo principal del cluster y le instalo git

![image](./Imágenes/15.png)
Clono el respectivo repositorio

![image](./Imágenes/16.png)
Luego de corregir un error en el código, se muestran los datos del archivo

![image](./Imágenes/17.png)
Resultado luego de correr Mr. Job

![image](./Imágenes/18.png)
Luego de copiar los datasets en el EMR, estos son entregado al Mr. Job y este es el output que se almacena en el EMR.

#Reto 3

##1.1
Usando el comando
python salarioPromSecEc.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-1

Se obtuvieron los siguientes outputs:
![image](./Imágenes/a.png)


##1.2
Usando el comando
 python salarioProm.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-2
 
 ![image](./Imágenes/b.png)

## 1.3

Usando el comando
 python secEmp.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user
/admin/p1-3

![image](./Imágenes/c.png)

#Reto 2

## 2.1
Con el comando

 python diaMinMax.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/admin/p2-1
 
 ![image](./Imágenes/d.png)

## 2.2
Con el comando 
 python accUpDown.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///us
er/admin/p2-2

![image](./Imágenes/e.png)

## 2.3
Con el comando
python blackDay.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///use
r/admin/p2-3

![image](./Imágenes/f.png)

#Reto 3

##3.1
Con el comando
 python pelUsuarioRating.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-1
 
 ![image](./Imágenes/g.png)

##3.2
Con el comando
 python masPel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user
/admin/p3-2

![image](./Imágenes/h.png)

##3.3
Con el comando
python menosPel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///us
er/admin/p3-3

![image](./Imágenes/i.png)

##3.4
Con el comando

python singlePel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///u
ser/admin/p3-4

![image](./Imágenes/j.png)

##3.5
Con el comando
 python peorProm.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///us
er/admin/p3-5

![image](./Imágenes/k.png)

##3.6
Con el comando
python mejorProm.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///u
ser/admin/p3-6

![image](./Imágenes/l.png)

##3.7
Con el comando
 python genero.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user
/admin/p3-7

![image](./Imágenes/m.png)

 

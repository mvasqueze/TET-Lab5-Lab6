# TET-Lab5-Lab6

#Lab5
![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/9076422f-dd08-4a20-852a-e5c0fe5faa1f)
Creación del bucket

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/b5a83f3e-0af0-4ed6-b8fb-1e3d4923936b)
Creación de las carpetas

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/fe169ff8-c893-49c0-aa46-fb946c2965fd)
Creación de la key

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/af58b6ad-822e-485f-9038-40aba164f0cb)
Cluster creado

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/979b904e-368e-4f33-9ee8-b0492f869a48)
Creación del perfil y verificación de clreación del S3

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/56c02aa3-0315-494b-8590-b6f3d3d2d3aa)
Creación y subida del .txt

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/dffb2105-ad2c-4d79-be74-4dc04e18f1ff)
Segundo directorio creado desde la consola

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/b2f11d16-8e8c-4f81-aade-6a0d8662c16a)
Constancia de la creación del directorio

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/463d0ed6-9b51-4599-9b69-60a4e56da19a)
Segundo archivo ya existente en la consola

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/5d48e6f3-e4b8-4146-8c43-d03137076245)
Constancia de creación desde la interfaz web

#Laboratorio 6

#Reto 1

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/19eea52e-c3b4-4aed-b478-a915856d7a5a)
Instalación del CLI en el local

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/63f5ed41-da16-4aa4-9650-5fc8dd9e134c)
Cambio el config.txt t credentials.txt en la carpeta de AWS por los datos del CLI

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/9ec2c467-4f31-487c-a30e-67ed07be21b0)
Creación del cluster (Development Cluster)

#Reto 2

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/1628b7cf-fca2-44e3-891c-cf9e244be29d)
Abro otra terminal, conecto con el nodo principal del cluster y le instalo git

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/b89557ec-4766-4ff6-a489-2346b2767f65)
Clono el respectivo repositorio

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/4d0a16c2-7f47-4126-b8ce-26da521295b0)
Luego de corregir un error en el código, se muestran los datos del archivo

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/61ce4af0-a9fa-49bb-b474-858f2df7f986)
Resultado luego de correr Mr. Job

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/8b9163d8-c0ba-48c2-8e4a-9001a69969ab)
Luego de copiar los datasets en el EMR, estos son entregado al Mr. Job y este es el output que se almacena en el EMR.

#Reto 3

##1.1
Usando el comando
python salarioPromSecEc.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-1

Se obtuvieron los siguientes outputs:
![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/bce5248e-54e3-4a06-adc7-99b463f9fae9)


##1.2
Usando el comando
 python salarioProm.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-2
 
 ![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/dbb4e1c3-b0cb-4646-ba61-766530f94990)

## 1.3

Usando el comando
 python secEmp.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user
/admin/p1-3

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/abe618f1-3af1-443c-ba6b-cd305c89be17)

#Reto 2

## 2.1
Con el comando

 python diaMinMax.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/admin/p2-1
 
 ![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/7f57eb29-9a6a-4004-a52f-078a92bf3f78)

## 2.2
Con el comando 
 python accUpDown.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///us
er/admin/p2-2

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/4350b9c5-9af4-4417-b027-52dbfa7a3bb8)

## 2.3
Con el comando
python blackDay.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///use
r/admin/p2-3

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/4b9647fd-42f5-460a-abfd-dd26573688cf)

#Reto 3

##3.1
Con el comando
 python pelUsuarioRating.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-1
 
 ![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/4978c24c-67cf-46de-bb83-a923a452036a)

##3.2
Con el comando
 python masPel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user
/admin/p3-2

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/ff41df15-8e7c-4b8a-87b7-3d136c22873d)

##3.3
Con el comando
python menosPel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///us
er/admin/p3-3

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/3e57d00d-f9af-48fe-92f1-03880ca66167)

##3.4
Con el comando

python singlePel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///u
ser/admin/p3-4

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/04747ca3-91e0-42da-81fe-cb0c8f0d2eb2)

##3.5
Con el comando
 python peorProm.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///us
er/admin/p3-5

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/d5818587-1676-4a42-81b5-64c201874700)

##3.6
Con el comando
python mejorProm.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///u
ser/admin/p3-6

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/ba87d5aa-e442-48c8-bd16-4d86b37104bb)

##3.7
Con el comando
 python genero.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user
/admin/p3-7

![image](https://github.com/mvasqueze/TET-Lab5-Lab6/assets/68928428/cdba5145-0e9c-4081-ad44-8a296e170d6c)

 

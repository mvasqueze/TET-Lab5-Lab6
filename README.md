# Lab5

## Creación del bucket y sus carpetas
![image](./Imágenes/1.png)

![image](./Imágenes/2.png)

## Creación de la key
![image](./Imágenes/3.png)
Creación de la key

## Creación del cluster
![image](./Imágenes/4.png)

## Ingreso a la interfez web, creación del perfil y constancia de la creación del S3
![image](./Imágenes/5.png)

## Creación y uploading via interfaz web del .txt
![image](./Imágenes/6.png)

## Creación del segundo directorio a través de la consola
![image](./Imágenes/7.png)

El comando usado para la creación del directorio es es siguiente:

```
hdfs dfs -mkdir /user/admin/test2
$ hdfs dfs -ls /user/admin
```

Constancia de la creación del directorio desde la interfaz web
![image](./Imágenes/8.png)

## Creación y subida del segundo archivo

Segundo archivo ya existente en la consola
![image](./Imágenes/9.png)

El archivo fue creado con:
```
$ sudo nano file2.txt
```

Y fue trasladado a la carpeta deseada con:
```
hdfs dfs -copyFromLocal file2.txt /user/admin/test2/
```

Constancia de creación desde la interfaz web
![image](./Imágenes/10.png)


# Laboratorio 6

## Reto 1
Inicialmente, abro una consola de powershell y ejecuto el comando 

```
pip install awscli
```
![Instalación de CLI en el local](./Imágenes/11.png)

Una vez instalado el CLI, ingreso a la ruta donde está almacenado (en mi caso This PC/Users/MiUsuario/AWS) y modifico el archivo config.txt y credentials.txt.

### Credentials 
Ingreso a la página principal del laboratorio, lo inicio y doy clic en "AWS details" y luego en el botón "Show".

![Credentials](./Imágenes/aws.png)

La información contenida en en apartado "AWS CLI" debe ser copiada y pegada en credentials.txt
![copypaste](./Imágenes/creden.png)

### Config

Posteriormente, en el mismo apartado del pánel del laboratorio, después de las credenciales se encuentra la región. 
![zona](./Imágenes/zona.png)

Es necesario incluir la información de la región en el archivo config.txt:

```
[default]
region = us-east-1
```

Quedarían los archivos de la siguiente manera:
![image](./Imágenes/12.png)

Posteriormente, se corre el siguiente comando:

```
aws emr create-cluster --release-label emr-6.10.0 --instance-type m4.large --instance-count 3 --log-uri s3://mvasqueze-lab-emr/logs --use-default-roles --ec2-attributes KeyName=emr-key,SubnetId=subnet-0f42d1e0fb0273f9d --no-termination-protected
```
Los espacios designados para la URI, el KeyName y Subnet ID deben ser reemplazados en concordancia con el S3, el .pem y una de las subnets que se posean.

Tras ejecutar dicho comando, debe aparecer algo similar a lo siguiente en consola:
![consola](./Imágenes/consola.png)

Esto indica que el cluster de tres instancias fue creado correctamente. A continuación, verificamos en la consola de AWS:
![Creación del cluster (Development Cluster)](./Imágenes/13.png)


## Reto 2

![image](./Imágenes/14.png)
Abro otra terminal, conecto con el nodo principal del cluster y le instalo git

```
ssh -i emr—key.pem hadoop@ec2-44-192-72-104.compute—l.amazonaws.com
sudo yum install git
```

Posteriormente, clono el respectivo repositorio
![image](./Imágenes/15.png)

```
git clone https://github.com/ST0263/st0263-2023-1.git
```
Luego, luego de modificar wordcount local debido a un error con las minúsculas, ejecuto wordcount-local sobre el dataset gutemberg-small

```
cd st0263-2023-1/Laboratorio\ N6-MapReduce/wordcount/
python wordcount-local.py /home/hadoop/st0263-2023-1/datasets/gutenberg-small/*.txt | sudo tee salida-serial.txt > /dev/null
more salida-serial.txt
```
El output fue el siguiente:
![image](./Imágenes/16.png)

A continuación vamos a correr MrJob en local, para lo cual necesitamos instalar python y la librería de MrJob:

```
sudo yum install python3-pip
sudo pip3 install mrjob
cd wordcount
python wordcount-mr.py ./datasets/gutenberg-small/*.txt
```

Resultado luego de correr Mr. Job en local.
![image](./Imágenes/17.png)


Luego de copiar los datasets en el EMR, estos son entregado al Mr. Job y este es el output que se almacena en el EMR.
![image](./Imágenes/18.png)

## Reto 3
Para realizar correctamente los tres apartados del tercer reto es necesario clonar el presente repositorio. El repositorio fue clonado en la máquina que se usó para llevar a cabo los tutoriales anteriores:

```
git clone https://github.com/mvasqueze/TET-Lab5-Lab6.git
cd TET-Lab5-Lab6
```

Hay una carpeta para cada uno de los siguientes apartados que contiene los códigos necesarios para obtener los resultados esperados.

### Ejercicios 1
Entrar a la carpeta P1 dentro del repositorio.
```
cd P1
```

#### 1.1
Usando el siguiente comando es posible obtener el salario promedio por sector económico; los outputs serán almacenados en la carpeta p1-1 que está incluída en la carpeta admin del cluster:
```
python salarioPromSecEc.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-1
```
Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p1-1/part-0000
hdfs dfs -cat /user/admin/p1-1/part-0001
hdfs dfs -cat /user/admin/p1-1/part-0002
```

Se obtuvieron los siguientes outputs:
![image](./Imágenes/a.png)


####  1.2
Usando el siguiente comando es posible obtener el salario promedio por empleado, representado por su ID; los outputs serán almacenados en la carpeta p1-2 que está incluída en la carpeta admin del cluster:

```
 python salarioProm.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-2
```
 
Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p1-2/part-0000
hdfs dfs -cat /user/admin/p1-2/part-0001
hdfs dfs -cat /user/admin/p1-2/part-0002
``` 

Se obtuvieron los siguientes outputs
 ![image](./Imágenes/b.png)

#### 1.3

Usando el siguiente comando es posible obtener la cantidad de sectores económicos correspondientes a cada empleado, representado por su ID; los outputs serán almacenados en la carpeta p1-3 que está incluída en la carpeta admin del cluster:
```
 python secEmp.py hdfs:///user/admin/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/p1-3
```
Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p1-3/part-0000
hdfs dfs -cat /user/admin/p1-3/part-0001
hdfs dfs -cat /user/admin/p1-3/part-0002
``` 

Se obtuvieron los siguientes outputs
![image](./Imágenes/c.png)

### Ejercicios 2
Entrar a la carpeta P2 dentro del repositorio.
```
cd ..
cd P2
```

#### 2.1
Usando el siguiente comando es posible obtener, para cada una de las empresas, el día en que más valor tenían sus acciones y el día en que menos valor tenían ; los outputs serán almacenados en la carpeta p2-1 que está incluída en la carpeta admin del cluster:

```
 python diaMinMax.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/admin/p2-1
```
 
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p2-1/part-0000
hdfs dfs -cat /user/admin/p2-1/part-0001
hdfs dfs -cat /user/admin/p2-1/part-0002
``` 
Se otuvieron los siguientes outputs: 
 ![image](./Imágenes/d.png)

#### 2.2
Usando el siguiente comando es posible obtener el comportamiento de las acciones de cada una de las empresas (si suben, bajan o se mantienen estables), representadas por su nombre; los outputs serán almacenados en la carpeta p2-2 que está incluída en la carpeta admin del cluster:
```
python accUpDown.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/admin/p2-2
```
Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p2-2/part-0000
hdfs dfs -cat /user/admin/p2-2/part-0001
hdfs dfs -cat /user/admin/p2-2/part-0002
``` 
Se otuvieron los siguientes outputs:
![image](./Imágenes/e.png)

#### 2.3
Usando el siguiente comando es posible obtener el día negro, es decir, el día en que las acciones tuvieron el valor más bajo; los outputs serán almacenados en la carpeta p2-3 que está incluída en la carpeta admin del cluster:

```
python blackDay.py hdfs:///user/admin/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/admin/p2-3
```
Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p2-3/part-0000
hdfs dfs -cat /user/admin/p2-3/part-0001
hdfs dfs -cat /user/admin/p2-3/part-0002
``` 
Se otuvieron los siguientes outputs:
![image](./Imágenes/f.png)

### Ejercicios 3

Entrar a la carpeta P3 dentro del repositorio.
```
cd ..
cd P3
```

#### 3.1
Usando el siguiente comando es posible obtener el promedio de los rating (calificación de 0 a 5.0) dados por cada usuario (representado por su ID) y el número de ratings que ha hecho; los outputs serán almacenados en la carpeta p3-1 que está incluída en la carpeta admin del cluster:
```
 python pelUsuarioRating.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-1
```
Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-1/part-0000
hdfs dfs -cat /user/admin/p3-1/part-0001
hdfs dfs -cat /user/admin/p3-1/part-0002
``` 
Se otuvieron los siguientes outputs: 
 ![image](./Imágenes/g.png)

##3.2
Usando el siguiente comando es posible obtener el día en que el se vieron más películas, y la cantidad de películas vistas; los outputs serán almacenados en la carpeta p3-2 que está incluída en la carpeta admin del cluster:
```
python masPel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-2
```
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-2/part-0000
hdfs dfs -cat /user/admin/p3-2/part-0001
hdfs dfs -cat /user/admin/p3-2/part-0002
``` 
Se otuvieron los siguientes outputs: 
![image](./Imágenes/h.png)

#### 3.3
Usando el siguiente comando es posible obtener el día en que el se vieron menos películas, y la cantidad de películas vistas; los outputs serán almacenados en la carpeta p3-3 que está incluída en la carpeta admin del cluster:
```
python menosPel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-3
```
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-3/part-0000
hdfs dfs -cat /user/admin/p3-3/part-0001
hdfs dfs -cat /user/admin/p3-3/part-0002
``` 
Se otuvieron los siguientes outputs: 
![image](./Imágenes/i.png)

#### 3.4

Usando el siguiente comando es posible obtener los usuarios (representados por su ID) que vieron una sola película, así como el rating que le dieron; los outputs serán almacenados en la carpeta p3-4 que está incluída en la carpeta admin del cluster:
```
python singlePel.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-4
```
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-4/part-0000
hdfs dfs -cat /user/admin/p3-4/part-0001
hdfs dfs -cat /user/admin/p3-4/part-0002
``` 
Se otuvieron los siguientes outputs: 
![image](./Imágenes/j.png)

#### 3.5
Usando el siguiente comando es posible obtener el día con los peores ratings, así como el promedio de los ratings dados por el usuario; los outputs serán almacenados en la carpeta p3-5 que está incluída en la carpeta admin del cluster:
```
python peorProm.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-5
```
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-5/part-0000
hdfs dfs -cat /user/admin/p3-5/part-0001
hdfs dfs -cat /user/admin/p3-5/part-0002
``` 
Se otuvieron los siguientes outputs: 
![image](./Imágenes/k.png)

#### 3.6
Usando el siguiente comando es posible obtener el día con los mejores ratings, así como el promedio de los ratings dados por el usuario; los outputs serán almacenados en la carpeta p3-6 que está incluída en la carpeta admin del cluster:
```
python mejorProm.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-6
```
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-6/part-0000
hdfs dfs -cat /user/admin/p3-6/part-0001
hdfs dfs -cat /user/admin/p3-6/part-0002
``` 
Se otuvieron los siguientes outputs: 
![image](./Imágenes/l.png)

#### 3.7
Usando el siguiente comando es posible obtener la mejor y la peor película por cada género basado en sus ratings, representadas por su ID; los outputs serán almacenados en la carpeta p3-7 que está incluída en la carpeta admin del cluster:
```
python genero.py hdfs:///user/admin/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/admin/p3-7
```
 Es posible consultar el output a partir de los siguientes comandos:
```
hdfs dfs -cat /user/admin/p3-7/part-0000
hdfs dfs -cat /user/admin/p3-7/part-0001
hdfs dfs -cat /user/admin/p3-7/part-0002
``` 
Se otuvieron los siguientes outputs: 
![image](./Imágenes/m.png)

## Diagrama

https://drive.google.com/file/d/1A6KXFej3AU7aGagj35IUXBm0zq6Ir-ED/view?usp=sharing

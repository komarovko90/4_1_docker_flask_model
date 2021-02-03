# python-flask-docker
�������� ������ ����� "�������� �������� � �������"

ML: sklearn, pandas, numpy
API: flask
������: � kaggle - https://www.kaggle.com/alekseykonotop/car-price-train-data?select=car_price_08_11_2020_final.csv

������: ����������� ��������� ���� �� �� ����������(���� price). ���������

������������ ��������:
- brand (object) ����� ������
['MERCEDES', 'TOYOTA', 'MITSUBISHI', 'HONDA', 'NISSAN', 'BMW', 'AUDI', 'VOLVO', 'INFINITI', 'SKODA', 'VOLKSWAGEN', 'LEXUS', 'OPEL', 'PEUGEOT', 'MAZDA', 'FIAT', 'RENAULT', 'JAGUAR', 'SUZUKI', 'MINI', 'PORSCHE', 'SUBARU', 'CITROEN']
- model_name (object) ������ ������
- engineDisplacement (int) ����� ���������
- enginePower (int) �������� ���������
- fuelType (object) ��� �������
- mileage (int) ������
- modelDate (int) ��� ������ ������������ ������
- numberOfDoors (int) ���������� ������
- productionDate (int) ��� ������������ ������
- vehicleTransmission (object) ��� �����������
- vendor (object) ������ ������������� 
- ��� (object) �������� ��� ����� ���
- ������ (object) ��� ������� ����
- ���� (object) � ����� ������� ��������� ����
- auto_class (object) ����� ����
- price_segment (object) ������� ������� ����
- seller_type (object) �������� - �������, ���������
- section (object) ����� ��� �� ����
- color (object) ���� ����

������: RandomForestRegressor

### ��������� ����������� � ������� �����
������ � ����������� ���������� �� linux ubuntu.
```
$ git clone https://github.com/fimochka-sudo/GB_docker_flask_example.git
$ cd price_auto 

$ sudo docker build -t price_auto .
```

### ��������� ���������

����� ��� ����� ������� ������� �������� � ��������� ���� ������������� ������ (<your_local_path_to_pretrained_models> ����� �������� �� ������ ���� � ����� ��������)
```
$ sudo docker run -d -p 8180:8180 -v /home/konstantin/flask_server:/app/app/models price_auto
```
sudo service docker restart


docker run -d -p 8180:8180 price_auto

### �������� localhost:8180
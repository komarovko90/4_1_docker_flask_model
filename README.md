# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/alekseykonotop/car-price-train-data?select=car_price_08_11_2020_final.csv

Задача: предсказать стоимость авто по ее параметрам(поле price). Регрессия

Используемые признаки:
- brand (object) марка машины
['MERCEDES', 'TOYOTA', 'MITSUBISHI', 'HONDA', 'NISSAN', 'BMW', 'AUDI', 'VOLVO', 'INFINITI', 'SKODA', 'VOLKSWAGEN', 'LEXUS', 'OPEL', 'PEUGEOT', 'MAZDA', 'FIAT', 'RENAULT', 'JAGUAR', 'SUZUKI', 'MINI', 'PORSCHE', 'SUBARU', 'CITROEN']
- model_name (object) модель машины
- engineDisplacement (int) объем двигателя
- enginePower (int) мощность двигателя
- fuelType (object) тип топлива
- mileage (int) пробег
- modelDate (int) год начала производства модели
- numberOfDoors (int) количество дверей
- productionDate (int) год производства машины
- vehicleTransmission (object) тип трансмиссии
- vendor (object) страна производитель 
- ПТС (object) оригинал или копия ПТС
- Привод (object) тип привода авто
- Руль (object) с какой стороны находится руль
- auto_class (object) класс авто
- price_segment (object) ценовой сегмент авто
- seller_type (object) владелец - частник, коммерция
- section (object) новое или бу авто
- color (object) цвет авто

Модель: RandomForestRegressor: course_work_finish.ipynb.

### Клонируем репозиторий и создаем образ
Работа с контейнером опробована на linux ubuntu.
```
$ git clone https://github.com/komarovko90/4_1_docker_flask_model.git
$ cd 4_1_docker_flask_model
$ sudo docker build -t price_auto .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ sudo docker run -d -p 8180:8180 -v <your_local_path_to_pretrained_models>:/app/app/models price_auto
```

### Работаем с сервисом 0.0.0.0:8180
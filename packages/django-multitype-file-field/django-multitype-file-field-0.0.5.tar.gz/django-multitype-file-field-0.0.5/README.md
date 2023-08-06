[![PyPi](https://img.shields.io/pypi/v/django-multitype-file-field.svg)](https://pypi.python.org/pypi/django-multitype-file-field)
[![Build Status](https://travis-ci.org/Apkawa/django-multitype-file-field.svg?branch=master)](https://travis-ci.org/Apkawa/django-multitype-file-field)
[![Coverage Status](https://coveralls.io/repos/github/Apkawa/django-multitype-file-field/badge.svg)](https://coveralls.io/github/Apkawa/django-multitype-file-field)
[![codecov](https://codecov.io/gh/Apkawa/django-multitype-file-field/branch/master/graph/badge.svg)](https://codecov.io/gh/Apkawa/django-multitype-file-field)
[![Requirements Status](https://requires.io/github/Apkawa/django-multitype-file-field/requirements.svg?branch=master)](https://requires.io/github/Apkawa/django-multitype-file-field/requirements/?branch=master)
[![PyPi](https://img.shields.io/pypi/pyversions/django-multitype-file-field.svg)](https://pypi.python.org/pypi/django-multitype-file-field)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Project for merging different file types, as example easy thumbnail image and unpacking archive in one field

# Installation

```bash
pip install django-multitype-file-field

```

or from git

```bash
pip install -e git+https://github.com/Apkawa/django-multitype-file-field.git#egg=django-multitype-file-field
```

## Django and python version

| Python<br/>Django |        3.5         |      3.6           |      3.7           |       3.8          |
|:-----------------:|--------------------|--------------------|--------------------|--------------------|
| 1.8               |       :x:          |      :x:           |       :x:          |      :x:           |
| 1.11              | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |      :x:           |
| 2.2               | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| 3.0               |       :x:          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |


# Usage

## models.py

```python
from django.db import models

from multitype_file_field.fields import MultiTypeFileField

# as example, with easy_thumbnails
from easy_thumbnails.fields import ThumbnailerImageField


class FileModel(models.Model):
    file = MultiTypeFileField(upload_to='test_archive',
        fields={
            None: models.FileField, # Fallback
            'image/svg+xml': models.FileField, # high priority,
            'image': (
                ThumbnailerImageField, 
                dict(resize_source=dict(size=(100, 100), sharpen=True, crop='smart'))
                ), # tuple, Field and args
            
        }
    )
```
Usage:

```python
from tests.models import TestModel
from django.core.files.base import ContentFile
model = TestModel()
model.file # => <FieldFile: None>
model.file = ContentFile('', name='example.png')
model.file # => <ImageFieldFile: example.png>
model.file = ContentFile('', name='example.txt')
model.file # => <FieldFile: example.txt>

```

# Contributing

## run example app

```bash
pip install -r requirements.txt
./test/manage.py migrate
./test/manage.py runserver
```

## run tests

```bash
pip install -r requirements.txt
pytest
tox
```

## Update version

```bash
python setup.py bumpversion
```

## publish pypi

```bash
python setup.py publish
```




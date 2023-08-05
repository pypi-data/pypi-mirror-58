# HiPay PythonSDK

HiPay SDK for Python. HiPay is a payment gateway platform. For more info about this see the website https://developer.hipay.com.

### Install

```
pip install hipay-python-sdk
```

### Use

```
hipay_mb_service = HiPayMBService(username="****", password="****")
```

### Get MB Reference
Generate a MB reference with the amount provided.
```
mb_reference = self.hipay_mb_service.get_reference_mb(email="email@mal.com", amount=10)
```
**Note:** For more info check the documentation [here.](https://trello-attachments.s3.amazonaws.com/5d0795d0a145ea1c06ca85d9/5dc2e959c28e25755811551a/0254737f7fc7a9226130194c22a209ac/multibanco_payshop_ManualTecnico_2.5.pdf)


### Get Reference Info
Check status about the MB Payment reference. Useful if you want to check if the payment have been preformed.
```
reference_info = self.hipay_mb_service.get_info_reference(mb_reference["reference"])
```
**Note:** For more info check the documentation [here.](https://trello-attachments.s3.amazonaws.com/5d0795d0a145ea1c06ca85d9/5dc2e959c28e25755811551a/0254737f7fc7a9226130194c22a209ac/multibanco_payshop_ManualTecnico_2.5.pdf)

### Build and Publish

```
python setup.py sdist
twine upload dist/*
```

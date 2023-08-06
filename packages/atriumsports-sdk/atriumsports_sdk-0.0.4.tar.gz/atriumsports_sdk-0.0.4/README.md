# Atrium Sports API SDK

Python module to make use of the Atrium Sports Datacore API


```python
import atriumsports

atrium = AtriumSports({
    'sport': 'basketball',
    'credential_id': 'XXXXX',
    'credential_secret': 'YYYY',
    'organizations': ['b1e34'],
})
datacore = atrium.client('datacore')
response = datacore.get('/o/b1a23/competitions', limit=500)
for data in response.data():
    print(data)
```

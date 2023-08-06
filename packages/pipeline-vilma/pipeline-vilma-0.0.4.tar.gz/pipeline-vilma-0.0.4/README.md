# Pipeline Vilma

## Configuration

```python
options = {
    "messager": {
        "server": "192.168.0.202",
        "queues": {
            "provider-to-collector": "p2c",
            "collector-to-instancer": "c2i",
            "instancer-to-estimator": "i2e",
            "estimator-to-app": "e2a"
        }
    },
    "database": {
        "url": "mongodb://localhost:27017/multisensor",
        "name": "multisensor",
        "collections": {
            "collector": "collector"
        }
    }
}
```

## Provider

## Collector

## Instancer

## Messager

# django redis cluster client

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": [{"host": "127.0.0.1", "port": "7000"}],
        "OPTIONS": {
            "CLIENT_CLASS": "hypersRedisCluster.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
    }
}
```
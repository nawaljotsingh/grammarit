import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


class Database():
    
    reddis=None

    def __init__(self):
        self.reddis = self.get_db_connection()
    
    def get_db_connection(self):
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        return r
    
    def get_value(self,key):
        self.reddis.get(key)
    
    def set_value(self,key, val):
        self.reddis.set(key, val)

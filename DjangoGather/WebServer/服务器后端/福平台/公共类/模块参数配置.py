




AUTH_USER_MODEL = '福平台.system.Users'
USERNAME_FIELD = 'username'
ALL_MODELS_OBJECTS = []  # 所有app models 对象



 
# token 有效时间 时 分 秒
TOKEN_LIFETIME = 12 * 60 * 60
token有效时间 = 12 * 60 * 60

# TOKEN_LIFETIME = 50

# 接口白名单，不需要授权直接访问
WHITE_LIST = ['/api/system/userinfo', '/api/system/permCode', '/api/system/menu/route/tree', '/api/system/user/*',
              '/api/system/user/set/repassword']

# 接口日志记录
API_LOG_ENABLE = True
API_LOG_METHODS = ['POST', 'GET', 'DELETE', 'PUT']
API_MODEL_MAP = {}

# 初始化需要执行的列表，用来初始化后执行
INITIALIZE_RESET_LIST = []











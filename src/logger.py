import os
import logging 
from datetime import datetime

Log=f"{datetime.now().strftime('%d_%m_%y_%h_%m')}.log"
log_file=os.path.join(os.getcwd(),'Log_files',Log)
os.makedirs(log_file,exist_ok=True)
log_path=os.path.join(log_file,Log)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(message)s'
)

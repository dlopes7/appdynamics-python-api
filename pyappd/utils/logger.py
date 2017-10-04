import logging

LOG_LEVEL = logging.DEBUG
log = logging.getLogger('appdynamics-api')
log.setLevel(LOG_LEVEL)
lh = logging.StreamHandler()
lh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log.addHandler(lh)
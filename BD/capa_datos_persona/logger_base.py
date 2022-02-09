import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',  # date format
                handlers=[
                    log.FileHandler('capa_datos.log'),  # creates a file with the warnings
                    log.StreamHandler()
                ])


if __name__ == '__main__':
    log.debug('debug level message')
    log.info('info level message')
    log.warning('warning level message')
    log.error('error level message')
    log.critical('warning level message')

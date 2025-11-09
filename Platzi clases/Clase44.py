def log_transaction(func):
    def wrapper():
        print("Log de la transaccion...")
        func()
        print('Log terminado...')
    return wrapper

@log_transaction
def process_payment():
    print('processing payment')
    
process_payment()
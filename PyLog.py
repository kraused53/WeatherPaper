import datetime

def make_time_stamp() -> str:
    return datetime.datetime.now().strftime('%b %d, %Y @ %I:%M:%S %p')

def make_log( message:str, log_level: int ) -> None:
    tag = ""

    if log_level == 0:
        tag += "  LOG] "
    elif log_level == 1:
        tag += " WARN] "
    else:
        tag += "ERROR] "

    print( tag + f"<{make_time_stamp()}> - {message}" )

def log( message:str ) -> None:
    make_log( message, 0 )

def warn( message:str ) -> None:
    make_log( message, 1 )

def error( message:str ) -> None:
    make_log( message, 2 )

if __name__ == '__main__':
    make_log( "This is just information", 0 )
    make_log( "This is a warning", 1 )
    make_log( "This is an error", 2 )

    log( "This is just information" )
    warn( "This is a warning" )
    error( "This is an error" )
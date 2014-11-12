from OpenSSLBuilder import OpenSSLBuilder

def get_builder():
    return OpenSSLBuilder(get_default_config_opts())

def get_default_config_opts():
    try:
        import configure_opts
    except ImportError:
        return None
    else:
        return configure_opts.default_opts

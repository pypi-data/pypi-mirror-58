import traceback

def print_version():
    from pkg_resources import get_distribution, DistributionNotFound
    try:
        __version__ = get_distribution("glmfpackage").version
        print(__version__)
    except DistributionNotFound:
        # package is not installed
        print(traceback.format_exc())
        print("__ no version __")
    
if __name__ == "__main__":
    print_version()
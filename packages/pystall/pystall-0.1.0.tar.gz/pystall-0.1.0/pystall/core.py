"""Contains core functionality of Pystall.

This module contains core functionality of Pystall including:
    - Base Resource class
    - The included basic Resource subclasses
    - The build() method

Classes
-------
Resource: 
    Base class to be inherited from and extended to suit specific resource.

EXEResource(Resource):
    Used to download and install .exe files.

MSIResource(Resource):
    Used to download and install .msi files.

StaticResource(Resource):
    Used to download static files (images, videos etc.).

Methods
-------
build(*resources):
    Downloads and installs specified resources. 
    NOTE: Pass an arbitrary number of Resource instances (comma delimited)

Examples
--------
```
from pystall.core import EXEResource, MSIResource, StaticResource, build

python = EXEResource("python-installer", "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe")

go = MSIResource("Golang", "https://dl.google.com/go/go1.13.5.windows-amd64.msi")

logo = StaticResource("Wallpaper", ".png", "https://canadiancoding.ca/static/img/post-banners/python-post-banner.9bf19b390832.png")

build(python, go, logo)
```

"""



"""
Code maintenance
TODO
----
  * Logging
  * Error Catching

"""

# Standard lib dependencies
import os                           # Path validation and checking which OS script is being run on.
import logging                      # Used to grab logs from functions and classes

import subprocess                   # Used to install/run binaries once downloaded
from zipfile import ZipFile         # Used to extract files from .zip archives
from abc import ABC, abstractmethod # Used to enforce subclassing from base Resource class

# Third party dependencies
import requests                     # Used to download files from the web
from tqdm import tqdm               # Used to create installation/download progress bars


# Setting up default downloads folder based on OS
if os.name == "nt":
    DESKTOP = f"{os.getenv('USERPROFILE')}\Desktop"
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\Downloads"
else: # PORT: Assuming variable is there for MacOS and Linux installs
    DESKTOP = f"{os.getenv('HOMER')}/Desktop" #TODO: Verify this is the right directory
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads" #TODO: Verify this is the right directory

def show_logs():
    import sys
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))

class Resource(ABC):
    """Base class to be inherited from and extended to suit specific resource.

    Attributes
    ----------

    label : (str)
        Human readable name for resource and used with extension in files name.

    extensions : (str)
        The extension of the filetype being downloaded
    
    location : (str)
        The path or URL to the resource that needs to be downloaded & installed
    
    arguments : (list|bool)
        Specify any arguments to be passed on installation, False indicates no arguments.
    
    downloaded : (bool)
        Used to delineate if Resource is downloaded, if using local file set to True, else leave as False.

    Methods
    -------
    download:
        Downloads Resource from location specified in self.location of the instance

    install (abstract):
        Subclass implemented function for how to install/configure resource once downloaded.

    Examples
    --------
    Subclassing a static resource class to download static assets (images, videos etc.)
    ```
    class StaticResource(Resource):
        def __init__(self, label, extension, location, arguments = False, downloaded = False):
            super().__init__(label, extension, location, arguments, downloaded)

        def install(self):
            logging.info("No installation necessary for StaticResources")
            pass
    ```
    """
    def __init__(self, label, extension, location, arguments = False, downloaded = False):
        
        self.label = label
        self.extension = extension
        self.location = location
        self.arguments = arguments
        self.downloaded = downloaded

    def download(self, file_path = False):
        """Downloads Resource from location specified in self.location of the instance.

        Attributes
        ----------
        file_path : (str|bool)
            The path to where the resource should download to. 
            Leave as false for download folder + name + extension.
            NOTE: Custom paths MUST include extension.
        
        Examples
        --------
        ```
        python = EXEResource('python-installer', 'https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe')

        python.download() # Downloads python installer exe to OS downloads folder
        ```
        """
        logging.info(f"Downloading {self.label}")

        if not file_path:
            file_path = f"{DOWNLOAD_FOLDER}{os.sep}{self.label}{self.extension}"

        if os.path.exists(file_path): # If file already exists
            self.downloaded = True
            self.location = file_path
            return

        logging.info("Starting binary download")
        file_content = requests.get(self.location)
        open(file_path, 'wb').write(file_content.content) # Save file
        # TODO: Error catching
        self.downloaded = True
        self.location = file_path

    @abstractmethod
    def install(self) -> None:
        """installation steps after all necessary downloads are completed"""
        raise NotImplementedError


class EXEResource(Resource):
    """Used to download and install .exe files.

    Attributes
    ----------

    label : (str)
        Human readable name for resource and used with extension in files name.
    
    location : (str)
        The path or URL to the resource that needs to be downloaded & installed
    
    arguments : (list|bool)
        Specify any arguments to be passed on installation, False indicates no arguments.
    
    downloaded : (bool)
        Used to delineate if Resource is downloaded, if using local file set to True, else leave as False.
    
    remove: (bool)
        Whether to delete the .exe after installation, by default True.

    Methods
    -------
    download:
        Downloads Resource from location specified in self.location of the instance

    install:
        Runs the .exe file with specified arguments.
        NOTE: assumes you have already downloaded the file or set the self.location to correct file path.

    Examples
    --------
    ```
    from pystall.core import EXEResource, build

    python = EXEResource("python-installer", "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe")

    build(python) # Runs the download() and install() methods on the 'python' instance
    ```
    """
    def __init__(self, label, location, arguments = False, downloaded = False, remove = True):
        super().__init__(label, ".exe", location, arguments, downloaded)
        self.remove = remove

    def install(self):
        """Runs the .exe specified in self.location"""
        if self.downloaded:
            logging.info(f"Installing {self.label}")
            installer = subprocess.Popen(self.location)
        else:
            logging.error(f"{self.label} failed to install due to not being downloaded")

        while installer.poll() == None:
            """loop runs until process has terminated"""
        
        if self.remove:
            logging.info(f"Removing installer {self.label}")
            os.remove(self.location)


class MSIResource(Resource):
    """Used to download and install .msi files.

    Attributes
    ----------

    label : (str)
        Human readable name for resource and used with extension in files name.
    
    location : (str)
        The path or URL to the resource that needs to be downloaded & installed
    
    arguments : (list|bool)
        Specify any arguments to be passed on installation, False indicates no arguments.
    
    downloaded : (bool)
        Used to delineate if Resource is downloaded, if using local file set to True, else leave as False.

    remove: (bool)
        Whether to delete the .exe after installation, by default True.

    Methods
    -------
    download:
        Downloads Resource from location specified in self.location of the instance

    install:
        Runs the .msi file with specified arguments.
        NOTE: assumes you have already downloaded the file or set the self.location to correct file path.

    Examples
    --------
    ```
    from pystall.core import MSIResource, build

    go = MSIResource("Golang", "https://dl.google.com/go/go1.13.5.windows-amd64.msi")

    build(go) # Runs the download() and install() methods on the 'go' instance
    ```
    """
    def __init__(self, label, location, arguments = False, downloaded = False, remove = True):
        super().__init__(label, ".msi", location, arguments, downloaded)
        self.remove = remove

    def install(self):
        """Runs the .msi file with specified arguments."""
        if self.downloaded:
            logging.info(f"Installing {self.label}")
            installer = subprocess.Popen(self.location, shell=True)
        else:
            logging.error(f"{self.name} failed to install due to not being downloaded")

        while installer.poll() == None:
            """loop runs until process has terminated"""

        if self.remove:
            logging.info(f"Removing installer {self.label}")
            os.remove(self.location)


class StaticResource(Resource):
    """Used to download static files (images, videos etc.).

    Attributes
    ----------

    label : (str)
        Human readable name for resource and used with extension in files name.

    extensions : (str)
        The extension of the filetype being downloaded.
    
    location : (str)
        The path or URL to the resource that needs to be downloaded & installed
    
    arguments : (list|bool)
        Specify any arguments to be passed on installation, False indicates no arguments.
    
    downloaded : (bool)
        Used to delineate if Resource is downloaded, if using local file set to True, else leave as False.

    Methods
    -------
    download:
        Downloads Resource from location specified in self.location of the instance

    install:
        Does nothing since there are no installation/configuration steps for static files

    Examples
    --------
    ```
    from pystall.core import StaticResource, build

    wallpaper = StaticResource("Wallpaper", ".png", "https://images.unsplash.com/photo-1541599468348-e96984315921?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&h=500&q=60")

    wallpaper.download() # Since no install is necessary

    build(wallpaper) # Another option to download the Resource
    ```
    """
    def __init__(self, label, extension, location, arguments = False, downloaded = False):
        super().__init__(label, extension, location, arguments, downloaded)

    def install(self):
        """Does nothing since there are no installation/configuration steps for static files"""
        logging.info("No installation necessary for StaticResources")

class ZIPResource(Resource):
    """Used to download and extract .zip files.

    Attributes
    ----------

    label : (str)
        Human readable name for resource and used with extension in files name.
    
    location : (str)
        The path or URL to the resource that needs to be downloaded & installed
    
    arguments : (list|bool)
        Specify any arguments to be passed on installation, False indicates no arguments.
    
    downloaded : (bool)
        Used to delineate if Resource is downloaded, if using local file set to True, else leave as False.

    remove: (bool)
        Whether to delete the .zip after installation, by default True.

    Methods
    -------
    download:
        Downloads Resource from location specified in self.location of the instance

    install:
        Extracts the .zip file.
        NOTE: assumes you have already downloaded the file or set the self.location to correct file path.

    Examples
    --------
    ```
    from pystall.core import ZIPResource, build

    micro = ZIPResource("micro editor", "https://github.com/zyedidia/micro/releases/download/v1.4.1/micro-1.4.1-win64.zip")

    build(micro)
    ```
    """
    def __init__(self, label, location, arguments = False, downloaded = False, remove = True):
        super().__init__(label, ".zip", location, arguments, downloaded)
        self.remove = remove

    def extract(self):
        """Extracts the .zip file."""
        extract_path = self.location[:-3:]
        logging.info(f"Extracting Zip archive {self.location} to {extract_path}")
        with ZipFile(self.location, "r") as archive:
                archive.extractall(extract_path) # Strip extension and extract to folder

    def install(self):
        """Extracts the .zip file and runs necessary installation steps. NOTE: Not yet implemented"""
        if self.downloaded:
            logging.info(f"Installing {self.label}")
            self.extract()
            
        else:
            logging.error(f"{self.name} failed to install due to not being downloaded")

        if self.remove:
            logging.info(f"Removing installer {self.label}")
            os.remove(self.location)


def build(*resources):
    """downloads and installs everything specified"""
    for resource in resources:
        if not resource.downloaded:
            resource.download()
        resource.install()


if __name__ == "__main__": # Used to test out functionality while developing
    show_logs()
    
    micro = ZIPResource("micro editor", "https://github.com/zyedidia/micro/releases/download/v1.4.1/micro-1.4.1-win64.zip")
    
    python = EXEResource("python-installer", "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe")
    
    go = MSIResource("Golang", "https://dl.google.com/go/go1.13.5.windows-amd64.msi")
    
    wallpaper = StaticResource("Wallpaper", ".png", "https://images.unsplash.com/photo-1541599468348-e96984315921?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&h=500&q=60")
   
    # build(micro)

    # Need to test this more
    # path = f"C:\\Users\\Kieran\\Downloads\\micro editor\\micro-1.4.1"

    # subprocess.Popen(f'setx path "%path%;{path}"')
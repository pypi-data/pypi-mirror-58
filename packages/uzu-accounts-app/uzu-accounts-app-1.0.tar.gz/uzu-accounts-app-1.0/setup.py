from setuptools import setup, find_packages

setup(
    name = 'uzu-accounts-app',          
    packages = find_packages(),  
    version = '1.0',      
    license='MIT',        
    description = 'AccountsApp is a generic django application tailored to Single Page Applications that abstracts user authentication and verification from the rest of your project.',
    author = 'Collins C. Chinedu (Kolynes)',                   
    author_email = 'collinschinedu@uzucorp.com',      
    url = 'https://github.com/Kolynes/AccountsApp.git',   
    download_url = 'https://github.com/Kolynes/AccountsApp/archive/0.2.tar.gz',    
    keywords = ['Authentication', 'Django', 'Account Verification'],   
    classifiers=[
        'Development Status :: 3 - Alpha',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',      
        'Programming Language :: Python :: 3.6',
    ],
)
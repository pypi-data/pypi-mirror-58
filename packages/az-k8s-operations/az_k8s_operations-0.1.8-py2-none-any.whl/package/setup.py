import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="az_k8s_operations", # Replace with your own username
    version="0.1.8",
    author="1V14713",
    author_email="mathieu.gravil@gmail.com",
    description="Collection of scripts to maintains aks cluster." ,
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r').read(),
    use_2to3=True,
    url="https://aksterraformstate.z6.web.core.windows.net/az_k8s_operations/",
    packages=setuptools.find_packages(),
      install_requires=[            # I get to this in a second
          #'azure==4.0.0',
          #'azure-devops==5.1.0b6',
          #'azure-graphrbac==0.61.1',
          #'azure-keyvault-secrets==4.0.0',
          #'azure-identity==1.0.1',
          'requests>=2.22.0',
          'xlsxwriter>=1.2.1', 
          'datetime>=4.3',
          'sendgrid==6.1.0',
          'filetype==1.0.5'
          ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=2.7.17, >=3.5',
)
